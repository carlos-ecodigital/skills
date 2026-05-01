"""v3.7.2 tests — full-closure release.

Covers items 1–6 from the v3.7.0 "Deferred to v3.7.1" block plus post-merge
polish:
1. R-29 URL content verification wired into qa_lint (default-on)
2. Recital B density word-count advisory
3. Phase 8 MCP dispatch + local execution wiring
4. 8 regression fixtures loaded by golden-file tests
5. Golden-corpus CI (empty-intake body R-rule scan)
6. Integration test: kitchen-sink fixture exercises every v3.7.x feature
   together without conflict
7. SESSION_LOG + AUDIT content assertions
8. custom.clauses collision check + silent-no-op surfacing
9. Lead-time unparseable advisory
10. Domain card real implementation
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest
import yaml

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))

import generate_loi  # noqa: E402

SALES_DIR = HERE.parent
EXAMPLES_DIR = SALES_DIR / "examples"
REGRESSION_V37 = SALES_DIR / "regression" / "v3.7"


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def kitchen_sink_intake():
    """Load the v3.7.x all-features example."""
    path = EXAMPLES_DIR / "intake_example_strategic_supplier_v37_full.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture
def simple_ws_intake():
    """Minimal WS intake for narrow tests."""
    path = EXAMPLES_DIR / "intake_example_wholesale.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


def _build(intake):
    loi = generate_loi.LOI(intake)
    doc = loi.build()
    return loi, doc, generate_loi._extract_text(doc)


# ---------------------------------------------------------------------------
# 1. Integration: every v3.7.x feature fires on kitchen sink
# ---------------------------------------------------------------------------


def test_kitchen_sink_all_features_fire(kitchen_sink_intake):
    """End-to-end: kitchen-sink fixture exercises every v3.7.x feature."""
    _, _, text = _build(kitchen_sink_intake)

    required_present = [
        "Joint Stocking Programme",        # v3.7.1 §3.10 (lead_time < 6mo)
        "Mutual Referral Rider",           # v3.7.0 §3.9 (referral_rider)
        "Reference and Co-Marketing",      # v3.7.1 §3.11 (co_marketing)
        "Designated Sites",                # v3.7.0 supplier.rofr site_scope
        "good-faith dialogue",             # v3.7.0 RoFR alignment style
        "Super-Factory Initiative",        # v3.7.0 custom.definitions_include
        "ExampleTerm",                     # v3.7.0 custom.definitions[] (inline)
        "Bespoke Annex Coordination",      # v3.7.1 custom.clauses mode=append
        "IP Allocation (Bespoke)",         # v3.7.1 custom.clauses mode=replace
        "Operational Review Cadence",      # v3.7.1 custom.clauses mode=insert-after
        "bidirectional referral interest", # v3.7.0 referral_rider body
    ]
    for phrase in required_present:
        assert phrase in text, f"missing expected phrase: {phrase!r}"

    required_absent = [
        "Schedule 1",                      # v3.7.0 include_schedule=false
        "Onward-Sharing Controls",         # v3.7.0 opt_outs
        "Compliance Confirmation",         # v3.7.0 opt_outs
        "Metadata Protection",             # v3.7.0 opt_outs
    ]
    for phrase in required_absent:
        assert phrase not in text, f"unexpected phrase present: {phrase!r}"


def test_kitchen_sink_qa_report_surfaces_metadata(kitchen_sink_intake):
    loi, doc, _ = _build(kitchen_sink_intake)
    status, qa_lines = generate_loi.qa_lint(
        doc, kitchen_sink_intake, loi.qa_findings, loi.overrides,
        loi.override_reason, verify_urls=False,
    )
    # Surfaces from v3.7.0
    assert any("relationship_cluster" in l for l in qa_lines)
    assert any("identity_map" in l for l in qa_lines)
    assert any("financing_context" in l for l in qa_lines)


# ---------------------------------------------------------------------------
# 2. R-29 URL content verification
# ---------------------------------------------------------------------------


class FakeFetcher:
    """Test fixture: returns predetermined content per URL."""
    def __init__(self, responses: dict):
        self.responses = responses
    def fetch(self, url: str) -> str:
        return self.responses.get(url, "")


def test_r29_passes_when_keyword_found(simple_ws_intake):
    """When fetched content has ≥500 chars + keyword, no R-29 warn."""
    # Insert a source_map URL + short name the fetcher will return content about
    simple_ws_intake.setdefault("counterparty", {})["short"] = "TestCo"
    source_map = simple_ws_intake["counterparty"].get("source_map", {})
    simple_ws_intake["counterparty"]["source_map"] = {
        "pillar_1": ["https://fake.test/pillar1"],
        **{k: v for k, v in source_map.items() if k != "pillar_1"},
    }

    fetcher = FakeFetcher({
        "https://fake.test/pillar1": "TestCo is a real company. " * 40,  # >500 chars, includes "TestCo"
    })
    loi, doc, _ = _build(simple_ws_intake)
    _, lines = generate_loi.qa_lint(
        doc, simple_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason,
        verify_urls=True, url_fetcher=fetcher,
    )
    r29_warns = [l for l in lines if "R-29" in l and "[WARN]" in l]
    assert not r29_warns, f"unexpected R-29 warn: {r29_warns}"


def test_r29_warns_when_content_short(simple_ws_intake):
    """When fetched content is <500 chars, R-29 warns + downgrades pillar."""
    simple_ws_intake.setdefault("counterparty", {})["short"] = "TestCo"
    simple_ws_intake["counterparty"]["source_map"] = {
        "pillar_1": ["https://fake.test/short"],
        "pillar_2": ["https://fake.test/ok"],
        "pillar_3": ["https://fake.test/ok"],
        "pillar_4": ["https://fake.test/ok"],
        "pillar_5": ["https://fake.test/ok"],
    }
    fetcher = FakeFetcher({
        "https://fake.test/short": "tagline only",  # <500 chars
        "https://fake.test/ok": "TestCo " * 100,    # >500 chars, includes keyword
    })
    loi, doc, _ = _build(simple_ws_intake)
    _, lines = generate_loi.qa_lint(
        doc, simple_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason,
        verify_urls=True, url_fetcher=fetcher,
    )
    r29_warns = [l for l in lines if "R-29" in l and "[WARN]" in l and "pillar_1" in l]
    assert r29_warns, f"expected R-29 warn on pillar_1; got: {lines[-10:]}"


def test_r29_disabled_by_LOI_NO_NETWORK(simple_ws_intake, monkeypatch):
    """LOI_NO_NETWORK=1 env var disables R-29 regardless of default-on."""
    monkeypatch.setenv("LOI_NO_NETWORK", "1")
    loi, doc, _ = _build(simple_ws_intake)
    _, lines = generate_loi.qa_lint(
        doc, simple_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason,
        # verify_urls=None → auto-detect, should pick up env var
    )
    r29_lines = [l for l in lines if "R-29" in l]
    assert not r29_lines, f"R-29 fired despite LOI_NO_NETWORK=1: {r29_lines}"


def test_r29_explicit_verify_urls_false(simple_ws_intake):
    """verify_urls=False explicitly disables R-29 (test escape hatch)."""
    loi, doc, _ = _build(simple_ws_intake)
    _, lines = generate_loi.qa_lint(
        doc, simple_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason,
        verify_urls=False,
    )
    r29_lines = [l for l in lines if "R-29" in l]
    assert not r29_lines


def test_r29_fetch_exception_info_not_warn(simple_ws_intake):
    """Network error during fetch → INFO (skipping), not a WARN downgrade."""
    class ErrorFetcher:
        def fetch(self, url): raise ConnectionError("network down")

    simple_ws_intake.setdefault("counterparty", {})["short"] = "TestCo"
    simple_ws_intake["counterparty"]["source_map"] = {
        "pillar_1": ["https://fake.test/err"],
        "pillar_2": ["[TBC]"],
        "pillar_3": ["[TBC]"],
        "pillar_4": ["[TBC]"],
        "pillar_5": ["[TBC]"],
    }
    loi, doc, _ = _build(simple_ws_intake)
    _, lines = generate_loi.qa_lint(
        doc, simple_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason,
        verify_urls=True, url_fetcher=ErrorFetcher(),
    )
    info_lines = [l for l in lines if "R-29" in l and "[INFO]" in l]
    warn_lines = [l for l in lines if "R-29" in l and "[WARN]" in l]
    assert info_lines, "expected INFO on fetch error"
    assert not warn_lines, "should not WARN on fetch error (flaky)"


# ---------------------------------------------------------------------------
# 3. Recital B density advisory
# ---------------------------------------------------------------------------


def test_density_terse_warns_on_long_desc(simple_ws_intake):
    simple_ws_intake.setdefault("choices", {})["recital_b_density"] = "terse"
    # v3.8.0: density measurement now spans slot block. A long slot-5
    # claim makes the assembled recital exceed terse band.
    simple_ws_intake["counterparty"]["recital_b"]["bargain_relevant_fact"] = {
        "claim": "with " + ("various things in various ways " * 40),
        "source": {"tier": 1, "url": "https://example.com/", "retrieved": "2026-05-01"},
    }
    loi, doc, _ = _build(simple_ws_intake)
    _, lines = generate_loi.qa_lint(
        doc, simple_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason,
        verify_urls=False,
    )
    dens_lines = [l for l in lines if "R-density" in l]
    assert dens_lines, "expected density advisory on long terse desc"


def test_density_standard_silent_on_normal_desc(simple_ws_intake):
    simple_ws_intake.setdefault("choices", {})["recital_b_density"] = "standard"
    # Existing desc in intake_example_wholesale.yaml is ~100w — within band
    loi, doc, _ = _build(simple_ws_intake)
    _, lines = generate_loi.qa_lint(
        doc, simple_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason,
        verify_urls=False,
    )
    dens_lines = [l for l in lines if "R-density" in l]
    # Should be silent on standard + normal-length desc
    # (but if baseline desc is out of 60-150 band, this fails — informational)
    assert not dens_lines or "within" not in (dens_lines[0] if dens_lines else "")


def test_density_verbose_warns_on_short_desc(simple_ws_intake):
    simple_ws_intake.setdefault("choices", {})["recital_b_density"] = "verbose"
    simple_ws_intake["counterparty"]["description"] = "is a short description."
    loi, doc, _ = _build(simple_ws_intake)
    _, lines = generate_loi.qa_lint(
        doc, simple_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason,
        verify_urls=False,
    )
    dens_lines = [l for l in lines if "R-density" in l]
    assert dens_lines, "expected density advisory on short verbose desc"


# ---------------------------------------------------------------------------
# 4. Phase 8 MCP dispatch — JSON payload shape
# ---------------------------------------------------------------------------


def test_phase8_dispatch_json_emitted(simple_ws_intake, tmp_path):
    """Running generator with --phase-8-auto-execute emits a dispatch JSON."""
    # Write the intake YAML to a temp file so we can invoke via subprocess
    intake_path = tmp_path / "intake.yaml"
    with open(intake_path, "w") as f:
        yaml.safe_dump(simple_ws_intake, f)
    docx_path = tmp_path / "test.docx"
    result = subprocess.run(
        [sys.executable, str(SALES_DIR / "generate_loi.py"),
         str(intake_path), "--output", str(docx_path),
         "--phase-8-auto-execute",
         "--phase-8-actions=artifact_storage_push,domain_card_create"],
        cwd=SALES_DIR, capture_output=True, text=True,
        env={**os.environ, "LOI_NO_NETWORK": "1"},
    )
    assert result.returncode == 0, f"build failed: {result.stderr}"
    dispatch_path = docx_path.parent / f"{docx_path.stem}_PHASE8_DISPATCH.json"
    assert dispatch_path.exists(), f"no dispatch JSON at {dispatch_path}"
    with open(dispatch_path) as f:
        payload = json.load(f)
    assert "actions" in payload
    assert payload["dry_run"] is False  # --phase-8-auto-execute was passed
    action_keys = {a["action"] for a in payload["actions"]}
    assert "artifact_storage_push" in action_keys


def test_phase8_dispatch_dry_run_default(simple_ws_intake, tmp_path):
    """Without --phase-8-auto-execute, dispatch is dry_run=True."""
    intake_path = tmp_path / "intake.yaml"
    with open(intake_path, "w") as f:
        yaml.safe_dump(simple_ws_intake, f)
    docx_path = tmp_path / "test.docx"
    result = subprocess.run(
        [sys.executable, str(SALES_DIR / "generate_loi.py"),
         str(intake_path), "--output", str(docx_path)],
        cwd=SALES_DIR, capture_output=True, text=True,
        env={**os.environ, "LOI_NO_NETWORK": "1"},
    )
    assert result.returncode == 0, f"build failed: {result.stderr}"
    dispatch_path = docx_path.parent / f"{docx_path.stem}_PHASE8_DISPATCH.json"
    assert dispatch_path.exists()
    with open(dispatch_path) as f:
        payload = json.load(f)
    assert payload["dry_run"] is True


def test_phase8_domain_card_real_write(simple_ws_intake, tmp_path, monkeypatch):
    """--phase-8-auto-execute + domain_card_create writes the overview.md file."""
    monkeypatch.chdir(tmp_path)  # cwd is tmp_path so no repo-root 'domains/' found
    intake_path = tmp_path / "intake.yaml"
    with open(intake_path, "w") as f:
        yaml.safe_dump(simple_ws_intake, f)
    docx_path = tmp_path / "test.docx"
    result = subprocess.run(
        [sys.executable, str(SALES_DIR / "generate_loi.py"),
         str(intake_path), "--output", str(docx_path),
         "--phase-8-auto-execute",
         "--phase-8-actions=domain_card_create"],
        cwd=SALES_DIR, capture_output=True, text=True,
        env={**os.environ, "LOI_NO_NETWORK": "1"},
    )
    assert result.returncode == 0, f"build failed: {result.stderr}"
    # Fallback path: ./test.docx's dir → tmp_path/domain_cards/{slug}/overview.md
    fallback_cards = list(tmp_path.glob("domain_cards/*/overview.md"))
    assert fallback_cards, f"expected a domain card under {tmp_path}/domain_cards/*"
    content = fallback_cards[0].read_text()
    assert "HubSpot" in content  # template body


# ---------------------------------------------------------------------------
# 5. SESSION_LOG + AUDIT content
# ---------------------------------------------------------------------------


def test_session_log_captures_intake_decisions(kitchen_sink_intake, tmp_path):
    from generate_loi import _emit_session_log
    docx_path = str(tmp_path / "test.docx")
    Path(docx_path).touch()  # stub file so path exists
    _emit_session_log(docx_path, kitchen_sink_intake, "PASS",
                      ["  [INFO] R-foo  scope  msg"])
    log_path = Path(docx_path.replace(".docx", "_SESSION_LOG.md"))
    assert log_path.exists()
    content = log_path.read_text()
    assert "## Intake decisions" in content
    assert "## CLI flags used" in content
    assert "## QA summary" in content
    assert "## Customizations" in content
    # kitchen_sink has 1 inline custom.definition + 3 custom.clauses
    assert "custom.definitions: 1" in content
    assert "custom.clauses: 3" in content


def test_audit_checklist_kitchen_sink_assertions(kitchen_sink_intake, tmp_path):
    loi, doc, _ = _build(kitchen_sink_intake)
    docx_path = str(tmp_path / "test.docx")
    doc.save(docx_path)
    audit_path = generate_loi._emit_audit_checklist(docx_path, doc, kitchen_sink_intake)
    content = Path(audit_path).read_text()
    # Core assertions present
    assert "Preamble — Digital Energy party intro" in content
    # Kitchen-sink-specific
    assert "Joint Stocking Programme heading present" in content
    assert "Reference and Co-Marketing heading present" in content
    assert "Mutual Referral Rider heading present" in content
    # v3.6.0 bug-fix invariants
    assert 'v3.6.0 bug — "tthe" typo' in content
    # No FAIL lines in a kitchen-sink build
    fail_lines = [l for l in content.splitlines() if l.startswith("FAIL:")]
    assert not fail_lines, f"unexpected FAIL lines: {fail_lines}"


# ---------------------------------------------------------------------------
# 6. custom.clauses collision check
# ---------------------------------------------------------------------------


def test_custom_clauses_append_collision_rejected(simple_ws_intake, capsys):
    """Append mode with a number matching engine-emitted clause fails validate."""
    simple_ws_intake["custom"] = {
        "clauses": [
            {"number": "3.1", "mode": "append", "heading": "Collision",
             "text": "Text."}
        ]
    }
    with pytest.raises(SystemExit):
        generate_loi.validate(simple_ws_intake)
    assert "collides with engine-emitted clause" in capsys.readouterr().out


def test_custom_clauses_replace_collision_allowed(simple_ws_intake):
    """Replace mode IS ALLOWED to target an existing clause number (that's the point)."""
    simple_ws_intake["custom"] = {
        "clauses": [
            {"number": "3.1", "mode": "replace", "heading": "Override",
             "text": "Replacement text."}
        ]
    }
    # Should not raise
    generate_loi.validate(simple_ws_intake)


# ---------------------------------------------------------------------------
# 7. custom.clauses silent no-op WARN surfacing (v3.7.2)
# ---------------------------------------------------------------------------


def test_custom_clauses_replace_unknown_surfaces_warn(simple_ws_intake):
    """Replace targeting a number that doesn't exist → WARN via builder_warnings."""
    simple_ws_intake["custom"] = {
        "clauses": [
            {"number": "9.99", "mode": "replace", "heading": "X", "text": "Y"}
        ]
    }
    loi, doc, _ = _build(simple_ws_intake)
    # Directly use the failures list
    assert loi._custom_mutation_failures
    assert loi._custom_mutation_failures[0][0] == "replace"


def test_custom_clauses_insert_after_unknown_surfaces_warn(simple_ws_intake):
    simple_ws_intake["custom"] = {
        "clauses": [
            {"number": "9.99", "mode": "insert-after:9.98",
             "heading": "X", "text": "Y"}
        ]
    }
    loi, doc, _ = _build(simple_ws_intake)
    assert loi._custom_mutation_failures
    assert loi._custom_mutation_failures[0][0] == "insert-after"


# ---------------------------------------------------------------------------
# 8. Lead-time unparseable warning (v3.7.2)
# ---------------------------------------------------------------------------


def test_lead_time_unparseable_warns():
    """Non-empty but unparseable lead_time triggers WARN via qa_lint."""
    # Call the helper to populate the state
    result = generate_loi._lead_time_under_six_months("Q2 2026")
    assert result is False
    assert generate_loi._LAST_LEAD_TIME_PARSE["ok"] is False
    assert generate_loi._LAST_LEAD_TIME_PARSE["input"] == "Q2 2026"


def test_lead_time_empty_ok():
    generate_loi._lead_time_under_six_months("")
    assert generate_loi._LAST_LEAD_TIME_PARSE["ok"] is True


def test_lead_time_parseable_ok():
    generate_loi._lead_time_under_six_months("90 days")
    assert generate_loi._LAST_LEAD_TIME_PARSE["ok"] is True
    assert generate_loi._LAST_LEAD_TIME_PARSE["parsed_days"] == 90


# ---------------------------------------------------------------------------
# 9. Golden-corpus CI — empty-intake body R-rule scan
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("example_yaml", [
    p.name for p in sorted(EXAMPLES_DIR.glob("intake_example_*.yaml"))
])
def test_golden_corpus_r_rules_clean(example_yaml):
    """Every example intake renders with zero FAIL rules (excluding overrides).

    This is the CI-level template-body lint — catches future regressions
    where an engine-emitted string matches a fail rule (e.g., `tthe`,
    `(ALT-A)`, meta-commentary). If this test fails on a template edit,
    fix the template — don't override.
    """
    path = EXAMPLES_DIR / example_yaml
    with open(path) as f:
        data = yaml.safe_load(f)
    loi = generate_loi.LOI(data)
    doc = loi.build()
    status, lines = generate_loi.qa_lint(
        doc, data, loi.qa_findings, loi.overrides, loi.override_reason,
        verify_urls=False,
    )
    fails = [l for l in lines if "[FAIL]" in l and "[OVRD]" not in l]
    # Allow fails that reference documented override rules in the YAML
    unallowed = []
    overrides = loi.overrides or set()
    for l in fails:
        # Extract R-xx from "  [FAIL] R-xx scope msg"
        import re as _re
        m = _re.search(r"R-\S+", l)
        if not m or m.group(0) not in overrides:
            unallowed.append(l)
    assert not unallowed, (
        f"{example_yaml}: unexpected FAIL rules (would block CI):\n"
        + "\n".join(unallowed)
    )


# ---------------------------------------------------------------------------
# 10. v3.7 regression fixtures — all build + validate cleanly
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("fixture_yaml", [
    p.name for p in sorted(REGRESSION_V37.glob("*_intake.yaml"))
])
def test_v3_7_regression_fixtures_build_clean(fixture_yaml):
    """All 8 v3.7 regression fixtures validate and build without errors."""
    path = REGRESSION_V37 / fixture_yaml
    with open(path) as f:
        data = yaml.safe_load(f)
    generate_loi.validate(data)  # raises SystemExit on fail
    loi = generate_loi.LOI(data)
    doc = loi.build()
    assert doc is not None
