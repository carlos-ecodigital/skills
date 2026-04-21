# Site Acquisition Lead (SAL) Runbook — Sites Stream

**Audience:** The Site Acquisition Lead currently responsible for originating and advancing Site deals (LOI → HoT) within the DE Benelux pipeline. Current incumbent: Co ten Wolde.

**Purpose:** Step-by-step operational guide. Companion to `SKILL.md`, `SOP.md`, `deal_yaml_schema.md`, `asset_taxonomy.md`, `recital_b_pillars.md`, `deal_folder_layout.md`, `site_qa_gate.md`, `portal_contract.md`. This runbook is the *doing* surface; the others are the *knowing* surfaces.

**Hard boundary (repeated):** the engine + test suite catch **structural**, **format**, **registry**, and **rule** failures. The SAL owns **data accuracy** — the right KvK number, the right parcel ID, the right MW figure — unless that field has a parsed-document authority (kvk_uittreksel, ato_document, kadaster_uittreksel), in which case the cross-doc gate catches mismatches. If a field has no document authority, garbage in → garbage out; QA will not save you.

---

## Prerequisites

Before invoking the Sites skill for a specific deal, the SAL must have:

1. **Sales-intake qualification.** The SP must have passed at least Tier 2 on the S-GRW (Site — Grower) sales-intake score (criteria: verified contact, confirmed asset holding, operational decision-maker identified). Deals below Tier 2 stay in sales-intake until qualified.
2. **HubSpot Deal in the Sites pipeline.** Pipeline ID `492649440`, in a dealstage between "New Deal" and "HoT Drafted". The Deal must have `deal_name`, `deal_stage`, and `deal_owner_id` set. TODO(SAL): confirm stage IDs + publish in a pipeline-stages reference doc.
3. **Drive folder created.** `{Counterparty}_Project_Benelux_Ops/` per `deal_folder_layout.md § 1.1`. Subfolders `documents/` and `drafts/` present.
4. **HubSpot Company records** for each Site Partner (ideally; the engine can proceed on LOI without Companies but HoT will fail at DataAcc-1 until Companies are associated).
5. **Permissions.** SAL has HubSpot Deal/Company/Contact read+write; Drive write on the deal folder; skill invocation privileges.

If any of these are missing, the engine surfaces them in Step 1 as blocking prerequisites and will not proceed.

---

## Step 1 — Open intake

### SAL action

Invoke the skill with the deal slug:

```
/legal-assistant sites loi {slug}
```

or for a HoT re-run on a deal that already has an LOI:

```
/legal-assistant sites hot {slug}
```

### Engine action

1. Loads `deal.yaml` from `{Counterparty}_Project_Benelux_Ops/deal.yaml`. If absent, creates a stub and populates `slug`, `hubspot_deal_id` (from SAL-provided context or slug-to-deal lookup), `counterparty_folder_name`.
2. Reads the HubSpot Deal via MCP: pipeline, dealstage, deal_value, contract_capacity_*, type_of_deal, dealtype, owner, associated Companies, associated Contacts.
3. Hydrates `deal.yaml` fields per the HubSpot ↔ deal.yaml field map (see `deal_yaml_schema.md`).
4. Runs the **pre-flight gate**: checks for each of the five prerequisites above. If any fail, returns a blocking report with the specific missing element.
5. Surfaces **DataAcc-1** if zero HubSpot Companies are associated with the Deal — SAL must create + associate at least one Company (Site Partner) before HoT can proceed. For LOI-only intake, engine can proceed but flags the gap.

### SAL decision point

- All prerequisites pass → proceed to Step 2.
- One or more fail → engine returns the list; SAL fixes in HubSpot / Drive / sales-intake, then re-invokes.

---

## Step 2 — Confirm & enrich

### SAL action

Review the engine's hydrated `deal.yaml` preview. The engine presents:

- **Hydrated fields.** What came from HubSpot, with a source tag per field.
- **LOI-stage gaps.** What the LOI template needs but HubSpot doesn't carry: preliminary pricing range, indicative timeline, role assignments per SP, BESS co-development flag, NCNDA existing Y/N.
- **HubSpot conflicts (if any).** Fields where a prior `deal.yaml` value disagrees with the current HubSpot value — engine proposes a resolution per the data-authority chain and asks SAL to confirm/override.

SAL fills the gaps and confirms conflict resolutions in a single batched exchange.

### Engine action

- Writes the resolved fields into `deal.yaml`.
- Logs every HubSpot-write to `drafts/hubspot-sync-log.json`.
- Records any SAL-driven override of the data-authority chain in `deal.yaml.hubspot.conflict_log` with justification.

### SAL decision point

- If a conflict is novel or high-stakes (commercial MW range changed, Heat Offtaker identity swapped) → SAL stops and confirms with Jelmer ten Wolde (deal owner) before proceeding.
- Otherwise → proceed to Step 3.

---

## Step 3 — Generate LOI

### SAL action

Trigger generation:

```
/legal-assistant sites loi generate {slug}
```

### Engine action

1. Loads `deal.yaml`.
2. Runs Recital B drafting per `recital_b_pillars.md` for each Site Partner (engine produces draft; SAL reviews in-skill before commit). TODO(SAL): if Recital B draft is weak, request a rewrite; do not let a placeholder paragraph go to a counterpart.
3. Renders the .docx using the LOI body template (`legal-assistant/sites/loi/loi-template-body-v1.docx`) + Section R (parties) + Section L (locations) + signature page (per Van Gog layout, no KvK in LOI sig block).
4. Runs `site_qa_gate.md` rule catalogue pre-save:
   - Bilingual pair balance (≤ 25% length ratio; calibrated to ≤ 15% after empirical calibration).
   - NL diacritic integrity.
   - Two-column body has no empty cells.
   - Cover title shows primary type only.
   - No salutation on cover.
   - No KvK in LOI sig block.
   - Validity period present (6 months or HoT supersession per Van Gog §5.3 / §6.1.6).
   - Fabrication gate: every numeric claim in Recital B has a source_map URL, parsed-doc ref, or `[TBC]`.
5. Emits:
   - `drafts/YYYYMMDD_DE_LOI_Site_{slug}_v1_(DRAFT).docx`
   - `drafts/YYYYMMDD_DE_LOI_Site_{slug}_v1_qa.txt`
   - Updates `deal.yaml.generated.loi_v1_path`, `.loi_v1_hash`.
6. If QA emits any `fail` without override → generation blocks; engine returns the failing rules with auto-fix hints where available.

### SAL review

1. Read `_qa.txt` top-to-bottom. Any unresolved `fail` → fix input data or request an override with a recorded reason.
2. Open the .docx in Word. Visual sanity check:
   - Cover page — title, parties "Between / And", date, no "NON-BINDING" on cover.
   - Body bilingual pairs — each English paragraph has a corresponding Nederlands paragraph; neither is empty; length ratio looks reasonable.
   - Section R — roles assigned to the correct B.V.s (for multi-SP deals like Van Gog, verify Grid Contributor / Landowner / Heat Offtaker B.V. identity and check that "Same as [role]" cross-refs are correct where a single SP fills multiple roles).
   - Section L — locations table populated; "TBD" and "N/A" only where truly unknown/non-applicable; no placeholder "—" except where the LOI schedule deliberately omits a column.
   - Signature page — DE signatory (Carlos Reuven Mattis Glender, Director), Site Partner signatory names + titles; no KvK on LOI; date line blank.

### SAL decision point

- All clear → LOI is ready. Move to Step 4.
- Needs corrections → update `deal.yaml` or escalate to Phase-4/5 revision per `feedback_planning_self_audit.md` (completeness > compression — do not ship partial content).

---

## Step 4 — Collect documents post-LOI

### SAL action

After LOI is signed (or in parallel, if SAL chooses to advance HoT data collection early), send the appropriate `document_collection_checklist.md` subset to the Site Partner. The subset is determined by the contributions each SP holds:

| SP role(s) | Documents to request |
|---|---|
| Grid Contributor | `kvk_uittreksel`, `ato_document`, `bess_grid_sharing_agreement` (if BESS co-dev) |
| Landowner | `kvk_uittreksel`, `kadaster_uittreksel`, `bestemmingsplan_excerpt`, `landowner_consent` (if different from grower), `financier_consent` (if mortgage) |
| Heat Offtaker | `kvk_uittreksel`, `site_plan` (optional), legacy heat source details (gas contract / CHP cert chain) |
| BESS Co-Developer | `bess_grid_sharing_agreement`, `bess_balancing_market_enrollment` |

The engine maintains the canonical subset logic — SAL can invoke:

```
/legal-assistant sites documents checklist {slug}
```

to emit a role-specific checklist.

### Upload protocol

SAL uploads received documents into `{Counterparty}_Project_Benelux_Ops/documents/` following the filename pattern `{doc_type}_{discriminator}_{YYYYMMDD}.pdf` (see `deal_folder_layout.md § 4.1`) and runs:

```
/legal-assistant sites documents register {slug}
```

The engine:

- Computes SHA-256 per file.
- Adds entries to `documents/_manifest.json` with `uploaded_by`, `uploaded_at`, `validity_expires`.
- Runs the relevant parser (kvk_parser, ato_parser, kadaster_parser, bestemmingsplan_parser) and writes outputs to `deal.yaml.enrichment.*`.
- Logs parser status (`success | partial | failed | manual`).

### SAL decision point

- Parser `success` → proceed.
- Parser `partial` → engine shows the fields it couldn't extract; SAL manually fills.
- Parser `failed` → SAL investigates (wrong doc type? corrupt PDF?); re-upload or mark `manual` and extract by hand.

### Redaction

Before upload, SAL redacts third-party PII per `deal_folder_layout.md § 9.1` and logs redactions in `notes/redaction_log_YYYYMMDD.md`. Redaction happens at SAL's desktop, not in the shared folder.

---

## Step 5 — Generate HoT

### SAL action

```
/legal-assistant sites hot generate {slug}
```

### Engine action

1. Loads `deal.yaml` (with all parsed enrichment from Step 4).
2. Runs **cross-doc gate**: Con (consistency), Gap (completeness), DataAcc (data accuracy) rule classes against registry `escalation_rules` + custom site-specific rules. Key examples:
   - `DataAcc-1`: at least one HubSpot Company associated per Site Partner.
   - `DataAcc-2`: KvK on `site_partners[].kvk` matches parsed `kvk_uittreksel`.
   - `DataAcc-3`: every `documents/*` file has a manifest entry and vice versa.
   - `Con-1`: ATO EAN matches declared DSO by postcode lookup.
   - `Con-2`: `locations[].dso` matches ATO-parsed DSO.
   - `Con-3`: ATO document within validity window (validity_days per registry).
   - `Gap-1`: every required HoT-stage field (registry Phase 1–7) filled or `[TBC]`.
   - `Gap-2`: every Site Partner has at least one contribution + one return.
   - Registry escalation rules per `hot/field-registry.json § escalation_rules`: non-standard heat split, co-investment included, missing landowner consent, joint signing authority.
3. Emits `drafts/cross-doc-gate-report.json` with findings.
4. If gate status = `FAIL`:
   - Engine blocks HoT generation.
   - SAL either (a) fixes inputs and re-runs, or (b) files a `gate_overrides` entry in `deal.yaml` per the format below and re-runs with overrides applied.
5. If gate status = `PASS` / `PASS_WITH_WARN`:
   - Renders the HoT .docx (LOI body carried forward + site-specific schedule per Van Gog §4.2 pattern).
   - Runs `site_qa_gate.md` pre-save (same rule catalogue as LOI + HoT-specific rules: KvK present in HoT sig block; binding-provision language intact; dates normalised).
   - Emits `drafts/YYYYMMDD_DE_HoT_Site_{slug}_v1_(DRAFT).docx` + `_qa.txt`.
   - Updates `deal.yaml.generated.hot_v1_path`, `.hot_v1_hash`, `cross_doc_gate_report_path`.

### `gate_overrides` format

```yaml
gate_overrides:
  - rule: DataAcc-2
    justification: "KvK mismatch between HubSpot Company record and kvk_uittreksel — HubSpot stale by one field (address); KvK doc is authoritative; HubSpot updated in next sync window"
    approver: "Co ten Wolde (SAL)"
    timestamp: "2026-04-19T16:42:00+02:00"
```

Every override must have rule, justification, approver, and timestamp. Unsigned overrides are rejected by the engine.

### SAL review

- Read `_qa.txt` + `cross-doc-gate-report.json` top-to-bottom.
- Open .docx in Word for visual check (same checklist as LOI Step 3, plus HoT sig block with KvK).
- Confirm every `[TBC]` is intentional (not a missed field).

### SAL decision point

- Clear → HoT is ready to share with counterpart. Update HubSpot Deal stage accordingly.
- Not clear → iterate back to Step 4 (missing docs) or Step 2 (data re-entry).

---

## Step 6 — Execution

### SAL action

- Counterpart signs (DocuSign or physical). SAL receives signed PDF.
- SAL moves signed PDF to `signed/` with filename `YYYYMMDD_DE_HoT_Site_{slug}_v1_(SIGNED).pdf`.
- SAL updates `deal.yaml.timeline.hot_signed_date`.
- SAL relays the signed PDF copy to the shared `/Signed HoTs/` Drive folder (per `deal_folder_layout.md § 6.2`).
- SAL updates HubSpot Deal stage to "HoT Signed" (TODO(SAL): confirm stage ID name).
- Engine records the execution in `deal.yaml.generated.hot_v1_signed_copy_path` on next invocation.

### Post-execution

The MSA stream (future Phase C) takes over from HoT execution onward. SAL's primary responsibility closes at HoT signing; handover is to deal owner (Jelmer) + legal (Yoni for amendment tracking, Halyna for notaris/execution admin where `recht van opstal` deeds are pending).

---

## Error recovery — top-5 failure classes

### F1 — Missing KvK on a Site Partner

**Symptom:** `DataAcc-1` or `DataAcc-2` failure; `site_partners[].kvk: "[TBC]"` never resolved.

**Resolution:**
1. SAL asks the Site Partner directly for their KvK number (email, call).
2. SAL asks SP to send a current KvK extract (`kvk_uittreksel`, issued within 90 days).
3. SAL uploads to `documents/`.
4. `kvk_parser` writes extracted KvK to `site_partners[].kvk`; engine re-validates.

If SP refuses or cannot produce, escalate to Jelmer — a deal without verifiable KvK cannot progress to HoT.

### F2 — KvK mismatch between HubSpot and parsed document

**Symptom:** `DataAcc-2` warn/fail.

**Resolution:** Data-authority chain — parsed document wins.
1. Engine updates `site_partners[].kvk` to the parsed value.
2. Engine writes the parsed value back to HubSpot (recorded in `drafts/hubspot-sync-log.json`).
3. Engine logs conflict + resolution in `deal.yaml.hubspot.conflict_log`.

If the parsed KvK is clearly wrong (SAL recognises it as a different SP's KvK), SAL investigates — usually the wrong kvk_uittreksel was uploaded (SAL's mistake) or the SP sent the wrong document.

### F3 — Parcel ID fails PDOK geo-validation

**Symptom:** `enrichment.pdok_parcel_confirmed: false`; SAL-entered `parcel_id` does not resolve in PDOK WFS.

**Resolution:** 99% of the time this is a typo. SAL re-checks the Kadaster extract and re-enters. If the parcel_id on the Kadaster extract itself doesn't resolve, SAL contacts Kadaster — the extract may be stale or the parcel may have been subdivided.

### F4 — ATO document stale

**Symptom:** `Con-3` warn; ATO `validity_expires` has passed or will pass before HoT signing.

**Resolution:** Request a fresh ATO from the Grid Contributor; upload; engine re-parses. If Grid Contributor cannot produce a fresh ATO (e.g., no change has happened but DSO has not reissued), SAL can file a `gate_overrides` entry with justification "no DSO reissuance; ATO remains in force per DSO confirmation email [reference]".

### F5 — Joint signing authority flag

**Symptom:** Registry escalation rule `joint_signing_authority` fires; `site_partners[].signatory.signing_authority: "joint"`.

**Resolution:** Engine flags that two signatures will be required on the execution page. SAL ensures the second signatory (typically a co-director) is (a) identified in `site_partners[].joint_signatories[]`, (b) included in the DocuSign envelope, (c) present on the signature page layout. No gate fail — this is a warning-level flag.

---

## Escalation triggers

Mirrors `hot/field-registry.json § escalation_rules`, mapped to owners:

| Trigger | Escalate to | Reason |
|---|---|---|
| Heat revenue split ≠ 50:50 | Carlos Reuven (commercial director) | Non-standard commercial terms require commercial-director approval |
| Grower co-investment included (F.2 == Include) | Jelmer ten Wolde (deal owner) | Affects SPV structure + financing |
| Grower is not landowner AND no landowner_consent | Carlos Reuven + `legal-counsel` | Land rights unenforceable without third-party consent (Art. 5.5(g)) |
| Joint signing authority | None (SAL handles; flag only) | Operational note, not a blocker |
| KvK cannot be obtained | Jelmer | Blocks HoT progression |
| Recht van opstal term departs from 30 years | Carlos Reuven + Jochem (grid/technical) | Affects DEC economics + amortisation |
| Parcel subdivided post-intake | `legal-counsel` (Yoni amendment tracker) | Requires re-draft of Section L + Kadaster re-issuance |
| SDE++ eligibility change during intake | Jelmer + BJTK (fixed-fee legal review) | Subsidy economics material to go/no-go |

---

## Hard boundary reminders

1. **The engine catches structural, format, registry, and rule failures.** It does not catch "SAL typed the wrong MW number" unless there's a document authority for that field.
2. **`[TBC]` is not a failure mode — it's an honest gap.** Every `[TBC]` in a shipped .docx is a promise to fill before execution. The `site_qa_gate.md` `R-S28` rule warns when total `[TBC]` count exceeds 5 body-wide.
3. **Do not ship without reading `_qa.txt` end-to-end.** The report is not decorative.
4. **Do not merge two Site Partners into one record to simplify Section R.** Multi-B.V. deals (Van Gog pattern) are the norm, not the exception; the schema supports them.
5. **Do not hand-edit generated `.docx` files.** Changes must flow through `deal.yaml` → regenerate. Hand-edits are lost on next regeneration; the QA gate is run against the generator output, not the hand-edit.

---

## End-to-end dry-run template

This section will be completed in Phase E with the Van Gog worked example. For now, placeholder with six enumerated TODOs per step.

### Step 1 — Open intake (Van Gog)

1. TODO(Phase-E): confirm HubSpot Deal ID + pipeline stage as of dry-run date.
2. TODO(Phase-E): document creation of `van Gog kwekerijen Grubbenvorst_Project_Benelux_Ops/` with `deal.yaml` hydrated from HubSpot.
3. TODO(Phase-E): capture which prerequisites passed / failed at open.
4. TODO(Phase-E): document DataAcc-1 surfacing (zero Companies associated).
5. TODO(Phase-E): capture screenshot or YAML snapshot of hydrated state.
6. TODO(Phase-E): record engine runtime for step.

### Step 2 — Confirm & enrich (Van Gog)

1. TODO(Phase-E): list LOI-stage gaps that engine asked SAL to fill (pricing range, timeline, role assignment, BESS flag).
2. TODO(Phase-E): document the three-B.V. role assignment logic (Grid Contributor / Landowner / Heat Offtaker per Van Gog Section R).
3. TODO(Phase-E): record any HubSpot conflicts + resolutions.
4. TODO(Phase-E): capture final `deal.yaml` pre-generation snapshot.
5. TODO(Phase-E): note any overrides + justifications.
6. TODO(Phase-E): track SAL decision timestamps.

### Step 3 — Generate LOI (Van Gog)

1. TODO(Phase-E): invoke `sites loi generate van-gog-grubbenvorst`.
2. TODO(Phase-E): capture QA report verbatim.
3. TODO(Phase-E): compare output .docx against the anchor PDF (April 2026 DocuSign envelope) for parity.
4. TODO(Phase-E): document any Recital B rewrites needed pre-ship.
5. TODO(Phase-E): confirm three signature blocks render correctly (no KvK, role labels correct).
6. TODO(Phase-E): record final .docx hash + filename.

### Step 4 — Collect documents (Van Gog)

1. TODO(Phase-E): emit per-SP checklist subsets.
2. TODO(Phase-E): upload sample `kvk_uittreksel` + `ato_document` + `kadaster_uittreksel` + `bestemmingsplan_excerpt`.
3. TODO(Phase-E): confirm manifest generation.
4. TODO(Phase-E): capture parser outputs written to `deal.yaml.enrichment`.
5. TODO(Phase-E): record parser statuses.
6. TODO(Phase-E): log any redactions applied pre-upload.

### Step 5 — Generate HoT (Van Gog)

1. TODO(Phase-E): invoke `sites hot generate van-gog-grubbenvorst`.
2. TODO(Phase-E): capture `cross-doc-gate-report.json`.
3. TODO(Phase-E): document any gate failures + resolution path (likely DataAcc-1 resolved by creating Companies).
4. TODO(Phase-E): compare HoT output vs anchor PDF HoT equivalent (when available — HoT anchor not yet produced).
5. TODO(Phase-E): confirm KvK appears in HoT sig block but not LOI.
6. TODO(Phase-E): record final .docx hash + filename.

### Step 6 — Execution (Van Gog)

1. TODO(Phase-E): document DocuSign envelope setup.
2. TODO(Phase-E): capture signed PDF filename convention + move to `signed/`.
3. TODO(Phase-E): verify relay to `/Signed HoTs/`.
4. TODO(Phase-E): update HubSpot stage.
5. TODO(Phase-E): log handover to Jelmer + Yoni.
6. TODO(Phase-E): close deal in SAL tracker.

---

## Appendix A — SAL email template pointers

TODO(SAL): the following templates are referenced but not drafted in v1.0:

- `document_request_email_template_{grid_contributor|landowner|heat_offtaker|bess_co_developer}.md` — polite Dutch/English email to counterpart requesting the subset of supporting documents per role.
- `loi_share_email_template.md` — cover note for sending `(DRAFT)` LOI to Site Partner for review.
- `hot_share_email_template.md` — cover note for HoT.
- `redaction_notice_email_template.md` — explains what was redacted and why, when SP receives a document back from DE.

Email style and template patterns live in `executive-comms` skill; SAL should reference those patterns rather than inventing new voice.

---

## Appendix B — Glossary (Dutch terms)

| Dutch | English | Used in |
|---|---|---|
| Aansluit- en Transportovereenkomst (ATO) | Connection & Transport Agreement | Grid interconnection contributions |
| Aansluitcapaciteit | Connection capacity | ATO; registry B.4 |
| Transportcapaciteit | Transport capacity | ATO; registry B.5/B.6 |
| Besloten vennootschap met beperkte aansprakelijkheid (B.V.) | Private limited company | All Dutch Site Partners |
| Bestemmingsplan | Municipal zoning plan | Documents; registry D.4 |
| Erfpacht | Leasehold | Land contribution instrument; registry D.2 |
| Gezamenlijk bevoegd | Jointly authorised | Signing authority; registry A.6 |
| Kamer van Koophandel (KvK) | Chamber of Commerce | Identity validation; registry A.2 |
| Netbeheerder | Distribution System Operator (DSO) | Grid; registry B.1 |
| Recht van opstal | Right of superficies | Primary land instrument; registry D.6 |
| Warmtelevering | Heat supply | Section 3.3 of LOI |
| Zelfstandig bevoegd | Solely authorised | Signing authority; registry A.6 |
