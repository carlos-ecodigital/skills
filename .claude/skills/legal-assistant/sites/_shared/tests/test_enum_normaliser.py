"""Tests for enum_normaliser.py — parser token → registry enum mapping."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest

_SHARED = Path(__file__).resolve().parents[1]
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

import enum_normaliser as en  # noqa: E402
import site_doc_base as sdb  # noqa: E402


@pytest.fixture
def registry():
    """Fresh registry dict per test (validation cache is id()-keyed, so
    fresh dicts re-validate — critical for the drift test)."""
    return sdb.load_registry()


# ---------------------------------------------------------------------------
# A6 signing authority
# ---------------------------------------------------------------------------

def test_normalise_signing_authority_sole(registry):
    assert en.normalise_field(
        "A6_signing_authority", "Sole", registry
    ) == "Sole / Zelfstandig bevoegd"


def test_normalise_signing_authority_joint(registry):
    assert en.normalise_field(
        "A6_signing_authority", "Joint", registry
    ) == "Joint / Gezamenlijk bevoegd"


def test_normalise_signing_authority_nl_variant(registry):
    assert en.normalise_field(
        "A6_signing_authority", "Zelfstandig bevoegd", registry
    ) == "Sole / Zelfstandig bevoegd"


# ---------------------------------------------------------------------------
# D2 title type
# ---------------------------------------------------------------------------

def test_normalise_title_type_eigendom_maps_to_full_ownership(registry):
    assert en.normalise_field(
        "D2_title_type", "Eigendom", registry
    ) == "Full ownership / Vol eigendom"


def test_normalise_title_type_recht_van_opstal_maps_to_other(registry):
    assert en.normalise_field(
        "D2_title_type", "Recht van opstal", registry
    ) == "Other / Anders"


def test_normalise_title_type_erfpacht_maps_to_leasehold(registry):
    assert en.normalise_field(
        "D2_title_type", "Erfpacht", registry
    ) == "Erfpacht / Leasehold"


# ---------------------------------------------------------------------------
# D3 encumbrances (bool → enum)
# ---------------------------------------------------------------------------

def test_normalise_encumbrances_true_maps_to_mortgage(registry):
    assert en.normalise_field(
        "D3_encumbrances", True, registry
    ) == "Mortgage / Hypotheek"


def test_normalise_encumbrances_false_maps_to_none(registry):
    assert en.normalise_field(
        "D3_encumbrances", False, registry
    ) == "None / Geen"


# ---------------------------------------------------------------------------
# Unknown token / non-enum passthrough / idempotence
# ---------------------------------------------------------------------------

def test_unknown_value_raises_enumnormalisererror(registry):
    with pytest.raises(en.EnumNormaliserError):
        en.normalise_field("D2_title_type", "Flarp", registry)


def test_non_enum_field_passes_through(registry):
    # A2_kvk_number is type 'text' — no enum options.
    assert en.normalise_field(
        "A2_kvk_number", "12345678", registry
    ) is None


def test_normalise_preserves_original_value_when_already_canonical(registry):
    canonical = "Sole / Zelfstandig bevoegd"
    assert en.normalise_field(
        "A6_signing_authority", canonical, registry
    ) == canonical


def test_normalise_case_insensitive_canonical(registry):
    # A registry option matched case-insensitively should still canonicalise.
    assert en.normalise_field(
        "D2_title_type", "erfpacht / leasehold", registry
    ) == "Erfpacht / Leasehold"


# ---------------------------------------------------------------------------
# normalise_parse_result
# ---------------------------------------------------------------------------

def test_normalise_parse_result_processes_all_fields(registry):
    parse_result = {
        # Enum — gets normalised
        "A6_signing_authority": "Sole",
        "D2_title_type": "Eigendom",
        "D3_encumbrances": False,
        # Non-enum — passes through
        "A1_legal_name": "Van Gog B.V.",
        "A2_kvk_number": "12345678",
    }
    out = en.normalise_parse_result(parse_result, registry)
    assert out["A6_signing_authority"] == "Sole / Zelfstandig bevoegd"
    assert out["D2_title_type"] == "Full ownership / Vol eigendom"
    assert out["D3_encumbrances"] == "None / Geen"
    assert out["A1_legal_name"] == "Van Gog B.V."
    assert out["A2_kvk_number"] == "12345678"
    # Confirm input is not mutated.
    assert parse_result["A6_signing_authority"] == "Sole"


# ---------------------------------------------------------------------------
# normalise_deal_yaml (walks nested structure)
# ---------------------------------------------------------------------------

def test_normalise_deal_yaml_walks_nested_structure(registry):
    deal = {
        "site_partners": [
            {
                "legal_name": "Van Gog B.V.",
                "signatory": {"signing_authority": "Joint"},
                "contributions": [
                    {
                        "asset": "land",
                        "details": {
                            "title_type": "Eigendom",
                            "encumbrances": True,
                        },
                    },
                    {
                        "asset": "grid_interconnection",
                        "details": {"mva": 10},  # no enum fields
                    },
                ],
            }
        ]
    }
    out = en.normalise_deal_yaml(deal, registry)
    sig = out["site_partners"][0]["signatory"]
    assert sig["signing_authority"] == "Joint / Gezamenlijk bevoegd"
    land_details = out["site_partners"][0]["contributions"][0]["details"]
    assert land_details["title_type"] == "Full ownership / Vol eigendom"
    assert land_details["encumbrances"] == "Mortgage / Hypotheek"
    # Non-enum field preserved.
    grid_details = out["site_partners"][0]["contributions"][1]["details"]
    assert grid_details == {"mva": 10}


# ---------------------------------------------------------------------------
# Registry drift detection
# ---------------------------------------------------------------------------

def test_registry_validation_on_import_catches_map_drift(registry):
    """If TOKEN_MAP targets values not present in registry options,
    validation must raise."""
    # Tamper a copy of the registry so its options don't match TOKEN_MAP.
    tampered = copy.deepcopy(registry)
    tampered["sections"]["D"]["fields"]["D2_title_type"]["options"] = [
        "Made / Up",
        "Never / Seen",
    ]
    with pytest.raises(en.EnumNormaliserError):
        en.normalise_field("D2_title_type", "Eigendom", tampered)


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------

def test_audit_enum_coverage_reports_mapped_and_passthrough(registry):
    audit = en.audit_enum_coverage(registry)
    # The three fields with TOKEN_MAP entries must appear as mapped.
    for fid in ("A6_signing_authority", "D2_title_type", "D3_encumbrances"):
        assert fid in audit["mapped"]
    # At least one known passthrough field (grower populates it canonically).
    assert "B1_dso" in audit["passthrough"]
    # No overlap.
    assert set(audit["mapped"]).isdisjoint(audit["passthrough"])
