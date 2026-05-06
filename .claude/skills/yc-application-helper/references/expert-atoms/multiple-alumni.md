# Multiple-Alumni / Named-Source Atoms (v2 — re-extracted with causal-chain protocol)

**Source:** archive/arc-31-application-tips.md (named primary sources distilled by Arc.dev)
**v2 changes:** All 9 atoms upgraded with explicit causal chains in `why_it_exists` and `underlying_model`.
**Atom prefix:** ARC-

**Atom count:** 9.

---

## ARC-001 — The 5-Minute Time Budget (Jason Shen, Ridejoy)

```yaml
atom_id: ARC-001
source: archive/arc-31-application-tips.md (Shen quote)
expert: Jason Shen, co-founder Ridejoy (YC alum)
applies_to_questions: [ALL — sets brevity budget for whole application]
rule_type: constraint (operational)
confidence: high (alumni-stated, partner-corroborated)
when_applies: Universal. Sets the brevity gate threshold.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) partners review 70-100 applications per day. (2) The cognitive budget per app is bounded by total daily attention divided by app count. (3) Shen's empirical figure: ~5 min per partner per app. (4) Therefore brevity isn't a stylistic preference; it's the only way the work gets done at scale. (5) Applications that exceed the budget either get skimmed (losing partner attention before key claims land) or get cut short (later sections unread). (6) Either failure mode reduces the application's effective signal.
underlying_model: Information density per word is the binding constraint. Long applications don't get rejected for being long; they get rejected for losing partner attention before the load-bearing signals land.
contradicts: none
```

> "Each app gets about 5 minutes of each partner's time on average."

**Application implication:** Skill brevity gate enforces total read time ≤ 3 minutes (leaves partner buffer + interrupts).

---

## ARC-005 — Excellence Not Perfection (Paul Buchheit, creator of Gmail)

```yaml
atom_id: ARC-005
source: archive/arc-31-application-tips.md (Buchheit quote)
expert: Paul Buchheit, ex-YC partner, creator of Gmail
applies_to_questions: [meta — application iteration]
rule_type: heuristic (anti-paralysis)
confidence: high
when_applies: When founders are trapped in iterative polishing of submitted text.
when_does_not_apply: When the draft genuinely fails substance gates — polish more then.
why_it_exists: Causal chain — (1) polishing has diminishing returns past a clarity threshold. (2) Applications that miss deadlines because of polishing-paralysis don't get evaluated at all. (3) Therefore "good enough submitted" beats "perfect never-submitted." (4) Buchheit's framing: perfectionism actively prevents progress, regardless of intent. (5) Founders who internalize this ship; founders who don't stay in editing mode past the point of useful improvement.
underlying_model: Submission > non-submission. Polishing past the substance gate adds zero value but costs deadline risk. Skill v-raw should be submission-grade; v-polished is optional.
contradicts: PG-009 (clarity = comprehension gate) at apparent surface — actually complementary: clarity must pass; polishing past clarity is the wasted effort.
```

> "Perfectionism is a disease. It stops progress and drives us crazy."

**Application implication:** Skill does NOT require v-polished for submission. v-raw with passing gates is shippable. User chooses whether to polish.

---

## ARC-013 — Show What You've Done

```yaml
atom_id: ARC-013
source: archive/arc-31-application-tips.md (aggregated alumni)
expert: aggregated alumni
applies_to_questions: [Q-FOUND-1, P-ACC-2, P-ACC-3]
rule_type: rule (evidence-led founder bios)
confidence: high
when_applies: Founder bios + things-built sections.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) adjectives ("driven, resourceful, formidable") are claims, not evidence. (2) Specific shipped projects ARE evidence — they constitute the behavioral history that produced founder traits. (3) Partners read claims as noise (anyone can claim adjectives) and read shipped work as signal. (4) Therefore evidence-led bios pattern-match positively; adjective-led bios pattern-match negatively (founder is performing rather than describing). (5) The mechanism is signal-detection: claims have no information density; named projects have high density.
underlying_model: Evidence-led writing is the canonical founder-credibility register. Showing > telling, where "showing" means specific named projects with named scale and named outcomes.
contradicts: none; reinforces ALTMAN-004, PG-010, PG-012.
```

> "Showcase individual and team accomplishments; highlight complementary strengths."

**Application implication:** P-ACC-3 (things you've built) MUST include concrete URLs to GitHub, deployed apps, published essays, talks, or named projects.

---

## ARC-019 — Metric Priority Order (David Chen, Strikingly)

```yaml
atom_id: ARC-019
source: archive/arc-31-application-tips.md (Chen quote)
expert: David Chen, co-founder Strikingly (YC alum)
applies_to_questions: [Q-PROG-5/6, Q-PROG-7/8, Q-IDEA-3]
rule_type: rule (priority — partners' implicit ranking)
confidence: high
when_applies: Traction questions. Choose the highest-priority metric you can honestly cite.
when_does_not_apply: Pre-launch where no metrics exist — fall back to LOIs (ALTMAN-007).
why_it_exists: Causal chain — (1) different metrics measure different aspects of business viability. (2) Profit > revenue because profit captures cost-discipline, not just demand. (3) Revenue > usage because revenue captures willingness-to-pay, not just willingness-to-try. (4) Usage > users because usage captures engagement, not just sign-up. (5) Users > audience because users actually consume the product, not just follow it. (6) Therefore each tier substitutes for the one above when higher isn't available, but doesn't replace it. (7) Audience-only claims signal "we have followers but no engaged users" — partners discount accordingly.
underlying_model: Tier-substitution hierarchy. Honestly cite the highest tier you have; don't dress lower-tier metrics as higher-tier (e.g., calling sign-up audience "users" or calling free pilots "revenue").
contradicts: none.
```

> Priority: profit > revenue > usage > users > audience.

**Application implication:** Q-PROG-5/6/7/8 lead with highest-tier metric available. Anti-pattern: "10,000 sign-ups" when monthly active is 50; partners discount sign-ups when active is hidden.

---

## ARC-021 — Specificity Over Generic (Jason Chen, Ridejoy)

```yaml
atom_id: ARC-021
source: archive/arc-31-application-tips.md (Chen quote)
expert: Jason Chen, co-founder Ridejoy
applies_to_questions: [Q-CO-7, Q-IDEA-1]
rule_type: rule (memorability + signal density)
confidence: high
when_applies: Product-description and idea sections.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) generic descriptions ("we help businesses succeed", "we leverage AI to") apply to thousands of applications equally. (2) Partners reading 100 apps/day need to differentiate them — generic descriptions don't differentiate. (3) Specific descriptions (named user, named verb, named scale) DO differentiate because the specifics are unique to the application. (4) Therefore specificity = memorability AND signal density. (5) Generic descriptions are equivalent to "this could be any startup" — which provides zero information about which startup THIS is.
underlying_model: Specificity is information density. Generic claims have zero information; specific anchors (name, number, date) have high information. Partners optimize for information density per word.
contradicts: none.
```

> "Be specific about the problem you are trying to solve."

**Application implication:** Skill concreteness gate: every claim has a specific anchor (name, number, date). Generic claims = revise.

---

## ARC-022 — Name the Flaws

```yaml
atom_id: ARC-022
source: archive/arc-31-application-tips.md (aggregated alumni)
expert: aggregated alumni
applies_to_questions: [Q-IDEA-2, Q-CO-7, Q-PROG-1]
rule_type: rule (counterintuitive — preemptive transparency)
confidence: high
when_applies: Product / idea / progress sections.
when_does_not_apply: Never; this is universal.
why_it_exists: Causal chain — (1) every product has flaws — these flaws are real and findable via diligence. (2) Concealment requires partners to discover flaws independently. (3) Discovery surprise damages trust ("they didn't know about this OR they hid it — both are bad signals"). (4) Founder-acknowledged flaws preempt the surprise: partners learn the flaw with the founder's framing already attached. (5) Therefore concealment is net-negative: flaws surface anyway, and concealment removes the founder's narrative-control opportunity (corroborates PG-011b).
underlying_model: Information asymmetry tactic. Founder-framed disclosure controls the framing; concealment lets partners construct the framing. Same logic as PG-011 / PG-011b applied to product flaws.
contradicts: none; corroborates PG-011, PG-011b.
```

> "Identify weaknesses and preliminary solutions; address counterarguments proactively."

**Application implication:** Skill encourages Q-IDEA-2 to acknowledge competitor strengths before naming differentiation. Q-CO-7 to acknowledge product limitations before describing roadmap.

---

## ARC-025 — Numbers Stick (Paul Graham, "How to Present to Investors")

```yaml
atom_id: ARC-025
source: archive/arc-31-application-tips.md (PG quote)
expert: Paul Graham
applies_to_questions: [Q-PROG-7/8, Q-IDEA-3, Q-PROG-5/6]
rule_type: rule (memory + compression)
confidence: high
when_applies: Any section that can be quantified.
when_does_not_apply: Soft questions where numbers don't apply (e.g., Q-CUR-1).
why_it_exists: Causal chain — (1) human memory privileges concrete > abstract. (2) Numbers are concrete; adjectives are abstract. (3) Partners reading 100 apps/day rely on memory to retain signal between read-time and decision-time. (4) Therefore numbers are partner-readable in a way adjectives are not — they survive the gap between read and decide. (5) BUT: too many numbers create noise. PG's discipline: 4-5 numbers per section. (6) The constraint is the discipline: forcing the founder to pick the most-load-bearing 4-5.
underlying_model: Memory + compression dual constraint. Numbers stick (memory) AND must be limited (compression). Founders who give 20 numbers create noise; founders who give 4-5 create signal.
contradicts: none.
```

> "Numbers stick in people's heads."

**Application implication:** Each application section gets ≤4-5 specific numbers. Skill flags sections with >5 numbers as noisy; with 0 numbers as vague.

---

## ARC-029 — Founder Video Format (Derek Andersen, Startup Grind, 3-time applicant)

```yaml
atom_id: ARC-029
source: archive/arc-31-application-tips.md (Andersen)
expert: Derek Andersen, founder/CEO Startup Grind
applies_to_questions: [Q-VIDEO-1]
rule_type: rule (operational spec)
confidence: high
when_applies: Founder video specifically.
when_does_not_apply: Demo video (Q-CO-4) which is product-focused, not founder-focused.
why_it_exists: Causal chain — (1) 3-time applicant evidence = format known to work for the YC partner audience. (2) The constraints (1 min, founders only, no music/effects) prevent over-production — over-produced videos suggest founders prioritize aesthetics over substance. (3) Founders speaking directly = signal of presence; production polish = noise that interferes with signal. (4) Therefore the format is partner-calibrated: it minimizes production-noise to maximize founder-signal. (5) Deviating from the format costs signal because partners notice the deviation as inattention to instructions (corroborates CALDWELL-004).
underlying_model: Production minimalism is a forcing function for content. Constraints prevent the founder from hiding behind aesthetics; what's left is the founder's actual presence and idea.
contradicts: none; reinforced by CALDWELL-004.
```

> Format: 1 minute. YouTube. Only founders speak. No fancy effects or music.

**Application implication:** Skill video-script template enforces 60-second budget (~150 spoken words), all founders on camera, no narration over visuals, no background music.

---

## ARC-030 — Recommendations: Quality Over Quantity (Harj Taggar, YC Partner)

```yaml
atom_id: ARC-030
source: archive/arc-31-application-tips.md (Taggar)
expert: Harj Taggar, YC partner, Triplebyte founder
applies_to_questions: [Q-CUR-1 (how heard / encouraged), meta — networking strategy]
rule_type: rule (signal density in recommendations)
confidence: high
when_applies: When applicants have access to YC alumni networks for endorsement.
when_does_not_apply: When applicants have no YC connections — don't fake or shallow-source.
why_it_exists: Causal chain — (1) recommendations vary in signal density: a recommendation from someone who actually knows the founder well says something specific; one from a networking-circuit acquaintance says nothing specific. (2) Partners can detect the difference by the specifics in the recommendation (named project worked together, specific anecdote, specific judgment). (3) Therefore one strong recommendation outweighs ten shallow ones — the signal is in the specifics, not the count. (4) Taggar's empirical claim: this is a known partner-evaluation pattern.
underlying_model: Recommendation depth, not breadth. Quality bar: the recommender must be able to cite specifics about the founder's behavior under stress. Anything less is shallow regardless of the recommender's prestige.
contradicts: CALDWELL-006 (networking-in is ineffective) at apparent surface — actually complementary: ARC-030 is about a single high-signal recommendation; CALDWELL-006 is about networking-as-strategy. The two coexist: one strong rec is fine; building a networking strategy as the path to YC is the anti-pattern. Documented in `contradictions-register.md`.
```

> "One strong recommendation exceeds ten shallow ones."

**Application implication:** Q-CUR-1 strong answer names a specific person who specifically advocated for the application with specifics. Anti-pattern: "many people in our network suggested YC."

---

---

## ARC-016 — Move to Silicon Valley (Paul Graham)

```yaml
atom_id: ARC-016
source: archive/arc-31-application-tips.md (PG quote, tip 16)
expert: Paul Graham
applies_to_questions: [Q-CO-8, Q-CO-9 (location)]
rule_type: rule (location preference)
confidence: high
when_applies: Founders living outside Silicon Valley AND no committed SF relocation plan in Q-CO-9.
when_does_not_apply: Founders already SF-based, or geography genuinely structural to the business (on-site grid integration, regulated local market, etc.).
why_it_exists: Causal chain — (1) YC's network density (alumni, partners, investors, talent) is concentrated in SF Bay Area. (2) Founders physically in SF capture this density via informal interactions partners cannot replicate from a distance. (3) Specifically: Series A investors prefer SF-based companies; senior engineering talent in AI/infra concentrates in SF; YC partner office hours are easier in person. (4) Therefore SF presence is a multiplier — not strictly required, but absence costs measurable signal in partner evaluation.
underlying_model: SF residence is a network-density multiplier, not a hard requirement. Per CALDWELL-002 (2023 invalid-excuses), location is NOT a disqualifier — but the inverse holds: SF presence accelerates outcomes. The skill recommends explicit relocation commitment in Q-CO-9 unless geography is genuinely structural.
contradicts: CALDWELL-002 (location-not-a-disqualifier) at apparent surface — actually complementary: CALDWELL-002 says non-SF doesn't kill; ARC-016 says SF accelerates. Both true.
```

> "Silicon Valley offers superior investor experience and specialized resources." (PG, via arc-31 tip 16)

**Application implication:** Q-CO-9 strong answer for non-SF founders: explicit commitment to SF-relocation for ≥12 months post-batch. Skill flags hedged or "we'll evaluate later" language as weakening Q-CO-9. Anti-pattern: non-SF founder + no commitment statement.

**Closes:** Phase 5B Fixture 07 (international team) which was PARTIAL because ARC-016 was referenced but body wasn't atomized. Fixture 07 should re-test as PASS.

---

## Summary

**Atoms:** 10 — all upgraded with explicit causal chains. ARC-016 added 2026-05-05 to close Fixture 07.
**Coverage:** Q-CO-7, Q-CO-8/9, Q-IDEA-1/2/3, Q-PROG-1, Q-PROG-5/6/7/8, Q-VIDEO-1, Q-FOUND-1, Q-CUR-1, P-ACC-2, P-ACC-3.
**Cross-references:** ARC-005 vs. PG-009 (clarity ≠ polish-paralysis), ARC-030 vs. CALDWELL-006 (rec ≠ networking-strategy), ARC-016 vs. CALDWELL-002 (SF accelerates, non-SF doesn't kill).
