"""Tests for the source-PDF integrity-check helpers in extract_legal_pdfs.

Scope is the checksum surface added for SEC-01: parsing the recorded sums,
hashing a file against an expected digest, and the aggregate gate that
main() uses to decide whether to halt. The extraction functions
(pdftotext / pymupdf) shell out to external binaries and are not exercised
here.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

import extract_legal_pdfs as mod


def _write(path: Path, data: bytes) -> str:
    path.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def test_load_expected_checksums_missing_file(monkeypatch, tmp_path):
    monkeypatch.setattr(mod, "CHECKSUMS_FILE", tmp_path / "absent.sha256")
    assert mod.load_expected_checksums() == {}


def test_load_expected_checksums_parses_and_skips_comments(monkeypatch, tmp_path):
    checks = tmp_path / "checksums.sha256"
    checks.write_text(
        "# a comment\n"
        "\n"
        "ABCDEF0123456789  appellate-style-manual.pdf\n"
        "0011223344556677  lc-drafting-manual.pdf\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(mod, "CHECKSUMS_FILE", checks)

    result = mod.load_expected_checksums()

    assert result == {
        "appellate-style-manual.pdf": "abcdef0123456789",
        "lc-drafting-manual.pdf": "0011223344556677",
    }


def test_verify_checksum_match_is_case_insensitive(tmp_path):
    pdf = tmp_path / "x.pdf"
    digest = _write(pdf, b"hello pdf")
    assert mod.verify_checksum(pdf, digest.upper()) is True


def test_verify_checksum_mismatch(tmp_path):
    pdf = tmp_path / "x.pdf"
    _write(pdf, b"hello pdf")
    assert mod.verify_checksum(pdf, "0" * 64) is False


def test_run_integrity_check_empty_no_file(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(mod, "CHECKSUMS_FILE", tmp_path / "absent.sha256")
    assert mod.run_integrity_check({}, tmp_path, ["a.pdf"]) is True
    out = capsys.readouterr().out
    assert "no absent.sha256 found" in out


def test_run_integrity_check_empty_template_present(monkeypatch, capsys, tmp_path):
    checks = tmp_path / "checksums.sha256"
    checks.write_text("# template only, no digests\n", encoding="utf-8")
    monkeypatch.setattr(mod, "CHECKSUMS_FILE", checks)
    assert mod.run_integrity_check({}, tmp_path, ["a.pdf"]) is True
    out = capsys.readouterr().out
    assert "template only" in out


def test_run_integrity_check_all_match(tmp_path):
    pdf = tmp_path / "a.pdf"
    digest = _write(pdf, b"content a")
    assert mod.run_integrity_check({"a.pdf": digest}, tmp_path, ["a.pdf"]) is True


def test_run_integrity_check_missing_digest_warns_but_passes(capsys, tmp_path):
    (tmp_path / "a.pdf").write_bytes(b"content a")
    # "a.pdf" is requested but only "b.pdf" has a recorded digest.
    assert (
        mod.run_integrity_check({"b.pdf": "0" * 64}, tmp_path, ["a.pdf"]) is True
    )
    assert "no checksum recorded for a.pdf" in capsys.readouterr().out


def test_run_integrity_check_mismatch_fails(capsys, tmp_path):
    _write(tmp_path / "a.pdf", b"content a")
    assert (
        mod.run_integrity_check({"a.pdf": "0" * 64}, tmp_path, ["a.pdf"]) is False
    )
    assert "checksum mismatch for a.pdf" in capsys.readouterr().err


def test_main_missing_pdfs_exits_with_guidance(monkeypatch, capsys, tmp_path):
    # No PDFs present: main() should print the download guidance and exit 1.
    monkeypatch.setattr(mod, "SOURCE_DIR", tmp_path)
    monkeypatch.setattr(mod, "RAW_TEXT_DIR", tmp_path / "raw-text")
    monkeypatch.setattr(mod, "PDFS", ["a.pdf"])
    with pytest.raises(SystemExit) as exc:
        mod.main()
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "Missing PDF files" in out
    assert "sha256sum *.pdf > checksums.sha256" in out


def test_assess_yield_flags_low_yield(tmp_path):
    pdf = tmp_path / "a.pdf"
    pdf.write_bytes(b"x" * 200_000)  # ~4 estimated pages at 50KB/page
    metrics = mod.assess_yield("short text\n\nmore", pdf)
    assert metrics["estimated_pages"] == 4
    assert metrics["needs_ocr"] is True
    assert metrics["lines"] == 2


def test_process_pdf_reports_good_yield(monkeypatch, capsys, tmp_path):
    pdf = tmp_path / "a.pdf"
    pdf.write_bytes(b"x" * 1000)
    monkeypatch.setattr(mod, "SOURCE_DIR", tmp_path)
    monkeypatch.setattr(mod, "RAW_TEXT_DIR", tmp_path / "raw-text")
    monkeypatch.setattr(
        mod, "extract_with_pdftotext", lambda p, o: "word " * 200
    )
    mod.process_pdf("a.pdf")
    out = capsys.readouterr().out
    assert "Processing: a.pdf" in out
    assert "Written to:" in out


def test_process_pdf_warns_on_low_yield(monkeypatch, capsys, tmp_path):
    pdf = tmp_path / "big.pdf"
    pdf.write_bytes(b"x" * 500_000)  # large file, tiny text -> needs_ocr
    monkeypatch.setattr(mod, "SOURCE_DIR", tmp_path)
    monkeypatch.setattr(mod, "RAW_TEXT_DIR", tmp_path / "raw-text")
    # Enough chars to pass the 500-char extraction floor but still low per page.
    monkeypatch.setattr(mod, "extract_with_pdftotext", lambda p, o: "y" * 600)
    mod.process_pdf("big.pdf")
    out = capsys.readouterr().out
    assert "Low character yield" in out
    assert "image-based" in out


def test_process_pdf_extraction_fails(monkeypatch, capsys, tmp_path):
    pdf = tmp_path / "a.pdf"
    pdf.write_bytes(b"x" * 1000)
    monkeypatch.setattr(mod, "SOURCE_DIR", tmp_path)
    monkeypatch.setattr(mod, "RAW_TEXT_DIR", tmp_path / "raw-text")
    monkeypatch.setattr(mod, "extract_with_pdftotext", lambda p, o: None)
    monkeypatch.setattr(mod, "extract_with_pymupdf", lambda p, o: None)
    mod.process_pdf("a.pdf")
    out = capsys.readouterr().out
    assert "FAILED: Could not extract text" in out


def test_main_checksum_mismatch_exits(monkeypatch, capsys, tmp_path):
    # PDF present but its recorded checksum does not match: main() exits 1
    # before any extraction is attempted.
    _write(tmp_path / "a.pdf", b"content a")
    monkeypatch.setattr(mod, "SOURCE_DIR", tmp_path)
    monkeypatch.setattr(mod, "RAW_TEXT_DIR", tmp_path / "raw-text")
    monkeypatch.setattr(mod, "PDFS", ["a.pdf"])
    monkeypatch.setattr(mod, "load_expected_checksums", lambda: {"a.pdf": "0" * 64})

    def _fail_if_called(_name):
        raise AssertionError("process_pdf must not run when integrity fails")

    monkeypatch.setattr(mod, "process_pdf", _fail_if_called)
    with pytest.raises(SystemExit) as exc:
        mod.main()
    assert exc.value.code == 1
    assert "checksum mismatch for a.pdf" in capsys.readouterr().err
