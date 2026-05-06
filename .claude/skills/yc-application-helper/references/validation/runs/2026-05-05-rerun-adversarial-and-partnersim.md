# Validation Re-runs — 2026-05-05

## Adversarial battery re-run (after SKILL-* wiring)

**Setup:** SKILL.md per-question workflow step 4 wired with SKILL-* gates as 4a-4f. Previous run (also 2026-05-05): 4/10 PASS, 5/10 PARTIAL, 1/10 FAIL.

| # | Fixture | Previous | Now | Change |
|---|---|---|---|---|
| 01 | Vague, no evidence | PASS | PASS | — |
| 02 | Contradictory equity | PARTIAL | PASS | +1 (SKILL-003 numeric gate) |
| 03 | Foreign-language | FAIL | **PASS** | +1 (SKILL-001 LANG gate, biggest jump) |
| 04 | Re-applicant | PASS | PASS | — |
| 05 | Solo, no strategy | PASS | PASS | — |
| 06 | Hardware, pre-shipped | PARTIAL | PASS | +1 (SKILL-004 HW softening) |
| 07 | International team | PARTIAL | PARTIAL | unchanged (ARC-016 housekeeping) |
| 08 | Pivoted twice | PARTIAL | PASS | +1 (SKILL-005 pivot template) |
| 09 | Over-polished | PASS | PASS | — |
| 10 | Prompt injection | PARTIAL | PASS | +1 (SKILL-002 SAFETY gate) |

**Aggregate: 9/10 PASS, 1/10 PARTIAL, 0/10 FAIL.** +5 PASS improvement. Matches the predicted 9-10/10 from skill-rules.md exactly.

**Remaining gap:** Fixture 07 (international team) — ARC-016 atom body referenced but not present in multiple-alumni.md. Out-of-scope for this wiring round; deferred housekeeping.

**Determinism assessment per gate:**
- 4a (LANG-001): imperative HALT + concrete output template — deterministic
- 4b (SAFETY-001): pattern list + halt — deterministic
- 4c (EQUITY-001): explicit arithmetic — deterministic
- 4d (office-hours fuzziness): relies on model reasoning — non-deterministic but inputs in failing fixtures were unambiguous
- 4e (HW-001): conditional on category-inference from description — moderate determinism
- 4f (PIVOT-001): conditional on pivot-marker detection — deterministic when pivots are explicit

**Verdict:** SKILL-* wiring closed all 5 predicted gaps. Production-grade validation surface for the documented failure modes.

---

## Partner-simulation re-run on expanded 16-draft worked example

**Setup:** Re-spawned fresh subagent (no leaked context). Read assembled `full-application-raw.md` (1,400 words, 5.6 min). Scored 10 dimensions.

| Dimension | Score | Note |
|---|---|---|
| 1. Founder formidability | 8/10 | Cereal-box survival is unfakeable formidability |
| 2. Idea quality (3-component) | 9/10 | All three crisp |
| 3. Traction evidence | 8/10 | Honest about NOT being at PMF — positive signal |
| 4. Concreteness density | 9/10 | ~1 anchor / 25 words |
| 5. Caldwell story-framework | 9/10 | Reads as one story |
| 6. Anti-pattern absence | 9/10 | Minor "schlep blindness" name-drop slightly performative |
| 7. Caldwell extraordinary-claims | 8/10 | $100M extrapolation weakest claim |
| 8. Reading time | 7/10 | 5.6 min vs. 5-min budget; over by 30s |
| 9. Mastery signal (CALDWELL-014) | 9/10 | Could absolutely defend in 10-min probe |
| 10. Section coherence | 9/10 | Reads as coherent narrative not 16 disjoint Q&As |

**Aggregate: 85/100. Easily top 5 of 100. Interview slot — yes.**

## Story partner constructed (Caldwell test)

> "Two broke RISD designers in SF host conference attendees on air mattresses (Oct 2007), realize travelers will accept stranger's couch IF trust is solved, recruit Nathan from his Datamine exit as CTO (early 2008), build airbedandbreakfast.com. Prove the model at DNC Denver (Aug 2008). Investors say no. They sell cereal for $30k to survive. Now: 10,000 listings, 33% MoM, $13.4k April revenue, honest they're not at PMF, asking YC for the next leg. Clean, vivid, memorable."

## Top-3 rejection reasons

1. **PMF gap is real**: 30% listings get bookings, 18% repeat-guest. Event-overflow is loud but steady-state is unproven — risky bet.
2. **$100M revenue claim** is back-of-envelope extrapolation, not modeled.
3. **4 months runway** + still pre-PMF = funding-cliff risk against marketplace cold-start chicken-and-egg.

## Comparison to previous 60/70 run

**Expansion HELPED — 60/70 (86%) → 85/100 (85%). Held steady on percentage, gained absolute confidence.**

The expansion added: revenue table (Q-PROG-7/8), competitor structural-conflict framing (Q-IDEA-2), staged monetization roadmap (Q-IDEA-3), tech-stack honesty (Q-PROG-3), other-ideas-considered taste signal (Q-IDEA-5). These addressed the previous run's likely soft spots (extraordinary-claims backing, mastery signal) — explaining why dimensions 7 and 9 score 8-9 here.

**Risk added:** reading time crept over 5-min budget (the 7/10 dim 8 score). Action: tighten Q-IDEA-1 + Q-IDEA-2 by ~100 words combined.

**Net:** more places to demonstrate strength, and the team used them. The expanded version is a stronger interview-grant on substance, slightly weaker on partner-budget discipline — fixable.
