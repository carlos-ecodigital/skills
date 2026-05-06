# Partner Evaluation Criteria — The Rubric

**Distilled from atoms in `expert-atoms/`. This file is the partner-simulation rubric for Phase 5C and the per-question gate reference.**

## The 3 Dimensions (Paul Graham, How to Convince Investors)

Per PG-010, partners evaluate startups across three dimensions, weighted in this order:

### Dimension 1 — Formidable Founders (DOMINANT)
- Founder "seems like they'll get what they want, regardless of obstacles"
- Most decisions happen within minutes; first impressions difficult to reverse
- 4 traits per ALTMAN-004: unstoppability, determination, formidability, resourcefulness
- Evidence required: specific named prior projects with verifiable outcomes (PG-012, ARC-013)
- Tested via: P-ACC-1 (wildcard / resourcefulness), P-ACC-2 (most-impressive-thing / formidability), P-ACC-3 (things built / determination)

### Dimension 2 — Promising Market
- Credible expansion sequence (PG-CONVINCE-003)
- Market need not be large *today*; must show plausible expansion path
- Why-now = unrealized shift incumbents have missed (ALTMAN-003)
- Pre-PMF: narrow-and-deep beats broad-and-shallow (PG-006)
- Tested via: Q-IDEA-1 (why), Q-IDEA-2 (competitors / what others don't understand), Q-IDEA-3 (how make money)

### Dimension 3 — Evidence of Traction
- Early stage: promising experiments (manual user acquisition, named user love, LOIs)
- Mature stage: experiments that worked (retention, revenue trajectory)
- Metric priority order (ARC-019): profit > revenue > usage > users > audience
- Pre-revenue B2B substitute: LOIs (ALTMAN-007)
- Tested via: Q-PROG-1, Q-PROG-5/6, Q-PROG-7/8, Q-PROG-9

## The 8 Verification Gates (skill applies per draft)

Per the architecture (Phase 3F):

1. **Word/character limit** — Q-CO-2 ≤50 chars, total app ≤3-min read time (ARC-001)
2. **Concreteness gate** — every claim has specific anchor (name, number, date) per ARC-021, ARC-025
3. **Founder-credibility gate** — bios contain ≥2 named prior projects with verifiable outcomes per PG-012, ALTMAN-004
4. **Brevity gate** — total reads in ≤3 min per ARC-001, PG-009
5. **Anti-pattern detection** — draft scanned against `anti-patterns.md` ANTI-001 through ANTI-014
6. **Anti-fabrication gate** — every factual claim traces to `company-facts.md` line
7. **Nuance preservation gate** — drafts reflect relevant `when_does_not_apply` conditions from cited atoms
8. **Partner-simulation gate (Phase 5C)** — fresh subagent role-plays YC partner reading

## Per-Question Evaluation Patterns

### Q-CO-2 (50-char description) — "the most leveraged sentence"
- Pass: noun-led, plain language, specific user, specific verb (HALE-006)
- Fail: marketing-speak, "platform," "revolutionize" (HALE-005, SEIBEL-001)
- Fail: pre-amble ("We're building...", "Imagine...") (HALE-007)
- Test: mom-test (HALE-004) — non-expert understands?

### Q-CO-7 (what your company makes)
- Pass: matter-of-fact (HALE-002), specific functionality in stages (ARC-021)
- Pass: name the flaws preemptively (ARC-022)
- Fail: same anti-vocabulary as Q-CO-2 plus "synergy/disrupt" cluster

### Q-IDEA-1 (why this idea / domain expertise / how know people need it)
- Pass: organic origin story, founder lived in the future (PG-004), schlep encountered (PG-001)
- Pass: 3 components present (HALE-001) — problem, solution, insight
- Pass: 4 ANTI-009 elements present — why-exists, who-suffers, why-unsolved, why-now
- Fail: sitcom-idea (PG-005), incumbent-substitute (ANTI-004), untested (ANTI-012), hedged (ANTI-005)

### Q-IDEA-2 (competitors / what others don't understand)
- Pass: explicit paradigm shift, schlep-as-moat (PG-002), named flaws acknowledged (ARC-022)
- Fail: feature comparison without paradigm shift, "we'll be 10% better"

### Q-IDEA-3 (how make money / how much)
- Pass: business-model precision (SEIBEL-003), specific metric (ARC-019), TAM-as-ceiling-not-gate (PG-CONVINCE-003)
- Fail: vague ARR projections, "10% of $1T market"

### Q-IDEA-5 (other ideas) — partner-stated highest-leverage
- Form quote: "Often when we fund people it's because of something they list here and not in the main application."
- Pass: ≥2 alternate ideas with specific reasoning, each at the same quality bar as the main idea
- Fail: empty / single throwaway

### Q-PROG-5/6 (users)
- Pass: named users with engagement evidence (ALTMAN-001, PG-006)
- Pass: manual acquisition methods cited (ALTMAN-008)
- Fail: bare sign-up counts without engagement, "we plan to acquire via SEO"

### Q-PROG-7/8 (revenue with monthly breakdown)
- Pass: honest 6-month trajectory; growth >5x annually compensates for unprofitability (PG-AORD-005)
- Fail: stagnant or declining months (visible to partners), inflated single-customer = "ARR"

### Q-VIDEO-1 (founder video)
- Format spec: 60s, founders on camera, no music/effects (ARC-029)
- Content spec: founders speak, no narration over visuals (ARC-029)
- Tone: sincere, earnest (SEIBEL-005)
- Anti-pattern: product demo as founder video (ANTI-011)

### P-ACC-1 (the wildcard, per-founder profile)
- PG: strong answers prompt re-evaluation of borderline applications (HTA-003)
- Pattern: specific resourceful exploit of a non-computer system (financial/social/physical/regulatory)
- Anti-pattern: tech-only example, vague "I figured out a way to..."

### P-ACC-2 (the most-important-question, per-founder profile)
- PG: "the most important question on the application"
- Pattern: 1-2 sentences naming specific thing built/achieved + scale (number, named users, recognition) + completed (not aspirational)
- Anti-pattern: adjective-only ("I am driven"), aspirational ("I am building..."), vague ("I led a team that did big things")

## Crusoe Test (synthesis pattern)

For any answer, the skill applies a "Crusoe test" — would this answer survive a partner who has seen 1000+ applications recognizing the pattern?
- If the answer matches a common rejection pattern (ANTI-001 to ANTI-013), partner pattern-matches negatively
- If the answer is genuinely novel + concrete + evidenced, partner pattern-matches positively
- The skill's job is to pull every answer toward the latter side
