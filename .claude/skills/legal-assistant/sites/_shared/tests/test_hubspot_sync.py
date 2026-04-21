"""Tests for hubspot_sync.py - Phase B7.

Uses a FakeHubSpotClient that stores Van Gog-like data locally so tests
never touch the real HubSpot MCP surface.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List

import pytest

_SHARED = Path(__file__).resolve().parents[1]
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

import hubspot_sync as hs  # noqa: E402


# ---------------------------------------------------------------------------
# Fake client + fixture data (Van Gog-like)
# ---------------------------------------------------------------------------


class FakeHubSpotClient(hs.HubSpotClient):
    """In-memory HubSpot double. Stores deals/companies/contacts + records
    update calls for assertion."""

    def __init__(
        self,
        deal: Dict[str, Any] | None = None,
        companies: List[Dict[str, Any]] | None = None,
        contacts: List[Dict[str, Any]] | None = None,
    ) -> None:
        self._deal = deal or {}
        self._companies = companies or []
        self._contacts = contacts or []
        self.updates: List[tuple[int, Dict[str, Any]]] = []

    def read_deal(self, deal_id: int) -> dict:
        return dict(self._deal)

    def read_associated_companies(self, deal_id: int) -> List[dict]:
        return [dict(c) for c in self._companies]

    def read_associated_contacts(self, deal_id: int) -> List[dict]:
        return [dict(c) for c in self._contacts]

    def update_deal_properties(self, deal_id: int, updates: Dict[str, Any]) -> None:
        self.updates.append((deal_id, dict(updates)))


def _van_gog_deal_properties() -> Dict[str, Any]:
    """Van Gog Grubbenvorst anchor deal 365739346165, heat recovery."""
    return {
        "dealname": "Van Gog Grubbenvorst - Heat Recovery LOI",
        "pipeline": "492649440",
        "dealstage": "1163932892",
        "hs_lastmodifieddate": "2026-04-15T10:00:00Z",
        "hubspot_owner_id": 521949924,
        "type_of_deal": "Heat Recovery",
        "dealtype": "newbusiness",
        "deal_value": 2500000.0,
        "deal_currency_code": "EUR",
        "contract_capacity___available__mw_": 3.5,
        "contract_capacity___potential__mw_": 5.0,
        "where_is_your_site_located_____city___country": "Grubbenvorst, NL",
        "site_ownership_deal": "recht_van_opstal",
        "how_do_you_currently_produce_heat_": "gas_ketel",
        "full_site___expected_launch_date": "2027-01-01",
        # intentionally unmapped property - should go into raw_extra
        "some_custom_property": "free-text",
    }


def _van_gog_companies_three() -> List[Dict[str, Any]]:
    return [
        {
            "id": 111001,
            "name": "Van Gog Grubbenvorst B.V.",
            "kvk": "12345678",
            "address": "Venloseweg 1, Grubbenvorst",
            "domain": "vangog.nl",
        },
        {
            "id": 111002,
            "name": "Van Gog Vastgoed B.V.",
            "kvk": "23456789",
            "address": "Venloseweg 1, Grubbenvorst",
        },
        {
            "id": 111003,
            "name": "Van Gog kwekerijen Grubbenvorst B.V.",
            "kvk": "34567890",
            "address": "Venloseweg 1, Grubbenvorst",
        },
    ]


def _van_gog_contacts() -> List[Dict[str, Any]]:
    return [
        {
            "id": 578654116067,
            "firstname": "Koen",
            "lastname": "Saris",
            "jobtitle": "Operationeel Directeur",
            "email": "k.saris@vangog.nl",
            "associated_company_id": 111001,
            "signing_authority": "sole",
        }
    ]


# ---------------------------------------------------------------------------
# read_deal
# ---------------------------------------------------------------------------


def test_read_deal_hydrates_hubspot_block():
    client = FakeHubSpotClient(
        deal=_van_gog_deal_properties(),
        companies=_van_gog_companies_three(),
        contacts=_van_gog_contacts(),
    )
    deal: Dict[str, Any] = {"hubspot_deal_id": 365739346165}

    hs.read_deal(client, deal)

    assert deal["hubspot"]["dealname"].startswith("Van Gog")
    assert deal["hubspot"]["pipeline"] == "492649440"
    assert deal["hubspot"]["dealstage"] == "1163932892"
    assert deal["hubspot"]["hs_lastmodifieddate"] == "2026-04-15T10:00:00Z"
    assert deal["hubspot"]["last_sync_at"]  # set to _now_iso()
    # Unmapped property preserved under raw_extra
    assert deal["hubspot"]["raw_extra"]["some_custom_property"] == "free-text"


def test_read_deal_hydrates_owner():
    client = FakeHubSpotClient(
        deal=_van_gog_deal_properties(),
        companies=[],
        contacts=[],
    )
    deal: Dict[str, Any] = {"hubspot_deal_id": 365739346165}
    hs.read_deal(client, deal)
    assert deal["owner"]["hubspot_owner_id"] == 521949924


def test_read_deal_hydrates_commercial_envelope():
    client = FakeHubSpotClient(
        deal=_van_gog_deal_properties(),
        companies=[],
        contacts=[],
    )
    deal: Dict[str, Any] = {"hubspot_deal_id": 365739346165}
    hs.read_deal(client, deal)
    c = deal["commercial"]
    assert c["deal_value_eur"] == 2500000.0
    assert c["currency"] == "EUR"
    assert c["contract_mw_available"] == 3.5
    assert c["contract_mw_potential"] == 5.0


def test_read_deal_creates_site_partners_from_associated_companies():
    client = FakeHubSpotClient(
        deal=_van_gog_deal_properties(),
        companies=_van_gog_companies_three(),
        contacts=_van_gog_contacts(),
    )
    deal: Dict[str, Any] = {"hubspot_deal_id": 365739346165}
    hs.read_deal(client, deal)

    partners = deal["site_partners"]
    assert len(partners) == 3
    assert partners[0]["legal_name"] == "Van Gog Grubbenvorst B.V."
    assert partners[0]["kvk"] == "12345678"
    assert partners[0]["entity_id"] == 111001
    # contributions/returns initialised empty
    assert partners[0]["contributions"] == []
    assert partners[0]["returns"] == []


def test_read_deal_attaches_contacts_to_site_partner_signatories():
    client = FakeHubSpotClient(
        deal=_van_gog_deal_properties(),
        companies=_van_gog_companies_three(),
        contacts=_van_gog_contacts(),
    )
    deal: Dict[str, Any] = {"hubspot_deal_id": 365739346165}
    hs.read_deal(client, deal)

    # Company 111001 (Van Gog Grubbenvorst B.V.) has the Koen Saris contact.
    gr = deal["site_partners"][0]
    assert "signatory" in gr
    assert gr["signatory"]["name"] == "Koen Saris"
    assert gr["signatory"]["title"] == "Operationeel Directeur"
    assert gr["signatory"]["contact_id"] == 578654116067
    assert gr["signatory"]["signing_authority"] == "sole"

    # Other partners have no associated contact -> no signatory key
    vastgoed = deal["site_partners"][1]
    kwek = deal["site_partners"][2]
    assert "signatory" not in vastgoed
    assert "signatory" not in kwek


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------


def _hydrated_van_gog_deal() -> Dict[str, Any]:
    """Hydrate a deal once and return it as a starting point for validate tests."""
    client = FakeHubSpotClient(
        deal=_van_gog_deal_properties(),
        companies=_van_gog_companies_three(),
        contacts=_van_gog_contacts(),
    )
    deal: Dict[str, Any] = {"hubspot_deal_id": 365739346165}
    hs.read_deal(client, deal)
    return deal


def test_validate_detects_legal_name_conflict():
    deal = _hydrated_van_gog_deal()
    deal["site_partners"][0]["legal_name"] = "WRONG NAME B.V."

    view = {
        "deal": _van_gog_deal_properties(),
        "companies": _van_gog_companies_three(),
        "contacts": _van_gog_contacts(),
    }
    conflicts = hs.validate(deal, view)
    name_conflicts = [c for c in conflicts if c.field_path.endswith("legal_name")]
    assert len(name_conflicts) == 1
    assert name_conflicts[0].local_value == "WRONG NAME B.V."
    assert name_conflicts[0].hubspot_value == "Van Gog Grubbenvorst B.V."


def test_validate_detects_kvk_conflict():
    deal = _hydrated_van_gog_deal()
    deal["site_partners"][0]["kvk"] = "99999999"

    view = {
        "deal": _van_gog_deal_properties(),
        "companies": _van_gog_companies_three(),
        "contacts": _van_gog_contacts(),
    }
    conflicts = hs.validate(deal, view)
    kvk_conflicts = [c for c in conflicts if c.field_path.endswith(".kvk")]
    assert len(kvk_conflicts) == 1
    assert kvk_conflicts[0].local_value == "99999999"
    assert kvk_conflicts[0].hubspot_value == "12345678"


def test_validate_empty_on_matching_data():
    deal = _hydrated_van_gog_deal()
    view = {
        "deal": _van_gog_deal_properties(),
        "companies": _van_gog_companies_three(),
        "contacts": _van_gog_contacts(),
    }
    conflicts = hs.validate(deal, view)
    assert conflicts == []


# ---------------------------------------------------------------------------
# resolve
# ---------------------------------------------------------------------------


def test_resolve_hubspot_wins_for_identity():
    deal = _hydrated_van_gog_deal()
    # Force a dealname drift, as though local got edited incorrectly
    deal["hubspot"]["dealname"] = "wrong-name-locally"
    conflicts = [
        hs.Conflict(
            field_path="hubspot.dealname",
            hubspot_property="dealname",
            local_value="wrong-name-locally",
            hubspot_value="Van Gog Grubbenvorst - Heat Recovery LOI",
        )
    ]
    hs.resolve(deal, conflicts)
    assert conflicts[0].resolution == "hubspot_wins"
    assert deal["hubspot"]["dealname"] == "Van Gog Grubbenvorst - Heat Recovery LOI"


def test_resolve_doc_wins_for_enriched_parcel_id():
    deal = _hydrated_van_gog_deal()
    # Pretend parsed-Kadaster doc set the local parcel_id already
    deal["locations"] = [{"parcel_id": "GRUBBENVORST A 1234"}]
    conflicts = [
        hs.Conflict(
            field_path="locations[0].parcel_id",
            hubspot_property="kadaster_parcel_id",
            local_value="GRUBBENVORST A 1234",
            hubspot_value="UNKNOWN",
            source_doc="documents/kadaster_uittreksel.pdf",
        )
    ]
    hs.resolve(deal, conflicts)
    assert conflicts[0].resolution == "doc_wins"
    # Local value preserved
    assert deal["locations"][0]["parcel_id"] == "GRUBBENVORST A 1234"


def test_resolve_appends_audit_entry():
    deal = _hydrated_van_gog_deal()
    conflicts = [
        hs.Conflict(
            field_path="hubspot.dealname",
            hubspot_property="dealname",
            local_value="x",
            hubspot_value="y",
        )
    ]
    hs.resolve(deal, conflicts)
    log = deal["hubspot"]["conflict_log"]
    assert len(log) == 1
    entry = log[0]
    assert entry["field"] == "hubspot.dealname"
    assert entry["hubspot_property"] == "dealname"
    assert entry["resolution"] == "hubspot_wins"
    assert entry["at"]  # ISO timestamp set
    # Mirrored into enrichment log for cross-doc gate
    assert deal["enrichment"]["conflict_log"][0]["field"] == "hubspot.dealname"


# ---------------------------------------------------------------------------
# write_enrichment
# ---------------------------------------------------------------------------


def test_write_enrichment_only_writes_mapped_fields():
    client = FakeHubSpotClient(deal={}, companies=[], contacts=[])
    deal = {"hubspot_deal_id": 365739346165}
    payload = hs.write_enrichment(
        client,
        deal,
        {
            "deal_value": 3000000.0,                           # mapped
            "contract_capacity___available__mw_": 4.0,          # mapped
            "totally_made_up_property": "nope",                # unmapped -> dropped
        },
    )
    assert "deal_value" in payload
    assert "contract_capacity___available__mw_" in payload
    assert "totally_made_up_property" not in payload
    # Only one call was actually forwarded to client
    assert len(client.updates) == 1
    assert client.updates[0][0] == 365739346165


def test_write_enrichment_never_writes_dealstage():
    client = FakeHubSpotClient(deal={}, companies=[], contacts=[])
    deal = {"hubspot_deal_id": 365739346165}
    payload = hs.write_enrichment(
        client,
        deal,
        {
            "dealstage": "1163932893",
            "pipeline": "492649440",
            "dealname": "renamed",
            "deal_value": 999.0,
        },
    )
    assert "dealstage" not in payload
    assert "pipeline" not in payload
    assert "dealname" not in payload
    assert payload == {"deal_value": 999.0}


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------


def test_set_path_creates_nested_keys():
    d: Dict[str, Any] = {}
    hs._set_path(d, "a.b.c", 42)
    assert d == {"a": {"b": {"c": 42}}}


def test_get_path_returns_none_for_missing_key():
    d = {"a": {"b": 1}}
    assert hs._get_path(d, "a.b") == 1
    assert hs._get_path(d, "a.c") is None
    assert hs._get_path(d, "x.y.z") is None
    assert hs._get_path(d, "x.y.z", default="fallback") == "fallback"


# ---------------------------------------------------------------------------
# Van Gog DataAcc-1 (expected gap)
# ---------------------------------------------------------------------------


def test_van_gog_zero_companies_surfaces_as_conflict():
    """Deal 365739346165 in HubSpot has 0 associated Companies, but
    deal.yaml expects 3 Van Gog B.V. entities. This should surface as a
    conflict (cross-doc gate DataAcc-1 fail), not a silent success."""
    # Local deal.yaml hydrated with 3 expected partners
    deal: Dict[str, Any] = {
        "hubspot_deal_id": 365739346165,
        "site_partners": [
            {"legal_name": "Van Gog Grubbenvorst B.V.", "kvk": "12345678"},
            {"legal_name": "Van Gog Vastgoed B.V.", "kvk": "23456789"},
            {
                "legal_name": "Van Gog kwekerijen Grubbenvorst B.V.",
                "kvk": "34567890",
            },
        ],
    }
    # But HubSpot shows 0 companies (the real-world DataAcc-1 gap)
    view = {"deal": {}, "companies": [], "contacts": []}

    conflicts = hs.validate(deal, view)
    count_conflicts = [
        c for c in conflicts if c.hubspot_property == "associated_companies_count"
    ]
    assert len(count_conflicts) == 1
    assert count_conflicts[0].local_value == 3
    assert count_conflicts[0].hubspot_value == 0
