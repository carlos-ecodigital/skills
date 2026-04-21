# Tone Markers — qualitative tokens → concrete drafting rules

Operators often specify voice with a short list of adjectives ("short, powerful, collaborative"). Without a translation layer, the draft takes 4–6 iterations to land. This table converges first-draft to operator intent.

## Marker table

| Token | Concrete rule |
|---|---|
| **Short** | ≤200 words total; ≤5 paragraphs; no tactical detail (no MW, specs, dates beyond validity). If the operator supplies MW/spec numbers in context, they belong in the LOI, not the cover email. |
| **Powerful** | Active verbs; one conviction sentence per paragraph; drop hedging ("I think / we believe / perhaps"); use concrete nouns over abstractions. |
| **Collaborative** | Opening acknowledges existing joint work; first-person-plural preferred over first-person-singular; close with joint-future phrasing ("for you and our customers"). |
| **Direct** | Imperative CTA; skip "I hope this finds you well"; bottom-line-up-front in the opening sentence. |
| **Warm** | Personal check-in opener; gratitude close; informal register; contractions allowed. |
| **Institutional** | No contractions; passive voice acceptable for legal accuracy; third-person self-reference acceptable ("Digital Energy will…"). |

## Combining markers

Markers combine. Where they conflict, the operator's order implies priority — first token wins.

- **"Short, powerful, collaborative"** (Jonathan, Cerebro cover email): ≤200w, active verbs, drop hedges, first-person-plural opener + close. This is the canonical DE cover-email voice.
- **"Warm, institutional"**: contradicts on contractions; warm wins. Use personal check-in opener but keep passive-voice legal accuracy where needed.
- **"Direct, powerful"**: compounding; no preamble, active verbs throughout, conviction in every paragraph.

## Output: tone audit

Every draft emitted by this skill includes an audit block at the end showing which rules were applied:

```
## Tone audit (applied: short, powerful, collaborative)
- Word count: 187 / 200 ✓
- Paragraphs: 4 / 5 ✓
- Active verb ratio: 88% ✓
- First-person-plural opener: "We've appreciated the ongoing…" ✓
- Hedging check: 0 instances of "I think / we believe / perhaps" ✓
- Joint-future close: "for you and our customers" ✓
```

The audit is operator-facing, not delivered. Strip before sending.

## Anti-patterns (flag on audit, not auto-fix)

- **"As per our discussion"** — institutional but cold; replace with specific shared context ("Following our London office discussion…").
- **"Please find attached"** — replace with a verb that says what the attachment does ("I've attached a draft LOI covering…").
- **"Kindly"** — obsequious; drop.
- **"I hope this finds you well"** — generic; replace with concrete check-in or drop entirely.
- **Bullet lists in cover emails** — contradict "warm"; bullets read institutional. Use prose. (Bullets are fine for internal; this is outbound.)

## Source

Tone markers are distilled from 4 iterations of the Cerebro Cloud cover email (Jonathan Glender, 2026-04-17) — converged on this taxonomy after observing which rules the operator applied at each edit step.
