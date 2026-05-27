#!/usr/bin/env python3
"""Resolve a person × style profile from config/profiles.toml.

Reads the active config (defaults to config/profiles.toml; falls back to
config/profiles.example.toml when the active file is missing), merges the
base defaults / person / style / cross-scoped overrides in that order, and
emits the resolved profile as JSON (default) or human-readable text.

Used by the seven reference-library agents to look up the active profile
at invocation time. Agents call this via the Bash tool:

    python3 {{LIBRARY_PATH}}/scripts/profile_resolver.py \\
        --person ariannah --style work-email --format json

Resolution rules:
    1. Layer order: base → person.<p> → style.<s> → overrides."<p>:<s>"
    2. Scalars: last writer wins.
    3. Lists: concatenate then dedupe (preserves order of first appearance).
    4. Tables: shallow-merged key by key.
    5. tier_3_overrides is person-scoped only (styles cannot override).
    6. legal_source is style-scoped only (persons cannot override).
    7. Domain gating: if a style declares required_domain and the resolved
       person does not list it in domains, exit with code 2 and an error.
    8. Missing person / style fall back to [defaults]. Missing defaults is a
       hard error (exit code 3).
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path
from typing import Any

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ModuleNotFoundError:
        sys.stderr.write(
            "error: this script needs Python 3.11+ (for tomllib) or the "
            "'tomli' package on older versions.\n"
        )
        sys.exit(4)


SCHEMA_VERSION = "2.0"

PERSON_ONLY_FIELDS = {
    "domains",
    "tier_3_overrides",
    "analogy_domains",
    "hedge_phrases",
    "ai_extensions",
    "calibration_source",
    "voice_attributes",
    "stylometry",
    "display_name",
}

STYLE_ONLY_FIELDS = {
    "legal_source",
    "required_domain",
    "palette",
    "formality",
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _default_config_paths() -> tuple[Path, Path]:
    root = _repo_root()
    return root / "config" / "profiles.toml", root / "config" / "profiles.example.toml"


def _load_config(explicit: str | None) -> tuple[dict[str, Any], Path]:
    if explicit:
        path = Path(explicit).resolve()
        if not path.exists():
            sys.stderr.write(f"error: config file not found: {path}\n")
            sys.exit(5)
        return _read_toml(path), path

    active, example = _default_config_paths()
    if active.exists():
        return _read_toml(active), active
    if example.exists():
        return _read_toml(example), example
    sys.stderr.write(
        f"error: no config file found. Looked for:\n  {active}\n  {example}\n"
        f"Run: cp {example} {active}\n"
    )
    sys.exit(5)


def _read_toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def _merge_lists(*lists: list[Any]) -> list[Any]:
    result: list[Any] = []
    seen: set[str] = set()
    for lst in lists:
        for item in lst:
            key = repr(item)
            if key not in seen:
                seen.add(key)
                result.append(item)
    return result


def _merge(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    """Shallow-merge overlay onto base. Lists concatenate-and-dedupe.

    Nested dicts merge one level deep (keys in overlay replace keys in base).
    """
    result: dict[str, Any] = {**base}
    for key, value in overlay.items():
        if key in result and isinstance(result[key], list) and isinstance(value, list):
            result[key] = _merge_lists(result[key], value)
        elif key in result and isinstance(result[key], dict) and isinstance(value, dict):
            merged = {**result[key]}
            for sub_key, sub_value in value.items():
                merged[sub_key] = sub_value
            result[key] = merged
        else:
            result[key] = value
    return result


def _split_scoped(
    section: dict[str, Any],
    person_only: set[str],
    style_only: set[str],
    source: str,
) -> dict[str, Any]:
    """Drop person-only fields from a style section (or vice versa)."""
    if source == "style":
        return {k: v for k, v in section.items() if k not in person_only}
    if source == "person":
        return {k: v for k, v in section.items() if k not in style_only}
    return dict(section)


def resolve(
    config: dict[str, Any],
    person_key: str | None,
    style_key: str | None,
) -> dict[str, Any]:
    defaults = config.get("defaults") or {}
    if not defaults:
        sys.stderr.write("error: config is missing a [defaults] section.\n")
        sys.exit(3)

    default_person = defaults.get("person")
    default_style = defaults.get("style")
    if not default_person or not default_style:
        sys.stderr.write(
            "error: [defaults] must declare both 'person' and 'style'.\n"
        )
        sys.exit(3)

    person_explicit = person_key is not None
    style_explicit = style_key is not None
    person_key = person_key or default_person
    style_key = style_key or default_style

    people = config.get("person") or {}
    styles = config.get("style") or {}
    overrides = config.get("overrides") or {}

    if person_key not in people:
        sys.stderr.write(
            f"error: person '{person_key}' is not defined. Known persons: "
            f"{sorted(people)}\n"
        )
        sys.exit(6)
    if style_key not in styles:
        sys.stderr.write(
            f"error: style '{style_key}' is not defined. Known styles: "
            f"{sorted(styles)}\n"
        )
        sys.exit(6)

    person = _split_scoped(people[person_key], PERSON_ONLY_FIELDS, STYLE_ONLY_FIELDS, "person")
    style = _split_scoped(styles[style_key], PERSON_ONLY_FIELDS, STYLE_ONLY_FIELDS, "style")

    required_domain = style.get("required_domain")
    person_domains = person.get("domains") or []
    if required_domain and required_domain not in person_domains:
        sys.stderr.write(
            f"error: DomainMismatch: person '{person_key}' cannot use style "
            f"'{style_key}' (requires domain '{required_domain}'; person has "
            f"{person_domains}).\n"
        )
        sys.exit(2)

    cross_key = f"{person_key}:{style_key}"
    cross = overrides.get(cross_key) or {}

    resolved_person = _merge({}, person)
    resolved_style = _merge({}, style)
    resolved_cross = _merge({}, cross)

    flat: dict[str, Any] = {
        "schema_version": config.get("schema_version", SCHEMA_VERSION),
        "person": {"key": person_key, **resolved_person},
        "style": {"key": style_key, **resolved_style},
        "tier_3_overrides": list(resolved_person.get("tier_3_overrides") or []),
        "meta": {
            "resolved_at": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "person_explicit": person_explicit,
            "style_explicit": style_explicit,
            "default_person": default_person,
            "default_style": default_style,
            "cross_override_applied": bool(cross),
        },
    }

    if resolved_cross:
        for key, value in resolved_cross.items():
            if key in PERSON_ONLY_FIELDS or key in {"voice_attributes", "stylometry"}:
                flat["person"][key] = value
            elif key in STYLE_ONLY_FIELDS:
                flat["style"][key] = value
            else:
                flat[key] = value

    # Re-sync the top-level tier_3_overrides convenience field after any cross
    # override that touched person.tier_3_overrides. Agents read either location
    # depending on context; they must agree.
    flat["tier_3_overrides"] = list(flat["person"].get("tier_3_overrides") or [])

    return flat


def _format_text(profile: dict[str, Any]) -> str:
    lines: list[str] = []
    person = profile["person"]
    style = profile["style"]
    meta = profile["meta"]
    lines.append("Resolved profile")
    lines.append("================")
    lines.append(f"  person:               {person['key']} ({person.get('display_name', '(unnamed)')})")
    lines.append(f"  style:                {style['key']}")
    lines.append(f"  palette:              {style.get('palette', '(none)')}")
    lines.append(f"  formality:            {style.get('formality', '(none)')}")
    lines.append(f"  legal_source:         {style.get('legal_source', 'none')}")
    lines.append(f"  domains:              {', '.join(person.get('domains') or []) or '(none)'}")
    lines.append(f"  tier_3_overrides:     {', '.join(profile.get('tier_3_overrides') or []) or '(none)'}")
    lines.append(f"  hedge_phrases:        {', '.join(person.get('hedge_phrases') or []) or '(none)'}")
    lines.append(f"  analogy_domains:      {', '.join(person.get('analogy_domains') or []) or '(none)'}")
    lines.append(f"  ai_extensions:        {', '.join(person.get('ai_extensions') or []) or '(none)'}")
    lines.append(f"  calibration_source:   {person.get('calibration_source') or '(none)'}")
    stylometry = person.get("stylometry") or {}
    if stylometry:
        lines.append("  stylometry:")
        for key, value in stylometry.items():
            lines.append(f"    {key:<28}{value}")
    voice = person.get("voice_attributes") or {}
    if voice:
        lines.append("  voice_attributes:")
        for key, value in voice.items():
            lines.append(f"    {key:<28}{value}")
    lines.append("")
    lines.append("Resolution metadata")
    lines.append("-------------------")
    for key, value in meta.items():
        lines.append(f"  {key:<28}{value}")
    return "\n".join(lines) + "\n"


def _list_inventory(config: dict[str, Any]) -> str:
    people = sorted((config.get("person") or {}).keys())
    styles = sorted((config.get("style") or {}).keys())
    defaults = config.get("defaults") or {}
    lines = [
        "Available profiles",
        "==================",
        f"  default person: {defaults.get('person', '(none)')}",
        f"  default style:  {defaults.get('style', '(none)')}",
        "",
        "  persons: " + (", ".join(people) if people else "(none)"),
        "  styles:  " + (", ".join(styles) if styles else "(none)"),
        "",
    ]
    overrides = config.get("overrides") or {}
    if overrides:
        lines.append("  cross-scoped overrides:")
        for key in sorted(overrides):
            lines.append(f"    - {key}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Resolve a person × style profile for reference-library agents.",
    )
    parser.add_argument("--person", help="Person key (default: from [defaults].person)")
    parser.add_argument("--style", help="Style key (default: from [defaults].style)")
    parser.add_argument(
        "--config",
        help="Path to a profiles.toml file. Defaults to config/profiles.toml, "
        "falling back to config/profiles.example.toml.",
    )
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="Output format (default: json).",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available persons and styles instead of resolving.",
    )
    args = parser.parse_args(argv)

    config, config_path = _load_config(args.config)

    if args.list:
        sys.stdout.write(_list_inventory(config))
        return 0

    profile = resolve(config, args.person, args.style)
    profile["meta"]["config_source"] = str(config_path)

    if args.format == "json":
        json.dump(profile, sys.stdout, indent=2, sort_keys=False)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(_format_text(profile))
    return 0


if __name__ == "__main__":
    sys.exit(main())
