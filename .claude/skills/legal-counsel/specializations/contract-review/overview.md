# Contract Review Specialization

## Purpose

Review, analyse, and advise on counterparty-drafted agreements. The inverse of contract-drafting: where drafting creates DE's paper, contract-review scores and responds to other parties' paper.

Current scope: NDAs. Future scope: service agreements, SPAs, JV agreements, and other document types as review workflows are built.

**This is not legal advice.** It is a structured analytical workflow applying DE's codified commercial preferences and risk tolerances. For high-stakes or novel situations, engage qualified external counsel.

---

## File Index

| File | Purpose | Lines |
|---|---|---|
| `overview.md` | This file. Specialization metadata and index. | ~80 |
| `nda-policy-positions.md` | DE's company-specific NDA policy: principles, judgement framework (DEFEND/NEGOTIATE/ACCEPT + Three-Layer Analysis), governing law, CI, NC, indemnity, return/destruction, unusual clauses, specified information. | ~280 |
| `nda-review-checklist.md` | 25-item NDA review checklist. Each item scored GREEN/AMBER/RED with default DEFEND/NEGOTIATE/ACCEPT priority. | ~240 |
| `authority-matrix.md` | Decision framework: risk level (STANDARD/ELEVATED/HIGH/UNACCEPTABLE) x deal context (low-stakes/high-stakes). Determines signing authority, presentation depth, and escalation path. | ~110 |
| `redline-playbook.md` | 15 pre-drafted redlines with preferred language, fallback, walk-away, and tone guidance. Plus cover email templates. | ~310 |
| `nda-review-workflow.md` | 7-phase NDA review process tying all files together. Intake, structural scan, three-layer analysis, recommendation, redline generation, negotiation tracking, pre-signature verification. | ~340 |
| `review-log-template.md` | Template for review memos saved after each NDA review. Institutional memory for precedent matching. | ~120 |

---

## Workflow Summary

1. **Intake:** Read document, ask deal context, classify stakes
2. **Structural Scan:** Map clauses against DE's NDA structure
3. **Three-Layer Analysis:** RAG scoring + clause interaction + devil's advocate + precedent matching
4. **Recommendation:** Context-adaptive presentation (3-line summary to full analysis)
5. **Redline:** Draft changes from playbook, generate cover email
6. **Negotiation:** Track counterparty responses, recommend next steps
7. **Pre-Signature:** Verify all checks, save review memo, prompt CRM update

---

## Integration with Other Specializations

| Specialization | Relationship |
|---|---|
| **contract-drafting** | DE's NDA template (from contract-drafting) serves as the benchmark. Review checklist items map to template sections. |
| **core (clause-library)** | Redline preferred language draws from the clause library for consistency. |
| **jurisdictions** | Governing law analysis references jurisdiction-specific rules (UK, NL, NO, CH, US). |
| **energy-project-finance** | NDA reviews for project finance deals may require additional sector-specific checks. |

---

## Key Design Principles

1. **AI does the work, Carlos makes the decision.** The workflow produces a complete analysis and recommendation. The user sees a summary calibrated to the stakes and decides.
2. **Minimal redlines, clear boundaries.** Per the Golden Rule: redline only what matters, accept everything else. Maximum 3-4 points per round.
3. **Speed is a competitive advantage.** The workflow targets 48-hour turnaround. AI analysis eliminates the bottleneck; the human decision is the only gate.
4. **Institutional memory.** Every review is logged. Precedent matching improves consistency and captures Carlos's actual judgement over time.
5. **Not legal advice.** This is a commercial decision-support tool. External counsel for UNACCEPTABLE risk or novel situations.

---

## Review Log Location

All completed review memos are saved to:
`/Users/crmg/Documents/DE Claude/legal/nda-reviews/`

File naming: `[YYYY-MM-DD]-[counterparty-name].md`

---

## Future Extensions

- **Service agreement review workflow** (post-NDA, higher complexity)
- **SPA/SHA review workflow** (M&A context)
- **Lease/licence review** (site agreements)
- **Automated registry checks** (Companies House API, KvK, Brønnøysund)
- **HubSpot integration** (auto-update deal records on review completion)
