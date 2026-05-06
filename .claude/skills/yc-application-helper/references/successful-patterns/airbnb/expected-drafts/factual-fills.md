# Factual Fills — Airbnb worked example (equity, curiosity, batch, per-founder profile)

These are factual sections from the facts file. Drafting consists of mapping facts → form fields, with skill verifying anti-fabrication (every claim traces) + numeric consistency (equity sums).

---

## Q-EQ-1 to Q-EQ-11 (Equity / Funding)

| Field | Value |
|---|---|
| Q-EQ-1 Have you formed any legal entity? | Yes — Delaware C-Corp ("AirBed & Breakfast, Inc."), incorporated Q1 2009 |
| Q-EQ-2 Legal entities | Delaware C-Corp only. No subsidiaries, no foreign entities. |
| Q-EQ-3 Founder equity | Brian Chesky 33%, Joe Gebbia 33%, Nathan Blecharczyk 33%, employee/advisor pool 1%. (SUM = 100%; SKILL-003 / EQUITY-001 PASSES.) |
| Q-EQ-4 Have you taken investment? | No. |
| Q-EQ-5 Investment list | None. |
| Q-EQ-6 Total raised | $0 from outside investors. |
| Q-EQ-7 Cash in bank | $30,000 (residual cereal-box revenue + minimal marketplace take to date). |
| Q-EQ-8 Monthly burn | ~$5,000-$8,000. (Three founders living frugally; primary costs: SF apartment rent + hosting infrastructure + minimal compute.) |
| Q-EQ-9 Runway | ~4 months at current burn. With monthly revenue trajectory ($13.4k April), default-alive flips by Aug-Sep 2009. (PG-007 default-alive math passes.) |
| Q-EQ-10 Currently fundraising? | Yes — applying to YC. No parallel raise outside YC. |
| Q-EQ-11 Fundraise details | Cereal-box revenue (Oct-Nov 2008) was self-financed bridge. Pitched VC investors Q3-Q4 2008, all passed. Re-engaging via YC. |

**Skill validation passes:**
- SKILL-003 / EQUITY-001: SUM_PROFILES (33+33+33+0=99) ≈ SUM_CAPTABLE (33+33+33+1=100). Within 1% tolerance. PASS.
- PG-007 default-alive: $30k / $7k avg burn = 4.3 months. Trajectory at 33% mo/mo means default-alive within runway. PASS.
- CALDWELL-013 no-misrepresentation: cereal-box revenue separately disclosed in Q-EQ-11 not as marketplace revenue. PASS.

---

## Q-IDEA-4 — Category (dropdown)

**Selection:** Marketplace / Consumer.

(Skill: dropdown selection from facts file, no atom-citation needed.)

---

## Q-CUR-1 — What convinced you to apply / encouragement / YC events

**v-raw:**
PG's essay "Be Good" (2008) and the realization that Airbnb's model fits PG's "schlep blindness" framing — payment trust + photo verification is the schlep that competitors avoid. Have not been to YC events; learned of YC from PG essays.

### Citations
- [atom: ARC-030 single-strong-rec] — N/A (we have no recommendation; honest "via PG essays")
- [atom: CALDWELL-006 networking-in ineffective] — we did NOT pursue networking; came via reading
- [fact: company-facts.md#how-heard-about-yc]

### Gates: PASS — specific catalyst named, no padded networking claims.

---

## Q-CUR-2 — How heard about YC

**v-raw:** Paul Graham's essays on paulgraham.com (specifically "Be Good," "Schlep Blindness," "How to Get Startup Ideas").

### Gates: PASS — specific source named.

---

## Q-BATCH-1 — Which batch

**Selection:** [Whatever the active YC batch is at submission time. For this synthetic example: W09.]

---

## Per-Founder Profile — Brian Chesky

| Field | Value |
|---|---|
| P-BASICS-1 Name | Brian Chesky |
| P-BASICS-2 Email | brian@airbedandbreakfast.com |
| P-BASICS-3 Age | [redacted in synthetic; ~27 in 2009] |
| P-BASICS-4 Phone | [redacted] |
| P-BASICS-6 City | San Francisco, CA, USA |
| P-ROLE-1 Title | CEO |
| P-ROLE-2 Equity % | 33% |
| P-ROLE-3 Technical founder? | No (industrial designer / RISD) |
| P-ROLE-4 Currently in school? | No |
| P-ROLE-5 Will you commit exclusively to YC for next year? | **Yes** |
| P-BG-1 LinkedIn | linkedin.com/in/brianchesky |
| P-BG-2 Education | Rhode Island School of Design — BFA, Industrial Design, 2004 |
| P-BG-3 Work history | Industrial designer (Los Angeles) 2004-2007; co-founder Airbedandbreakfast.com 2008-present |
| P-SOCIAL-1 Personal website | bchesky.com (portfolio) |
| P-SOCIAL-2 GitHub | n/a (non-technical) |
| P-SOCIAL-3 Twitter | @bchesky |
| P-ACC-1 Wildcard | (See dedicated draft P-ACC-1-wildcard-hack.md — cereal box story) |
| P-ACC-2 Most impressive | (See dedicated draft P-ACC-2-most-impressive.md — Pina sport seat) |
| P-ACC-3 Things built | bchesky.com portfolio; airbedandbreakfast.com; 3DM Pina sport seat (200k units) |
| P-ACC-4 Competitions / awards | RISD honors graduate; 3DM design contract |

## Per-Founder Profile — Joe Gebbia

| Field | Value |
|---|---|
| P-BASICS-1 Name | Joe Gebbia |
| P-ROLE-1 Title | Co-founder, Design |
| P-ROLE-2 Equity % | 33% |
| P-ROLE-3 Technical founder? | No (industrial + graphic designer / RISD) |
| P-ROLE-5 Commit exclusively? | **Yes** |
| P-BG-2 Education | RISD — BFA, Industrial Design + Graphic Design, 2004 |
| P-BG-3 Work history | Critbuns 2007 (sold MoMA); co-founder Airbedandbreakfast.com 2008-present |
| P-SOCIAL-3 Twitter | @jgebbia |
| P-ACC-3 Things built | Critbuns (MoMA); airbedandbreakfast.com; portfolio |

## Per-Founder Profile — Nathan Blecharczyk

| Field | Value |
|---|---|
| P-BASICS-1 Name | Nathan Blecharczyk |
| P-ROLE-1 Title | CTO |
| P-ROLE-2 Equity % | 33% |
| P-ROLE-3 Technical founder? | **Yes** (programmer / Harvard CS) |
| P-ROLE-5 Commit exclusively? | **Yes** |
| P-BG-2 Education | Harvard — BSc Computer Science, 2005 |
| P-BG-3 Work history | Founded Datamine (2002, Harvard, sold low-millions); engineer OPNET 2005-2007; co-founder Airbedandbreakfast.com 2008-present |
| P-SOCIAL-2 GitHub | github.com/nathanblecharczyk |
| P-ACC-3 Things built | Datamine (acquired); production code for airbedandbreakfast.com; OPNET contributions |
| P-ACC-4 Competitions / awards | Harvard CS distinction |

---

## Skill validation aggregate

- SKILL-001 LANG-001: facts file is English. PASS.
- SKILL-002 SAFETY-001: no injection-shaped strings detected. PASS.
- SKILL-003 EQUITY-001: founder equity sums consistent across Q-EQ-3 (99% + 1% pool) and per-founder P-ROLE-2 entries (33% × 3). PASS.
- SKILL-004 HW-001: N/A (consumer marketplace, not hardware).
- SKILL-005 PIVOT-001: facts show pivot from "Airbedandbreakfast for conferences only" to "broader peer-to-peer rooms." 1 minor pivot, narrative coherent. PASS.
- ALTMAN-006 builder + seller split: builder (Nathan Yes), seller capability (Brian + Joe via design + customer-discovery work). PASS.
- CALDWELL-009 5x technical-talent multiplier: ≥1 technical founder (Nathan) — multiplier engaged. PASS.

All skill gates pass on this facts-file → factual-fills mapping. No anti-fabrication violations.
