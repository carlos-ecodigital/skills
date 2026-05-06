# P-ACC-2 — "Most impressive thing you've built or achieved" (Airbnb worked example)

**Per PG-012: this is THE most important question on the application.** 1-2 sentences. Hard gate per skill.

## Brian Chesky — v-raw drafts (3 candidates)

### Candidate 1 (specific named project + scale + named retail)
> Designed the Pina sport seat for 3DM — sold 200,000 units across 8 countries by age 24.
[14 words / 1 sentence. Passes hard gate per PG-012: specific name, specific scale (200k units), specific outcome (8 countries), completed (not aspirational), age signal of formidability.]

### Candidate 2 (the cereal-box wildcard recovery story)
> Designed and shipped two limited-edition cereal boxes (Obama O's, Cap'n McCain's) timed to the 2008 election; sold $30,000 in 2 months, kept Airbnb alive through dead-money.
[~30 words / 2 sentences. Passes hard gate. Stronger as the wildcard P-ACC-1; for P-ACC-2 the Pina seat is more universally readable.]

### Candidate 3 (combined — too long)
> Designed Pina sport seat (200k units shipped across 8 countries) and Obama O's / Cap'n McCain's cereal boxes ($30k in 2 months that kept Airbnb alive in 2008).
[FAILS the 1-2 sentence compression test by trying to do too much. Pick one.]

## Joe Gebbia — v-raw drafts (2 candidates)

### Candidate 1
> Designed Critbuns — a cushion for art-critique sessions — sold in the MoMA Design Store at age 23.
[Passes hard gate: specific name, specific retail anchor (MoMA), age signal.]

### Candidate 2
> Co-designed and shipped 800 limited-edition cereal boxes (Obama O's / Cap'n McCain's) in October 2008, generating $30k that bridged Airbnb's first dead-money period.
[Passes; same as Brian's Candidate 2 but co-attributed.]

## Nathan Blecharczyk — v-raw drafts (2 candidates)

### Candidate 1
> Built and sold Datamine, a referral-marketing platform, while at Harvard — operated profitably from a dorm room and exited for a low-millions undisclosed sum.
[Passes hard gate: specific company name, specific scale (low millions), specific context (Harvard dorm), completed (exited).]

### Candidate 2 (alternate emphasis)
> Founded Datamine my freshman year at Harvard and ran it profitably for 3 years before selling it.
[Passes; less detail but cleaner. Datamine name + profitable + 3 years + sold = 4 specifics in 17 words.]

## v-polished

Each candidate passed through humanizer + executive-comms; substance preserved. Polishing here mostly trims awkward phrasing without changing claims. Example for Brian Cand 1:

> Designed 3DM's Pina sport seat — 200,000 units sold in 8 countries before I turned 24.

(Substantively identical; minor flow improvement.)

## Citations

- [atom: PG-012] hard gate — vagueness here cannot be salvaged elsewhere
- [atom: PG-010] formidability via specific evidence (each draft names a specific shipped project)
- [atom: ALTMAN-004] founder trait quartet — Pina seat shows determination + execution; cereal boxes show resourcefulness; Datamine shows formidability
- [atom: ARC-013] show what you've done — concrete projects with named outcomes
- [fact: company-facts.md#founders] each draft traces to facts-file Most-Impressive entries

## Anti-pattern checks

- ❌ Adjective-only ("I am driven and resourceful") — not present
- ❌ Aspirational framing ("I'm building...") — not present
- ❌ Vague scope claim ("led a team that did big things") — not present
- ❌ No specific scale/outcome — every candidate has named scale (units, dollars, retail outlet, age)

## Gate report

| Gate | Brian Cand1 | Joe Cand1 | Nathan Cand1 |
|---|---|---|---|
| Hard gate (PG-012) | PASS | PASS | PASS |
| 1-2 sentences | PASS (1) | PASS (1) | PASS (1) |
| Specific named project | PASS (Pina) | PASS (Critbuns) | PASS (Datamine) |
| Specific scale | PASS (200k units, 8 countries) | PASS (MoMA national distribution) | PASS (low-millions exit) |
| Completed not aspirational | PASS | PASS | PASS |
| Anti-fabrication | PASS (matches facts file) | PASS | PASS |

## Why this is partner-readable

The hard-gate test for P-ACC-2 is: in 1-2 sentences, does the founder communicate "I have shipped real things at real scale"? Each candidate above passes this test. The pattern:

> [Specific named project] — [specific scale or outcome] — [optional age/context signal]

Anti-pattern P-ACC-2 (would FAIL the hard gate):

> "I'm a hard-working entrepreneur who has built several products and led teams to success in challenging environments."

This anti-pattern has zero specifics, zero shipped projects named, zero scale. It's adjective-only — exactly what PG-012 says cannot be salvaged elsewhere.

## Skill behavior

When the skill produces P-ACC-2 candidates, it MUST:
1. Generate 2-3 variants per founder (different emphasis or phrasing)
2. Validate each against the hard-gate criteria above
3. If facts file lacks substance for a passing candidate, output `[GAP: facts file lacks substantive prior-shipped achievement for {founder name}; close before submission]`
4. Never produce vague-sounding fills to close the gap. Anti-fabrication is absolute.
