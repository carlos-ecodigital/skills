"""M6 — MDCS end-to-end verification (Pipeline A, Bespoke type).

Runs the committed `examples/intake_example_bespoke_mdcs.yaml` through
`generate_loi.py` and asserts the output is structurally correct:
  - builds without error
  - QA gate passes (no FAIL rules)
  - 9 clauses present with Heading 1 style
  - footer version stamp DE-LOI-Bespoke-v1.0
  - audit_agreement (document-factory, M2) returns 0 R-21 and 0
    placeholder violations

Pipeline B verification (rebrand on a real MDCS .docx) is not covered
here because it requires an external input file. Use
`document-factory/tools/m6_verify_rebrand.py <input.docx>` to exercise
that path against any MDCS-shape document.
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

_COLOCATION = Path(__file__).resolve().parent.parent
_DOC_FACTORY = _COLOCATION.parent.parent / "document-factory"
_FIXTURE = _COLOCATION / "examples" / "intake_example_bespoke_mdcs.yaml"

sys.path.insert(0, str(_DOC_FACTORY))
sys.path.insert(0, str(_COLOCATION))

_spec = importlib.util.spec_from_file_location(
    "generate_loi", str(_COLOCATION / "generate_loi.py")
)
generate_loi = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(generate_loi)

from audit_profiles import audit_agreement  # noqa: E402


@pytest.fixture
def mdcs_intake() -> dict:
    # Explicit UTF-8 — CI runners may not default to it, and the fixture
    # contains non-ASCII (curly quotes, en-dashes in recital text).
    with open(_FIXTURE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_mdcs_fixture_exists() -> None:
    assert _FIXTURE.exists(), f"Missing M6 fixture: {_FIXTURE}"


def test_mdcs_fixture_type_is_bespoke(mdcs_intake: dict) -> None:
    assert mdcs_intake["type"] == "Bespoke"


def test_mdcs_intake_validates(mdcs_intake: dict) -> None:
    """MDCS Bespoke YAML passes the validator without raising SystemExit."""
    try:
        generate_loi.validate(mdcs_intake)
    except SystemExit as e:
        pytest.fail(f"validate() raised SystemExit: {e}")


def test_mdcs_loi_builds(mdcs_intake: dict) -> None:
    """MDCS Bespoke LOI builds a Document without errors."""
    loi = generate_loi.LOI(mdcs_intake)
    doc = loi.build()
    assert doc is not None
    # 9 clauses expected (numbered 1–9). Exact match on style name so
    # future "Heading 10" / "Heading 1 Continued" styles don't silently
    # inflate the count.
    headings = [p.text for p in doc.paragraphs if p.style.name == "Heading 1"]
    assert len(headings) == 9, (
        f"Expected 9 Heading 1 clauses, got {len(headings)}:\n" + "\n".join(headings)
    )
    # Clause 1 must be the joint-offering clause (the defining bespoke element).
    assert "Partnership Model and Joint Offering" in headings[0]


def test_mdcs_footer_version_stamp(mdcs_intake: dict) -> None:
    """MDCS Bespoke output's footer stamps DE-LOI-Bespoke-v1.0."""
    doc = generate_loi.LOI(mdcs_intake).build()
    texts = [p.text for p in doc.paragraphs]
    assert any("DE-LOI-Bespoke-v1.0" in t for t in texts), (
        "Expected 'DE-LOI-Bespoke-v1.0' in body footer. "
        f"Last paragraphs: {texts[-5:]}"
    )


def test_mdcs_qa_gate_passes(mdcs_intake: dict) -> None:
    """MDCS Bespoke output passes the QA gate (no FAIL rules)."""
    doc = generate_loi.LOI(mdcs_intake).build()
    status, report = generate_loi.qa_lint(
        doc, mdcs_intake,
        builder_findings=[],
        overrides=set(),
        override_reason="",
    )
    assert status in ("PASS", "PASS_WITH_WARN"), (
        f"QA gate did not pass. status={status}\n" + "\n".join(report)
    )
    assert not any("[FAIL]" in line for line in report), (
        "FAIL marker in QA report:\n" + "\n".join(report)
    )


def test_mdcs_audit_agreement_clean(mdcs_intake: dict) -> None:
    """MDCS Bespoke output passes document-factory's audit_agreement
    (no R-21 party duplication, no placeholder tokens)."""
    doc = generate_loi.LOI(mdcs_intake).build()
    vios = audit_agreement(doc)
    r21 = [v for v in vios if "R-21" in v]
    placeholder = [v for v in vios if "placeholder" in v]
    assert not r21, f"R-21 fired on Bespoke MDCS output: {r21}"
    assert not placeholder, f"Placeholder fired on Bespoke MDCS output: {placeholder}"


def test_mdcs_cli_smoke_regenerates_cleanly(tmp_path: Path) -> None:
    """Matches the CI smoke step: `python3 generate_loi.py <fixture>`
    runs to completion with exit code 0 and emits a .docx + _qa.txt."""
    # Run in a temp cwd so the generated files don't pollute the repo.
    result = subprocess.run(
        [
            sys.executable,
            str(_COLOCATION / "generate_loi.py"),
            str(_FIXTURE),
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"generate_loi.py exited {result.returncode}\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )
    docx = list(tmp_path.glob("*LOI-Bespoke_MDCS*.docx"))
    qa_txt = list(tmp_path.glob("*_qa.txt"))
    assert docx, f"No .docx produced. Files: {os.listdir(tmp_path)}"
    assert qa_txt, "No QA report produced"
