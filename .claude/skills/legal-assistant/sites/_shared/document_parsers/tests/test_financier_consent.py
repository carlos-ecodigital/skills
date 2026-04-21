"""Tests for FinancierConsentParser - Phase B5."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PARENT = Path(__file__).resolve().parents[2]
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from document_parsers.base import CorruptDocError  # noqa: E402
from document_parsers.financier_consent import FinancierConsentParser  # noqa: E402


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), text, fontsize=10)
    doc.save(str(path))
    doc.close()


SAMPLE_BANK = (
    "Instemmingsbrief grondfinancier\n"
    "Rabobank Westland e.o. N.V., gevestigd te Naaldwijk,\n"
    "KvK nummer 30110055,\n"
    "verklaart hierbij in te stemmen met de voorgenomen ontwikkeling\n"
    "op het perceel waarvoor hypotheek nummer 2019-000123 is gevestigd.\n"
    "Datum: 12 april 2026\n"
    "Handtekening\n"
    "Namens Rabobank, mevr. J. de Jong\n"
)

SAMPLE_FALLBACK_BANK = (
    "Geachte relatie,\n"
    "Namens ABN AMRO Bank bevestigen wij dat wij geen bezwaar\n"
    "hebben tegen de ontwikkeling. Wij refereren aan hypotheek\n"
    "kenmerk NL-HYP-2022-987654 op het betreffende perceel.\n"
    "Datum: 03-04-2026\n"
    "Getekend, de kredietbeheerder\n"
)

SAMPLE_CORRUPT = b"Pretend PDF -- not valid -- deliberately corrupt bytes here"


def test_financier_consent_bank_name_labeled(tmp_path):
    p = tmp_path / "fin.pdf"
    _make_pdf(SAMPLE_BANK, p)
    r = FinancierConsentParser(p).parse()
    assert "Rabobank" in r.fields_populated["_financier_name"]


def test_financier_consent_kvk(tmp_path):
    p = tmp_path / "fin.pdf"
    _make_pdf(SAMPLE_BANK, p)
    r = FinancierConsentParser(p).parse()
    assert r.fields_populated["_financier_kvk"] == "30110055"


def test_financier_consent_encumbrance_reference(tmp_path):
    p = tmp_path / "fin.pdf"
    _make_pdf(SAMPLE_BANK, p)
    r = FinancierConsentParser(p).parse()
    # Normalise: the reference token should include the year segment.
    assert "2019" in r.fields_populated["_encumbrance_reference"]


def test_financier_consent_dated_word_form(tmp_path):
    p = tmp_path / "fin.pdf"
    _make_pdf(SAMPLE_BANK, p)
    r = FinancierConsentParser(p).parse()
    assert r.fields_populated["_consent_date"] == "2026-04-12"


def test_financier_consent_dated_numeric(tmp_path):
    p = tmp_path / "fin.pdf"
    _make_pdf(SAMPLE_FALLBACK_BANK, p)
    r = FinancierConsentParser(p).parse()
    assert r.fields_populated["_consent_date"] == "2026-04-03"


def test_financier_consent_fallback_known_bank(tmp_path):
    p = tmp_path / "fin.pdf"
    _make_pdf(SAMPLE_FALLBACK_BANK, p)
    r = FinancierConsentParser(p).parse()
    assert "ABN" in r.fields_populated["_financier_name"].upper()


def test_financier_consent_signed_positive(tmp_path):
    p = tmp_path / "fin.pdf"
    _make_pdf(SAMPLE_BANK, p)
    r = FinancierConsentParser(p).parse()
    assert r.fields_populated["_signed"] is True


def test_financier_consent_corrupt_pdf(tmp_path):
    p = tmp_path / "broken.pdf"
    p.write_bytes(SAMPLE_CORRUPT)
    with pytest.raises(CorruptDocError):
        FinancierConsentParser(p).parse()


def test_financier_consent_parser_metadata():
    assert FinancierConsentParser.doc_type == "financier_consent"
    assert FinancierConsentParser.parser_version == "0.1"
    assert "_financier_name" in FinancierConsentParser.populates_fields
    assert "_encumbrance_reference" in FinancierConsentParser.populates_fields
