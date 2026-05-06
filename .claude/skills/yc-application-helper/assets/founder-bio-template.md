# Founder Profile — [Founder Name]

**Note:** Each founder fills their own profile independently in the live YC form. Submission is gated on every founder profile being complete.

---

## P-BASICS-1 to P-BASICS-6 — Identity (factual)

- Name: [from facts file]
- Email: [from facts file]
- Age: [from facts file, if disclosable]
- Phone: [from facts file]
- Gender: [optional]
- City: [from facts file]

---

## P-ROLE-1 — Title / main responsibility
[from facts file]

## P-ROLE-2 — Equity %
[from facts file]

## P-ROLE-3 — Are you a technical founder? (Yes/No)
[from facts file — binary builder-presence filter per ALTMAN-006. If team has zero Yes, flag as serious anti-pattern.]

## P-ROLE-4 — Currently in school?
[from facts file]

## P-ROLE-5 — Will you commit exclusively for next year?
[from facts file — must be Yes per FAQ-003 / ANTI-008. Hedging = disqualification.]

---

## P-BG-1 — LinkedIn URL
[from facts file]

## P-BG-2 — Education (≥1 entry required)
[from facts file]

## P-BG-3 — Work history (≥1 entry required, validation-enforced)
[from facts file — partners may request references post-acceptance]

---

## P-SOCIAL — Personal website / GitHub / Twitter (optional)
[from facts file]

---

## P-ACC-1 — The wildcard (PG's borderline-rejection recovery surface)

**Question:** "Please tell us about a time you most successfully hacked some (non-computer) system to your advantage."

**v-raw draft (1-2 candidates):**

[Candidate 1: specific resourceful exploit of a non-computer system. Concrete details, named context, named outcome. Resourcefulness signal per ALTMAN-004 trait quartet.]

[Candidate 2 (alternate framing): same content, different angle.]

**v-polished draft:**
[Humanizer + voice applied to selected candidate]

**Atom citations:** [atom: HTA-003], [atom: PG-010 — formidability via specific evidence], [atom: ALTMAN-004 — resourcefulness trait]

**Gate notes:**
- Specific named context? [Yes/No]
- Tech-only example detected (anti-pattern)? [Yes/No]
- Vague "I figured out a way" framing detected? [Yes/No]

---

## P-ACC-2 — THE most important question (PG's anchor)

**Question:** "Please tell us in one or two sentences about the most impressive thing other than this startup that you have built or achieved."

**v-raw drafts (2-3 candidates per founder — user picks):**

**Candidate 1:**
[Specific named achievement + scale (number, named users, named recognition) + completed (not aspirational). 1-2 sentences max.]

**Candidate 2:**
[Same content, different framing emphasis.]

**Candidate 3:**
[Same content, third framing emphasis.]

**v-polished drafts:**
[Humanizer + voice applied to all 3 candidates]

**Atom citations:** [atom: PG-012 — hard gate], [atom: PG-010 — first-sentence weighted], [atom: ALTMAN-004 — formidability + unstoppability]

**HARD GATE:** Per PG-012, vagueness here cannot be salvaged elsewhere. Skill flags any candidate that:
- Names a generic role ("led a team") rather than specific achievement
- Frames aspirationally ("I'm building...") rather than completed
- Lacks scale/outcome (number, named users, named recognition)
- Reads as adjective-only ("I am driven and resourceful")

If all candidates fail the gate, output `[GAP: facts file lacks substantive prior-shipped achievement for [founder name]; close before submission]`.

---

## P-ACC-3 — Things you've built before (with URLs)

[List from facts file. Each item: project name + URL + 1-line outcome. Per ARC-013/015 — show what you've done.]

- [Project name] — [URL] — [1-line outcome]
- [Project name] — [URL] — [1-line outcome]

**Anti-pattern check:** No URLs at all = anti-pattern per ANTI-006. Vague "various projects" framing = anti-pattern.

---

## P-ACC-4 — Competitions / awards / papers (optional)

[List from facts file. Empty acceptable.]

---

## Per-founder gate report

- P-ROLE-3 (technical?) populated: [Yes/No]
- P-ROLE-5 (commit?) = Yes: [Yes/No — anti-pattern if not]
- Work history ≥1 entry: [Yes/No — required]
- P-ACC-2 passes hard gate: [Yes/No]
- P-ACC-1 has resourcefulness signal: [Yes/No]
- P-ACC-3 has ≥1 URL: [Yes/No]
- LinkedIn URL present: [Yes/No]

**Profile status:** READY / [list blockers]
