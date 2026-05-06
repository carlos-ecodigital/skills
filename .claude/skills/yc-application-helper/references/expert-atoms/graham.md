# Paul Graham — Atomized (v3 — re-extracted with causal-chain protocol)

**Sources:** archive/pg-schlep-blindness.md, pg-how-to-get-startup-ideas.md, pg-default-alive-or-dead.md, pg-how-to-convince-investors.md, yc-howtoapply-page.md

**v3 changes from v2:** PG-004, PG-006, PG-010 rewritten with explicit causal chains in `why_it_exists` and `underlying_model`. Other atoms unchanged from v2 (passed reviewer audit).

**Atom count:** 17. Per-expert share ~30% of corpus.

---

## PG-001 — The Schlep Reframe

```yaml
atom_id: PG-001
source: archive/pg-schlep-blindness.md (lines 14-22)
expert: Paul Graham
applies_to_questions: [Q-IDEA-1, Q-IDEA-2, Q-PROG-1]
rule_type: reframe / heuristic
confidence: high
when_applies: Default for Q-IDEA-1 framing — "why this idea" answered through schlep encountered.
when_does_not_apply: Pure-research / deep-tech where the "schlep" is technical risk rather than tedium; here the schlep is technical impossibility others abandoned.
why_it_exists: Causal chain — (1) the unconscious filters out schlep-laden ideas pre-consciously, before they reach evaluation. (2) Conscious "what should I solve?" frameworks therefore fail systematically because they operate downstream of the filter. (3) The reframe ("what do I wish someone else would solve for me?") routes around the filter by inverting agency — you are now the user complaining, not the founder evaluating.
underlying_model: Schlep blindness is a Type-1 error rate problem in idea-generation: the filter rejects valuable ideas because their tediousness/regulatory/political surface markers correlate with low-status work. The reframe defeats the filter without addressing it directly.
contradicts: none
```

> "Your unconscious won't even let you see ideas that involve painful schleps."
> "What problem do I wish someone else would solve for me?"

**Application implication:** Strongest Q-IDEA-1 answers identify a specific schlep the founder personally encountered. Anti-pattern: "we wanted to build a cool app." Pattern: "I spent 6 months trying to do X and the existing tools were unusable, here's what they get wrong."

---

## PG-001b — Ignorance as Antidote

```yaml
atom_id: PG-001b
source: archive/pg-schlep-blindness.md (lines 26-28)
expert: Paul Graham
applies_to_questions: [Q-IDEA-1, Q-FOUND-1]
rule_type: pattern (counterintuitive — strategic value of inexperience)
confidence: high
when_applies: Young / first-time founders attempting schlep-heavy or "obviously hard" problems.
when_does_not_apply: Founders who explicitly cite their experience as a moat — formidability comes from prior shipping; ignorance is irrelevant for them.
why_it_exists: Causal chain — (1) experienced founders see obstacles clearly because they've encountered similar ones before. (2) This clarity activates the schlep-blindness filter (PG-001) more strongly. (3) Young founders, lacking that obstacle-pattern-recognition, simply do not see the reasons not to try. (4) Their parallel lack of self-awareness about their own limitations cancels the obstacle-blindness — they don't know it's hard AND they don't know they shouldn't try.
underlying_model: "Mistakes that cancel out" — two ignorance vectors (about obstacles + about self) compound to produce action where experienced founders would freeze. This is why YC funds so many young first-time founders on hard problems.
contradicts: PG-010 (formidability via specific evidence) at apparent surface — actually complementary: formidability + ignorance = young founders who ship despite not knowing the obstacles.
```

> "Young founders lack awareness of obstacles ahead AND awareness of their own limitations; mistakes cancel out. Experienced founders only lack the first."

**Application implication:** Q-FOUND-1 / per-founder profile — first-time / young founders shouldn't apologize for inexperience. Inexperience on a hard problem is positive when paired with shipping evidence. Anti-pattern: "we acknowledge we're young but..." defensive framing.

---

## PG-002 — Schlep as Moat

```yaml
atom_id: PG-002
source: archive/pg-schlep-blindness.md (lines 16-22)
expert: Paul Graham
applies_to_questions: [Q-IDEA-2]
rule_type: pattern (positive)
confidence: high
when_applies: Q-IDEA-2 when the company is doing regulated, infrastructure-heavy, complex-onboarding, or politically-contested work.
when_does_not_apply: Pure-software fast-iteration plays where the moat is execution speed.
why_it_exists: Causal chain — (1) competitors share the same schlep-blindness filter as the founder. (2) Their unconscious rejects the same opportunity for the same reason. (3) Founders who consciously override their own filter are doing what competitors structurally cannot. (4) Each year competitors stay away due to the filter, the moat compounds via lock-in (regulatory relationships, fraud-prevention infrastructure, customer trust).
underlying_model: Defensibility through tedium-tolerance is a willingness moat, not a technology moat. Stripe didn't beat competitors via technology — they beat competitors who could have built the same thing but unconsciously didn't try.
contradicts: none; complements ALTMAN-003 (why-now = unrealized shift).
```

> "Schleps are not merely inevitable, but pretty much what business consists of. A company is defined by the schleps it will undertake."

**Application implication:** Q-IDEA-2 strong answer: "We're willing to do [specific schlep]. Competitors avoid it because [specific reason]. This compounds because [specific lock-in mechanism]."

---

## PG-003 — The Founder 3-Test (with organic-origin prerequisite)

```yaml
atom_id: PG-003
source: archive/pg-how-to-get-startup-ideas.md (lines 9-15 + 49-54)
expert: Paul Graham
applies_to_questions: [Q-IDEA-1, Q-FOUND-1]
rule_type: rule with prerequisite check
confidence: high
when_applies: ALL Q-IDEA-1 evaluations after the organic-origin prerequisite passes.
when_does_not_apply: Non-founder-led ideas — fail the prerequisite by definition.
why_it_exists: Causal chain — (1) founder-product fit is upstream of every other capability the founder needs. (2) Without it, the founder doesn't dogfood, can't iterate from real pain, and depends on hires for product velocity. (3) The 3-test is necessary but not sufficient: a "made-up" idea (PG-005) could theoretically satisfy all 3 but still fail because the founder didn't *experience* the want — they engineered the want backward from "what could be a company." The organic prerequisite catches that.
underlying_model: The 3-test is what partners check; the organic prerequisite is what produces a credible 3-test in the first place. Both must hold.
contradicts: none, but interlocked with PG-005.
```

> Best startup ideas: (1) something the founders themselves want, (2) that they themselves can build, (3) that few others realize are worth doing.

**Application implication:** Q-IDEA-1 must demonstrably satisfy all three AND show organic origin. Skill flags "we identified a market opportunity and decided to build for it" framing as the made-up signature.

---

## PG-004 — Live in the Future (multi-path, mechanism-explicit) ⟵ v3 UPGRADED

```yaml
atom_id: PG-004
source: archive/pg-how-to-get-startup-ideas.md (lines 38-47)
expert: Paul Graham
applies_to_questions: [Q-IDEA-1, Q-IDEA-2, Q-PROG-3]
rule_type: rule (universal — multi-path)
confidence: high
when_applies: ALWAYS. Strong Q-IDEA-1 answers identify WHICH path of leading-edge proximity the founder is on.
when_does_not_apply: Never as a category exemption. If no path applies, the application is sitcom-shaped.
why_it_exists: Causal chain — (1) startup ideas come from "external stimulus hitting a prepared mind." (2) Stimulus is widely available; preparation is not. (3) Preparation is produced by leading-edge proximity, but that proximity has multiple distinct paths: (a) RESEARCHER pushing technical boundaries (Bell Labs / Xerox PARC pattern), (b) HEAVY USER with daily exposure (Drew Houston / USB stick), (c) DEMOGRAPHIC INSIDER in the target population (Mark Zuckerberg / heavy-computer-user Harvard student), (d) PRIOR-INDUSTRY INSIDER who saw the gap from inside (Stripe Collisons / Limerick teenagers selling internet products globally), (e) EARLY ADOPTER AT SCALE who tested many tools and noticed pattern of failure. (4) Each path produces "prepared mind" via different mechanism — but every successful YC application MUST claim ONE.
underlying_model: Partners scan Q-IDEA-1 for which path the founder is on. They reward whichever path is honestly claimed and dismiss applications that claim none — claim-of-none signals the founder constructed the idea backward from market analysis rather than forward from experience. Researcher path is rare; heavy-user and demographic-insider paths dominate at YC stage.
contradicts: none directly; complements PG-003.
```

> "Live in the future, then build what's missing."
> "You can be at the leading edge as a user."
> "Their experiences had prepared them to notice the opportunities."

**Application implication:** Q-IDEA-1 strong answer explicitly identifies which path the founder is on. Skill prompts the founder during facts-file intake: "Which path of leading-edge proximity describes you on this idea? (researcher / heavy user / demographic insider / prior-industry insider / early-adopter-at-scale)." Anti-pattern: framing the opportunity from market-research perspective with no path claimed.

---

## PG-005 — Organic vs. Sitcom Ideas

```yaml
atom_id: PG-005
source: archive/pg-how-to-get-startup-ideas.md (lines 49-54)
expert: Paul Graham
applies_to_questions: [Q-IDEA-1, Q-PROG-5/6]
rule_type: anti-pattern detector
confidence: high
when_applies: Any Q-IDEA-1 / Q-PROG-5 evaluation.
when_does_not_apply: Established markets with clear demand baselines (better CRM, better PM tool) — these can be made-up but still fundable on execution.
why_it_exists: Causal chain — (1) when an idea is made-up rather than experienced, the founder hasn't felt the pain. (2) Without that felt-pain reference, the founder can't distinguish "users would tolerate v1" from "users would say nice things if asked." (3) Real users say "I need this NOW" — fake users say "yeah maybe." (4) Made-up ideas always die at the user-test because the founder has been calibrating against imagined users, not real ones.
underlying_model: Singular intense demand beats distributed mild interest. The same principle as PG-006 stated diagnostically — real demand sounds intense; fake sounds mild. Real demand passes "would you use the v1 today?"; fake passes only "would you theoretically use a polished product?"
contradicts: none; same principle as PG-006 stated as a diagnostic.
```

> "When you test it, people say 'Yeah, maybe I could see using something like that,' which means zero actual demand. Sum that reaction across the entire population, and you have zero users."

**Application implication:** Skill scans Q-IDEA-1 + Q-PROG-5/6 for organic-idea signals. Anti-pattern: "we think users would benefit from..."

---

## PG-005b — The User-Test Diagnostic

```yaml
atom_id: PG-005b
source: archive/pg-how-to-get-startup-ideas.md (lines 50-54)
expert: Paul Graham
applies_to_questions: [Q-IDEA-1, Q-PROG-5/6]
rule_type: diagnostic test (operational)
confidence: high
when_applies: During facts-file intake to test whether customer-discovery has produced organic or sitcom signals.
when_does_not_apply: After concrete revenue / paying customers exist.
why_it_exists: Causal chain — (1) the tone of user reactions, not the count, distinguishes real from fake demand. (2) "Yeah, maybe" is the canonical sitcom-signal because it's polite-noncommittal — what users say when they don't want to engage but don't want to be rude. (3) "When can I have it?" / "I would pay for this today" / "I've been looking for this for years" are the canonical organic-signals because they bypass politeness and reveal urgency.
underlying_model: User reactions follow a politeness-vs-urgency axis. Mild interest expressed politely is the noise floor; urgency cuts through. The diagnostic is: pull the strongest specific quote from a real potential user. Strength of that quote IS the diagnostic.
contradicts: none
```

> Diagnostic for facts file: "What was the most enthusiastic specific reaction from a real potential user when you described this product? Quote them verbatim."

**Application implication:** Skill's pre-draft fuzziness gate tests Q-IDEA-1 facts against this diagnostic. Strongest cited reaction = "yeah maybe" = flag as sitcom-shaped before drafting.

---

## PG-006 — Narrow-and-Deep Beats Broad-and-Shallow ⟵ v3 UPGRADED

```yaml
atom_id: PG-006
source: archive/pg-how-to-get-startup-ideas.md (lines 19-35)
expert: Paul Graham
applies_to_questions: [Q-IDEA-3, Q-PROG-5/6, Q-CO-7]
rule_type: rule (stage-conditional)
confidence: high
when_applies: AT YC APPLICATION STAGE (pre-PMF). Intensity-of-demand from a small group is what works.
when_does_not_apply: Post-PMF — then PG-CONVINCE-003 applies. Applicants commonly confuse these two rules.
why_it_exists: Causal chain — (1) A 2-person startup ships a "crappy version one" with bugs, missing features, and rough UX. (2) Most users abandon at first friction; only users with NO viable alternative tolerate v1 incompleteness. (3) "No viable alternative" comes from depth of dependency, not breadth of demand. (4) Microsoft/Altair: owners were programming in machine language without Basic — the dependency was so deep that incomplete-but-existing > nothing. (5) Early Facebook at Harvard: students had no usable social network for their context — same dependency. (6) Without that dependency-driven tolerance, v1 dies before iteration can produce v2. (7) Therefore narrow-deep is a survival prerequisite at YC stage; broad-shallow can't survive v1.
underlying_model: At YC stage the question is "who has no viable alternative and therefore tolerates the v1?" — not "how big is the market in 5 years?" Intensity = no-alternative dependency. Breadth = alternatives exist; mild-interest users go elsewhere at first friction.
contradicts: PG-CONVINCE-003 (TAM as ceiling, expansion path) — stage-conditional. Pre-PMF apply PG-006; post-PMF apply PG-CONVINCE-003. Documented in `contradictions-register.md` CONTRADICTION-001.
```

> "Something a small number of people want a large amount."
> "Who wants this so much that they'll use it even when it's a crappy version one made by a two-person startup?"
> Microsoft/Altair: "Without this software they were programming in machine language."

**Application implication:** Q-PROG-5/6 strong answer names a specific intense user with no alternative, not "10,000 sign-ups." Q-IDEA-3 leads with depth-of-engagement, not TAM. Skill detects TAM-led framing in Q-IDEA-3 and flags as anti-pattern (signals applicant misread which rule applies).

---

## PG-007 — Default Alive Test

```yaml
atom_id: PG-007
source: archive/pg-default-alive-or-dead.md (lines 11-26)
expert: Paul Graham
applies_to_questions: [Q-PROG-7/8, Q-EQ-7/8/9]
rule_type: framework (with competence gate)
confidence: high
when_applies: Founders with any revenue and any spend should know their default-alive/dead status.
when_does_not_apply: Pre-spend, pre-revenue idea-stage applications.
why_it_exists: Causal chain — (1) the test reveals whether current trajectory leads to profitability before runway exhaustion. (2) Founders who've computed it have done basic financial discipline. (3) Founders who haven't have either avoided the question or treated it as irrelevant. (4) That avoidance is a competence signal independent of the actual numbers — it tells partners how the founder thinks about runway. (5) "Half the founders I talk to don't know" — meaning the simple act of knowing differentiates from half the applicant pool.
underlying_model: Partners read Q-EQ-7/8/9 + Q-PROG-8 as both a math test (does the math work) AND a competence test (did the founder do the math). Both fail modes — bad math AND no math — kill applications.
contradicts: none
```

> "Assuming expenses remain constant and revenue growth is what it has been, do they make it to profitability on the money they have left?"
> "Half the founders I talk to don't know whether they're default alive or default dead."

**Application implication:** Skill cross-checks Q-EQ-7/8 against Q-EQ-9 runway and Q-PROG-8 trajectory. Implausibilities flagged. Vague Q-EQ-9 ("we haven't computed this") flagged as competence fail.

---

## PG-008 — Hiring Too Fast

```yaml
atom_id: PG-008
source: archive/pg-default-alive-or-dead.md (lines 28-39)
expert: Paul Graham
applies_to_questions: [Q-EQ-* (use of proceeds), Q-PROG-1, Q-IDEA-3]
rule_type: anti-pattern (with causal mechanism)
confidence: high
when_applies: Applications with explicit hiring plans in use-of-proceeds.
when_does_not_apply: Late-stage YC applications with proven PMF + revenue.
why_it_exists: Causal chain — (1) founders observe successful companies have large staffs. (2) They infer hiring → growth (effect mistaken for cause). (3) When they hire pre-PMF, founder bandwidth shifts from product to management. (4) Product iteration slows. (5) Burn rate spikes simultaneously. (6) Slower iteration + faster burn = death sequence. (7) The Airbnb counterexample: 4-month no-hire post-YC kept founders product-focused while raising bar on hiring.
underlying_model: Hiring solves capacity problems, not product problems. Slow growth signals product problems. Therefore hiring during slow growth = wrong solution to wrong problem.
contradicts: none
```

> "Hiring too fast is by far the biggest killer of startups that raise money."
> "Airbnb waited 4 months after raising money at the end of Y Combinator before they hired their first employee."

**Application implication:** Use-of-proceeds framing emphasizes product, infrastructure, customer acquisition. Heavy hiring framing = anti-pattern.

---

## PG-008b — Slow Growth Signals Product Problems

```yaml
atom_id: PG-008b
source: archive/pg-default-alive-or-dead.md (lines 36-39)
expert: Paul Graham
applies_to_questions: [Q-PROG-1, Q-EQ-* (use of proceeds), Q-IDEA-3]
rule_type: diagnostic rule
confidence: high
when_applies: When the application describes a growth slowdown OR plans hiring to fix slow growth.
when_does_not_apply: Robust growth genuinely capacity-constrained.
why_it_exists: Causal chain — (1) growth has two failure modes: capacity-bound (have demand, can't deliver) and demand-bound (have capacity, no demand). (2) Hiring solves capacity-bound, never demand-bound. (3) At YC stage, slow growth almost always means demand-bound (product doesn't make users want more). (4) Therefore "we plan to hire to accelerate growth" is a category error: hiring won't fix the actual problem.
underlying_model: Skill treats "we plan to hire to accelerate growth" as a category-error flag. Correct response to slow growth is product iteration or customer-acquisition refinement.
contradicts: none
```

> "Slow growth typically signals product problems, not staffing gaps."

**Application implication:** Q-PROG-1 / Q-IDEA-3 / use-of-proceeds — applications framing growth-acceleration as hiring plans get a category-error flag. Strong answers frame growth-acceleration as product-iteration or customer-acquisition plans.

---

## PG-009 — Clarity = Comprehension Gate

```yaml
atom_id: PG-009
source: archive/pg-how-to-convince-investors.md (lines 11-18)
expert: Paul Graham
applies_to_questions: [ALL — especially Q-CO-2, Q-CO-7, Q-IDEA-1]
rule_type: rule (foundational comprehension gate)
confidence: high
when_applies: Every written response.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) explanation is downstream of understanding: you can only explain what you understand. (2) Therefore inability to explain is evidence of inability to understand. (3) Partners cannot fund a founder who doesn't understand the business — regardless of merit, the founder cannot iterate, hire, sell, or pivot without understanding. (4) Therefore unclear writing triggers a binary disqualifier independent of the substance of the idea.
underlying_model: Clarity is a comprehension gate, not a stylistic preference. Drafts that fail clarity are eliminated before substance evaluation; they do not score "less good." This is binary, not continuous.
contradicts: none
```

> "If you can't explain your plans concisely, you don't really understand them."

**Application implication:** Skill brevity gate enforces ≤3-min total reading time. Drafts requiring re-reading are eliminated, not patched.

---

## PG-009b — Marketing Jargon as Incompetence Signal

```yaml
atom_id: PG-009b
source: archive/pg-how-to-convince-investors.md (lines 11-18)
expert: Paul Graham
applies_to_questions: [ALL written]
rule_type: rule (stylistic register)
confidence: high
when_applies: Every written response.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) people who understand their business explain it the same way to engineers, customers, investors, and themselves. (2) People who don't understand develop separate "investor language" using marketing register. (3) Partners notice the dissonance: language that doesn't match how internal-team-discussions sound is performance-language, not comprehension-language. (4) Performance-language reveals founder is hiding something or doesn't have it.
underlying_model: Internal-discussion language IS the test. If the founder describes the company differently to a co-founder vs. to an investor, the investor version is corrupted. The internal version is correct.
contradicts: none; layered with HALE-005, SEIBEL-001.
```

> "Avoid marketing jargon; use the same straightforward language you'd employ discussing the business internally."

**Application implication:** Skill validation: have the founder describe the company in 2 ways — to a co-founder vs. to an investor. Significant divergence = investor version corrupted. Internal version is correct register.

---

## PG-010 — Formidable Founders (with cognitive lock-in mechanism) ⟵ v3 UPGRADED

```yaml
atom_id: PG-010
source: archive/pg-how-to-convince-investors.md (lines 22-30)
expert: Paul Graham
applies_to_questions: [Q-FOUND-1, P-ACC-1, P-ACC-2, P-ACC-3]
rule_type: rule (dominant + first-impression-locked)
confidence: high
when_applies: Founder profile evaluation. Dominant evaluation dimension AND fastest-decided.
when_does_not_apply: Ideas-only applications without founder evidence — formidability shifts to P-ACC-1 (wildcard) and P-ACC-2 (most-impressive).
why_it_exists: Causal chain — (1) partners read 100 apps/day; cognitive load forces fast judgment. (2) The first signal sets a Bayesian prior. (3) Subsequent signals update the prior, but updates are weak — once a positive prior is set, weak later signals get charitable interpretation; once a negative prior is set, even strong later signals get skeptical interpretation. (4) This is impression-stickiness via cognitive lock-in: the partner's frame, set in the first sentences, filters all subsequent reading. (5) Therefore the first sentence of a founder bio matters more than the cumulative volume — it determines whether the rest is read sympathetically or skeptically.
underlying_model: Formidability isn't evaluated comprehensively; it's evaluated locked-in. Comprehensive-evidence framing may be stronger than what partners require for the gate; one strong specific signal in the first sentence wins. The skill should optimize for the first sentence being maximally specific and strong, then add evidence after.
contradicts: none
```

> "Investors evaluate startups across three primary dimensions: Formidable founders... Promising market... Evidence of traction. Founder dimension is dominant."
> "Most investor decisions happen within minutes. Initial impressions difficult to reverse."

**Application implication:** Founder bios optimize for first-sentence impact (named project + scale + outcome), then add depth. Skill founder-credibility gate enforces ≥2 named prior projects but specifically scores the FIRST one for specificity and strength.

---

## PG-011 — Address Rejection Head-On

```yaml
atom_id: PG-011
source: archive/pg-how-to-convince-investors.md (lines 44-45)
expert: Paul Graham
applies_to_questions: [Q-PROG-11, Q-PROG-12, Q-EQ-* (failed prior raises)]
rule_type: rule (counterintuitive)
confidence: high
when_applies: Applications disclosing prior YC rejection, prior accelerator participation, or prior fundraise.
when_does_not_apply: First-time applicants with no prior fundraise.
why_it_exists: See PG-011b for the underlying tactical mechanism. Surface rule: confidence + transparency = signal of conviction.
underlying_model: Conviction grounded in genuine self-assessment communicates execution likelihood more than pitch technique.
contradicts: none
```

> "Address rejection head-on: rather than seeming evasive about investor turndowns, candidly explain why those rejections were mistaken."

**Application implication:** Q-PROG-11/12 strong answers explain prior outcomes confidently with what changed. Anti-pattern: hedging or omission.

---

## PG-011b — Narrative Control on Rejection

```yaml
atom_id: PG-011b
source: archive/pg-how-to-convince-investors.md (lines 44-45)
expert: Paul Graham
applies_to_questions: [Q-PROG-11, Q-PROG-12, Q-EQ-*]
rule_type: tactic (information asymmetry)
confidence: high
when_applies: Applicant has prior rejections, failed fundraises, or prior controversies discoverable via diligence.
when_does_not_apply: Clean histories.
why_it_exists: Causal chain — (1) partners conduct diligence; prior rejections / failures will surface. (2) The applicant therefore has only one choice: control the framing or let partners construct their own. (3) Self-framing happens at application read-time; partner-framing happens later. (4) Whichever framing lands first sticks (PG-010 cognitive lock-in extended to story-level). (5) Therefore proactive disclosure with confident framing locks in the founder's interpretation; concealment lets partners construct a worse one.
underlying_model: Information-asymmetry tactic. The first version of a story that lands tends to stick. Founders frame their own rejections; founders who hide them lose framing to partner imagination.
contradicts: none
```

> Tactical layer: hidden liabilities discovered later destroy trust. Proactive framing controls when and how partners learn.

**Application implication:** Skill detects in company facts any prior rejection / failed raise / controversy. Auto-generates Q-PROG-11/12 / equity-question draft framing the issue first. Anti-pattern: facts file mentions a prior issue but the draft conceals it.

---

## PG-012 — The Most Important Question (P-ACC-2 hard gate)

```yaml
atom_id: PG-012
source: archive/yc-howtoapply-page.md (PG verbatim) + per-founder profile P-ACC-2
expert: Paul Graham
applies_to_questions: [P-ACC-2]
rule_type: rule (hard gate)
confidence: high
when_applies: P-ACC-2 in per-founder profile, every founder.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) PG explicitly designates this "the most important question." (2) The 1-2 sentence constraint forces compression: founders must name the most impressive thing they've done in <50 words. (3) Founders who have shipped real things compress easily because they pick the strongest specific signal. (4) Founders who haven't shipped real things resort to vagueness, scope-claims, or aspirational framing — all detectable. (5) Therefore the question functions as a binary filter: shipped-real-things vs. hasn't.
underlying_model: Hard gate, not weighted dimension. Vagueness here cannot be salvaged by strong answers elsewhere. The question separates founders who have specific shipping evidence (with named scale/recognition/dollar amounts) from founders who don't.
contradicts: PG-009 (clarity) reinforces; HALE-002 (lead with what) parallels.
```

> "Please tell us in one or two sentences about something impressive that each founder has built or achieved."
> PG: "the most important question on the application."

**Application implication:** Skill produces 2-3 candidates per founder. Each: specific thing built/achieved + scale/outcome (number, named users, named recognition) + delivered (not aspirational). Skill treats this as binary gate; vague drafts hard-flagged.

---

## Summary

**Atoms:** 17 (12 v2-passed + 3 v3-upgraded: PG-004, PG-006, PG-010 with explicit causal chains)
**Coverage:** Q-IDEA-1, Q-IDEA-2, Q-IDEA-3, Q-PROG-1, Q-PROG-5/6, Q-PROG-7/8, Q-PROG-11, Q-PROG-12, Q-EQ-7/8/9, Q-CO-2, Q-CO-7, Q-FOUND-1, P-ACC-1 (indirect), P-ACC-2.
**Contradictions:** PG-006 vs. PG-CONVINCE-003 in `contradictions-register.md` CONTRADICTION-001.
