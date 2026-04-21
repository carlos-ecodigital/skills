# `deal.yaml` Schema v1.0 — Sites Stream Single Source of Truth

Scope: Site LOI + HoT intake. Progressively filled. LOI engine reads LOI-stage fields; HoT engine reads all + enriches + writes back. Mirrors HubSpot Deal + associated Companies (one per Site Partner) + Contacts (signatories).

**Data-authority chain** (newest-authoritative, implemented by `hubspot_sync.py` + cross-doc gate `DataAcc-1..3`):

```
Parsed document (ATO, Kadaster, KvK extract, SDE++ letter)   [most authoritative]
  > HubSpot (SoR for CRM identity & pipeline state)
    > LOI intake (manual SAL entry)
      > Vragenformulier (legacy intake surface)                [least authoritative]
```

If parsed doc disagrees with HubSpot, doc wins **and** updates HubSpot with audit entry. If HubSpot disagrees with LOI intake, HubSpot wins **and** corrects deal.yaml with audit entry.

---

## Top-level shape

```yaml
# ─── Identity ─────────────────────────────────────────────────────────────────
slug:                   # human slug, e.g., "van-gog-grubbenvorst"
hubspot_deal_id:        # integer, SoR anchor (e.g., 365739346165)
counterparty_folder_name: # Drive folder, e.g., "van Gog kwekerijen Grubbenvorst_Project_Benelux_Ops"
                        # (convention: "{Counterparty}_Project_Benelux_Ops/")

# ─── HubSpot sync state ───────────────────────────────────────────────────────
hubspot:
  pipeline:             # "492649440"
  dealstage:            # "1163932892"
  dealname:             # mirrors HubSpot dealname; read-only from HubSpot
  hs_lastmodifieddate:  # ISO8601 — used by sync to detect staleness
  last_sync_at:         # ISO8601 — when engine last read/wrote
  conflict_log: []      # audit trail of resolutions
  # - { field, local_value, hubspot_value, resolution: "hubspot_wins|doc_wins|manual", at, source_doc? }

# ─── Ownership & review routing ───────────────────────────────────────────────
owner:
  hubspot_owner_id:     # 521949924
  name:                 # "Jelmer ten Wolde" (looked up via search_owners)
  email:

# ─── Deal archetype & commercial envelope ─────────────────────────────────────
deal_archetype:         # HubSpot `type_of_deal` (e.g., "Heat Recovery", "BESS Only")
dealtype:               # HubSpot `dealtype` (e.g., "newbusiness")
commercial:
  deal_value_eur:       # HubSpot `deal_value` (indicative; LOI-stage preliminary)
  currency:             # "EUR"
  contract_mw_available:   # HubSpot `contract_capacity___available__mw_`
  contract_mw_potential:   # HubSpot `contract_capacity___potential__mw_`
  # Further commercial stage fields populated per stage
  pricing:
    preliminary:        # stage: loi  — range or "cpi_indexed"
    indicative:         # stage: hot  — tighter range with doc-backing
    # definitive:       # stage: msa  (future)

# ─── Site Partners (1..N) — Section R of the LOI ──────────────────────────────
site_partners:
  - entity_id:          # HubSpot Company ID (integer). Gated by DataAcc-1 if missing.
    legal_name:         # "Van Gog Grubbenvorst B.V."
    kvk:                # 8-digit; validated against KVK API + kvk_uittreksel doc
    registered_address: # validated against KvK extract
    signatory:
      contact_id:       # HubSpot Contact ID (e.g., 578654116067 for Koen Saris)
      name:             # "Koen Saris"
      title:            # "Operationeel Directeur"
      email:
      signing_authority: # "sole" | "joint" | "pending_poa" — drives escalation_rules.joint_signing_authority
    contributions: []   # see Contributions below
    returns: []         # see Returns below

# ─── Locations — Section L of the LOI ─────────────────────────────────────────
locations:
  - parcel_id:          # Kadaster reference, e.g., "GRUBBENVORST A 1234"
    address:
    postcode:
    dso:                # "Enexis" | "Liander" | "Westland Infra" | ... validated via postcode→DSO lookup
    municipality:
    bestemmingsplan_designation:  # from bestemmingsplan_excerpt doc

# ─── Optional add-ons (activate conditional template sections) ────────────────
addons:
  bess_co_development: false  # derived: any site_partners[].contributions[].asset == equipment_bess
  btm_renewables: false        # SAM-003 future hook

# ─── Documents — per registry.supporting_documents; chain-of-custody ──────────
documents:
  - path:               # relative to {Counterparty}_Project_Benelux_Ops/documents/
    type:               # enum: kvk_uittreksel | ato_document | kadaster_uittreksel | bestemmingsplan_excerpt | landowner_consent | financier_consent | site_plan | bess_grid_sharing_agreement | bess_balancing_market_enrollment | chp_commissioning_cert | chp_maintenance_contract | chp_gasketel_cert | solar_pv_yield_report | solar_pv_connection_agreement | co2_supply_contract
    hash:               # sha256:...
    uploaded_at:        # ISO8601
    uploaded_by:        # SAL / Co / etc.
    parsed: false
    parser_version:     # e.g., "ato_parser@1.0"
    phase:              # 1..5 from registry.supporting_documents.<type>.request_at_phase
    validity_expires:   # uploaded_at + registry.supporting_documents.<type>.validity_days
    partner_entity_id:  # which Site Partner this doc belongs to (subset logic)

# ─── Enrichment audit ─────────────────────────────────────────────────────────
enrichment:
  kvk_active:           # boolean — KvK API + kvk_uittreksel cross-check
  pdok_parcel_confirmed: # boolean — PDOK WFS geo-validates parcel_id
  dso_matches_postcode: # boolean — postcode lookup matches declared DSO
  sde_eligibility:      # "confirmed" | "pending" | "not_applicable"
  last_enrichment_at:

# ─── Gate overrides (fail → warn with justification) ──────────────────────────
gate_overrides:
  # - rule: Con-1
  #   justification: "Heat pricing adjusted post-ATO grid quote; intentional"
  #   approver: "SAL / Co ten Wolde"
  #   timestamp: "2026-04-20T10:00:00Z"

# ─── Generated artifacts ──────────────────────────────────────────────────────
generated:
  loi_v1_path:          # drafts/YYYYMMDD_DE_LOI_Site_{slug}_v1_(DRAFT).docx
  loi_v1_qa_path:       # drafts/..._qa.txt
  loi_v1_hash:          # sha256 for regression/determinism
  hot_v1_path:
  hot_v1_qa_path:
  hot_v1_hash:
  cross_doc_gate_report_path:

# ─── Timeline (LOI §4.3 target + derived milestones) ──────────────────────────
timeline:
  loi_drafted_date:
  loi_signed_date:
  hot_target_date:       # = loi_signed_date + 90 days (per Van Gog §4.3)
  hot_drafted_date:
  hot_signed_date:
  pre_feasibility_status: # "not_started" | "in_progress" | "complete"
```

---

## Contribution / Return sub-schemas

### `contributions[]` — what a Site Partner secures FOR the Project

```yaml
- asset:            # enum: land | property | grid_interconnection | gas_connection | equipment_chp | equipment_bess | equipment_solar_pv
  instrument:       # asset-specific legal instrument:
                    # land         → recht_van_opstal | leasehold | sale
                    # property     → lease | recht_van_opstal | sale
                    # grid_*       → ato_sharing | ato_transfer | new_ato
                    # gas          → gas_contract_transfer | decommission_then_new
                    # equipment_*  → bess_jv_50_50 | contribution_in_kind | equipment_lease | equipment_transfer
  details:          # free-form map; canonical keys per asset class:
                    # land:         { parcel_id, area_m2, area_m2_per_mw }
                    # grid_*:       { mva, dso, ean_code, import_mw, export_mw, ato_doc_ref }
                    # equipment_bess: { mw, mwh, chemistry, co_invest_pct }
                    # equipment_chp: { kw_e, kw_th, age_years, maintenance_status }
  stage_tag:        # loi | hot — when this contribution is committed
  source_doc_ref:   # documents[].path proving the contribution (e.g., ATO for grid)
```

### `returns[]` — what DE delivers TO the Site Partner

```yaml
- value:            # enum: money | energy_heat | energy_power | energy_storage | energy_backup | equity
  instrument:       # value-specific:
                    # money        → cash_payment | revenue_share | kind_contribution
                    # energy_heat  → heat_supply_agreement (future MSA)
                    # energy_power → power_supply_agreement
                    # equity       → bess_spv_equity | projectbv_equity | conversion_right
  details:          # free-form per value class:
                    # energy_heat: { mwh_per_year, price_eur_mwh, price_mechanism: "cpi_indexed" | "fixed", term_years, delta_t_requirement_c }
                    # equity:      { percent, convert_at_fid_to, vesting }
                    # money:       { amount_eur, schedule, escalation_pct_per_year }
  stage_tag:        # loi | hot
```

---

## Role-label derivation (display only)

Template renders role labels per Van Gog LOI §1.4. Computed by `site_doc_base.derive_labels(site_partner)`:

| Condition on `site_partner` | Label rendered |
|---|---|
| any `contributions[].asset` starts with `grid_` | **Grid Contributor** / Netbijdrager |
| any `contributions[].asset` == `land` or `property` | **Landowner** / Grondeigenaar |
| any `returns[].value` == `energy_heat` | **Heat Offtaker** / Warmteafnemer |

A single Site Partner can carry multiple labels (e.g., Van Gog Grubbenvorst B.V. is both Grid Contributor and — if it held land — Landowner). Template renders comma-separated where multi-labeled.

Architecture rule: **engines reason over `contributions` + `returns`, never over role labels.** Labels are a display convention only.

---

## Stage filter semantics (`stage_tag`)

- `stage: loi` — captured in LOI, non-binding, top-of-funnel signal
- `stage: hot` — binding commitment; requires supporting documents per registry
- `stage: both` — present in both (identity fields: slug, site_partners.legal_name, locations.parcel_id)
- `stage: msa` — reserved, not used in LOI/HoT build

LOI engine reads: `stage ∈ {loi, both}` + LOI-required fields validated.
HoT engine reads: all stages + runs enrichment + cross-doc gate + writes back to HubSpot.

---

## HubSpot ↔ deal.yaml field map (canonical)

Identity + pipeline state is sourced from HubSpot Deal; Site Partners from associated Companies; Signatories from associated Contacts. Unmapped HubSpot properties are preserved in `hubspot.raw_extra: {...}` for audit without being authoritative.

| HubSpot property | deal.yaml path | Direction |
|---|---|---|
| Deal.id | `hubspot_deal_id` | HS → yaml (immutable) |
| Deal.dealname | `hubspot.dealname` + derive `slug` | HS → yaml |
| Deal.pipeline | `hubspot.pipeline` | HS → yaml |
| Deal.dealstage | `hubspot.dealstage` | HS → yaml (read-only; stage transitions via HubSpot UI) |
| Deal.hs_lastmodifieddate | `hubspot.hs_lastmodifieddate` | HS → yaml |
| Deal.hubspot_owner_id | `owner.hubspot_owner_id` | HS → yaml |
| Deal.type_of_deal | `deal_archetype` | HS → yaml |
| Deal.dealtype | `dealtype` | HS → yaml |
| Deal.deal_value | `commercial.deal_value_eur` | HS ↔ yaml (two-way; engine writes HoT-stage refinement back) |
| Deal.deal_currency_code | `commercial.currency` | HS → yaml |
| Deal.contract_capacity___available__mw_ | `commercial.contract_mw_available` | HS ↔ yaml |
| Deal.contract_capacity___potential__mw_ | `commercial.contract_mw_potential` | HS ↔ yaml |
| Deal.what_temperature_do_you_need_for_your_heat_system_ | (derived into `site_partners[].returns[].details.delta_t_requirement_c` or `heat_supply_temp_c`) | HS → yaml; engine enriches back after ATO-doc parse |
| Deal.what_s_your_approximate_heat_capacity__mwth___ | `site_partners[with heat_offtaker].returns[energy_heat].details.mwth` | HS → yaml; enriched back |
| Deal.heat_utilisation_hours | `returns[energy_heat].details.annual_utilisation_hours` | HS → yaml; enriched back |
| Deal.where_is_your_site_located_____city___country | `locations[0].address` (first location) | HS → yaml; enriched back post-Kadaster |
| Deal.site_ownership_deal | `site_partners[landowner].contributions[land].instrument` | HS → yaml |
| Deal.how_do_you_currently_produce_heat_ | `deal_meta.legacy_heat_source` (informational; HS only) | HS → yaml |
| Deal.full_site___expected_launch_date | `timeline.expected_launch_date` | HS ↔ yaml |
| Company.name | `site_partners[].legal_name` | HS → yaml (blocked by DataAcc-1 if no associated Companies) |
| Company.domain / website | `site_partners[].website` | HS → yaml |
| (Company.kvk — custom property if present) | `site_partners[].kvk` | HS ↔ yaml; authoritative doc = kvk_uittreksel |
| Contact.firstname + lastname | `site_partners[].signatory.name` | HS → yaml |
| Contact.jobtitle | `site_partners[].signatory.title` | HS → yaml |
| Contact.email | `site_partners[].signatory.email` | HS → yaml |

**Write-back** (engine → HubSpot) only for enrichment-derived values with audit in `hubspot.conflict_log`. Identity + dealstage are never written by the engine.

---

## Gaps on the Van Gog anchor deal (surfaced, not pre-fixed)

Per user direction, these surface as cross-doc gate findings in Phase B7 tests rather than being hand-fixed:

1. **Zero Companies associated** → `DataAcc-1` fail; three Van Gog B.V. entities (Grubbenvorst B.V., Vastgoed B.V., kwekerijen Grubbenvorst B.V.) need to be created + associated before HoT can generate.
2. **Site properties empty** (heat temp, capacity MWth, location) → engine gracefully handles as enrichment-pending; parsed docs (ATO, Kadaster) fill and write back.
3. **No KVK field on Deal; presumed on Company** — schema notes this as authoritative-via-doc (kvk_uittreksel) with HubSpot write-back.

---

## Versioning

`deal.yaml` schema version is pinned in the root:

```yaml
deal_yaml_schema_version: "1.0"
```

Schema changes require:
- bump per registry `template-version.md` cadence (v1.0 → v1.1 legal + NL-native review gate)
- backward-compatibility policy: v1.0 files remain readable by v1.x engines; migrations via `site_doc_base.migrate_deal_yaml(from, to)` when needed.
