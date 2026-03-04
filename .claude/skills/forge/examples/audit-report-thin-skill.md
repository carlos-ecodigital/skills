# Example Audit Report: Thin Skill (Score: 58)

> This is an example of a forge W3 audit for a skill that needs significant work.
> Use as a reference for what a D-grade audit looks like and how to produce an upgrade plan.
> Note: This is a hypothetical example for illustration, not a real skill audit.

## Skill Audit: example-thin-skill

**Date:** 2026-02-19
**Audited by:** forge
**Skill type:** Domain Executor

## Score Summary

| Category | Weight | Score (0-10) | Weighted |
|----------|--------|-------------|----------|
| Domain Depth | 20% | 4 | 8.0 |
| Workflow Clarity | 12% | 6 | 7.2 |
| Integration Design | 12% | 3 | 3.6 |
| Context Engineering | 10% | 7 | 7.0 |
| Tool Design Quality | 10% | 5 | 5.0 |
| Eval Scaffolding | 10% | 0 | 0.0 |
| Scope Boundaries | 8% | 6 | 4.8 |
| Trigger Coverage | 8% | 7 | 5.6 |
| Anti-Pattern Guards | 5% | 3 | 1.5 |
| Reference File Ratio | 5% | 4 | 2.0 |
| **TOTAL** | **100%** | | **44.7** |

**Grade: D — Needs rebuild or major upgrade**

## Strengths

- **Context Engineering (7/10):** SKILL.md is appropriately sized (~150 lines). Some separation between instructions and references exists.
- **Trigger Coverage (7/10):** Description has 8 trigger phrases covering the main use cases. Could add more domain terms.
- **Workflow Clarity (6/10):** Two workflows defined with basic intake → output structure. Missing quality gates.

## Gaps

| Gap | Category | Impact | Effort | Priority |
|-----|----------|--------|--------|----------|
| Reference files contain only generic knowledge | Domain Depth | H | H | 1 |
| No eval scenarios | Eval Scaffolding | H | M | 2 |
| No integration table or cross-references | Integration Design | H | L | 3 |
| Reference files are thin (<30 lines each) | Reference File Ratio | M | M | 4 |
| No anti-patterns section | Anti-Pattern Guards | M | L | 5 |
| Tools declared but no usage patterns documented | Tool Design Quality | M | M | 6 |
| Scope defined but non-scope missing | Scope Boundaries | L | L | 7 |

## Detailed Gap Analysis

### Domain Depth (4/10) — Critical
The reference files exist but contain textbook-level information:
- `references/overview.md` (28 lines) — generic overview that could be found in any introduction
- `references/frameworks.md` (42 lines) — lists framework names without specific data, benchmarks, or decision criteria
- **Missing:** Named sources, specific numbers, comparison matrices, decision frameworks with conditions, real-world examples

**Fix:** Replace each reference file with practitioner-grade content. Add specific numbers, named standards, benchmarks from real sources. Aim for 100-200 lines per reference file. Add at least 2 new reference files covering the core domain knowledge gaps.

### Eval Scaffolding (0/10) — Critical
No test scenarios exist. No way to verify the skill works or has regressed.

**Fix:** Create 3-5 test scenarios per `eval-scaffolding.md` template. Include at least: (1) happy path for main workflow, (2) edge case with ambiguous input, (3) scope boundary test (should defer to another skill).

### Integration Design (3/10) — High Impact
The skill mentions two other skills by name but has no routing table, no handoff triggers, and no cross-references from other skills back to this one.

**Fix:** Add an Integration table. Verify that the skills referenced also reference this skill back (bidirectional). Define specific trigger conditions for handoffs.

## Upgrade Plan (Priority Order)

| # | Action | Category Impact | Effort | Estimated Score Gain |
|---|--------|----------------|--------|---------------------|
| 1 | Rewrite reference files with practitioner-grade depth | Domain Depth +4 | 2 hours | +8.0 |
| 2 | Create 4 eval scenarios | Eval Scaffolding +8 | 30 min | +8.0 |
| 3 | Add integration table + verify cross-references | Integration Design +5 | 20 min | +6.0 |
| 4 | Add "What You Do NOT Own" section | Scope Boundaries +2 | 10 min | +1.6 |
| 5 | Add anti-patterns section (3-5 items) | Anti-Pattern Guards +4 | 15 min | +2.0 |
| 6 | Document tool usage patterns with examples | Tool Design Quality +3 | 20 min | +3.0 |
| **Total** | | | **~3.5 hours** | **+28.6 (→ ~73)** |

**Post-upgrade projected score: ~73 (Grade C, approaching B)**

To reach Grade B (≥75), would additionally need:
- 2 more reference files with specific data tables (+2 Domain Depth → +4.0)
- 1 more eval scenario covering failure mode (+1 Eval Scaffolding → +1.0)

## Anti-Pattern Flags

| Anti-Pattern | Detected? | Details |
|-------------|-----------|---------|
| AP-1: Premature Complexity | No | Appropriate single-agent pattern |
| AP-4: Missing Evaluation | **Yes** | Zero eval scenarios |
| AP-6: Context Rot | No | Sizes are appropriate |
| AP-11: Vague Instructions | **Yes** | "Analyze thoroughly" without criteria |
| AP-15: Scope Creep | **Partial** | Non-scope not documented |
| AP-16: Orphan Skill | **Yes** | Not referenced by any ops orchestrator |

## Recommendation

**Do not use this skill in production until upgraded to ≥75.** The thin reference files mean outputs will be generic rather than expert-level. The missing eval scenarios mean regressions will go undetected. Priority 1 and 2 fixes (reference rewrite + eval scenarios) address 55% of the score gap and should be done first.
