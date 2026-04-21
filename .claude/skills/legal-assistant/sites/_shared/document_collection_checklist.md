# Document Collection Checklist — HoT Phase B4

**Skill:** `legal-assistant` · **Stage:** HoT (post-LOI signing) · **Registry:** `sites/hot/field-registry.json` v1.1
**Generated from:** `supporting_documents` block (15 entries) — do not hand-edit; regenerate from registry.

---

## 1. Purpose

This checklist is the human-readable view of the registry's `supporting_documents` block. The Site Acquisition Lead (SAL) uses it as the master reference for which evidentiary documents must be gathered from each Site Partner between LOI signing and HoT execution.

A Site Partner does **not** need to provide every document on the master list. The SAL sends each partner a subset derived from that partner's `contributions[]` entry in the deal YAML. Identity documents are universal; land, grid, and equipment documents are scoped to the assets that partner is actually contributing.

**Data-authority chain** (per `deal_yaml_schema.md`):

```
Site Partner intake → SAL uploads to /documents/ → parser extracts → registry field verified → gate passes → HoT draft generated
```

Every field in the HoT that carries legal weight must trace back to an uploaded, hashed, parser-validated document in this checklist.

## 2. How to use (SAL workflow)

1. **Review the partner's `contributions[]`** in the deal YAML. Note which assets appear (identity is always implicit; land, grid_interconnection, property, equipment_chp, equipment_bess, equipment_solar_pv, heat_supply, gas_connection).
2. **Subset the master list** using the _Partner-subset rule_ column in §4 below. Only send each partner what applies to their contributions.
3. **Send the request** — use the partner's native language (NL label where available) and cite the registry field(s) the document verifies so the partner understands what is being validated.
4. **Track uploads** into `{Counterparty}_Project_Benelux_Ops/documents/` with the filename convention `{phase}_{type}_{partner_slug}_{YYYYMMDD}.pdf`.
5. **Parser runs** automatically on upload. The parser stamps `parser_version_applied` and either passes (fields extracted, gate clears) or flags a mismatch for SAL review.
6. **Record chain of custody** in `documents/_manifest.json` — SHA-256 hash, `uploaded_at`, `uploaded_by`, `parser_version_applied`, `validity_expires` (= `uploaded_at` + `validity_days` from registry).
7. **Escalate** per `escalation_rules` in the registry when a required document is missing, expired, or contradicts declared field values (e.g., ATO MVA disagreeing with B.4 intake).

## 3. Per-asset groupings

The collection requirement is determined per Site Partner by matching the partner's `contributions[].asset` values to the groupings below.

### 3.1 Identity

**Trigger:** For every Site Partner — always required regardless of contribution mix.

| Doc ID | Label (EN) | Label (NL) | R/C | Phase |
|---|---|---|---|---|
| `kvk_uittreksel` | KVK extract | KVK-uittreksel | Required | 1 |

### 3.2 Land

**Trigger:** Required if any `contributions[].asset` ∈ {`land`, `property`}.

| Doc ID | Label (EN) | Label (NL) | R/C | Phase |
|---|---|---|---|---|
| `kadaster_uittreksel` | Kadaster extract | Kadaster-uittreksel | Required | 5 |
| `landowner_consent` | Landowner consent letter | Instemmingsbrief grondeigenaar | Conditional-Optional | 5 |
| `financier_consent` | Land Financier consent letter | Instemmingsbrief grondfinancier | Conditional-Optional | 5 |
| `site_plan` | Greenhouse layout / site plan | Kasplattegrond / situatietekening | Optional | 5 |

### 3.3 Grid Interconnection

**Trigger:** Required if any `contributions[].asset` == `grid_interconnection`.

| Doc ID | Label (EN) | Label (NL) | R/C | Phase |
|---|---|---|---|---|
| `ato_document` | ATO document (DSO contract) | ATO-document | Required | 3 |

### 3.4 Equipment CHP

**Trigger:** Required if any `contributions[].asset` == `equipment_chp`.

| Doc ID | Label (EN) | Label (NL) | R/C | Phase |
|---|---|---|---|---|
| `chp_commissioning_cert` | CHP commissioning certificate | WKK-inbedrijfstellingscertificaat | Conditional-Required | 3 |
| `chp_maintenance_contract` | CHP maintenance contract | WKK-onderhoudscontract | Conditional-Optional | 3 |
| `chp_gasketel_cert` | Gas-boiler certificate (gasketel) | Gasketelcertificaat | Conditional-Required | 3 |

### 3.5 Equipment BESS

**Trigger:** Required if any `contributions[].asset` == `equipment_bess`.

| Doc ID | Label (EN) | Label (NL) | R/C | Phase |
|---|---|---|---|---|
| `bess_grid_sharing_agreement` | BESS grid-sharing agreement | BESS-netdelingsovereenkomst | Conditional-Optional | 4 |
| `bess_balancing_market_enrollment` | BESS balancing-market participation enrollment | BESS-inschrijving balanceringsmarkt | Conditional-Optional | 4 |

### 3.6 Equipment SolarPV

**Trigger:** Required if any `contributions[].asset` == `equipment_solar_pv`.

| Doc ID | Label (EN) | Label (NL) | R/C | Phase |
|---|---|---|---|---|
| `solar_pv_yield_report` | Solar PV yield report | Opbrengstrapport zonnepanelen | Conditional-Required | 4 |
| `solar_pv_connection_agreement` | Solar PV connection agreement | Zonnepanelen-aansluitovereenkomst | Conditional-Required | 3 |

### 3.7 Heat-specific

**Trigger:** Conditional — cross-asset; typically tied to grower `heat_supply` contribution + cultivation type.

| Doc ID | Label (EN) | Label (NL) | R/C | Phase |
|---|---|---|---|---|
| `co2_supply_contract` | CO₂ supply contract (grower) | CO₂-leveringscontract (teler) | Conditional-Optional | 4 |

### 3.8 Regulatory

**Trigger:** Cross-asset site-level regulatory evidence; collected once per site (via the partner holding `land`).

| Doc ID | Label (EN) | Label (NL) | R/C | Phase |
|---|---|---|---|---|
| `bestemmingsplan_excerpt` | Zoning plan excerpt | Bestemmingsplan-uittreksel | Required | 5 |

## 4. Per-document detail

One row per registry entry, in the asset-group order from §3. All values are taken **verbatim** from `field-registry.json` v1.1.

| # | Doc ID | Label (EN) | Label (NL) | Required / Conditional | Condition | Phase | Verifies | Validity | Review tier | Days to receive | Partner-subset rule |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `kvk_uittreksel` | KVK extract | KVK-uittreksel | Required | — | 1 | `A1_legal_name`, `A2_kvk_number`, `A3_registered_address`, `A6_signing_authority` | 30 days | `sal` | 1 d | Every Site Partner (identity is universal). |
| 2 | `kadaster_uittreksel` | Kadaster extract | Kadaster-uittreksel | Required | — | 5 | `D1_kadaster_parcels`, `D2_title_type`, `D3_encumbrances` | 90 days | `sal` | 3 d | Only Site Partners whose contributions include `land` or `property`. |
| 3 | `landowner_consent` | Landowner consent letter | Instemmingsbrief grondeigenaar | Conditional-Optional | `grower_is_not_landowner` | 5 | _(no field-level verification; document-as-checklist)_ | 180 days | `legal_counsel` | 21 d | Only when `grower_is_not_landowner` — collected from the landowner partner. |
| 4 | `financier_consent` | Land Financier consent letter | Instemmingsbrief grondfinancier | Conditional-Optional | `has_land_financier` | 5 | _(no field-level verification; document-as-checklist)_ | 180 days | `legal_counsel` | 21 d | Only when `has_land_financier` — collected from the financier partner. |
| 5 | `site_plan` | Greenhouse layout / site plan | Kasplattegrond / situatietekening | Optional | — | 5 | _(no field-level verification; document-as-checklist)_ | No expiry (one-time snapshot) | `sal` | 5 d | Collected from the partner who holds `land` / `property` (optional). |
| 6 | `ato_document` | ATO document (DSO contract) | ATO-document | Required | — | 3 | `B2_ean_code`, `B4_total_connection_mva`, `B5_total_import_mw`, `B6_total_export_mw` | 365 days | `legal_counsel` | 10 d | Only Site Partners whose contributions include `grid_interconnection`. |
| 7 | `chp_commissioning_cert` | CHP commissioning certificate | WKK-inbedrijfstellingscertificaat | Conditional-Required | `any contribution.asset == equipment_chp` | 3 | `F1_chp_lease`, `F1a_chp_lease_fee` | 365 days | `sal` | 14 d | Only Site Partners contributing `equipment_chp`. |
| 8 | `chp_maintenance_contract` | CHP maintenance contract | WKK-onderhoudscontract | Conditional-Optional | `any contribution.asset == equipment_chp` | 3 | _(no field-level verification; document-as-checklist)_ | 365 days | `legal_counsel` | 14 d | Only Site Partners contributing `equipment_chp`. |
| 9 | `chp_gasketel_cert` | Gas-boiler certificate (gasketel) | Gasketelcertificaat | Conditional-Required | `any contribution.asset == equipment_chp AND chp is gas-fired` | 3 | `F1_chp_lease` | 365 days | `sal` | 14 d | Only Site Partners contributing `equipment_chp` AND the CHP is gas-fired. |
| 10 | `bess_grid_sharing_agreement` | BESS grid-sharing agreement | BESS-netdelingsovereenkomst | Conditional-Optional | `any contribution.asset == equipment_bess` | 4 | `B4_total_connection_mva`, `B11_ato_transfer_mode` | 365 days | `legal_counsel` | 21 d | Only Site Partners contributing `equipment_bess`. |
| 11 | `bess_balancing_market_enrollment` | BESS balancing-market participation enrollment | BESS-inschrijving balanceringsmarkt | Conditional-Optional | `any contribution.asset == equipment_bess` | 4 | _(no field-level verification; document-as-checklist)_ | 365 days | `sal` | 14 d | Only Site Partners contributing `equipment_bess`. |
| 12 | `solar_pv_yield_report` | Solar PV yield report | Opbrengstrapport zonnepanelen | Conditional-Required | `any contribution.asset == equipment_solar_pv` | 4 | _(no field-level verification; document-as-checklist)_ | 365 days | `sal` | 14 d | Only Site Partners contributing `equipment_solar_pv`. |
| 13 | `solar_pv_connection_agreement` | Solar PV connection agreement | Zonnepanelen-aansluitovereenkomst | Conditional-Required | `any contribution.asset == equipment_solar_pv` | 3 | `B1_dso`, `B4_total_connection_mva` | 365 days | `legal_counsel` | 21 d | Only Site Partners contributing `equipment_solar_pv`. |
| 14 | `co2_supply_contract` | CO₂ supply contract (grower) | CO₂-leveringscontract (teler) | Conditional-Optional | `crop_uses_co2_enrichment` | 4 | _(no field-level verification; document-as-checklist)_ | 365 days | `legal_counsel` | 21 d | Only when `crop_uses_co2_enrichment`; collected from the grower partner. |
| 15 | `bestemmingsplan_excerpt` | Zoning plan excerpt | Bestemmingsplan-uittreksel | Required | — | 5 | `D4_zoning_designation` | 180 days | `sal` | 5 d | Required for the site (cross-asset regulatory); collected from the partner holding `land`. |

### 4.1 Expanded detail (per document)

#### 4.1.1 `kvk_uittreksel` — KVK extract / KVK-uittreksel

- **Status:** Required
- **Collected at phase:** 1
- **Verifies registry fields:** `A1_legal_name`, `A2_kvk_number`, `A3_registered_address`, `A6_signing_authority`
- **Validity window:** 30 days
- **Review tier:** `sal`
- **Typical days to receive:** 1
- **Partner-subset rule:** Every Site Partner (identity is universal).

#### 4.1.2 `kadaster_uittreksel` — Kadaster extract / Kadaster-uittreksel

- **Status:** Required
- **Collected at phase:** 5
- **Verifies registry fields:** `D1_kadaster_parcels`, `D2_title_type`, `D3_encumbrances`
- **Validity window:** 90 days
- **Review tier:** `sal`
- **Typical days to receive:** 3
- **Partner-subset rule:** Only Site Partners whose contributions include `land` or `property`.

#### 4.1.3 `landowner_consent` — Landowner consent letter / Instemmingsbrief grondeigenaar

- **Status:** Conditional-Optional
- **Condition:** `grower_is_not_landowner`
- **Collected at phase:** 5
- **Verifies registry fields:** _(no field-level verification; document-as-checklist)_
- **Validity window:** 180 days
- **Review tier:** `legal_counsel`
- **Typical days to receive:** 21
- **Partner-subset rule:** Only when `grower_is_not_landowner` — collected from the landowner partner.

#### 4.1.4 `financier_consent` — Land Financier consent letter / Instemmingsbrief grondfinancier

- **Status:** Conditional-Optional
- **Condition:** `has_land_financier`
- **Collected at phase:** 5
- **Verifies registry fields:** _(no field-level verification; document-as-checklist)_
- **Validity window:** 180 days
- **Review tier:** `legal_counsel`
- **Typical days to receive:** 21
- **Partner-subset rule:** Only when `has_land_financier` — collected from the financier partner.

#### 4.1.5 `site_plan` — Greenhouse layout / site plan / Kasplattegrond / situatietekening

- **Status:** Optional
- **Collected at phase:** 5
- **Verifies registry fields:** _(no field-level verification; document-as-checklist)_
- **Validity window:** No expiry (one-time snapshot)
- **Review tier:** `sal`
- **Typical days to receive:** 5
- **Partner-subset rule:** Collected from the partner who holds `land` / `property` (optional).

#### 4.1.6 `ato_document` — ATO document (DSO contract) / ATO-document

- **Status:** Required
- **Collected at phase:** 3
- **Verifies registry fields:** `B2_ean_code`, `B4_total_connection_mva`, `B5_total_import_mw`, `B6_total_export_mw`
- **Validity window:** 365 days
- **Review tier:** `legal_counsel`
- **Typical days to receive:** 10
- **Partner-subset rule:** Only Site Partners whose contributions include `grid_interconnection`.

#### 4.1.7 `chp_commissioning_cert` — CHP commissioning certificate / WKK-inbedrijfstellingscertificaat

- **Status:** Conditional-Required
- **Condition:** `any contribution.asset == equipment_chp`
- **Collected at phase:** 3
- **Verifies registry fields:** `F1_chp_lease`, `F1a_chp_lease_fee`
- **Validity window:** 365 days
- **Review tier:** `sal`
- **Typical days to receive:** 14
- **Partner-subset rule:** Only Site Partners contributing `equipment_chp`.

#### 4.1.8 `chp_maintenance_contract` — CHP maintenance contract / WKK-onderhoudscontract

- **Status:** Conditional-Optional
- **Condition:** `any contribution.asset == equipment_chp`
- **Collected at phase:** 3
- **Verifies registry fields:** _(no field-level verification; document-as-checklist)_
- **Validity window:** 365 days
- **Review tier:** `legal_counsel`
- **Typical days to receive:** 14
- **Partner-subset rule:** Only Site Partners contributing `equipment_chp`.

#### 4.1.9 `chp_gasketel_cert` — Gas-boiler certificate (gasketel) / Gasketelcertificaat

- **Status:** Conditional-Required
- **Condition:** `any contribution.asset == equipment_chp AND chp is gas-fired`
- **Collected at phase:** 3
- **Verifies registry fields:** `F1_chp_lease`
- **Validity window:** 365 days
- **Review tier:** `sal`
- **Typical days to receive:** 14
- **Partner-subset rule:** Only Site Partners contributing `equipment_chp` AND the CHP is gas-fired.

#### 4.1.10 `bess_grid_sharing_agreement` — BESS grid-sharing agreement / BESS-netdelingsovereenkomst

- **Status:** Conditional-Optional
- **Condition:** `any contribution.asset == equipment_bess`
- **Collected at phase:** 4
- **Verifies registry fields:** `B4_total_connection_mva`, `B11_ato_transfer_mode`
- **Validity window:** 365 days
- **Review tier:** `legal_counsel`
- **Typical days to receive:** 21
- **Partner-subset rule:** Only Site Partners contributing `equipment_bess`.

#### 4.1.11 `bess_balancing_market_enrollment` — BESS balancing-market participation enrollment / BESS-inschrijving balanceringsmarkt

- **Status:** Conditional-Optional
- **Condition:** `any contribution.asset == equipment_bess`
- **Collected at phase:** 4
- **Verifies registry fields:** _(no field-level verification; document-as-checklist)_
- **Validity window:** 365 days
- **Review tier:** `sal`
- **Typical days to receive:** 14
- **Partner-subset rule:** Only Site Partners contributing `equipment_bess`.

#### 4.1.12 `solar_pv_yield_report` — Solar PV yield report / Opbrengstrapport zonnepanelen

- **Status:** Conditional-Required
- **Condition:** `any contribution.asset == equipment_solar_pv`
- **Collected at phase:** 4
- **Verifies registry fields:** _(no field-level verification; document-as-checklist)_
- **Validity window:** 365 days
- **Review tier:** `sal`
- **Typical days to receive:** 14
- **Partner-subset rule:** Only Site Partners contributing `equipment_solar_pv`.

#### 4.1.13 `solar_pv_connection_agreement` — Solar PV connection agreement / Zonnepanelen-aansluitovereenkomst

- **Status:** Conditional-Required
- **Condition:** `any contribution.asset == equipment_solar_pv`
- **Collected at phase:** 3
- **Verifies registry fields:** `B1_dso`, `B4_total_connection_mva`
- **Validity window:** 365 days
- **Review tier:** `legal_counsel`
- **Typical days to receive:** 21
- **Partner-subset rule:** Only Site Partners contributing `equipment_solar_pv`.

#### 4.1.14 `co2_supply_contract` — CO₂ supply contract (grower) / CO₂-leveringscontract (teler)

- **Status:** Conditional-Optional
- **Condition:** `crop_uses_co2_enrichment`
- **Collected at phase:** 4
- **Verifies registry fields:** _(no field-level verification; document-as-checklist)_
- **Validity window:** 365 days
- **Review tier:** `legal_counsel`
- **Typical days to receive:** 21
- **Partner-subset rule:** Only when `crop_uses_co2_enrichment`; collected from the grower partner.

#### 4.1.15 `bestemmingsplan_excerpt` — Zoning plan excerpt / Bestemmingsplan-uittreksel

- **Status:** Required
- **Collected at phase:** 5
- **Verifies registry fields:** `D4_zoning_designation`
- **Validity window:** 180 days
- **Review tier:** `sal`
- **Typical days to receive:** 5
- **Partner-subset rule:** Required for the site (cross-asset regulatory); collected from the partner holding `land`.

## 5. Chain of custody

Every uploaded document is registered in `{Counterparty}_Project_Benelux_Ops/documents/_manifest.json`. The SAL records:

| Field | Purpose |
|---|---|
| `path` | Relative path within `documents/` |
| `type` | Registry doc ID (one of the 15 above) |
| `hash` | `sha256:...` fingerprint (immutable proof of what was received) |
| `uploaded_at` | ISO 8601 UTC timestamp |
| `uploaded_by` | SAL owner or Co-owner |
| `parsed` | Boolean — has the parser run? |
| `parser_version_applied` | e.g., `ato_parser@1.0` — for regression auditing |
| `phase` | 1–5, per registry `request_at_phase` |
| `validity_expires` | `uploaded_at` + `validity_days` from registry |
| `partner_entity_id` | Which Site Partner this doc belongs to (enforces subset logic) |

The hash is computed **before** any redaction pass (see §6) so downstream verifiers can prove the SAL did not alter substantive content.

## 6. Redaction policy

Before uploading any document to the deal folder, the SAL removes 3rd-party PII that is not load-bearing for the HoT. Load-bearing PII (grower directors named in KVK, signatories on ATO, cadastral owner on Kadaster) is retained because it is directly referenced in the template.

Redaction targets typically include:

- Employee names in CHP maintenance contracts (except the counter-signatory)
- Customer account numbers on utility bills (if attached as supporting evidence)
- Unrelated parcels or co-owner details on Kadaster extracts covering multiple plots
- Banking / IBAN details in consent letters from financiers (only the legal entity + signatory are required)
- CO₂ supplier's private contact details (keep legal entity, supply volumes, term)

See `deal_folder_layout.md` for the per-document redaction checklist. Redaction is performed on a **copy**; the original hashed file is retained in a restricted-access subfolder for legal audit.

## 7. Quick-reference checklist (SAL-facing)

Print or clone this for each Site Partner. Tick only rows whose _Trigger_ matches the partner's contributions.

| ☐ | Trigger | Doc | NL label | Phase | Review | Days |
|---|---|---|---|---|---|---|
| ☐ | All partners | `kvk_uittreksel` (KVK extract) | KVK-uittreksel | 1 | `sal` | 1 d |
| ☐ | Land / property | `kadaster_uittreksel` (Kadaster extract) | Kadaster-uittreksel | 5 | `sal` | 3 d |
| ☐ | Land / property | `landowner_consent` (Landowner consent letter) | Instemmingsbrief grondeigenaar | 5 | `legal_counsel` | 21 d |
| ☐ | Land / property | `financier_consent` (Land Financier consent letter) | Instemmingsbrief grondfinancier | 5 | `legal_counsel` | 21 d |
| ☐ | Land / property | `site_plan` (Greenhouse layout / site plan) | Kasplattegrond / situatietekening | 5 | `sal` | 5 d |
| ☐ | Grid | `ato_document` (ATO document (DSO contract)) | ATO-document | 3 | `legal_counsel` | 10 d |
| ☐ | CHP | `chp_commissioning_cert` (CHP commissioning certificate) | WKK-inbedrijfstellingscertificaat | 3 | `sal` | 14 d |
| ☐ | CHP | `chp_maintenance_contract` (CHP maintenance contract) | WKK-onderhoudscontract | 3 | `legal_counsel` | 14 d |
| ☐ | CHP | `chp_gasketel_cert` (Gas-boiler certificate (gasketel)) | Gasketelcertificaat | 3 | `sal` | 14 d |
| ☐ | BESS | `bess_grid_sharing_agreement` (BESS grid-sharing agreement) | BESS-netdelingsovereenkomst | 4 | `legal_counsel` | 21 d |
| ☐ | BESS | `bess_balancing_market_enrollment` (BESS balancing-market participation enrollment) | BESS-inschrijving balanceringsmarkt | 4 | `sal` | 14 d |
| ☐ | Solar PV | `solar_pv_yield_report` (Solar PV yield report) | Opbrengstrapport zonnepanelen | 4 | `sal` | 14 d |
| ☐ | Solar PV | `solar_pv_connection_agreement` (Solar PV connection agreement) | Zonnepanelen-aansluitovereenkomst | 3 | `legal_counsel` | 21 d |
| ☐ | CO₂ crop | `co2_supply_contract` (CO₂ supply contract (grower)) | CO₂-leveringscontract (teler) | 4 | `legal_counsel` | 21 d |
| ☐ | Site-level | `bestemmingsplan_excerpt` (Zoning plan excerpt) | Bestemmingsplan-uittreksel | 5 | `sal` | 5 d |

**Completion gate:** A HoT draft cannot be generated for a Site Partner until every applicable row is ticked, uploaded, parsed, and non-expired.

---

### Appendix A — `_partner_subset_logic` (verbatim from registry)

> A supporting_documents entry is required for a site_partner ONLY if that partner's contributions[] includes an asset matching the entry's verify-scope. Examples: ATO required only for Grid Contributors (contributions.asset == grid_interconnection); Kadaster required only for Landowners (contributions.asset == land); Equipment OEM specs only for partners contributing that equipment class. For identity docs (KVK), required for every Site Partner regardless of contribution mix.

### Appendix B — Registry inconsistencies flagged at generation

- `bess_grid_sharing_agreement.verifies` references `B11_ato_transfer_mode`, but section B contains no field with that key (B.11 in v1.1 is `B11_future_import_mw`). The parser will fail to resolve this target — fix at next registry bump.
- Several entries lack a `verifies` list (`landowner_consent`, `financier_consent`, `site_plan`, `bess_balancing_market_enrollment`, `chp_maintenance_contract`, `solar_pv_yield_report`, `co2_supply_contract`). These act as evidentiary checklists rather than field-extraction inputs; that is intentional but should be made explicit by adding `verifies: []` to the four where the key is entirely missing (`kvk_uittreksel`-style entries that pre-date v1.1 schema tightening).
- `site_plan` has no `conditional` flag yet is marked `required: false` — treat as Optional (documented above).

---

_Regenerate this file from `sites/hot/field-registry.json` whenever the `supporting_documents` block is edited. Do not hand-edit rows — the registry is the source of truth._
