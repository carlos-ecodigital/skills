"""v3.7.3 advisor-feedback regression tests.

Three changes from board-advisor (Santiago) review of the Polarise
Wholesale LOI on 2026-04-23, refined with Jelmer + Carlos on
2026-04-28:

  Point 1 (WS Cl. 4.2(b)) — Sales Order Form reframed as a non-binding
    capacity and pricing summary prepared during technical scoping, so
    that 4.1, 4.2, and 4.6 reconcile (capacity is only reserved at MSA
    execution).

  Point 2 (Cl. 5.3, all NCNDA types + SS variant) — Lender direct
    agreement language tightened from open-ended ("may include") to a
    closed list ("shall be limited to") with an explicit no-worse-off
    carve-out covering pricing, service levels, liability profile,
    indemnity scope, and payment obligations. Step-in and substitution
    rights are bounded to performance of Provider's obligations under
    the MSA / Framework Agreement.

  Point 4a (Cl. 7.3, all NCNDA types + DS Cl. 4.3 cross-reference) —
    Deemed Introduction reframed as Deemed Introduction by Category
    with a 10-Business-Day named-list backstop on Customer's written
    request, so that the Customer can ascertain the universe of
    off-limits parties without DE bearing per-LOI individual-naming
    overhead.

Per PRINCIPLES.md #4: render-logic changes ship with tests that
exercise the new branch.
"""
from __future__ import annotations

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
    """Concatenate all rendered body text (paragraphs + table cells)."""
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


# ----- Point 1: WS Cl. 4.2(b) SOF non-binding ---------------------------

def test_point1_ws_sof_non_binding():
    """Wholesale Cl. 4.2(b) must describe SOF as a non-binding capacity
    and pricing summary, not a binding capacity commitment."""
    data = _load("intake_example_wholesale.yaml")
    text = _render_text(data)
    assert "non-binding capacity and pricing summary" in text, (
        "Cl. 4.2(b) must describe SOF as non-binding planning instrument"
    )
    assert "binding capacity commitment" not in text, (
        "Pre-v3.7.3 'binding capacity commitment' phrasing must be removed"
    )


def test_point1_only_affects_wholesale():
    """Cl. 4.2(b) reframing applies only to the Wholesale variant; EU
    has no SOF clause, DS uses a different Cl. 4 structure, and SS / EP
    use Framework Agreement / IP-and-Deliverables respectively."""
    for intake in [
        "intake_example_enduser.yaml",
        "intake_example_distributor.yaml",
        "intake_example_strategic_supplier.yaml",
        "intake_example_ecosystem_partnership.yaml",
    ]:
        data = _load(intake)
        text = _render_text(data)
        assert "non-binding capacity and pricing summary" not in text, (
            f"{intake}: Wholesale-only SOF reframing must not leak"
        )


# ----- Point 2: Cl. 5.3 closed-list lender language ---------------------

@pytest.mark.parametrize("intake", [
    "intake_example_wholesale.yaml",
    "intake_example_distributor.yaml",
    "intake_example_enduser.yaml",
])
def test_point2_lender_closed_list(intake):
    """Cl. 5.3 must use the closed-list 'shall be limited to' formulation
    rather than the open-ended pre-v3.7.3 'may include'."""
    data = _load(intake)
    text = _render_text(data)
    assert "shall be limited to the following customary items only" in text, (
        f"{intake}: Cl. 5.3 must use closed-list formulation"
    )
    assert "may include, as is customary in project finance" not in text, (
        f"{intake}: pre-v3.7.3 open-ended 'may include' formulation must be removed"
    )


@pytest.mark.parametrize("intake", [
    "intake_example_wholesale.yaml",
    "intake_example_distributor.yaml",
    "intake_example_enduser.yaml",
    "intake_example_strategic_supplier.yaml",
])
def test_point2_no_worse_off_carve_out(intake):
    """Cl. 5.3 must include the no-worse-off carve-out covering pricing,
    service levels, liability profile, indemnity scope, and payment
    obligations (advisor's required protection plus Jelmer's
    indemnity-scope addition)."""
    data = _load(intake)
    text = _render_text(data)
    assert "without the" in text and "separate written consent" in text, (
        f"{intake}: Cl. 5.3 must require Customer separate written consent"
    )
    for required in ["pricing", "service levels", "liability profile",
                     "indemnity scope", "payment obligations"]:
        assert required in text, (
            f"{intake}: Cl. 5.3 carve-out must include '{required}'"
        )


@pytest.mark.parametrize("intake", [
    "intake_example_wholesale.yaml",
    "intake_example_distributor.yaml",
    "intake_example_enduser.yaml",
])
def test_point2_step_in_bounded(intake):
    """Cl. 5.3(c) must bound step-in and substitution rights to
    performance of Provider's obligations under the MSA, not an
    open-ended grant."""
    data = _load(intake)
    text = _render_text(data)
    assert "step-in and substitution rights" in text
    assert "limited to the performance of Digital Energy's obligations under the MSA" in text, (
        f"{intake}: Cl. 5.3(c) step-in/substitution must be MSA-bounded"
    )


def test_point2_ss_step_in_bounded_to_framework_agreement():
    """SS Cl. 5.3 (Financing Continuity Acknowledgment) must bound
    step-in to performance of obligations under the Framework Agreement
    (the SS-equivalent of MSA)."""
    data = _load("intake_example_strategic_supplier.yaml")
    text = _render_text(data)
    assert "limited to the performance of Digital Energy's obligations under the Framework Agreement" in text, (
        "SS Cl. 5.3 step-in/substitution must be Framework-Agreement-bounded"
    )


# ----- Point 4a: Cl. 7.3 Deemed Introduction by Category ----------------

@pytest.mark.parametrize("intake", [
    "intake_example_wholesale.yaml",
    "intake_example_distributor.yaml",
    "intake_example_strategic_supplier.yaml",
])
def test_point4a_deemed_introduction_by_category_heading(intake):
    """Cl. 7.3 heading must be 'Deemed Introduction by Category', not
    plain 'Deemed Introduction'."""
    data = _load(intake)
    text = _render_text(data)
    assert "Deemed Introduction by Category" in text, (
        f"{intake}: Cl. 7.3 heading must be 'Deemed Introduction by Category'"
    )


@pytest.mark.parametrize("intake", [
    "intake_example_wholesale.yaml",
    "intake_example_distributor.yaml",
    "intake_example_strategic_supplier.yaml",
])
def test_point4a_named_list_backstop(intake):
    """Cl. 7.3 must include the 10-Business-Day named-list backstop on
    Customer's written request."""
    data = _load(intake)
    text = _render_text(data)
    assert "ten (10) Business Days" in text, (
        f"{intake}: Cl. 7.3 must include the 10-Business-Day name-list backstop"
    )
    assert "list of the named Associated Counterparties" in text, (
        f"{intake}: Cl. 7.3 must reference the named-list provision"
    )


def test_point4a_distributor_4_3_cross_references_7_3():
    """Distributor Cl. 4.3 must defer to Cl. 7.3 for the deemed-
    introduction mechanic, rather than repeating the old 'all
    Associated Counterparties for that site' formulation inline."""
    data = _load("intake_example_distributor.yaml")
    text = _render_text(data)
    assert "Clause 7.3" in text, (
        "DS Cl. 4.3 must cross-reference Cl. 7.3"
    )


def test_point4a_no_old_unconditional_deemed_introduction():
    """The pre-v3.7.3 'deemed introduction of all Associated
    Counterparties for that site. Digital Energy is not required to
    separately name' formulation must no longer appear in any rendered
    LOI body."""
    for intake in [
        "intake_example_wholesale.yaml",
        "intake_example_distributor.yaml",
        "intake_example_strategic_supplier.yaml",
    ]:
        data = _load(intake)
        text = _render_text(data)
        assert "not required to separately name each" not in text, (
            f"{intake}: pre-v3.7.3 unconditional deemed-introduction phrasing leaked"
        )
