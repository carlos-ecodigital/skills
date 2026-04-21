"""Integration: parser chassis exception hierarchy + real-PDF extraction."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from document_parsers import (
    CorruptDocError,
    DocumentParser,
    ParserError,
    UnreadableScanError,
)
from document_parsers.generic_pdf import GenericPDFParser


_VAN_GOG_PDF = Path("/Users/crmg/Downloads/DEC_LOI_Lodewijk_VanGog_DRAFT_v1.pdf")


def test_exception_hierarchy_consistent():
    assert issubclass(CorruptDocError, ParserError)
    assert issubclass(UnreadableScanError, ParserError)


def test_generic_pdf_extracts_12_pages_of_van_gog():
    if not _VAN_GOG_PDF.exists():
        pytest.skip("Van Gog PDF not accessible")
    r = GenericPDFParser(_VAN_GOG_PDF).parse()
    assert r.fields_populated["_page_count"] == 12
    assert "Letter of Intent" in r.fields_populated["_raw_text"]


def test_parser_hash_matches_independent_sha256(tmp_path):
    p = tmp_path / "f.bin"
    p.write_bytes(b"0123456789")
    r = GenericPDFParser(p)
    assert r._compute_hash() == hashlib.sha256(b"0123456789").hexdigest()


def test_all_specialised_parsers_importable():
    """Every shipped parser exposes doc_type + parser_version + populates_fields."""
    from document_parsers import ato, sde_plus, kadaster, kvk, bestemmingsplan
    from document_parsers import landowner_consent, financier_consent, equipment_oem

    parsers = [
        ato.ATOParser,
        sde_plus.SDEPlusParser,
        kadaster.KadasterParser,
        kvk.KvKParser,
        bestemmingsplan.BestemmingsplanParser,
        landowner_consent.LandownerConsentParser,
        financier_consent.FinancierConsentParser,
        equipment_oem.EquipmentOEMParser,
    ]
    for P in parsers:
        assert hasattr(P, "doc_type"), P
        assert hasattr(P, "parser_version"), P
        assert hasattr(P, "populates_fields"), P
        assert issubclass(P, DocumentParser), P


def test_generic_pdf_raises_corrupt_on_bad_bytes(tmp_path):
    p = tmp_path / "bad.pdf"
    p.write_bytes(b"not a PDF")
    with pytest.raises(CorruptDocError):
        GenericPDFParser(p).parse()


def test_generic_pdf_raises_unreadable_scan(tmp_path):
    import fitz
    p = tmp_path / "empty.pdf"
    d = fitz.open()
    d.new_page()
    d.save(str(p))
    d.close()
    with pytest.raises(UnreadableScanError):
        GenericPDFParser(p).parse()
