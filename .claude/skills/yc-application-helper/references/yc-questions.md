# YC Application — Question Set, Intent, Atom Pointers

**Source of truth:** `archive/yc-application-questions-summer-2026.md` (verbatim from active form, 2026-05-04)
**Per-founder profile source:** `archive/yc-founder-profile-summer-2026.md`
**Schema version:** Summer 2026
**Refresh trigger:** start of every YC batch cycle, or any partner-disclosed schema change

This file pre-loads, per question: verbatim text, what YC partners are testing, word/character limits, and pointers to relevant atoms in `expert-atoms/`, `anti-patterns.md`, and `successful-patterns/`. The skill loads this file as the entry point for any per-question drafting.

---

## Section: Founders (main form)

### Q-FOUND-1 — Per-founder profile completion (gating)
**Form text:** Each founder must complete their own profile separately. Submission is blocked if any founder profile is incomplete (validation banner observed: "Founders info is required").

**What partners test:** Each founder's individual credibility, commitment, technical capacity, prior shipped work. The per-founder profile carries PG-canonical questions (P-ACC-1, P-ACC-2 — see Per-Founder Profile section below).

**Word/char limits:** Variable per profile sub-question.

**Atom pointers:**
- Anchor rule: see profile section below
- Bios must be evidence-led, not adjective-led: `expert-atoms/graham.md` PG-010, `expert-atoms/altman.md` ALTMAN-004
- Multi-founder coordination: `expert-atoms/altman.md` ALTMAN-005
- Skills split (≥1 builder, ≥1 seller): `expert-atoms/altman.md` ALTMAN-006
- **5x technical-talent multiplier**: `expert-atoms/caldwell.md` CALDWELL-009 (Caldwell explicit: at least one founder at top-YC-company hireable level = 5x interview odds; internships at Stripe/Airbnb count)
- **Story-framework partner mental model**: `expert-atoms/caldwell.md` CALDWELL-008 (partner reads bios constructing characters/setting/trajectory; obfuscation = no story = rejection)
- Anti-pattern (no work history, no co-founder strategy): `anti-patterns.md` ANTI-007

### Q-FOUND-2 — Technical work attribution
**Form text:** "Have any of you written code, or done other technical work on your product? If you have, which of [it] was done by a non-founder? Please explain."

**What partners test:** Whether the founding team has the skills to build the product themselves, or whether work has been outsourced. FAQ states: "It's important for the founding team to have the skills to build their product themselves, rather than outsourcing it to someone else."

**Word/char limits:** Free-text, partner-readable in seconds.

**Atom pointers:**
- Faq baseline: `archive/yc-faq-application.md` FAQ-002
- Partner expectation: `expert-atoms/altman.md` ALTMAN-006 (≥1 builder)
- Anti-pattern: outsourced product = serious flag

### Q-FOUND-3 — Looking for co-founder
**Form text:** "Are you looking for a co-founder?"

**What partners test:** For solo founders — whether they recognize the structural disadvantage and have a plan. For multi-founder teams — typically marked No.

**Atom pointers:**
- Solo OK but disadvantaged: `archive/yc-faq-application.md` FAQ-001
- Anti-pattern (solo without strategy): `anti-patterns.md` ANTI-007
- Co-founder relationship quality: `expert-atoms/altman.md` ALTMAN-005
- **Co-founder matching as partner-endorsed remedy**: `expert-atoms/caldwell.md` CALDWELL-016 (non-technical solos / non-technical teams should reference YC's co-founder matching tool)

---

## Section: Founder Video (main form)

### Q-VIDEO-1 — Founder video
**Form text:** Upload founder video. (Per /howtoapply and arc-31 tip 29: ~1 minute, all founders on camera, YouTube-hostable, no fancy effects/music.)

**What partners test:** Communication ability, founder presence, sincerity. Per Seibel via interview prep: "be earnest" / "be sincere, straightforward and natural." Anti-pattern: product-focused video instead of founder-focused.

**Word/char limits:** ~60 seconds = ~150 spoken words.

**Atom pointers:**
- Format spec: `expert-atoms/multiple-alumni.md` ARC-029 (Andersen)
- Format compliance signals (1 min, all founders, deviations interpreted): `expert-atoms/caldwell.md` CALDWELL-004
- **No adversarial / Shark-Tank register**: `expert-atoms/caldwell.md` CALDWELL-010 (memorized speeches, "Hello people, we are here to tell you about X" backfire)
- **Authenticity as positive signal**: `expert-atoms/caldwell.md` CALDWELL-015 (positive complement to CALDWELL-010 — "be yourself, not Shark Tank")
- Founders, not product: `anti-patterns.md` ANTI-011
- Sincerity > polish: `expert-atoms/seibel.md` SEIBEL-005 (interviews framing carries to video)
- Founder formidability via specific evidence: `expert-atoms/altman.md` ALTMAN-004
- Increases interview likelihood: `archive/yc-howtoapply-page.md` HTA-best-practices

---

## Section: Company (main form)

### Q-CO-2 — 50-character description (THE leverage question)
**Form text:** "Describe what your company does in 50 characters or less."
**Limit:** **50 characters**

**What partners test:** Whether you can compress your idea to its essence. Partners read ~100 applications/day at ~5 min each. This is the sentence they use to decide whether to keep reading.

**Atom pointers:**
- Anchor rule (lead with what, not why or how): `expert-atoms/hale.md` HALE-002
- Concrete description format: `expert-atoms/hale.md` HALE-006 + concrete examples Airbnb/Dropbox/Lumini
- Anti-marketing-speak: `expert-atoms/hale.md` HALE-005, `expert-atoms/seibel.md` SEIBEL-001, `expert-atoms/multiple-alumni.md` ARC-003/004
- X-for-Y conditional: `expert-atoms/hale.md` HALE-003
- Excitement test: `expert-atoms/altman.md` ALTMAN-002
- Clarity = competence: `expert-atoms/graham.md` PG-009
- Mom test for clarity: `expert-atoms/hale.md` HALE-004

### Q-CO-7 — What your company is going to make
**Form text:** "What is your company going to make? Please describe your product and what it does or will do."

**What partners test:** Concrete product comprehension. Are you building something specific or hand-waving?

**Atom pointers:**
- Matter-of-fact: `archive/yc-howtoapply-page.md` (PG: "matter-of-fact descriptions")
- Lead with what: `expert-atoms/hale.md` HALE-002
- Specific functionality in stages: `expert-atoms/multiple-alumni.md` ARC-021 (Chen, Ridejoy)
- Name the flaws: `expert-atoms/multiple-alumni.md` ARC-022
- Anti-pattern (marketing-speak, jargon, "platform," "the X of Y"): `expert-atoms/hale.md` HALE-005

### Q-CO-8/9 — Location
**Form text:** "Where do you live now, and where would the company be based after YC? (Use the format City A, Country A / City B, Country B)" + "Explain your decision regarding location."

**What partners test:** Commitment to SF / YC ecosystem. Hedged answers signal half-commitment.

**Atom pointers:**
- SF advantage: `expert-atoms/multiple-alumni.md` ARC-016 (PG SV)
- (Limited atom coverage; primarily a factual-disclosure question)

---

## Section: Progress (main form)

### Q-PROG-1 — How far along
**Atom pointers:** PG-005 (who-wants-this-now test), ALTMAN-007 (LOIs for enterprise pre-rev), ALTMAN-008 (do things that don't scale), ARC-013/018/019/025/026, ANTI-002 (ceremony over building)

### Q-PROG-2 — Full-time / time spent
**Atom pointers:** FAQ-003 (full-time commitment expected), ANTI-008 (day job hedging), ARC-027 (efficient progress)

### Q-PROG-3 — Tech stack
**What partners test:** Builder credibility, modern tooling fluency. AI-native expectation.
**Atom pointers:** Limited — partners care about transparency. Cross-reference Q-PROG-4 (coding agent session).

### Q-PROG-4 — Coding agent session [NEW Summer 2026]
**Form text:** "Optional - attach a coding agent session you're particularly proud of."
**Form helper:** "This is a special prompt for the Summer 2026 batch to give people a chance to show off the skills with using tools."

**What partners test:** AI-native fluency. Whether the founder uses modern coding agents (Claude Code, Cursor, etc.) effectively. Validates alignment with YC partner roster's own current building practice (per Lightcone-coding-agent-context atom).

**"Optional" warning:** Despite the label, AI-native technical applicants should treat this as MANDATORY. Per LC-001/LC-002.

**Atom pointers:**
- New-question framing: `archive/yc-application-questions-summer-2026.md` APP-Q-002
- YC-ecosystem alignment: `archive/lightcone-coding-agent-context.md` LC-001/LC-002
- Plan-mode default: `expert-atoms/lightcone-cherny.md` LC-001
- Pair-with-model not pure-vibe: LC-002
- Selective hand-coding for opinionated parts: LC-003
- Multi-agent parallel orchestration: LC-004
- Quality bar invariance: LC-005
- Custom workflow tooling (slash commands, stop hooks): LC-006
- Subagent competitive critique: LC-007
- Judgment at checkpoints: LC-008
- Show-don't-tell craft: `expert-atoms/altman.md` ALTMAN-008
- Empirical 5x technical-talent multiplier: `expert-atoms/caldwell.md` CALDWELL-009 (relevant when Q-PROG-4 is the proxy for technical fluency)

### Q-PROG-5/6 — Users / paying customers
**Atom pointers:** SEIBEL-002 (own-PMF self-knowledge), ALTMAN-001 (love > like), PG-006 (narrow-deep > broad-shallow), PG-005 (who-wants-this-now), ARC-018/019, ANTI-003 (lack of social proof and traction — verbatim partner-stated rejection reason), ANTI-010 (imaginary demand), **CALDWELL-014 (mastery-probe interview signal — drafts must contain substance defensible in 10-min live conversation)**

### Q-PROG-7/8 — Revenue (with 6-month USD breakdown)
**Atom pointers:** SEIBEL-003 (business-model precision), SEIBEL-006 ($150-250K MRR for Series A), PG-007 (default alive test), PG-007 (>5x growth), ARC-019, ARC-025 (PG: numbers stick in heads, limit 4-5), **CALDWELL-014 (mastery-probe — numbers must cohere across sections), CALDWELL-013 (no misrepresentation — monthly framed as annual = automatic disqualification)**

### Q-PROG-9 — Revenue source breakdown
**Atom pointers:** SEIBEL-003 (categorize honestly), ARC-019 (priority: profit > revenue > usage > users > audience)

### Q-PROG-11 — Re-applicant
**Atom pointers:** FAQ-008 (encouraged to re-apply), PG-011 (address rejection head-on), PG-011b (narrative control), CALDWELL-005 (33% accepted previously rejected), **CALDWELL-011 (feedback internalization heavily weighted; demand specific YC feedback + measurable changes)**

### Q-PROG-12 — Other accelerators
**Atom pointers:** PG-011 (don't hide rejections; explain why they were mistaken), CALDWELL-007 (predatory advisor caution if applicable)

---

## Section: Idea (main form)

### Q-IDEA-1 — Why this idea / domain expertise / how do you know people need it (THE most-atomized question)
**Form text:** "Why did you pick this idea to work on? Do you have domain expertise in this area? How do you know people need what you're making?"

**What partners test:** Whether the idea is organic (founder-experienced) or made-up (sitcom). Whether the founder has lived in the future. Whether they've stress-tested with real humans.

**Atom pointers:**
- Don't think, notice: `expert-atoms/graham.md` PG-003 (3-test: want + can build + few realize)
- Live in the future: `expert-atoms/graham.md` PG-004
- Organic > made-up: `expert-atoms/graham.md` PG-005
- Schlep willingness: `expert-atoms/graham.md` PG-001 (the "what do I wish someone else would solve for me" reframe)
- Schlep as moat: `expert-atoms/graham.md` PG-002
- Excitement test: `expert-atoms/altman.md` ALTMAN-002
- Why-now = unrealized shift: `expert-atoms/altman.md` ALTMAN-003
- 3 components (Problem, Solution, Insight): `expert-atoms/hale.md` HALE-001
- Domain knowledge: `expert-atoms/multiple-alumni.md` ARC-023 (Lee, RentHop)
- Anti-patterns: `anti-patterns.md` ANTI-004 (incumbent-substitute), ANTI-009 (unprecise problem), ANTI-012 (untested), ANTI-005 ("I don't have a good answer")

### Q-IDEA-2 — Competitors / what you understand others don't
**Atom pointers:** PG /howtoapply (insight over novelty), HALE-001 (insight = unfair advantage), ALTMAN-003 (why-now = unrealized shift), PG-002 (schlep willingness as differentiation), ARC-022 (name flaws preempt counterargs), ANTI-004 (paradigm vs incremental)

### Q-IDEA-3 — How will you make money / how much
**Atom pointers:** ALTMAN-007 (LOIs for enterprise), SEIBEL-003 (B2B-vs-Enterprise-vs-SaaS precision), ARC-019 (metric priority), PG-007 (default alive logic), ALTMAN-009 (TAM = ceiling, not gate)

### Q-IDEA-5 — Other ideas considered (form-stated high-leverage)
**Form-stated quote:** "Often when we fund people it's because of something they list here and not in the main application."

**Atom pointers:** ARC-028 (alternate ideas as conversation surface), application-form quote APP-Q-004 (highest-leverage signal in form)

---

## Section: Equity / Funding (main form)

Q-EQ-1 through Q-EQ-11 are largely factual disclosure. Atom pointers limited; primary risk is precision.

**Atom pointers:**
- Default alive math: `expert-atoms/graham.md` PG-007
- Hiring anti-pattern: PG-008 (hiring too fast), PG-008 (Airbnb 4-month-no-hire counterexample)
- Address prior rejections: PG-011 + PG-011b
- **Misrepresentation = automatic disqualification**: `expert-atoms/caldwell.md` CALDWELL-013 — specific kill case: monthly revenue framed as annual. Skill anti-fabrication gate is BINARY at this question type, not graduated.
- Extraordinary claims = extraordinary evidence: CALDWELL-012 (any large named-customer / large dollar / prestigious-credential claim must trace to verifiable evidence in facts file)

---

## Section: Curious + Batch Preference (main form)

Soft questions; minimal atom density. Treat as low-leverage factual disclosure.

---

## Per-Founder Profile (separate form, gating submission)

### P-BASICS-1 to P-BASICS-6 — Name, email, age, phone, gender, city
Factual; no atoms.

### P-ROLE-1 — Title / main responsibility
Factual.

### P-ROLE-2 — Equity percent
Factual; cross-check with Q-EQ-3 (founder equity breakdown) for consistency.

### P-ROLE-3 — Are you a technical founder? (Yes/No, gating filter)
**Atom pointers:** ALTMAN-006 (≥1 builder required); team summary should show ≥1 Yes; all-No applications fail unless exceptional commercial-only case made.

### P-ROLE-5 — Will you commit exclusively for next year? (Yes/No, the commitment gate)
**Atom pointers:** FAQ-003 (full-time expected), ANTI-008 (no day-job hedging). Hedged or No = disqualification.

### P-BG-1 — LinkedIn URL (required)
Factual.

### P-BG-2 — Education (required, ≥1 entry)
Factual; partners may request transcripts post-acceptance.

### P-BG-3 — Work history (required, ≥1 entry — validation-enforced)
**Atom pointers:** ARC-013/014 (show what you've done, complementary strengths); ANTI-006 (no prior shipped work = anti-pattern); ALTMAN-004 (formidability via specific evidence)

### P-ACC-1 — The wildcard (PG-canonical)
**Form text:** "Please tell us about a time you most successfully hacked some (non-computer) system to your advantage."

**What partners test (verbatim PG via /howtoapply):** Strong answers can prompt re-evaluation of borderline applications. The wildcard is a recovery surface.

**Atom pointers:**
- HTA-003 (the wildcard itself)
- PROFILE-002 (resourcefulness signal — what good answers look like)
- Reinforces ALTMAN-004 (resourcefulness as core founder trait)

### P-ACC-2 — The most important question (PG-canonical)
**Form text:** "Please tell us in one or two sentences about the most impressive thing other than this startup that you have built or achieved."

**What partners test (verbatim PG via /howtoapply):** PG explicitly calls this "the most important question on the application." Founder credibility anchor.

**Atom pointers:**
- HTA-002 (PG: most-important-question framing)
- PROFILE-001 (1-2 sentence brutal compression test)
- ALTMAN-004 (formidability via specific evidence)
- PG-010 (founder formidability is #1 dimension)
- ARC-013 (show what you've done)

### P-ACC-3 — Things you've built before
**Atom pointers:** ARC-013/015 (online presence, GitHub), URL specificity (PROFILE-006)

### P-ACC-4 — Competitions / awards / papers
Optional, low-stakes.

---

## Atom-pointer index (placeholder until per-expert files complete)

The pointers above reference atoms in:
- `expert-atoms/graham.md` (PG-* atoms)
- `expert-atoms/altman.md` (ALTMAN-* atoms)
- `expert-atoms/hale.md` (HALE-* atoms)
- `expert-atoms/seibel.md` (SEIBEL-* atoms)
- `expert-atoms/multiple-alumni.md` (ARC-* atoms — Buchheit, Taggar, Andersen, Shen, etc.)
- `anti-patterns.md` (ANTI-* atoms)
- `archive/yc-faq-application.md` (FAQ-* atoms)
- `archive/yc-howtoapply-page.md` (HTA-* atoms)
- `archive/lightcone-coding-agent-context.md` (LC-* atoms)
- `archive/yc-application-questions-summer-2026.md` (APP-Q-* atoms)
- `archive/yc-founder-profile-summer-2026.md` (PROFILE-* atoms)
