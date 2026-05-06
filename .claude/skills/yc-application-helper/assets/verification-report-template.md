---
title: "Verification Report Output Template"
domain: SKILL
status: active
---

# Verification Report — [Company Name] YC Application

**Generated:** [timestamp]
**Skill version:** yc-application-helper v1.0
**Corpus snapshot:** 2026-05-04
**Facts file:** [path]

---

## Submission readiness

**Status:** READY / NOT READY / READY WITH CAVEATS

[If NOT READY, list blocking issues at top.]

---

## Per-question gate results

| Question | Limit | Drafted? | Concreteness | Founder-cred | Brevity | Anti-pattern | Fabrication | Nuance | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Q-CO-2 | 50 chars | ✓/✗ | ✓/✗ | n/a | ✓/✗ | clean / ANTI-014 (platform) | ✓ | ✓ | PASS / FAIL |
| Q-CO-7 | — | ... | | | | | | | |
| Q-FOUND-2 | — | | | | | | | | |
| Q-FOUND-3 | — | | | | | | | | |
| Q-VIDEO-1 (script) | 150 words | | | | | | | | |
| Q-PROG-1 | — | | | | | | | | |
| Q-PROG-2 | — | | | | | | | | |
| Q-PROG-3 | — | | | | | | | | |
| Q-PROG-4 (coding agent) | optional | | | | | | | | |
| Q-PROG-5/6 | — | | | | | | | | |
| Q-PROG-7/8 | — | | | | | | | | |
| Q-PROG-9 | — | | | | | | | | |
| Q-PROG-11 | — | | | | | | | | |
| Q-PROG-12 | — | | | | | | | | |
| Q-IDEA-1 | — | | | | | | | | |
| Q-IDEA-2 | — | | | | | | | | |
| Q-IDEA-3 | — | | | | | | | | |
| Q-IDEA-4 | dropdown | | | | | | | | |
| Q-IDEA-5 | — | | | | | | | | |
| Q-EQ-1 to Q-EQ-11 | factual | | | | | | | | |
| Q-CUR-1/2 | — | | | | | | | | |

---

## Per-founder profile gate results

For each founder:

### [Founder Name]
- P-ROLE-3 (technical?): [Yes/No] — team has ≥1 Yes? [Yes/No]
- P-ROLE-5 (commit Yes?): [Yes/No]
- Work history ≥1 entry: [Yes/No]
- P-ACC-1 has resourcefulness signal: [Yes/No]
- P-ACC-2 passes hard gate: [Yes/No] — [if No, list reasons]
- P-ACC-3 has ≥1 URL: [Yes/No]
- LinkedIn URL: [Yes/No]
- Profile complete: [Yes/No]

---

## Anti-pattern detection summary

[Each ANTI- atom triggered by any draft, with location:]
- [atom: ANTI-014] "platform" detected in Q-CO-2 line N
- [atom: ANTI-005] hedge "we believe" detected in Q-IDEA-1 line N
- [...]

---

## Anti-fabrication audit

[Every factual claim and its trace to facts file:]
- "$120K MRR" in Q-PROG-7 → [fact: company-facts.md#traction-revenue]
- "5 paying customers" in Q-PROG-6 → [fact: company-facts.md#customers]
- [Any claim that doesn't trace = FABRICATION FLAG]

---

## Open gaps (must close before submission)

- [ ] [Gap description] — [needs X from Y by date]
- [...]

---

## Submission timing

- **Target deadline:** [date]
- **Days until deadline:** [N]
- **Realistic gap-closure timeline:** [N days / not blocking]

---

## Partner-simulation results (Phase 5C — if invoked)

[Fresh subagent role-played as YC partner reading the application. Top 3 reasons they would reject:]
1. [reason]
2. [reason]
3. [reason]

[Rebuttal / addressed in current draft? Yes/No per item.]

---

## Recommended pre-submit actions (priority order)

1. [Highest-leverage action]
2. [Next]
3. [...]
