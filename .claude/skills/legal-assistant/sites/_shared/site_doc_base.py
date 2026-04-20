"""
Shared chassis for Sites-stream document engines (LOI + HoT).

Responsibilities:
- Load ``field-registry.json`` (v1.1+) and expose typed accessors.
- Filter registry fields by ``stage`` (loi/hot/both) and ``asset`` tag.
- Derive bilingual role labels from a Site Partner's contributions + returns.
- Determine whether a document type is required for a given Site Partner
  based on their contribution mix (partner_subset_logic).
- Provide the ``SiteDocBase`` abstract base class that both
  ``generate_site_loi.SiteLOI`` and ``generate_site_hot.SiteHoT`` extend.

The actual engines stay self-contained; this module centralises the
cross-cutting concerns so they don't drift between LOI and HoT.

Phase B6 of the sites-stream plan.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

# Registry lives one level up under sites/hot/
_REGISTRY_PATH = (
    Path(__file__).resolve().parents[1] / "hot" / "field-registry.json"
)

# ---------------------------------------------------------------------------
# Role-label mappings
# ---------------------------------------------------------------------------

#: Asset-class or return-value → (role label EN, role label NL).
#: Keep this dict authoritative; engines MUST NOT hard-code strings.
ROLE_LABEL_MAP: Dict[str, Tuple[str, str]] = {
    # Contributions
    "grid_interconnection": ("Grid Contributor", "Netbijdrager"),
    "gas_connection": ("Gas Contributor", "Gasbijdrager"),
    "land": ("Landowner", "Grondeigenaar"),
    "property": ("Landowner", "Grondeigenaar"),
    "equipment_chp": ("Equipment Contributor", "Apparatuurbijdrager"),
    "equipment_bess": ("Equipment Contributor", "Apparatuurbijdrager"),
    "equipment_solar_pv": ("Equipment Contributor", "Apparatuurbijdrager"),
    # Returns (value) → role
    "energy_heat": ("Heat Offtaker", "Warmteafnemer"),
    "energy_power": ("Power Offtaker", "Energieafnemer"),
    "energy_storage": ("Storage Offtaker", "Opslagafnemer"),
    "energy_backup": ("Backup Offtaker", "Back-upafnemer"),
    "equity": ("Equity Partner", "Aandelenpartner"),
    "money": ("Compensation Recipient", "Vergoedingsontvanger"),
}


# ---------------------------------------------------------------------------
# Registry accessors
# ---------------------------------------------------------------------------

def load_registry(path: Optional[Path] = None) -> dict:
    """Load field-registry.json and validate basic shape."""
    reg_path = path or _REGISTRY_PATH
    with open(reg_path, "r", encoding="utf-8") as f:
        reg = json.load(f)
    # Minimum structural assertions — catch corruption early.
    for key in ("version", "sections", "supporting_documents"):
        if key not in reg:
            raise ValueError(f"registry missing required top-level key: {key}")
    return reg


def iter_fields(registry: dict) -> Iterable[Tuple[str, str, dict]]:
    """Yield ``(section_id, field_id, field_dict)`` for every field."""
    for sec_id, sec in registry.get("sections", {}).items():
        if not isinstance(sec, dict):
            continue
        for field_id, field_def in sec.get("fields", {}).items():
            yield sec_id, field_id, field_def


def fields_by_stage(registry: dict, stage: str) -> List[Tuple[str, str, dict]]:
    """Return fields whose ``stage`` matches ``stage`` (or 'both')."""
    if stage not in ("loi", "hot"):
        raise ValueError(f"stage must be 'loi' or 'hot', got {stage!r}")
    out: List[Tuple[str, str, dict]] = []
    for sec_id, fid, fdef in iter_fields(registry):
        tag = fdef.get("stage")
        if tag == stage or tag == "both":
            out.append((sec_id, fid, fdef))
    return out


def fields_by_asset(registry: dict, asset: str) -> List[Tuple[str, str, dict]]:
    """Return fields whose ``asset`` matches ``asset``."""
    out: List[Tuple[str, str, dict]] = []
    for sec_id, fid, fdef in iter_fields(registry):
        if fdef.get("asset") == asset:
            out.append((sec_id, fid, fdef))
    return out


def required_field_ids(registry: dict, stage: Optional[str] = None) -> List[str]:
    """IDs of all required fields; optionally filtered by stage."""
    out: List[str] = []
    for sec_id, fid, fdef in iter_fields(registry):
        if not fdef.get("required"):
            continue
        if stage and fdef.get("stage") not in (stage, "both"):
            continue
        out.append(fid)
    return out


# ---------------------------------------------------------------------------
# Role-label derivation
# ---------------------------------------------------------------------------

def _dedup(items: Iterable[Tuple[str, str]]) -> Tuple[List[str], List[str]]:
    """Preserve insertion order; dedupe on the EN label."""
    seen: set = set()
    en_out: List[str] = []
    nl_out: List[str] = []
    for en, nl in items:
        if en in seen:
            continue
        seen.add(en)
        en_out.append(en)
        nl_out.append(nl)
    return en_out, nl_out


def derive_role_labels(site_partner: dict) -> Tuple[List[str], List[str]]:
    """Return ``(en_labels, nl_labels)`` for a Site Partner.

    Labels are derived from the partner's ``contributions[].asset`` and
    ``returns[].value`` using ``ROLE_LABEL_MAP``. Duplicates are removed
    (insertion-order preserved).

    Site-sourcing semantics (Van Gog §1.4 compatible):
    - Grid Contributor appears if any contribution is grid_interconnection.
    - Landowner appears if any contribution is land or property.
    - Heat Offtaker appears if any return is energy_heat.
    - Equipment Contributor appears for equipment_* contributions unless
      the engine is in "legacy role-label" mode where those partners are
      also Grid Contributors (caller's choice; default: include).

    Returns empty lists if the partner has no contributions or returns
    that map to a known label.
    """
    labels: List[Tuple[str, str]] = []
    for contrib in site_partner.get("contributions") or []:
        asset = contrib.get("asset")
        if asset in ROLE_LABEL_MAP:
            labels.append(ROLE_LABEL_MAP[asset])
    for ret in site_partner.get("returns") or []:
        value = ret.get("value")
        if value in ROLE_LABEL_MAP:
            labels.append(ROLE_LABEL_MAP[value])
    return _dedup(labels)


def derive_addon_flags(deal: dict) -> Dict[str, bool]:
    """Derive the addon-activation flags from the deal.yaml contribution
    mix. Engines use these to gate optional template blocks."""
    site_partners = deal.get("site_partners") or []
    flags: Dict[str, bool] = {
        "bess_co_development": False,
        "btm_renewables": False,
        "chp_present": False,
        "gas_present": False,
    }
    for sp in site_partners:
        for c in sp.get("contributions") or []:
            asset = c.get("asset")
            if asset == "equipment_bess":
                flags["bess_co_development"] = True
            if asset == "equipment_solar_pv":
                flags["btm_renewables"] = True
            if asset == "equipment_chp":
                flags["chp_present"] = True
            if asset == "gas_connection":
                flags["gas_present"] = True
    # Merge with any explicit deal.addons overrides (deal.yaml takes precedence
    # if operator flagged something manually before derivation).
    explicit = deal.get("addons") or {}
    for k, v in explicit.items():
        if isinstance(v, bool):
            flags[k] = v
    return flags


# ---------------------------------------------------------------------------
# Partner-subset logic for supporting_documents
# ---------------------------------------------------------------------------

#: Map supporting_documents entry → required contribution asset class.
#: If a doc is required but the partner doesn't contribute that asset,
#: the doc is not required for that partner.
#: Source: registry::_partner_subset_logic narrative + verifies[] hints.
_DOC_TO_ASSET: Dict[str, Optional[str]] = {
    "kvk_uittreksel": None,               # required for every Site Partner
    "ato_document": "grid_interconnection",
    "kadaster_uittreksel": "land",
    "bestemmingsplan_excerpt": "land",
    "landowner_consent": "land",
    "financier_consent": "land",
    "site_plan": "land",
    "bess_grid_sharing_agreement": "equipment_bess",
    "bess_balancing_market_enrollment": "equipment_bess",
    "chp_commissioning_cert": "equipment_chp",
    "chp_maintenance_contract": "equipment_chp",
    "chp_gasketel_cert": "equipment_chp",
    "solar_pv_yield_report": "equipment_solar_pv",
    "solar_pv_connection_agreement": "equipment_solar_pv",
    "co2_supply_contract": None,          # grower-level, not asset-tied
}


def docs_required_for_partner(
    registry: dict,
    site_partner: dict,
) -> List[str]:
    """Return the IDs of supporting_documents entries required for THIS
    partner given their contribution mix. Applies partner_subset_logic."""
    sd = registry.get("supporting_documents", {})
    contribs = site_partner.get("contributions") or []
    partner_assets = {c.get("asset") for c in contribs if c.get("asset")}

    required: List[str] = []
    for doc_id, doc_spec in sd.items():
        if doc_id.startswith("_"):
            continue
        if not doc_spec.get("required"):
            continue
        linked_asset = _DOC_TO_ASSET.get(doc_id)
        if linked_asset is None:
            # Required for everybody (identity doc).
            required.append(doc_id)
        elif linked_asset in partner_assets:
            required.append(doc_id)
    return required


# ---------------------------------------------------------------------------
# Validity window helper
# ---------------------------------------------------------------------------

def doc_is_stale(
    registry: dict,
    doc_entry: dict,
    as_of_iso_date: Optional[str] = None,
) -> bool:
    """Return True if ``doc_entry`` (as recorded in deal.yaml::documents[])
    is past its validity window per the registry's validity_days."""
    from datetime import date as _date, timedelta

    doc_type = doc_entry.get("type")
    if not doc_type:
        return False
    sd = registry.get("supporting_documents", {})
    spec = sd.get(doc_type)
    if not spec:
        return False
    validity_days = spec.get("validity_days")
    if validity_days is None:
        return False  # no expiry
    uploaded_at = doc_entry.get("uploaded_at")
    if not uploaded_at:
        return False  # can't determine without upload date
    # Parse ISO date (YYYY-MM-DD) — accept full timestamps too.
    try:
        if "T" in uploaded_at:
            uploaded_at = uploaded_at.split("T", 1)[0]
        uploaded_date = _date.fromisoformat(uploaded_at)
    except ValueError:
        return False
    as_of = _date.fromisoformat(as_of_iso_date) if as_of_iso_date else _date.today()
    return (as_of - uploaded_date) > timedelta(days=validity_days)


# ---------------------------------------------------------------------------
# SiteDocBase — abstract base class for LOI + HoT engines
# ---------------------------------------------------------------------------

@dataclass
class EnrichmentReport:
    """Summary of enrichment + validation results after a run."""
    fields_resolved: Dict[str, Any] = field(default_factory=dict)
    fields_tbc: List[str] = field(default_factory=list)
    parser_warnings: List[str] = field(default_factory=list)
    sync_conflicts: List[dict] = field(default_factory=list)


class SiteDocBase:
    """Shared orchestration surface for LOI + HoT engines.

    Subclasses implement ``render_document(deal) -> Document`` — everything
    else lives here (deal loading, registry access, role-label decoration,
    addon derivation, stage filtering, QA hooks).
    """

    #: Which stage this engine renders (``"loi"`` or ``"hot"``).
    stage: str = "loi"

    def __init__(self, registry_path: Optional[Path] = None):
        self.registry = load_registry(registry_path)

    # --- Deal lifecycle ---------------------------------------------------

    @staticmethod
    def load_deal(deal_yaml_path: Path) -> dict:
        """Load + validate a deal.yaml."""
        import yaml
        with open(deal_yaml_path, "r", encoding="utf-8") as f:
            deal = yaml.safe_load(f)
        schema_version = deal.get("deal_yaml_schema_version")
        if schema_version != "1.0":
            raise ValueError(
                f"deal.yaml schema version mismatch: got {schema_version!r}, "
                "expected '1.0'"
            )
        return deal

    def decorate_deal(self, deal: dict) -> dict:
        """Attach derived fields (role labels, addon flags) to the deal.
        Non-destructive — returns the same deal dict (mutations allowed)."""
        for sp in deal.get("site_partners") or []:
            en, nl = derive_role_labels(sp)
            sp["_role_labels_en"] = en
            sp["_role_labels_nl"] = nl
        deal["_addons_effective"] = derive_addon_flags(deal)
        return deal

    # --- Stage filtering --------------------------------------------------

    def stage_fields(self) -> List[Tuple[str, str, dict]]:
        """Fields applicable to this engine's stage."""
        return fields_by_stage(self.registry, self.stage)

    # --- Integration hooks (stubbed; Phase B5/B7/B8 fill in) --------------

    def hydrate_from_hubspot(self, deal: dict) -> dict:
        """TODO(Phase B7 / hubspot_sync.py): round-trip read + validate +
        write_enrichment + conflict resolution. Passthrough for now."""
        return deal

    def parse_documents(self, deal: dict, documents_dir: Path) -> dict:
        """TODO(Phase B5 / document_parsers): iterate deal['documents'][],
        invoke parsers, populate enrichment targets. Passthrough for now."""
        return deal

    def run_cross_doc_gate(self, deal: dict) -> list[dict]:
        """TODO(Phase B8 / cross_doc_gate.py): run rules + return verdicts.
        Empty list for now."""
        return []

    # --- Enrichment reporting --------------------------------------------

    def build_enrichment_report(self, deal: dict) -> EnrichmentReport:
        """Summarise the state of required fields for the current stage."""
        report = EnrichmentReport()
        req_ids = required_field_ids(self.registry, stage=self.stage)
        # Registry field IDs don't map directly to deal.yaml paths — for v1
        # we walk the structured site_partners[].contributions[].details and
        # flag any remaining None/[TBC] values as TBC.
        tbc = _walk_for_tbc(deal)
        report.fields_tbc = tbc
        return report

    # --- Template method --------------------------------------------------

    def render_document(self, deal: dict):
        raise NotImplementedError("subclass must implement render_document")


def _walk_for_tbc(obj, path: str = "") -> List[str]:
    """Walk a deal dict; return a list of dotted paths where values are
    None or the literal string ``[TBC]``. Used for Gap-1 gate previews."""
    out: List[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.startswith("_"):
                continue  # internal / derived fields
            sub = f"{path}.{k}" if path else k
            out.extend(_walk_for_tbc(v, sub))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            sub = f"{path}[{i}]"
            out.extend(_walk_for_tbc(v, sub))
    else:
        if obj is None or obj == "[TBC]":
            out.append(path)
    return out
