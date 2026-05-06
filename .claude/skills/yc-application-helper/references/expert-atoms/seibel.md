# Michael Seibel — Atomized (v2 — re-extracted with causal-chain protocol)

**Sources:** archive/seibel-decade-of-learnings.md, archive/arc-31-application-tips.md (Seibel quotes), archive/yc-interviews-page.md
**v2 changes:** SEIBEL-002 + SEIBEL-003 + SEIBEL-004 mechanisms upgraded; 2 new atoms added (SEIBEL-006 traction-stage calibration, SEIBEL-007 signal-filter mechanism).

**Atom count:** 7 (was 5).

---

## SEIBEL-001 — Eliminate Marketing Speak (with named banned terms)

```yaml
atom_id: SEIBEL-001
source: archive/arc-31-application-tips.md (verbatim Seibel quote)
expert: Michael Seibel
applies_to_questions: [ALL written]
rule_type: anti-pattern (vocabulary, named)
confidence: high
when_applies: Every written response.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) marketing-speak is what consultants and PR firms use to sound impressive without committing to specifics. (2) Founders who use it are either trained-in-consultant-register or hiding lack of substance. (3) "Platform" specifically is named-banned because it can mean almost anything (marketplace, API, infrastructure, app, suite) — its ambiguity is the tell. (4) Each banned term triggers a mini-rejection that the founder must overcome with later content; cumulative buzzword count drains the partner's patience.
underlying_model: Plain-language is the partner-readable register. Anything else costs trust. The named-banned terms are the canonical detector signals.
contradicts: none; corroborates HALE-005.
```

> "Eliminate jargon, acronyms, marketing speak, and any ambiguous terms such as 'platform.'"

**Application implication:** Skill anti-pattern detection includes "platform" specifically (Seibel-flagged). The word "platform" in a description = mandatory flag.

---

## SEIBEL-002 — PMF Self-Knowledge (as credibility baseline) ⟵ v2 UPGRADED

```yaml
atom_id: SEIBEL-002
source: archive/seibel-decade-of-learnings.md
expert: Michael Seibel
applies_to_questions: [Q-PROG-5/6, Q-PROG-7/8]
rule_type: rule (founder honesty + credibility baseline)
confidence: high
when_applies: User and revenue questions.
when_does_not_apply: Idea-stage with no users / revenue — but here founders must say "we don't yet" rather than fabricate.
why_it_exists: Causal chain — (1) the founder is the biggest expert in their own company because they have access to data partners do not. (2) Therefore the founder's OWN judgment about PMF status is the partner's prior — partners assume the founder's self-assessment is accurate. (3) When the founder's stated assessment differs from what the data implies, two interpretations exist: (a) the founder is being dishonest, or (b) the founder is confused about their own state. (4) Both interpretations damage credibility — but (b) is worse because it signals the founder doesn't have the operational self-awareness needed to run the company. (5) Therefore deviation from honest self-assessment isn't just a dishonesty signal, it's a competence signal. (6) "Investor confusion about your PMF (because you presented confused signals) = your problem, not theirs."
underlying_model: Self-knowledge IS the credibility baseline. Partners read Q-PROG-5/6/7/8 as a proxy for "does the founder know their own state." Founders who don't know fail the competence gate even before the data is evaluated.
contradicts: none; reinforces ANTI-003 (lack of social proof and traction = verbatim partner rejection reason).
```

> "You know whether you have product market fit or not... You are the biggest expert in your company."

**Application implication:** Q-PROG-5/6/7/8 require self-honest framing. Single customer ≠ PMF (state honestly). Partners punish exaggeration MORE than honest absence because exaggeration signals self-confusion.

---

## SEIBEL-003 — Business Model Determinism ⟵ v2 UPGRADED

```yaml
atom_id: SEIBEL-003
source: archive/seibel-decade-of-learnings.md
expert: Michael Seibel
applies_to_questions: [Q-IDEA-3, Q-PROG-7/8/9]
rule_type: rule (deterministic cascade)
confidence: high
when_applies: Business-model and revenue-source questions, especially B2B.
when_does_not_apply: Genuine consumer products with clear B2C dynamics.
why_it_exists: Causal chain — (1) categorizing the business as SaaS vs. Enterprise isn't a positioning choice — it's a recognition of the underlying customer dynamics. (2) Once you pick the model, MULTIPLE downstream factors are determined automatically: pricing tier (low-ACV self-serve vs. high-ACV custom), sales cycle length (days/weeks vs. months/quarters), team type (PLG / marketing-led vs. enterprise-AE), customer-success structure, and contract terms. (3) Founders who frame "SaaS" but operate Enterprise (or vice versa) reveal they don't understand the cascade — they think the business model is a label they apply, when it's actually the structural shape of their customer relationships. (4) Partners detect the category mismatch by comparing the founder's self-categorization against operational signals (customer count + ACV + sales cycle) — mismatch = signal of confusion.
underlying_model: The model is decided BY the customer dynamics, not chosen by the founder. Self-categorization that mismatches operational reality = confusion-signal independent of which category is "right."
contradicts: none.
```

> Strategy must align with pricing and customer type — these factors are "decided for you."

**Application implication:** Skill detects category mismatch. Pre-revenue or 1-customer "enterprise" applications described as "SaaS" = anti-pattern. Skill cross-checks Q-IDEA-3 self-categorization against Q-PROG-6 customer count + Q-PROG-7/8 revenue + Q-PROG-9 source breakdown for consistency.

---

## SEIBEL-004 — Patience Principle (as predictive calibration) ⟵ v2 UPGRADED

```yaml
atom_id: SEIBEL-004
source: archive/seibel-decade-of-learnings.md
expert: Michael Seibel
applies_to_questions: [Q-IDEA-1, Q-PROG-1]
rule_type: pattern (predictive — over-confidence as PMF-blindness signal)
confidence: medium-high
when_applies: When the application claims to have already solved a hard problem.
when_does_not_apply: Cases where the founder honestly acknowledges discovery is ongoing.
why_it_exists: Causal chain — (1) Twitch (originally Justin.tv) took six years to find PMF, despite an experienced and capable founding team. (2) This isn't an outlier — it's the typical pattern for hard problems. (3) Therefore founders who sound CERTAIN at application time about a hard problem are statistically more likely to be PMF-blind: their certainty is unwarranted given the base rate. (4) Conversely, founders who acknowledge ongoing discovery match the base rate and signal calibrated thinking. (5) Partners pattern-match against this base rate: certainty about a hard problem at YC stage = warning signal.
underlying_model: Statistical pattern matching. Over-confidence at application time correlates with PMF-blindness later. Honest engagement with discovery state correlates with founder calibration. The skill detects over-confidence and softens it.
contradicts: none.
```

> "If your plan is you already have solved the problem... beware, it might take a lot longer."

**Application implication:** Q-IDEA-1 + Q-PROG-1 should communicate honest engagement with the problem, not premature certainty. Skill softens over-confident framings ("we have solved X" → "we have shipped a v1 that addresses X"). Anti-pattern: "we have solved" / "we have figured out" / "we have nailed" framings on hard problems.

---

## SEIBEL-005 — Interview: Speak Naturally

```yaml
atom_id: SEIBEL-005
source: archive/yc-interviews-page.md
expert: Michael Seibel (page is partner-authored)
applies_to_questions: [Q-VIDEO-1, all interview-stage; framing applies to written app voice]
rule_type: rule (voice)
confidence: high
when_applies: Founder video and interview prep. Carries to overall application voice — sincere > rehearsed.
when_does_not_apply: Highly technical answers where precision matters more than warmth.
why_it_exists: Partners evaluate "whether you'll be enjoyable to work with during the journey ahead." Performance/over-rehearsed = anti-pattern.
underlying_model: Sincere uncertainty in conversation is acceptable; sincere uncertainty written into the application is not (per ANTI-005). Resolve via skill: drafts must be confident on the page; founders speak sincerely in person.
contradicts: ANTI-005 — resolved via form-vs-conversation distinction in `contradictions-register.md` CONTRADICTION-003.
```

> "Be earnest." "Sincere, straightforward and natural."

**Application implication:** Founder video tone = sincere/straightforward. v-polished should not lose sincerity. Phase 5C partner-simulation gate verifies.

---

## SEIBEL-006 — Traction-Stage Calibration (NEW — was missing in v1)

```yaml
atom_id: SEIBEL-006
source: archive/seibel-decade-of-learnings.md (extracted as standalone atom from $150-250K MRR / $1M ARR / Series A discussion)
expert: Michael Seibel
applies_to_questions: [Q-PROG-5/6, Q-PROG-7/8]
rule_type: rule (calibration prior)
confidence: high
when_applies: Traction questions — especially when the founder is choosing how to frame revenue / users.
when_does_not_apply: Idea-stage applications with no traction to calibrate.
why_it_exists: Causal chain — (1) partners have a mental model of "realistic traction at stage X" built from seeing thousands of applications. (2) Most B2B companies should target $150-250K monthly recurring revenue before Series A; raising at $1M ARR with minimal runway gives investors "maximum leverage" against the founder. (3) Founders who DRAMATICALLY UNDER-CLAIM relative to that prior signal lack of confidence or absence of traction; founders who DRAMATICALLY OVER-CLAIM signal exaggeration or category confusion (e.g., calling a single high-ACV pilot "ARR"). (4) Both deviation directions trigger pattern-match against partners' prior. (5) Therefore the calibration is bilateral: under-claiming and over-claiming both fail.
underlying_model: Partners have a calibrated prior; deviation either direction = anti-pattern. Skill should help founders frame traction in the calibrated band when the underlying numbers support it, and frame honestly when they don't.
contradicts: none.
```

> "Most B2B companies should target $150-250K monthly recurring revenue before Series A. Raising at $1M ARR with minimal runway gives investors 'maximum leverage.'"

**Application implication:** Skill cross-checks Q-PROG-7/8 numbers against the partner-prior calibration. Significant deviation either direction = flag for review. Anti-pattern: claiming "ARR" from a single non-recurring pilot.

---

## SEIBEL-007 — Signal Filter (Partners Eliminate in First 2 Minutes) (NEW — was missing in v1)

```yaml
atom_id: SEIBEL-007
source: archive/seibel-decade-of-learnings.md (mechanism extracted from "lack of social proof and traction" canonical-rejection-reason discussion)
expert: Michael Seibel (corroborated by ANTI-003 verbatim partner feedback)
applies_to_questions: [Q-PROG-5/6, Q-PROG-7/8, Q-FOUND-1, Q-VIDEO-1]
rule_type: rule (signal-filter mechanism)
confidence: high
when_applies: Universal — describes how partners process applications.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) partners read ~100 applications per day. (2) The default state of an application is "eliminate"; partners look for reasons to keep reading. (3) Two signals dominate the first 2 minutes: traction evidence + founder evidence. (4) Applications with NEITHER trigger early elimination because partners have no reason to invest the remaining 3 minutes of cognitive budget. (5) Applications with EITHER one survive the first filter and earn deeper review. (6) Therefore traction is not aspirational; it's a signal-filter that gates partner attention. (7) Same for founder evidence — at minimum P-ACC-2 (most-impressive) must contain a specific signal to survive the first filter.
underlying_model: Default-eliminate cognitive workflow. Applications need at least one survival signal in the first 2 minutes; without one, the remaining content isn't read carefully. Skill should ensure every application has at least one strong survival signal early.
contradicts: none.
```

> Partners eliminate at first signal-absence; survive only with traction OR founder evidence in the first 2 minutes.

**Application implication:** Skill ensures Q-PROG-5/6 + P-ACC-2 collectively contain at least one strong survival signal. Anti-pattern: weak Q-PROG-5/6 (no users / no LOIs) AND weak P-ACC-2 (vague founder achievement) = early-elimination shape.

---

## Summary

**Atoms:** 7 (5 from v1 + 2 new SEIBEL-006/007; SEIBEL-002/003/004 upgraded with mechanisms)
**Coverage:** Q-PROG-5/6, Q-PROG-7/8, Q-IDEA-1, Q-IDEA-3, Q-VIDEO-1, ALL written (via SEIBEL-001 + SEIBEL-007)
