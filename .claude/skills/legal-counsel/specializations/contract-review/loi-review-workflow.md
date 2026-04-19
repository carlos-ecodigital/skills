# LOI Review Workflow

Single-phase structured review of a colocation Letter of Intent produced by the `legal-assistant` skill. This workflow is the **callee side** of `legal-assistant` Phase 7.5 — a mandatory non-bypassable review gate that sits between automated QA pass (Phase 7) and delivery (Phase 8).

**Target:** 5–10 minute structured pass against 4 explicit checks. Returns one of three envelopes (`PASS` / `FLAG-FOR-REVISION` / `REJECT`) that the caller can parse deterministically.

---

## Trigger

Invoked from `legal-assistant` Phase 7.5. Canonical caller is `/Users/crmg/Claude/skills/.claude/skills/legal-assistant/SKILL.md` Phase 7.5 block (lines ~372–410).

**Inputs the caller passes:**
| Input | Example | Use |
|---|---|---|
| `.docx` path | `/tmp/20260417_DEG_LOI-WS_Polarise_(DRAFT).docx` | Read rendered output |
| intake YAML path | `/tmp/intake_polarise_20260417.yaml` | Read intake context + source_map |
| QA report path | `/tmp/20260417_DEG_LOI-WS_Polarise_(DRAFT)_qa.txt` | See automated-linter findings |
| `counterparty.source_map` | inline dict | Source-verification anchor |

**Invocation pattern**: reference-only (per codebase convention verified in v3.5.2 audit). Caller names this file in SKILL.md; on next turn, the agent loads this workflow file in-context and runs the 4-point review. No runtime Task-tool coupling; no automated handoff. Enforcement is **social** — Phase 7.5 fails closed if this workflow is not run.

---

## How to Run This Workflow

### Step 0 — Document acquisition

Open the `.docx` via `python-docx` and extract text by paragraph. Read the intake YAML for source_map + commercial context. Read the QA report for prior linter findings (R-14 warnings, R-23 attribution status, etc.).

### Step 1 — Clause-type appropriateness check

Read each operative clause and verify it fits the LOI type. Specifically:

| LOI type | Cl. 5 MUST be | Flag if |
|---|---|---|
| End User (EU) | "Project Finance and Assignment" (revenue-bankability) | other |
| Distributor (DS) | "Project Finance and Assignment" | other |
| Wholesale (WS) | "Project Finance and Assignment" | other |
| **Strategic Supplier (SS)** | **"Supply Chain and Delivery Commitment"** (supply-side, NOT revenue-bankability) | Cl. 5 says "Revenue Bankability" → **FLAG** (type-mismatch bug) |
| Ecosystem Partnership (EP) | No Cl. 5 Finance — structure is lighter | Cl. 5 Finance present → FLAG |

Other clause-type checks:
- Recital A tail must match type (EU = enterprises/AI labs/research; DS = channel partners; WS = megawatt-scale NeoCloud; SS = EPC/modular/OEM; EP = ecosystem/policy)
- Cl. 3 commercial model must match type (EU = bare_metal/managed; DS = partnership_mode; WS = MW IT + sites; SS = purposes 1–2; EP = collaboration_themes)
- Defined term: provider = `"Digital Energy"` (v3.5.2 brand-name); counterparty = `the Customer` / `the Partner` / `the Supplier` per type

**Output of step 1**: pass / flag with specific line pointers.

### Step 2 — Meta-commentary scan

Search rendered body for phrases that **describe the LOI's purpose** rather than **create obligations**. Regex patterns:

```
The Provider's ability to (secure|obtain|access)
is intended to evidence
depends in part on
while non-binding in its commercial terms
to support the Provider's financing
will require the exchange of (Confidential Information|material)
The Parties acknowledge that the Provider intends
```

Plus any sentence that reads as commentary about the instrument itself rather than an operative provision.

**Typical culprits** (v3.4 fixed): Recital C/D preambles; Cl. 5.1 commentary. If any re-emerged → FLAG.

**Output of step 2**: pass / flag with specific clause + snippet.

### Step 3 — Cross-clause consistency check

Verify alignment between interdependent clauses:

- **Cl. 5 ↔ Cl. 3**: commercial model described in Cl. 3 must be the one Cl. 5 supports (e.g., WS Cl. 3 MW IT → Cl. 5 references Financing Parties; SS Cl. 3 supply purposes → Cl. 5 is supply-side)
- **Recital A tail ↔ Cl. 3 offer**: Recital A framing must introduce the commercial offer Cl. 3 instantiates
- **Parties Preamble ↔ cover page ↔ sig block**: legal name, address, registration identical across all three (v3.5.2 Parties Preamble addition requires this consistency)
- **Cl. 6 confidentiality survival**: duration must match the `protection.confidentiality_survival` intake value; no drift
- **Cl. 7 non-circumvention duration**: matches `protection.nc_duration` (EU/DS/WS/SS — not EP)

**Output of step 3**: pass / flag with cross-reference pointer.

### Step 4 — Source verification sample

Randomly select **3 material claims** from Recital B. For each:
1. Extract the claim text (e.g., "supports Deutsche Telekom's Industrial AI Cloud")
2. Identify the pillar it belongs to (1 identity / 2 business / 3 track record / 4 fit / 5 pipeline)
3. Verify the corresponding pillar in `counterparty.source_map` has a tier-1 URL
4. Spot-check one URL via WebFetch — does the claim appear on that page?

**Verdict per sample**:
- URL exists + claim verifiable → PASS
- URL exists + claim not on page → **FLAG** (attribution failure)
- Pillar marked `[TBC]` → PASS (acceptable draft state)
- No URL + no `[TBC]` → **FLAG** (fabrication gate)
- Claim relies on tier-2 press but no qualifier → **FLAG**

Three samples total; overall step passes if all three are clean (or marked `[TBC]` appropriately).

**Output of step 4**: pass / flag per sample + overall verdict.

---

## Two-pass review (v3.5.6 Scope G-bis)

**Important**: as of v3.5.6, this junior workflow is the **first pass** of a two-pass Phase 7.5 review. The envelope you produce below is a **draft** that feeds into the senior counsel refinement pass at `loi-senior-review-pass.md` (sibling file in this directory). The senior pass reviews your envelope, catches what you missed across six senior-review axes (commercial posture, precedent consistency, counterparty-reading, Signal-Test deep check, identity/execution hygiene, deliverability/aftermath), and produces the **final** envelope that `legal-assistant` consumes.

**When you return your envelope below, do not assume it is final.** The senior pass may:
- **Upgrade** your `FLAG` or `REJECT` to `PASS` if it finds the issue you flagged is a false positive — with a documented reason.
- **Downgrade** your `PASS` to `FLAG` or `REJECT` if it finds a deeper issue across the six senior axes that your 4-point checklist did not cover.
- **Consolidate** multiple junior flags into a single prioritised fix list.

Your job in the junior pass is to produce an **honest and complete** 4-point-checklist envelope. The senior's job is to review it. Do not try to pre-empt the senior's judgement calls — that is not what a junior pass is for.

**Flow**: this file (junior) → `loi-senior-review-pass.md` (senior) → final envelope returned to `legal-assistant`.

---

## Return envelope

Produce one of three outputs. Format is strict so `legal-assistant` Phase 7.5 can parse deterministically. **This envelope is the junior pass output — it feeds into the senior pass, not directly to `legal-assistant`.**

### PASS

```
LOI_REVIEW_RESULT: PASS
Reviewer: legal-counsel (loi-review-workflow)
Date: 2026-04-17T14:30:00Z
Inputs:
  docx: /tmp/20260417_DEG_LOI-WS_Polarise_(DRAFT).docx
  intake: /tmp/intake_polarise_20260417.yaml
Checks:
  [1] Clause-type appropriateness: PASS
  [2] Meta-commentary scan: PASS
  [3] Cross-clause consistency: PASS
  [4] Source verification (3 samples): PASS
Notes: [optional brief note, ≤ 100 words]
```

**legal-assistant action on PASS**: proceed to Phase 8 (Delivery).

### FLAG-FOR-REVISION

```
LOI_REVIEW_RESULT: FLAG-FOR-REVISION
Reviewer: legal-counsel (loi-review-workflow)
Date: 2026-04-17T14:30:00Z
Inputs: [as above]
Checks:
  [1] Clause-type appropriateness: [PASS | FLAG — detail]
  [2] Meta-commentary scan: [PASS | FLAG — detail]
  [3] Cross-clause consistency: [PASS | FLAG — detail]
  [4] Source verification: [PASS | FLAG — per-sample detail]
Recommended fix route:
  - Back to Phase 5 (Recital B redraft): [reason + specific edit]
  - Back to Phase 6 (intake confirmation gate): [reason + specific edit]
Notes: [specific line-level feedback for caller to action]
```

**legal-assistant action on FLAG**: routes back to the named phase; user reconfirms; rebuilds; resubmits to Phase 7.5.

### REJECT

```
LOI_REVIEW_RESULT: REJECT
Reviewer: legal-counsel (loi-review-workflow)
Date: 2026-04-17T14:30:00Z
Inputs: [as above]
Reason: [one-line root cause]
Detail: [≤ 300 words — why this LOI cannot be delivered in its current form, e.g. material fabrication, wrong LOI type, irreducible consistency break]
Escalate to: Carlos Reuven (CEO) + Jonathan Glender (CGO)
```

**legal-assistant action on REJECT**: stop. Do not deliver. Escalate per Reason. User decides next step manually (regenerate, abandon, escalate to legal-counsel for full redraft).

---

## Fail-closed behavior

If this workflow cannot be completed for any reason (inputs missing, docx unreadable, WebFetch down, reviewer aborts mid-flow):
- Treat as implicit `REJECT` with Reason = "Phase 7.5 incomplete — review not performed"
- Do NOT return PASS by default
- Do NOT allow Phase 8 to proceed
- Caller is responsible for re-invoking after fixing inputs

This is the v3.5.2 scope G fail-closed spec. No override path in v3.5.x.

---

## Scope (non-goals)

This workflow is **LOI-specific**. It does NOT:
- Review NDAs (see `nda-review-workflow.md`)
- Negotiate LOI terms (counterparty redlines → escalate full legal-counsel engagement)
- Draft LOIs from scratch (that's `legal-assistant`)
- Handle MIA counterparty introductions (separate pathway)
- Handle M&A / investment / CIA-CAP / generic commercial LOIs outside the 5 DE types

If the review reveals an out-of-scope counterparty type: return REJECT with Reason = "out-of-scope for 5-type LOI framework".

---

## Versioning

- **v1.0** — 2026-04-17 — initial release alongside legal-assistant v3.5.2
- Sync with `legal-assistant/CHANGELOG.md`; any material change to caller contract (inputs, return envelope) must bump both skills in lock-step
