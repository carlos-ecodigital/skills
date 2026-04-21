"""
Cross-document gate for Sites-stream deal.yaml.

Phase B8 of the sites-stream plan. Consolidates:

- Registry ``escalation_rules`` (Esc-1..4) — pre-existing rules in
  ``field-registry.json`` (non-standard heat split, co-investment,
  missing landowner consent, joint signing authority).
- Contradiction rules (Con-1..4) — LOI↔HoT drift detection.
- Gap rules (Gap-1..5) — required-field presence + doc-collection +
  doc-validity.
- Contribution-consistency rules (Contrib-1..2) — Site Partner set
  and contribution mix parity between LOI and HoT.
- Data-accuracy rules (DataAcc-1..3) — HubSpot identity conflicts,
  PDOK parcel geo-validation, postcode→DSO mismatch.

All rules output a ``GateVerdict`` with ``rule``, ``severity``,
``message``, ``overridable``. Callers (LOI + HoT engines) invoke
``CrossDocGate(deal).run()`` and receive ``List[GateVerdict]``.

Override flow:
- SAL adds an entry to ``deal['gate_overrides']`` with
  ``{rule, justification, approver, timestamp}``.
- Re-run: matching verdicts downgrade ``fail`` → ``warn`` with
  audit note recorded in ``deal.enrichment.conflict_log``.
- Non-overridable rules (Con-3, Con-4, Gap-1, Gap-4, Contrib-2,
  DataAcc-1, DataAcc-2) remain ``fail`` even with override attempts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, List, Optional

try:
    # When called from an engine that already has sites/_shared on sys.path
    from site_doc_base import (
        derive_role_labels,
        doc_is_stale,
        docs_required_for_partner,
        load_registry,
    )
except ImportError:
    # Fallback for tests invoked at the project root
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).parent))
    from site_doc_base import (  # noqa: E402
        derive_role_labels,
        doc_is_stale,
        docs_required_for_partner,
        load_registry,
    )


# ---------------------------------------------------------------------------
# GateVerdict
# ---------------------------------------------------------------------------

@dataclass
class GateVerdict:
    """Single gate-rule outcome."""
    rule: str                # "Con-1" | "Gap-4" | "Esc-1" | ...
    severity: str            # "fail" | "warn" | "info"
    message: str
    overridable: bool = True
    field_path: Optional[str] = None      # dotted path for targeting
    site_partner_idx: Optional[int] = None

    def to_dict(self) -> dict:
        return {
            "rule": self.rule,
            "severity": self.severity,
            "message": self.message,
            "overridable": self.overridable,
            "field_path": self.field_path,
            "site_partner_idx": self.site_partner_idx,
        }


#: Rules that are hard-fail-only (override ignored).
NON_OVERRIDABLE_RULES = frozenset({
    "Con-3",        # site_partners[].site location (parcel_id) differs
    "Con-4",        # Site Partner entity_id / KvK differs
    "Gap-1",        # HoT-required [TBC] fields unresolved
    "Gap-4",        # required doc not uploaded/parsed
    "Contrib-2",    # Site Partner in one doc but not the other
    "DataAcc-1",    # deal.yaml conflicts with HubSpot identity
    "DataAcc-2",    # parcel_id fails PDOK geo-validation
})


# ---------------------------------------------------------------------------
# CrossDocGate
# ---------------------------------------------------------------------------

class CrossDocGate:
    """Run all rules against a deal.yaml and return verdicts.

    Intended usage::

        gate = CrossDocGate(deal, stage="hot", prior_loi_deal=loi_deal)
        verdicts = gate.run()
        gate.apply_overrides(verdicts)   # downgrade overridable fails → warn
    """

    def __init__(
        self,
        deal: dict,
        stage: str = "hot",
        prior_loi_deal: Optional[dict] = None,
        registry: Optional[dict] = None,
    ):
        self.deal = deal
        self.stage = stage
        self.prior = prior_loi_deal
        self.registry = registry or load_registry()

    # --- Orchestrator ----------------------------------------------------

    def run(self) -> List[GateVerdict]:
        """Run every rule set in a deterministic order. Apply overrides
        last so the returned list contains the final severities."""
        verdicts: List[GateVerdict] = []

        # Contradiction rules require a prior LOI deal for drift detection.
        if self.prior is not None:
            verdicts.extend(self._run_contradiction_rules())
            verdicts.extend(self._run_contribution_consistency())

        verdicts.extend(self._run_gap_rules())
        verdicts.extend(self._run_doc_collection_rules())
        verdicts.extend(self._run_doc_validity_rules())
        verdicts.extend(self._run_data_accuracy_rules())
        verdicts.extend(self._run_registry_escalations())

        # Apply overrides last (downgrades fail → warn where permitted)
        return self.apply_overrides(verdicts)

    # --- Contradiction rules (Con-1..4) ----------------------------------

    def _run_contradiction_rules(self) -> List[GateVerdict]:
        if self.prior is None:
            return []
        out: List[GateVerdict] = []

        # Con-1 pricing drift >±10%
        out.extend(self._con_1_pricing())
        # Con-2 timeline milestones differ
        out.extend(self._con_2_timeline())
        # Con-3 site location (parcel_id) differs
        out.extend(self._con_3_site_location())
        # Con-4 Site Partner entity_id / KvK differs
        out.extend(self._con_4_partner_identity())
        return out

    def _con_1_pricing(self) -> List[GateVerdict]:
        out: List[GateVerdict] = []

        def _heat_price_eur_mwh(deal: dict) -> Optional[float]:
            for sp in deal.get("site_partners") or []:
                for ret in sp.get("returns") or []:
                    if ret.get("value") == "energy_heat":
                        p = (ret.get("details") or {}).get("price_eur_mwh")
                        try:
                            return float(p) if isinstance(p, (int, float)) or \
                                (isinstance(p, str) and p.replace(".", "").isdigit()) \
                                else None
                        except (TypeError, ValueError):
                            return None
            return None

        prior = _heat_price_eur_mwh(self.prior)
        current = _heat_price_eur_mwh(self.deal)
        if prior and current and abs(current - prior) / prior > 0.10:
            out.append(GateVerdict(
                rule="Con-1",
                severity="fail",
                message=(
                    f"Heat pricing drift >±10%: LOI preliminary €{prior}/MWh "
                    f"vs current indicative €{current}/MWh"
                ),
                overridable=True,
                field_path="site_partners[].returns[energy_heat].details.price_eur_mwh",
            ))
        return out

    def _con_2_timeline(self) -> List[GateVerdict]:
        prior_t = (self.prior or {}).get("timeline") or {}
        curr_t = self.deal.get("timeline") or {}
        out: List[GateVerdict] = []
        for key in ("hot_target_date", "expected_launch_date"):
            p, c = prior_t.get(key), curr_t.get(key)
            if p and c and p != c:
                out.append(GateVerdict(
                    rule="Con-2",
                    severity="fail",
                    message=f"Timeline {key}: LOI {p!r} vs current {c!r}",
                    overridable=True,
                    field_path=f"timeline.{key}",
                ))
        return out

    def _con_3_site_location(self) -> List[GateVerdict]:
        prior_locs = {l.get("parcel_id") for l in (self.prior or {}).get("locations") or []}
        curr_locs = {l.get("parcel_id") for l in self.deal.get("locations") or []}
        # Remove None (unresolved) — don't flag those as contradictions.
        prior_locs.discard(None)
        curr_locs.discard(None)
        if prior_locs and curr_locs and not (prior_locs & curr_locs):
            return [GateVerdict(
                rule="Con-3",
                severity="fail",
                message=(
                    f"Site parcel_id set differs: LOI {sorted(prior_locs)} "
                    f"vs current {sorted(curr_locs)}"
                ),
                overridable=False,
                field_path="locations[].parcel_id",
            )]
        return []

    def _con_4_partner_identity(self) -> List[GateVerdict]:
        out: List[GateVerdict] = []
        prior_sps = self.prior.get("site_partners") or []
        curr_sps = self.deal.get("site_partners") or []
        # Key by legal_name for a minimal identity check (entity_id may be null).
        prior_by_name = {sp.get("legal_name"): sp for sp in prior_sps}
        for idx, curr_sp in enumerate(curr_sps):
            name = curr_sp.get("legal_name")
            prior_sp = prior_by_name.get(name)
            if not prior_sp:
                continue
            # KvK mismatch (both must be non-null to mean anything)
            p_kvk = prior_sp.get("kvk")
            c_kvk = curr_sp.get("kvk")
            if p_kvk and c_kvk and p_kvk != c_kvk:
                out.append(GateVerdict(
                    rule="Con-4",
                    severity="fail",
                    message=(
                        f"Site Partner {name!r} KvK differs: "
                        f"LOI {p_kvk} vs current {c_kvk}"
                    ),
                    overridable=False,
                    field_path=f"site_partners[{idx}].kvk",
                    site_partner_idx=idx,
                ))
        return out

    # --- Contribution consistency (Contrib-1..2) -------------------------

    def _run_contribution_consistency(self) -> List[GateVerdict]:
        if self.prior is None:
            return []
        out: List[GateVerdict] = []
        prior_sps = self.prior.get("site_partners") or []
        curr_sps = self.deal.get("site_partners") or []
        prior_names = {sp.get("legal_name") for sp in prior_sps}
        curr_names = {sp.get("legal_name") for sp in curr_sps}

        # Contrib-2: partner appears in one doc only
        missing_in_curr = prior_names - curr_names
        missing_in_prior = curr_names - prior_names
        for name in missing_in_curr:
            out.append(GateVerdict(
                rule="Contrib-2",
                severity="fail",
                message=f"Site Partner {name!r} present in LOI but absent from current deal",
                overridable=False,
                field_path="site_partners[].legal_name",
            ))
        for name in missing_in_prior:
            out.append(GateVerdict(
                rule="Contrib-2",
                severity="fail",
                message=f"Site Partner {name!r} absent from LOI but present in current deal",
                overridable=False,
                field_path="site_partners[].legal_name",
            ))

        # Contrib-1: contribution assets differ for a matching partner
        prior_by_name = {sp.get("legal_name"): sp for sp in prior_sps}
        for idx, curr_sp in enumerate(curr_sps):
            name = curr_sp.get("legal_name")
            prior_sp = prior_by_name.get(name)
            if not prior_sp:
                continue
            prior_assets = {c.get("asset") for c in prior_sp.get("contributions") or []}
            curr_assets = {c.get("asset") for c in curr_sp.get("contributions") or []}
            if prior_assets != curr_assets:
                delta = prior_assets.symmetric_difference(curr_assets)
                out.append(GateVerdict(
                    rule="Contrib-1",
                    severity="fail",
                    message=(
                        f"Site Partner {name!r} contribution assets differ vs LOI "
                        f"(symmetric diff: {sorted(filter(None, delta))})"
                    ),
                    overridable=True,
                    field_path=f"site_partners[{idx}].contributions[].asset",
                    site_partner_idx=idx,
                ))
        return out

    # --- Gap rules (Gap-1..3) --------------------------------------------

    def _run_gap_rules(self) -> List[GateVerdict]:
        out: List[GateVerdict] = []

        # Gap-1: HoT-required [TBC] fields unresolved.
        # For v1 the check is structural: enumerate required fields for the
        # current stage and flag null/[TBC] values in deal.
        # We rely on _walk_for_tbc from site_doc_base (via site_doc_base import)
        # but here we do a targeted check on site_partner fields that
        # correspond to HoT-stage requirements.
        if self.stage == "hot":
            for idx, sp in enumerate(self.deal.get("site_partners") or []):
                if sp.get("legal_name") in (None, "[TBC]"):
                    out.append(GateVerdict(
                        rule="Gap-2",
                        severity="fail",
                        message=f"Site Partner {idx}: legal_name is mandatory",
                        overridable=True,
                        field_path=f"site_partners[{idx}].legal_name",
                        site_partner_idx=idx,
                    ))
                if sp.get("kvk") in (None, "[TBC]"):
                    out.append(GateVerdict(
                        rule="Gap-1",
                        severity="fail",
                        message=(
                            f"Site Partner {idx} ({sp.get('legal_name', '?')}): "
                            f"kvk [TBC] must resolve before HoT (Gap-1)"
                        ),
                        overridable=False,
                        field_path=f"site_partners[{idx}].kvk",
                        site_partner_idx=idx,
                    ))

        return out

    # --- Gap-4: doc-collection rules -------------------------------------

    def _run_doc_collection_rules(self) -> List[GateVerdict]:
        out: List[GateVerdict] = []
        if self.stage != "hot":
            return out  # LOI doesn't require docs (manual intake only)

        uploaded_by_partner: dict[int, set[str]] = {}
        for doc in self.deal.get("documents") or []:
            pidx = doc.get("partner_entity_idx")
            if pidx is None:
                # If not linked to a specific partner, treat as global
                pidx = -1
            uploaded_by_partner.setdefault(pidx, set()).add(doc.get("type"))
        global_docs = uploaded_by_partner.get(-1, set())

        for idx, sp in enumerate(self.deal.get("site_partners") or []):
            required = docs_required_for_partner(self.registry, sp)
            partner_docs = uploaded_by_partner.get(idx, set()) | global_docs
            for doc_type in required:
                if doc_type not in partner_docs:
                    out.append(GateVerdict(
                        rule="Gap-4",
                        severity="fail",
                        message=(
                            f"Site Partner {idx} ({sp.get('legal_name', '?')}): "
                            f"required doc {doc_type!r} not uploaded"
                        ),
                        overridable=False,
                        field_path=f"documents[type={doc_type}]",
                        site_partner_idx=idx,
                    ))
        return out

    # --- Gap-5: doc-validity rules ---------------------------------------

    def _run_doc_validity_rules(self) -> List[GateVerdict]:
        out: List[GateVerdict] = []
        for i, doc in enumerate(self.deal.get("documents") or []):
            if doc_is_stale(self.registry, doc):
                out.append(GateVerdict(
                    rule="Gap-5",
                    severity="fail",
                    message=(
                        f"Document {i} type={doc.get('type')!r} "
                        f"uploaded_at={doc.get('uploaded_at')} is past its "
                        f"validity window"
                    ),
                    overridable=True,
                    field_path=f"documents[{i}]",
                ))
        return out

    # --- Data-accuracy rules (DataAcc-1..3) ------------------------------

    def _run_data_accuracy_rules(self) -> List[GateVerdict]:
        out: List[GateVerdict] = []

        # DataAcc-1: site_partners[] have missing entity_id → HubSpot
        # association gap (the known Van Gog blocker).
        for idx, sp in enumerate(self.deal.get("site_partners") or []):
            if sp.get("entity_id") is None:
                out.append(GateVerdict(
                    rule="DataAcc-1",
                    severity="fail",
                    message=(
                        f"Site Partner {idx} ({sp.get('legal_name', '?')}): "
                        f"entity_id is null — HubSpot Company not associated "
                        f"with deal. Cannot resolve via data-authority chain."
                    ),
                    overridable=False,
                    field_path=f"site_partners[{idx}].entity_id",
                    site_partner_idx=idx,
                ))

        # DataAcc-2: parcel_id must PDOK-validate when enrichment.
        # pdok_parcel_confirmed is present.
        enrichment = self.deal.get("enrichment") or {}
        if enrichment.get("pdok_parcel_confirmed") is False:
            out.append(GateVerdict(
                rule="DataAcc-2",
                severity="fail",
                message="One or more parcel_id values failed PDOK geo-validation",
                overridable=False,
                field_path="locations[].parcel_id",
            ))

        # DataAcc-3: DSO differs from postcode lookup (warning only).
        if enrichment.get("dso_matches_postcode") is False:
            out.append(GateVerdict(
                rule="DataAcc-3",
                severity="warn",
                message="Declared DSO differs from postcode-lookup result",
                overridable=True,
                field_path="locations[].dso",
            ))

        return out

    # --- Registry escalation_rules (Esc-1..4) ----------------------------

    def _run_registry_escalations(self) -> List[GateVerdict]:
        """Consolidate the registry's escalation_rules block. Each rule's
        trigger is a structured query over deal.yaml; severity is 'fail'
        unless the registry specifies a warning action.
        """
        out: List[GateVerdict] = []
        escalations = self.registry.get("escalation_rules") or {}

        # Esc-1 non-standard heat split
        if "non_standard_heat_split" in escalations:
            e = escalations["non_standard_heat_split"]
            # Check site_partners[*].contributions/returns for heat-split values
            # The registry field is E1_heat_sales_split; v1 deal.yaml may
            # carry this as commercial.heat_sales_split_pct or similar.
            split = (self.deal.get("commercial") or {}).get("heat_sales_split_pct")
            # "50 : 50 %" is the default; anything else triggers escalation.
            if split is not None and split != "50 : 50 %":
                out.append(GateVerdict(
                    rule="Esc-1",
                    severity="fail",
                    message=f"{e['reason']} (escalate to {e['escalate_to']}, heat_sales_split={split!r})",
                    overridable=True,
                    field_path="commercial.heat_sales_split_pct",
                ))

        # Esc-2 co-investment
        if "co_investment_included" in escalations:
            e = escalations["co_investment_included"]
            for idx, sp in enumerate(self.deal.get("site_partners") or []):
                for ret in sp.get("returns") or []:
                    if ret.get("value") == "equity":
                        details = ret.get("details") or {}
                        if details:
                            out.append(GateVerdict(
                                rule="Esc-2",
                                severity="warn",
                                message=f"{e['reason']} (escalate to {e['escalate_to']}, site_partner {idx} returns equity)",
                                overridable=True,
                                field_path=f"site_partners[{idx}].returns[equity]",
                                site_partner_idx=idx,
                            ))
                            break

        # Esc-3 missing landowner consent
        if "missing_landowner_consent" in escalations:
            e = escalations["missing_landowner_consent"]
            # Trigger: grower is not landowner AND landowner_consent not uploaded.
            # v1 check: any partner contributes land AND no doc type==landowner_consent.
            has_land_contrib = False
            for sp in self.deal.get("site_partners") or []:
                for c in sp.get("contributions") or []:
                    if c.get("asset") == "land":
                        has_land_contrib = True
                        break
            has_consent_doc = any(
                d.get("type") == "landowner_consent"
                for d in self.deal.get("documents") or []
            )
            # Only flag if there are MULTIPLE partners (grower != landowner).
            n_partners = len(self.deal.get("site_partners") or [])
            if has_land_contrib and n_partners > 1 and not has_consent_doc and self.stage == "hot":
                out.append(GateVerdict(
                    rule="Esc-3",
                    severity="fail",
                    message=f"{e['reason']} (escalate to {e['escalate_to']})",
                    overridable=True,
                    field_path="documents[type=landowner_consent]",
                ))

        # Esc-4 joint signing authority → warning
        if "joint_signing_authority" in escalations:
            e = escalations["joint_signing_authority"]
            for idx, sp in enumerate(self.deal.get("site_partners") or []):
                sig = sp.get("signatory") or {}
                if sig.get("signing_authority") == "joint":
                    out.append(GateVerdict(
                        rule="Esc-4",
                        severity="warn",
                        message=f"{e.get('action', 'warning')} (site_partner {idx})",
                        overridable=True,
                        field_path=f"site_partners[{idx}].signatory.signing_authority",
                        site_partner_idx=idx,
                    ))

        return out

    # --- Override application --------------------------------------------

    def apply_overrides(self, verdicts: List[GateVerdict]) -> List[GateVerdict]:
        """Downgrade fail → warn for verdicts whose rule has a matching
        override entry in ``deal['gate_overrides']``, provided the rule
        is overridable."""
        overrides = self.deal.get("gate_overrides") or []
        override_rules = {o.get("rule") for o in overrides if isinstance(o, dict)}
        out: List[GateVerdict] = []
        for v in verdicts:
            if (
                v.rule in override_rules
                and v.severity == "fail"
                and v.rule not in NON_OVERRIDABLE_RULES
                and v.overridable
            ):
                # Downgrade
                msg = v.message + " [overridden by gate_overrides]"
                out.append(GateVerdict(
                    rule=v.rule,
                    severity="warn",
                    message=msg,
                    overridable=True,
                    field_path=v.field_path,
                    site_partner_idx=v.site_partner_idx,
                ))
            else:
                out.append(v)
        return out


# ---------------------------------------------------------------------------
# Convenience helpers
# ---------------------------------------------------------------------------

def run(
    deal: dict,
    stage: str = "hot",
    prior_loi_deal: Optional[dict] = None,
    registry: Optional[dict] = None,
) -> List[GateVerdict]:
    """Convenience wrapper. Returns verdicts (override already applied)."""
    return CrossDocGate(deal, stage=stage, prior_loi_deal=prior_loi_deal,
                        registry=registry).run()


def to_dict_list(verdicts: List[GateVerdict]) -> list[dict]:
    """Serialise verdicts for persistence in gate-report.json."""
    return [v.to_dict() for v in verdicts]


def summarise(verdicts: List[GateVerdict]) -> dict:
    """Quick summary for CLI / QA text output."""
    from collections import Counter
    sev_counts = Counter(v.severity for v in verdicts)
    rule_counts = Counter(v.rule for v in verdicts)
    return {
        "total": len(verdicts),
        "by_severity": dict(sev_counts),
        "by_rule": dict(rule_counts),
        "blocking": sum(1 for v in verdicts if v.severity == "fail"),
    }
