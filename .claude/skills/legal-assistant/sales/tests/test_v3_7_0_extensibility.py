"""v3.7.0 extensibility tests — YAML schema additions + engine behaviors.

Test-first per PRINCIPLES.md #4. Covers:
- Schema validation for new optional fields
- Confidentiality opt-outs + renumbering
- supplier.rofr parameterization (alignment / hard_minimum / milestone)
- supplier.referral_rider
- choices.include_schedule=false
- custom.definitions[] + custom.definitions_include[]
- custom.clauses[] (append mode)
- QA report surfaces for relationship_cluster / identity_map / financing_context
- scripts/phase8_actions.py dispatch payloads
- scripts/artifact_storage.py dry-run
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

import pytest

HERE = Path(__file__).parent
ENGINE = HERE.parent / "generate_loi.py"
SKILL_ROOT = HERE.parent.parent  # .../legal-assistant

# Make the colocation dir importable.
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(SKILL_ROOT))

import generate_loi  # noqa: E402


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def base_ss_intake():
    """Minimal Strategic Supplier intake — used as a base for all v3.7.0 tests."""
    return {
        "type": "StrategicSupplier",
        "provider": {
            "legal_name": "Digital Energy Netherlands B.V.",
            "short": "Digital Energy",
            "jurisdiction": "the Netherlands",
            "reg_type": "KvK",
            "reg_number": "[TBC]",
            "address": "[TBC]",
        },
        "counterparty": {
            "name": "TestSupplier Ltd.",
            "short": "TestSupplier",
            # v3.8.0: `description` removed; using slot block.
            "recital_b": {
                "legal_identity": {
                    "legal_form": "Ltd",
                    "jurisdiction": "United Kingdom",
                    "registration": {"type": "Companies House", "number": "[TBC]"},
                    "source": {"tier": 1, "url": "[TBC]", "retrieved": "2026-05-01"},
                },
                "operational_verb": {
                    "verb": "manufacturing",
                    "object": "modular data-centre infrastructure",
                    "source": {"tier": 1, "url": "[TBC]", "retrieved": "2026-05-01"},
                },
                "customer_use_case": {
                    "category": "data-centre operators",
                    "source": {"tier": 1, "url": "[TBC]", "retrieved": "2026-05-01"},
                },
                "material_asset": {
                    "asset": "Manchester manufacturing facility",
                    "source": {"tier": 1, "url": "[TBC]", "retrieved": "2026-05-01"},
                },
            },
            "jurisdiction": "the United Kingdom",
            "reg_number": "[TBC]",
            "address": "[TBC]",
            "contact_name": "Alex Contact",
            "signatory_name": "Sam Signatory",
            "signatory_title": "[TBC]",
            "source_map": {
                "pillar_1": ["https://example.com/about"],
                "pillar_2": ["https://example.com/products"],
                "pillar_3": ["https://example.com/customers"],
                "pillar_4": ["https://example.com/strategy"],
                "pillar_5": ["https://example.com/pipeline"],
            },
        },
        "programme": {
            "recital_a_variant": "default",
        },
        "dates": {
            "loi_date": "20 April 2026",
            "validity_date": "20 April 2027",
        },
        "supplier": {
            "capability_category": "modular_infrastructure",
            "core_capability": "Factory-built data-centre modules",
            "strategic_purposes": ["pipeline_visibility"],
        },
        "choices": {
            "joint_ip": "background",
            "exclusivity": False,
        },
    }


@pytest.fixture
def base_ws_intake():
    """Minimal Wholesale intake."""
    return {
        "type": "Wholesale",
        "provider": {
            "legal_name": "Digital Energy Netherlands B.V.",
            "short": "Digital Energy",
            "jurisdiction": "the Netherlands",
            "reg_type": "KvK",
            "reg_number": "[TBC]",
            "address": "[TBC]",
        },
        "counterparty": {
            "name": "TestCustomer Ltd.",
            "short": "TestCustomer",
            # v3.8.0: `description` field removed; using slot block.
            "recital_b": {
                "legal_identity": {
                    "legal_form": "Ltd",
                    "jurisdiction": "United Kingdom",
                    "registration": {"type": "Companies House", "number": "[TBC]"},
                    "source": {"tier": 1, "url": "[TBC]", "retrieved": "2026-05-01"},
                },
                "operational_verb": {
                    "verb": "providing",
                    "object": "AI compute services",
                    "source": {"tier": 1, "url": "[TBC]", "retrieved": "2026-05-01"},
                },
                "customer_use_case": {
                    "category": "AI workloads",
                    "source": {"tier": 1, "url": "[TBC]", "retrieved": "2026-05-01"},
                },
                "material_asset": {
                    "asset": "London office",
                    "source": {"tier": 1, "url": "[TBC]", "retrieved": "2026-05-01"},
                },
            },
            "jurisdiction": "the United Kingdom",
            "reg_number": "[TBC]",
            "address": "[TBC]",
            "signatory_name": "Sam Signatory",
            "signatory_title": "[TBC]",
            "source_map": {
                "pillar_1": ["https://example.com/about"],
                "pillar_2": ["https://example.com/products"],
                "pillar_3": ["https://example.com/customers"],
                "pillar_4": ["https://example.com/strategy"],
                "pillar_5": ["https://example.com/pipeline"],
            },
        },
        "programme": {"recital_a_variant": "default"},
        "dates": {
            "loi_date": "20 April 2026",
            "validity_date": "20 April 2027",
        },
        "commercial": {
            "indicative_mw": "10 MW IT",
        },
        "choices": {},
    }


def _build(intake):
    """Build + return rendered text for a given intake."""
    loi = generate_loi.LOI(intake)
    doc = loi.build()
    return loi, doc, generate_loi._extract_text(doc)


# ---------------------------------------------------------------------------
# Schema validation
# ---------------------------------------------------------------------------


def test_v3_7_0_include_schedule_valid_bool(base_ws_intake):
    """choices.include_schedule accepts True or False."""
    base_ws_intake["choices"] = {"include_schedule": False}
    generate_loi.validate(base_ws_intake)  # should not exit


def test_v3_7_0_include_schedule_rejects_non_bool(base_ws_intake, capsys):
    base_ws_intake["choices"] = {"include_schedule": "yes"}
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    assert "include_schedule must be a boolean" in capsys.readouterr().out


def test_v3_7_0_confidentiality_opt_outs_valid_keys(base_ws_intake):
    base_ws_intake["choices"] = {
        "confidentiality_opt_outs": ["onward_sharing", "metadata_protection"]
    }
    generate_loi.validate(base_ws_intake)


def test_v3_7_0_confidentiality_opt_outs_rejects_unknown(base_ws_intake, capsys):
    base_ws_intake["choices"] = {"confidentiality_opt_outs": ["bogus_key"]}
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    assert "invalid key 'bogus_key'" in capsys.readouterr().out


def test_v3_7_0_supplier_rofr_ss_only(base_ws_intake, capsys):
    """supplier.rofr is only valid for StrategicSupplier type."""
    base_ws_intake["supplier"] = {"rofr": {"lock_out_style": "alignment"}}
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    assert "supplier.rofr is only valid" in capsys.readouterr().out


def test_v3_7_0_supplier_rofr_lock_out_style(base_ss_intake, capsys):
    base_ss_intake["supplier"]["rofr"] = {"lock_out_style": "invalid_style"}
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ss_intake)
    assert "lock_out_style must be one of" in capsys.readouterr().out


def test_v3_7_0_referral_rider_ss_only(base_ws_intake, capsys):
    base_ws_intake["supplier"] = {"referral_rider": True}
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    assert "supplier.referral_rider is only valid" in capsys.readouterr().out


def test_v3_7_0_custom_definitions_shape(base_ws_intake, capsys):
    base_ws_intake["custom"] = {"definitions": [{"key": "Foo"}]}  # missing text
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    assert "must have 'key' and 'text'" in capsys.readouterr().out


def test_v3_7_0_custom_clauses_mode(base_ws_intake, capsys):
    base_ws_intake["custom"] = {
        "clauses": [
            {"number": "3.X", "text": "...", "mode": "wrongmode"}
        ]
    }
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    assert "mode must be one of" in capsys.readouterr().out


def test_v3_7_0_financing_context_requires_target(base_ws_intake, capsys):
    base_ws_intake["dates"]["financing_context"] = {
        "linked_to_fundraise": True,
        # missing fundraise_close_target AND buffer_months_post_close
    }
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    out = capsys.readouterr().out
    assert "fundraise_close_target required" in out
    assert "buffer_months_post_close required" in out


# ---------------------------------------------------------------------------
# Confidentiality opt-outs behavior
# ---------------------------------------------------------------------------


def test_v3_7_0_opt_out_onward_sharing(base_ws_intake):
    """Opt-out of onward_sharing removes §6.9 Onward-Sharing Controls text.

    Remaining sub-clauses renumber sequentially (no gap at 6.9).
    """
    base_ws_intake["choices"]["confidentiality_opt_outs"] = ["onward_sharing"]
    _, _, text = _build(base_ws_intake)
    assert "Onward-Sharing Controls" not in text
    # §6.9 still exists (but now points to what was §6.10 Compliance Confirmation)
    assert "6.9 Compliance Confirmation" in text


def test_v3_7_0_opt_out_three_suppresses_all(base_ws_intake):
    """Opting out of all three renumbers cleanly to 13 sub-clauses."""
    base_ws_intake["choices"]["confidentiality_opt_outs"] = [
        "onward_sharing", "compliance_confirmation", "metadata_protection"
    ]
    _, _, text = _build(base_ws_intake)
    assert "Onward-Sharing Controls" not in text
    assert "Compliance Confirmation" not in text
    assert "Metadata Protection" not in text
    # 13 mandatory sub-clauses + 0 optional — last should be 6.13
    assert "6.13 Remedies" in text
    # §6.14 should not exist (original 16-clause structure implied it)
    assert "6.14" not in text


def test_v3_7_0_opt_out_none_preserves_16_clauses(base_ws_intake):
    """When opt_outs is empty, original 16-sub-clause rendering is preserved."""
    _, _, text = _build(base_ws_intake)
    assert "Onward-Sharing Controls" in text
    assert "Compliance Confirmation" in text
    assert "Metadata Protection" in text
    assert "6.16 Remedies" in text


# ---------------------------------------------------------------------------
# supplier.rofr parameterization
# ---------------------------------------------------------------------------


def test_v3_7_0_rofr_alignment_style(base_ss_intake):
    base_ss_intake["supplier"]["rofr"] = {
        "site_scope": "1-3 Designated Sites",
        "response_window": "20 Business Days",
        "lock_out_style": "alignment",
        "continues_on_remaining": True,
    }
    _, _, text = _build(base_ss_intake)
    assert "1-3 Designated Sites" in text
    assert "good-faith dialogue" in text
    assert "continue to apply to any remaining Designated Sites" in text


def test_v3_7_0_rofr_sole_discretion_default(base_ss_intake):
    """Default lock_out_style is sole_discretion — no alignment text."""
    _, _, text = _build(base_ss_intake)
    assert "good-faith dialogue" not in text
    assert "active development pipeline" in text  # default site_scope


def test_v3_7_0_rofr_hard_minimum(base_ss_intake):
    base_ss_intake["supplier"]["rofr"] = {"lock_out_style": "hard_minimum"}
    _, _, text = _build(base_ss_intake)
    assert "not fewer than one Designated Site" in text


def test_v3_7_0_rofr_milestone(base_ss_intake):
    base_ss_intake["supplier"]["rofr"] = {"lock_out_style": "milestone"}
    _, _, text = _build(base_ss_intake)
    assert "pre-commitment deliverables" in text


# ---------------------------------------------------------------------------
# supplier.referral_rider
# ---------------------------------------------------------------------------


def test_v3_7_0_referral_rider_adds_clause(base_ss_intake):
    base_ss_intake["supplier"]["referral_rider"] = True
    _, _, text = _build(base_ss_intake)
    assert "Mutual Referral Rider" in text
    assert "bidirectional referral interest" in text


def test_v3_7_0_referral_rider_default_off(base_ss_intake):
    _, _, text = _build(base_ss_intake)
    assert "Mutual Referral Rider" not in text


# ---------------------------------------------------------------------------
# include_schedule
# ---------------------------------------------------------------------------


def test_v3_7_0_include_schedule_false_omits_schedule(base_ws_intake):
    base_ws_intake["choices"]["include_schedule"] = False
    _, _, text = _build(base_ws_intake)
    # Schedule 1 heading should not appear
    assert "Schedule 1" not in text


def test_v3_7_0_include_schedule_false_scrubs_reference(base_ws_intake):
    base_ws_intake["choices"]["include_schedule"] = False
    _, _, text = _build(base_ws_intake)
    # §8.1(a) should not say "and Schedule 1"
    assert "and Schedule 1 of this LOI are non-binding" not in text
    assert "Clauses 2 through 4 of this LOI are non-binding" in text


def test_v3_7_0_include_schedule_false_scrubs_42d(base_ws_intake):
    """§4.2(d) drops 'schedules, or operational annexes' when schedule omitted."""
    base_ws_intake["choices"]["include_schedule"] = False
    _, _, text = _build(base_ws_intake)
    assert "schedules, or operational annexes" not in text


def test_v3_7_0_include_schedule_true_default(base_ws_intake):
    """Default include_schedule=True preserves v3.6.0 behavior."""
    _, _, text = _build(base_ws_intake)
    assert "Schedule 1" in text


# ---------------------------------------------------------------------------
# custom.definitions[] + definitions_include[]
# ---------------------------------------------------------------------------


def test_v3_7_0_custom_definitions_injected(base_ws_intake):
    base_ws_intake["custom"] = {
        "definitions": [
            {"key": "Widget Program",
             "text": "means the bespoke programme described in Annex Z."},
        ]
    }
    _, _, text = _build(base_ws_intake)
    assert "Widget Program" in text
    assert "bespoke programme described in Annex Z" in text


def test_v3_7_0_definitions_include_loads_library(base_ws_intake):
    """definitions_include pulls from _shared/loi-common-defined-terms.md."""
    library = generate_loi._load_common_defined_terms()
    if not library:
        pytest.skip("Common defined-terms library not found in this layout.")
    # Super-Factory Initiative is the canonical entry.
    assert "super_factory_initiative" in library
    assert "Super-Factory Initiative" in library["super_factory_initiative"]["name"]


def test_v3_7_0_custom_clauses_append(base_ws_intake):
    base_ws_intake["custom"] = {
        "clauses": [
            {"number": "9.1", "mode": "append", "heading": "Custom Trailer",
             "text": "This is a custom trailing clause for testing."}
        ]
    }
    _, _, text = _build(base_ws_intake)
    assert "Custom Trailer" in text
    assert "custom trailing clause for testing" in text


# ---------------------------------------------------------------------------
# QA report surfaces
# ---------------------------------------------------------------------------


def test_v3_7_0_qa_surfaces_relationship_cluster(base_ws_intake):
    base_ws_intake["counterparty"]["relationship_cluster"] = {
        "group_id": "test-group-1",
        "primary_entity": "TestCustomer Ltd.",
        "affiliated_entities": [
            {"name": "Related Supplier Co.", "role": "EPC supplier"},
        ],
    }
    loi, doc, _ = _build(base_ws_intake)
    status, qa_lines = generate_loi.qa_lint(
        doc, base_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason
    )
    assert any("relationship_cluster" in l and "test-group-1" in l for l in qa_lines)


def test_v3_7_0_qa_surfaces_identity_map(base_ws_intake):
    base_ws_intake["counterparty"]["identity_map"] = {
        "sam_signatory": {
            "display_name": "Sam Signatory",
            "email_domains": [{"domain": "example.com", "role": "primary"}],
        }
    }
    loi, doc, _ = _build(base_ws_intake)
    _, qa_lines = generate_loi.qa_lint(
        doc, base_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason
    )
    assert any("identity_map: 1 person" in l for l in qa_lines)


def test_v3_7_0_qa_surfaces_financing_context(base_ws_intake):
    base_ws_intake["dates"]["financing_context"] = {
        "linked_to_fundraise": True,
        "fundraise_close_target": "2026-12-31",
        "buffer_months_post_close": 9,
    }
    loi, doc, _ = _build(base_ws_intake)
    _, qa_lines = generate_loi.qa_lint(
        doc, base_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason
    )
    assert any("financing_context" in l and "2026-12-31" in l for l in qa_lines)


def test_v3_7_0_qa_surfaces_certifications(base_ws_intake):
    """R-11 helper surfaces detected certs in QA report."""
    base_ws_intake["counterparty"]["description"] = (
        "AI compute customer holding ISO 27001 certification."
    )
    loi, doc, _ = _build(base_ws_intake)
    _, qa_lines = generate_loi.qa_lint(
        doc, base_ws_intake, loi.qa_findings, loi.overrides, loi.override_reason
    )
    assert any("ISO" in l and "certifications_detected" in l for l in qa_lines)


# ---------------------------------------------------------------------------
# scripts/phase8_actions.py dispatch payloads
# ---------------------------------------------------------------------------


@pytest.fixture
def phase8_intake():
    return {
        "type": "Wholesale",
        "counterparty": {"name": "Acme Corp", "domain": "acme.com"},
        "dates": {"loi_date": "20 April 2026"},
    }


def test_phase8_hubspot_payload(phase8_intake):
    """v3.7.4 update: bare call (no dedup_decision) now returns a SEARCH
    payload to enforce dedup-check-first. The full upsert payload is
    asserted in test_v3_7_4_hubspot_dedup.py with explicit decisions."""
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.hubspot_upsert_company(phase8_intake, "/tmp/out.docx")
    assert payload["tool"] == "search_crm_objects"
    assert payload["action"] == "hubspot_search_company"
    assert payload["requires_operator_review"] is True
    # Then with force_create: full create payload
    payload2 = phase8_actions.hubspot_upsert_company(
        phase8_intake, "/tmp/out.docx",
        dedup_decision={
            "force_create": True,
            "reason": "test fixture: search returned zero matches",
            "search_run_at": "2026-04-30T10:00:00Z",
        },
    )
    assert payload2["tool"] == "manage_crm_objects"
    assert len(payload2["dispatch"]) == 2
    assert payload2["dispatch"][0]["properties"]["name"] == "Acme Corp"


def test_phase8_clickup_payload(phase8_intake):
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    payload = phase8_actions.clickup_create_task(phase8_intake, "/tmp/out.docx")
    assert payload["tool"] == "clickup_create_task"
    assert "Acme Corp" in payload["dispatch"]["name"]
    assert "Wholesale" in payload["dispatch"]["name"]


def test_phase8_run_dry_run_default(phase8_intake):
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    result = phase8_actions.run_phase_8_actions(
        phase8_intake,
        "/tmp/out.docx",
        actions=["hubspot_upsert_company", "clickup_create_task"],
    )
    assert result["dry_run"] is True
    assert len(result["actions"]) == 2
    assert result["errors"] == []


def test_phase8_unknown_action_reports(phase8_intake):
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import phase8_actions
    result = phase8_actions.run_phase_8_actions(
        phase8_intake, "/tmp/out.docx", actions=["bogus_action"]
    )
    assert any("Unknown action" in e for e in result["errors"])


# ---------------------------------------------------------------------------
# scripts/artifact_storage.py
# ---------------------------------------------------------------------------


def test_artifact_storage_dry_run_returns_target_path(phase8_intake):
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts import artifact_storage
    target = artifact_storage.upload_artifact(
        "/tmp/out.docx", phase8_intake, dry_run=True
    )
    assert "20260420_DEG_LOI-Wholesale_acme-corp" in target


def test_artifact_storage_slugify():
    sys.path.insert(0, str(SKILL_ROOT))
    from scripts.artifact_storage import _slugify
    assert _slugify("Acme Corp.") == "acme-corp"
    assert _slugify("Cerebro Cloud") == "cerebro-cloud"
    assert _slugify("") == "counterparty"
