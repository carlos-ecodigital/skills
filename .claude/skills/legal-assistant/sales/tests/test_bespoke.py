"""M4 — Bespoke LOI type tests.

Covers:
  - Schema validation: happy path + every rejection case.
  - Build pipeline: produces a Document without errors.
  - QA catalog enforcement: bespoke clauses run the same gate as
    templated types (R-1 banned phrase, R-7 Unicode arrow).
  - YAML overrides: agreement_type / subject / party_label work.
"""
from __future__ import annotations

import importlib.util
import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

import pytest

_COLOCATION = Path(__file__).resolve().parent.parent
_DOC_FACTORY = _COLOCATION.parent.parent / "document-factory"
sys.path.insert(0, str(_DOC_FACTORY))
sys.path.insert(0, str(_COLOCATION))

# Load generate_loi.py by file path — the colocation dir isn't a package.
_spec = importlib.util.spec_from_file_location(
    "generate_loi", str(_COLOCATION / "generate_loi.py")
)
generate_loi = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(generate_loi)


def _minimal_bespoke() -> dict:
    """Minimum viable Bespoke YAML-as-dict. Every test derives from this."""
    return {
        "type": "Bespoke",
        "provider": {
            "short_name": "Digital Energy",
            "signatory_name": "Carlos Reuven",
            "signatory_title": "Founder & CEO",
        },
        "counterparty": {
            "name": "Acme Bespoke B.V.",
            "short": "Acme",
            "description": "a test counterparty used by the bespoke suite",
            "signatory_name": "Test Signatory",
            "signatory_title": "Director",
        },
        "programme": {"recital_a_variant": "default"},
        "dates": {"loi_date": "2026-04-17"},
        "clauses": [
            {
                "number": "1",
                "heading": "Partnership Model",
                "paragraphs": [
                    "1.1 The Parties intend to develop an integrated offering."
                ],
                "subclauses": [
                    {"letter": "a", "text": "the Provider delivers facility infrastructure;"},
                    {"letter": "b", "text": "the Partner delivers managed services."},
                ],
            },
            {
                "number": "2",
                "heading": "Non-Binding Status",
                "paragraphs": [
                    "2.1 This LOI is non-binding.",
                ],
            },
        ],
    }


def _call_validate(d: dict) -> list[str]:
    """Run validate() and capture the error list. validate() uses
    sys.exit(1) + prints to stdout on failure; we capture stdout to
    recover the errors."""
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            generate_loi.validate(d)
        return []  # validation passed
    except SystemExit:
        return [
            line.strip().lstrip("- ").strip()
            for line in buf.getvalue().splitlines()
            if line.strip().startswith("-")
        ]


# ───────────────────────────── schema validation


def test_happy_path_passes_validation() -> None:
    assert _call_validate(_minimal_bespoke()) == []


def test_missing_clauses_rejected() -> None:
    d = _minimal_bespoke()
    del d["clauses"]
    errs = _call_validate(d)
    assert any("clauses required for Bespoke" in e for e in errs), errs


def test_empty_clauses_list_rejected() -> None:
    d = _minimal_bespoke()
    d["clauses"] = []
    errs = _call_validate(d)
    assert any("clauses required for Bespoke" in e for e in errs), errs


def test_clause_missing_heading_rejected() -> None:
    d = _minimal_bespoke()
    d["clauses"][0].pop("heading")
    errs = _call_validate(d)
    assert any("heading required" in e for e in errs), errs


def test_clause_missing_number_rejected() -> None:
    d = _minimal_bespoke()
    d["clauses"][0].pop("number")
    errs = _call_validate(d)
    assert any("number required" in e for e in errs), errs


def test_clause_missing_paragraphs_rejected() -> None:
    d = _minimal_bespoke()
    d["clauses"][0].pop("paragraphs")
    errs = _call_validate(d)
    assert any("paragraphs required" in e for e in errs), errs


def test_subclause_missing_letter_rejected() -> None:
    d = _minimal_bespoke()
    d["clauses"][0]["subclauses"][0].pop("letter")
    errs = _call_validate(d)
    assert any("letter required" in e for e in errs), errs


def test_subclause_missing_text_rejected() -> None:
    """Symmetry with test_subclause_missing_letter_rejected — both
    subclause fields are validated, so both must have a test."""
    d = _minimal_bespoke()
    d["clauses"][0]["subclauses"][0].pop("text")
    errs = _call_validate(d)
    assert any("text required" in e for e in errs), errs


def test_optional_recital_missing_text_rejected() -> None:
    d = _minimal_bespoke()
    d["recitals"] = [{"letter": "C"}]   # text missing
    errs = _call_validate(d)
    assert any("recitals[0].text required" in e for e in errs), errs


def test_optional_recital_missing_letter_rejected() -> None:
    """Symmetry with test_optional_recital_missing_text_rejected — both
    recital fields are validated, so both must have a test."""
    d = _minimal_bespoke()
    d["recitals"] = [{"text": "Some recital content."}]   # letter missing
    errs = _call_validate(d)
    assert any("recitals[0].letter required" in e for e in errs), errs


def test_error_message_lists_bespoke_in_allowed_types() -> None:
    d = _minimal_bespoke()
    d["type"] = "NotAType"
    errs = _call_validate(d)
    assert any("Bespoke" in e for e in errs), errs


# ───────────────────────────── build pipeline


def test_build_returns_document() -> None:
    loi = generate_loi.LOI(_minimal_bespoke())
    doc = loi.build()
    assert doc is not None
    # Sanity: there should be body content from our 2 clauses + recitals.
    paragraph_texts = [p.text for p in doc.paragraphs]
    # Clause headings present
    assert any("Partnership Model" in t for t in paragraph_texts)
    assert any("Non-Binding Status" in t for t in paragraph_texts)
    # Subclause lettering present
    assert any(t.startswith("(a)") for t in paragraph_texts)
    assert any(t.startswith("(b)") for t in paragraph_texts)


def test_build_respects_agreement_type_override() -> None:
    d = _minimal_bespoke()
    d["agreement_type"] = "Letter of Intent and NCNDA"
    loi = generate_loi.LOI(d)
    assert loi.agreement_type == "Letter of Intent and NCNDA"


def test_build_respects_subject_override() -> None:
    d = _minimal_bespoke()
    d["subject"] = "Custom Bespoke Deal Subject"
    loi = generate_loi.LOI(d)
    assert loi.subject == "Custom Bespoke Deal Subject"


def test_build_respects_party_label_override() -> None:
    d = _minimal_bespoke()
    d["party_label"] = "Supplier"
    loi = generate_loi.LOI(d)
    assert loi.party == "Supplier"


def test_build_uses_defaults_when_no_overrides() -> None:
    loi = generate_loi.LOI(_minimal_bespoke())
    assert loi.agreement_type == "Letter of Intent"
    assert loi.subject == "Bespoke Engagement"
    assert loi.party == "Counterparty"


def test_build_includes_optional_recital_c() -> None:
    d = _minimal_bespoke()
    d["recitals"] = [
        {"letter": "C", "text": "The Parties have identified complementary capabilities."},
    ]
    loi = generate_loi.LOI(d)
    doc = loi.build()
    texts = [p.text for p in doc.paragraphs]
    assert any(t.startswith("(C) The Parties have identified") for t in texts), texts


# ───────────────────────────── QA gate — full catalog still applies


def _qa(doc, data) -> tuple[str, list[str]]:
    """Thin wrapper around qa_lint's 5-arg signature for tests."""
    return generate_loi.qa_lint(
        doc, data,
        builder_findings=[],
        overrides=set(),
        override_reason="",
    )


def test_qa_catches_unicode_arrow_in_bespoke_clause() -> None:
    """R-7: a Bespoke paragraph containing '→' must trip the QA gate,
    identical behavior to templated types."""
    d = _minimal_bespoke()
    d["clauses"][0]["paragraphs"].append("1.2 Revenue flows Provider → Partner → Customer.")
    loi = generate_loi.LOI(d)
    doc = loi.build()
    status, report = _qa(doc, d)
    assert status == "FAIL"
    assert any("[FAIL] R-7" in line for line in report), (
        "Expected R-7 to fire on Unicode arrow. Report:\n" + "\n".join(report)
    )


def test_qa_catches_five_year_commitment_in_bespoke_clause() -> None:
    """R-1: banned commitment-term phrase must fire on Bespoke content."""
    d = _minimal_bespoke()
    d["clauses"][1]["paragraphs"].append(
        "2.2 The parties agree to a minimum commitment term of 5 years."
    )
    loi = generate_loi.LOI(d)
    doc = loi.build()
    status, report = _qa(doc, d)
    assert status == "FAIL"
    assert any("[FAIL] R-1" in line for line in report), (
        "Expected R-1 to fire. Report:\n" + "\n".join(report)
    )


def test_qa_clean_bespoke_passes() -> None:
    """Happy path: a clean Bespoke document with no banned phrases has
    status PASS or PASS_WITH_WARN (no FAILs)."""
    d = _minimal_bespoke()
    loi = generate_loi.LOI(d)
    doc = loi.build()
    status, report = _qa(doc, d)
    assert status in ("PASS", "PASS_WITH_WARN"), (
        f"Expected no fails. status={status}\n" + "\n".join(report)
    )
    assert not any("[FAIL]" in line for line in report), (
        "FAIL marker in report:\n" + "\n".join(report)
    )


# ───────────────────────────── footer version stamp


def test_footer_version_is_v1_0_for_bespoke() -> None:
    """Footer should emit DE-LOI-Bespoke-v1.0 as the version reference."""
    loi = generate_loi.LOI(_minimal_bespoke())
    doc = loi.build()
    texts = [p.text for p in doc.paragraphs]
    assert any("DE-LOI-Bespoke-v1.0" in t for t in texts), (
        "Expected 'DE-LOI-Bespoke-v1.0' in body footer. "
        f"Last paragraphs: {texts[-5:]}"
    )
