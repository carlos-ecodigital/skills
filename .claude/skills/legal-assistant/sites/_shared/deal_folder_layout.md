# Deal Folder Layout — `{Counterparty}_Project_Benelux_Ops/`

**Purpose:** Operational spec for the per-deal Drive folder that hosts `deal.yaml`, parser-input documents, generated drafts, and signed artefacts. Canonical for all deals originated by the Sites Stream (Site Sourcing — LOI + HoT).

**Authority anchors:**
- `deal_yaml_schema.md § Top-level shape` — `counterparty_folder_name`, `documents[]`, `generated.*_path`, `timeline.*`.
- `hot/field-registry.json § supporting_documents` — authoritative doc-type enum.
- Existing Drive state (April 2026) — several folders predate this spec and are grandfathered (see §1.2).

---

## 1. Folder naming

### 1.1 Canonical convention

```
{Counterparty}_Project_Benelux_Ops/
```

Rules:

- `{Counterparty}` — short human name in Title Case, generally mirroring the HubSpot Company name primary hyphenated form. When the deal spans multiple linked B.V.s (Van Gog pattern), use the family/group short name, **not** the specific role-filling B.V.
- Suffix `_Project_Benelux_Ops` is mandatory for new folders.
- `_Ops` distinguishes the operational project folder from any legacy marketing or prospect folders.

**Examples:**

```
van Gog kwekerijen Grubbenvorst_Project_Benelux_Ops/
Westland Bloemen_Project_Benelux_Ops/
Greenhouse Consortium Noord-Holland_Project_Benelux_Ops/
```

### 1.2 Grandfathered variants

Folders created before this spec may appear under these variants. The engine accepts them at read-time via `counterparty_folder_name` override in `deal.yaml`; all new folders must use the canonical form.

| Variant | Status | Example |
|---|---|---|
| `{Counterparty}_Project_Benelux/` (no `_Ops`) | Grandfathered — read-only support | `Solynta_Project_Benelux/` |
| `{Counterparty}_Project_Benelux_Ops_typofix/` (typo variants) | Grandfathered — document in `deal.yaml.notes` | rare; case-by-case |
| All-lowercase / kebab-case | Grandfathered — read-only support | `van-gog-grubbenvorst_project_benelux_ops/` |

TODO(SAL lead): an audit of existing Drive folders for non-canonical variants should be produced; the migration path is "rename on next deal touch" (not bulk-rename).

---

## 2. Subfolder contract

```
{Counterparty}_Project_Benelux_Ops/
├── deal.yaml                             # SSOT — always at root
├── deal.yaml.lock                        # optional — engine-held advisory lock during writes
├── documents/
│   ├── _manifest.json                    # chain-of-custody register
│   ├── kvk_uittreksel_{kvk}_{YYYYMMDD}.pdf
│   ├── ato_document_{ean_last6}_{YYYYMMDD}.pdf
│   ├── kadaster_uittreksel_{parcel_id}_{YYYYMMDD}.pdf
│   ├── bestemmingsplan_excerpt_{gemeente}_{YYYYMMDD}.pdf
│   ├── landowner_consent_{YYYYMMDD}.pdf  (conditional)
│   ├── financier_consent_{YYYYMMDD}.pdf  (conditional)
│   ├── site_plan_{YYYYMMDD}.pdf          (optional)
│   └── … additional supporting docs per registry
├── drafts/
│   ├── YYYYMMDD_DE_LOI_Site_{slug}_v1_(DRAFT).docx
│   ├── YYYYMMDD_DE_LOI_Site_{slug}_v1_qa.txt
│   ├── YYYYMMDD_DE_HoT_Site_{slug}_v1_(DRAFT).docx
│   ├── YYYYMMDD_DE_HoT_Site_{slug}_v1_qa.txt
│   ├── cross-doc-gate-report.json
│   └── hubspot-sync-log.json
├── signed/                               # populated at execution
│   └── → moved to /Signed HoTs/ shared Drive once both counterparts have signed
├── portal-intake.json                    # optional — Phase-2 portal drop-point
└── notes/                                # free-form SAL notes; not consumed by engine
    ├── meeting_notes_YYYYMMDD.md
    └── redaction_log_YYYYMMDD.md
```

**Root-only files:** `deal.yaml` and `portal-intake.json` (when present). All other files live in their subfolder.

**Engine-managed subfolders:** `documents/` (read-write on upload; read-only on parse), `drafts/` (write-only by engine, versioned), `signed/` (read-only after move).

---

## 3. `deal.yaml` placement and lifecycle

### 3.1 Placement

Single file at folder root. Never duplicated; never in subfolders.

### 3.2 Lifecycle

| Phase | Event | Writer | Notes |
|---|---|---|---|
| Creation | SAL opens intake | SAL (manually) or engine (auto-hydrated from HubSpot) | Includes `deal_yaml_schema_version`, `slug`, `hubspot_deal_id`, `counterparty_folder_name` |
| LOI stage | `stage: loi` fields filled | SAL + engine | Engine resolves conflicts per data-authority chain |
| Documents collected | Post-LOI docs uploaded | SAL | `documents[]` array updated with SHA-256 + parser version |
| HoT stage | `stage: hot` fields filled | engine + SAL | Engine runs enrichment + cross-doc gate, writes back to `enrichment.*`, `hubspot.conflict_log` |
| Regeneration | Counter-offer or SAL correction | engine | `generated.*_hash` recomputed; version bumped in filename |
| Execution | Counterparts signed | SAL | `timeline.loi_signed_date` / `.hot_signed_date` set; signed PDFs moved to `signed/` then relayed to `/Signed HoTs/` |

### 3.3 Advisory lock

Engine writes of `deal.yaml` are atomic (rename-based) to avoid split writes during long runs. An optional `deal.yaml.lock` sentinel file may be held by the engine for the duration of enrichment; SAL tooling should refuse writes while the lock exists.

---

## 4. Document conventions (`documents/`)

### 4.1 Filename pattern

```
{doc_type}_{discriminator}_{YYYYMMDD}.{ext}
```

- `doc_type` — authoritative enum from `hot/field-registry.json § supporting_documents` (e.g., `kvk_uittreksel`, `ato_document`, `kadaster_uittreksel`, `bestemmingsplan_excerpt`, `landowner_consent`, `financier_consent`, `site_plan`, `bess_grid_sharing_agreement`, `bess_balancing_market_enrollment`, `chp_commissioning_cert`, `chp_maintenance_contract`, `chp_gasketel_cert`, `solar_pv_yield_report`, `solar_pv_connection_agreement`, `co2_supply_contract`, `gas_supply_contract`).
- `discriminator` — short stable identifier:
  - KvK extract → `{kvk}` (8 digits)
  - ATO → `{ean_last6}` (last 6 of EAN — avoids EAN PII exposure in filename)
  - Kadaster → `{parcel_id_normalised}` (e.g., `GRUBBENVORST-A-1234`)
  - Bestemmingsplan → `{gemeente}` slug
  - Consent letters → omit discriminator or use counterparty short name
- `YYYYMMDD` — date the document was **issued** (not uploaded). If issuance date is unclear, use `YYYYMMDD` of upload with a trailing `_upl`.
- Extension — typically `pdf`; scans accepted as `pdf`; photos of paper consents as `jpg` with SAL annotation in notes.

### 4.2 Collision suffix

Multiple documents of the same type on the same day for the same discriminator use letter suffixes: `_a`, `_b`, `_c` (e.g., two ATO documents on the same day for different tranches: `ato_document_871687_20260410_a.pdf` + `ato_document_871687_20260410_b.pdf`). Rare in practice.

### 4.3 `_manifest.json` — chain-of-custody register

Required at `documents/_manifest.json`. Every file in `documents/` has an entry. Schema:

```json
{
  "manifest_version": "1.0",
  "documents": [
    {
      "path": "kvk_uittreksel_12345678_20260415.pdf",
      "type": "kvk_uittreksel",
      "hash": "sha256:3a4f…",
      "size_bytes": 184321,
      "uploaded_at": "2026-04-15T11:23:04+02:00",
      "uploaded_by": "co.tenwolde@digitalenergy.eu",
      "issued_date": "2026-04-15",
      "parser_version_applied": "kvk_parser@1.0",
      "parser_status": "success",
      "parser_output_ref": "deal.yaml#enrichment.kvk_active",
      "partner_entity_id": "12345678901",
      "validity_days": 90,
      "validity_expires": "2026-07-14"
    }
  ]
}
```

- `hash` — `sha256:` prefix + 64 hex chars, computed on upload.
- `uploaded_at` — ISO 8601 with local timezone offset.
- `uploaded_by` — email or username.
- `partner_entity_id` — HubSpot Company ID of the Site Partner this doc pertains to; used by cross-doc gate to match docs to the correct SP subset.
- `validity_expires` — uploaded_at + `supporting_documents.<type>.validity_days` per registry. Stale docs trigger `Con` class warnings.
- `parser_status` — `success | partial | failed | manual`. `manual` = no automated parser available (e.g., `landowner_consent`).

---

## 5. Drafts conventions (`drafts/`)

### 5.1 Filename pattern

```
YYYYMMDD_DE_{DocType}_Site_{slug}_v{N}[{sub}]_(STATE).docx
YYYYMMDD_DE_{DocType}_Site_{slug}_v{N}[{sub}]_qa.txt
```

- `YYYYMMDD` — generation date.
- `DE` — fixed producer prefix.
- `{DocType}` — `LOI` or `HoT`.
- `Site` — document class.
- `{slug}` — `deal.yaml.slug`.
- `v{N}` — major version (starts at `v1`).
- `{sub}` — optional collision suffix `b`, `c`, … for same-day regeneration (e.g., `v1b`).
- `(STATE)` — `(DRAFT)` during work, `(FINAL)` on SAL freeze, `(SIGNED)` after execution.

### 5.2 QA sidecar

Every .docx has a matching `_qa.txt` generated by `site_qa_gate.md` rules (mirrors commercial `loi-qa-gate.md` output format). Filename replaces `.docx` with `_qa.txt` (note: the state suffix is dropped from the QA filename to avoid proliferation):

```
20260419_DE_LOI_Site_van-gog-grubbenvorst_v1_(DRAFT).docx
20260419_DE_LOI_Site_van-gog-grubbenvorst_v1_qa.txt
```

### 5.3 Cross-doc gate report

Single JSON at `drafts/cross-doc-gate-report.json`, overwritten on each HoT generation. Schema (indicative):

```json
{
  "generated_at": "2026-04-19T16:22:10+02:00",
  "deal_yaml_hash": "sha256:...",
  "findings": [
    {
      "rule_id": "DataAcc-1",
      "severity": "fail",
      "message": "No HubSpot Companies associated with Deal 365739346165",
      "resolution_hint": "Create + associate Site Partner B.V.s in HubSpot before HoT generation"
    },
    {
      "rule_id": "Con-3",
      "severity": "warn",
      "message": "ATO document expired 2024-09-01; validity_days=365; 206 days stale",
      "resolution_hint": "Request fresh ATO from Grid Contributor"
    }
  ],
  "overrides_applied": [],
  "status": "FAIL"
}
```

### 5.4 HubSpot sync log

Append-only JSONL at `drafts/hubspot-sync-log.json` (file extension `.json` retained for tooling compatibility; content is line-delimited):

```json
{"at": "2026-04-19T16:22:11+02:00", "direction": "HS→yaml", "field": "contract_capacity___available__mw_", "hs_value": 25.5, "yaml_value": null, "resolution": "hs_to_yaml"}
{"at": "2026-04-19T16:22:12+02:00", "direction": "yaml→HS", "field": "what_s_your_approximate_heat_capacity__mwth___", "yaml_value": 21.25, "hs_value": null, "resolution": "enrichment_writeback", "source_doc_ref": "documents/ato_document_871687_20260415.pdf"}
```

---

## 6. Signed artefacts (`signed/`)

### 6.1 Local placement

On execution, the SAL moves the signed PDFs into `signed/`:

```
YYYYMMDD_DE_LOI_Site_{slug}_v{N}_(SIGNED).pdf
YYYYMMDD_DE_HoT_Site_{slug}_v{N}_(SIGNED).pdf
```

The SAL updates `deal.yaml.timeline.loi_signed_date` / `.hot_signed_date` at the same time.

### 6.2 Relay to `/Signed HoTs/`

Executed HoT PDFs are then relayed to the shared Drive folder `/Signed HoTs/` so that downstream teams (finance, legal archive, MSA stream) can index from a single location. The LOI may remain deal-local (policy: LOIs are not indexed centrally; HoTs are).

Relay is performed by SAL, not by the engine. Engine records the relay in `deal.yaml.generated.hot_v1_signed_copy_path` when SAL confirms.

---

## 7. Version lifecycle

### 7.1 Major versions

- `v1` — first SAL-approved draft shared externally (or ready to be).
- `v2` — produced on counter-offer or substantive re-draft triggered by counterpart feedback.
- `v3`, `v4`, … — further iterations.

Version bump triggers:

- Counterpart returns redlines requiring a re-draft (not simple accept-changes).
- SAL applies a material change (new Site Partner added, new location added, pricing restructured).
- Engine cannot apply the change inline via `deal.yaml` edit + regenerate at the same version; if structural.

Non-triggers (stay on same major version):

- Typo corrections.
- Signatory name update.
- Same-day regeneration after SAL feedback (use `_v1b` sub-suffix instead).

### 7.2 State suffixes

- `(DRAFT)` — in SAL's hands; not shared externally except under "subject to review" banner.
- `(FINAL)` — SAL has frozen; counterpart review copy.
- `(SIGNED)` — executed PDF; lives only in `signed/` + `/Signed HoTs/`.

### 7.3 Retention

- `(DRAFT)` — retained for audit; never deleted.
- `(FINAL)` — retained for audit.
- `(SIGNED)` — retained permanently in `/Signed HoTs/`; local `signed/` copy retained.

---

## 8. Chain-of-custody policy

Every document in `documents/` MUST have a `_manifest.json` entry within the same commit / Drive sync interval (target: under 5 minutes). The cross-doc gate reports a **DataAcc-3** fail when a file exists in `documents/` with no manifest entry or vice versa.

The manifest is append-only; a superseded document (e.g., fresh ATO replacing an expired one) gets a new entry with a new filename. The old file is **not deleted** — it remains in `documents/` with a `superseded_by: "ato_document_…_a.pdf"` field in its manifest entry. Audit trail is preserved.

If a document must be removed for legal or privacy reasons, SAL logs the removal in `notes/redaction_log_{YYYYMMDD}.md` and updates the manifest entry with `removed: true` + `removal_reason: "..."` + `removed_by:` + `removed_at:`.

---

## 9. Redaction policy

### 9.1 PII before upload

SAL redacts third-party PII from supporting documents before upload. Per-doc-type checklist:

| Doc type | Redaction targets |
|---|---|
| `kvk_uittreksel` | Private addresses of individual UBOs (home addresses); personal phone numbers. Keep: legal entity name, KvK, registered office, functionaries with title. |
| `ato_document` | Customer bank details; internal DSO contact emails. Keep: EAN, MVA, import/export MW, contract dates, parties. |
| `kadaster_uittreksel` | N/A — Kadaster extracts are already a public record; no redaction required. |
| `bestemmingsplan_excerpt` | N/A — municipal public record. |
| `landowner_consent` | Only if the consent letter contains unrelated personal data of the landowner (phone, BSN). |
| `financier_consent` | Bank employee contact details, internal memo references, account numbers. Keep: bank legal name, consent scope, signing authority. |
| `site_plan` | Private residential details on adjacent parcels. |
| `chp_commissioning_cert` | Operator bank details if present. |
| `co2_supply_contract` | Bank details; counterparty commercial terms unrelated to the CO₂ supply (if the contract is a bundle). |

### 9.2 Redaction log

Every redaction is logged in `notes/redaction_log_{YYYYMMDD}.md` with:

- Document affected.
- Field(s) redacted.
- Redaction method (black box; replaced with `[REDACTED — PII]`; etc.).
- Redactor (SAL email).
- Justification.

---

## 10. Portal drop-point (future Phase 2)

When the intake portal ships (see `portal_contract.md`), Site Partner submissions land at `portal-intake.json` at the folder root. A one-shot engine transform converts the JSON into `deal.yaml` + uploads any attached documents into `documents/`.

Until the portal ships, this file is absent; SAL fills `deal.yaml` manually.

---

## 11. `notes/` — free-form SAL workspace

Not consumed by the engine. SAL-only. Typical contents:

- `meeting_notes_YYYYMMDD.md` — Fireflies transcripts, call summaries, key commitments from the counterpart.
- `redaction_log_YYYYMMDD.md` — see §9.2.
- `SAL_log.md` — running log of decisions, escalations, follow-ups.
- `counterpart_correspondence/` — copies of emails requested by finance/legal for archival; not consumed by any parser.

Folder structure inside `notes/` is up to SAL discretion.

---

## 12. Validation (implemented via `site_doc_base.validate_folder_layout`)

Checks performed on folder open:

1. `deal.yaml` present at root.
2. `documents/` and `drafts/` exist (create if missing).
3. `documents/_manifest.json` exists iff `documents/` is non-empty.
4. Every file in `documents/` has a manifest entry and vice versa (DataAcc-3).
5. `deal.yaml.counterparty_folder_name` matches folder-on-disk name (warn if mismatch).
6. No unexpected files at folder root (warn if present; ignore if in `.ignore` list: `.DS_Store`, `Thumbs.db`, `~$*.docx`).

Failures return a structured list to the skill runner; SAL decides whether to correct now or proceed with override.

---

## 13. Gaps / TODOs

1. **Grandfathered folder audit** — no authoritative list of existing non-canonical folders; TODO(SAL lead) to produce + socialise rename plan.
2. **`/Signed HoTs/` folder spec** — location + access policy are referenced here but not formally spec'd; TODO(Halyna / admin ops) to publish.
3. **Manifest schema version bump policy** — v1.0 manifest omits `schema_version` per-file fields (only `manifest_version` at top); v1.1 should add.
4. **Cross-deal document reuse** — if the same `kvk_uittreksel` is valid for multiple deals (same Site Partner, multiple sites), current spec duplicates the file. Future: a shared `_kvk_cache/` at the SAL workspace level with hashed dedup. Not v1.0.
5. **Hash algorithm** — SHA-256 is mandated here; no provision for rotation. Adequate for audit, not for adversarial settings. No action required at v1.0.
