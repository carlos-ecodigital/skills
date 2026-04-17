# How to Request a DE Legal Document

> **Previously `loi-generator`.** The skill was renamed `legal-assistant` on 2026-04-13 because it now covers both commercial streams (colocation LOIs + grower Site HoTs), not just LOIs. If you've been using `/loi-generator`, use `/legal-assistant` instead.

## What is this?

Digital Energy has two streams of pre-contractual documents. `legal-assistant` produces both:

- **Colocation LOIs** — End User, Distributor (Mode A/B), Wholesale. v3.0. YAML → branded .docx.
- **DE Site HoTs** — grower Heads of Terms (Annex A). v1.0. Conversational 7-phase intake → populated Annex A + locked body copy.

You provide the brief. Claude gathers missing info, generates the document, runs a quality check, and outputs files for your review.

**For anything else — M&A LOIs, investment term sheets, counterparty redlines, legal advisory, CIA-CAP (capital introduction) — use `legal-counsel` instead.**

## Requesting an LOI (Colocation)

### Step 1: Tell Claude what you need

> "Generate an LOI for [Company]. They are [what they do]. They want [what they want from DE]."

Examples:
- "Generate an LOI for Lambda. GPU cloud provider, 10 MW of colocation capacity."
- "Generate an LOI for TechForce Solutions. SI wanting to integrate their managed services with our DEC platform."
- "Generate an LOI for Meridian AI. Small startup, bare metal colocation for training."
- "Generate an LOI for Nordic Advisors. They'll refer enterprise customers — referral arrangement."

More detail = better output. Include capacity, territory, timeline, pricing if known.

### Step 2: Answer Claude's questions

Claude asks for missing info in one batch, not iteratively: counterparty details (legal name, address, registration), contact person and signatory, commercial specifics. If you don't know, say so — Claude flags as `[TO BE CONFIRMED]` and still generates.

### Step 3: Review the output

Claude produces a .docx. **Review before sending.** Check:
1. **Recital B** — counterparty description sounds right?
2. **Clause 3** — commercial terms match what was discussed?
3. **Signature block** — correct names and titles?
4. **`[TO BE CONFIRMED]` fields** — fill before sending.

### Step 4: Send

- Export to PDF if needed.
- DocuSign or email for wet signature.
- After signing, rename: `YYYYMMDD_DEG_LOI-{Type}_{Company}_(SIGNED).pdf`.
- Attach to HubSpot deal.

### Which LOI type?

| If the counterparty... | Type |
|---|---|
| Buys compute for their own use (enterprise, AI lab, startup) | **End User** |
| Packages DE capacity with their services to sell to others (SI, MSP, platform) | **Distributor** |
| Just introduces customers, doesn't deliver services | **Distributor (Referral / Mode B)** |
| Buys bulk capacity to resell (neocloud, GPU cloud) | **Wholesale** |

You don't specify the type — Claude figures it out from your description and confirms with you before generating.

## Requesting a DE Site HoT (Site Sourcing)

### Step 1: Start the intake

> "Start a DE Site HoT intake for [Grower]. They're a [crop] grower in [location], currently [size] ha, [expansion plans]."

Examples:
- "Start a DE Site HoT for Moerman Paprika B.V. Paprika grower in Westland, 6 ha, looking to expand to 10 ha."
- "Generate a Site HoT for Kwekerij Van Dijk. Tomato grower, De Lier, 8 ha."

### Step 2: Answer the 7-phase intake

Claude walks through 7 conversational phases covering 48 Annex A fields. Each phase is a small batch of questions, not a giant form:

1. **Identification** — legal name, KVK, address, project name. Bring: KVK uittreksel.
2. **Signatory & Greenhouse** — signer + authority (solo vs joint), greenhouse location, size, crops.
3. **Electrical Connection** — DSO, EAN, ATO ref, three-tier capacities. Bring: ATO document.
4. **Heat Supply** — outlet / return temps, price per MWh, EB calculation.
5. **Land & Property** — Kadaster refs, title type, encumbrances, opstalrecht term. Bring: Kadaster uittreksel, bestemmingsplan. If grower isn't landowner or land is mortgaged, additional parties + consent letters.
6. **Commercial Terms** — heat split (standard 50:50), payment term, effective date.
7. **Optional Provisions + Notices** — CHP lease, co-investment, contact emails.

Some conditions escalate automatically (non-standard heat split → Carlos; co-investment → Jelmer; grower ≠ landowner with no consent → Carlos + legal-counsel).

### Step 3: Confirm the summary

Claude presents a full summary table before generating. Check everything. Ask for changes before generation.

### Step 4: Review the output

Claude writes everything to the SSOT at `contracts/hots/active/{grower-slug}/`:
- `annex-a-data.json` — all the structured field data
- `DE-Site-HoT_Annex_A_{Company}.docx` — populated Annex A (NOTE: currently pending — see caveat below)
- `DE-Site-HoT_Body_{Company}.docx` — the locked bilingual body, copied unmodified
- `intake-log.md` — the full Q&A transcript
- `status.md` — draft status + escalations + missing docs + next step

Carlos (or legal-counsel for legal questions) reviews before sending to the grower.

### Current caveat (2026-04-13)

The Site HoT `.docx` form-fill engine is pending a Git LFS fetch of the template binaries. Until it ships, the intake runs to completion and writes `annex-a-data.json`, but the Annex A docx step writes a placeholder marker file instead of a populated document. This is flagged in the completion report. Body copy is also pending an LFS fetch. See `de-site-hot/templates/README.md` for fetch instructions.

## Questions?

Ask Carlos or Jelmer. Full technical documentation in the `legal-assistant` skill directory (`ASSEMBLY_GUIDE.md`, `FEATURE_MATRIX.md`, `field-registry.json`).
