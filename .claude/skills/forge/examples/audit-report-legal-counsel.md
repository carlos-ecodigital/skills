# Example Audit Report: legal-counsel (Score: 94)

> This is an example of a forge W3 audit for the highest-scoring skill in the ecosystem.
> Use as a reference for what an A-grade audit report looks like.

## Skill Audit: legal-counsel

**Date:** 2026-02-19
**Audited by:** forge
**Skill type:** Matrix Composer

## Score Summary

| Category | Weight | Score (0-10) | Weighted |
|----------|--------|-------------|----------|
| Domain Depth | 20% | 10 | 20.0 |
| Workflow Clarity | 12% | 9 | 10.8 |
| Integration Design | 12% | 9 | 10.8 |
| Context Engineering | 10% | 10 | 10.0 |
| Tool Design Quality | 10% | 8 | 8.0 |
| Eval Scaffolding | 10% | 8 | 8.0 |
| Scope Boundaries | 8% | 10 | 8.0 |
| Trigger Coverage | 8% | 10 | 8.0 |
| Anti-Pattern Guards | 5% | 9 | 4.5 |
| Reference File Ratio | 5% | 10 | 5.0 |
| **TOTAL** | **100%** | | **93.1** |

**Grade: A**

## Strengths

- **Matrix Composition (10/10 Context Engineering):** 10 specializations × 4 jurisdictions with clean loading rules. Each request loads only the relevant specialization + jurisdiction files, keeping context lean. This is the gold standard for progressive disclosure.
- **Domain Depth (10/10):** Reference files contain specific statute citations, case law references, regulatory framework details, and template clauses. A practicing lawyer would find this useful, not generic.
- **Scope Boundaries (10/10):** Crystal clear "What You Own" (10 legal specializations) and "What You Do NOT Own" (ops coordination, financial modeling, content writing). Every boundary points to the correct alternative skill.
- **Trigger Coverage (10/10):** Description is 800+ characters covering 30+ legal document types, legal questions, and advisory scenarios. Routing catches virtually every legal-related user request.
- **Reference File Ratio (10/10):** SKILL.md is ~120 lines of pure orchestration. All legal knowledge lives in `core/`, `specializations/`, and `jurisdictions/` directories. Perfect 75/25 split.

## Gaps

| Gap | Category | Impact | Effort | Priority |
|-----|----------|--------|--------|----------|
| No MCP integration documented | Tool Design Quality | M | L | 1 |
| Eval scenarios not shipped with skill | Eval Scaffolding | M | M | 2 |
| No explicit anti-patterns section (embedded in general principles) | Anti-Pattern Guards | L | L | 3 |

## Upgrade Plan

1. **Add MCP integration patterns (Tool Design Quality → +1):** Document how legal-counsel interacts with HubSpot (via ops-dealops) for deal-related legal work and Google Drive (via ops-dataroomops) for data room documents. Add `allowed-tools` with relevant MCP declarations.
2. **Add eval scenarios (Eval Scaffolding → +1):** Create 5 test scenarios: (a) NDA drafting for NL jurisdiction, (b) SHA review for corporate/M&A, (c) scope boundary test (financial question → defer to project-financing), (d) multi-jurisdiction request (NL + UK), (e) edge case with overlapping specializations.
3. **Extract anti-patterns to explicit section (Anti-Pattern Guards → +0.5):** Move the embedded "do not" rules from general principles into a dedicated Anti-Patterns section for visibility.

## Integration Opportunities

- **ops-dataroomops:** legal-counsel produces documents that feed directly into the data room. Should add explicit handoff: "after drafting [document], suggest user file via ops-dataroomops."
- **ops-dealops:** Legal milestones (LOI signed, SHA executed) should trigger ops-dealops deal stage updates. Add routing: "when a legal document is finalized, suggest updating the deal stage."

## Why This Is Gold Standard

This skill demonstrates what great looks like:
1. **Combinatorial expertise handled elegantly:** The matrix composition pattern (specialization × jurisdiction) scales without bloating context. Adding a new jurisdiction means adding one directory, not rewriting SKILL.md.
2. **Knowledge density:** Reference files aren't summaries — they're practitioner-level knowledge with specific citations that would pass peer review.
3. **Clean boundaries:** No scope creep. Legal-counsel never tries to do financial modeling (project-financing) or ops coordination (ops-dealops). It knows its lane.
