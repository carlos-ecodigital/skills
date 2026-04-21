# How to Request a DE Legal Document

> **Previously `loi-generator`.** Renamed `legal-assistant` on 2026-04-13. If you've been using `/loi-generator`, use `/legal-assistant` or `/loi` instead.

## What is this?

Digital Energy has two streams of pre-contractual documents. `legal-assistant` produces both:

- **Colocation LOIs** — 5 types: End User, Distributor (Mode A/B), Wholesale, Strategic Supplier, Ecosystem Partnership. v3.2 (v1.0 for SS/EP). YAML → branded .docx + pre-save QA report.
- **DE Site HoTs** — grower Heads of Terms (Annex A). v1.0. Conversational 7-phase intake.

You provide the brief. Claude gathers context from your existing systems (HubSpot, ClickUp, website, press, email), asks for gaps in one batched round, drafts Recital B for your review, generates the document, runs a QA linter, and hands off.

**For anything else — M&A LOIs, investment term sheets, counterparty redlines, legal advisory, CIA-CAP (capital introduction) — use `legal-counsel` instead.**

---

## Requesting a Colocation LOI (v3.3 flow)

### Step 1 — Invoke

Either:
- `/loi [CompanyName]` (recommended — slash command, pre-fills name), OR
- Natural language: "Generate an LOI for [Company]", "Draft LOI for [Company]", etc.

### Step 2 — Answer triage questions (one batched round)

Claude asks for:
1. Counterparty short name
2. Website URL
3. HubSpot company record ID (or name to search)
4. ClickUp project / task IDs (if any)
5. Paths to relevant email threads / Fireflies meetings / decks / press
6. Relationship context: who owns it, why now, what triggered the LOI
7. Desired turnaround

**Minimum input floor:** counterparty legal name + **at least one** description source (website, HubSpot, ClickUp, deck, or email thread). Below the floor, Claude won't proceed — it will list what's missing.

**Be honest about what you have.** If no website, say "no website". Claude will not invent data.

### Step 3 — Confirm the type

Claude applies the 5-type decision tree and proposes one:

| Counterparty | Type |
|---|---|
| Buys compute for own use (enterprise, AI lab, startup) | **End User (EU)** |
| Packages DE capacity with their own services (SI, MSP, platform) | **Distributor (DS)** — Mode A or B |
| Buys bulk capacity to resell (neocloud, GPU cloud) | **Wholesale (WS)** |
| Supplies equipment / services / build capability to DE (EPC, modular vendor) | **Strategic Supplier (SS)** |
| Co-positioning / no commercial flow (standards body, university, research consortium) | **Ecosystem Partnership (EP)** |

Green confidence → Claude proceeds. Yellow/red → Claude asks one clarifying question first.

### Step 4 — Let Claude do source capture

Claude fetches your website, HubSpot company + deals + engagement, ClickUp tasks, LinkedIn, recent press (18 months), KVK/Companies House, plus any files you named.

You do nothing in this phase. Wait.

### Step 5 — Answer gap questions (one batched round)

Claude returns a list of facts it sourced, and a list of gaps it needs you to fill. Answer all in one message. Common gaps:
- Exact legal entity form (B.V. / LLC / GmbH / etc.)
- Signatory name and title
- Indicative capacity (MW IT — no DEC Blocks)
- Indicative term (years; "indicative only", no "minimum")
- Recital A variant (default / sovereignty / integration) — Claude suggests one; confirm
- Pricing in LOI? (default: no — deferred to MSA)
- Existing NDA? (default: no — embed NCNDA)
- **For Strategic Supplier**: 1–2 strategic purposes (capacity lock-in, pricing/volume, supply-chain de-risking, engineering integration, pipeline visibility), plus purpose-specific fields (lead-time target, volume, joint IP)
- **For Ecosystem Partnership**: relationship type, collaboration themes, joint activity categories, announcement protocol, logo use

### Step 6 — Review Recital B draft

Claude presents a 3–5 sentence counterparty description (Recital B) with a source map showing which pillar each claim came from. Accept or request specific edits. The 5 pillars: Identity & Scale → Core business → Track record & proof points → Strategic fit → Forward plans (optional).

### Step 7 — Confirm the pre-flight summary

Claude presents a single-screen summary of every value that will go into the document. Confirm or request changes. This is your last chance to catch errors before generation.

### Step 8 — Receive the output

You get:
- `.docx` at `YYYYMMDD_DEG_LOI-{Type}_{Company}_(DRAFT).docx`
- `.docx_qa.txt` QA report (PASS / PASS_WITH_WARN / FAIL with details)

**If QA FAIL**, Claude surfaces the specific rules that tripped and offers auto-fix, override, or manual edit. Do not push through without fixing — the rules exist because previous LOIs had those problems.

### Step 9 — Next-step menu

Claude offers: open in Word / export to PDF / draft DocuSign email via `executive-comms` / log in HubSpot / done.

After signing: rename `_(DRAFT).docx` → `_(SIGNED).pdf`, attach to HubSpot deal, update stage to "LOI Signed".

---

## What Claude will NOT do

- Invent data. If a fact isn't sourced, Claude either asks or flags `[TO BE CONFIRMED]`.
- Negotiate or redline. If the counterparty returns redlines, stop and invoke `legal-counsel`.
- Send anything. Human reviews and sends.
- Modify the Site HoT body. Body is locked at v1.0.
- Produce MSAs, Sales Order Forms, SLAs, post-LOI documents. Separate workstreams.
- Put value-prop language in the closing. Closing is hardcoded "We look forward to working with you." If you need value-prop / near-signature content, ask for a companion cover letter via `executive-comms`.

---

## Requesting a DE Site HoT (Site Sourcing)

### Step 1 — Start the intake

> "Start a DE Site HoT intake for [Grower]. They're a [crop] grower in [location], currently [size] ha, [expansion plans]."

### Step 2 — Answer the 7-phase intake

Claude walks through 7 conversational phases covering 48 Annex A fields. Each phase is a small batch, not a giant form.

1. **Identification** — legal name, KVK, address, project name. Bring: KVK uittreksel.
2. **Signatory & Greenhouse** — signer + authority (solo vs joint), greenhouse location, size, crops.
3. **Electrical Connection** — DSO, EAN, ATO ref, three-tier capacities. Bring: ATO document.
4. **Heat Supply** — outlet / return temps, price per MWh, EB calculation.
5. **Land & Property** — Kadaster refs, title type, encumbrances, opstalrecht term. Bring: Kadaster uittreksel, bestemmingsplan. If grower ≠ landowner or land is mortgaged, additional parties + consent letters.
6. **Commercial Terms** — heat split (standard 50:50), payment term, effective date.
7. **Optional Provisions + Notices** — CHP lease, co-investment, contact emails.

Escalations are automatic (non-standard heat split → Carlos; co-investment → Jelmer; grower ≠ landowner with no consent → Carlos + legal-counsel).

### Step 3 — Confirm the summary

Claude presents a full summary table before generating. Check everything. Ask for changes.

### Step 4 — Review the output

Claude writes to the SSOT at `contracts/hots/active/{grower-slug}/`:
- `annex-a-data.json` — structured field data
- `DE-Site-HoT_Annex_A_{Company}.docx` — populated Annex A (LIVE; 3-pass XML form-fill via `sites/hot/generate_site_hot.py` v0.1)
- `DE-Site-HoT_Body_{Company}.docx` — locked bilingual body copy (LIVE; `shutil.copy2` + SHA-256 verification)
- `intake-log.md` — Q&A transcript
- `status.md` — draft status + escalations + missing docs + next step

Carlos (or legal-counsel for legal questions) reviews before sending to the grower.

### Current caveat

Site HoT engine is LIVE at v0.1 (commit `2298ba1`). Single-partner fill path is the primary supported case — multi-partner Annex A fan-out is queued for Wave 2 and emits a `WARN: multi-partner HoT…` on stderr when detected. Registry enum normalisation layer (bare tokens "Eigendom"/"Sole" → slash-combined bilingual "Full ownership / Vol eigendom" / "Sole / Zelfstandig bevoegd") is also queued — raw tokens surface through to QA today. See `sites/_shared/sal_runbook.md` for the full self-serve runbook.

---

## Questions?

Ask Carlos or Jelmer. Full technical documentation in the `legal-assistant` skill directory (`SKILL.md`, `ASSEMBLY_GUIDE.md`, `FEATURE_MATRIX.md`, `CHANGELOG.md`, `_shared/loi-recital-a-library.md`, `_shared/counterpart-description-framework.md`, `_shared/loi-qa-gate.md`).

## Naming conventions (preserved)

| Document | Pattern |
|---|---|
| LOI (draft) | `YYYYMMDD_DEG_LOI-{Type}_{Company}_(DRAFT).docx` |
| LOI (signed) | `YYYYMMDD_DEG_LOI-{Type}_{Company}_(SIGNED).pdf` |
| Site HoT Annex A | `DE-Site-HoT_Annex_A_{Company}.docx` |
| Site HoT Body | `DE-Site-HoT_Body_{Company}.docx` |

Status values: `DRAFT` → `SENT` → `SIGNED` → `LAPSED` → `SUPERSEDED`.
