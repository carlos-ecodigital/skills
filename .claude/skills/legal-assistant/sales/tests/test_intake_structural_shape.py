"""Intake structural-shape linter — v3.5.8 PRINCIPLES.md tripwire #12.

Asserts all 6 reference intake YAMLs in `colocation/examples/` share a
consistent structural shape. The generator depends on a stable set of
top-level + second-level keys; a YAML-only edit that renames a key, drops
a section, or desyncs conventions between types can silently break the
render path for a single LOI type while every other type still works —
the exact class of regression that escapes golden-file tests (they only
exercise paths the fixtures exercise).

**Failure mode this guards against (observed in v3.5.5):** distributor
intake shipped with `commercial:` section present but missing
`indicative_mw`; Wholesale generator tolerated the absence, Distributor
generator raised KeyError at render time. Test-harness gap: shape was
never asserted, only output was fingerprinted.

This test is deliberately prescriptive — it encodes the intake contract.
Changes here are real: any shape change needs an explicit update to the
expected keys + a CHANGELOG migration note for downstream users.
"""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml


_TESTS_DIR = Path(__file__).resolve().parent
_COLOCATION_DIR = _TESTS_DIR.parent
_EXAMPLES_DIR = _COLOCATION_DIR / "examples"


# -----------------------------------------------------------------------------
# Contract: minimum top-level keys required in every intake
# -----------------------------------------------------------------------------

REQUIRED_TOP_LEVEL = {
    "type",
    "provider",
    "counterparty",
    "dates",
    "programme",
    "protection",
    "choices",
}

# type → additional required top-level sections
TYPE_REQUIRED_TOPLEVEL: dict[str, set[str]] = {
    "EndUser": {"commercial"},
    "Wholesale": {"commercial", "schedule_1"},
    "Distributor": {"commercial", "partnership_mode"},
    "StrategicSupplier": {"supplier"},
    "EcosystemPartnership": {"ecosystem"},
}

REQUIRED_PROVIDER = {
    "legal_name",
    "short_name",
    "address",
    "kvk",
    "signatory_name",
    "signatory_title",
}

REQUIRED_COUNTERPARTY = {
    "name",
    "short",
    "address",
    "jurisdiction",
    "signatory_name",
    "signatory_title",
    "description",
    "source_map",
}

REQUIRED_DATES = {"loi_date", "validity_date"}
REQUIRED_PROGRAMME = {"platform_mw", "recital_a_variant", "site_count"}

EXPECTED_TYPE_FOR_FILE: dict[str, str] = {
    "intake_example_enduser.yaml": "EndUser",
    "intake_example_wholesale.yaml": "Wholesale",
    "intake_example_distributor.yaml": "Distributor",
    "intake_example_distributor_referral.yaml": "Distributor",
    "intake_example_strategic_supplier.yaml": "StrategicSupplier",
    # v3.7.2: kitchen-sink example exercising every v3.7.x feature together
    "intake_example_strategic_supplier_v37_full.yaml": "StrategicSupplier",
    "intake_example_ecosystem_partnership.yaml": "EcosystemPartnership",
}

# M4 Bespoke type — architecturally distinct from the 6 templated types.
# Intentionally excluded from EXPECTED_TYPE_FOR_FILE because the Bespoke
# schema is less prescriptive (no required `dates.validity_date`, no
# required `programme.platform_mw` / `programme.site_count`) — those
# fields are template-specific, not universal. Bespoke examples are
# covered by a dedicated test suite (tests/test_bespoke.py,
# tests/test_mdcs_bespoke.py). They are listed here so
# test_all_intakes_discovered reconciles the full on-disk set.
BESPOKE_FILES: dict[str, str] = {
    "intake_example_bespoke.yaml": "Bespoke",
    "intake_example_bespoke_mdcs.yaml": "Bespoke",
}


def _discover_intakes() -> list[tuple[str, Path]]:
    return [
        (p.name, p)
        for p in sorted(_EXAMPLES_DIR.glob("intake_example_*.yaml"))
    ]


@pytest.fixture(scope="module")
def intakes() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for name, path in _discover_intakes():
        with open(path) as f:
            out[name] = yaml.safe_load(f)
    return out


# -----------------------------------------------------------------------------
# Top-level shape
# -----------------------------------------------------------------------------

class TestTopLevelShape:
    """Every intake must carry the minimum top-level contract + its
    type-specific additions. Drift here breaks the generator for one
    LOI type while others continue to work — silent until someone regens."""

    def test_all_intakes_discovered(self, intakes):
        """The fixture set is the contract — if a file is renamed or
        deleted, the test surface has to be updated explicitly.

        Set = templated types (EXPECTED_TYPE_FOR_FILE) ∪ Bespoke
        examples (BESPOKE_FILES) present on disk. Adding a new example
        YAML requires registering it in one of the two dicts.

        v3.7.2: the bespoke examples are filtered to those present on
        disk — staging repos may not carry the bespoke set (M4 sites-
        stream) even though upstream does. The mirror-manifest requires
        this file to be byte-identical between repos, so the filter is
        the cleanest way to accommodate the known divergence."""
        import os as _os
        expected_templated = set(EXPECTED_TYPE_FOR_FILE)
        # Filter BESPOKE_FILES to those actually present on disk.
        present_bespoke = {
            name for name in BESPOKE_FILES
            if _os.path.exists(str(_EXAMPLES_DIR / name))
        }
        expected = expected_templated | present_bespoke
        assert set(intakes.keys()) == expected, (
            f"Intake file set drifted. Expected {sorted(expected)}, "
            f"got {sorted(intakes)}."
        )

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_required_top_level_keys(self, intakes, name):
        d = intakes[name]
        missing = REQUIRED_TOP_LEVEL - set(d.keys())
        assert not missing, f"{name} missing required top-level keys: {missing}"

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_type_value_matches_filename(self, intakes, name):
        d = intakes[name]
        assert d["type"] == EXPECTED_TYPE_FOR_FILE[name], (
            f"{name} declares type={d['type']!r}, "
            f"expected {EXPECTED_TYPE_FOR_FILE[name]!r}"
        )

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_type_specific_sections(self, intakes, name):
        d = intakes[name]
        t = d["type"]
        required = TYPE_REQUIRED_TOPLEVEL.get(t, set())
        missing = required - set(d.keys())
        assert not missing, (
            f"{name} (type={t}) missing type-specific sections: {missing}"
        )


# -----------------------------------------------------------------------------
# Provider + counterparty shape
# -----------------------------------------------------------------------------

class TestPartyShape:
    """provider + counterparty are consumed by every render path
    (Parties Preamble, sig block, footer). Missing field → template
    renders literal None/KeyError on a single type without regressing the
    others."""

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_provider_shape(self, intakes, name):
        provider = intakes[name].get("provider") or {}
        missing = REQUIRED_PROVIDER - set(provider.keys())
        assert not missing, f"{name}.provider missing: {missing}"

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_counterparty_shape(self, intakes, name):
        cp = intakes[name].get("counterparty") or {}
        missing = REQUIRED_COUNTERPARTY - set(cp.keys())
        assert not missing, f"{name}.counterparty missing: {missing}"

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_provider_nl_bv_seed_values(self, intakes, name):
        """v3.5.1 A'': seed YAMLs should show the Dutch BV address, NOT
        the Swiss AG parent address. Prevents accidental Zug leak back
        into the example set."""
        provider = intakes[name].get("provider") or {}
        addr = provider.get("address") or ""
        assert "Zug" not in addr, (
            f"{name}.provider.address contains 'Zug' — should be NL BV, "
            f"not Swiss AG parent"
        )
        # Positive check: legal_name should clearly be Dutch BV
        legal = provider.get("legal_name") or ""
        assert "B.V." in legal or "Netherlands" in legal, (
            f"{name}.provider.legal_name={legal!r} — expected Dutch BV"
        )

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_provider_nl_bv_signatory_is_carlos(self, intakes, name):
        """v3.5.1 A: seed YAMLs default to Carlos Reuven / Director
        (statutory capacity under Dutch law). Jelmer ten Wolde shipped
        in 5 seed YAMLs in v3.4 — regression guard."""
        provider = intakes[name].get("provider") or {}
        signatory = provider.get("signatory_name") or ""
        # Not strict "must be Carlos" — EP fixture can use a group-level
        # signer — but explicitly ban the v3.4 bug.
        assert "Jelmer ten Wolde" not in signatory, (
            f"{name}.provider.signatory_name='Jelmer ten Wolde' — "
            f"v3.5.1 A fix: default for NL BV pre-MSA should be Carlos Reuven"
        )


# -----------------------------------------------------------------------------
# Supporting sections
# -----------------------------------------------------------------------------

class TestSupportingSections:
    """Shape of dates, programme, protection, choices — shallow but
    prevents silent rename/drop."""

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_dates_shape(self, intakes, name):
        dates = intakes[name].get("dates") or {}
        missing = REQUIRED_DATES - set(dates.keys())
        assert not missing, f"{name}.dates missing: {missing}"

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_programme_shape(self, intakes, name):
        programme = intakes[name].get("programme") or {}
        missing = REQUIRED_PROGRAMME - set(programme.keys())
        assert not missing, f"{name}.programme missing: {missing}"

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_recital_a_variant_enum(self, intakes, name):
        programme = intakes[name].get("programme") or {}
        v = programme.get("recital_a_variant")
        assert v in {"default", "sovereignty", "integration", "bespoke"}, (
            f"{name}.programme.recital_a_variant={v!r} — not in allowed enum"
        )


# -----------------------------------------------------------------------------
# source_map shape (v3.4 Scope D fabrication gate)
# -----------------------------------------------------------------------------

class TestSourceMapShape:
    """counterparty.source_map underpins R-23 fabrication gate. Shape
    drift here silently disables the gate for one LOI type.

    Contract: dict keyed by pillar_1..pillar_5; each value is a list
    (URLs or [TBC] markers)."""

    EXPECTED_PILLARS = {"pillar_1", "pillar_2", "pillar_3", "pillar_4", "pillar_5"}

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_source_map_is_dict(self, intakes, name):
        cp = intakes[name].get("counterparty") or {}
        sm = cp.get("source_map")
        assert isinstance(sm, dict), (
            f"{name}.counterparty.source_map must be a dict, got {type(sm).__name__}"
        )

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_source_map_pillars_present(self, intakes, name):
        sm = intakes[name]["counterparty"]["source_map"]
        missing = self.EXPECTED_PILLARS - set(sm.keys())
        assert not missing, (
            f"{name}.counterparty.source_map missing pillars: {missing}"
        )

    @pytest.mark.parametrize("name", list(EXPECTED_TYPE_FOR_FILE.keys()))
    def test_source_map_values_are_list_or_marker(self, intakes, name):
        """De-facto v3.5.x contract: pillar value is EITHER a list
        (canonical URL-list, Scope J7) OR a scalar string (legacy
        convention — `[TBC]` marker or inferred-from-phase rationale).
        Scalar `None` / dict / int is out of contract — silent breakage
        risk in R-23 scanning."""
        sm = intakes[name]["counterparty"]["source_map"]
        for pillar, val in sm.items():
            assert isinstance(val, (list, str)), (
                f"{name}.counterparty.source_map.{pillar} must be list or str, "
                f"got {type(val).__name__} ({val!r})"
            )
