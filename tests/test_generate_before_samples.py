"""Tests for the pure helpers in generate_before_samples.

Covers .env key parsing, frontmatter building, and sample writing. The
OpenRouter network call (call_openrouter) is not exercised here.
"""

from __future__ import annotations

import pytest

import generate_before_samples as mod

SAMPLE = mod.SAMPLES[0]


def test_load_api_key_reads_value(monkeypatch, tmp_path):
    env = tmp_path / ".env"
    env.write_text("OPENROUTER_API_KEY=sk-test-123\n", encoding="utf-8")
    monkeypatch.setattr(mod, "ENV_FILE", env)
    assert mod.load_api_key() == "sk-test-123"


def test_load_api_key_missing_file_exits(monkeypatch, tmp_path):
    monkeypatch.setattr(mod, "ENV_FILE", tmp_path / "absent.env")
    with pytest.raises(SystemExit):
        mod.load_api_key()


def test_load_api_key_absent_key_exits(monkeypatch, tmp_path):
    env = tmp_path / ".env"
    env.write_text("OTHER=1\n", encoding="utf-8")
    monkeypatch.setattr(mod, "ENV_FILE", env)
    with pytest.raises(SystemExit):
        mod.load_api_key()


def test_build_frontmatter_has_delimiters_and_fields():
    fm = mod.build_frontmatter(SAMPLE)
    assert fm.startswith("---\n")
    assert "stage: before" in fm
    assert f"format: {SAMPLE['format_label']}" in fm
    assert "system_prompt: none" in fm  # SAMPLES[0] has no system prompt


def test_save_sample_writes_file(monkeypatch, tmp_path):
    monkeypatch.setattr(mod, "SAMPLES_DIR", tmp_path / "before")
    out = mod.save_sample(SAMPLE, "body text")
    assert out.exists()
    content = out.read_text(encoding="utf-8")
    assert content.endswith("body text")
    assert content.startswith("---\n")
