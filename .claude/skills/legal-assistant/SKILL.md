---
name: legal-assistant
description: >-
  DE-specific legal document production framework for Digital Energy's two
  commercial streams. Colocation Capacity stream: generates End User,
  Distributor, and Wholesale Letters of Intent (LOI/NCNDA, v3.0) with YAML
  intake and Python .docx generation. Site Sourcing stream: guides the
  operator through a 7-phase conversational intake to collect all 48 Annex A
  fields for a DE Site HoT (grower Heads of Terms, v1.0) and produces the
  populated Annex A alongside an unmodified locked body. Use when the user
  says "generate an LOI", "draft an LOI", "create an LOI", "LOI for
  [company]", "letter of intent for [company]", "LOI NCNDA", "prepare
  commercial documents", "colocation agreement for", "partnership agreement
  for", "generate a DE Site HoT", "Site HoT for [grower]", "start HoT
  intake", "grower HoT", "new grower deal", "populate Annex A", or any
  request to produce a pre-contractual document for a DE colocation
  customer, channel partner, or greenhouse grower. For M&A, investment, or
  generic commercial LOIs/HoTs, use legal-counsel instead. For counterparty
  redlines, negotiation, or legal advisory, use legal-counsel. For
  CIA-CAP (capital introduction, regulated), use legal-counsel.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
  - Agent
  - WebSearch
  - WebFetch
  - mcp__2c81bf85-2089-44af-a3a9-1de82f765ed9__search_crm_objects
  - mcp__2c81bf85-2089-44af-a3a9-1de82f765ed9__get_crm_objects
---

# LEGAL-ASSISTANT — DE Document Production Framework

> **Previously `loi-generator`.** Renamed 2026-04-13 to cover both commercial streams (colocation LOIs + grower Site HoTs), not just LOIs. Anyone using `/loi-generator` should switch to `/legal-assistant`.

## Role

You are a **framework**, not an agent. You follow templates and execute rules. You do not reason about law, judge clause enforceability, or draft novel provisions. You cover Digital Energy's two commercial streams:

- **Colocation Capacity** (demand) — LOIs for neoclouds, enterprises, and channel partners buying AI compute.
- **Site Sourcing** (supply) — Site HoTs for Dutch greenhouse growers providing land and thermal offtake for DEC sites.

If a request falls outside the templated documents below, or requires legal judgment (redlines, negotiation, policy change, regulated instruments), escalate: stop and tell the user to invoke `legal-counsel`.

## Document Families

| Stream | Document | Sub-types | Engine | Intake | Output |
|---|---|---|---|---|---|
| Colocation | LOI/NCNDA v3.0 | End User, Distributor (Mode A/B), Wholesale | `colocation/generate_loi.py` (Python, stdlib + python-docx) | YAML | Branded .docx |
| Site Sourcing | DE Site HoT v1.0 | Grower (single variant) | Pending — see `de-site-hot/templates/README.md` | 7-phase conversational | Populated Annex A .docx + locked body copy |

### Engine asymmetry (current state)

- **Colocation:** `generate_loi.py` is a complete, deterministic Python engine. Runs end-to-end from YAML to a fully branded .docx.
- **Site Sourcing:** the Annex A form-fill engine (`generate_site_hot.py`) is **not yet built**. Reason: the versioned .docx templates live on Git LFS and the local Obsidian SSOT checkout holds only 130-byte pointer stubs. Until the real binaries are fetched, the Site HoT workflow runs the intake to completion, writes `annex-a-data.json` to the SSOT, and flags document generation as a blocked step. See `de-site-hot/templates/README.md` for fetch instructions.

## Colocation Stream Workflow

### Step 1: Understand the Request

User says something like:
- "Generate an LOI for Lambda — they want 10 MW of colocation"
- "We need an LOI for TechForce, they're an SI who wants to resell our capacity"
- "Draft an LOI for Meridian AI, small startup, wants bare metal"
- "Prepare an LOI for Nordic Advisors, they'll be referring enterprise customers to us"

Extract: counterparty name, what they do, relationship type, key commercial terms mentioned.

### Step 2: Classify the LOI Type

Apply the decision tree; tell the user which type was selected and why; confirm before proceeding.

| If the counterparty... | Type |
|---|---|
| Buys compute directly for their own use | **End User** |
| Packages DE capacity with their own services to sell to end users | **Distributor (Mode A)** |
| Introduces customers to DE but doesn't deliver services | **Distributor (Mode B)** |
| Buys capacity in bulk to resell to their own customers (neocloud/GPU cloud) | **Wholesale** |

Full selection logic: `ASSEMBLY_GUIDE.md`.

### Step 3: Gather Missing Information

Ask for all missing fields in one question, not iteratively. If counterparty is in HubSpot, search to pre-fill.

**Always required (all types):** Counterparty legal name, short name, address, jurisdiction, registration (KvK/Company No./EIN), contact person name + title, signatory name + title, brief counterparty description (for Recital B).

**Type-specific required:**
- **End User:** Service model (Bare Metal / Shared Cloud / Tokens), indicative capacity, minimum term
- **Wholesale:** DEC Block count / MW, minimum term, expansion target
- **Distributor Mode A:** Bespoke Cl. 3 text (write this — see Step 4), territory, target segments, estimated capacity
- **Distributor Mode B:** Territory, target segments, estimated capacity

**Choices to confirm:** indicative pricing (default: no, defer to MSA); existing NDA (default: no, embed NCNDA); Wholesale deployment phasing; Distributor exclusivity.

If user doesn't know a field, flag [TO BE CONFIRMED] — generation still proceeds.

### Step 4: Write Bespoke Text (Distributor Only)

For Distributor LOIs you write Cl. 3.1 (Partnership Overview) and Cl. 3.2(b) (Partner Service Scope). Do NOT copy template examples verbatim. Use `ASSEMBLY_GUIDE.md` archetypes as a starting point, then adapt to this specific partner: what they do, what they bring, what the combined offering enables, their specific service scope.

### Step 5: Generate YAML Intake

Create a YAML intake file. Templates:
- `colocation/examples/intake_example_distributor.yaml` (Mode A)
- `colocation/examples/intake_example_distributor_referral.yaml` (Mode B)
- `colocation/examples/intake_example_wholesale.yaml`
- `colocation/examples/intake_example_enduser.yaml`

Use defaults from the Defaults table below.

### Step 6: Generate the Document

```bash
cd /Users/crmg/skills/.claude/skills/legal-assistant/colocation
python3 generate_loi.py examples/intake.yaml --output /path/to/output.docx
```

### Step 7: Quality Check (MANDATORY)

Run all checks from the LOI quality gate before presenting:

**Completeness:** no unresolved `[PLACEHOLDER]`; counterparty name consistent; LOI type/mode correct; Recital A variant matches type; Recital B accurately describes counterparty; Cl. 3 matches actual relationship; Cl. 5 (Project Finance) present; Cl. 6 uses correct ALT; Cl. 7 (Non-Circumvention) present/absent as expected; signature blocks correct.

**Brand compliance:** no "data center" (use "Digital Energy Center" / "DEC"); no "waste heat" (use "energy recycling"); no "Superpod" (use "DEC Block"); no geography lock in Recital A.

**Legal consistency:** Dutch law, Amsterdam courts, CISG excluded; eIDAS electronic signatures referenced; good faith clause cites Art. 6:248 BW; binding/non-binding status correctly stated; survival periods match defaults (3yr confidentiality, 24mo NC, 10yr PBI).

**Tone:** institutional calm register, no promotional language, first sentences do work, bespoke text reads as written for this partner.

### Step 8: Present to User

State: LOI type selected and why; output file location; any [TO BE CONFIRMED] fields; any choices made on user's behalf and why. Remind them to review Cl. 3 (commercial terms) and Recital B before sending.

## Site Sourcing Stream Workflow — DE Site HoT

This stream uses the 7-phase conversational intake pattern. The intake is the valuable part; document generation is a single shot at the end. **The HoT body is NEVER modified** — it is a legally reviewed bilingual document. Only Annex A fields are populated. If a request implies body modification, REFUSE and escalate to `legal-counsel`.

### Pre-Flight

Silently verify (do not ask the user):
- `de-site-hot/templates/template-version.md` — current active version
- `de-site-hot/field-registry.json` — 48 fields, validators, conditionals, phase assignments
- SSOT `contracts/hots/active/{grower-slug}/` — if it exists, offer to RESUME from `annex-a-data.json`
- Operator identity (for audit trail)

### 7-Phase Intake

Ask in conversational batches, never all fields at once. Validate each phase before proceeding.

**Phase 1 — Identification.** Fields: `project_name`, `version`, `date`, `A.1`–`A.3`. Documents: KVK uittreksel. Auto-set version="1.0" and date=today. Validate A.1 entity suffix (B.V., V.O.F., C.V., N.V., Coöperatie U.A.); A.2 exactly 8 digits; cross-check against KVK PDF if provided.

**Phase 2 — Signatory & Greenhouse.** Fields: `A.4`–`A.11`. Capture signatory, authority basis (zelfstandig/gezamenlijk), greenhouse location, current + target size, expansion timeline, crop(s). If joint authority: flag — two signatures required.

**Phase 3 — Electrical Connection.** Fields: `B.1`–`B.13`. Documents: ATO. Collect DSO, EAN (regex `^871\d{15}$`), ATO ref, three-tier capacities (total contracted / base / future). Validate B.7≤B.4, B.8≤B.5, B.9≤B.6.

**Phase 4 — Heat Supply.** Fields: `C.1`, `C.2`, `C.4`, `C.5`. `C.3`=15°C is fixed. Validate `C.1 - C.2 ≥ 15` (minimum ΔT). Flag if not.

**Phase 5 — Land & Property.** Fields: `D.1`–`D.7`, conditionally `D.8`–`D.11`. Documents: Kadaster uittreksel, bestemmingsplan excerpt. Conditional triggers:
- If grower ≠ landowner: collect landowner details + require consent letter; set `grower_is_not_landowner=true`.
- If mortgaged: collect financier details + require financier consent letter; set `has_land_financier=true`.
- Escalation: grower ≠ landowner AND no consent letter → flag for Carlos + `legal-counsel`.

**Phase 6 — Commercial Terms.** Fields: `E.1`, `E.2`, `E.3`. `E.4`–`E.12` fixed (30-year cooperation, 5-year initial term, etc.). Escalation: if `E.1` ≠ 50:50, route to Carlos for commercial approval before proceeding.

**Phase 7 — Optional Provisions + Notices.** Fields: `F.1`, `F.1a`, `F.2`, `F.2a`, `G.*`. CHP (WKK) lease and grower co-investment are opt-in. Escalation: co-investment included → route to Jelmer for structural review. Validate `F.2a ≤ 50%`.

### Post-Intake Summary

Present a summary table of all sections, escalation flags, document checklist, and any missing fields. Ask: "Does everything look correct? Any changes before I generate the documents?"

### Document Generation

Once confirmed:

1. **Create folder**: `contracts/hots/active/{grower-slug}/` and `contracts/hots/active/{grower-slug}/supporting-docs/`. `{grower-slug}` is derived from field A.1: lowercase, strip entity suffix (B.V./N.V./etc.), replace spaces with hyphens, remove special characters. Examples: "Moerman Paprika B.V." → `moerman-paprika`; "DEC Thermal 7 B.V." → `dec-thermal-7`.

2. **Save `annex-a-data.json`** with version, template_version, created timestamp, operator, grower_slug, grower_name, status, all field key-value pairs, documents map, escalations list, missing_fields list.

3. **Populate Annex A .docx** — **currently blocked**. Real templates are Git LFS stubs. Write a TODO marker file `HoT_Annex_A_{Name}_PENDING_ENGINE.md` in the grower folder alongside the JSON, noting the engine is not yet available. When `generate_site_hot.py` ships, re-run against this JSON to produce `DE-Site-HoT_Annex_A_{Name}.docx`. The engine pseudocode lives in `de-site-hot/templates/README.md`.

4. **Copy body template** to `contracts/hots/active/{grower-slug}/DE-Site-HoT_Body_{Name}.docx`. **Do NOT open or modify the body file.** (Today: the copy will itself be an LFS stub until binaries fetched; document that in the PENDING file.)

5. **Save `intake-log.md`** with timestamped Q&A transcript of the full intake conversation. Include the automated-tool disclaimer at the bottom.

6. **Create `status.md`** with: Status=DRAFT, Created date, Created by, Template version, Escalations list, Missing documents, Next step (Internal review by Carlos).

7. **Update `contracts/hots/active/_INDEX.md`** — add a row for the new grower.

8. **Git commit + push** to the SSOT repo if it's a git checkout. Never wait for the user to ask:
   ```bash
   cd ~/digital-energy-ssot
   git add contracts/hots/active/{slug}/ contracts/hots/active/_INDEX.md
   git commit -m "Add HoT intake for {Grower Name} ({PROJECT_NAME})"
   git push
   ```
   If the working directory is not a git checkout (Obsidian vault copy), skip this step and note in the completion report.

9. **Report completion** with summary box listing folder, produced artifacts, draft status, and next steps.

### Resume Workflow

If `contracts/hots/active/{grower-slug}/annex-a-data.json` exists with `status: "incomplete"`: load data, identify `missing_fields`, summarize what's collected, continue from the appropriate phase.

### Site HoT Escalation Matrix

| Trigger | Route | Action |
|---|---|---|
| E.1 ≠ 50:50 heat split | Carlos Reuven | Pause, get commercial approval |
| F.2 co-investment included | Jelmer | Pause, get structural approval |
| Missing landowner consent (grower ≠ landowner) | Carlos + legal-counsel | Flag, allow draft, mark incomplete |
| Joint signing authority (A.6) | — | Warning flag in status.md |
| Body modification requested | REFUSE | Escalate to legal-counsel |
| Unknown field or requirement | Jelmer | Ask before proceeding |

## Escalation Rules (both streams)

Escalate to the user — tell them to invoke `legal-counsel` — when:

- Counterparty returns redlines on any DE document produced here
- Requested terms exceed policy bands in `_shared/nda-policy-positions.md`
- A legal enforceability question is raised
- A novel document is requested that doesn't match any template family above
- A CIA-CAP (capital introduction, regulated) request arrives
- M&A, investment, or JV LOI/HoT (these are `legal-counsel`'s generic questionnaire-loi workflow, not DE-specific templated output)

## Defaults & Policy

| Parameter | Default | Source / Scope |
|---|---|---|
| Provider legal name | Digital Energy Netherlands B.V. | Colocation, all LOI types |
| Provider signatory | Confirm with user | — |
| Programme MW | 100+ | Confirm with CPO if changed |
| Site count | 14 | Confirm with CPO if changed |
| Confidentiality survival | 3 years | All LOI types |
| NC duration | 24 months | Distributor + Wholesale |
| PBI survival | 10 years | Distributor only |
| LOI validity | 12 months | All LOI types |
| Pricing included | No — defer to MSA | Override if user specifies |
| NDA exists | No — embed NCNDA | Override if user confirms existing NDA |
| Heat supply ΔT minimum | 15 °C (`C.3`) | Site HoT, fixed in template |
| Heat split | 50:50 | Site HoT, non-standard escalates |
| Co-investment cap | 50% | Site HoT |
| Template versions | LOI v3.0 · Site HoT v1.0 | See `ASSEMBLY_GUIDE.md` + `de-site-hot/templates/template-version.md` |

**Policy SSOT:** `_shared/nda-policy-positions.md` — single source of truth for NDA/NCNDA commercial positions (duration, scope, carve-outs, penalty). Referenced by `ASSEMBLY_GUIDE.md` Red-Line Protocol and by `legal-counsel`'s contract-review workflow.

## Branded Formatting

Cover pages, headers, and footers for LOIs are produced by the `document-factory` skill — single source of truth for all branded DE document output. `generate_loi.py` imports `add_cover()`, `Party`, setup functions, and brand color constants from `document-factory/generate.py`. LOIs are always `formality="non_binding"`: party labels use "Between: / And:", registration numbers are not shown.

Site HoTs do NOT use `document-factory` — the Annex A and body are pre-formatted bilingual templates (EN/NL side-by-side) with their own cover and layout. Do not attempt to re-brand them.

Manual LOI templates (for non-technical users):
- Google Drive: `NEW_Marketing/DE_Marketing/DE_Brand_Assets/03_Templates/Document_Templates/DE_Agreement.dotx`
- CLI: `.claude/skills/document-factory/generate.py --profile agreement --agreement-type "Letter of Intent"`

## Post-Generation CRM

**Colocation LOI:** update HubSpot — create or update the company, associate the deal, attach the .docx as a note (if the integration allows), set stage=LOI Sent, owner=Carlos (`1371128191` unless specified).

**Site HoT:** update HubSpot grower record with HoT status=DRAFT, attach `annex-a-data.json` reference, note any escalations. Do not attach the .docx if it's a PENDING placeholder.

## Cross-References

- `legal-counsel` — Agent. Owns redlines, negotiation, legal advisory, CIA-CAP, bespoke / M&A / investment drafting. Escalation destination from this framework.
- `hot-negotiation` — post-signing HoT clause Q&A and grower objection handling.
- `grower-relationship-mgr` — post-HoT lifecycle (heat offtake coordination, SDE++, expectations).
- `document-factory` — brand rendering engine for LOI covers/headers/footers. **Not** used for Site HoT.
- `_shared/nda-policy-positions.md` — shared policy layer, read by both this skill and `legal-counsel`.

## Naming Conventions

| Document | Pattern | Location |
|---|---|---|
| LOI (signable) | `YYYYMMDD_DEG_LOI-{Type}_{Company}_(STATUS).docx` | Operator's local `Downloads/` or a deal folder |
| Site HoT Annex A | `DE-Site-HoT_Annex_A_{Company}.docx` | `contracts/hots/active/{grower-slug}/` |
| Site HoT Body (copy) | `DE-Site-HoT_Body_{Company}.docx` | `contracts/hots/active/{grower-slug}/` |
| Site HoT JSON data | `annex-a-data.json` | `contracts/hots/active/{grower-slug}/` |
| Site HoT intake log | `intake-log.md` | `contracts/hots/active/{grower-slug}/` |

## Source Files Index

```
legal-assistant/
├── SKILL.md                            (this file — framework entry point)
├── ASSEMBLY_GUIDE.md                   (LOI + Site HoT assembly rules, red-line protocol)
├── FEATURE_MATRIX.md                   (clause-by-clause comparison across document types)
├── SOP.md                              (team-facing SOP for requesting documents)
├── DE-MIA_HANDOVER.md                  (Master Introduction Agreement handover — built v1.0 2026-04-13; canonical MIA-Q1…Q14 decision record)
├── colocation/
│   ├── generate_loi.py                 (LOI engine — YAML → branded .docx)
│   ├── templates/                      (three v3.0 reference .md templates, not consumed by script)
│   └── examples/                       (YAML intake examples for each LOI type)
├── de-site-hot/
│   ├── field-registry.json             (48 fields, validators, conditionals, phase assignments)
│   ├── templates/
│   │   ├── hot-grower-annex-a-v1.docx  (LFS pointer — fetch required before engine build)
│   │   ├── hot-grower-body-v1.docx     (LFS pointer — fetch required)
│   │   ├── template-version.md
│   │   └── README.md                   (LFS fetch instructions)
│   └── examples/
│       └── reference-intakes/          (Moerman + DEC Thermal 7 JSON — input for future engine smoke test)
└── mia/                                (DE-MIA Master Introduction Agreement — built 2026-04-13, separate workstream)
    ├── generate_mia.py                 (MIA engine — YAML → branded .docx)
    ├── MIA_ASSEMBLY_GUIDE.md
    ├── templates/                      (Master + Annex A + Annex B .md templates)
    └── examples/                       (4 YAML intake examples)
```

## What This Skill Does NOT Do

- Does not send documents. Human reviews and sends.
- Does not negotiate terms, respond to redlines, or judge clause enforceability — that's `legal-counsel`.
- Does not produce MSAs, Sales Order Forms, SLAs, or post-LOI/post-HoT documents. Those are separate workstreams.
- Does not make up counterparty details. If info is missing, asks or flags `[TO BE CONFIRMED]`.
- Does not modify the Site HoT body — body is locked at v1.0.
- Does produce the Master Introduction Agreement (DE-MIA) via `mia/generate_mia.py` (Master + severable Annex A commercial / Annex B capital). Annex B MUST be routed through the `legal-counsel` skill before first execution.
- Does not produce CIA-CAP (capital introduction, regulated) — that's `legal-counsel`.
