# End-to-End Skill Test — DEC Facts File — 2026-05-05

**Setup:** Fresh subagent (no leaked context) simulated end-user invocation of yc-application-helper on `/Users/crmg/Claude/yc-applications/digital-energy/company-facts.md`. Pre-draft helper scripts pre-run; agent applied the skill's per-question workflow to produce v-raw drafts for 3 high-leverage questions.

## Pre-draft gate results (deterministic scripts, run on DEC facts)

| Gate | Result |
|---|---|
| LANG-001 (check_language.py) | PASS — 19% English-density (threshold 15%) |
| SAFETY-001 (check_safety.py) | PASS — no injection patterns |
| EQUITY-001 (check_equity.py) | INFO — equity fields are [GAP]-marked; founders must close before submission |
| Office-hours fuzziness gate (4d) | 2 [FUZZY] flags — demand reality + desperate specificity (no named user love-evidence) |
| HW-001 category check (4e) | Partial — DEC is hybrid (compute + energy); Q-CO-4 demo expectation softens to KWAKEL-01 site photo / CAD render / Blockheating evidence as substitutes |
| PIVOT-001 check (4f) | N/A — no explicit pivot history |

## Drafts produced

### Q-CO-2 (50-char description) — 3 candidates

| # | Candidate | Chars | Score |
|---|---|---|---|
| 1 | "AI compute centers that produce energy, not use it." | 51 | 6/10 (over by 1) |
| 2 | **"Modular AI data centers that heat greenhouses."** | **47** | **8/10 (recommended)** |
| 3 | "Edge AI factories with free heat for growers." | 46 | 7/10 |

**Verdict:** Submission-ready (Candidate 2).

### Q-IDEA-1 (Why this idea / domain expertise / how do you know people need it)

~300 words. Atoms applied: HALE-001 3-component frame, PG-001 schlep, PG-004 live-in-future, ALTMAN-003 incumbent structural conflict, PG-002 schlep-as-moat.

**[GAP] flags surfaced (5):**
- Carlos's specific named distributed-compute project + scale
- Jonathan's specific named "500MW+ DC deployment" project + dates
- Co's named EUR 2B+ PPA deal credibility anchor
- Named greenhouse partner with binding evidence (current 14-sites + 3 GW LOI is option/HoT/non-binding)
- At least one named user reaction quote

**Gate verdict:** PARTIAL — concreteness on why-now but founder-credibility FAIL on 3 of 4 founders.

### Q-IDEA-2 (Competitors / what you understand others don't)

~340 words. Atoms applied: HALE-001 insight, PG-002 schlep-as-moat, ALTMAN-003 structural conflict, ANTI-004 paradigm-not-feature.

**[GAP] flags surfaced (4):**
- Evidence any hyperscaler / Equinix / Crusoe rep has been asked and declined (structural conflict is currently thesis, not tested observation)
- Verified DSCR math under cable-pooling stack (1.2x → 1.4-1.6x asserted, not modeled in facts)
- Quote from competitor's customer who churned to DEC OR named greenhouse who chose DEC over CHP/geothermal
- First-principles comparator MWh prices for gas CHPs in NL (insight rests on this comparison being grounded)

**Gate verdict:** PARTIAL — strongest insight in the application, but partly thesis. Concreteness PARTIAL.

## Aggregate result

**Total [GAP] flags: 9 (0 + 5 + 4) across 3 drafts.**

**Top 3 highest-leverage gaps:**
1. Per-founder named achievements (Carlos, Jonathan, Co — Jelmer alone passes PG-012) — closing this lifts Q-IDEA-1 + 4 per-founder profile P-ACC-2 questions simultaneously
2. One named greenhouse partner with binding-or-near-binding evidence + direct quote — converts traction narrative from thesis to fact; touches Q-IDEA-1, Q-IDEA-2, Q-PROG-5/6, Q-CO-4
3. Comparator gas CHP / geothermal €/MWh numbers — Q-IDEA-2's central insight rests on this comparison being grounded; without numbers a partner can dismiss the moat as hand-wave

## Verdict: NOT submission-ready

Blockers:
- Q-IDEA-1 fails founder-credibility gate on 3 of 4 founders
- Q-IDEA-2 needs grounding on incumbent structural conflict + comparator prices
- 0 paying tenants + 0 binding offtake + ~3 GW LOI self-flagged as marketing-claim → Q-PROG-5/6 will fail ANTI-010 unless a named binding partner closes before submission

Q-CO-2 candidate 2 is submission-ready as-is.

Estimated work to reach partner-readable threshold: 1-2 days of founder input on 3 leverage gaps.

## Skeptical-lens self-assessment from agent

> "The skill operated within scope. It did not overcompensate for missing facts. The gate report would force the founder back to the facts file before submission — which is the correct outcome.
>
> The draft for Q-IDEA-1 looks ~80% complete and reads well, but it is load-bearing on facts that don't yet exist (Carlos's distributed compute scale, Jonathan's 500MW DC, Co's EUR 2B PPA). A founder reading the draft might mistake 'looks good' for 'submission-ready' — which is exactly the failure mode the skill exists to prevent. The [GAP] flags are doing real work here."

## What this run validates

- Skill produces useful drafts where facts are strong (insight + why-now sections flowed directly from the pitch narrative v3.2 work)
- Skill correctly flags gaps where facts are weak — anti-fabrication discipline held end-to-end
- Skill operates within scope: did not overcompensate for missing facts, did not invent founder achievements, did not invent partner names, did not invent comparator prices
- Gate report would force the founder back to the facts file — which is the correct outcome
- 50-char description (Q-CO-2) is the most submission-ready output without caveat
- Q-IDEA-2 is the most insight-dense draft in the application but needs grounding
- Pre-revenue + 0 binding + LOI-as-marketing-claim is workable IF named binding partner closes before submission

## Lessons for skill v1.1

1. The skill's "[GAP] flag honesty" is its load-bearing safety mechanism — the test confirmed it fires correctly under partial-information conditions
2. Hybrid companies (software + hardware + infrastructure like DEC) trigger HW-001 only partially — may benefit from a HW-002 or HYBRID-001 atom for category-spanning cases
3. The output `[GAP]` flag count is itself a useful submission-readiness metric — "≤2 [GAP] flags across all drafts" could be a Phase 6 gate
4. Q-IDEA-2 came out as the strongest draft (per the agent), suggesting paradigm-not-feature framing under structural-conflict atoms is the highest-yield section for facts files that have done the strategic positioning work
