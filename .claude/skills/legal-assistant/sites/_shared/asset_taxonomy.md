# Asset × Contribution × Value-Exchange Taxonomy — Sites Stream

**Scope:** Canonical model that the Sites engines (LOI + HoT) reason over. Every Site Partner has a set of **contributions** (assets they secure *for* the Project) and a set of **returns** (values DE delivers *to* them). Role labels ("Grid Contributor", "Landowner", "Heat Offtaker") are derived for display only; engines never branch on labels.

**Authority anchors:**
- `deal_yaml_schema.md` — top-level schema + `contributions[]` / `returns[]` sub-schemas.
- `hot/field-registry.json` — 48-field grower-HoT field catalogue (Sections A–G + supporting documents + escalation rules).
- Van Gog LOI (14-04-2026) — reference pattern for multi-asset, multi-B.V. contributions with separate roles (§1.4, §3.x, Section R, Section L).

**Architectural rule (repeated throughout):** engines operate on `contributions` + `returns`. Labels are rendered last, from the data. A Site Partner with `contributions[land, grid_interconnection]` + `returns[energy_heat, money]` carries three labels; the engine does not know and does not care — it computes the LOI text from the contributions and returns themselves.

---

## 1. Assets — what a Site Partner can contribute

An **asset** is a thing of value the Site Partner holds, which the Project needs access to. Assets have definitions, canonical Dutch legal instruments, canonical detail keys on `contributions[].details`, and a supporting-document mapping that the HoT cross-doc gate uses to validate contribution claims.

### 1.1 Land

**Definition.** A Kadaster-identified parcel (or fraction of a parcel) used to host the DEC, a BESS footprint, heat-transfer infrastructure, or ancillary works. Scope excludes parcels used only for cable routing crossings — those are handled as easements and fall under the `property` bucket below when formalised.

**Dutch legal instruments.**

| Instrument | Use case | Notes |
|---|---|---|
| `recht_van_opstal` (right of superficies) | Primary DEC placement; 30-year initial term per Van Gog §3.8 | Notarial deed; registerable in Kadaster. Schema: `contributions[].instrument: recht_van_opstal`. |
| `leasehold` (erfpacht) | Alternative to `recht_van_opstal` when parcel is municipality-owned or when landowner prefers canon-based income | Long-duration grant; tends to follow municipal templates. |
| `sale` | Freehold transfer — rare for Site LOIs but retained as an option | Used only when the SP wants to exit land holding fully. |

**Canonical `details` keys.**

```yaml
details:
  parcel_id: "GRUBBENVORST A 1234"     # Kadaster reference: gemeente sectie nummer
  area_m2: 6375                          # total allocated
  area_m2_per_mw: 300                    # Van Gog §3.5 rule-of-thumb; used for pre-feasibility sizing
  opstalrecht_term_years: 30             # registry field D6; Van Gog §3.8
  title_type: "full_ownership"           # ∈ {full_ownership, erfpacht, other}; registry D2
  encumbrances: "none"                   # ∈ {none, mortgage, other}; registry D3
  zoning_designation: "Glastuinbouw"     # registry D4; validated against bestemmingsplan_excerpt
```

**Supporting documents** (validated by cross-doc gate):

| Doc type | Parser | Validates |
|---|---|---|
| `kadaster_uittreksel` | `kadaster_parser` | `parcel_id`, `title_type`, `encumbrances` |
| `bestemmingsplan_excerpt` | `bestemmingsplan_parser` | `zoning_designation` |
| `landowner_consent` (conditional) | manual hash-check | Activated when `grower_is_not_landowner`; required by registry `escalation_rules.missing_landowner_consent` |
| `financier_consent` (conditional) | manual hash-check | Activated when `has_land_financier` (mortgage on parcel) |

**Forward-compat to MSA stage.** Land contributions convert to a notarial `recht van opstal` deed (or erfpacht grant) executed between the `ProjectBV` and the Landowner at Financial Close. Template reference: `recht-van-opstal-deed-v1.docx` (future artefact — not yet drafted; DE-MIA Annex A clause library is the current placeholder).

---

### 1.2 Property

**Definition.** Buildings, structures, or installations already on the parcel that the Project uses — greenhouse water infrastructure, existing heat-distribution pipes, ancillary offices, process halls. Distinguished from **land** because the value attaches to the structure rather than the ground.

**Dutch legal instruments.**

| Instrument | Use case |
|---|---|
| `lease` (huurovereenkomst) | Temporary use of an existing building for Project construction staging or BESS enclosure |
| `recht_van_opstal` | When the existing structure is brought into ProjectBV ownership |
| `sale` | Rare; used if the structure is decommissioned and sold to ProjectBV |

**Canonical `details` keys.** Free-form, commonly includes `building_id`, `floor_area_m2`, `condition`, `intended_use`. No hard-coded detail contract at v1.0 — property contributions are captured narratively and validated by SAL during intake.

**Supporting documents.** Usually a site plan (`site_plan`) and a photo-set; no dedicated parser.

---

### 1.3 Infrastructure — Grid Interconnection + ATO

**Definition.** The physical and contractual right to import/export electricity from/to the public grid. In the Netherlands this is constituted by a DSO connection (aansluiting) and a transport allocation (transport), governed by an Aansluit- en Transportovereenkomst (**ATO**) between the connection holder and the DSO.

**Dutch legal instruments.**

| Instrument | Meaning | Typical trigger |
|---|---|---|
| `ato_sharing` | Existing ATO held by SP is shared with ProjectBV/BESS SPV under a sub-allocation agreement | SP retains primary ATO; BESS + DEC use sub-allocations. Van Gog pattern (25.5 MW split). |
| `ato_transfer` | Full ATO transfer from SP to ProjectBV | Clean break; SP exits grid-holding role post-transfer. |
| `new_ato` | New ATO application by SP (or by ProjectBV with SP cooperation) filed with DSO | Queue times 18–36 months in Liander/Enexis congestion zones; pre-feasibility gate. |

**Canonical `details` keys.**

```yaml
details:
  mva: 25.5                              # B.4 total connection capacity
  dso: "Enexis"                          # ∈ {Liander, Stedin, Enexis, Westland Infra, Coteq, Rendo}
  ean_code: "871687120000123456"         # B.2 EAN — 18 digits starts with 871
  import_mw: 18.5                        # B.5
  export_mw: 7.0                         # B.6
  base_import_mw: 18.5                   # B.8 — current baseline
  base_export_mw: 7.0                    # B.9
  future_import_mw: null                 # B.11 — reservation target, subject to DSO
  future_export_mw: null                 # B.12
  sap_configuration: "cable_pooling"     # ∈ {cable_pooling, mloea, other} — registry B.13
  ato_doc_ref: "documents/ato_enexis_8716…pdf"
  ato_valid_until: "2029-06-30"          # stale-doc gate trigger
```

**Supporting documents.**

| Doc type | Parser | Validates |
|---|---|---|
| `ato_document` | `ato_parser` | `ean_code`, `mva`, `import_mw`, `export_mw` |
| `bess_grid_sharing_agreement` | manual hash-check | Activated when `bess_co_development: true` and configuration is `ato_sharing` |

**Forward-compat to MSA stage.** Grid contributions convert to one of:
- **ATO Transfer Agreement** — tripartite DSO + SP + ProjectBV (novation).
- **ATO Sharing Agreement** — bilateral SP ↔ ProjectBV with a DSO acknowledgement.
- **New ATO** — DSO-issued; SP party only as applicant-on-behalf or land-access provider.

Van Gog precedent: two grid connections (18.5 MW + 7 MW) held by Van Gog Grubbenvorst B.V. (Grid Contributor B.V.), shared with ProjectBV under `ato_sharing`. See Section L, row L1 of the Van Gog LOI schedule.

---

### 1.4 Infrastructure — Gas Connection

**Definition.** An existing natural-gas supply contract and physical connection. In the DEC model, gas is being *replaced* (by DEC heat delivery under `energy_heat` returns); the contribution is usually "allowing the gas contract to be decommissioned and the connection repurposed or terminated".

**Dutch legal instruments.**

| Instrument | Meaning |
|---|---|
| `gas_contract_transfer` | SP transfers the supply contract to ProjectBV (unusual — DEC doesn't consume gas) |
| `decommission_then_new` | SP agrees to decommission the existing gas contract on a schedule tied to DEC heat-RFS; relevant for `energy_heat` returns |

**Canonical `details` keys.**

```yaml
details:
  ean_gas: "52…"                         # 18 digits; gas EAN starts with 52 or 54
  supplier: "Vattenfall B.V."
  annual_consumption_m3: 1200000         # baseline, for heat-replacement sizing
  decommission_trigger: "dec_heat_rfs"   # ∈ {dec_heat_rfs, fixed_date, none}
```

**Supporting documents.** `gas_supply_contract` (no dedicated parser at v1.0; manual hash-check + SAL extraction).

**Forward-compat.** Gas contract decommissioning is formalised inside the HPA (Heat Purchase Agreement) as a covenant of the Heat Offtaker, not as a standalone MSA.

---

### 1.5 Equipment — CHP (Combined Heat and Power, WKK)

**Definition.** An existing gas-fired CHP unit the SP currently operates for greenhouse heating/power. Relevant for grower sites where the CHP is the legacy heat source DEC is replacing; the equipment may be leased by the ProjectBV during a transitional period or retained by the SP as backup.

**Dutch legal instruments.**

| Instrument | Meaning |
|---|---|
| `equipment_lease` | ProjectBV leases the CHP from SP (transitional, backup capacity) — registry F.1 |
| `equipment_transfer` | CHP transferred to ProjectBV |
| `contribution_in_kind` | CHP contributed as equity-in-kind; rare |

**Canonical `details` keys.**

```yaml
details:
  kw_e: 2000                             # electrical
  kw_th: 2400                            # thermal
  age_years: 8
  maintenance_status: "current"          # ∈ {current, overdue, contract_expired}
  gasketel_cert_valid_until: "2027-01-31"
```

**Supporting documents.**

| Doc type | Parser | Validates |
|---|---|---|
| `chp_commissioning_cert` | manual hash-check | Identity + install date |
| `chp_maintenance_contract` | manual hash-check | `maintenance_status` |
| `chp_gasketel_cert` | manual hash-check | `gasketel_cert_valid_until` (stale ≥ 12 months out = warn) |

**Forward-compat.** CHP lease (F.1a fee; registry escalation: none) or transfer agreement — separate from HPA.

---

### 1.6 Equipment — BESS (Battery Energy Storage System)

**Definition.** A Battery Energy Storage System co-located with DEC, typically LFP chemistry. In the DE model, BESS is a pre-DEC revenue generator for the Grid Contributor (standalone returns from energy arbitrage + FCR/aFRR/mFRR + capacity market) that later converts into ProjectBV equity at Financial Close. Van Gog §3.2 reference: "approximately 25.5 MW / 51 MWh utilising lithium iron phosphate (LFP) technology".

**Dutch legal instruments.**

| Instrument | Meaning |
|---|---|
| `bess_jv_50_50` | 50/50 JV between DE and Grid Contributor via a dedicated BESS SPV |
| `contribution_in_kind` | SP contributes grid-sharing rights in lieu of cash equity |
| `equipment_lease` | ProjectBV/BESS SPV leases BESS from a third-party owner (non-default; flagged) |

**Canonical `details` keys.**

```yaml
details:
  mw: 25.5
  mwh: 51
  chemistry: "LFP"                       # ∈ {LFP, NMC, other}
  co_invest_pct: 50                      # SP's share in the BESS SPV
  revenue_streams:                       # indicative set
    - arbitrage
    - fcr                                # frequency containment reserve
    - afrr                               # automatic frequency restoration reserve
    - mfrr                               # manual frequency restoration reserve
    - capacity_market
  conversion_at_fid_to: "projectbv_equity"   # ∈ {projectbv_equity, cash_exit, rollover}
```

**Supporting documents.**

| Doc type | Parser | Validates |
|---|---|---|
| `bess_grid_sharing_agreement` | manual hash-check | Grid allocation between DEC and BESS |
| `bess_balancing_market_enrollment` | manual hash-check | TenneT programme registration (FCR / aFRR / mFRR) |

**Forward-compat.** BESS JV is formalised in a Shareholders' Agreement for the BESS SPV + a Grid Sharing Agreement + a Services/Operations Agreement. Conversion mechanics at DEC FID are drafted into the HoT per Van Gog §3.2.

**Derived flag.** `addons.bess_co_development: true` when any `contributions[].asset == equipment_bess` — activates conditional template sections (BESS cl. 3.2, escalation `co_investment_escalate_to_jelmer`).

---

### 1.7 Equipment — Solar PV

**Definition.** A behind-the-meter rooftop or ground-mounted PV array. Typically provides distributed generation into the SP's ATO (reducing net import) or supplies the DEC directly on private-wire.

**Dutch legal instruments.**

| Instrument | Meaning |
|---|---|
| `contribution_in_kind` | PV asset contributed to the Project |
| `equipment_lease` | PV leased to ProjectBV or to the SP via the Project |
| `equipment_transfer` | PV sold to ProjectBV |

**Canonical `details` keys.**

```yaml
details:
  mwp: 1.8                               # peak capacity
  annual_yield_mwh: 1620
  commissioning_date: "2022-06-01"
  private_wire: true                     # ∈ {true, false}; false = flows through ATO
  ppa_existing: false
```

**Supporting documents.**

| Doc type | Parser | Validates |
|---|---|---|
| `solar_pv_yield_report` | manual hash-check | `mwp`, `annual_yield_mwh` |
| `solar_pv_connection_agreement` | manual hash-check | Grid-connection consistency |

**Forward-compat.** Formalised in a PPA (if behind-the-meter off-take to ProjectBV) or as an equipment transfer agreement.

---

## 2. Values — what DE returns to the Site Partner

A **value** is a thing DE delivers back in exchange for a contribution. Values are classified along two orthogonal axes: (a) form (money / energy / equity), (b) instrument-specific terms (cash-payment schedule, heat-supply agreement terms, equity conversion mechanics).

### 2.1 Money

| Instrument | Meaning | Typical trigger |
|---|---|---|
| `cash_payment` | Lump sum or scheduled cash to SP — rare at LOI stage | Used for land purchase or CHP buyout |
| `revenue_share` | % of a defined revenue stream (heat sales, BESS market revenue, development fee carry) | Van Gog pattern: 50% gross heat revenues to Grid Contributor + 20% of DE's development fee to Grid Contributor, settled as ProjectBV equity |
| `kind_contribution` | In-kind service (construction support, operational access) valued at a booked rate | Non-default; surface to approval |

**Canonical `details` keys.**

```yaml
details:
  amount_eur: 960000                     # for cash_payment or lump elements
  schedule: "installments_4q"            # ∈ {lump_sum, installments_NQ, milestone_linked}
  escalation_pct_per_year: 2.5           # CPI or fixed
  percent_of_base: 50                    # for revenue_share — % of gross heat revenues
  revenue_base: "heat_gross"             # ∈ {heat_gross, heat_net, bess_ebitda, development_fee}
```

### 2.2 Energy — Heat

Canonical DE value exchange with the Heat Offtaker. Delivered via a direct pipeline from DEC to the Heat Offtaker's site (greenhouse, industrial hall).

| Instrument | Meaning |
|---|---|
| `heat_supply_agreement` (future HPA) | Long-term offtake between ProjectBV and Heat Offtaker; price-indexed; minimum offtake |

**Canonical `details` keys.**

```yaml
details:
  mwh_per_year: 170000                   # annual volume commitment
  price_eur_mwh: 15.0                    # Van Gog indicative; subject to HoT
  price_mechanism: "cpi_indexed"         # ∈ {fixed, cpi_indexed, formula}
  term_years: 30                         # matches recht_van_opstal term
  delta_t_requirement_c: 15              # registry C.3 — fixed minimum
  outlet_temp_c: 60                      # registry C.1
  return_temp_c: 45                      # registry C.2
  mwth: 21.25                            # Van Gog L1 — recoverable thermal
  annual_utilisation_hours: 8000
  minimum_offtake_pct: 80                # credit-support equivalent
```

**Forward-compat.** Heat Purchase Agreement (HPA) between ProjectBV and Heat Offtaker.

### 2.3 Energy — Power

Non-default DE return; may appear when DEC supplies surplus power to SP on private-wire (off-peak).

| Instrument | Meaning |
|---|---|
| `power_supply_agreement` (future PPA) | Scheduled MWh supply at agreed tariff |

**`details` keys**: `mwh_per_year`, `price_eur_mwh`, `term_years`, `private_wire` (bool).

### 2.4 Energy — Storage

Paired with `equipment_bess` contribution. SP sees value as "uninterrupted backup during grid-outage events" or "grid-balancing capacity reserved for SP's own operations".

| Instrument | Meaning |
|---|---|
| `storage_reservation_agreement` | Reserved % of BESS capacity for SP balancing + backup |

**`details` keys**: `reserved_mw`, `reserved_mwh`, `outage_sla_hours`, `term_years`.

### 2.5 Energy — Backup

CHP-transition-period value. SP retains the existing CHP as backup during the first N months of DEC operations.

| Instrument | Meaning |
|---|---|
| `backup_reserve_agreement` | DEC commits capacity; CHP retained on cold-standby |

### 2.6 Equity

| Instrument | Meaning |
|---|---|
| `bess_spv_equity` | Direct equity in the BESS SPV (pre-DEC-FID) |
| `projectbv_equity` | Equity in the ProjectBV (post-DEC-FID) |
| `conversion_right` | Right for SP to convert BESS equity → ProjectBV equity at FID per HoT-defined mechanics |

**Canonical `details` keys.**

```yaml
details:
  percent: 4.7                           # Van Gog anticipated combined ProjectBV stake
  convert_at_fid_to: "projectbv_equity"
  vesting:
    cliff_months: 12
    linear_months: 48
  lockup_years: 3
```

**Forward-compat.** Shareholders' Agreement of the ProjectBV + Subscription Agreement at Financial Close.

### 2.7 DEC Sub-SPV equity (strategic roadmap, not v1.0 deal flow)

DE's longer-term architecture contemplates sub-SPVs specialised per asset class:

| Sub-SPV | Assets held | When relevant |
|---|---|---|
| **AI Factory SPV** | Compute infrastructure (GPU racks, network fabric, AI-workload-facing capacity) | Future: when SP wants exposure to compute upside |
| **Thermal Factory SPV** | Heat recovery + pipeline assets + HPA offtake rights | When SP is a large heat buyer preferring direct thermal exposure |
| **Power Factory SPV** | BESS + PV + grid-sharing rights | Current: BESS JV per Van Gog |

Sub-SPV returns appear on `returns[].instrument` as `<sub_spv>_equity` (schema reserves this enum extension; not implemented at v1.0).

---

## 3. Role-label derivation

Labels are a **display convention** computed from contributions/returns per the Van Gog LOI §1.4 schema. Engines do not branch on labels. The LOI template renders role labels in Section R (parties table) and in the signature page (per-role sign blocks). See `deal_yaml_schema.md § Role-label derivation` for the authoritative table; mirrored here:

| Derivation rule | Label (EN / NL) |
|---|---|
| any `contributions[].asset` starts with `grid_` | **Grid Contributor** / **Netbijdrager** |
| any `contributions[].asset` ∈ {`land`, `property`} | **Landowner** / **Grondeigenaar** |
| any `returns[].value` == `energy_heat` | **Heat Offtaker** / **Warmteafnemer** |

**Composition.** A single Site Partner can carry multiple labels. The Van Gog anchor deal has three distinct B.V.s filling the three roles:

| B.V. | Role labels |
|---|---|
| Van Gog Grubbenvorst B.V. | Grid Contributor |
| Van Gog Grubbenvorst Vastgoed B.V. | Landowner |
| Van Gog kwekerijen Grubbenvorst B.V. | Heat Offtaker |

In a simpler deal a single B.V. may carry all three labels — the LOI template concatenates them comma-separated in the party line.

**Extension roadmap.** Additional labels may be added as new contribution/return classes are introduced (e.g., `BESS Co-Developer` when `equipment_bess` is present; `CHP Lessor` when CHP is leased to ProjectBV). v1.0 does not surface these — they're inferrable from the contribution set — but the architectural rule ("engines reason over data, labels render from data") continues to hold.

---

## 4. Composition — how assets and values map together

Every `contribution` implies a plausible set of `returns`. The engine does not enforce mappings (the SAL + user confirm during intake), but the below table is the **canonical expectation set** used to scaffold questions in the intake runbook:

| Contribution asset | Canonical return values | Rationale |
|---|---|---|
| `land` | `money` (revenue_share on heat or cash for opstal canon); optionally `equity` | Landowner's value comes from canon fee, heat revenue share, or equity stake |
| `property` | `money` (lease income) | Property use is typically compensated as lease |
| `grid_interconnection` | `money` (revenue_share from heat sales — Van Gog pattern) + `equity` (BESS JV then ProjectBV conversion) | Grid Contributor's value is tied to enabling DEC operation; proportional to contributed capacity |
| `gas_connection` | `energy_heat` (DEC supplies heat; SP retires gas contract) | Gas decommissioning is the *act*; heat delivery is the *return* |
| `equipment_chp` | `money` (lease fee) + `energy_backup` (SP retains CHP rights during transition) | CHP retained as backup via lease or sold to ProjectBV |
| `equipment_bess` | `equity` (BESS SPV) + `money` (BESS market revenue share) + conversion rights | BESS is both asset and revenue instrument |
| `equipment_solar_pv` | `energy_power` (PV offsets DEC import) + `money` (PPA or grid injection revenue share) | PV either private-wired to DEC or grid-injected |

**Engine rule:** during intake, for each declared contribution, the engine proposes the canonical return set and asks the SAL to confirm/adjust/add. Novel compositions (e.g., a land contribution returning BESS equity) are accepted but flagged for commercial-director review.

---

## 5. MSA forward-compatibility map

Each v1.0 contribution/return flows into a future per-asset Master Services Agreement (MSA) or equivalent instrument. The schema reserves `stage_tag: msa` but does not populate at v1.0. Mapping is documented here for continuity — Phase C (MSA stream) will consume this table.

| Asset / Value | v1.0 instrument (LOI/HoT) | Future MSA / agreement |
|---|---|---|
| `land` | `recht_van_opstal` intended | **Recht van Opstal Deed** (notarial) — bilateral ProjectBV ↔ Landowner, executed at Financial Close. Template reference (future): `recht-van-opstal-deed-v1.docx`. |
| `property` | `lease` | **Property Lease Agreement** |
| `grid_interconnection` (sharing) | `ato_sharing` | **ATO Sharing Agreement** (bilateral SP ↔ ProjectBV with DSO acknowledgement) |
| `grid_interconnection` (transfer) | `ato_transfer` | **ATO Transfer (Novation) Agreement** (tripartite DSO + SP + ProjectBV) |
| `grid_interconnection` (new) | `new_ato` | **New ATO with DSO** (standard DSO template) |
| `gas_connection` | `decommission_then_new` | Covenant inside the **Heat Purchase Agreement** (no standalone doc) |
| `equipment_chp` | `equipment_lease` | **CHP Lease Agreement** (ProjectBV ↔ SP) or **CHP Transfer Agreement** |
| `equipment_bess` | `bess_jv_50_50` | **BESS SPV Shareholders' Agreement** + **BESS Grid Sharing Agreement** + **BESS Services & Operations Agreement** + (at DEC FID) **Equity Conversion Agreement** into ProjectBV SHA |
| `equipment_solar_pv` | various | **PV PPA** (if private-wire off-take) or **Equipment Transfer Agreement** |
| `money` | `cash_payment` / `revenue_share` / `kind_contribution` | Embedded in the governing agreement for the contribution (HPA revenue share is inside HPA; development fee carry is inside ProjectBV SHA) |
| `energy_heat` | `heat_supply_agreement` | **Heat Purchase Agreement (HPA)** — bilateral ProjectBV ↔ Heat Offtaker |
| `energy_power` | `power_supply_agreement` | **Power Purchase Agreement (PPA)** |
| `energy_storage` | `storage_reservation_agreement` | **Storage Reservation Agreement** (off BESS SPV) |
| `energy_backup` | `backup_reserve_agreement` | Annex to HPA or standalone **Backup Capacity Agreement** |
| `equity` (BESS SPV) | `bess_spv_equity` | **BESS SPV Subscription Agreement** + **BESS SPV SHA** |
| `equity` (ProjectBV) | `projectbv_equity` | **ProjectBV Subscription Agreement** + **ProjectBV SHA** |
| `equity` (conversion right) | `conversion_right` | Conversion mechanics drafted into **ProjectBV SHA** + **BESS SPV SHA**, triggered at DEC FID |

---

## 6. Schema TODOs exposed by this taxonomy

Items the taxonomy surfaces that are not (yet) modelled in `deal_yaml_schema.md` v1.0:

1. **`storage_reservation_agreement` instrument** for `returns[value: energy_storage]` is referenced here but not enumerated in the schema's `instrument:` field on `returns[]`. Low-priority; likely added in v1.1 when a first storage-reservation deal flows.
2. **`backup_reserve_agreement` instrument** for `returns[value: energy_backup]` — same gap.
3. **Sub-SPV equity enum** (`ai_factory_equity`, `thermal_factory_equity`, `power_factory_equity`) — reserved, not enumerated.
4. **`property` contribution lacks a canonical detail contract.** Intentionally free-form in v1.0; registry Phase C should propose a detail schema if property contributions recur.
5. **Role-label composition for novel asset classes** (e.g., a future `BESS Co-Developer` label) — not currently derived by `site_doc_base.derive_labels`. Update required when `equipment_bess` as a sole contribution becomes a primary role rather than a co-label.
6. **`gas_connection` documents** — `gas_supply_contract` is referenced but not in the registry `supporting_documents` enum. Add to registry in Phase B3.

TODO(registry maintainer): resolve items 1–6 in registry v1.1.
