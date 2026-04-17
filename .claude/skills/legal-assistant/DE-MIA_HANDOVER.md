# DE-MIA — Master Introduction Agreement: Handover

**Status:** Built v1.0. All templates, YAML examples, assembly guide, and generation script produced.
**Owner:** Carlos (Digital Energy)
**Related:** LOI/NCNDA v3.0 system (`legal-assistant` skill, `colocation/` sub-module). MIA is the companion fee instrument referenced in DS Mode B (Cl. 3.4) and contemplated in DS Cl. 6 broadened scope.
**Last updated:** 2026-04-13 (v2.1 — all open questions answered; see Revision log)

---

## Why this exists

DE has three distinct fee instruments collapsing into one master document with two severable annexes. This avoids a proliferation of overlapping agreements and keeps regulated activity (capital introductions) cleanly walled off from unregulated activity (commercial referrals).

- **Commercial introduction** (someone introduces a paying *customer*) — unregulated.
- **Capital introduction** (someone introduces an *investor*) — touches AFM/FCA/SEC perimeter.
- Same act ("an introduction"), fundamentally different regulatory regime depending on what is introduced.

The MIA structure isolates the regulated piece in Annex B with its own automatic suspension and severability, so a regulatory change to Annex B cannot contaminate the Master or Annex A.

---

## Architecture

```
DE-MIA-v1.0 (Master Introduction Agreement)
  Master Framework — always present
    - Parties and relationship
    - Confidentiality (standalone — works with or without LOI)
    - Non-circumvention (for introduced contacts)
    - Term, termination, survival
    - Governing law (Dutch), Amsterdam courts, CISG excluded
    - Severability — each annex independently severable

  Annex A: Commercial Introductions — activated if applicable
    - Qualifying introduction criteria
    - Fee schedule: residual % MRR (tiered) OR one-time flat
    - Payment terms, pipeline exclusion list
    - Duration / tail period

  Annex B: Capital Introductions — activated if applicable
    - Named investor list (pre-approved by DE)
    - Fee schedule: flat fee per intro OR capped %
    - Strict activity limitations (introduction only)
    - Regulatory representations and warranties
    - Automatic suspension on regulatory change
    - Enhanced severability
```

A partner can sign Master + A only, Master + B only, or Master + both (rare — different skill sets).

---

## Annex A — Commercial Introductions (as built — dual fee election per MIA-Q11)

Introducer elects per Qualifying Introduction: Capitalised one-time (default, operationally simpler) **or** Tiered residual % MRR.

| Introduced capacity | Tiered residual (Option 1) | Capitalised one-time (Option 2, default) |
|---|---|---|
| < 5 MW IT committed | 8–10% of MRR | 3 months MRR equivalent |
| 5–20 MW IT | 6–8% of MRR | 2 months MRR equivalent |
| > 20 MW IT | 4–6% of MRR | 1.5 months MRR equivalent |

*Fee numbers are illustrative plan defaults, not validated against DE's past offers or market rates (see MIA-P2).*

**Qualifying trigger:** Written introduction accepted by DE + Customer signs MSA + first invoice paid.
**Tail:** 12 months after agreement termination (harmonised with Annex B per MIA-Q13).
**Pipeline exclusion:** Defensive carve-out clause — fee void if Provider can demonstrate direct relationship or prior 12-month contact (per MIA-Q12). No upfront list.

---

## Annex B — Capital Introductions (regulatory safeguards)

To keep the arrangement **outside** the regulated perimeter (AFM / FCA / SEC / FINMA), Annex B must include all six of the below. None are optional.

### 1. Strict activity limitations — what the Introducer MAY do
- Provide DE's contact information to a potential investor
- Arrange an initial meeting between DE and the potential investor
- Share publicly available information about DE
- Confirm factual, non-evaluative information about DE on request

### 2. Prohibited activities — what the Introducer MAY NOT do
- Provide investment advice or recommendations
- Solicit, promote, or market the investment opportunity
- Negotiate investment terms on behalf of either party
- Distribute offering materials, financial models, or non-public information
- Hold, receive, or transmit funds or securities
- Make representations about expected returns or risk profiles
- Act as agent or representative of DE in any investment discussions

### 3. Regulatory representations (both parties)
- Introducer represents it is **not** a regulated investment firm, broker-dealer, placement agent, or financial intermediary, and holds no licence implying such status
- Introducer represents its activities under Annex B are limited to effecting introductions and do not constitute investment services under MiFID II, the Wft, the FCA Handbook, or the US Securities Exchange Act
- DE represents it has not engaged the Introducer as a placement agent or financial advisor
- Both parties acknowledge the arrangement is structured to fall outside the regulatory perimeter and agree to restructure or suspend Annex B if regulatory circumstances change

### 4. Fee structure — three options (lowest to highest regulatory risk)

| Option | Structure | Risk profile |
|---|---|---|
| **1** | Flat fee per qualifying introduction (e.g. EUR 25,000–100,000), **not** linked to amount invested | Lowest. Eliminates "transaction-based compensation" trigger. |
| **2 (selected — see MIA-Q9)** | Capped % of capital committed (2% up to EUR 250,000 max per intro) | Moderate. Cap demonstrates fee is not purely transaction-based. Activity limitations and reps must be strongest tier. |
| **3** | Tiered % (3% / 2% / 1%) | Highest. Industry standard but closest to broker-dealer compensation. Requires CEO + counsel sign-off per deal. |

Default position: **Option 2 (capped %).** 2% of capital committed, EUR 250,000 cap per introduction. Activity limitations (sec. 1–3) must stay strongest tier given moderate-risk fee structure. Option 3 requires escalated counsel review.

### 5. Named investor list mechanism
- Introducer provides written list of specific investors they intend to introduce
- DE reviews and approves/rejects within 10 Business Days
- Only approved investors qualify for fees
- Investors with whom DE has had contact within prior 12 months are excluded
- List can be updated on demand (no fixed cadence — see MIA-Q14)

### 6. Enhanced severability + automatic suspension
- If any provision of Annex B is held to constitute a regulated activity, Annex B terminates automatically **without** affecting the Master Framework or Annex A
- Fees already paid under Annex B prior to termination are non-refundable
- The Master Framework's confidentiality and non-circumvention survive Annex B termination
- If any regulatory authority (AFM, FCA, SEC, FINMA, or equivalent) issues guidance, enforcement, or legislation that would cause Annex B activities to require a licence the Introducer does not hold, **Annex B is automatically suspended** until the parties agree a compliant restructuring or terminate Annex B. Master + Annex A continue unaffected during suspension.

### Standard Annex B fee schedule (as built — Option 2)

| Capital committed | Fee |
|---|---|
| Any amount | 2% of capital committed, max EUR 250,000 per introduction |

**Qualifying trigger:** Named investor on approved list + first substantive meeting held + investor commits capital.
**Tail:** 12 months after agreement termination (harmonised with Annex A per MIA-Q13).
**Pipeline exclusion:** Defensive carve-out clause — fee void if Provider can demonstrate direct relationship or prior 12-month contact (per MIA-Q12). No upfront list attached.

---

## Confidentiality dependency — interaction with LOI templates

| Scenario | Confidentiality source |
|---|---|
| MIA signed **alongside** an LOI | LOI provides confidentiality. MIA references it (ALT-A). |
| MIA signed **without** an LOI | MIA must contain its own embedded confidentiality (ALT-B). |

The LOI Distributor template (Cl. 6) was already broadened to cover information exchanged "in connection with this LOI and any companion agreements between the Parties" so the LOI confidentiality reaches MIA exchanges where both are signed.

DS Mode B Cl. 3.4 already says: "The economic terms of the referral arrangement will be set out in a separate Referral Agreement between the Parties." That Referral Agreement is the MIA + Annex A.

---

## Build sequence (COMPLETE)

1. ~~**Master Framework**~~ — DONE. Confidentiality (ALT-A/ALT-B) and non-circumvention clauses adapted from LOI v3.0 Tier B. Pipeline carve-out (Cl. 7) is a new MIA-specific clause. → `mia/templates/DE-MIA-v1.0_Master_TEMPLATE.md`
2. ~~**Annex A**~~ — DONE. Dual fee election (capitalised one-time default + tiered residual MRR). Schedule A-1 per-execution. → `mia/templates/DE-MIA-v1.0_AnnexA_Commercial_TEMPLATE.md`
3. ~~**Annex B**~~ — DONE. All 6 safeguards. Option 2 fee (2% / EUR 250k cap). Termination-for-cause + clawback. **Hard gate: `legal-counsel` skill review required before first execution** (see assembly guide §10). → `mia/templates/DE-MIA-v1.0_AnnexB_Capital_TEMPLATE.md`
4. ~~**YAML intake + generation script**~~ — DONE. 4 YAML examples (master_only, commercial, capital, both). `generate_mia.py` — python-docx, document-factory cover integration, scope-based annex activation. → `mia/examples/` + `mia/generate_mia.py`
5. ~~**Skill integration**~~ — DONE. Built into `legal-assistant` (not loi-generator) per MIA-Q8. Assembly guide at `mia/MIA_ASSEMBLY_GUIDE.md`. Decision: `legal-assistant/mia/` follows the `<doctype>/` convention.

---

## Files (BUILT — v1.0)

Location: `~/skills/.claude/skills/legal-assistant/mia/` (follows `<doctype>/` convention per MIA-Q8 corrected answer).

| File | Path |
| :---- | :---- |
| Master template | `mia/templates/DE-MIA-v1.0_Master_TEMPLATE.md` |
| Annex A template | `mia/templates/DE-MIA-v1.0_AnnexA_Commercial_TEMPLATE.md` |
| Annex B template | `mia/templates/DE-MIA-v1.0_AnnexB_Capital_TEMPLATE.md` |
| Assembly guide | `mia/MIA_ASSEMBLY_GUIDE.md` |
| YAML: master only | `mia/examples/intake_example_master_only.yaml` |
| YAML: commercial | `mia/examples/intake_example_commercial.yaml` |
| YAML: capital | `mia/examples/intake_example_capital.yaml` |
| YAML: both | `mia/examples/intake_example_both.yaml` |
| Generation script | `mia/generate_mia.py` |

---

## Open questions (answer-pending)

Each question has a stable ID. Answer inline by filling the **Answer:** line.
Tags: `[BLOCKING]` = must answer before drafting begins. `[DEFERRABLE]` = can be answered during drafting.

### MIA-Q1 [BLOCKING] — Specific Introducer waiting?
Is there a specific Introducer waiting for this document, or is it speculative? If specific, that shapes Annex B scope and named-investor list immediately.

**Answer:** Yes — four specific parties to onboard. See §Introducer pipeline below.
- **Commercial only (Annex A):** Nick Alderwelde (Sovereign AI)
- **Capital only (Annex B):** Rutger
- **Both (Master + A + B):** Tal Katran; Arie Rastinger

### MIA-Q2 [BLOCKING] — Pay capital-intro fees at all?
Is DE prepared to pay capital-introduction fees at all? Many institutional founders refuse on principle (signals weakness, contaminates cap-table optics). Confirm before drafting Annex B at all.

**Answer:** Yes — DE will pay capital-intro fees under controlled terms. Build Annex B.

### MIA-Q3 [BLOCKING] — Does Annex B exist now?
Does Annex B even need to exist now, or is the immediate need only Annex A (commercial)? Building Annex B without a real use case wastes counsel review fees.

**Answer:** Yes — build Annex B now. Dutch counsel engagement is on the critical path (see MIA-Q5).

### MIA-Q4 [BLOCKING] — Existing informal arrangements?
Does the MIA replace or coexist with any informal/verbal finder's-fee arrangements DE has already made? Need an inventory before deploying a template that could conflict.

**Answer:** None existing — clean slate. But four Introducers to onboard via this MIA (see MIA-Q1 answer + §Introducer pipeline). No legacy carve-outs needed; first executions ARE the inventory.

### MIA-Q5 [BLOCKING] — Dutch counsel relationship?
Annex B regulatory reps and warranties need external legal sign-off before first execution — do not deploy from template alone. Is there a named Dutch counsel relationship to reference, or is "engage Dutch counsel" an action Carlos still owns?

**Answer:** Use the `legal-counsel` skill for review. Annex B reps and warranties to be reviewed via legal-counsel skill before first execution. External Dutch counsel engagement deferred unless legal-counsel flags items requiring outside review.

### MIA-Q6 [DEFERRABLE] — Self-identify as "Referral Agreement"?
Should the MIA explicitly self-identify as the "Referral Agreement" referenced in LOI Distributor Mode B Cl. 3.4? Avoids ambiguity if both are signed together.

**Answer:** Yes — self-identify. Master clause to state: "This Agreement is the Referral Agreement contemplated by LOI Distributor Mode B Cl. 3.4 where applicable."

### MIA-Q7 [DEFERRABLE] — Signing entity B.V. or AG?
LOI v3.0 chose B.V. for jurisdictional alignment. MIA may need to differ when the introduced object is equity in AG (capital) vs colocation services in B.V. (commercial). May need both, depending on which annex is active.

**Answer:** Per-deal selectable. Template supports both B.V. and AG; selector in YAML intake per execution. Default guidance: B.V. for Master + Annex A (commercial), AG for Annex B (capital), but Operator overrides per deal.

### MIA-Q8 [DEFERRABLE] — Build into loi-generator or wait for legal-assistant?
The restructure plan already absorbs loi-generator into legal-assistant. Building MIA into loi-generator now creates migration debt.

**Answer:** Build into `legal-assistant`. Per repo convention (mirroring `legal-assistant/colocation/`), files land at:
- `~/skills/.claude/skills/legal-assistant/mia/templates/`
- `~/skills/.claude/skills/legal-assistant/mia/examples/`
- `~/skills/.claude/skills/legal-assistant/mia/generate_mia.py`

(Original Q8 phrasing said `legal-assistant/templates/mia/` — corrected here to follow the established `<doctype>/templates/` convention.)

### MIA-Q9 [BLOCKING] — Annex B fee option default?
Provisional default is Option 1 (flat) — see §Annex B fee structure. Confirm sign-off, and confirm risk appetite on Option 1 vs Option 2: Option 1 (flat) is regulatorily safest but commercially weaker (introducers prefer upside). What is the negotiating posture?

**Answer:** Option 2 (capped %) — overrides original spec default of Option 1. Use 2% of capital committed with EUR 250k cap per introduction as the standard. Update §Annex B sec. 4 and §Standard Annex B fee schedule accordingly. Activity limitations and reps must be the strongest tier (per §Annex B sec. 1–3) given the moderate-risk fee structure.

### MIA-Q10 [BLOCKING] — VAT / invoicing default?
Invoicing entity, currency, payment terms. Cross-border example: Introducer in UK, DE in NL, customer in Germany.

**Answer:** Per-deal in annex execution schedule. Template leaves invoicing entity, currency, and payment terms blank; each MIA execution fills in based on counterparty jurisdiction. Add explicit placeholder fields in YAML intake.

### MIA-Q11 [BLOCKING] — Annex A default fee structure?
Residual % MRR or capitalised one-time? Affects operational burden materially. See MIA-P5 — operational simplicity argues for capitalised one-time as default.

**Answer:** Both — Introducer's choice per deal. Template offers both capitalised one-time (X months MRR equivalent at MSA execution) AND residual % MRR (tiered 8-10% / 6-8% / 4-6%). Selector in YAML intake; Introducer elects during MIA negotiation. Default presentation order: capitalised first (operationally simpler).

### MIA-Q12 [DEFERRABLE] — Pipeline exclusion mechanism?
Need a kept-current list of (a) customers already in DE pipeline, (b) investors with prior 12-month contact. Where does this live — HubSpot list export, static schedule appendix, or living document?

**Answer:** No upfront exclusion list attached to the agreement. List is implicit, derived from HubSpot + other DE communication channels. Mechanism instead: defensive carve-out clause stating fee is void/not due if DE can demonstrate the introduced party was already a direct relationship OR DE had been in touch within the prior 12 months. Burden of proof on DE; HubSpot record + email/comms history serve as evidence. Drafting note: clause must be in both Annex A and Annex B with parallel language; harmonised 12-month look-back across both annexes.

### MIA-Q13 [BLOCKING] — Tail period harmonisation?
Annex A tail is "initial contract term"; Annex B tail is 18 months. Should they harmonise, or stay differentiated? Confirm intentional.

**Answer:** Harmonise to 12 months post-termination for both Annex A and Annex B. Update §Annex A and §Annex B fee schedule subsections accordingly. Tighter than original Annex B 18-month default.

### MIA-Q14 [DEFERRABLE] — Named investor list cadence?
Quarterly cadence assumed for the named investor list (see §Annex B sec. 5). Confirm with whoever manages capital intro relationships.

**Answer:** On-demand only — no fixed cadence. Introducer requests additions/changes; DE approves within the 10 Business Day window already specified in §Annex B sec. 5. Update §Annex B sec. 5 to remove "quarterly" language.

---

## Gaps (missed in original handover)

### MIA-G1 — Source plan not re-read in full
Handover was assembled from a conversation summary, not a fresh read of `/Users/crmg/.claude/plans/cuddly-doodling-donut.md`. Anything refined in the live plan since the summary may be missing.

### MIA-G2 — LOI v3.0 binding clauses not verified for portability
Master Framework confidentiality + non-circumvention assumed liftable from LOI Cl. 6/7. They may not lift cleanly — LOI clauses are drafted in LOI context.

### MIA-G3 — Execution mechanics absent
Signature blocks, effective date, eIDAS reference, governing-law clause text, Dutch entity choice (B.V. vs AG) not specified.

### MIA-G4 — Non-DS LOI interaction not addressed
Can a Wholesale or End User counterparty also sign an MIA (e.g. neocloud referring customers)? Not documented.

### MIA-G5 — Conflicts / tie-break rules absent
No "first written introduction wins" mechanic — the most common dispute trigger in finder's-fee agreements.

### MIA-G6 — VAT / withholding / cross-border invoicing not covered
Introducer in UK, DE in NL, customer in Germany — who invoices, in what currency, with what tax treatment. (Overlaps with MIA-Q10.)

### MIA-G7 — Non-circumvention for introduced contacts under-specified
Listed as a Master Framework component but no duration, scope, or carve-out for pre-existing relationships.

**Status:** CLOSED (v3.0). Master Cl. 6 specifies duration ([NC_DURATION], default 12 months), scope (Introduced Parties per activated Annex), and carve-out (Cl. 6.3 Independent Knowledge Exception).

### MIA-G8 — Pipeline exclusion list mechanic unresolved
Flagged as open question (MIA-Q12) but no proposed mechanism (HubSpot list export attached as schedule? Living document? Static appendix?).

**Status:** CLOSED (v2.1). Resolved via defensive carve-out clause in Master Cl. 7 (no upfront list). See MIA-Q12 answer.

### MIA-G9 — Memory record not coordinated with legal-assistant restructure
`project_de_mia.md` and the legal-assistant restructure plan need cross-referencing to avoid collision.

**Status:** CLOSED (v3.0). Memory `project_de_mia.md` updated with v2.1 + v3.0 build notes. Handover §Cross-references updated to point to legal-assistant paths.

---

## Polish (fixes to apply during/after drafting)

### MIA-P1 — Annex B Option 3 framing is contradictory
Described as "industry standard but avoid." Either remove it entirely or gate it behind named-counsel sign-off per deal.

**Status:** ADDRESSED (v3.0). §Annex B sec. 4 updated to show Option 2 as selected. Option 3 retained in spec but gated behind "CEO + counsel sign-off per deal" in both spec and assembly guide §6.

### MIA-P2 — Fee numbers are illustrative not validated
EUR 50k flat / EUR 250k cap / 8–10% MRR — none benchmarked against DE's actual past offers or market rates. Treat as plan defaults, not policy.

**Status:** OPEN. Warning added to §Annex A spec body and assembly guide §4. Fee numbers remain illustrative. Validate against first-wave deal economics (Nick, Rutger) before hardening.

### MIA-P3 — "Dutch counsel review before first execution" should be a hard build-sequence gate
Not optional for Annex B. Promote from open decision to gate in §Build sequence step 3.

**Status:** CLOSED (v3.0). Promoted to hard gate in: (a) §Build sequence step 3 (bold text); (b) Annex B template drafter instruction step 2 (MANDATORY); (c) assembly guide §10 (dedicated section); (d) Schedule B-1 includes counsel-review confirmation field.

### MIA-P4 — Tail-period inconsistency unresolved
Annex A = "initial contract term", Annex B = 18 months. Propose a default and confirm with Carlos. (See MIA-Q13.)

**Status:** CLOSED (v2.1). Harmonised to 12 months for both annexes per MIA-Q13.

### MIA-P5 — MRR-percentage residuals are operationally heavy
Multi-year per-customer tracking and recurring payments. Recommended alternative: capitalised one-time payment at MSA execution (e.g. X months MRR equivalent). Make this the default if operational simplicity matters. (See MIA-Q11.)

**Status:** ADDRESSED (v2.1). MIA-Q11 resolved: both options available, Introducer elects per deal, capitalised one-time is the default. Template Cl. A.4.5 sets capitalised as default when no election made.

### MIA-P6 — No termination-for-cause mechanic
If an Introducer breaches Annex B activity limits (e.g. starts soliciting investors), needs explicit termination + clawback for fees paid.

**Status:** CLOSED (v3.0). Annex B Cl. B.11 implements immediate termination on breach of B.3/B.4/B.5 + 12-month fee clawback.

### MIA-P7 — "Automatic suspension" of Annex B is elegant but vague
Who declares it? On what evidence? Needs a notice mechanism and a triggering-event definition.

**Status:** CLOSED (v3.0). Annex B Cl. B.12 implements: 4 defined Regulatory Triggers (B.12.1(a)–(d)), written notice mechanism (B.12.2), effect of suspension (B.12.3), 60-day restructure-or-terminate window (B.12.4).

---

## Introducer pipeline (to onboard via MIA)

Four specific Introducers identified for first-wave MIA execution. None have existing informal arrangements (MIA-Q4); these are first-time onboardings.

| Introducer | Annex(es) | Affiliation | Notes |
|---|---|---|---|
| Nick Alderwelde | A (Commercial) | Sovereign AI | First commercial-only execution |
| Rutger | B (Capital) | *(to confirm)* | First capital-only execution; Annex B counsel-review path applies |
| Tal Katran | A + B (Both) | *(to confirm)* | Master + both annexes |
| Arie Rastinger | A + B (Both) | *(to confirm)* | Master + both annexes |

Operational follow-ups before first execution:
- Confirm full names, entities, jurisdictions for all four
- For each "Both" execution, confirm whether one signing event covers Master + A + B or whether annexes execute on different dates
- Create CRM records (HubSpot) for each as MIA Introducer contacts so the §Q12 defensive carve-out has provable contact-history evidence going forward

---

## Cross-skill TODOs

- Bespoke-closing constraint fix for `legal-assistant/SKILL.md` tracked in `~/skills/.claude/skills/legal-assistant/OPEN_ITEMS.md` as `OPEN-1` (MIA-unrelated).

---

## Revision log

- **2026-04-13 v1** — Original 7-section spec drafted (Why / Architecture / Annex A / Annex B / Confidentiality dependency / Build sequence / Open decisions).
- **2026-04-13 v1.1** — Gaps & polish addendum added (missed items, polish items, 17 open questions, document structure issues, carry-over).
- **2026-04-13 v2** — Restructure: consolidated decision lists into single canonical question list with stable IDs (MIA-Q1…MIA-Q14) and inline `**Answer:**` scaffolding; tagged 9 BLOCKING (Q1–Q5, Q9, Q10, Q11, Q13) and 5 DEFERRABLE (Q6–Q8, Q12, Q14); renumbered gaps (MIA-G1…G9) and polish (MIA-P1…P7); relocated bespoke-closing carry-over to `legal-assistant/OPEN_ITEMS.md` as `OPEN-1` (path updated post loi-generator → legal-assistant rename); removed obsolete §Document structure issues; deleted superseded §Open decisions before drafting.
- **2026-04-13 v2.1** — All 14 open questions answered inline. Key decisions: Annex B fee = Option 2 (capped %, 2% / EUR 250k cap); Annex A fee = both options (Introducer's choice per deal); tail period harmonised to 12 months; signing entity per-deal selectable; MIA self-identifies as LOI Cl. 3.4 Referral Agreement; build target = `legal-assistant/mia/`; Dutch counsel review via `legal-counsel` skill; pipeline exclusion via defensive carve-out clause (no upfront list); named investor list = on-demand. Added §Introducer pipeline with 4 first-wave targets (Nick Alderwelde, Rutger, Tal Katran, Arie Rastinger).
- **2026-04-13 v3.0** — **BUILT.** All 9 files produced at `legal-assistant/mia/` (3 templates, 4 YAML examples, 1 assembly guide, 1 generate script). §Files section updated from "when built" to "BUILT". Handover status changed from "Designed, not built" to "Built v1.0". Cross-references updated for legal-assistant migration.
- **2026-04-14 v3.1** — Post-build hardening: smoke-tested `generate_mia.py` against all 4 YAML examples (commercial / capital / both / master-only) — all four scopes generate clean .docx output with correctly-rendered nested quotes. Fixed ~20 f-string / string-literal quote-escape bugs caught during smoke test. Updated stale cross-references in `SKILL.md` (lines 300, 328), `FEATURE_MATRIX.md` (§Companion status line), `ASSEMBLY_GUIDE.md` (added MIA pointer), and `SKILLS_INDEX.md` (added `legal-assistant` skill row #62; legal domain count 2→3).

---

## Cross-references

- LOI v3.0 system: `~/skills/.claude/skills/legal-assistant/colocation/`
- LOI assembly guide: `~/skills/.claude/skills/legal-assistant/ASSEMBLY_GUIDE.md`
- MIA files: `~/skills/.claude/skills/legal-assistant/mia/` (templates, examples, generate_mia.py, MIA_ASSEMBLY_GUIDE.md)
- Plan: `/Users/crmg/.claude/plans/cuddly-doodling-donut.md` (Phase 2 → Section D documents the MIA architecture in full)
- Memory: `project_loi_ncnda_v3.md` (mentions MIA as companion framework — now built)
- Memory: `project_de_mia.md` (MIA-specific project memory)
- Restructure plan: `~/.claude/plans/legal-assistant-restructure-handover.md` (loi-generator → legal-assistant migration — complete)
