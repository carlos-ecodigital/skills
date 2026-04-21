"""End-to-end HoT pipeline integration test.

Exercises every sites-stream integration point in a single run:

  1. **deal.yaml load**    — ``engine.load_deal``
  2. **HubSpot hydrate**   — ``engine.hydrate_from_hubspot(deal, client=fake)``
  3. **Document parsers**  — ``engine.parse_documents(deal, documents_dir)``
  4. **Cross-doc gate**    — ``engine.run_cross_doc_gate(deal)``
  5. **HoT body + Annex A**— ``engine.copy_body`` + ``engine.populate_annex_a``
  6. **Output router**     — ``output_router.route`` with a ``tmp_path`` base

Synthetic PDFs are produced per-test (PyMuPDF-built) so the suite never
touches real Drive paths or real HubSpot. The FakeHubSpotClient is a
minimal in-memory double mirroring the shape used by
``_shared/tests/test_hubspot_sync.py``.

The fixture pivots on the 3-partner Van Gog deal (Grid / Landowner /
Heat Offtaker); that shape stresses the section-to-partner mapping in
``parse_documents`` (``partner_entity_idx`` routing).
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, List

import pytest
import yaml

# conftest.py wires sites/_shared + sites/hot + sites/loi on sys.path.

import cross_doc_gate as cdg  # noqa: E402
import generate_site_hot as engine  # noqa: E402
import hubspot_sync as hs  # noqa: E402
import output_router as router  # noqa: E402

# Reuse the embedded Van Gog YAML produced by Wave-2 hot tests.
_HOT_TESTS = Path(__file__).resolve().parents[1] / "hot" / "tests"
if str(_HOT_TESTS) not in sys.path:
    sys.path.insert(0, str(_HOT_TESTS))

import fixtures_embedded  # noqa: E402


# ---------------------------------------------------------------------------
# FakeHubSpotClient — mirrors _shared/tests/test_hubspot_sync.FakeHubSpotClient
# but adds a factory constructor seeded with Van Gog data.
# ---------------------------------------------------------------------------


class FakeHubSpotClient(hs.HubSpotClient):
    """In-memory HubSpot double. ``.updates`` records every
    ``update_deal_properties`` call for assertion."""

    def __init__(
        self,
        deal: Dict[str, Any] | None = None,
        companies: List[Dict[str, Any]] | None = None,
        contacts: List[Dict[str, Any]] | None = None,
    ) -> None:
        self._deal = deal or {}
        self._companies = companies or []
        self._contacts = contacts or []
        self.read_deal_calls = 0
        self.read_companies_calls = 0
        self.read_contacts_calls = 0
        self.updates: List[tuple[int, Dict[str, Any]]] = []

    # --- Read surface (HubSpotClient contract) ---

    def read_deal(self, deal_id: int) -> dict:
        self.read_deal_calls += 1
        return dict(self._deal)

    def read_associated_companies(self, deal_id: int) -> List[dict]:
        self.read_companies_calls += 1
        return [dict(c) for c in self._companies]

    def read_associated_contacts(self, deal_id: int) -> List[dict]:
        self.read_contacts_calls += 1
        return [dict(c) for c in self._contacts]

    def update_deal_properties(self, deal_id: int, updates: Dict[str, Any]) -> None:
        self.updates.append((deal_id, dict(updates)))

    # --- Van Gog factory ---

    @classmethod
    def with_van_gog_data(cls) -> "FakeHubSpotClient":
        """Seed a fake client with Van Gog 3-Company / 4-Contact shape."""
        return cls(
            deal={
                "dealname": "van Gog kwekerijen Grubbenvorst",
                "pipeline": "492649440",
                "dealstage": "1163932892",
                "hs_lastmodifieddate": "2026-04-15T10:00:00Z",
                "hubspot_owner_id": 521949924,
                "type_of_deal": "Heat Recovery",
                "dealtype": "newbusiness",
                "deal_value": 300000.0,
                "deal_currency_code": "EUR",
                "contract_capacity___available__mw_": 3.0,
                "contract_capacity___potential__mw_": 10.0,
                "where_is_your_site_located_____city___country":
                    "Grubbenvorst, NL",
            },
            companies=[
                {
                    "id": 111001,
                    "name": "Van Gog Grubbenvorst B.V.",
                    "kvk": "12345678",
                    "address": "Horsterweg 1, 5971 NA Grubbenvorst",
                    "domain": "vangog.nl",
                },
                {
                    "id": 111002,
                    "name": "Van Gog Grubbenvorst Vastgoed B.V.",
                    "kvk": "23456789",
                    "address": "Horsterweg 1, 5971 NA Grubbenvorst",
                },
                {
                    "id": 111003,
                    "name": "Van Gog kwekerijen Grubbenvorst B.V.",
                    "kvk": "34567890",
                    "address": "Horsterweg 3, 5971 NA Grubbenvorst",
                },
            ],
            contacts=[
                {
                    "id": 5001,
                    "firstname": "Marion",
                    "lastname": "van Gog",
                    "jobtitle": "Directeur",
                    "email": "marion@vangog.nl",
                    "associated_company_id": 111001,
                    "signing_authority": "sole",
                },
                {
                    "id": 5002,
                    "firstname": "Marion",
                    "lastname": "van Gog",
                    "jobtitle": "Directeur",
                    "email": "marion@vangogvastgoed.nl",
                    "associated_company_id": 111002,
                    "signing_authority": "sole",
                },
                {
                    "id": 5003,
                    "firstname": "Koen",
                    "lastname": "Saris",
                    "jobtitle": "Operationeel Directeur",
                    "email": "koen.saris@vangogkwekerijen.nl",
                    "associated_company_id": 111003,
                    "signing_authority": "sole",
                },
                {
                    "id": 5004,
                    "firstname": "Lodewijk",
                    "lastname": "van Gog",
                    "jobtitle": "CFO",
                    "email": "lodewijk@vangog.nl",
                    "associated_company_id": 111001,
                    "signing_authority": "joint",
                },
            ],
        )


# ---------------------------------------------------------------------------
# Synthetic parser fixtures — minimal PDFs that the parsers can read.
# ---------------------------------------------------------------------------


def _make_pdf(text: str, path: Path) -> None:
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    for i, line in enumerate(text.split("\n")):
        page.insert_text((50, 50 + i * 14), line, fontsize=9)
    # Pad with filler so parsers' density checks never flip to "scan".
    for j in range(4):
        filler = (
            "Lorem ipsum dolor sit amet consectetur adipiscing elit "
            "sed do eiusmod tempor incididunt ut labore et dolore "
            "magna aliqua. " * 3
        )
        page.insert_text((50, 200 + j * 20), filler, fontsize=8)
    doc.save(str(path))
    doc.close()


def _make_synth_kvk_pdf(path: Path) -> None:
    _make_pdf(
        "Uittreksel Kamer van Koophandel\n"
        "KvK-nummer: 12345678\n"
        "Statutaire naam: Van Gog Grubbenvorst B.V.\n"
        "Vestigingsadres: Horsterweg 1, 5971 NA Grubbenvorst\n"
        "Bestuurders:\n"
        "Marion van Gog, Directeur\n"
        "Zelfstandig bevoegd",
        path,
    )


def _make_synth_ato_pdf(path: Path) -> None:
    _make_pdf(
        "Aansluit- en Transportovereenkomst\n"
        "Netbeheerder: Enexis Netbeheer B.V.\n"
        "Klant: Van Gog Grubbenvorst B.V.\n"
        "EAN: 871687510000099999\n"
        "ATO-nr: ATO 20250777\n"
        "Gecontracteerde capaciteit: 16 MVA\n"
        "Afname: 10 MW\n"
        "Teruglevering: 6 MW",
        path,
    )


def _make_synth_kadaster_pdf(path: Path) -> None:
    _make_pdf(
        "Kadaster Uittreksel\n"
        "Gemeente Horst aan de Maas, sectie G, nummer 8812\n"
        "Eigendom: Van Gog Grubbenvorst Vastgoed B.V.\n"
        "Titeltype: Eigendom\n"
        "Geen hypotheek of beslag aangetroffen.",
        path,
    )


def _make_synth_bestemmingsplan_pdf(path: Path) -> None:
    _make_pdf(
        "Bestemmingsplan uittreksel\n"
        "Gemeente: Horst aan de Maas\n"
        "Bestemming: Agrarisch - Glastuinbouw\n"
        "Dit perceel is gelegen in Glastuinbouwgebied.",
        path,
    )


# ---------------------------------------------------------------------------
# Shared deal fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def van_gog_deal_yaml(tmp_path):
    """Materialise the 3-partner Van Gog fixture and return its .yaml path."""
    return fixtures_embedded.write_van_gog_fixture(tmp_path)


def _load_and_mark(deal_yaml_path: Path, hubspot_deal_id: int | None = None) -> dict:
    """Load + optionally tag the deal with a HubSpot id (for tests that
    exercise the HubSpot hydrate path)."""
    deal = engine.load_deal(deal_yaml_path)
    if hubspot_deal_id is not None:
        deal["hubspot_deal_id"] = hubspot_deal_id
    return deal


def _attach_three_docs(deal: dict, docs_dir: Path, today: date) -> None:
    """Synthesise the 3 partner-scoped PDFs and register them on the deal."""
    docs_dir.mkdir(parents=True, exist_ok=True)
    _make_synth_kvk_pdf(docs_dir / "kvk_partner0.pdf")
    _make_synth_ato_pdf(docs_dir / "ato_partner0.pdf")
    _make_synth_kadaster_pdf(docs_dir / "kadaster_partner1.pdf")
    deal["documents"] = [
        {
            "type": "kvk_uittreksel",
            "path": "kvk_partner0.pdf",
            "partner_entity_idx": 0,
            "uploaded_at": today.isoformat(),
        },
        {
            "type": "ato_document",
            "path": "ato_partner0.pdf",
            "partner_entity_idx": 0,
            "uploaded_at": today.isoformat(),
        },
        {
            "type": "kadaster_uittreksel",
            "path": "kadaster_partner1.pdf",
            "partner_entity_idx": 1,
            "uploaded_at": today.isoformat(),
        },
    ]


# ---------------------------------------------------------------------------
# 1. Happy path — full pipeline
# ---------------------------------------------------------------------------


def test_van_gog_hot_full_pipeline(tmp_path, van_gog_deal_yaml):
    """Full pipeline: HubSpot fake → deal.yaml → 3 synthesised parser docs
    → enrichment → cross_doc_gate → HoT engine → body+annex .docx + qa
    + gate-report."""
    deal = _load_and_mark(van_gog_deal_yaml, hubspot_deal_id=365739346165)

    # --- HubSpot hydrate (1) ---
    fake_hs = FakeHubSpotClient.with_van_gog_data()
    deal = engine.hydrate_from_hubspot(deal, client=fake_hs)
    assert fake_hs.read_deal_calls >= 1
    assert fake_hs.read_companies_calls >= 1
    # After read_deal, site_partners are rebuilt from HubSpot companies —
    # there are 3 partners, one per company.
    assert len(deal["site_partners"]) == 3

    # --- Document parsers (2) ---
    docs_dir = tmp_path / "documents"
    _attach_three_docs(deal, docs_dir, date.today())
    deal = engine.parse_documents(deal, docs_dir)

    parser_log = deal["enrichment"]["parser_log"]
    ok_entries = [e for e in parser_log if e.get("status") == "ok"]
    # Every one of the 3 docs parsed successfully.
    assert len(ok_entries) == 3, parser_log
    doc_types_ok = {e["doc_type"] for e in ok_entries}
    assert doc_types_ok == {"kvk_uittreksel", "ato_document", "kadaster_uittreksel"}

    # ATO output must have landed on partner 0's grid_interconnection details.
    p0 = deal["site_partners"][0]
    grid = next(c for c in p0["contributions"] if c.get("asset") == "grid_interconnection")
    assert grid["details"].get("dso") == "Enexis"
    assert grid["details"].get("ean_code") == "871687510000099999"

    # Kadaster output must have landed on partner 1's land details.
    p1 = deal["site_partners"][1]
    land = next(c for c in p1["contributions"] if c.get("asset") in ("land", "property"))
    assert land["details"].get("kadaster_parcels"), land["details"]

    # --- Cross-doc gate (3) ---
    verdicts = engine.run_cross_doc_gate(deal)
    assert isinstance(verdicts, list)
    rules = {v["rule"] for v in verdicts}
    # hydrate_from_hubspot rebuilds site_partners from HubSpot Companies
    # (stripping the LOI-stage contributions/returns) — so only parser-
    # written fields remain on each partner. With that shape:
    #   - Gap-4 must fire for partners still missing required docs
    #     (partners 1 and 2 both need kvk_uittreksel; partner 2 also
    #     needs nothing else since it has no contributions post-hydrate).
    #   - Esc-3 must fire because a partner contributes land (partner 1,
    #     reconstructed by the parser merge) and no landowner_consent
    #     doc was uploaded.
    assert "Gap-4" in rules, rules
    assert "Esc-3" in rules, rules

    # --- HoT body + annex (4) ---
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    body_path = out_dir / "body.docx"
    annex_path = out_dir / "annex.docx"

    _, body_sha = engine.copy_body(body_path)
    # SHA-256 of body template matches copy.
    expected_sha = hashlib.sha256(engine.BODY_TEMPLATE.read_bytes()).hexdigest()
    assert body_sha == expected_sha
    assert body_path.exists() and body_path.stat().st_size > 5000

    registry = engine.sdb.load_registry()
    values = engine.build_field_values(deal)
    stats = engine.populate_annex_a(engine.ANNEX_A_TEMPLATE, annex_path, values, registry)
    assert annex_path.exists() and annex_path.stat().st_size > 5000
    assert len(stats.fields_written) >= 5

    # --- QA + gate reports (5) ---
    qa_path = out_dir / "qa.txt"
    gate_path = out_dir / "gate.json"
    engine.write_qa_report(deal, values, stats, verdicts, body_sha, qa_path)
    engine.write_gate_report(verdicts, gate_path)
    qa_text = qa_path.read_text()
    assert "Body template SHA-256" in qa_text
    gate_payload = json.loads(gate_path.read_text())
    assert gate_payload["stage"] == "hot"
    assert gate_payload["verdicts"] == verdicts

    # --- Output router (6) — route to a fake Drive base under tmp_path ---
    fake_drive = tmp_path / "drive"
    fake_drive.mkdir()
    artifact = router.OutputArtifact(
        src_path=body_path,
        slug="van-gog-grubbenvorst",
        counterparty_folder_name="Van Gog Grubbenvorst_Project_Benelux_Ops",
        doc_kind="hot",
    )
    dest = router.route(artifact, drive_base=fake_drive)
    assert dest.exists()
    assert dest.parent.name == "drafts"


# ---------------------------------------------------------------------------
# 2. Missing required doc → Gap-4 fires
# ---------------------------------------------------------------------------


def test_missing_required_doc_triggers_gap4(tmp_path, van_gog_deal_yaml):
    """Partner 1 contributes land but we upload ZERO landowner docs →
    cross_doc_gate emits Gap-4 for the missing kadaster_uittreksel."""
    deal = _load_and_mark(van_gog_deal_yaml)

    # Only upload a KvK for partner 0 — nothing for partner 1 who needs
    # kadaster_uittreksel + bestemmingsplan_excerpt for its land contribution.
    docs_dir = tmp_path / "documents"
    docs_dir.mkdir()
    _make_synth_kvk_pdf(docs_dir / "kvk_partner0.pdf")
    deal["documents"] = [
        {"type": "kvk_uittreksel", "path": "kvk_partner0.pdf",
         "partner_entity_idx": 0, "uploaded_at": date.today().isoformat()},
    ]
    engine.parse_documents(deal, docs_dir)

    verdicts = engine.run_cross_doc_gate(deal)
    gap4 = [v for v in verdicts if v["rule"] == "Gap-4"]
    # Expect at least one Gap-4 hit for partner 1's missing kadaster doc.
    assert gap4, f"expected Gap-4 but got rules={[v['rule'] for v in verdicts]}"
    # Every Gap-4 is non-overridable per cross_doc_gate.NON_OVERRIDABLE_RULES.
    assert all(v["overridable"] is False for v in gap4)


# ---------------------------------------------------------------------------
# 3. HubSpot conflict → conflict_log populated
# ---------------------------------------------------------------------------


def test_hubspot_conflict_updates_conflict_log(tmp_path, van_gog_deal_yaml):
    """When HubSpot Company.name differs from local site_partners[].legal_name
    the hydrate path records an audit entry in hubspot.conflict_log."""
    deal = _load_and_mark(van_gog_deal_yaml, hubspot_deal_id=365739346165)

    # Seed fake HubSpot with a KvK that disagrees with the deal.yaml fixture.
    fake = FakeHubSpotClient.with_van_gog_data()
    # The fixture's partner 0 has kvk "12345678" — force a drift.
    fake._companies[0]["kvk"] = "99999999"

    # First call: hydrate replaces local partners with HubSpot-derived set,
    # so there is no conflict at that stage — we then mutate the hydrated
    # partner[0] and run validate+resolve manually to exercise the log.
    engine.hydrate_from_hubspot(deal, client=fake)
    deal["site_partners"][0]["kvk"] = "11111111"  # simulated local drift

    view = {
        "deal": fake.read_deal(365739346165),
        "companies": fake.read_associated_companies(365739346165),
        "contacts": fake.read_associated_contacts(365739346165),
    }
    conflicts = hs.validate(deal, view)
    assert conflicts, "expected at least one conflict"
    hs.resolve(deal, conflicts)

    conflict_log = deal["hubspot"]["conflict_log"]
    assert conflict_log, "hubspot.conflict_log should be populated"
    kvk_entries = [e for e in conflict_log if e["field"].endswith(".kvk")]
    assert kvk_entries, conflict_log


# ---------------------------------------------------------------------------
# 4. Stale doc → Gap-5 verdict
# ---------------------------------------------------------------------------


def test_stale_doc_triggers_gap5(tmp_path, van_gog_deal_yaml):
    """A document uploaded outside its validity window fires Gap-5."""
    deal = _load_and_mark(van_gog_deal_yaml)

    docs_dir = tmp_path / "documents"
    docs_dir.mkdir()
    _make_synth_kvk_pdf(docs_dir / "kvk_partner0.pdf")

    # KvK uittreksels expire after 30 days (registry default) — backdate 400d.
    stale_date = (date.today() - timedelta(days=400)).isoformat()
    deal["documents"] = [
        {"type": "kvk_uittreksel", "path": "kvk_partner0.pdf",
         "partner_entity_idx": 0, "uploaded_at": stale_date},
    ]
    engine.parse_documents(deal, docs_dir)

    verdicts = engine.run_cross_doc_gate(deal)
    gap5 = [v for v in verdicts if v["rule"] == "Gap-5"]
    assert gap5, (
        f"expected Gap-5 (stale doc) but got "
        f"rules={sorted({v['rule'] for v in verdicts})}"
    )
    msg = gap5[0]["message"]
    assert "kvk_uittreksel" in msg
    assert "validity window" in msg


# ---------------------------------------------------------------------------
# 5. Dry-run mode leaves Drive untouched
# ---------------------------------------------------------------------------


def test_dry_run_leaves_drive_untouched(tmp_path, van_gog_deal_yaml, monkeypatch):
    """output_router dry-run via SITES_OUTPUT_ROUTER_DRY_RUN=1 must NOT write
    to the Drive base even though route() returns a plausible path."""
    # Generate a body .docx to feed to the router.
    body = tmp_path / "body.docx"
    engine.copy_body(body)
    assert body.exists()

    fake_drive = tmp_path / "drive"
    fake_drive.mkdir()

    monkeypatch.setenv(router.DRY_RUN_ENV, "1")
    artifact = router.OutputArtifact(
        src_path=body,
        slug="van-gog-grubbenvorst",
        counterparty_folder_name="Van Gog Grubbenvorst_Project_Benelux_Ops",
        doc_kind="hot",
    )
    dest = router.route(artifact, drive_base=fake_drive)

    # Returned dest is inside the fake Drive folder convention, but NOTHING
    # was actually written (drafts/ subfolder wasn't created, no copy).
    assert "Van Gog Grubbenvorst_Project_Benelux_Ops" in str(dest)
    assert not dest.exists()
    assert not (fake_drive / "Van Gog Grubbenvorst_Project_Benelux_Ops" / "drafts").exists()
    # Manifest must NOT have been written either.
    manifest = (
        fake_drive / "Van Gog Grubbenvorst_Project_Benelux_Ops"
        / "drafts" / "_manifest.json"
    )
    assert not manifest.exists()


# ---------------------------------------------------------------------------
# 6. CLI end-to-end — exercises main() which wires all stages together
# ---------------------------------------------------------------------------


def test_cli_end_to_end_writes_all_four_artifacts(tmp_path, van_gog_deal_yaml):
    """The CLI entry point runs load → hydrate (no client) → parse → gate
    → body copy → annex fill → QA + gate report. Four files must appear."""
    # Attach documents file-layout relative to deal.yaml parent.
    docs_dir = van_gog_deal_yaml.parent / "documents"
    docs_dir.mkdir(exist_ok=True)
    _make_synth_kvk_pdf(docs_dir / "kvk_partner0.pdf")
    _make_synth_ato_pdf(docs_dir / "ato_partner0.pdf")
    _make_synth_kadaster_pdf(docs_dir / "kadaster_partner1.pdf")

    # Re-write the deal.yaml with a documents block since main() reads from disk.
    deal_dict = yaml.safe_load(van_gog_deal_yaml.read_text())
    deal_dict["documents"] = [
        {"type": "kvk_uittreksel", "path": "kvk_partner0.pdf",
         "partner_entity_idx": 0, "uploaded_at": date.today().isoformat()},
        {"type": "ato_document", "path": "ato_partner0.pdf",
         "partner_entity_idx": 0, "uploaded_at": date.today().isoformat()},
        {"type": "kadaster_uittreksel", "path": "kadaster_partner1.pdf",
         "partner_entity_idx": 1, "uploaded_at": date.today().isoformat()},
    ]
    van_gog_deal_yaml.write_text(yaml.safe_dump(deal_dict, sort_keys=False))

    out_dir = tmp_path / "out"
    rc = engine.main([str(van_gog_deal_yaml), "--out-dir", str(out_dir)])
    assert rc == 0

    body = list(out_dir.glob("*_DE_HoT_Site_van-gog-grubbenvorst_v1_(DRAFT)_body.docx"))
    annex = list(out_dir.glob("*_DE_HoT_Site_van-gog-grubbenvorst_v1_(DRAFT)_annex-a.docx"))
    qa = list(out_dir.glob("*_DE_HoT_Site_van-gog-grubbenvorst_v1_qa.txt"))
    gate = list(out_dir.glob("*_DE_HoT_Site_van-gog-grubbenvorst_v1_gate-report.json"))
    assert len(body) == 1, list(out_dir.iterdir())
    assert len(annex) == 1
    assert len(qa) == 1
    assert len(gate) == 1

    # Body .docx SHA must match the template exactly (locked body rule).
    body_sha = hashlib.sha256(body[0].read_bytes()).hexdigest()
    tpl_sha = hashlib.sha256(engine.BODY_TEMPLATE.read_bytes()).hexdigest()
    assert body_sha == tpl_sha

    payload = json.loads(gate[0].read_text())
    assert payload["stage"] == "hot"
    assert isinstance(payload["verdicts"], list)
