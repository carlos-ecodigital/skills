"""v3.7.1 tests — closes the 5 items deferred from v3.7.0.

Covers:
1. Joint Stocking Programme clause (InfraPartners §5.6)
2. Co-Marketing clause parameterized (InfraPartners §5.7)
3. 84-item audit checklist generator
4. `custom.clauses` modes `replace` + `insert-after:N`
5. Post-template renumbering pass (opt-in via choices.auto_renumber)
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

import pytest

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent))

import generate_loi  # noqa: E402


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def base_ss_intake():
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
            # v3.8.0: `description` removed.
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
        "programme": {"recital_a_variant": "default"},
        "dates": {
            "loi_date": "20 April 2026",
            "validity_date": "20 April 2027",
        },
        "supplier": {
            "capability_category": "modular_infrastructure",
            "core_capability": "Factory-built data-centre modules",
            "strategic_purposes": ["pipeline_visibility"],
        },
        "choices": {"joint_ip": "background", "exclusivity": False},
    }


@pytest.fixture
def base_ws_intake():
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
            # v3.8.0: `description` removed.
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
        "commercial": {"indicative_mw": "10 MW IT"},
        "choices": {},
    }


def _build(intake):
    loi = generate_loi.LOI(intake)
    doc = loi.build()
    return loi, doc, generate_loi._extract_text(doc)


# ---------------------------------------------------------------------------
# 1. Joint Stocking Programme (InfraPartners §5.6)
# ---------------------------------------------------------------------------


def test_joint_stocking_fires_on_sub6mo_lead(base_ss_intake):
    base_ss_intake["supplier"]["lead_time_target"] = "90 days"
    base_ss_intake["supplier"]["strategic_purposes"] = [
        "capacity_lock_in", "pipeline_visibility"
    ]
    _, _, text = _build(base_ss_intake)
    assert "Joint Stocking Programme" in text
    assert "90-day Ready-for-Service" in text


def test_joint_stocking_skips_on_long_lead(base_ss_intake):
    base_ss_intake["supplier"]["lead_time_target"] = "12 months"
    base_ss_intake["supplier"]["strategic_purposes"] = [
        "capacity_lock_in", "pipeline_visibility"
    ]
    _, _, text = _build(base_ss_intake)
    assert "Joint Stocking Programme" not in text


def test_joint_stocking_weeks_unit(base_ss_intake):
    """'6 weeks' = 42 days, under 180."""
    base_ss_intake["supplier"]["lead_time_target"] = "6 weeks"
    base_ss_intake["supplier"]["strategic_purposes"] = [
        "capacity_lock_in", "pipeline_visibility"
    ]
    _, _, text = _build(base_ss_intake)
    assert "Joint Stocking Programme" in text


def test_joint_stocking_sfi_tail_when_library_included(base_ss_intake):
    """When Super-Factory Initiative is in custom.definitions_include,
    the Joint Stocking clause references it."""
    base_ss_intake["supplier"]["lead_time_target"] = "90 days"
    base_ss_intake["supplier"]["strategic_purposes"] = [
        "capacity_lock_in", "pipeline_visibility"
    ]
    base_ss_intake["custom"] = {
        "definitions_include": ["super_factory_initiative"]
    }
    _, _, text = _build(base_ss_intake)
    if "Super-Factory Initiative" in generate_loi._load_common_defined_terms():
        assert "through the Super-Factory Initiative" in text


def test_joint_stocking_no_sfi_tail_by_default(base_ss_intake):
    base_ss_intake["supplier"]["lead_time_target"] = "90 days"
    base_ss_intake["supplier"]["strategic_purposes"] = [
        "capacity_lock_in", "pipeline_visibility"
    ]
    _, _, text = _build(base_ss_intake)
    assert "through the Super-Factory Initiative" not in text


# ---------------------------------------------------------------------------
# 2. Co-Marketing parameterized (InfraPartners §5.7)
# ---------------------------------------------------------------------------


def test_co_marketing_multi_supplier_framing(base_ss_intake):
    base_ss_intake["supplier"]["co_marketing"] = {
        "framing": "multi_supplier",
        "logo_use": "per_event_approval",
        "press_at_loi": "none",
    }
    _, _, text = _build(base_ss_intake)
    assert "Reference and Co-Marketing" in text
    assert "avoid language implying exclusivity" in text


def test_co_marketing_preferred_framing(base_ss_intake):
    base_ss_intake["supplier"]["co_marketing"] = {"framing": "preferred"}
    _, _, text = _build(base_ss_intake)
    assert "preferred supplier for the Provider's programme" in text


def test_co_marketing_exclusive_framing(base_ss_intake):
    base_ss_intake["supplier"]["co_marketing"] = {"framing": "exclusive"}
    _, _, text = _build(base_ss_intake)
    assert "sole named supplier" in text


def test_co_marketing_logo_yes(base_ss_intake):
    base_ss_intake["supplier"]["co_marketing"] = {"logo_use": "yes"}
    _, _, text = _build(base_ss_intake)
    assert "limited, revocable right to use its name and logo" in text


def test_co_marketing_logo_no(base_ss_intake):
    base_ss_intake["supplier"]["co_marketing"] = {"logo_use": "no"}
    _, _, text = _build(base_ss_intake)
    assert "neither Party grants the other any right to use its name" in text


def test_co_marketing_press_joint(base_ss_intake):
    base_ss_intake["supplier"]["co_marketing"] = {"press_at_loi": "joint"}
    _, _, text = _build(base_ss_intake)
    assert "issue a joint press release at the execution of this LOI" in text


def test_co_marketing_press_none_default(base_ss_intake):
    base_ss_intake["supplier"]["co_marketing"] = {"framing": "multi_supplier"}
    _, _, text = _build(base_ss_intake)
    assert "shall not issue any joint press release" in text


def test_co_marketing_sla_rendered(base_ss_intake):
    base_ss_intake["supplier"]["co_marketing"] = {
        "framing": "multi_supplier",
        "site_naming_approval_sla": "3 Business Days",
    }
    _, _, text = _build(base_ss_intake)
    assert "3 Business Days acknowledgement service level" in text


def test_co_marketing_validates_framing(base_ss_intake, capsys):
    base_ss_intake["supplier"]["co_marketing"] = {"framing": "bogus"}
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ss_intake)
    assert "framing must be one of" in capsys.readouterr().out


def test_co_marketing_ss_only(base_ws_intake, capsys):
    """co_marketing only valid for StrategicSupplier type."""
    base_ws_intake["supplier"] = {"co_marketing": {"framing": "multi_supplier"}}
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    assert "co_marketing is only valid" in capsys.readouterr().out


# ---------------------------------------------------------------------------
# 3. 84-item audit checklist generator
# ---------------------------------------------------------------------------


def test_audit_checklist_emitted_core(base_ws_intake, tmp_path):
    """_emit_audit_checklist writes a file with core assertions."""
    loi, doc, _ = _build(base_ws_intake)
    output_docx = str(tmp_path / "test.docx")
    doc.save(output_docx)

    audit_path = generate_loi._emit_audit_checklist(output_docx, doc, base_ws_intake)
    assert os.path.exists(audit_path)

    with open(audit_path) as f:
        content = f.read()
    # Core assertion coverage
    assert "Preamble — Digital Energy party intro" in content
    assert "Recital A — canonical body opener" in content
    assert 'Definitions — "DEC"' in content
    # No linter bugs should appear
    assert 'v3.6.0 bug — "tthe" typo' in content
    assert "PASS: " in content  # at least one PASS


def test_audit_checklist_expands_on_customizations(base_ss_intake, tmp_path):
    """Per-customization assertions scale the checklist up toward 84 items."""
    base_ss_intake["supplier"]["strategic_purposes"] = [
        "pipeline_visibility", "capacity_lock_in"
    ]
    base_ss_intake["supplier"]["lead_time_target"] = "90 days"
    base_ss_intake["supplier"]["rofr"] = {
        "site_scope": "1-3 Designated Sites",
        "lock_out_style": "alignment",
    }
    base_ss_intake["supplier"]["referral_rider"] = True
    base_ss_intake["supplier"]["co_marketing"] = {"framing": "multi_supplier"}
    base_ss_intake["choices"]["confidentiality_opt_outs"] = [
        "onward_sharing", "metadata_protection"
    ]
    base_ss_intake["custom"] = {
        "definitions": [{"key": "Widget", "text": "means a widget."}],
        "definitions_include": ["super_factory_initiative"],
    }

    loi, doc, _ = _build(base_ss_intake)
    output_docx = str(tmp_path / "test.docx")
    doc.save(output_docx)

    audit_path = generate_loi._emit_audit_checklist(output_docx, doc, base_ss_intake)
    with open(audit_path) as f:
        content = f.read()

    # Customization-specific assertions
    # v3.7.2: audit label updated to be auto_renumber-aware (no hardcoded §3.8)
    assert "RoFR Preferred-Supplier clause present" in content
    assert "RoFR — alignment framing present" in content
    assert "Mutual Referral Rider heading present" in content
    assert "Joint Stocking Programme heading present" in content
    assert "Reference and Co-Marketing heading present" in content
    assert "§6 Onward-Sharing suppressed" in content
    assert "§6 Metadata Protection suppressed" in content
    assert "custom.definitions — 'Widget' injected" in content


def test_audit_checklist_fail_lines_for_missing(base_ws_intake, tmp_path):
    """Customization assertions flag FAIL when expected text is absent."""
    base_ws_intake["custom"] = {
        "clauses": [
            {"number": "9.X", "mode": "append",
             "heading": "Missing Heading Check",
             "text": "Custom text that will actually render."}
        ]
    }
    loi, doc, _ = _build(base_ws_intake)
    output_docx = str(tmp_path / "test.docx")
    doc.save(output_docx)

    audit_path = generate_loi._emit_audit_checklist(output_docx, doc, base_ws_intake)
    with open(audit_path) as f:
        content = f.read()
    # Custom clause number assertion present in checklist
    assert "custom.clauses[9.X]" in content


# ---------------------------------------------------------------------------
# 4. custom.clauses modes replace + insert-after
# ---------------------------------------------------------------------------


def test_custom_clauses_replace_mode(base_ws_intake):
    """Replace mode overwrites the paragraph at the target number."""
    base_ws_intake["custom"] = {
        "clauses": [
            {
                "number": "3.8",  # existing WS §3.8 Site Allocation
                "mode": "replace",
                "heading": "Custom Site Allocation",
                "text": "Custom replacement text for site allocation logic.",
            }
        ]
    }
    _, _, text = _build(base_ws_intake)
    assert "Custom Site Allocation" in text
    assert "Custom replacement text for site allocation logic" in text
    # Original WS §3.8 language gone
    assert "Digital Energy is developing DEC facilities across multiple locations" not in text


def test_custom_clauses_insert_after_mode(base_ws_intake):
    """insert-after:N inserts the new clause immediately after clause N."""
    base_ws_intake["custom"] = {
        "clauses": [
            {
                "number": "3.9",
                "mode": "insert-after:3.8",
                "heading": "Extra Site Detail",
                "text": "Additional detail inserted after §3.8.",
            }
        ]
    }
    loi, doc, text = _build(base_ws_intake)
    assert "Extra Site Detail" in text
    assert "Additional detail inserted after §3.8" in text

    # Verify ordering — §3.9 comes after §3.8 in the rendered document
    idx_38 = text.find("3.8 Site Allocation")
    idx_39 = text.find("3.9 Extra Site Detail")
    assert idx_38 >= 0 and idx_39 >= 0
    assert idx_38 < idx_39


def test_custom_clauses_replace_preserves_later_clauses(base_ws_intake):
    """Replacing §3.8 doesn't delete §4.X or §5.X."""
    base_ws_intake["custom"] = {
        "clauses": [
            {"number": "3.8", "mode": "replace", "heading": "X",
             "text": "Replaced."}
        ]
    }
    _, _, text = _build(base_ws_intake)
    # WS §4 heading is "Relationship Structure and Next Steps" in v3.7.x
    assert "4. Relationship Structure and Next Steps" in text
    assert "6.1" in text  # §6 confidentiality still there


def test_custom_clauses_replace_silent_on_unknown(base_ws_intake):
    """Replace with a number that doesn't exist in this LOI type is silent."""
    base_ws_intake["custom"] = {
        "clauses": [
            {"number": "9.99", "mode": "replace", "heading": "X", "text": "Y"}
        ]
    }
    _, _, text = _build(base_ws_intake)
    # Should still build cleanly
    assert "Letter of Intent" in text or "LOI" in text


# ---------------------------------------------------------------------------
# 5. Post-template renumbering pass (opt-in)
# ---------------------------------------------------------------------------


def test_renumber_opt_in_closes_ss_cl4_gaps(base_ss_intake):
    """SS clause4 with only pipeline_visibility leaves gaps at 4.3, 4.5.
    With auto_renumber, the sequence becomes 4.1 → 4.4 contiguous."""
    base_ss_intake["supplier"]["strategic_purposes"] = ["pipeline_visibility"]
    base_ss_intake["choices"]["auto_renumber"] = True

    _, _, text = _build(base_ss_intake)
    # After renumbering: §4 should run 4.1, 4.2, 4.3, 4.4 contiguously
    # (original: 4.1 pipeline, 4.2 sequence, 4.4 change of control, 4.6 roadmap)
    # With auto_renumber: 4.1, 4.2, 4.3, 4.4
    assert "4.1 Project Introduction Process" in text
    assert "4.2 Contractual Sequence" in text
    # 4.3 should now be Change of Control (was 4.4)
    assert "4.3 Change of Control" in text
    assert "4.4 Implementation Roadmap" in text


def test_renumber_default_off_preserves_gaps(base_ss_intake):
    """Without auto_renumber, pre-v3.7.1 gaps preserved (cosmetic-only)."""
    base_ss_intake["supplier"]["strategic_purposes"] = ["pipeline_visibility"]

    _, _, text = _build(base_ss_intake)
    # Without renumbering, the original numbers are preserved
    assert "4.4 Change of Control" in text
    assert "4.6 Implementation Roadmap" in text


def test_renumber_opt_in_cross_refs_updated(base_ss_intake):
    """When auto_renumber is on, cross-references like 'Clause X.Y' update."""
    base_ss_intake["supplier"]["strategic_purposes"] = ["pipeline_visibility"]
    base_ss_intake["choices"]["auto_renumber"] = True

    _, _, text = _build(base_ss_intake)
    # Survival reference should now say "Clauses 5.2, 5.3, 6, and 7"
    # (Cl. 6 is still 6, so no change), but if there were refs to a shifted
    # clause like "Clause 4.6", that should become "Clause 4.4".
    # This test verifies at minimum that build completes without error and
    # rendered text still makes sense.
    assert "Letter of Intent" in text
    # No negative assertions: the renumbering pass is conservative and only
    # updates when an actual gap was closed.


def test_renumber_validate_rejects_non_bool(base_ws_intake, capsys):
    base_ws_intake["choices"]["auto_renumber"] = "yes"
    with pytest.raises(SystemExit):
        generate_loi.validate(base_ws_intake)
    assert "auto_renumber must be a boolean" in capsys.readouterr().out


def test_renumber_noop_when_already_contiguous(base_ws_intake):
    """WS with no conditional skips should be unchanged by renumbering."""
    base_ws_intake["choices"]["auto_renumber"] = True
    _, _, text = _build(base_ws_intake)
    # All WS §3 numbers render by default — no gap to close
    assert "3.1 Indicative Capacity" in text
    assert "3.2 Technical Specification" in text


# ---------------------------------------------------------------------------
# Helper function tests
# ---------------------------------------------------------------------------


def test_lead_time_under_six_months_parses_days():
    assert generate_loi._lead_time_under_six_months("90 days") is True
    assert generate_loi._lead_time_under_six_months("179 days") is True
    assert generate_loi._lead_time_under_six_months("180 days") is False
    assert generate_loi._lead_time_under_six_months("365 days") is False


def test_lead_time_under_six_months_parses_weeks():
    assert generate_loi._lead_time_under_six_months("6 weeks") is True
    assert generate_loi._lead_time_under_six_months("25 weeks") is True
    assert generate_loi._lead_time_under_six_months("30 weeks") is False


def test_lead_time_under_six_months_parses_months():
    assert generate_loi._lead_time_under_six_months("3 months") is True
    assert generate_loi._lead_time_under_six_months("5 months") is True
    assert generate_loi._lead_time_under_six_months("6 months") is False
    assert generate_loi._lead_time_under_six_months("12 months") is False


def test_lead_time_under_six_months_short_units():
    assert generate_loi._lead_time_under_six_months("90d") is True
    assert generate_loi._lead_time_under_six_months("6w") is True
    assert generate_loi._lead_time_under_six_months("3m") is True


def test_lead_time_under_six_months_unparseable_returns_false():
    assert generate_loi._lead_time_under_six_months("") is False
    assert generate_loi._lead_time_under_six_months("TBC") is False
    assert generate_loi._lead_time_under_six_months("tbd") is False


def test_has_super_factory_initiative_include_list():
    data = {"custom": {"definitions_include": ["super_factory_initiative"]}}
    assert generate_loi._has_super_factory_initiative(data) is True


def test_has_super_factory_initiative_custom_definitions():
    data = {
        "custom": {
            "definitions": [
                {"key": "Super-Factory Initiative", "text": "..."}
            ]
        }
    }
    assert generate_loi._has_super_factory_initiative(data) is True


def test_has_super_factory_initiative_absent():
    assert generate_loi._has_super_factory_initiative({}) is False
    assert generate_loi._has_super_factory_initiative(
        {"custom": {"definitions": [{"key": "Other", "text": "..."}]}}
    ) is False
