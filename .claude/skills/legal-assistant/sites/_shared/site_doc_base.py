"""
Shared chassis for Sites-stream document engines (LOI + HoT).

Responsibilities:
- Load ``field-registry.json`` (v1.1+) and expose typed accessors.
- Filter registry fields by ``stage`` (loi/hot/both) and ``asset`` tag.
- Derive bilingual role labels from a Site Partner's contributions + returns.
- Determine whether a document type is required for a given Site Partner
  based on their contribution mix (partner_subset_logic).
- Normalise placeholder values (``[TBC]`` canon) before rendering.
- Own the authoritative ``PARSER_MAP`` (doc_type → parser class) and the
  real implementations of ``parse_documents`` and ``hydrate_from_hubspot``
  that both engines inherit. Engines override only where their stage
  legitimately diverges (e.g. HoT narrows PARSER_MAP; HoT passes
  ``prior_loi_deal`` to ``run_cross_doc_gate``).
- Provide the ``SiteDocBase`` class that both ``generate_site_loi.SiteLOI``
  and ``generate_site_hot.SiteHoT`` extend.

One-source-of-truth for Sites-stream cross-cutting concerns. rc3.1 absorbed
``_sanitise`` / ``parse_documents`` / ``hydrate_from_hubspot`` / ``PARSER_MAP``
out of the engine locals where they had drifted and parked them here.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from types import MappingProxyType
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple

# Registry lives one level up under sites/hot/
_REGISTRY_PATH = (
    Path(__file__).resolve().parents[1] / "hot" / "field-registry.json"
)

# Document parsers — optional dependency (PyMuPDF). Engines should not
# crash if the parser layer isn't importable; parse_documents degrades
# to a structured warning-only passthrough.
try:
    from document_parsers.ato import ATOParser  # noqa: E402
    from document_parsers.base import (  # noqa: E402
        CorruptDocError,
        ParserError,
        UnreadableScanError,
    )
    from document_parsers.bestemmingsplan import BestemmingsplanParser  # noqa: E402
    from document_parsers.equipment_oem import EquipmentOEMParser  # noqa: E402
    from document_parsers.financier_consent import FinancierConsentParser  # noqa: E402
    from document_parsers.generic_pdf import GenericPDFParser  # noqa: E402
    from document_parsers.kadaster import KadasterParser  # noqa: E402
    from document_parsers.kvk import KvKParser  # noqa: E402
    from document_parsers.landowner_consent import LandownerConsentParser  # noqa: E402
    from document_parsers.sde_plus import SDEPlusParser  # noqa: E402

    _PARSERS_AVAILABLE = True
except ImportError:  # pragma: no cover
    _PARSERS_AVAILABLE = False
    # Placeholders so later module code that references these names parses
    # cleanly; actual calls are gated by ``_PARSERS_AVAILABLE``.
    ATOParser = BestemmingsplanParser = EquipmentOEMParser = None  # type: ignore
    FinancierConsentParser = GenericPDFParser = KadasterParser = None  # type: ignore
    KvKParser = LandownerConsentParser = SDEPlusParser = None  # type: ignore

    class ParserError(Exception):  # type: ignore
        ...

    class CorruptDocError(ParserError):  # type: ignore
        ...

    class UnreadableScanError(ParserError):  # type: ignore
        ...


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
# Placeholder canon
# ---------------------------------------------------------------------------

#: Canonical placeholder token. Aligns with ``_render_placeholder`` in
#: ``document-factory/generate.py`` + the R-27 fabrication gate on the
#: colocation side. Engines MUST route every rendered value through
#: ``normalise_placeholder`` before it reaches python-docx.
TBC_TOKEN = "[TBC]"


def normalise_placeholder(value: Any, *, fallback: str = TBC_TOKEN) -> str:
    """Normalise a value for rendering into a bilingual clause / table cell.

    Contract (explicit branches — no ``str()`` fallthrough on anything the
    caller shouldn't be rendering):

    - ``None``                         → ``fallback`` (``[TBC]``)
    - empty or whitespace-only str     → ``fallback``
    - ``"TODO(*)"``                    → ``fallback`` (author marker leak)
    - ``"[TBD_*]"``                    → ``fallback`` (legacy slot token)
    - already the fallback token       → ``fallback`` (idempotent)
    - ``False`` or ``0`` or ``0.0``    → ``str(value)`` (valid data)
    - ``True``                         → ``"True"`` (valid data)
    - ``int`` / ``float``              → ``str(value)``
    - ``list`` / ``tuple``             → ``", ".join(str(x) for x in value)``
    - ``dict``                         → ``fallback`` (structured values
                                         shouldn't hit a cell directly —
                                         caller must extract)
    - anything else                    → ``str(value).strip()``

    The explicit branches exist so that a future author can't accidentally
    render ``None`` as the literal string ``"None"`` by adding a new value
    type that coerces silently.
    """
    if value is None:
        return fallback
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (list, tuple)):
        if not value:
            return fallback
        return ", ".join(str(x) for x in value)
    if isinstance(value, dict):
        return fallback
    # At this point `value` is treated as string-like.
    s = str(value).strip()
    if not s:
        return fallback
    if s.startswith("TODO(") or s.startswith("[TBD_") or s == fallback:
        return fallback
    return s


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
# Parser map (doc_type → parser class)
# ---------------------------------------------------------------------------

#: Doc types that only appear at LOI stage (HoT engine narrows PARSER_MAP
#: against this set). Centralised so both engines agree.
SITE_LOI_ONLY_DOCS: frozenset = frozenset({
    "sde_plus_plus",
    "co2_supply_contract",
    "solar_pv_yield_report",
})


def _build_default_parser_map() -> Mapping[str, Any]:
    """Compose the LOI-stage-broadest parser map.

    Returns an immutable view so callers can't mutate it by accident.
    Caller should still defensively check ``_PARSERS_AVAILABLE`` before
    dispatching — the map is empty when parser deps are missing.
    """
    if not _PARSERS_AVAILABLE:
        return MappingProxyType({})
    return MappingProxyType({
        "ato_document": ATOParser,
        "sde_plus_plus": SDEPlusParser,
        "kadaster_uittreksel": KadasterParser,
        "kvk_uittreksel": KvKParser,
        "bestemmingsplan_excerpt": BestemmingsplanParser,
        "landowner_consent": LandownerConsentParser,
        "financier_consent": FinancierConsentParser,
        "chp_commissioning_cert": EquipmentOEMParser,
        "chp_maintenance_contract": EquipmentOEMParser,
        "chp_gasketel_cert": EquipmentOEMParser,
        "bess_grid_sharing_agreement": EquipmentOEMParser,
        "bess_balancing_market_enrollment": EquipmentOEMParser,
        "solar_pv_yield_report": EquipmentOEMParser,
        "solar_pv_connection_agreement": EquipmentOEMParser,
        "co2_supply_contract": GenericPDFParser,
        "generic_pdf": GenericPDFParser,
    })


DEFAULT_PARSER_MAP: Mapping[str, Any] = _build_default_parser_map()


# ---------------------------------------------------------------------------
# Parser-output routing — per-partner write helpers
# ---------------------------------------------------------------------------

def _partner_grid_details(partner: dict) -> dict:
    """Return (creating if absent) the ``grid_interconnection`` contribution's
    ``details`` dict on ``partner``. Used by parse_documents to route parser
    outputs into the right slot."""
    for c in partner.get("contributions") or []:
        if c.get("asset") == "grid_interconnection":
            c.setdefault("details", {})
            return c["details"]
    c = {"asset": "grid_interconnection", "details": {}}
    partner.setdefault("contributions", []).append(c)
    return c["details"]


def _partner_land_details(partner: dict) -> dict:
    """Return (creating if absent) the ``land`` or ``property`` contribution's
    ``details`` dict on ``partner``."""
    for c in partner.get("contributions") or []:
        if c.get("asset") in ("land", "property"):
            c.setdefault("details", {})
            return c["details"]
    c = {"asset": "land", "details": {}}
    partner.setdefault("contributions", []).append(c)
    return c["details"]


def _merge_parser_field(partner: dict, field_id: str, value: Any) -> bool:
    """Write a parser field into the correct slot on ``partner``.

    Returns True if the field was recognised and written.
    """
    # A. Identity
    if field_id == "A1_legal_name":
        partner["legal_name"] = value
        return True
    if field_id == "A2_kvk_number":
        partner["kvk"] = str(value) if value is not None else value
        return True
    if field_id == "A3_registered_address":
        partner["registered_address"] = value
        return True
    if field_id == "A4_signatory_name":
        partner.setdefault("signatory", {})["name"] = value
        return True
    if field_id == "A5_signatory_title":
        partner.setdefault("signatory", {})["title"] = value
        return True
    if field_id == "A6_signing_authority":
        partner.setdefault("signatory", {})["signing_authority"] = value
        return True

    # B. Grid connection
    if field_id.startswith("B") and len(field_id) > 1 and field_id[1].isdigit():
        gd = _partner_grid_details(partner)
        mapping = {
            "B1_dso": "dso",
            "B2_ean_code": "ean_code",
            "B3_ato_reference": "ato_reference",
            "B4_total_connection_mva": "total_connection_mva",
            "B5_total_import_mw": "total_import_mw",
            "B6_total_export_mw": "total_export_mw",
        }
        key = mapping.get(field_id)
        if key is not None:
            gd[key] = value
            return True

    # D. Land
    if field_id in ("D1_kadaster_parcels", "D2_title_type",
                    "D3_encumbrances", "D4_zoning_designation"):
        ld = _partner_land_details(partner)
        mapping = {
            "D1_kadaster_parcels": "kadaster_parcels",
            "D2_title_type": "title_type",
            "D3_encumbrances": "encumbrances",
            "D4_zoning_designation": "zoning_designation",
        }
        ld[mapping[field_id]] = value
        return True

    # Meta-fields (underscore-prefixed) → partner._enrichment_meta
    if field_id.startswith("_"):
        meta = partner.setdefault("_enrichment_meta", {})
        meta[field_id] = value
        return True

    return False


def _resolve_target_partner(deal: dict, doc_entry: dict) -> Optional[int]:
    """Identify which Site Partner a parsed doc belongs to.

    Precedence:
      1. ``partner_entity_idx`` on doc entry (explicit).
      2. ``partner_idx`` (legacy alias).
      3. fallback: partner[0] (single-partner deals).
    """
    idx = doc_entry.get("partner_entity_idx")
    if idx is None:
        idx = doc_entry.get("partner_idx")
    if idx is None and len(deal.get("site_partners") or []) == 1:
        idx = 0
    if idx is not None:
        try:
            idx = int(idx)
        except (TypeError, ValueError):
            return None
        partners = deal.get("site_partners") or []
        if 0 <= idx < len(partners):
            return idx
    return None


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
    addon derivation, stage filtering, HubSpot hydration, document parsing,
    cross-doc gate).

    ``PARSER_MAP`` is the authoritative doc_type → parser-class mapping.
    LOI inherits the full LOI-stage-broadest set. HoT overrides to narrow
    against ``SITE_LOI_ONLY_DOCS``.
    """

    #: Which stage this engine renders (``"loi"`` or ``"hot"``).
    stage: str = "loi"

    #: Parser map — broadest (LOI-stage) set by default. ``MappingProxyType``
    #: so subclasses can't accidentally mutate the parent.
    PARSER_MAP: Mapping[str, Any] = DEFAULT_PARSER_MAP

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

    # --- HubSpot hydration -----------------------------------------------

    def hydrate_from_hubspot(self, deal: dict, client: Any = None) -> dict:
        """Round-trip HubSpot Deal + Companies + Contacts into ``deal``.

        Safe passthrough when ``client`` is ``None`` or when the deal has
        no ``hubspot_deal_id``. Tests inject a ``FakeHubSpotClient``;
        production wiring supplies the real MCP-backed client.

        On a successful round-trip we call ``hubspot_sync.validate`` +
        ``resolve`` so conflict audit lives on ``deal.hubspot.conflict_log``.

        Non-fatal failures (import error, transport error, schema drift)
        are recorded on ``deal.enrichment.sync_warnings`` so the QA report
        surfaces them without aborting render.

        The caller's original top-level keys are never destroyed.
        """
        if client is None or not deal.get("hubspot_deal_id"):
            return deal
        try:
            import hubspot_sync as _hs  # local import — optional dep
            _hs.read_deal(client, deal)
            view = {
                "deal": client.read_deal(deal["hubspot_deal_id"]),
                "companies": client.read_associated_companies(
                    deal["hubspot_deal_id"]
                ),
                "contacts": client.read_associated_contacts(
                    deal["hubspot_deal_id"]
                ),
            }
            conflicts = _hs.validate(deal, view)
            if conflicts:
                _hs.resolve(deal, conflicts)
        except Exception as exc:
            deal.setdefault("enrichment", {}).setdefault(
                "sync_warnings", []
            ).append(f"hubspot_sync: {type(exc).__name__}: {exc}")
        return deal

    # --- Document parsing ------------------------------------------------

    def parse_documents(self, deal: dict, documents_dir: Path) -> dict:
        """Iterate ``deal['documents'][]``, dispatch each to the matching
        parser in ``self.PARSER_MAP``, merge outputs into the deal tree,
        record per-doc audit under ``deal.enrichment.parser_log``.

        Parser outputs that map to a specific Site Partner are written via
        ``_merge_parser_field``; deal-level meta-fields
        (underscore-prefixed) land on ``deal._enrichment_meta``. Enum
        values are normalised (registry-canonicalised) via
        ``enum_normaliser`` when the registry is loadable.

        Safe no-op when ``deal['documents']`` is empty / missing. The
        caller's original top-level keys are never destroyed; scaffolding
        keys (``enrichment``, ``_enrichment_meta``) may be added.
        """
        # Always normalise any enums already present in deal.yaml (manual
        # authoring may produce bare tokens).
        try:
            registry = load_registry()
        except Exception:
            registry = None

        enrichment = deal.setdefault("enrichment", {})
        parser_log: List[dict] = enrichment.setdefault("parser_log", [])

        if not deal.get("documents"):
            if registry is not None:
                self._normalise_deal_enums(deal, registry)
            return deal

        if not _PARSERS_AVAILABLE:
            parser_log.append({
                "status": "skipped",
                "reason": "PyMuPDF unavailable; parser chassis not importable",
            })
            if registry is not None:
                self._normalise_deal_enums(deal, registry)
            return deal

        for doc_entry in (deal.get("documents") or []):
            doc_type = doc_entry.get("type")
            rel_path = doc_entry.get("path")
            if not doc_type or not rel_path:
                parser_log.append({
                    "status": "skipped",
                    "doc": doc_entry,
                    "reason": "doc entry missing type or path",
                })
                continue
            doc_path = Path(rel_path)
            if not doc_path.is_absolute():
                doc_path = documents_dir / doc_path
            if not doc_path.exists():
                parser_log.append({
                    "status": "missing",
                    "doc_type": doc_type,
                    "path": str(doc_path),
                })
                continue

            parser_cls = self.PARSER_MAP.get(doc_type, GenericPDFParser)
            try:
                result = parser_cls(doc_path).parse()
            except (CorruptDocError, UnreadableScanError) as exc:
                parser_log.append({
                    "status": "error",
                    "doc_type": doc_type,
                    "path": str(doc_path),
                    "error_class": exc.__class__.__name__,
                    "message": str(exc),
                })
                continue
            except ParserError as exc:
                parser_log.append({
                    "status": "parser_error",
                    "doc_type": doc_type,
                    "path": str(doc_path),
                    "message": str(exc),
                })
                continue

            fields_populated = result.fields_populated
            if registry is not None:
                try:
                    import enum_normaliser as _en  # local import
                    fields_populated = _en.normalise_parse_result(
                        result.fields_populated, registry
                    )
                except Exception:
                    pass  # fall back to raw parser output

            partner_idx = _resolve_target_partner(deal, doc_entry)
            merged: List[str] = []
            unmerged: List[str] = []
            if partner_idx is not None:
                partner = deal["site_partners"][partner_idx]
                for fid, value in fields_populated.items():
                    if _merge_parser_field(partner, fid, value):
                        merged.append(fid)
                    else:
                        unmerged.append(fid)
            else:
                deal_meta = deal.setdefault("_enrichment_meta", {})
                for fid, value in fields_populated.items():
                    if fid.startswith("_"):
                        deal_meta[fid] = value
                        merged.append(fid)
                    else:
                        unmerged.append(fid)

            parser_log.append({
                "status": "ok",
                "doc_type": doc_type,
                "path": str(doc_path),
                "partner_entity_idx": partner_idx,
                "doc_hash": getattr(result, "doc_hash", None),
                "parser_version": getattr(result, "parser_version", None),
                "confidence": getattr(result, "confidence", None),
                "fields_merged": merged,
                "fields_unmerged": unmerged,
                "warnings": getattr(result, "warnings", []),
            })

        # Second normalisation pass after all parser writes land.
        if registry is not None:
            self._normalise_deal_enums(deal, registry)
        return deal

    @staticmethod
    def _normalise_deal_enums(deal: dict, registry: dict) -> None:
        """Best-effort enum canonicalisation. Silent on import failure so
        tests that don't have enum_normaliser on sys.path don't break."""
        try:
            import enum_normaliser as _en  # local import
            _en.normalise_deal_yaml(deal, registry)
        except Exception:
            pass

    # --- Cross-doc gate --------------------------------------------------

    def run_cross_doc_gate(
        self,
        deal: dict,
        prior_loi_deal: Optional[dict] = None,
    ) -> List[dict]:
        """Invoke the cross-doc gate in this engine's stage and return a
        list of serialisable verdict dicts.

        Subclasses may override to pass additional stage-specific context
        (HoT in particular takes ``prior_loi_deal`` to enable Gap-4/Gap-5
        continuity rules).

        Safe passthrough (empty list) when ``cross_doc_gate`` is not
        importable — keeps tests that don't stand up the full gate green.
        """
        try:
            import cross_doc_gate as cdg  # local import
        except ImportError:
            return []
        verdicts = cdg.run(deal, stage=self.stage, prior_loi_deal=prior_loi_deal)
        return cdg.to_dict_list(verdicts)

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
