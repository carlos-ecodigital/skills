# LOI Senior Counsel Refinement Pass

**Purpose.** Second review pass in the Phase 7.5 two-stage review (v3.5.6 Scope G-bis). The **junior-tier** `loi-review-workflow.md` produces a first-draft envelope (`PASS` / `FLAG-FOR-REVISION` / `REJECT`) from a structured 4-point check. This pass — **senior counsel** — reviews the junior's envelope, catches what the junior missed, upgrades or downgrades the verdict where warranted, and produces the **final** envelope that the `legal-assistant` skill consumes in Phase 7.5.

This mirrors how contracts review actually happens in any competent law firm: the associate does the grunt review against a checklist, the partner reviews the associate's memo and the underlying document, asks the questions the checklist didn't, and signs off (or redirects). Without this second pass, Phase 7.5 is a syntactic gate — the structured 4-point sweep. With it, Phase 7.5 becomes a real judgement gate.

---

## Trigger

Invoked immediately after `loi-review-workflow.md` (the junior pass) returns its envelope. Canonical entry point is `legal-assistant` Phase 7.5, which now runs the two passes in sequence:

1. Load `loi-review-workflow.md`, run the junior 4-point review, obtain a draft envelope.
2. Load this file (`loi-senior-review-pass.md`), review the junior's output, produce the final envelope.
3. Return the **final** envelope to `legal-assistant` (the skill only acts on the senior's verdict — the junior's envelope is an intermediate artefact, not the gate).

**Inputs** (same as the junior pass plus the junior's output):

| Input | Example | Use |
|---|---|---|
| `.docx` path | `/tmp/20260417_DEG_LOI-WS_Polarise_(DRAFT).docx` | Re-read the instrument with senior judgement (do not trust the junior's summary) |
| intake YAML path | `/tmp/intake_polarise_20260417.yaml` | Cross-check the instrument against the intake for scope drift |
| QA report | `/tmp/20260417_DEG_LOI-WS_Polarise_(DRAFT)_qa.txt` | Sanity-check R-22/R-23/R-24/R-25/R-27/R-28 output + the new R-23 pillar-attribution diagnostic (v3.5.6 Scope D) |
| `counterparty.source_map` | inline dict | Verify source attribution independently of the junior's sample |
| **Junior envelope** | `PASS` / `FLAG` / `REJECT` + notes from `loi-review-workflow.md` | **Review, don't defer to.** The junior's output is a starting point, not a conclusion. |

**Invocation pattern**: reference-only (same as the junior file; same codebase convention verified in v3.5.2 audit). Phase 7.5 enforcement (v3.5.6 Scope G) is the code-level gate — this file is the human-judgement gate that sits inside it.

---

## Posture

A senior counsel is not a line-editor. A senior counsel asks **different** questions than the junior. The junior pass is a **checklist** (did we miss anything in the four known categories?). The senior pass is a **commercial-legal reading of the instrument as a whole** (is the deal defensible, proportionate to risk, consistent with precedent, and ready to send to a counterparty-of-record whose counsel will do their own senior review on receipt?).

If the senior finds themselves mostly agreeing with the junior's notes, the senior isn't earning their keep. A useful senior pass adds value in at least one of the axes below on every non-trivial LOI.

---

## Six senior-review axes

Run through each axis explicitly. Some will pass silently; at least one will usually surface something the junior did not.

### Axis 1 — Commercial posture & proportionality

Questions the junior's checklist does not ask:

- Does the **commercial ask** in Cl. 3 match the **counterparty profile** in Recital B? (e.g., asking a seed-stage NeoCloud for 50 MW with a 5-year pre-payment: disproportionate — flag even if every clause is internally consistent.)
- Is the **binding/non-binding framing** (Cl. 5, Cl. 6, Cl. 7, Cl. 8) proportionate to what the Provider will rely on the counterparty for? (e.g., a 3 MW pilot LOI with a 36-month non-circumvention tail is excessive; a 100 MW LOI with a 3-month NC is under-protected.)
- **Term** — does the indicative term in Cl. 3 match the counterparty's own published contract norms? (A 10-year LOI to a counterparty whose published MSAs run 3-year is a non-starter; the junior won't flag this because the LOI is internally consistent.)
- **Signatory level** — is the counterparty's signatory proposed at the right seniority for the commercial stakes? (A 50 MW LOI signed by a regional VP rather than CEO is a precedent problem regardless of whether the sig block renders correctly.)

**Verdict contribution**: any "no" here is at minimum a `FLAG`. A disproportionate commercial posture is never a `PASS` regardless of how clean the document renders.

### Axis 2 — Precedent and consistency with prior DE instruments

The junior pass looks at this LOI in isolation. The senior pass looks at it against the **corpus of signed and prior-drafted DE LOIs**.

- Is this LOI consistent with **recent signed precedent** of the same type? (If the last three signed WS LOIs all carried a 12-month confidentiality survival and this one has 3 years, why?)
- Are defined terms consistent with the DE house-style glossary? (Provider = "Digital Energy" brand-name; per v3.5.2. Defined terms must not drift across instruments.)
- Does the Recital A tail match the **canonical v3.4 body + per-type tail** without bespoke drift? (If the engine drifted, that's a generator regression, not a review finding — but the senior catches it.)
- Is the Cl. 5 treatment consistent with the type matrix (EU/DS/WS = revenue bankability; SS = supply chain; EP = no Cl. 5)? (Junior R-23 + type-check covers this, but the senior re-checks because the type-check has been a source of v3.4-class bugs historically.)

**Verdict contribution**: precedent drift without documented justification → `FLAG`. Bespoke deviation with a documented reason → `PASS` (note the reason in the senior's envelope).

### Axis 3 — Counterparty-reading (read as opposing counsel would)

Read the LOI as if you were the counterparty's senior counsel seeing this for the first time. What would you redline?

- Does **Cl. 6 Confidentiality** have carve-outs the counterparty's counsel will immediately push back on? (Compelled-disclosure, pre-existing-knowledge, independently-developed, public-domain exceptions — present? Proportionate?)
- Does **Cl. 7 Non-Circumvention** have a territorial and temporal scope a reasonable counterparty can accept? (Overbroad NC is a guaranteed redline.)
- Does **Cl. 8 General** (governing law, dispute resolution, notices) match what the counterparty's jurisdiction actually recognizes? (e.g., US LLC counterparty + Dutch governing law + no seat-of-arbitration clause → predictable redline on receipt.)
- Are there **unsigned-but-material** side references that the counterparty's counsel will ask about? (Any reference to a separate NDA, MSA, or framework agreement that the counterparty hasn't seen → flag for Phase 5/6 clarification.)

**Verdict contribution**: items reasonable opposing counsel would redline → `FLAG-FOR-REVISION` with specific language proposed by the senior. The goal is to pre-empt the redline, not to ship a draft that provokes one.

### Axis 4 — Signal-Test and source-verification deep check

The junior pass runs a 3-claim random sample. The senior pass does a **deeper read** of Recital B:

- Every **named endorser** in Recital B: is the counterparty→endorser relationship currently active? (A named customer who has since churned is a misrepresentation.)
- Every **numeric claim** in Recital B: does the pillar diagnostic (v3.5.6 Scope D) match the claim's topic? (A "60 MW" claim matched to `pillar_1` instead of `pillar_3` is a mis-filed attribution — not a failure, but a signal.)
- Any **tier-2 claim**: is the publisher-attribution qualifier (`as publicly reported by`, `according to`, `reportedly`) present in the prose? (v3.5.3-cont Scope H pattern.)
- Any **self-announced forward plans** surviving in Recital B? (Per v3.5.2 Signal-Test Gate 1, self-announced forward plans fail gate 1 and should live in Cl. 3, not Recital B.)

**Verdict contribution**: any uncorroborated named endorser or surviving self-announced forward plan → `FLAG-FOR-REVISION` with specific redraft. Mis-filed pillar attribution → `PASS` with a note for intake hygiene.

### Axis 5 — Identity and execution hygiene

- **Parties Preamble** (v3.5.2 Scope A''') — does every legal identifier match the counterparty's **official registry** as the senior independently spot-checks? (Junior samples 3 material claims; senior spot-checks 1 identity field per party.)
- **Signatory capacity** — is the proposed signatory on the counterparty side someone with **published signing authority** (Geschäftsführer, Director with registered power of representation, etc.)? Or is it a placeholder name the counterparty will replace at execution, which the senior accepts with an explicit note?
- **Footer entity** (v3.5.1 Scope A'''') — does the footer entity (BV vs AG) match the signatory's legal capacity? (A Carlos-as-BV-Director LOI with an AG footer is a v3.5.1 regression; senior catches.)
- **Jurisdiction in Parties Preamble** — is the counterparty jurisdiction stated consistently with the counterparty's actual jurisdiction of formation? ([TBC] is acceptable; a wrong jurisdiction is not.)

**Verdict contribution**: any mismatch here → `FLAG-FOR-REVISION` with the correction specified. Senior never waves these through because they're the most-checked fields by opposing counsel on receipt.

### Axis 6 — Deliverability and aftermath

- Does the **Phase 8 delivery path** make sense for this counterparty? (DocuSign to a known work email? Side-channel to a CEO whose company email is bouncing? Physical? — this is often out of the LOI text, but the senior sets the expectation.)
- Is there a **post-delivery action** the Provider has committed to that needs to happen within N days of signature? (e.g., a "Provider will supply draft MSA within 30 days of this LOI" clause — who owns that follow-up on the Provider side?)
- Are there **regulatory or disclosure triggers** the senior sees? (FDI screening for cross-border LOIs, competition-law carve-outs for multi-party consortia, etc. — not always in the LOI but the senior notes them for the deal-team.)

**Verdict contribution**: deliverability issues → `FLAG` with a recommended operational fix (not a document redraft). Regulatory triggers → note in envelope; not typically a blocker unless the LOI itself creates a filing obligation.

---

## Verdict rules

The senior's envelope **supersedes** the junior's. The rules for reconciling:

| Junior verdict | Senior finding | Senior verdict |
|---|---|---|
| PASS | senior concurs after all six axes | PASS |
| PASS | senior surfaces a FLAG-level issue in any axis | FLAG-FOR-REVISION (senior overrides) |
| PASS | senior surfaces a REJECT-level issue | REJECT (senior overrides) |
| FLAG-FOR-REVISION | senior concurs or extends the flag list | FLAG-FOR-REVISION (consolidate + clarify) |
| FLAG-FOR-REVISION | senior finds the flag is a false positive (junior over-flagged) | PASS with "junior flag dismissed, reason: …" |
| FLAG-FOR-REVISION | senior finds a deeper REJECT issue | REJECT (senior escalates) |
| REJECT | senior concurs | REJECT (adopt junior's reason, add senior's confirmation) |
| REJECT | senior finds the REJECT is premature (junior missed a mitigating factor) | FLAG-FOR-REVISION with specific fix (senior de-escalates with explicit reasoning) |

**Senior never silently accepts the junior's verdict.** The final envelope always carries a senior note, even when it's "concurred with junior; no additional issues surfaced across axes 1–6."

---

## Output envelope (format `legal-assistant` parses)

### PASS

```
LOI_REVIEW_RESULT: PASS
Reviewer: legal-counsel (two-stage)
  Junior pass: loi-review-workflow.md — [PASS/FLAG/REJECT as originally returned]
  Senior pass: loi-senior-review-pass.md — PASS (concurs / overrides with note)
Date: 2026-04-17T14:30:00Z
Senior axis results:
  [1] Commercial posture: PASS
  [2] Precedent consistency: PASS
  [3] Counterparty-reading: PASS
  [4] Signal-Test deep check: PASS
  [5] Identity/execution hygiene: PASS
  [6] Deliverability/aftermath: PASS
Senior notes: [≤200 words — at minimum, name what the senior cross-checked beyond the junior's sample]
```

### FLAG-FOR-REVISION

```
LOI_REVIEW_RESULT: FLAG-FOR-REVISION
Reviewer: legal-counsel (two-stage)
  Junior pass: loi-review-workflow.md — [result]
  Senior pass: loi-senior-review-pass.md — FLAG (consolidated / new issues / dismissed junior flags)
Date: 2026-04-17T14:30:00Z
Senior axis results:
  [1] … PASS / FLAG — detail
  [2] … PASS / FLAG — detail
  [3] … PASS / FLAG — detail
  [4] … PASS / FLAG — detail
  [5] … PASS / FLAG — detail
  [6] … PASS / FLAG — detail
Recommended fix route:
  Back to Phase 5 (Recital B redraft): [specific senior-authored redraft language]
  Back to Phase 6 (intake confirmation): [specific intake-level fix]
  Dismissed junior flags: [list + reason each was a false positive]
Senior notes: [≤300 words — prioritise the issues by severity]
```

### REJECT

```
LOI_REVIEW_RESULT: REJECT
Reviewer: legal-counsel (two-stage)
  Junior pass: loi-review-workflow.md — [result]
  Senior pass: loi-senior-review-pass.md — REJECT
Date: 2026-04-17T14:30:00Z
Reason: [one-line root cause]
Detail: [≤400 words — why this LOI cannot be delivered; which axis surfaced the reject; whether this is a document-level fix (regenerate) or a deal-level fix (re-scope) or an escalation (counsel-out / decline)]
Escalate to: Carlos Reuven (CEO) + Jonathan Glender (CGO) + [other specific DE personnel]
Senior recommendation: [regenerate / re-scope / decline / counsel-out]
```

---

## Fail-closed behaviour

Same rule as the junior pass: if this senior review cannot be completed for any reason (inputs missing, docx unreadable, junior envelope malformed, reviewer aborts mid-flow), treat as implicit `REJECT` with Reason = "Phase 7.5 senior pass incomplete — review not performed". Do not return `PASS` by default. The caller (`legal-assistant`) will block Phase 8 on the implicit `REJECT` per Scope G enforcement (when enabled).

---

## Scope (non-goals)

This senior pass is **LOI-specific**. It does not:

- Review NDAs (see `nda-review-workflow.md`)
- Draft or negotiate LOI terms (redlines belong in a full legal-counsel engagement, not in Phase 7.5)
- Run the 4-point structured review the junior handles (that's the junior pass's job — this pass reviews the junior's output, not the raw document against a checklist)
- Handle MIA counterparty introductions, M&A instruments, investment term sheets, or any non-DE-5-type instrument

If the senior review surfaces that the instrument is out-of-scope for the 5-type LOI framework: return `REJECT` with Reason = "out-of-scope for 5-type LOI framework; needs full legal-counsel engagement".

---

## Versioning

- **v1.0** — 2026-04-17 — initial release as v3.5.6 Scope G-bis (senior counsel refinement pass). Invoked after `loi-review-workflow.md` v1.0 (v3.5.2 Scope C).
- Any change to the senior-envelope format is a contract change to `legal-assistant`'s Phase 7.5 parsing — bump both files in lock-step.
