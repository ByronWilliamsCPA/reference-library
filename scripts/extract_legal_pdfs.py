"""Extract text from Oregon legal style PDFs into raw text files.

Usage:
    python scripts/extract_legal_pdfs.py

Tries pdftotext first (fast, handles text-based PDFs). Falls back to pymupdf
(fitz) for compressed or encoded PDFs. Reports character yield so you can
identify image-based PDFs that need the Claude Code Read tool fallback.

Outputs: legal-style/source-pdfs/raw-text/{name}.txt
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SOURCE_DIR = REPO_ROOT / "legal-style" / "source-pdfs"
RAW_TEXT_DIR = SOURCE_DIR / "raw-text"

PDFS = [
    "appellate-style-manual.pdf",
    "lc-drafting-manual.pdf",
    "lc-form-style-manual.pdf",
]

# If average chars per page falls below this threshold, the PDF is likely
# image-based and requires the Claude Code Read tool for OCR extraction.
MIN_CHARS_PER_PAGE = 100


def extract_with_pdftotext(pdf_path: Path, output_path: Path) -> str | None:
    """Attempt extraction using pdftotext CLI. Returns text or None if unavailable."""
    if not shutil.which("pdftotext"):
        return None

    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), str(output_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(f"  pdftotext error: {result.stderr.strip()}")
        return None

    text = output_path.read_text(encoding="utf-8", errors="replace")
    return text


def extract_with_pymupdf(pdf_path: Path, output_path: Path) -> str | None:
    """Attempt extraction using pymupdf. Returns text or None if unavailable."""
    try:
        import pymupdf  # type: ignore[import-untyped]  # noqa: PLC0415
    except ImportError:
        print("  pymupdf not installed — skipping (run: pip install pymupdf)")
        return None

    doc = pymupdf.open(str(pdf_path))
    pages: list[str] = []
    for page in doc:
        pages.append(page.get_text())
    doc.close()

    text = "\n\n".join(pages)
    output_path.write_text(text, encoding="utf-8")
    return text


def assess_yield(text: str, pdf_path: Path) -> dict[str, object]:
    """Report extraction quality metrics."""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    chars = len(text.strip())

    # Estimate page count from file size (rough: 50KB per page average for text PDFs)
    size_bytes = pdf_path.stat().st_size
    estimated_pages = max(1, size_bytes // 50_000)

    chars_per_page = chars / estimated_pages

    return {
        "chars": chars,
        "lines": len(lines),
        "estimated_pages": estimated_pages,
        "chars_per_page": round(chars_per_page, 1),
        "needs_ocr": chars_per_page < MIN_CHARS_PER_PAGE,
    }


def process_pdf(pdf_name: str) -> None:
    """Extract text from a single PDF using the best available method."""
    pdf_path = SOURCE_DIR / pdf_name
    stem = Path(pdf_name).stem
    output_path = RAW_TEXT_DIR / f"{stem}.txt"

    print(f"\n{'=' * 60}")
    print(f"Processing: {pdf_name}")
    print(f"  Size: {pdf_path.stat().st_size:,} bytes")

    text: str | None = None

    # Try pdftotext first
    print("  Trying pdftotext...", end=" ", flush=True)
    text = extract_with_pdftotext(pdf_path, output_path)
    if text and len(text.strip()) > 500:  # noqa: PLR2004
        print("OK")
    else:
        print("insufficient yield" if text else "not available")
        text = None

    # Fall back to pymupdf
    if text is None:
        print("  Trying pymupdf...", end=" ", flush=True)
        text = extract_with_pymupdf(pdf_path, output_path)
        if text and len(text.strip()) > 500:  # noqa: PLR2004
            print("OK")
        else:
            print("insufficient yield" if text else "not available")
            text = None

    if text is None:
        print(f"\n  FAILED: Could not extract text from {pdf_name}")
        print(f"  ACTION NEEDED: Use Claude Code Read tool on {pdf_path}")
        print("  Example: Read the file 20 pages at a time:")
        print(f"    Read(file_path='{pdf_path}', offset=1, limit=20)")
        return

    metrics = assess_yield(text, pdf_path)
    print(f"\n  Results:")
    print(f"    Characters extracted: {metrics['chars']:,}")
    print(f"    Non-empty lines:      {metrics['lines']:,}")
    print(f"    Estimated pages:      {metrics['estimated_pages']}")
    print(f"    Chars per page (est): {metrics['chars_per_page']}")

    if metrics["needs_ocr"]:
        print(f"\n  WARNING: Low character yield ({metrics['chars_per_page']} chars/page).")
        print("  This PDF appears to be image-based (scanned).")
        print("  Use the Claude Code Read tool for OCR extraction:")
        print(f"    Read(file_path='{pdf_path}', pages='1-20')")
        print("  Repeat in 20-page increments until complete.")
    else:
        print(f"\n  Written to: {output_path}")


def main() -> None:
    """Run extraction for all PDFs."""
    RAW_TEXT_DIR.mkdir(parents=True, exist_ok=True)

    missing = [p for p in PDFS if not (SOURCE_DIR / p).exists()]
    if missing:
        print("Missing PDF files:")
        for name in missing:
            print(f"  {SOURCE_DIR / name}")
        print("\nDownload with:")
        print("  curl -O https://www.courts.oregon.gov/publications/Documents/UpdatedStyleManual2002.pdf")
        print("  curl -O https://www.oregonlegislature.gov/lc/PDFs/draftingmanual.pdf")
        print("  curl -O https://www.oregonlegislature.gov/lc/PDFs/form-stylemanual.pdf")
        sys.exit(1)

    for pdf_name in PDFS:
        process_pdf(pdf_name)

    print(f"\n{'=' * 60}")
    print("Extraction complete. Raw text files:")
    for txt_file in sorted(RAW_TEXT_DIR.glob("*.txt")):
        size = txt_file.stat().st_size
        print(f"  {txt_file.name}: {size:,} chars")


if __name__ == "__main__":
    main()
