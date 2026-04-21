"""HubSpot bilateral sync for Sites-stream deal.yaml.

Reads Deal + associated Companies + Contacts from HubSpot; resolves
conflicts against parsed-doc / LOI-intake per the newest-authoritative
chain (parsed_doc > HubSpot > LOI intake); writes enrichment-derived
values back to HubSpot as property updates.

Per plan ``deal_yaml_schema.md``: "HubSpot - deal.yaml field map".

Data-authority chain (implemented here + cross-doc gate ``DataAcc-1..3``):

    Parsed document (ATO, Kadaster, KvK extract, SDE++ letter)
      > HubSpot (SoR for CRM identity & pipeline state)
        > LOI intake (manual SAL entry)
          > Vragenformulier (legacy intake surface)

If parsed doc disagrees with HubSpot, doc wins AND updates HubSpot with
audit entry. If HubSpot disagrees with LOI intake, HubSpot wins AND
corrects deal.yaml with audit entry.

Phase B7 of the sites-stream plan.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Field map - HubSpot property -> deal.yaml path (dotted / path-expression)
#
# Per `deal_yaml_schema.md`: "HubSpot - deal.yaml field map (canonical)".
# Identity + pipeline state is sourced from HubSpot Deal; Site Partners
# from associated Companies; Signatories from associated Contacts.
# Unmapped HubSpot properties are preserved in ``hubspot.raw_extra``.
# ---------------------------------------------------------------------------

HUBSPOT_FIELD_MAP: Dict[str, str] = {
    # Identity / pipeline state
    "dealname": "hubspot.dealname",
    "pipeline": "hubspot.pipeline",
    "dealstage": "hubspot.dealstage",
    "hs_lastmodifieddate": "hubspot.hs_lastmodifieddate",
    # Ownership
    "hubspot_owner_id": "owner.hubspot_owner_id",
    # Archetype + commercial envelope
    "type_of_deal": "deal_archetype",
    "dealtype": "dealtype",
    "deal_value": "commercial.deal_value_eur",
    "deal_currency_code": "commercial.currency",
    "contract_capacity___available__mw_": "commercial.contract_mw_available",
    "contract_capacity___potential__mw_": "commercial.contract_mw_potential",
    # Heat-specific (enriched back after ATO-doc parse)
    "what_temperature_do_you_need_for_your_heat_system_": (
        "site_partners[?heat].returns[energy_heat].details.heat_supply_temp_c"
    ),
    "what_s_your_approximate_heat_capacity__mwth___": (
        "site_partners[?heat].returns[energy_heat].details.mwth"
    ),
    "heat_utilisation_hours": (
        "site_partners[?heat].returns[energy_heat].details.annual_utilisation_hours"
    ),
    # Location
    "where_is_your_site_located_____city___country": "locations[0].address",
    # Ownership / legacy intake
    "site_ownership_deal": (
        "site_partners[?landowner].contributions[land].instrument"
    ),
    "how_do_you_currently_produce_heat_": "deal_meta.legacy_heat_source",
    "full_site___expected_launch_date": "timeline.expected_launch_date",
}

#: HubSpot properties the engine is NEVER allowed to write back. Identity +
#: pipeline state transitions happen only in the HubSpot UI.
NEVER_WRITE: frozenset = frozenset(
    {
        "hubspot_deal_id",
        "dealstage",
        "pipeline",
        "dealname",
        "hs_lastmodifieddate",
    }
)


# ---------------------------------------------------------------------------
# Conflict record
# ---------------------------------------------------------------------------


@dataclass
class Conflict:
    """A detected discrepancy between local deal.yaml and HubSpot-of-record.

    Attributes:
        field_path:       Dotted path inside deal.yaml.
        hubspot_property: Canonical HubSpot property name.
        local_value:      Current value in deal.yaml.
        hubspot_value:    Current value in HubSpot.
        resolution:       One of ``hubspot_wins`` / ``doc_wins`` / ``manual``.
        source_doc:       Parsed document path that justifies ``doc_wins``.
        at:               ISO8601 timestamp of detection.
    """

    field_path: str
    hubspot_property: str
    local_value: Any
    hubspot_value: Any
    resolution: str = "manual"
    source_doc: Optional[str] = None
    at: str = ""

    def to_audit_entry(self) -> Dict[str, Any]:
        """Serialise to the structure appended to ``hubspot.conflict_log``."""
        return {
            "field": self.field_path,
            "hubspot_property": self.hubspot_property,
            "local_value": self.local_value,
            "hubspot_value": self.hubspot_value,
            "resolution": self.resolution,
            "source_doc": self.source_doc,
            "at": self.at or _now_iso(),
        }


def _now_iso() -> str:
    """Return current UTC time as ISO8601 string (seconds precision)."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


# ---------------------------------------------------------------------------
# Path helpers - dotted path get / set for nested dicts + list indices
# ---------------------------------------------------------------------------


def _set_path(target: dict, path: str, value: Any) -> None:
    """Set ``value`` at dotted ``path`` inside ``target``, creating keys.

    Supports:
        ``a.b.c``             -> nested dict keys
        ``a.b[0].c``          -> numeric list indices (extends list w/ None)

    Path-expressions with selectors (``[?heat]``, ``[energy_heat]``) are NOT
    resolved here; enrichment write-back handles those separately via
    ``write_enrichment`` which walks the domain structure.
    """
    if not path:
        raise ValueError("empty path")
    parts = _tokenize(path)
    cur: Any = target
    for i, part in enumerate(parts):
        is_last = i == len(parts) - 1
        if isinstance(part, int):
            if not isinstance(cur, list):
                raise TypeError(
                    f"path expects list at position {i} but got {type(cur).__name__}"
                )
            while len(cur) <= part:
                cur.append(None)
            if is_last:
                cur[part] = value
            else:
                if cur[part] is None:
                    nxt = parts[i + 1]
                    cur[part] = [] if isinstance(nxt, int) else {}
                cur = cur[part]
        else:
            if not isinstance(cur, dict):
                raise TypeError(
                    f"path expects dict at position {i} but got {type(cur).__name__}"
                )
            if is_last:
                cur[part] = value
            else:
                if part not in cur or cur[part] is None:
                    nxt = parts[i + 1]
                    cur[part] = [] if isinstance(nxt, int) else {}
                cur = cur[part]


def _get_path(target: dict, path: str, default: Any = None) -> Any:
    """Return value at dotted ``path`` inside ``target`` or ``default``.

    Safe: never raises on missing keys / out-of-range indices.
    """
    try:
        parts = _tokenize(path)
    except ValueError:
        return default
    cur: Any = target
    for part in parts:
        if isinstance(part, int):
            if not isinstance(cur, list) or part >= len(cur):
                return default
            cur = cur[part]
        else:
            if not isinstance(cur, dict) or part not in cur:
                return default
            cur = cur[part]
    return cur


def _tokenize(path: str) -> List[Any]:
    """Tokenize ``a.b[0].c`` -> ``["a", "b", 0, "c"]``.

    Selector expressions like ``[?heat]`` or ``[energy_heat]`` are
    tokenised as string keys (callers must handle) - ``_set_path`` itself
    rejects those.
    """
    out: List[Any] = []
    buf = ""
    i = 0
    while i < len(path):
        ch = path[i]
        if ch == ".":
            if buf:
                out.append(buf)
                buf = ""
        elif ch == "[":
            if buf:
                out.append(buf)
                buf = ""
            j = path.find("]", i)
            if j == -1:
                raise ValueError(f"unclosed [ in path: {path!r}")
            inner = path[i + 1 : j]
            if inner.isdigit():
                out.append(int(inner))
            else:
                # Selector or string key - stored as raw string for caller.
                out.append(inner)
            i = j
        else:
            buf += ch
        i += 1
    if buf:
        out.append(buf)
    return out


# ---------------------------------------------------------------------------
# HubSpot client surface
# ---------------------------------------------------------------------------


class HubSpotClient:
    """Abstract client surface.

    Real implementation calls the HubSpot MCP server; for testability
    the engine accepts a client instance so tests can pass a mock
    (see ``tests/test_hubspot_sync.py::FakeHubSpotClient``).
    """

    def read_deal(self, deal_id: int) -> dict:
        """Return Deal properties dict."""
        raise NotImplementedError

    def read_associated_companies(self, deal_id: int) -> List[dict]:
        """Return list of Company objects associated with the Deal."""
        raise NotImplementedError

    def read_associated_contacts(self, deal_id: int) -> List[dict]:
        """Return list of Contact objects associated with the Deal.

        Contacts are matched to Companies via ``associated_company_id``
        field on each contact dict (fake client convention).
        """
        raise NotImplementedError

    def update_deal_properties(self, deal_id: int, updates: Dict[str, Any]) -> None:
        """Write property updates back to the Deal."""
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Read: hydrate deal.yaml from HubSpot
# ---------------------------------------------------------------------------

# Properties we don't explicitly map but preserve under hubspot.raw_extra.
_PRESERVE_UNMAPPED = True


def read_deal(client: HubSpotClient, deal: dict) -> dict:
    """Hydrate ``deal`` in place from HubSpot.

    Populates:
      - ``hubspot.*``                   (identity / pipeline state)
      - ``owner.hubspot_owner_id``
      - ``deal_archetype`` / ``dealtype``
      - ``commercial.*`` envelope fields
      - ``locations[0].address`` (best-effort; Kadaster enriches later)
      - ``site_partners[]``             (one per associated Company)
      - ``site_partners[].signatory``   (first associated Contact per company)
      - ``hubspot.raw_extra``           (unmapped properties, audit-only)

    Returns the hydrated dict (same object).
    """
    deal_id = deal.get("hubspot_deal_id")
    if deal_id is None:
        raise ValueError("deal.hubspot_deal_id is required before read_deal")

    deal_props = client.read_deal(deal_id)
    companies = client.read_associated_companies(deal_id)
    contacts = client.read_associated_contacts(deal_id)

    # ------------------------------------------------------------------
    # Apply Deal-level field map
    # ------------------------------------------------------------------
    raw_extra: Dict[str, Any] = {}
    for prop, val in deal_props.items():
        if prop in HUBSPOT_FIELD_MAP:
            target_path = HUBSPOT_FIELD_MAP[prop]
            # Selector paths (contain "[?") are only reachable once
            # site_partners exist; skip here - set after partner hydration.
            if "[?" in target_path:
                raw_extra.setdefault("_pending_selector", {})[prop] = val
                continue
            try:
                _set_path(deal, target_path, val)
            except (TypeError, ValueError):
                raw_extra[prop] = val
        else:
            if _PRESERVE_UNMAPPED:
                raw_extra[prop] = val

    if raw_extra:
        _set_path(deal, "hubspot.raw_extra", raw_extra)

    deal.setdefault("hubspot", {})["last_sync_at"] = _now_iso()

    # ------------------------------------------------------------------
    # Site partners - one per associated Company
    # ------------------------------------------------------------------
    partners: List[dict] = []
    for co in companies:
        sp: Dict[str, Any] = {
            "entity_id": co.get("id"),
            "legal_name": co.get("name"),
            "kvk": co.get("kvk"),
            "registered_address": co.get("address"),
            "website": co.get("domain") or co.get("website"),
            "contributions": [],
            "returns": [],
        }
        # First contact associated with this company becomes the signatory.
        for ct in contacts:
            if ct.get("associated_company_id") == co.get("id"):
                first = ct.get("firstname", "") or ""
                last = ct.get("lastname", "") or ""
                full_name = (first + " " + last).strip() or ct.get("name")
                sp["signatory"] = {
                    "contact_id": ct.get("id"),
                    "name": full_name,
                    "title": ct.get("jobtitle"),
                    "email": ct.get("email"),
                    "signing_authority": ct.get("signing_authority", "pending_poa"),
                }
                break
        partners.append(sp)

    deal["site_partners"] = partners
    return deal


# ---------------------------------------------------------------------------
# Validate + resolve conflicts
# ---------------------------------------------------------------------------


def validate(deal: dict, hubspot_view: dict) -> List[Conflict]:
    """Compare ``deal`` against a HubSpot-of-record snapshot.

    ``hubspot_view`` has shape::

        {
            "deal": {<deal properties>},
            "companies": [<company dicts>],
            "contacts": [<contact dicts>],
        }

    Returns a list of :class:`Conflict` with ``resolution`` unset
    (caller invokes :func:`resolve`).
    """
    conflicts: List[Conflict] = []
    hs_deal = hubspot_view.get("deal", {}) or {}

    # ------------------------------------------------------------------
    # Deal-level simple scalar comparisons
    # ------------------------------------------------------------------
    for prop, target_path in HUBSPOT_FIELD_MAP.items():
        if "[?" in target_path:
            continue  # handled under company/partner path
        if prop not in hs_deal:
            continue
        hs_val = hs_deal[prop]
        local_val = _get_path(deal, target_path)
        if local_val is None and hs_val in (None, ""):
            continue
        if _values_equal(local_val, hs_val):
            continue
        conflicts.append(
            Conflict(
                field_path=target_path,
                hubspot_property=prop,
                local_value=local_val,
                hubspot_value=hs_val,
                at=_now_iso(),
            )
        )

    # ------------------------------------------------------------------
    # Companies - legal_name + KvK per partner (positional match)
    # ------------------------------------------------------------------
    local_partners = deal.get("site_partners", []) or []
    hs_companies = hubspot_view.get("companies", []) or []

    # DataAcc-1: Van Gog expects 3 but HubSpot shows 0 - surface as conflict.
    if len(local_partners) != len(hs_companies):
        conflicts.append(
            Conflict(
                field_path="site_partners",
                hubspot_property="associated_companies_count",
                local_value=len(local_partners),
                hubspot_value=len(hs_companies),
                at=_now_iso(),
            )
        )

    # Match companies by entity_id when possible, else positionally.
    hs_by_id = {c.get("id"): c for c in hs_companies if c.get("id") is not None}
    for idx, sp in enumerate(local_partners):
        ent_id = sp.get("entity_id")
        hs_co = hs_by_id.get(ent_id) or (
            hs_companies[idx] if idx < len(hs_companies) else None
        )
        if hs_co is None:
            continue

        # legal_name
        if sp.get("legal_name") != hs_co.get("name"):
            conflicts.append(
                Conflict(
                    field_path=f"site_partners[{idx}].legal_name",
                    hubspot_property="Company.name",
                    local_value=sp.get("legal_name"),
                    hubspot_value=hs_co.get("name"),
                    at=_now_iso(),
                )
            )
        # kvk
        if sp.get("kvk") and hs_co.get("kvk") and sp.get("kvk") != hs_co.get("kvk"):
            conflicts.append(
                Conflict(
                    field_path=f"site_partners[{idx}].kvk",
                    hubspot_property="Company.kvk",
                    local_value=sp.get("kvk"),
                    hubspot_value=hs_co.get("kvk"),
                    at=_now_iso(),
                )
            )

    return conflicts


def _values_equal(a: Any, b: Any) -> bool:
    """Loose equality: treat None/empty-string as equivalent, compare numbers
    permissively (int/float) and strings case-insensitive."""
    if a is None and (b is None or b == ""):
        return True
    if b is None and a == "":
        return True
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return float(a) == float(b)
    if isinstance(a, str) and isinstance(b, str):
        return a.strip().lower() == b.strip().lower()
    return a == b


#: Identity fields: HubSpot always wins, no question.
_IDENTITY_FIELDS: frozenset = frozenset(
    {
        "hubspot.dealname",
        "hubspot.pipeline",
        "hubspot.dealstage",
        "hubspot.hs_lastmodifieddate",
        "owner.hubspot_owner_id",
        "deal_archetype",
        "dealtype",
    }
)

#: Enriched asset fields: parsed doc wins (doc_wins) when a source_doc is
#: present on the Conflict; else defaults to HubSpot.
_ENRICHED_FIELDS_PREFIXES: tuple = (
    "locations[",
    "site_partners[",
    "commercial.contract_mw_",
    "commercial.deal_value_eur",
)


def resolve(deal: dict, conflicts: List[Conflict]) -> dict:
    """Resolve conflicts per the data-authority chain.

    Mutates ``deal`` in place:
      - Identity fields -> HubSpot value wins; local overwritten.
      - Enriched asset fields -> if conflict has ``source_doc`` set,
        local (doc-backed) value wins; else HubSpot wins.
      - All resolutions are appended as audit entries to
        ``deal.hubspot.conflict_log`` (also ``deal.enrichment.conflict_log``
        for backward compatibility with cross-doc gate).

    Returns ``deal``.
    """
    hs_block = deal.setdefault("hubspot", {})
    audit_log = hs_block.setdefault("conflict_log", [])
    enrich_log = deal.setdefault("enrichment", {}).setdefault("conflict_log", [])

    for c in conflicts:
        if c.field_path in _IDENTITY_FIELDS or c.hubspot_property in NEVER_WRITE:
            c.resolution = "hubspot_wins"
            try:
                _set_path(deal, c.field_path, c.hubspot_value)
            except (TypeError, ValueError):
                pass
        elif _is_enriched_field(c.field_path) and c.source_doc:
            c.resolution = "doc_wins"
            # Local already holds the doc-backed value; no mutation needed.
        else:
            # Default: HubSpot wins unless explicitly annotated doc_wins.
            c.resolution = "hubspot_wins"
            try:
                if not c.field_path.startswith("site_partners"):
                    _set_path(deal, c.field_path, c.hubspot_value)
            except (TypeError, ValueError):
                pass

        entry = c.to_audit_entry()
        audit_log.append(entry)
        enrich_log.append(entry)

    return deal


def _is_enriched_field(path: str) -> bool:
    """Return True if ``path`` points to an enrichment-derived field."""
    return any(path.startswith(p) for p in _ENRICHED_FIELDS_PREFIXES)


# ---------------------------------------------------------------------------
# Write back: enrichment-derived values -> HubSpot
# ---------------------------------------------------------------------------


def write_enrichment(
    client: HubSpotClient, deal: dict, fields: Dict[str, Any]
) -> Dict[str, Any]:
    """Write enrichment-derived values back to HubSpot.

    Only writes fields whose keys appear in the *values* of
    :data:`HUBSPOT_FIELD_MAP` (the canonical mapped set). Identity fields
    listed in :data:`NEVER_WRITE` are filtered out regardless.

    Parameters
    ----------
    client:
        HubSpot client instance (real or fake).
    deal:
        deal.yaml dict. ``hubspot_deal_id`` must be set.
    fields:
        Mapping of HubSpot *property name* -> new value. Only entries
        matching the canonical map are forwarded.

    Returns
    -------
    dict
        The exact payload actually sent to HubSpot (post-filter).
    """
    deal_id = deal.get("hubspot_deal_id")
    if deal_id is None:
        raise ValueError("deal.hubspot_deal_id is required before write_enrichment")

    allowed_props = set(HUBSPOT_FIELD_MAP.keys())
    payload: Dict[str, Any] = {}
    for prop, val in fields.items():
        if prop in NEVER_WRITE:
            continue
        if prop not in allowed_props:
            continue
        payload[prop] = val

    if payload:
        client.update_deal_properties(deal_id, payload)
        # Audit the write so we can trace engine-originated changes.
        hs_block = deal.setdefault("hubspot", {})
        write_log = hs_block.setdefault("write_log", [])
        write_log.append(
            {
                "at": _now_iso(),
                "deal_id": deal_id,
                "properties": list(payload.keys()),
            }
        )

    return payload


__all__ = [
    "Conflict",
    "HubSpotClient",
    "HUBSPOT_FIELD_MAP",
    "NEVER_WRITE",
    "read_deal",
    "validate",
    "resolve",
    "write_enrichment",
    "_set_path",
    "_get_path",
]
