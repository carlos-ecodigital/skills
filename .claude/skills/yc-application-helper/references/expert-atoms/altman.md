# Sam Altman — Atomized (v2 — re-extracted with causal-chain protocol)

**Source:** archive/altman-startup-playbook.md
**v2 changes:** ALTMAN-001 + ALTMAN-003 + ALTMAN-008 mechanisms upgraded; 2 new atoms added (ALTMAN-009 TAM-as-ceiling, ALTMAN-010 excitement-as-veto).

**Atom count:** 10 (was 8).

---

## ALTMAN-001 — Love > Like (with sequencing) ⟵ v2 UPGRADED

```yaml
atom_id: ALTMAN-001
source: archive/altman-startup-playbook.md
expert: Sam Altman
applies_to_questions: [Q-PROG-5/6, Q-IDEA-1]
rule_type: rule (with causal sequencing)
confidence: high
when_applies: User-traction questions and idea-quality framing AT YC STAGE. Sequencing: love-testing PRECEDES growth-scaling.
when_does_not_apply: Post-PMF, after love is established and the question is how to scale.
why_it_exists: Causal chain — (1) the binary is love-vs-like, not love-then-scale-vs-scale-direct. (2) "Make something users love. If you do that, then you have to figure out how to get a lot more users" — the IF-THEN structure is the rule. (3) Founders who scale before establishing love produce low-retention growth that looks good in vanity metrics but dies. (4) Founders who establish love first earn the right to scale because they have a load-bearing core to scale FROM. (5) Therefore at YC stage, the question isn't "do you have growth" but "do you have love" — and growth without love is anti-pattern.
underlying_model: Love-testing is a prerequisite, not an alternative. The skill should detect founders who present scale-without-love (e.g., "10k sign-ups but 5 actively using daily") as failing the prerequisite — the small-N who love is the load-bearing signal, not the large-N who once signed up.
contradicts: none; reinforces PG-006 (narrow-deep) via the same intensity logic.
```

> "Make something users love. If you do that, then you have to figure out how to get a lot more users."
> "It's much better to first make a product a small number of users love than a product that a large number of users like."

**Application implication:** Q-PROG-5/6 strong answer cites specific love-evidence (named user using daily, organic referral, paid retention). Anti-pattern: scale-claim without intensity-claim. Skill prioritizes love-evidence over user-count.

---

## ALTMAN-002 — The Excitement Test

```yaml
atom_id: ALTMAN-002
source: archive/altman-startup-playbook.md
expert: Sam Altman
applies_to_questions: [Q-CO-2, Q-CO-7, Q-IDEA-1]
rule_type: validation test
confidence: high
when_applies: Description and idea fields.
when_does_not_apply: Never.
why_it_exists: See ALTMAN-010 for the underlying veto-gate mechanism. Surface rule: zero excitement on first hearing kills the application.
underlying_model: Excitement is partner shorthand for "this could be huge if it works."
contradicts: none.
```

> "If the idea does not really excite at least some people the first time they hear it, that's bad."

**Application implication:** Skill validation: spawn fresh subagent reading Q-CO-2 / Q-IDEA-1 drafts; ask "does this excite you?" Flat-no = restructure.

---

## ALTMAN-003 — Why-Now = Unrealized Shift (with incumbent-blindness mechanism) ⟵ v2 UPGRADED

```yaml
atom_id: ALTMAN-003
source: archive/altman-startup-playbook.md
expert: Sam Altman
applies_to_questions: [Q-IDEA-1, Q-IDEA-2]
rule_type: pattern (positive)
confidence: high
when_applies: "Why now" framing. Strong answers name a shift incumbents have STRUCTURALLY missed.
when_does_not_apply: Mature markets where the shift is already obvious — here why-now must name a sub-shift others haven't seen.
why_it_exists: Causal chain — (1) the why-now is fundable when it's a shift incumbents are STRUCTURALLY incapable of addressing, not just slow. (2) Structural incapability comes from THREE specific sources: (a) BUSINESS-MODEL CONFLICT — addressing the shift cannibalizes existing revenue (e.g., Kodak's film business blocked digital camera commitment), (b) ORGANIZATIONAL CONFLICT — addressing requires a different team type (e.g., AI startups need ML engineers; SaaS incumbents have web engineers), (c) TECHNICAL CONFLICT — addressing requires architecturally different infrastructure (e.g., real-time streaming vs. batch). (3) "Big companies are bad at addressing those" because of these conflicts, not because of ignorance. (4) The strongest why-now answers identify which structural conflict prevents incumbents.
underlying_model: Incumbent inertia is a 3-pronged structural phenomenon, not a generic slowness. Founders who name the specific structural barrier (cannibalization / wrong-team / wrong-architecture) demonstrate they've thought beyond "they're big and slow."
contradicts: none; complements PG-002 (schlep moat).
```

> "We like it when major technological shifts are just starting that most people haven't realized yet — big companies are bad at addressing those."

**Application implication:** Q-IDEA-1 strong answer names: (a) specific shift, (b) WHICH of the 3 structural conflicts blocks incumbents (cannibalization / org / architecture), (c) why this team noticed first. Anti-pattern: generic "big companies are slow" without naming the specific structural barrier.

---

## ALTMAN-004 — The Founder Trait Quartet

```yaml
atom_id: ALTMAN-004
source: archive/altman-startup-playbook.md
expert: Sam Altman
applies_to_questions: [Q-FOUND-1, P-ACC-2, P-ACC-1]
rule_type: rule (founder evaluation)
confidence: high
when_applies: Every founder bio.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) startups face obstacles outside the founder's training and tools. (2) Therefore specific tech-stack experience does not predict success — it predicts only narrow-domain execution. (3) The four traits (unstoppability, determination, formidability, resourcefulness) predict success because they're domain-independent. (4) Each trait must be evidenced via specific named projects shipped through obstacles, not via adjectives — adjectives are claim-of-traits without evidence.
underlying_model: Trait-evidence is behavior under stress, not credentials. P-ACC-1 (wildcard) is purpose-built for resourcefulness; P-ACC-2 (most-impressive) is purpose-built for unstoppability + formidability.
contradicts: none; reinforces PG-010, PG-012.
```

> Essential traits: **"unstoppability, determination, formidability, and resourcefulness."** Specific tech experience does NOT make this list.

**Application implication:** P-ACC-2 must communicate ≥2 of the 4 traits via specific evidence. Skill founder-credibility gate scans for trait-evidence presence (named projects with obstacles overcome), not trait-claims.

---

## ALTMAN-005 — Co-Founder Pre-Existing Relationship

```yaml
atom_id: ALTMAN-005
source: archive/altman-startup-playbook.md
expert: Sam Altman
applies_to_questions: [Q-FOUND-3, P-* (per founder)]
rule_type: rule
confidence: high
when_applies: Multi-founder applications.
when_does_not_apply: Solo applicants — different anti-pattern (ANTI-007).
why_it_exists: Causal chain — (1) startups encounter periods of months-to-years of friction with no immediate reward. (2) Co-founders abandon when the friction exceeds their tolerance for the relationship. (3) Strangers have low relationship-tolerance because they have no prior shared trust. (4) Pre-existing relationships have higher relationship-tolerance because the friction is processed through "I know this person well." (5) Therefore co-founder splits during stress are top-3 startup death cause; pre-existing relationships are the structural defense.
underlying_model: Co-founder durability under stress correlates with prior relationship duration. Partners ask how founders met because they're estimating durability.
contradicts: none.
```

> "You want someone you know well, not someone you just met at a cofounder dating thing."

**Application implication:** Founder bios + Q-FOUND-3 must establish how co-founders know each other and for how long. Anti-pattern: vague "we partnered up" framing.

---

## ALTMAN-006 — Skills Split (Builder + Seller)

```yaml
atom_id: ALTMAN-006
source: archive/altman-startup-playbook.md
expert: Sam Altman
applies_to_questions: [Q-FOUND-1, Q-FOUND-2, P-ROLE-3]
rule_type: rule (team composition)
confidence: high
when_applies: All technical-product applications.
when_does_not_apply: Pure-services / non-product businesses (rare at YC).
why_it_exists: Causal chain — (1) tech startups need both product velocity AND customer acquisition. (2) Product velocity requires builder; customer acquisition requires seller. (3) Outsourcing either is fragile: outsourced product means dependencies break feedback loops; outsourced sales means founder can't iterate the message. (4) Therefore at least one of each must be on the founding team. (5) P-ROLE-3 ("are you a technical founder?" Yes/No) is the binary check on builder presence; seller capability surfaces in P-ACC-3 (prior shipped sales/distribution).
underlying_model: Two structural functions, both founding-team-required. All-builders applications fail at GTM; all-sellers fail at iteration.
contradicts: none.
```

> "Tech startups need at least one founder who can build the company's product or service, and at least one founder who is (or can become) good at sales."

**Application implication:** Application team summary must show ≥1 P-ROLE-3 = Yes. All-No = serious anti-pattern.

---

## ALTMAN-007 — LOIs for Pre-Revenue Enterprise

```yaml
atom_id: ALTMAN-007
source: archive/altman-startup-playbook.md
expert: Sam Altman
applies_to_questions: [Q-PROG-6, Q-IDEA-3, Q-PROG-7/8]
rule_type: rule (substitution for revenue)
confidence: high
when_applies: B2B / enterprise applications pre-revenue.
when_does_not_apply: Consumer applications — replaced by user counts and engagement.
why_it_exists: Causal chain — (1) pre-revenue B2B applications have no demand evidence. (2) Without demand evidence, partners cannot distinguish them from imaginary-demand cases (ANTI-010). (3) LOIs are the lowest-cost concrete demand evidence available pre-revenue: a real customer named in writing committing to evaluate or buy. (4) Securing an LOI requires real customer conversations, which is the PMF-precursor signal partners reward.
underlying_model: LOI substitutes for revenue at enterprise stage because both signal "real customer named, real demand expressed." Revenue is stronger because money has changed hands; LOI is acceptable because the customer-conversation work has been done.
contradicts: none.
```

> "Enterprise solutions: secure letters of intent before building."

**Application implication:** Pre-revenue B2B applications without LOIs face a credibility gap. Skill flags this gap and recommends LOI acquisition before submission.

---

## ALTMAN-008 — Do Things That Don't Scale (with sensory mechanism) ⟵ v2 UPGRADED

```yaml
atom_id: ALTMAN-008
source: archive/altman-startup-playbook.md
expert: Sam Altman (canonical PG framing)
applies_to_questions: [Q-PROG-1, Q-PROG-5/6, Q-IDEA-1]
rule_type: heuristic (counterintuitive, with sensory-detail mechanism)
confidence: high
when_applies: Any traction or user-acquisition framing at YC stage.
when_does_not_apply: Post-PMF where scale matters more than depth.
why_it_exists: Causal chain — (1) the data-collection regime that produces real PMF insight requires founder-user contact at the individual level. (2) Surveys + analytics dashboards produce SUMMARIZED data — counts, percentages, aggregate patterns. (3) Summarized data hides the micro-problems that kill products: "the button is in the wrong place," "the loading state is confusing," "I almost gave up at step 3." (4) Direct observation ("Sit in their office") reveals these micro-problems because the founder watches the user struggle in real time. (5) Therefore the directive isn't generic "be hands-on" — it's specifically about FIRSTHAND OBSERVATION as the data source that surveys cannot replace.
underlying_model: Manual user acquisition is incidentally important; firsthand observation is the LOAD-BEARING mechanism. Skill should emphasize observation evidence over interview evidence — the founder describing a specific user's specific moment of struggle is the partner-readable signal.
contradicts: none.
```

> "Literally watch them use your product. Sit in their office if you can."
> "Do things that don't scale."

**Application implication:** Q-PROG-1 / Q-PROG-5/6 strong answer cites specific observation moments ("watched user X get stuck on Y for Z minutes"), not just acquisition counts. Anti-pattern: "we plan to acquire via SEO/ads/virality" without prior observation evidence.

---

## ALTMAN-009 — TAM as Ceiling on Expansion (NEW — was missing in v1)

```yaml
atom_id: ALTMAN-009
source: archive/altman-startup-playbook.md (TAM-mention extracted as standalone atom)
expert: Sam Altman
applies_to_questions: [Q-IDEA-3, Q-PROG-1]
rule_type: rule (stage-conditional, distinct from PG-006)
confidence: high
when_applies: Q-IDEA-3 ("how much could you make?") — when the application has demonstrated narrow-deep beachhead and is articulating expansion.
when_does_not_apply: Pre-PMF where PG-006 (intensity, not breadth) applies. The two rules are NOT contradictory — they apply to different sections of the same application: Q-PROG-5/6 follows PG-006; Q-IDEA-3 invokes ALTMAN-009.
why_it_exists: Causal chain — (1) at YC stage, partners care about narrow-deep traction. (2) BUT they also care that the company COULD become large eventually. (3) TAM is the ceiling: how big can the company become if the beachhead expands successfully? (4) A narrow-deep startup with no plausible expansion path is a small business, not a venture. (5) Therefore Q-IDEA-3 must show: (a) narrow-deep current focus (per PG-006), (b) credible expansion path that touches a meaningfully large TAM. (6) Both halves required.
underlying_model: PG-006 is about NOW; ALTMAN-009 is about LATER. Strong applications carry both. Weak applications either lead with TAM (failing PG-006 at YC stage) or lead with narrow without expansion (failing ALTMAN-009 on venture-scale).
contradicts: PG-006 at apparent surface — actually stage-conditional. Documented in `contradictions-register.md` CONTRADICTION-001 as resolved via stage-conditional logic.
```

> "TAM sets upper bound on company size. Market needn't be large today, but must show credible expansion sequence."

**Application implication:** Q-IDEA-3 strong answer: lead with narrow-deep beachhead, then describe credible expansion path. Both halves required. Skill validates Q-IDEA-3 contains BOTH narrow-deep evidence AND expansion-path articulation.

---

## ALTMAN-010 — Excitement as Veto-Gate (NEW — was missing in v1)

```yaml
atom_id: ALTMAN-010
source: archive/altman-startup-playbook.md (excitement-test mechanism, distinct from ALTMAN-002 surface rule)
expert: Sam Altman
applies_to_questions: [Q-CO-2, Q-CO-7, Q-IDEA-1]
rule_type: rule (veto criterion)
confidence: high
when_applies: Description and idea fields. Underlying mechanism for ALTMAN-002.
when_does_not_apply: Never.
why_it_exists: Causal chain — (1) excitement on first hearing isn't a refinement dimension that improves the application — it's a veto criterion that disqualifies. (2) An application that fails the excitement test cannot be SAVED by strong traction or strong founders, because partners need a reason to push for the interview slot beyond their own conviction. (3) Without excitement, partners have to defend the application internally against the partner roster — and "this could be huge if it works" is the only sustainable defense. (4) Therefore excitement isn't optional; its absence is structurally disqualifying.
underlying_model: ALTMAN-002 says "excitement matters." ALTMAN-010 says "excitement is the veto gate, not a quality dimension." Distinction matters because ALTMAN-002 alone reads as "polish it up"; ALTMAN-010 reads as "without this, polish doesn't help."
contradicts: none.
```

> "If the idea doesn't really excite at least some people the first time they hear it, that's bad" — interpreted as veto, not refinement.

**Application implication:** Skill treats excitement-test failure as binary disqualifier. If a draft gets "flat-no" from fresh-subagent excitement test, the response is restructure (not polish).

---

## Summary

**Atoms:** 10 (8 from v1 + 2 new ALTMAN-009/010; ALTMAN-001/003/008 upgraded with mechanisms)
**Coverage:** Q-CO-2, Q-CO-7, Q-IDEA-1, Q-IDEA-2, Q-IDEA-3, Q-PROG-1, Q-PROG-5/6, Q-PROG-7/8, Q-FOUND-1/2/3, P-ROLE-3, P-ACC-1/2/3
