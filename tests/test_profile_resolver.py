"""Tests for scripts/profile_resolver.py.

Covers the merge logic, domain gating, error paths, and CLI entry point.
Run with: pytest tests/test_profile_resolver.py
"""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

import pytest

import profile_resolver as pr

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def minimal_config() -> dict:
    """A small but complete config exercising most resolver paths."""
    return {
        "schema_version": "2.0",
        "defaults": {"person": "alice", "style": "email"},
        "person": {
            "alice": {
                "display_name": "Alice",
                "domains": ["personal", "legal:oregon"],
                "tier_3_overrides": ["no-em-dash"],
                "hedge_phrases": ["typically"],
                "analogy_domains": ["libraries"],
                "ai_extensions": [],
                "calibration_source": "writing-style/style-profile.md",
                "voice_attributes": {"tone": "warm"},
                "stylometry": {"ttr_min": 0.4},
            },
            "bob": {
                "display_name": "Bob",
                "domains": ["personal"],
                "tier_3_overrides": [],
            },
        },
        "style": {
            "email": {
                "palette": "Warm/Conversational",
                "formality": 3,
                "legal_source": "none",
            },
            "brief": {
                "palette": "Formal/Scholarly",
                "formality": 5,
                "legal_source": "appellate-style-manual",
                "required_domain": "legal:oregon",
            },
        },
        "overrides": {
            "alice:email": {"hedge_density": [0.03, 0.07]},
        },
    }


@pytest.fixture
def config_file(tmp_path: Path, minimal_config: dict) -> Path:
    """Write minimal_config to a real TOML file and return the path."""
    body = (
        textwrap.dedent(
            """
        schema_version = "2.0"

        [defaults]
        person = "alice"
        style  = "email"

        [person.alice]
        display_name       = "Alice"
        domains            = ["personal", "legal:oregon"]
        tier_3_overrides   = ["no-em-dash"]
        hedge_phrases      = ["typically"]
        analogy_domains    = ["libraries"]
        ai_extensions      = []
        calibration_source = "writing-style/style-profile.md"

          [person.alice.voice_attributes]
          tone = "warm"

          [person.alice.stylometry]
          ttr_min = 0.4

        [person.bob]
        display_name     = "Bob"
        domains          = ["personal"]
        tier_3_overrides = []

        [style.email]
        palette      = "Warm/Conversational"
        formality    = 3
        legal_source = "none"

        [style.brief]
        palette         = "Formal/Scholarly"
        formality       = 5
        legal_source    = "appellate-style-manual"
        required_domain = "legal:oregon"

        [overrides."alice:email"]
        hedge_density = [0.03, 0.07]
        """
        ).strip()
        + "\n"
    )
    target = tmp_path / "profiles.toml"
    target.write_text(body, encoding="utf-8")
    return target


# ---------------------------------------------------------------------------
# Pure helpers
# ---------------------------------------------------------------------------


class TestMergeLists:
    def test_concatenates_and_dedupes(self):
        result = pr._merge_lists(["a", "b"], ["b", "c"])
        assert result == ["a", "b", "c"]

    def test_preserves_first_occurrence_order(self):
        result = pr._merge_lists(["x", "y"], ["y", "x", "z"])
        assert result == ["x", "y", "z"]

    def test_empty_lists(self):
        assert pr._merge_lists([], []) == []

    def test_handles_nested_dicts(self):
        result = pr._merge_lists([{"a": 1}], [{"a": 1}, {"b": 2}])
        assert result == [{"a": 1}, {"b": 2}]


class TestMerge:
    def test_scalar_overlay_wins(self):
        base = {"x": 1, "y": 2}
        overlay = {"y": 99}
        assert pr._merge(base, overlay) == {"x": 1, "y": 99}

    def test_lists_concatenate_dedupe(self):
        base = {"items": ["a", "b"]}
        overlay = {"items": ["b", "c"]}
        assert pr._merge(base, overlay) == {"items": ["a", "b", "c"]}

    def test_nested_dict_shallow_merges(self):
        base = {"voice": {"tone": "warm", "precision": "high"}}
        overlay = {"voice": {"tone": "formal"}}
        result = pr._merge(base, overlay)
        assert result == {"voice": {"tone": "formal", "precision": "high"}}

    def test_overlay_adds_new_keys(self):
        assert pr._merge({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}

    def test_does_not_mutate_inputs(self):
        base = {"x": [1, 2]}
        overlay = {"x": [3]}
        pr._merge(base, overlay)
        assert base == {"x": [1, 2]}
        assert overlay == {"x": [3]}


class TestSplitScoped:
    def test_style_section_drops_person_only_fields(self):
        section = {"palette": "Warm", "domains": ["personal"]}
        result = pr._split_scoped(section, {"domains"}, {"palette"}, "style")
        assert "domains" not in result
        assert "palette" in result

    def test_person_section_drops_style_only_fields(self):
        section = {"domains": ["personal"], "legal_source": "none"}
        result = pr._split_scoped(section, {"domains"}, {"legal_source"}, "person")
        assert "domains" in result
        assert "legal_source" not in result

    def test_unknown_source_raises(self):
        # A typo in source must not silently bypass the scope enforcement
        # that _split_scoped exists to apply. Unknown values raise.
        with pytest.raises(ValueError, match=r"must be 'person' or 'style'"):
            pr._split_scoped({"a": 1}, set(), set(), "other")


# ---------------------------------------------------------------------------
# Core resolve()
# ---------------------------------------------------------------------------


class TestResolve:
    def test_uses_defaults_when_keys_omitted(self, minimal_config):
        profile = pr.resolve(minimal_config, None, None)
        assert profile["person"]["key"] == "alice"
        assert profile["style"]["key"] == "email"
        assert profile["meta"]["person_explicit"] is False
        assert profile["meta"]["style_explicit"] is False

    def test_explicit_keys_marked_explicit(self, minimal_config):
        profile = pr.resolve(minimal_config, "bob", "email")
        assert profile["person"]["key"] == "bob"
        assert profile["meta"]["person_explicit"] is True
        assert profile["meta"]["style_explicit"] is True

    def test_tier_3_overrides_flow_through(self, minimal_config):
        profile = pr.resolve(minimal_config, "alice", "email")
        assert profile["tier_3_overrides"] == ["no-em-dash"]

    def test_tier_3_overrides_empty_when_person_omits(self, minimal_config):
        profile = pr.resolve(minimal_config, "bob", "email")
        assert profile["tier_3_overrides"] == []

    def test_cross_override_applies(self, minimal_config):
        profile = pr.resolve(minimal_config, "alice", "email")
        # hedge_density is not in PERSON_ONLY or STYLE_ONLY, so it goes top-level
        assert profile.get("hedge_density") == [0.03, 0.07]
        assert profile["meta"]["cross_override_applied"] is True

    def test_no_cross_override_when_pair_absent(self, minimal_config):
        profile = pr.resolve(minimal_config, "bob", "email")
        assert profile["meta"]["cross_override_applied"] is False

    def test_cross_override_extends_tier_3_overrides(self, minimal_config):
        # Cross overrides honor concat-dedupe per rule 3 of the docstring.
        # A cross-level tier_3_overrides list ADDS to the person's list.
        minimal_config["overrides"]["alice:email"]["tier_3_overrides"] = ["no-oxford"]
        profile = pr.resolve(minimal_config, "alice", "email")
        assert profile["tier_3_overrides"] == ["no-em-dash", "no-oxford"]
        assert profile["person"]["tier_3_overrides"] == ["no-em-dash", "no-oxford"]

    def test_cross_override_routes_style_only_field(self, minimal_config):
        # A cross-level palette (STYLE_ONLY) lands in flat["style"], not "person".
        minimal_config["overrides"]["alice:email"]["palette"] = "Formal/Scholarly"
        profile = pr.resolve(minimal_config, "alice", "email")
        assert profile["style"]["palette"] == "Formal/Scholarly"
        assert "palette" not in profile["person"]

    def test_cross_override_shallow_merges_voice_attributes(self, minimal_config):
        # voice_attributes is a PERSON_ONLY table; a cross override merges
        # key-by-key per rule 4 (existing keys not in the override survive).
        minimal_config["overrides"]["alice:email"]["voice_attributes"] = {
            "precision": "high",
        }
        profile = pr.resolve(minimal_config, "alice", "email")
        assert profile["person"]["voice_attributes"] == {
            "tone": "warm",  # preserved from person.alice
            "precision": "high",  # added by cross override
        }

    def test_cross_override_with_only_tier_3_overrides(self):
        # Isolated scenario: a cross block whose only key is tier_3_overrides.
        config = {
            "schema_version": "2.0",
            "defaults": {"person": "p", "style": "s"},
            "person": {"p": {"domains": ["x"], "tier_3_overrides": ["a"]}},
            "style": {"s": {"palette": "Warm/Conversational"}},
            "overrides": {"p:s": {"tier_3_overrides": ["b"]}},
        }
        profile = pr.resolve(config, "p", "s")
        assert profile["tier_3_overrides"] == ["a", "b"]
        assert profile["meta"]["cross_override_applied"] is True

    def test_domain_mismatch_exits_7(self, minimal_config, capsys):
        with pytest.raises(SystemExit) as exc_info:
            pr.resolve(minimal_config, "bob", "brief")
        assert exc_info.value.code == 7
        captured = capsys.readouterr()
        assert "DomainMismatch" in captured.err
        assert "legal:oregon" in captured.err

    def test_unknown_person_exits_6(self, minimal_config, capsys):
        with pytest.raises(SystemExit) as exc_info:
            pr.resolve(minimal_config, "ghost", "email")
        assert exc_info.value.code == 6
        assert "ghost" in capsys.readouterr().err

    def test_unknown_style_exits_6(self, minimal_config, capsys):
        with pytest.raises(SystemExit) as exc_info:
            pr.resolve(minimal_config, "alice", "nonexistent")
        assert exc_info.value.code == 6
        assert "nonexistent" in capsys.readouterr().err

    def test_missing_defaults_section_exits_3(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            pr.resolve({}, None, None)
        assert exc_info.value.code == 3
        assert "defaults" in capsys.readouterr().err

    def test_defaults_missing_person_or_style_exits_3(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            pr.resolve({"defaults": {"person": "alice"}}, None, None)
        assert exc_info.value.code == 3

    def test_required_domain_satisfied_resolves(self, minimal_config):
        profile = pr.resolve(minimal_config, "alice", "brief")
        assert profile["style"]["legal_source"] == "appellate-style-manual"

    def test_person_only_fields_not_polluted_by_style(self, minimal_config):
        # voice_attributes is person-scoped; make sure style sections can't bleed in.
        minimal_config["style"]["email"]["voice_attributes"] = {"tone": "EVIL"}
        profile = pr.resolve(minimal_config, "alice", "email")
        assert profile["person"]["voice_attributes"]["tone"] == "warm"


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------


class TestLoadConfig:
    def test_explicit_path_loads(self, config_file):
        config, path = pr._load_config(str(config_file))
        assert config["defaults"]["person"] == "alice"
        assert path == config_file.resolve()

    def test_explicit_path_missing_exits_5(self, tmp_path, capsys):
        with pytest.raises(SystemExit) as exc_info:
            pr._load_config(str(tmp_path / "nope.toml"))
        assert exc_info.value.code == 5
        assert "not found" in capsys.readouterr().err

    def test_falls_back_to_example_when_active_missing(
        self, monkeypatch, tmp_path, config_file
    ):
        # Simulate: no active profiles.toml, but profiles.example.toml exists.
        example = tmp_path / "config" / "profiles.example.toml"
        example.parent.mkdir(parents=True)
        example.write_text(config_file.read_text())
        active = tmp_path / "config" / "profiles.toml"  # does not exist
        monkeypatch.setattr(pr, "_default_config_paths", lambda: (active, example))

        config, path = pr._load_config(None)
        assert config["defaults"]["person"] == "alice"
        assert path == example

    def test_prefers_active_over_example(self, monkeypatch, tmp_path, config_file):
        active = tmp_path / "active.toml"
        active.write_text(config_file.read_text())
        example = tmp_path / "example.toml"
        example.write_text(
            'schema_version = "2.0"\n[defaults]\nperson = "OTHER"\nstyle = "OTHER"\n'
        )
        monkeypatch.setattr(pr, "_default_config_paths", lambda: (active, example))

        config, path = pr._load_config(None)
        assert config["defaults"]["person"] == "alice"
        assert path == active

    def test_no_config_found_exits_5(self, monkeypatch, tmp_path, capsys):
        active = tmp_path / "a.toml"
        example = tmp_path / "b.toml"
        monkeypatch.setattr(pr, "_default_config_paths", lambda: (active, example))
        with pytest.raises(SystemExit) as exc_info:
            pr._load_config(None)
        assert exc_info.value.code == 5


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------


class TestFormatText:
    def test_includes_key_fields(self, minimal_config):
        profile = pr.resolve(minimal_config, "alice", "email")
        text = pr._format_text(profile)
        assert "alice" in text
        assert "Alice" in text
        assert "Warm/Conversational" in text
        assert "no-em-dash" in text
        assert "Resolution metadata" in text


class TestListInventory:
    def test_lists_persons_styles_and_defaults(self, minimal_config):
        text = pr._list_inventory(minimal_config)
        assert "alice" in text
        assert "bob" in text
        assert "email" in text
        assert "brief" in text
        assert "alice:email" in text

    def test_handles_empty_config(self):
        text = pr._list_inventory({})
        assert "persons" in text
        assert "styles" in text


# ---------------------------------------------------------------------------
# CLI entry
# ---------------------------------------------------------------------------


class TestMain:
    # main() returns None on success; non-success paths call sys.exit()
    # with a documented exit code. The contract is "no SystemExit means
    # success," not a return value check.

    def test_default_invocation_emits_json(self, config_file, capsys):
        pr.main(["--config", str(config_file)])
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["person"]["key"] == "alice"
        assert data["meta"]["config_source"] == str(config_file)

    def test_text_format(self, config_file, capsys):
        pr.main(["--config", str(config_file), "--format", "text"])
        assert "Resolved profile" in capsys.readouterr().out

    def test_list_flag(self, config_file, capsys):
        pr.main(["--config", str(config_file), "--list"])
        out = capsys.readouterr().out
        assert "alice" in out
        assert "bob" in out

    def test_explicit_person_and_style(self, config_file, capsys):
        pr.main(["--config", str(config_file), "--person", "bob", "--style", "email"])
        data = json.loads(capsys.readouterr().out)
        assert data["person"]["key"] == "bob"

    def test_domain_mismatch_propagates_exit_7(self, config_file):
        with pytest.raises(SystemExit) as exc_info:
            pr.main(
                ["--config", str(config_file), "--person", "bob", "--style", "brief"]
            )
        assert exc_info.value.code == 7

    def test_malformed_toml_exits_5(self, tmp_path, capsys):
        bad = tmp_path / "bad.toml"
        bad.write_text("this is not valid TOML = = =\n")
        with pytest.raises(SystemExit) as exc_info:
            pr._load_config(str(bad))
        assert exc_info.value.code == 5
        assert "malformed" in capsys.readouterr().err.lower()

    def test_shipped_example_config_resolves(self):
        """End-to-end check against the real shipped example file."""
        repo_root = Path(__file__).resolve().parent.parent
        example = repo_root / "config" / "profiles.example.toml"
        config, _ = pr._load_config(str(example))
        profile = pr.resolve(config, None, None)
        assert profile["person"]["key"] == "default"
        assert "no-em-dash" in profile["tier_3_overrides"]
