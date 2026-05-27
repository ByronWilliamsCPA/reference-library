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
    1. Layer order: base -> person.<p> -> style.<s> -> overrides."<p>:<s>".
       The --person and --style CLI flags SELECT which layers apply; they
       are not themselves an additional override layer.
    2. Scalars: last writer wins.
    3. Lists: concatenate then dedupe (preserves order of first appearance).
    4. Tables: shallow-merged key by key.
    5. tier_3_overrides is person-scoped only (styles cannot override).
    6. legal_source is style-scoped only (persons cannot override).
    7. Domain gating runs against the person's resolved domains BEFORE any
       cross-scoped overrides apply. Cross overrides cannot grant domain
       access; that protects the gate from being silently bypassed.
    8. Missing person / style fall back to [defaults]. Missing defaults is a
       hard error (exit code 3).

Exit codes:
    0  success
    2  argparse usage error (invalid CLI args; argparse default)
    3  config missing required [defaults] section or keys
    4  tomllib/tomli not available (pre-3.11 Python without tomli)
    5  config file not found, malformed, or unreadable
    6  unknown person or style key
    7  DomainMismatch: style requires a domain the person does not have
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

# Rendered in formatted output when a field is unset. Centralized so the
# placeholder string lives in exactly one place (resolves python:S1192).
_NONE_PLACEHOLDER = "(none)"

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


# #CRITICAL: TOML files read here are external resources. Malformed input
# or filesystem failures must produce a documented exit code (5), not a raw
# Python traceback that breaks the agent's exit-code contract.
# #VERIFY: every except branch ends in sys.exit(5).
def _read_toml(path: Path) -> dict[str, Any]:
    try:
        with path.open("rb") as handle:
            return tomllib.load(handle)
    except tomllib.TOMLDecodeError as exc:
        sys.stderr.write(f"error: malformed TOML in {path}: {exc}\n")
        sys.exit(5)
    except OSError as exc:
        sys.stderr.write(f"error: cannot read {path}: {exc}\n")
        sys.exit(5)


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
        elif (
            key in result and isinstance(result[key], dict) and isinstance(value, dict)
        ):
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
    """Drop person-only fields from a style section (or vice versa).

    `source` must be "person" or "style"; any other value raises
    ValueError. The previous silent passthrough was a foot-gun: a typo
    bypassed the scope enforcement that this function exists to apply.
    """
    if source == "style":
        return {k: v for k, v in section.items() if k not in person_only}
    if source == "person":
        return {k: v for k, v in section.items() if k not in style_only}
    raise ValueError(f"source must be 'person' or 'style', got {source!r}")


def _resolve_defaults(config: dict[str, Any]) -> tuple[str, str]:
    """Validate the [defaults] block and return (default_person, default_style)."""
    defaults = config.get("defaults") or {}
    if not defaults:
        sys.stderr.write("error: config is missing a [defaults] section.\n")
        sys.exit(3)
    default_person = defaults.get("person")
    default_style = defaults.get("style")
    if not default_person or not default_style:
        sys.stderr.write("error: [defaults] must declare both 'person' and 'style'.\n")
        sys.exit(3)
    return default_person, default_style


def _require_key(label: str, key: str, known: dict[str, Any]) -> None:
    """Exit 6 if `key` is not in `known`."""
    if key in known:
        return
    sys.stderr.write(
        f"error: {label} '{key}' is not defined. Known {label}s: {sorted(known)}\n"
    )
    sys.exit(6)


def _check_domain_gate(
    person_key: str,
    person: dict[str, Any],
    style_key: str,
    style: dict[str, Any],
) -> None:
    """Exit 7 if the style's required_domain is not in the person's domains.

    Runs against the base person record only. Cross overrides cannot grant
    access to a domain the person does not have; see rule 7 in the module
    docstring.
    """
    required_domain = style.get("required_domain")
    person_domains = person.get("domains") or []
    if not required_domain or required_domain in person_domains:
        return
    sys.stderr.write(
        f"error: DomainMismatch: person '{person_key}' cannot use style "
        f"'{style_key}' (requires domain '{required_domain}'; person has "
        f"{person_domains}).\n"
    )
    sys.exit(7)


def _route_cross_overrides(
    cross: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Partition cross-override keys by scope (person, style, other).

    PERSON_ONLY_FIELDS already includes voice_attributes and stylometry, so
    only one membership check is needed.
    """
    # #ASSUME: cross-override keys are strings; TOML guarantees this.
    person_overlay: dict[str, Any] = {}
    style_overlay: dict[str, Any] = {}
    other_overlay: dict[str, Any] = {}
    for key, value in cross.items():
        if key in PERSON_ONLY_FIELDS:
            person_overlay[key] = value
        elif key in STYLE_ONLY_FIELDS:
            style_overlay[key] = value
        else:
            other_overlay[key] = value
    return person_overlay, style_overlay, other_overlay


def _apply_cross_overrides(
    flat: dict[str, Any], cross: dict[str, Any]
) -> dict[str, Any]:
    """Merge a cross-override block into the resolved profile.

    Honors the same merge rules as the other layers (rule 3: lists
    concat-dedupe; rule 4: tables shallow-merge; scalars replace).
    """
    if not cross:
        return flat
    person_overlay, style_overlay, other_overlay = _route_cross_overrides(cross)
    if person_overlay:
        flat["person"] = _merge(flat["person"], person_overlay)
    if style_overlay:
        flat["style"] = _merge(flat["style"], style_overlay)
    if other_overlay:
        flat = _merge(flat, other_overlay)
    return flat


def resolve(
    config: dict[str, Any],
    person_key: str | None,
    style_key: str | None,
) -> dict[str, Any]:
    # #CRITICAL: this function is the public resolution contract. Every exit
    # code (3, 6, 7) emitted here is documented in the module docstring and
    # consumed by agents that branch on the return code.
    default_person, default_style = _resolve_defaults(config)

    person_explicit = person_key is not None
    style_explicit = style_key is not None
    person_key = person_key or default_person
    style_key = style_key or default_style

    people = config.get("person") or {}
    styles = config.get("style") or {}
    overrides = config.get("overrides") or {}

    _require_key("person", person_key, people)
    _require_key("style", style_key, styles)

    person = _split_scoped(
        people[person_key], PERSON_ONLY_FIELDS, STYLE_ONLY_FIELDS, "person"
    )
    style = _split_scoped(
        styles[style_key], PERSON_ONLY_FIELDS, STYLE_ONLY_FIELDS, "style"
    )

    _check_domain_gate(person_key, person, style_key, style)

    cross_key = f"{person_key}:{style_key}"
    cross = overrides.get(cross_key) or {}
    resolved_at = _dt.datetime.now(_dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    flat: dict[str, Any] = {
        "schema_version": config.get("schema_version", SCHEMA_VERSION),
        "person": {"key": person_key, **person},
        "style": {"key": style_key, **style},
        "tier_3_overrides": list(person.get("tier_3_overrides") or []),
        "meta": {
            "resolved_at": resolved_at,
            "person_explicit": person_explicit,
            "style_explicit": style_explicit,
            "default_person": default_person,
            "default_style": default_style,
            "cross_override_applied": bool(cross),
        },
    }

    flat = _apply_cross_overrides(flat, cross)

    # Re-sync the top-level tier_3_overrides convenience field after any
    # cross override that touched person.tier_3_overrides. Agents read
    # either location depending on context; they must agree.
    flat["tier_3_overrides"] = list(flat["person"].get("tier_3_overrides") or [])

    return flat


def _scalar_line(label: str, value: Any, fallback: str = _NONE_PLACEHOLDER) -> str:
    """Render a single scalar field as a left-aligned label/value line."""
    rendered = value if value not in (None, "", []) else fallback
    return f"  {label:<22}{rendered}"


def _list_line(label: str, values: list[Any] | None) -> str:
    """Render a list field as a comma-joined value line."""
    joined = ", ".join(values) if values else ""
    return _scalar_line(label, joined)


def _format_table_block(label: str, table: dict[str, Any]) -> list[str]:
    """Format a nested table (e.g., stylometry, voice_attributes) as lines.

    Returns an empty list when the table is empty so the caller can skip
    the header.
    """
    if not table:
        return []
    out = [f"  {label}:"]
    for key, value in table.items():
        out.append(f"    {key:<28}{value}")
    return out


def _format_summary(profile: dict[str, Any]) -> list[str]:
    """Build the scalar summary section of the formatted profile."""
    person = profile["person"]
    style = profile["style"]
    display = person.get("display_name", "(unnamed)")
    return [
        "Resolved profile",
        "================",
        f"  person:               {person['key']} ({display})",
        f"  style:                {style['key']}",
        _scalar_line("palette:", style.get("palette")),
        _scalar_line("formality:", style.get("formality")),
        _scalar_line("legal_source:", style.get("legal_source"), fallback="none"),
        _list_line("domains:", person.get("domains")),
        _list_line("tier_3_overrides:", profile.get("tier_3_overrides")),
        _list_line("hedge_phrases:", person.get("hedge_phrases")),
        _list_line("analogy_domains:", person.get("analogy_domains")),
        _list_line("ai_extensions:", person.get("ai_extensions")),
        _scalar_line("calibration_source:", person.get("calibration_source")),
    ]


def _format_text(profile: dict[str, Any]) -> str:
    person = profile["person"]
    meta = profile["meta"]
    lines: list[str] = _format_summary(profile)
    lines.extend(_format_table_block("stylometry", person.get("stylometry") or {}))
    lines.extend(
        _format_table_block("voice_attributes", person.get("voice_attributes") or {})
    )
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
        f"  default person: {defaults.get('person', _NONE_PLACEHOLDER)}",
        f"  default style:  {defaults.get('style', _NONE_PLACEHOLDER)}",
        "",
        "  persons: " + (", ".join(people) if people else _NONE_PLACEHOLDER),
        "  styles:  " + (", ".join(styles) if styles else _NONE_PLACEHOLDER),
        "",
    ]
    overrides = config.get("overrides") or {}
    if overrides:
        lines.append("  cross-scoped overrides:")
        for key in sorted(overrides):
            lines.append(f"    - {key}")
    return "\n".join(lines) + "\n"


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Resolve a person x style profile for reference-library agents.",
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
    return parser


def main(argv: list[str] | None = None) -> None:
    """CLI entry point. Either writes output and returns, or calls sys.exit().

    Successful completion falls through to a natural process exit (code 0).
    Error paths inside resolve() / _load_config() call sys.exit() directly
    with the documented exit code.
    """
    args = _build_arg_parser().parse_args(argv)
    config, config_path = _load_config(args.config)

    if args.list:
        sys.stdout.write(_list_inventory(config))
        return

    profile = resolve(config, args.person, args.style)
    profile["meta"]["config_source"] = str(config_path)

    if args.format == "json":
        json.dump(profile, sys.stdout, indent=2, sort_keys=False)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(_format_text(profile))


if __name__ == "__main__":
    main()
