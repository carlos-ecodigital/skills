# Portal Contract — Phase-2 Intake Portal → `deal.yaml`

**Purpose:** Specification for the JSON payload that the future Site Partner intake portal emits, which the engine converts into a valid `deal.yaml` seeded with Phase-1 + Phase-2 (LOI-stage) fields. Enables Site Partners to self-serve the initial intake without SAL bottleneck, while preserving the data-authority chain.

**Authority anchors:**
- `deal_yaml_schema.md` — canonical `deal.yaml` shape; portal payload is a strict subset.
- `hot/field-registry.json § sections A–G` — bilingual labels (EN + NL), validation rules, phase assignments.
- `deal_folder_layout.md § 10` — drop-point convention at `{Counterparty}_Project_Benelux_Ops/portal-intake.json`.

**Scope boundary:**
- IN scope: field schema, validation rules, submission protocol, error surfacing, drop-point convention, bilingual labels.
- OUT of scope (explicitly): UI framework (React/Svelte/Vue — portal team's choice), authentication mechanism (SSO vs email-link — separate side-task), file hosting (portal writes to Drive or to an intermediate bucket — portal team's choice), portal deployment (Cloudflare Pages vs Vercel vs Netlify — portal team's choice), analytics / consent banners, i18n beyond the EN/NL pair defined here.

---

## 1. Schema — `portal-intake.json`

### 1.1 Top-level shape

```json
{
  "portal_contract_version": "1.0",
  "submitted_at": "2026-04-19T14:30:00+02:00",
  "submitted_by_email": "info@vangogkwekerijen.nl",
  "submitted_by_name": "Marion van Gog",
  "language_preference": "nl",
  "deal_context": {
    "hubspot_deal_id": 365739346165,
    "slug_hint": "van-gog-grubbenvorst",
    "counterparty_folder_name": "van Gog kwekerijen Grubbenvorst_Project_Benelux_Ops"
  },
  "site_partners": [ { /* one object per SP; see §2 */ } ],
  "locations": [ { /* one object per location; see §3 */ } ],
  "commercial": { /* see §4 */ },
  "attachments": [ { /* see §5 */ } ],
  "consent": {
    "gdpr_privacy_notice_read": true,
    "gdpr_privacy_notice_read_at": "2026-04-19T14:28:00+02:00",
    "information_is_accurate": true
  }
}
```

Fields marked `required` below are engine-blocking — submission cannot be accepted without them. Fields marked `optional` are fillable later by SAL.

### 1.2 Top-level field contract

| Field | Type | Required | Validation | Bilingual label (EN / NL) |
|---|---|---|---|---|
| `portal_contract_version` | string | required | equals `"1.0"` | — / — |
| `submitted_at` | string (ISO 8601) | required | ISO 8601 with TZ offset | Submission date / Datum van indiening |
| `submitted_by_email` | string (email) | required | RFC 5322; must match one of the `site_partners[].signatory.email` OR a delegated contact | Your email / Uw e-mailadres |
| `submitted_by_name` | string | required | min 2 chars | Your name / Uw naam |
| `language_preference` | string | required | `"en"` or `"nl"` — drives error-message language | Preferred language / Taalvoorkeur |
| `deal_context.hubspot_deal_id` | integer | required | positive integer; must resolve to a Deal in pipeline `492649440` | — / — |
| `deal_context.slug_hint` | string | optional | kebab-case; engine regenerates if absent | — / — |
| `deal_context.counterparty_folder_name` | string | required | matches folder naming convention (see `deal_folder_layout.md § 1.1`) | — / — |
| `consent.gdpr_privacy_notice_read` | boolean | required | must be `true` | I have read the privacy notice / Ik heb de privacyverklaring gelezen |
| `consent.gdpr_privacy_notice_read_at` | string (ISO 8601) | required | ISO 8601 with TZ | Timestamp / Tijdstempel |
| `consent.information_is_accurate` | boolean | required | must be `true` | I confirm the information above is accurate to the best of my knowledge / Ik bevestig dat de bovenstaande informatie naar mijn beste weten juist is |

---

## 2. Site Partners

One object per Site Partner. For multi-B.V. deals (Van Gog pattern), portal supports up to 5 SPs in a single submission; more than 5 → SAL splits into multiple deals.

### 2.1 Per-SP field contract

| Field | Type | Required | Validation | Bilingual label (EN / NL) |
|---|---|---|---|---|
| `legal_name` | string | required | must end with valid Dutch entity suffix: `B.V.`, `V.O.F.`, `C.V.`, `N.V.`, `Coöperatie U.A.` (registry A.1) | Legal company name / Statutaire naam |
| `kvk` | string | required | regex `^\d{8}$` (registry A.2) | KVK number / KVK-nummer |
| `registered_address` | string | required | non-empty; portal hints at "street, postcode, city" format (registry A.3) | Registered address (street, postcode, city) / Statutair adres (straat, postcode, plaats) |
| `entity_form` | string | optional | derived from `legal_name` suffix if absent | Entity form / Rechtsvorm |
| `sector` | string | optional | free-form; used for Pillar 2 scaffolding | Sector / Sector |
| `year_founded` | integer | optional | 1900 ≤ year ≤ current | Year founded / Oprichtingsjaar |
| `signatory.name` | string | required | min 2 chars (registry A.4) | Name of signatory / Naam ondertekenaar |
| `signatory.title` | string | required | min 2 chars; example "Directeur" (registry A.5) | Title of signatory / Functie ondertekenaar |
| `signatory.email` | string (email) | required | RFC 5322 | Email of signatory / E-mail ondertekenaar |
| `signatory.signing_authority` | enum | required | `"sole"` or `"joint"` (registry A.6) | Signing authority / Tekenbevoegdheid |
| `signatory.joint_signatory_name` | string | conditional | required if `signing_authority == "joint"` | Co-signatory name / Naam medeondertekenaar |
| `signatory.joint_signatory_title` | string | conditional | required if `signing_authority == "joint"` | Co-signatory title / Functie medeondertekenaar |
| `signatory.joint_signatory_email` | string (email) | conditional | required if `signing_authority == "joint"` | Co-signatory email / E-mail medeondertekenaar |
| `role_self_declared` | array of enum | required | non-empty subset of `["grid_contributor", "landowner", "heat_offtaker", "bess_co_developer"]` | Role(s) in this project / Rol(len) in dit project |
| `source_map.pillar_1` | array of string (URL) | optional | each a valid URL | Public sources about your company / Openbare bronnen over uw bedrijf |

### 2.2 Multi-B.V. note

When a single family holding operates multiple B.V.s (Van Gog pattern), the portal UI should let the Site Partner identify linked SPs via an "add another entity" button. Each linked entity becomes its own `site_partners[]` object. The portal may pre-fill `registered_address` from a prior SP when the user clicks "same as [SP #1]".

---

## 3. Locations

### 3.1 Per-location field contract

| Field | Type | Required | Validation | Bilingual label (EN / NL) |
|---|---|---|---|---|
| `parcel_id` | string | required | format hint `gemeente sectie nummer` (registry D.1) | Kadaster parcel reference / Kadastrale perceelreferentie |
| `address` | string | required | non-empty | Address / Adres |
| `postcode` | string | required | Dutch postcode regex `^\d{4}\s?[A-Z]{2}$` (case-insensitive, normalised to uppercase + single space) | Postcode / Postcode |
| `municipality` | string | optional | free-form | Municipality / Gemeente |
| `dso` | enum | required | one of `["Liander", "Stedin", "Enexis", "Westland Infra", "Coteq", "Rendo", "Other"]` (registry B.1); if `"Other"`, free-form `dso_other` field must be filled | DSO / Netbeheerder |
| `dso_other` | string | conditional | required if `dso == "Other"` | Other DSO (specify) / Andere netbeheerder (specificeer) |
| `ean_code` | string | optional (required for Grid Contributor SP) | regex `^871\d{15}$` (registry B.2) | EAN code (18 digits, starts with 871) / EAN-code (18 cijfers, begint met 871) |
| `mva` | number | optional (required for Grid Contributor SP) | positive number (registry B.4) | Total connection capacity (MVA) / Totale aansluitcapaciteit (MVA) |
| `import_mw` | number | optional (required for Grid Contributor SP) | non-negative (registry B.5) | Import capacity (MW) / Invoercapaciteit (MW) |
| `export_mw` | number | optional (required for Grid Contributor SP) | non-negative (registry B.6) | Export capacity (MW) / Uitvoercapaciteit (MW) |
| `zoning_designation` | string | optional (required for Landowner SP) | free-form (registry D.4) | Zoning designation / Bestemming |
| `title_type` | enum | optional (required for Landowner SP) | `"full_ownership"` / `"erfpacht"` / `"other"` (registry D.2) | Title type / Eigendomstype |
| `encumbrances` | enum | optional (required for Landowner SP) | `"none"` / `"mortgage"` / `"other"` (registry D.3) | Encumbrances / Bezwaringen |
| `area_m2` | number | optional | positive | Available land area (m²) / Beschikbare grondoppervlakte (m²) |
| `linked_site_partner_kvk` | string | required | KvK of the Site Partner that holds primary rights at this location | Which entity holds rights at this location? / Welke entiteit houdt rechten op deze locatie? |

---

## 4. Commercial (LOI-stage preliminary)

| Field | Type | Required | Validation | Bilingual label (EN / NL) |
|---|---|---|---|---|
| `preliminary_heat_offtake_mwh_per_year` | number | optional | non-negative | Approximate annual heat demand (MWh) / Bij benadering jaarlijkse warmtevraag (MWh) |
| `preliminary_heat_price_eur_mwh` | number | optional | non-negative | Indicative heat price (EUR/MWh) / Indicatieve warmteprijs (EUR/MWh) |
| `preliminary_timeline_preference` | enum | optional | `"asap"`, `"within_12_months"`, `"1_2_years"`, `"na"` | Preferred timeline / Gewenste planning |
| `existing_heat_source` | enum | optional | `"gas_chp_wkk"`, `"gas_boiler"`, `"biomass"`, `"electric"`, `"other"` | Current heat source / Huidige warmtebron |
| `bess_co_development_interest` | boolean | optional | — | Interested in BESS co-development? / Interesse in BESS mede-ontwikkeling? |
| `bess_co_invest_pct_appetite` | number | conditional | 0 ≤ x ≤ 50; required if `bess_co_development_interest == true` | BESS co-investment appetite (%) / BESS mede-investeringsbereidheid (%) |

---

## 5. Attachments

SP uploads supporting documents via the portal. Each becomes an entry in the payload + is relayed into `documents/`.

### 5.1 Per-attachment field contract

| Field | Type | Required | Validation |
|---|---|---|---|
| `type` | enum | required | one of `supporting_documents` enum values (see `hot/field-registry.json`) |
| `filename` | string | required | sanitised (alphanumeric + `_` + `-` + `.`); max 120 chars |
| `size_bytes` | integer | required | ≤ 20 MB per file; ≤ 100 MB total submission |
| `mime_type` | string | required | `"application/pdf"` or `"image/jpeg"` (scans/photos of paper consents accepted) |
| `sha256` | string | required | computed by portal on upload |
| `partner_kvk` | string | required | KvK of the SP this document pertains to |
| `issued_date` | string (YYYY-MM-DD) | optional | if absent, engine uses upload timestamp |
| `upload_url` | string (URL) | required | secure URL for engine to fetch the file — signed, time-limited |

### 5.2 Accepted types at Phase-1 (portal Phase-1 = initial submission, not registry Phase-1)

Initial submission accepts these document types:

- `kvk_uittreksel` (most valuable single upload; validates Identity)
- `ato_document` (Grid Contributor)
- `kadaster_uittreksel` (Landowner)
- `bestemmingsplan_excerpt` (Landowner)
- `site_plan` (optional)

Post-LOI documents (landowner_consent, financier_consent, chp_*, bess_*, solar_pv_*, co2_supply_contract, gas_supply_contract) are collected via the SAL document-collection workflow per `sal_runbook.md § Step 4`, not the initial portal submission. The portal may offer a second "add documents later" tab, but the initial submission requires only the five above.

---

## 6. Validation & error surfacing

### 6.1 Client-side pre-submission validation

The portal UI enforces:

1. All `required` fields populated.
2. All regex-validated fields match pattern (KvK, EAN, postcode, email).
3. Conditional-required fields populated when their condition is met (joint signatory fields, DSO_other, BESS co-invest pct, Grid Contributor capacity fields, Landowner title fields).
4. File size + MIME-type per-attachment limits enforced.
5. Consent checkboxes ticked.

Validation errors are surfaced inline per field, in the `language_preference` chosen at session start. Errors block submission.

### 6.2 Server-side validation (engine-side, post-submission)

The engine validates:

1. All client-side validation rules re-checked (defence in depth).
2. `hubspot_deal_id` resolves to a Deal in pipeline `492649440`.
3. `submitted_by_email` matches a known SP signatory or delegated contact for the Deal.
4. SHA-256 hashes match after engine download.
5. KvK cross-check against KVK API (not blocking; enrichment-only).
6. EAN checksum (EAN-18 modulo check); warn on fail.
7. Postcode→DSO consistency (not blocking; enrichment-only).

Server-side failures return a structured error list to the portal:

```json
{
  "status": "error",
  "errors": [
    {
      "field": "site_partners[0].kvk",
      "code": "KVK_NOT_FOUND",
      "message_en": "KvK number not found in KVK register",
      "message_nl": "KVK-nummer niet gevonden in het Handelsregister",
      "severity": "warn",
      "blocking": false
    }
  ]
}
```

Severity values: `"fail"` (blocks acceptance), `"warn"` (accepted; flagged to SAL for review).

### 6.3 Error-message locale rules

- All user-facing messages produced in `language_preference` (NL or EN).
- Engine logs + internal error traces remain in English for SAL readability regardless of user locale.
- A user-facing NL fallback to EN is acceptable when a specific error message has not yet been translated; engine emits `message_nl` equal to `message_en` and flags `translation_pending: true` for portal maintainer.

---

## 7. Submission protocol

### 7.1 Drop-point

On acceptance, portal relays the payload to:

```
{Counterparty}_Project_Benelux_Ops/portal-intake.json
```

Canonical location per `deal_folder_layout.md § 10`. Attachments are downloaded by the engine from `upload_url` values and placed into `{Counterparty}_Project_Benelux_Ops/documents/` with filenames matching the convention in `deal_folder_layout.md § 4.1`.

### 7.2 One-shot transform

Engine runs a one-shot transform: `portal-intake.json` → `deal.yaml`. Transform logic:

1. Copy `deal_context.*` → top-level identity fields.
2. For each `site_partners[]` entry, construct a `deal.yaml.site_partners[]` entry, mapping portal fields to schema fields. `role_self_declared` becomes a SAL-review hint (engine does NOT accept self-declared roles as authoritative; SAL confirms against contributions during intake review).
3. For each `locations[]` entry, construct a `deal.yaml.locations[]` entry.
4. For each `attachments[]` entry, construct a `deal.yaml.documents[]` entry + add to `documents/_manifest.json`.
5. Write `portal_intake_received_at`, `portal_intake_payload_hash` into `deal.yaml.portal_intake_metadata`.
6. Emit a transform report at `drafts/portal-transform-report.json` with any warn-severity issues for SAL review.

After transform, SAL is notified (HubSpot Deal comment + optionally email) to review in SAL workflow Step 2 (Confirm & enrich).

### 7.3 Idempotence

Re-submission (SP resubmits with corrections) overwrites `portal-intake.json` but does NOT overwrite `deal.yaml` — the engine produces a diff and asks SAL to accept/reject changes field-by-field.

### 7.4 Write-back to HubSpot

Portal submission does NOT directly write to HubSpot. The engine writes to HubSpot (if at all) on SAL's next invocation, honoring the data-authority chain: parsed documents (attachments) > HubSpot > LOI intake > portal. Portal submission is treated as "LOI intake" tier for conflict-resolution purposes; SAL can promote specific fields to a higher tier with justification.

---

## 8. Security & privacy

### 8.1 Authentication

OUT of scope for this contract. Portal team decides between:

- Email-link + one-time code to a known signatory email on the Deal.
- Microsoft / Google OIDC SSO for counterparties with corporate accounts.
- Bank-ID (iDIN) — Dutch preference.

Whatever mechanism is chosen, `submitted_by_email` must be verified before submission is accepted by the engine.

### 8.2 Data protection

- Portal stores submitted data encrypted at rest (AES-256 or better).
- Attachments transit via HTTPS only; `upload_url` is time-limited (24 hours post-submission).
- GDPR privacy notice is shown on landing page; consent is captured in the submission payload.
- Submissions are retained by the portal for 90 days for user edit-resubmit; thereafter deleted from portal storage while preserved in the deal folder (which has its own retention policy).

### 8.3 Injection safety

All string inputs are treated as untrusted; engine sanitises before interpolating into `deal.yaml`, .docx templates, or HubSpot writes. Portal UI + engine both XSS-escape user-submitted strings before rendering.

---

## 9. Bilingual labels — consolidated

For portal UI i18n, the labels defined in §2–§4 form the authoritative bilingual dictionary for the initial submission form. Additional UI strings (button labels, navigation, confirmation screens) are out of scope for this contract and are the portal team's responsibility.

Authoritative label precedence: `hot/field-registry.json § sections A-G` → this contract's bilingual columns → any fallback. Registry is the single source of truth; this contract mirrors and is kept in sync on registry version bumps.

---

## 10. Versioning & evolution

- `portal_contract_version: "1.0"` is the initial release.
- `1.x` versions add optional fields only (backward compatible).
- `2.0` reserved for breaking changes (renamed required fields, removed fields, changed required-ness).
- Engine must accept any `portal_contract_version` for which a transform is registered; unknown version → reject with clear error.

---

## 11. Gaps / TODOs

1. **Authentication mechanism** — deferred to portal side-task; this contract assumes email-verified submitter but does not bind to a mechanism.
2. **Attachment hosting** — engine expects signed `upload_url`s; portal team chooses the storage backend.
3. **UI framework + design system** — out of scope; DE brand palette (`project_de_brand_palette` memory) is the reference for visual style when portal team starts.
4. **Offline / partial saves** — portal may save draft submissions; payload shape for drafts is identical except `consent.*` may be incomplete. Engine ignores drafts (portal `status: "draft"`); only `status: "submitted"` payloads are transformed.
5. **Post-submission SP edit** — SP can edit until SAL promotes the submission into `deal.yaml`. Thereafter, changes go through SAL.
6. **Multi-site deals** — where a single SP has multiple project sites under the same LOI, portal supports multiple `locations[]` entries linked to one or more SPs. UX for this is portal team's call; schema supports it.

TODO(portal team): when portal scope kicks off, publish a `portal_implementation_plan.md` referencing this contract version.
