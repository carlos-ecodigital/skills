"""Tests for LandownerConsentParser - Phase B5."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import CorruptDocError  # noqa: E402
from document_parsers.landowner_consent import LandownerConsentParser  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), text, fontsize=10)
    doc.save(str(path))
    doc.close()


SAMPLE_FULL = (
    "Instemmingsbrief grondeigenaar\n"
    "Ondergetekende: Jan de Vries Holding B.V., gevestigd te Maasdijk,\n"
    "KvK nummer 12345678,\n"
    "verklaart hierbij dat zij hierbij verleent instemming met de\n"
    "ontwikkeling van een warmtekrachtkoppeling op het perceel\n"
    "aan de Zuidweg 14, gemeente Westland.\n"
    "Datum: 14 april 2026\n"
    "Handtekening\n"
    "Jan de Vries\n"
)

SAMPLE_NUM_DATE = (
    "Instemmingsbrief\n"
    "Ondergetekende: Piet Bakker,\n"
    "wonende te Naaldwijk, verklaart hierbij dat hij\n"
    "maakt geen bezwaar tegen de voorgenomen ontwikkeling.\n"
    "Datum: 05-03-2026\n"
    "Getekend\n"
    "Piet Bakker\n"
)

SAMPLE_NO_SIG = (
    "Geachte heer,\n"
    "ondergetekende: Marianne Jansen,\n"
    "wonende te Pijnacker, ga akkoord met de plaatsing van zonnepanelen\n"
    "op de schuur. Geen datum vermeld in deze brief - test data only text.\n"
)


def test_landowner_consent_extracts_name_and_kvk(tmp_path):
    p = tmp_path / "consent.pdf"
    _make_pdf(SAMPLE_FULL, p)
    r = LandownerConsentParser(p).parse()
    assert r.fields_populated["_landowner_name"].startswith("Jan de Vries")
    assert r.fields_populated["_landowner_kvk"] == "12345678"


def test_landowner_consent_extracts_word_date(tmp_path):
    p = tmp_path / "consent.pdf"
    _make_pdf(SAMPLE_FULL, p)
    r = LandownerConsentParser(p).parse()
    assert r.fields_populated["_consent_date"] == "2026-04-14"


def test_landowner_consent_extracts_numeric_date(tmp_path):
    p = tmp_path / "consent.pdf"
    _make_pdf(SAMPLE_NUM_DATE, p)
    r = LandownerConsentParser(p).parse()
    assert r.fields_populated["_consent_date"] == "2026-03-05"


def test_landowner_consent_scope_detected(tmp_path):
    p = tmp_path / "consent.pdf"
    _make_pdf(SAMPLE_FULL, p)
    r = LandownerConsentParser(p).parse()
    scope = r.fields_populated["_consent_scope"]
    assert "hierbij verleent" in scope.lower() or "instemming" in scope.lower()


def test_landowner_consent_signed_positive(tmp_path):
    p = tmp_path / "consent.pdf"
    _make_pdf(SAMPLE_FULL, p)
    r = LandownerConsentParser(p).parse()
    assert r.fields_populated["_signed"] is True


def test_landowner_consent_signed_negative(tmp_path):
    p = tmp_path / "consent.pdf"
    _make_pdf(SAMPLE_NO_SIG, p)
    r = LandownerConsentParser(p).parse()
    assert r.fields_populated["_signed"] is False


def test_landowner_consent_no_kvk_for_residential(tmp_path):
    p = tmp_path / "consent.pdf"
    _make_pdf(SAMPLE_NO_SIG, p)
    r = LandownerConsentParser(p).parse()
    assert "_landowner_kvk" not in r.fields_populated
    assert any("_landowner_kvk" in w for w in r.warnings)


def test_landowner_consent_corrupt_pdf(tmp_path):
    p = tmp_path / "not.pdf"
    p.write_bytes(b"this is not a PDF -- junk bytes that PyMuPDF rejects")
    with pytest.raises(CorruptDocError):
        LandownerConsentParser(p).parse()


def test_landowner_consent_parser_metadata():
    assert LandownerConsentParser.doc_type == "landowner_consent"
    assert LandownerConsentParser.parser_version == "0.1"
    assert "_consent_date" in LandownerConsentParser.populates_fields
    assert "_signed" in LandownerConsentParser.populates_fields
