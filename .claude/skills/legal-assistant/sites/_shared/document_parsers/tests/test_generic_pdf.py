"""Tests for GenericPDFParser — Phase B5."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import CorruptDocError, UnreadableScanError  # noqa: E402
from document_parsers.generic_pdf import GenericPDFParser  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    """Helper: produce a native-text PDF via PyMuPDF."""
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), text, fontsize=10)
    doc.save(str(path))
    doc.close()


def test_generic_pdf_extracts_text_from_van_gog():
    """Real native-text PDF — the Van Gog LOI."""
    vg = Path("/Users/crmg/Downloads/DEC_LOI_Lodewijk_VanGog_DRAFT_v1.pdf")
    if not vg.exists():
        pytest.skip("Van Gog PDF not available in this environment")
    result = GenericPDFParser(vg).parse()
    assert "Letter of Intent" in result.fields_populated["_raw_text"]
    assert result.fields_populated["_page_count"] == 12


def test_generic_pdf_raises_unreadable_scan_on_empty(tmp_path):
    p = tmp_path / "empty.pdf"
    import fitz
    doc = fitz.open()
    doc.new_page()
    doc.save(str(p))
    doc.close()
    with pytest.raises(UnreadableScanError):
        GenericPDFParser(p).parse()


def test_generic_pdf_raises_corrupt_on_non_pdf_bytes(tmp_path):
    p = tmp_path / "not.pdf"
    p.write_bytes(b"this is clearly not a PDF file")
    with pytest.raises(CorruptDocError):
        GenericPDFParser(p).parse()


def test_generic_pdf_extracts_text_with_density(tmp_path):
    p = tmp_path / "dense.pdf"
    text = " ".join(["lorem ipsum dolor sit amet"] * 50)
    _make_pdf(text, p)
    result = GenericPDFParser(p).parse()
    assert "lorem ipsum" in result.fields_populated["_raw_text"]
    assert result.fields_populated["_page_count"] == 1


def test_generic_pdf_warns_on_low_density(tmp_path):
    p = tmp_path / "sparse.pdf"
    _make_pdf("Short text for sparse scan: fifty-one chars of body.", p)
    result = GenericPDFParser(p).parse()
    assert any("low text density" in w for w in result.warnings)


def test_generic_pdf_parser_metadata():
    assert GenericPDFParser.doc_type == "generic_pdf"
    assert GenericPDFParser.parser_version == "0.1"
    assert GenericPDFParser.populates_fields == []


def test_generic_pdf_populates_no_registry_fields(tmp_path):
    p = tmp_path / "x.pdf"
    # Need ≥50 chars to avoid UnreadableScanError
    _make_pdf("Some regular text content here for parsing purposes please thanks.", p)
    result = GenericPDFParser(p).parse()
    non_meta = {k for k in result.fields_populated if not k.startswith("_")}
    assert non_meta == set()


def test_generic_pdf_confidence_is_half(tmp_path):
    p = tmp_path / "x.pdf"
    _make_pdf("Some text content with density above threshold " * 10, p)
    result = GenericPDFParser(p).parse()
    assert result.confidence == 0.5
