"""v3.7.0 linter + CLI + session-tooling tests.

Tests for rules R-29, R-30, R-31, R-27/R-28 broadening, R-11 helper,
R-21 scope narrowing, CLI flags, density profile, SESSION_LOG artifact,
and brochure source_map token / R-24 warn.

All tests written RED-first (before implementation) per PRINCIPLES.md #4.
Baseline: 307 tests green. None of these may touch existing tests.
"""
from __future__ import annotations

import copy
import os
import sys
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

_TESTS_DIR = Path(__file__).resolve().parent
_COLOCATION_DIR = _TESTS_DIR.parent
_EXAMPLES_DIR = _COLOCATION_DIR / "examples"


def _load(name: str) -> dict:
    with open(_EXAMPLES_DIR / name) as f:
        return yaml.safe_load(f)


def _ws_base() -> dict:
    return _load("intake_example_wholesale.yaml")


def _ss_base() -> dict:
    return _load("intake_example_strategic_supplier.yaml")


# ---------------------------------------------------------------------------
# Render helpers
# ---------------------------------------------------------------------------

def _build_loi(data: dict):
    """Build a LOI and return (loi, doc) objects."""
    from generate_loi import LOI
    loi = LOI(data)
    loi.build()
    return loi, loi.doc


def _qa_from_loi(loi, data: dict) -> tuple:
    """Run qa_lint on a built LOI; return (status, lines)."""
    from generate_loi import qa_lint
    return qa_lint(loi.doc, data, loi.qa_findings, loi.overrides, loi.override_reason)


def _qa(data: dict) -> tuple:
    """Build LOI and run qa_lint; return (status, lines)."""
    loi, doc = _build_loi(data)
    return _qa_from_loi(loi, data)


def _qa_raw_text(text: str, data: dict) -> tuple:
    """Run qa_lint over a raw text string wrapped in a fake doc object."""
    from generate_loi import qa_lint

    class _FakeDoc:
        def __init__(self, text):
            self._text = text
            self.paragraphs = [_FakePara(line) for line in text.split("\n")]
            self.tables = []

    class _FakePara:
        def __init__(self, t):
            self.text = t

    fake_doc = _FakeDoc(text)
    return qa_lint(fake_doc, data, [], set(), "")


# ===========================================================================
# R-29: URL content verification
# ===========================================================================

class FakeFetcher:
    """Injected URL fetcher for test isolation (no real network)."""

    def __init__(self, responses: dict):
        self._responses = responses

    def fetch(self, url: str) -> str:
        return self._responses.get(url, "")


def test_r29_keyword_found_passes():
    """R-29: URL returns >=500 chars containing claim keyword -> returns True."""
    from generate_loi import _check_url_content
    url = "https://example.com/gpu-infra"
    keyword = "gpu"
    long_content = "gpu cloud compute data center accelerated " * 15  # >500 chars
    assert len(long_content) >= 500
    fetcher = FakeFetcher({url: long_content})
    result = _check_url_content(url, keyword, fetcher=fetcher)
    assert result is True


def test_r29_keyword_missing_downgrades():
    """R-29: URL returns >=500 chars but keyword absent -> returns False."""
    from generate_loi import _check_url_content
    url = "https://example.com/page"
    keyword = "nuclear"
    long_content = "solar wind hydro renewable energy storage " * 15  # >=500 chars
    assert len(long_content) >= 500
    fetcher = FakeFetcher({url: long_content})
    result = _check_url_content(url, keyword, fetcher=fetcher)
    assert result is False


def test_r29_fetch_failure_flagged():
    """R-29: fetcher returns empty string (fetch failure) -> returns False."""
    from generate_loi import _check_url_content
    url = "https://dark-site.example.com"
    fetcher = FakeFetcher({})  # no response -> empty string
    result = _check_url_content(url, "any", fetcher=fetcher)
    assert result is False


# ===========================================================================
# R-30: Double-period detector
# ===========================================================================

def test_r30_double_period_caught():
    """R-30: body contains '..' (not '...') -> FAIL."""
    data = _ws_base()
    # v3.8.0: inject double period via slot 5 claim (description removed).
    data["counterparty"]["recital_b"]["bargain_relevant_fact"] = {
        "claim": "with announced anchor capacity.. across European sites",
        "source": {"tier": 1, "url": "https://example.com/", "retrieved": "2026-05-01"},
    }
    loi, doc = _build_loi(data)
    from generate_loi import _extract_text
    text = _extract_text(doc)
    assert ".." in text, "Test precondition: '..' must appear in rendered text"
    status, lines = _qa_from_loi(loi, data)
    r30_lines = [l for l in lines if "R-30" in l]
    assert r30_lines, "R-30 did not fire. Lines:\n" + "\n".join(lines)
    assert "[FAIL]" in r30_lines[0]


def test_r30_ellipsis_ignored():
    """R-30: '...' ellipsis must NOT be flagged."""
    data = _ws_base()
    text = "The parties agree to the following terms... subject to negotiation."
    status, lines = _qa_raw_text(text, data)
    r30_lines = [l for l in lines if "R-30" in l]
    assert not r30_lines, "R-30 wrongly fired on ellipsis. Lines:\n" + "\n".join(lines)


def test_r30_numbered_list_ignored():
    """R-30: '3.1.' numbered-list notation must NOT be flagged."""
    data = _ws_base()
    text = "This is Clause 3.1. The next obligation is at Clause 3.2."
    status, lines = _qa_raw_text(text, data)
    r30_lines = [l for l in lines if "R-30" in l]
    assert not r30_lines, "R-30 wrongly fired on '3.1.' notation. Lines:\n" + "\n".join(lines)


# ===========================================================================
# R-31: contact_name == signatory_name
# ===========================================================================

def test_r31_equal_names_warn():
    """R-31: contact_name == signatory_name (case-insensitive, trimmed) -> WARN."""
    data = _ws_base()
    data["counterparty"]["contact_name"] = "Alex Park"
    data["counterparty"]["signatory_name"] = "Alex Park"
    status, lines = _qa(data)
    r31_lines = [l for l in lines if "R-31" in l]
    assert r31_lines, "R-31 did not fire on equal names. Lines:\n" + "\n".join(lines)
    assert "[WARN]" in r31_lines[0]
    assert "single-point-of-contact" in r31_lines[0].lower()


def test_r31_different_names_silent():
    """R-31: contact_name != signatory_name -> no R-31 firing."""
    data = _ws_base()
    data["counterparty"]["contact_name"] = "Sarah Chen"
    data["counterparty"]["signatory_name"] = "Alex Park"
    status, lines = _qa(data)
    r31_lines = [l for l in lines if "R-31" in l]
    assert not r31_lines, "R-31 wrongly fired on different names. Lines:\n" + "\n".join(lines)


# ===========================================================================
# R-27 / R-28 broadening: bare TBC
# ===========================================================================

def test_r27_bare_tbc_in_sig_block_fires():
    """R-27 broadening: bare 'TBC' (no brackets) in sig-block Name field -> FAIL."""
    data = _ws_base()
    text = "Name: TBC\nTitle: Chief Executive Officer\n\nName: Carlos Reuven\nTitle: Director"
    status, lines = _qa_raw_text(text, data)
    r27_lines = [l for l in lines if "R-27" in l]
    assert r27_lines, "R-27 did not fire on bare TBC. Lines:\n" + "\n".join(lines)


def test_r27_bracketed_tbc_still_fires():
    """R-27: original [TBC] bracketed form still fires."""
    data = _ws_base()
    text = "Name: [TBC]\nTitle: Director\n\nName: Carlos Reuven\nTitle: Director"
    status, lines = _qa_raw_text(text, data)
    r27_lines = [l for l in lines if "R-27" in l]
    assert r27_lines, "R-27 did not fire on bracketed [TBC]. Lines:\n" + "\n".join(lines)


# ===========================================================================
# R-11: certifications_in_source helper
# ===========================================================================

def test_r11_certifications_in_source_populated():
    """certifications_in_source(intake) returns list of detected ISO/certs."""
    from generate_loi import certifications_in_source
    data = _ws_base()
    # v3.8.0: certifications scanned across slot fields, not description.
    # Inject via slot 5 claim.
    data["counterparty"]["recital_b"]["bargain_relevant_fact"] = {
        "claim": "certified under ISO 27001 and ISO 14001, pursuing SOC 2",
        "source": {"tier": 1, "url": "https://example.com/", "retrieved": "2026-05-01"},
    }
    certs = certifications_in_source(data)
    assert isinstance(certs, list)
    assert len(certs) >= 1
    found = " ".join(certs)
    assert "ISO" in found or "SOC" in found


# ===========================================================================
# R-21 scope narrowing: purpose-built allowed in Cl. 3
# ===========================================================================

def test_r21_purpose_built_in_recital_b_fires():
    """R-21: 'purpose-built' in Recital B context text -> WARN fires."""
    data = _ws_base()
    text = (
        "(B) NeoScale is a purpose-built GPU cloud provider [TBC -- synthetic example].\n"
        "The parties agree to the following terms.\n"
    )
    status, lines = _qa_raw_text(text, data)
    r21_lines = [l for l in lines if "R-21" in l and "[WARN]" in l]
    assert r21_lines, "R-21 did not fire for 'purpose-built' in Recital B. Lines:\n" + "\n".join(lines)


def test_r21_purpose_built_in_cl3_passes():
    """R-21: 'purpose-built' ONLY inside Clause 3 product text -> no R-21 WARN."""
    data = _ws_base()
    # Text where purpose-built appears ONLY in a Clause 3 section
    text = (
        "3. PRODUCT CAPABILITIES\n"
        "3.1 The Supplier offers purpose-built server infrastructure for AI compute.\n"
        "4. COMMERCIAL TERMS\n"
        "4.1 Pricing is indicative.\n"
    )
    status, lines = _qa_raw_text(text, data)
    r21_lines = [l for l in lines if "R-21" in l and "[WARN]" in l]
    assert not r21_lines, (
        "R-21 wrongly fired for 'purpose-built' in Cl. 3 product text. "
        "Lines:\n" + "\n".join(lines)
    )


# ===========================================================================
# CLI flags parse correctly
# ===========================================================================

def test_cli_recital_b_only_flag_parsed():
    """--recital-b-only <path> is parsed by _parse_arg."""
    from generate_loi import _parse_arg
    with patch("sys.argv", ["generate_loi.py", "intake.yaml",
                             "--recital-b-only", "/tmp/existing.docx"]):
        val = _parse_arg("--recital-b-only")
    assert val == "/tmp/existing.docx"


def test_cli_audit_only_flag_detected():
    """--audit-only flag is detectable via _parse_flag."""
    from generate_loi import _parse_flag
    with patch("sys.argv", ["generate_loi.py", "intake.yaml", "--audit-only"]):
        assert _parse_flag("--audit-only") is True


def test_cli_verify_source_urls_flag_detected():
    """--verify-source-urls flag is detectable via _parse_flag."""
    from generate_loi import _parse_flag
    with patch("sys.argv", ["generate_loi.py", "intake.yaml", "--verify-source-urls"]):
        assert _parse_flag("--verify-source-urls") is True


def test_cli_phase_8_auto_execute_flag_parsed():
    """--phase-8-auto-execute flag is defined and detectable."""
    from generate_loi import _parse_flag
    with patch("sys.argv", ["generate_loi.py", "intake.yaml", "--phase-8-auto-execute"]):
        assert _parse_flag("--phase-8-auto-execute") is True


# ===========================================================================
# density: terse / standard / verbose
# ===========================================================================

def _ws_with_density(density: str) -> dict:
    data = _ws_base()
    data.setdefault("choices", {})["recital_b_density"] = density
    return data


def _recital_b_word_count(data: dict) -> int:
    """Extract Recital B text from rendered body and count words."""
    import re
    from generate_loi import LOI, _extract_text
    loi = LOI(data)
    loi.build()
    text = _extract_text(loi.doc)
    m = re.search(r"\(B\)\s*(.*?)(?=\(C\)\s|\(D\)\s|\n##\s|\Z)", text, re.DOTALL)
    if not m:
        return 0
    return len(m.group(1).split())


def test_density_terse_shorter_than_standard():
    """terse density -> word count <= standard."""
    terse = _recital_b_word_count(_ws_with_density("terse"))
    standard = _recital_b_word_count(_ws_with_density("standard"))
    assert terse <= standard, (
        f"Expected terse ({terse}w) <= standard ({standard}w) Recital B word count"
    )


def test_density_verbose_longer_than_standard():
    """verbose density -> word count >= standard."""
    verbose = _recital_b_word_count(_ws_with_density("verbose"))
    standard = _recital_b_word_count(_ws_with_density("standard"))
    assert verbose >= standard, (
        f"Expected verbose ({verbose}w) >= standard ({standard}w) Recital B word count"
    )


def test_density_invalid_rejected():
    """choices.recital_b_density with unknown value -> SystemExit from validate()."""
    data = _ws_base()
    data.setdefault("choices", {})["recital_b_density"] = "ultra_verbose"
    with pytest.raises(SystemExit):
        from generate_loi import validate
        validate(data)


# ===========================================================================
# SESSION_LOG.md artifact
# ===========================================================================

def test_session_log_emitted(tmp_path):
    """SESSION_LOG.md is emitted alongside the .docx at end of main()."""
    import subprocess
    intake_src = _EXAMPLES_DIR / "intake_example_wholesale.yaml"
    out_docx = str(tmp_path / "test_out.docx")
    result = subprocess.run(
        [sys.executable, str(_COLOCATION_DIR / "generate_loi.py"),
         str(intake_src), "--output", out_docx],
        capture_output=True, text=True
    )
    stem = Path(out_docx).stem
    log_path = tmp_path / f"{stem}_SESSION_LOG.md"
    assert log_path.exists(), (
        f"SESSION_LOG.md not found at {log_path}.\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )


def test_session_log_has_expected_sections(tmp_path):
    """SESSION_LOG.md contains all required section headers."""
    import subprocess
    intake_src = _EXAMPLES_DIR / "intake_example_wholesale.yaml"
    out_docx = str(tmp_path / "test_out2.docx")
    subprocess.run(
        [sys.executable, str(_COLOCATION_DIR / "generate_loi.py"),
         str(intake_src), "--output", out_docx],
        capture_output=True, text=True
    )
    stem = Path(out_docx).stem
    log_path = tmp_path / f"{stem}_SESSION_LOG.md"
    if not log_path.exists():
        pytest.skip("SESSION_LOG not emitted -- checked by test_session_log_emitted")
    content = log_path.read_text()
    for section in ["## Intake decisions", "## CLI flags used",
                     "## QA summary", "## Customizations"]:
        assert section in content, f"Missing section '{section}' in SESSION_LOG.md"


# ===========================================================================
# Brochure source_map token
# ===========================================================================

def _ws_with_brochure_pillar(pillar_key: str = "pillar_1") -> dict:
    data = _ws_base()
    data["counterparty"]["source_map"][pillar_key] = "internal:brochure_20260417_cerebro"
    return data


def test_brochure_token_accepted_by_r23():
    """internal:brochure_* token in source_map -> R-23 does NOT fail (tier-2 accepted)."""
    data = _ws_with_brochure_pillar("pillar_1")
    # v3.8.0: inject material claim via slot 5 (description removed).
    data["counterparty"]["recital_b"]["bargain_relevant_fact"] = {
        "claim": "with 22 MW of GPU capacity across European sites",
        "source": {"tier": 2, "url": "internal:brochure_20260501_test", "retrieved": "2026-05-01"},
    }
    status, lines = _qa(data)
    r23_fail = [l for l in lines if "R-23" in l and "[FAIL]" in l]
    assert not r23_fail, (
        "R-23 wrongly failed for brochure token. Lines:\n" + "\n".join(lines)
    )


def test_r24_brochure_fires_warn():
    """R-24 (warn): any pillar using internal:brochure_* -> warn about corroboration."""
    data = _ws_with_brochure_pillar("pillar_3")
    status, lines = _qa(data)
    r24_lines = [l for l in lines if "R-24" in l and "[WARN]" in l]
    assert r24_lines, (
        "R-24 did not fire for brochure token. Lines:\n" + "\n".join(lines)
    )
    assert "corroboration" in r24_lines[0].lower() or "brochure" in r24_lines[0].lower()


def test_brochure_and_url_mix_ok():
    """Mix of internal:brochure_* and real URL pillars -> R-23 passes, R-24 warns."""
    data = _ws_with_brochure_pillar("pillar_3")
    data["counterparty"]["source_map"]["pillar_1"] = "https://example.com/about"
    data["counterparty"]["source_map"]["pillar_2"] = "https://example.com/products"
    status, lines = _qa(data)
    r23_fail = [l for l in lines if "R-23" in l and "[FAIL]" in l]
    assert not r23_fail, f"R-23 wrongly failed for mixed token set"
    r24_warn = [l for l in lines if "R-24" in l and "[WARN]" in l]
    assert r24_warn, f"R-24 should still warn when brochure is in mix"
