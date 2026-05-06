# YC Founder Profile — Summer 2026 (Verbatim)

**Source:** Per-founder profile screenshot from logged-in YC application
**Retrieved:** 2026-05-04
**Acquisition method:** Direct screenshot from active applicant view (Carlos Reuven, Digital Energy)

## Section: Basics

**P-BASICS-1 (required):** Name (full name)
**P-BASICS-2 (required):** Email
**P-BASICS-3 (optional):** Age — dropdown
**P-BASICS-4 (required):** Phone Number — international
- Helper text: "We may use this number to call or text you about your application. International numbers will be called with WhatsApp."
**P-BASICS-5 (optional):** Gender — text field
**P-BASICS-6 (required):** City where you currently live — autocomplete

## Section: Role & Responsibilities

**P-ROLE-1 (required):** "What is your title, or if you haven't set it yet, main responsibility?"
- Helper: "CEO, CTO, Sales, Engineering, etc."

**P-ROLE-2 (required):** "What percent equity do you have?"
- Helper: "If you haven't incorporated yet, give the equity percent you expect to have."

**P-ROLE-3 (required):** "Are you a technical founder?" (Yes/No)
- Helper: "You are a programmer, engineer, or scientist who can build the product without outside assistance."
- **Critical: this is a binary signal partners use to filter for builder presence on the team.**

**P-ROLE-4 (optional):** "Are you currently in school?" (Yes/No)

**P-ROLE-5 (required):** "If accepted to YC, will you commit to working exclusively on this project for the next year?" (Yes/No)
- Helper: "i.e., you won't be in school or have another job"
- **Critical: this is the commitment gate. "No" or qualified answers fail FAQ-003 / ANTI-008 (day-job hedging).**

## Section: Background

**P-BG-1 (required):** Your LinkedIn URL — direct URL field
**P-BG-2 (required):** Education — composite, Add button per entry
- Helper: "Include your college and any advanced degrees. Should you be accepted, we may ask for academic transcripts. If you didn't attend college, list the last school you attended."
- Each entry: institution, degree, field of study, dates
**P-BG-3 (required):** Work History — composite, Add button per entry
- Helper: "Should you be accepted, we may ask for references."
- Each entry: company, role, dates, description
- **Validation banner observed:** "Work history is required" — submission blocked without entries.

## Section: Social Media (all optional)

**P-SOCIAL-1:** Personal website
**P-SOCIAL-2:** Github URL
**P-SOCIAL-3:** Twitter URL

## Section: Accomplishments — THE TWO PG-CANONICAL QUESTIONS

**P-ACC-1 (the wildcard, per /howtoapply):**
> "Please tell us about a time you most successfully hacked some (non-computer) system to your advantage."

This is the question PG references as the wildcard that "can prompt re-evaluation of borderline applications." Strong answers are application-defining for borderline cases.

**P-ACC-2 (the "most important question," per /howtoapply):**
> "Please tell us in one or two sentences about the most impressive thing other than this startup that you have built or achieved."

PG explicitly calls this **"the most important question on the application."** This lives in the per-founder profile, not the main form. Each founder answers separately.

**P-ACC-3 (concrete builds):**
> "Tell us about things you've built before. For example apps you've built, websites, open source contributions. Include URLs if possible."

Long-form, supports multiple URLs / projects.

**P-ACC-4 (formal recognition):**
> "List any competitions/awards you have won, or papers you've published."

Long-form. (Optional — empty acceptable.)

## Critical findings

### Finding 1: PG's "most important question" lives in profile, not main application
**Implication:** Skill must produce per-founder bio outputs that explicitly answer P-ACC-2 with concrete specifics — named achievement, named scale, named outcome. The 1-2 sentence format is a brutal compression test.

### Finding 2: PG's wildcard ("hacked non-computer system") is in profile
**Implication:** Skill must produce a per-founder hack-story output. This is the recovery surface for borderline applications per PG's stated framing on /howtoapply.

### Finding 3: P-ROLE-3 is a binary builder-presence filter
**Implication:** Per ALTMAN-006 (skills split: at least one builder), partners scan profiles for ≥1 founder marked technical = Yes. Solo non-technical founder = serious anti-pattern.

### Finding 4: P-ROLE-5 is the commitment gate
**Implication:** "No" or hedged answer = automatic disqualification. Skill must demand explicit Yes from facts file before drafting profile.

### Finding 5: Work history is required (validation-enforced)
**Implication:** Bio must include at least one work history entry per founder. Empty work history blocks submission. For founders straight from school, entries should include internships / projects / first jobs.

## Atoms (preliminary — Phase 2 multi-passes)

- **PROFILE-001 (the impressive thing — 1-2 sentences):** Tightest constraint in the entire application. PG's "most important question." Skill produces 2-3 candidate variants per founder; user picks.
- **PROFILE-002 (the wildcard hack):** Recovery surface. Strong founders find a non-computer story that demonstrates resourcefulness, defiance of conventional rules, real-world cleverness. Examples in the wild include: gaming the financial aid system, hacking a physical lock with cleverness, exploiting a marketplace inefficiency, social-engineering an interview, running an arbitrage no one else saw.
- **PROFILE-003 (technical founder binary):** Each founder is Yes or No. Application-team summary should show ≥1 Yes. If all founders mark No, that's a kill signal for technical applications; commercial-only teams may survive only if exceptionally strong on customer/distribution.
- **PROFILE-004 (commitment gate):** P-ROLE-5 must be Yes. No exceptions. Hedging here = disqualification.
- **PROFILE-005 (work history requirement):** Each founder needs ≥1 work history entry. Skill validation: error if missing.
- **PROFILE-006 (URL specificity):** P-ACC-3 says "include URLs if possible." Concrete URLs to GitHub repos, deployed apps, published essays, talks given are partner-readable evidence. Bio without URLs underperforms.

## Cross-references

- P-ACC-2 directly satisfies HTA-002 (PG's "most important question")
- P-ACC-1 directly satisfies HTA-003 (the wildcard)
- P-ROLE-3 directly satisfies ALTMAN-006 (builder requirement)
- P-ROLE-5 directly satisfies FAQ-003 + ANTI-008 (commitment, no day-job hedging)
- Work-history-required corroborates ARC-007 (Andersen) on showing concrete prior work
- Cross-reference HTA-002, ALTMAN-004 (formidability via specific evidence) on how to write P-ACC-2

## Coverage matrix updates (Phase 1 closure)

Q-FOUND-1 was previously "per-founder profile — schema not captured." **Now: schema fully captured. Coverage strong.** ≥6 atoms across PG, Altman, multiple alumni.
