# NDA Signing Authority Matrix

Decision framework for determining who can sign an NDA and what action to take, based on two dimensions: the NDA's risk level and the deal's commercial context.

---

## 1. Risk Level Determination

After completing the NDA Review Checklist and Three-Layer Analysis, aggregate the per-clause RAG scores into an overall risk level:

| Risk Level | Criteria | Description |
|---|---|---|
| **STANDARD** | All Green, maximum 2 minor Amber (both tagged ACCEPT) | Clean NDA with market-standard terms. No action items. |
| **ELEVATED** | 3-5 Amber (any priority tag), no Red | Some flags but all within negotiable range. May warrant light redline or awareness note. |
| **HIGH** | Any Red clause, or 6+ Amber | Material issues requiring attention before signing. |
| **UNACCEPTABLE** | Any Critical Red flag (see Section 3), or 3+ Red clauses | Do not sign without resolution. Engage external counsel or reject. |

**Upgrade rules from Three-Layer Analysis:**
- Clause-Interaction Analysis identifies a compound risk → upgrade overall risk by one level
- Devil's Advocate identifies a concern that cannot be dismissed → upgrade overall risk by one level
- Precedent Matching shows DE previously rejected similar terms → flag for consistency

---

## 2. Deal Context Classification

| Context | Classification | Examples |
|---|---|---|
| Neocloud buyer relationship | **High-stakes** | CoreWeave, Lambda, Crusoe, any compute buyer exploring colocation |
| Investor relationship | **High-stakes** | VC, PE, family office, strategic investor during fundraise |
| Grower partnership | **High-stakes** | Greenhouse/land partner for site development |
| M&A context | **High-stakes** | Any NDA for acquisition, merger, or strategic combination |
| Vendor / service provider | **Low-stakes** | Software vendors, consultants, equipment suppliers |
| Standard advisor engagement | **Low-stakes** | Non-strategic advisors, general consultants |
| General commercial exploration | **Low-stakes** | Early-stage discussions without specific deal on the table |

---

## 3. Decision Matrix

### Current Model: Carlos (Sole Signatory)

| Risk Level | Low-Stakes Context | High-Stakes Context |
|---|---|---|
| **STANDARD** | **SIGN.** Present concise summary (3 lines). Carlos confirms. | **SIGN.** Present concise summary (3 lines). Carlos confirms. |
| **ELEVATED** | **SIGN with awareness note.** Present concise summary (5-8 lines) noting Amber items and their priority tags. Carlos confirms. | **Full analysis.** Present complete RAG table, compound risk flags, devil's advocate, precedent context. Carlos decides: sign as-is or light redline. |
| **HIGH** | **REDLINE.** Present full analysis. Generate redlines for all Red items and DEFEND-tagged Ambers. Carlos reviews and approves redline. | **REDLINE + consider external counsel.** Present full analysis with explicit note: "Consider having external counsel review the Red flags before signing." Carlos decides approach. |
| **UNACCEPTABLE** | **REJECT or ESCALATE.** Present full analysis. Recommend: reject the NDA, propose DE's template instead, or engage external counsel. | **REJECT or ESCALATE.** Present full analysis. Do not sign without external counsel review and resolution of all Critical Red flags. |

### Summary of Presentation Depth

| Situation | What Carlos Sees |
|---|---|
| STANDARD (any context) | 3-line summary: "This NDA is clean. [Counterparty], [governing law], mutual. Recommend signing. Confirm?" |
| ELEVATED + low-stakes | 5-8 line summary: risk score, Amber items with ACCEPT/NEGOTIATE tags, recommendation, devil's advocate one-liner. "Confirm?" |
| ELEVATED + high-stakes | Full analysis: RAG table, compound risk flags, devil's advocate section, precedent context, recommended action, redline options |
| HIGH (any context) | Full analysis + generated redlines + cover email draft |
| UNACCEPTABLE (any context) | Full analysis + explicit "do not sign" recommendation + proposed alternative path |

---

## 4. Critical Red Flags

The following findings trigger UNACCEPTABLE regardless of context. These are non-negotiable:

1. **Hidden IP assignment or licence grant.** The NDA purports to assign or licence DE's intellectual property to the counterparty. NDAs should never create IP obligations.

2. **Non-compete or exclusivity not disclosed upfront.** Competitive restrictions buried in NDA terms. These must be in separate commercial agreements with adequate consideration.

3. **Sanctioned or unstable jurisdiction governing law.** Governing law of a jurisdiction subject to international sanctions, or where rule of law is unreliable.

4. **One-way uncapped indemnity without limitation.** DE indemnifies the counterparty for any breach, with no reciprocal obligation and no cap. Disproportionate and unacceptable.

5. **Waiver of injunctive relief rights.** The NDA restricts or waives DE's right to seek interim or injunctive relief from a court. This eliminates DE's primary enforcement mechanism.

6. **Unilateral amendment right.** The counterparty can modify the NDA terms without DE's consent. Fundamentally undermines the agreement.

7. **NDA as gateway to other obligations.** The NDA includes binding commitments beyond confidentiality: exclusivity periods, binding arbitration on commercial disputes, minimum purchase obligations, or similar.

---

## 5. Extensibility: Future Multi-Signer Model

When DE adds team members who handle NDAs, the authority matrix expands:

| Authority Tier | Who | Can Sign |
|---|---|---|
| **Tier 1** | Team member | STANDARD risk + Low-stakes context only |
| **Tier 2** | Senior team member | STANDARD + ELEVATED in any context |
| **Tier 3** | Carlos (CEO) | Full authority across all risk levels and contexts |
| **External counsel** | Law firm | Required for UNACCEPTABLE risk level |

**Delegation rules:**
- Tier 1/2 must use the review workflow. No signing without completing the analysis.
- If Tier 1/2 encounters HIGH or UNACCEPTABLE, it automatically escalates to Tier 3.
- Carlos can delegate specific counterparty NDAs to Tier 2 on a case-by-case basis ("you can sign the [Counterparty] NDA if it scores ELEVATED or below").
- All decisions are logged in the review log regardless of who signs.

---

## 6. Escalation Protocol

When escalation to external counsel is recommended:

1. **Prepare a brief:** NDA document + RAG assessment table + specific Red/Critical flags + DE's preferred positions on each flagged item.
2. **State the question clearly:** "We need external counsel to review clauses [x, y, z] and advise whether DE's proposed redlines are appropriate, or whether alternative approaches exist."
3. **Set a deadline:** External counsel review should not exceed 48 hours for NDA-level issues.
4. **Cost awareness:** NDA reviews should be fixed-fee or capped. Do not accept open-ended engagement for NDA review.

---

## 7. Leverage Modifier

The counterparty risk categorization (nda-policy-positions.md Section 10) determines DE's leverage position. This modifier adjusts how the review workflow applies DEFEND/NEGOTIATE/ACCEPT priorities.

### When Counterparty Has Leverage (DE has NO leverage)

DE needs this relationship more than they need DE. Examples: large neocloud buyer, institutional investor, major strategic partner.

| Adjustment | Effect |
|---|---|
| NEGOTIATE items on market-standard clauses | Downgrade to ACCEPT. Don't waste capital on low-yield asks. |
| DEFEND items | Unchanged. Material risk exists regardless of leverage. |
| Maximum redline points per round | 2 (instead of 3-4). Every ask costs political capital. |
| Cover email tone | More appreciative. Lead with thanks. Frame asks as "minor." |
| Template battle | Do not push DE's template. Accept their paper immediately. |

**Exception:** NEGOTIATE items that are DE company policy (e.g., "indemnity basis" → "reasonable costs") remain NEGOTIATE regardless of leverage. These are low-cost, high-signal asks that demonstrate DE reads the document carefully.

### When Roughly Equal

Neither party is dependent. Mutual interest, similar scale.

| Adjustment | Effect |
|---|---|
| NEGOTIATE items | Apply as standard per policy |
| Maximum redline points | 3-4 per round |
| Cover email tone | Balanced, professional |
| Template battle | Push back once ("we've already sent our NDA"). Accept theirs if they insist. |

### When DE Has Leverage

DE controls access (to growers, sites, pipeline) and counterparty needs DE's assets. Examples: vendor wanting DE's business, advisor seeking engagement, broker needing site access.

| Adjustment | Effect |
|---|---|
| NEGOTIATE items | Keep as NEGOTIATE. Worth asking. |
| Additional asks | Can include 1 "nice-to-have" beyond strict policy (e.g., financing source carve-out, Affiliate assignment). |
| Maximum redline points | 4-5 per round |
| Cover email tone | More direct. Frame asks as "our standard position." |
| Template battle | Push DE's template first. Insist once if they counter. |

---

## 8. Urgency Modifier

When the counterparty intake flags urgency (deadline or blocking situation), the workflow adjusts **presentation only** — never risk assessment.

| Adjustment | Normal Mode | Urgent Mode |
|---|---|---|
| Phase 4 presentation | Risk-appropriate (summary or full) | Skip "show full analysis" option. Go straight to recommendation + decision. |
| Phase 5 timing | Redlines generated after Phase 4 approval | Pre-generate redlines alongside recommendation (one-step approval). |
| Devil's advocate | Full section (2-4 concerns) | 1 sentence summary of strongest concern + dismissal. |
| Review memo flag | — | "Reviewed under time pressure — consider re-reviewing if circumstances change." |

**Hard rule:** Urgency NEVER changes the risk level or the scoring. A RED clause is RED whether the deadline is Friday or next month. Urgency only affects how quickly the recommendation reaches the user.
