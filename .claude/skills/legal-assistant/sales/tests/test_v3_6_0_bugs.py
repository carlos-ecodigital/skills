"""v3.6.0 bug-fix regression tests.

Seven production-blocking bugs surfaced by three field retrospectives
(Cerebro Wholesale 2026-04-17, Armada Strategic Supplier 2026-04-19,
InfraPartners Strategic Supplier 2026-04-19). Each test is written to
fail against the pre-v3.6.0 engine and pass after the fix.

Per PRINCIPLES.md #4 — render-logic changes must ship with tests that
exercise the new branch. These tests are the enforcement.
"""
from __future__ import annotations

import copy
from pathlib import Path

import pytest
import yaml

from generate_loi import LOI


_TESTS_DIR = Path(__file__).resolve().parent
_COLOCATION_DIR = _TESTS_DIR.parent
_EXAMPLES_DIR = _COLOCATION_DIR / "examples"


def _load(name: str) -> dict:
    with open(_EXAMPLES_DIR / name) as f:
        return yaml.safe_load(f)


def _render_text(data: dict) -> str:
    """Build LOI; return concatenated body text (paragraphs + tables).

    Skips the cover-page generation to avoid python-docx image-load
    dependency in test envs; body-level assertions only."""
    loi = LOI(data)
    loi.build()
    parts: list[str] = []
    for p in loi.doc.paragraphs:
        if p.text:
            parts.append(p.text)
    for tbl in loi.doc.tables:
        for row in tbl.rows:
            for cell in row.cells:
                parts.append(cell.text)
    return "\n".join(parts)


# ----- Bug 1: Cl. 8.2 `tthe` typo (all non-EndUser types) ---------------

@pytest.mark.parametrize("intake", [
    "intake_example_wholesale.yaml",
    "intake_example_distributor.yaml",
    "intake_example_strategic_supplier.yaml",
    # EP does not render Cl. 8.2 Good Faith (different general-provisions
    # structure; its cl_general starts at 7 and skips the good-faith block).
])
def test_bug1_no_tthe_typo(intake):
    """Armada §2.1: non-EndUser Cl. 8.2 emits 'tthe good faith' (double-t).

    Root cause (line ~1583): ternary concat
      + ("" if EU else "...,  t") + ("T" if EU else "t") + "he good faith"
    For non-EU: "...t" + "t" + "he" -> "tthe". Fix: drop the extra t in
    the first fragment OR drop the second t — either works."""
    text = _render_text(_load(intake))
    assert "tthe" not in text.lower(), (
        f"{intake}: 'tthe' typo still present in Cl. 8.2 Good Faith body"
    )
    assert "the good faith" in text.lower(), (
        f"{intake}: Cl. 8.2 'good faith' phrase missing after fix"
    )


def test_bug1_enduser_unchanged():
    """EU path starts the sentence: 'The good faith obligation...' — must
    survive the non-EU fix untouched."""
    text = _render_text(_load("intake_example_enduser.yaml"))
    assert "The good faith obligation" in text


# ----- Bug 2: §8.1(b) "Project Finance and Assignment" leak in SS -------

def test_bug2_ss_cl8_1b_clause5_name():
    """InfraPartners §4.1: SS doc says 'Clauses 5 (Project Finance and
    Assignment)' in §8.1(b) — but SS Cl. 5 is 'Supply Chain and Delivery
    Commitment'. Engine hardcoded the WS/DS label at line ~1577 without
    branching on self.t."""
    text = _render_text(_load("intake_example_strategic_supplier.yaml"))
    # The buggy substring:
    assert "Clauses 5 (Project Finance and Assignment)" not in text, (
        "SS §8.1(b) still says 'Project Finance and Assignment' — should "
        "say 'Supply Chain and Delivery Commitment'"
    )
    # The expected correct substring:
    assert "Supply Chain and Delivery Commitment" in text, (
        "SS Cl. 5 heading 'Supply Chain and Delivery Commitment' must "
        "appear somewhere in the doc"
    )
    # And §8.1(b) specifically must reference it:
    lower = text.lower()
    # find the §8.1(b) binding-provisions line and assert it contains
    # the SS-correct phrase
    idx = lower.find("(b) binding provisions")
    assert idx != -1, "§8.1(b) line not found"
    snippet = text[idx:idx + 400]
    assert "Supply Chain and Delivery Commitment" in snippet, (
        f"SS §8.1(b) should reference 'Supply Chain and Delivery "
        f"Commitment' in Clause 5; actual snippet: {snippet!r}"
    )


@pytest.mark.parametrize("intake", [
    "intake_example_wholesale.yaml",
    "intake_example_distributor.yaml",
])
def test_bug2_ws_ds_cl8_1b_unchanged(intake):
    """WS + DS paths legitimately use 'Project Finance and Assignment'
    for Clause 5 — must not regress when fixing SS."""
    text = _render_text(_load(intake))
    assert "Project Finance and Assignment" in text


# ----- Bug 3: §8.9 "(ALT-A)" leak when no NDA ---------------------------

def test_bug3_no_alt_a_marker_when_no_existing_nda():
    """InfraPartners §4.2: §8.9 reads 'any NDA referenced in Clause 6
    (ALT-A)' even when choices.existing_nda is False. '(ALT-A)' is a
    drafting variant marker that must not leak to final output."""
    # Wholesale intake defaults to existing_nda: False
    data = _load("intake_example_wholesale.yaml")
    data.setdefault("choices", {})["existing_nda"] = False
    text = _render_text(data)
    assert "(ALT-A)" not in text, (
        "'(ALT-A)' drafting marker leaked into §8.9 body — must be "
        "stripped or gated on existing_nda"
    )


def test_bug3_alt_a_marker_also_absent_when_nda_true():
    """With existing_nda: true the '(ALT-A)' marker is still an engine-
    internal label, not customer-facing prose. Must not appear in either
    branch."""
    data = _load("intake_example_wholesale.yaml")
    data.setdefault("choices", {})["existing_nda"] = True
    text = _render_text(data)
    assert "(ALT-A)" not in text


# ----- Bug 4: Cl. 4.2 meta-commentary trailer (SS + WS) -----------------

_META_TRAILER = (
    "Each stage is designed to provide increasing commercial certainty"
)


@pytest.mark.parametrize("intake", [
    "intake_example_strategic_supplier.yaml",
    "intake_example_wholesale.yaml",
])
def test_bug4_no_meta_trailer_in_cl4_2(intake):
    """Armada §2.2: Cl. 4.2 ends with meta-commentary sentence 'Each
    stage is designed to provide increasing commercial certainty and to
    support Digital Energy's project finance activities.' — which R-22
    should catch but doesn't because it's in the template, not YAML-
    injected. Bug duplicated across SS (line ~1312) and WS (line ~1386)."""
    text = _render_text(_load(intake))
    assert _META_TRAILER not in text, (
        f"{intake}: Cl. 4.2 meta-commentary trailer still present"
    )


# ----- Bug 5: Double-period on Recital B --------------------------------

def test_bug5_no_double_period_recital_b():
    """Armada §2.3 + InfraPartners §4.3: engine appends literal '.' to
    counterparty.description without stripping existing trailing period.
    If YAML description already ends in '.', Recital B renders '..'"""
    data = _load("intake_example_wholesale.yaml")
    # Force a description that ends in a period (common pattern)
    data["counterparty"]["description"] = (
        "builds GPU clusters for frontier-lab workloads in EU jurisdictions."
    )
    text = _render_text(data)
    # Recital B line must not contain '..'
    for line in text.split("\n"):
        if line.startswith("(B)"):
            assert ".." not in line.replace("...", ""), (
                f"Recital B contains double-period: {line!r}"
            )
            break
    else:
        pytest.fail("Recital B line not found in rendered doc")


# ----- Bug 6: Double-period on SS Cl. 3.1(b) core_capability ------------

def test_bug6_no_double_period_ss_cl3_1b():
    """SS Cl. 3.1(b) at line ~1177 appends '.' to supplier.core_capability
    without stripping existing trailing period. Same class as bug 5."""
    data = _load("intake_example_strategic_supplier.yaml")
    data.setdefault("supplier", {})["core_capability"] = (
        "high-capacity liquid-cooling manufactured modules with integrated "
        "busway and monitoring."
    )
    text = _render_text(data)
    # Find the "(b) the Supplier would contribute..." line
    for line in text.split("\n"):
        if "(b) the" in line.lower() and "would contribute" in line.lower():
            assert ".." not in line.replace("...", ""), (
                f"SS Cl. 3.1(b) contains double-period: {line!r}"
            )
            break
    else:
        pytest.fail("SS Cl. 3.1(b) contribution line not found")


# ----- Bug 7: Preamble missing reg_number for Party 2 -------------------

def test_bug7_preamble_cp_reg_number_renders_without_reg_type():
    """InfraPartners §4.4: preamble §(2) omits counterparty reg_number if
    reg_type is absent. Party 1 has a KvK fallback; Party 2 has no
    parallel fallback. Fix: emit reg_number even when reg_type is empty
    (use a sensible 'company number' default)."""
    data = _load("intake_example_wholesale.yaml")
    data["counterparty"]["reg_number"] = "HRB 17714"
    data["counterparty"].pop("reg_type", None)  # no reg_type
    data["counterparty"]["jurisdiction"] = "Germany"
    data["counterparty"]["address"] = "Südring 11, 33106 Paderborn, Germany"
    text = _render_text(data)
    # The reg_number must appear in the Party 2 preamble line
    party2_lines = [l for l in text.split("\n") if l.startswith("(2)")]
    assert party2_lines, "Party 2 preamble line not found"
    assert "HRB 17714" in party2_lines[0], (
        f"Party 2 preamble should include reg_number even without "
        f"explicit reg_type; actual line: {party2_lines[0]!r}"
    )


def test_bug7_preamble_cp_reg_number_still_renders_with_reg_type():
    """Regression: when reg_type IS provided, the existing rendering
    must continue to work."""
    data = _load("intake_example_wholesale.yaml")
    data["counterparty"]["reg_type"] = "Handelsregister"
    data["counterparty"]["reg_number"] = "HRB 17714"
    data["counterparty"]["jurisdiction"] = "Germany"
    data["counterparty"]["address"] = "Südring 11, 33106 Paderborn, Germany"
    text = _render_text(data)
    party2_lines = [l for l in text.split("\n") if l.startswith("(2)")]
    assert party2_lines
    assert "Handelsregister" in party2_lines[0]
    assert "HRB 17714" in party2_lines[0]


# ----- Doc-only addition: auto-version output filename ------------------
# (Item b from v3.6.0 plan.) Tested via CLI smoke in tests/test_cli_*.py
# if added later; for now the engine-level change is just in main() which
# is not covered by unit tests. Flagged in CHANGELOG.


# ----- Doc-only addition: SKILL.md SS strategic-purpose table -----------
# (Item k.) Pure doc; verified by mirror-integrity if manifest tracks it.

# ----- Doc-only addition: DE signatory-title memo -----------------------
# (Item m.) Pure doc.
