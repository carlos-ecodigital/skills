# Anti-Patterns — Consolidated Failure Modes

**Sources:**
- `archive/anti-patterns-rejection-evidence.md` (W23 founder, Lior Neu-ner, Founders Corner)
- Cross-source anti-pattern atoms surfaced from PG, Hale, Altman, Seibel
- YC partner-stated rejection reasons (verbatim)

**Anti-pattern atom prefix:** ANTI-

---

## ANTI-001 — Pivoting in the Interview

```yaml
atom_id: ANTI-001
source: archive/anti-patterns-rejection-evidence.md (W23 diceduckmonk founder)
applies_to_questions: [Q-IDEA-1, Q-IDEA-5, Q-PROG-1]
rule_type: anti-pattern (interview-stage)
when_triggers: Founder pivots from authentic original product to "grander idea" during interview.
why_it_kills: Founder coherence is the partner's prior. Pivoting in interview = chaos signal.
```

**Verbatim founder self-diagnosis (W23):**
> "We got carried away with the ceremony of doing a startup for startup sake and not actually building the business."

**Application implication:** Q-IDEA-1 / Q-IDEA-5 must be coherent with each other and with the actual operational state. Skill validates internal consistency.

---

## ANTI-002 — Ceremony Over Building

```yaml
atom_id: ANTI-002
applies_to_questions: [Q-PROG-1]
rule_type: anti-pattern (focus)
when_triggers: Application emphasizes pitch deck / brand / messaging over user engagement / sales.
why_it_kills: Polish without substance = signal that founder hasn't done customer work.
```

**Application implication:** Q-PROG-1 evaluates how-far-along by what was BUILT and SOLD, not what was DESIGNED. Skill flags applications where progress framing is dominated by branding/messaging.

---

## ANTI-003 — Lack of Social Proof and Traction (verbatim YC partner rejection reason)

```yaml
atom_id: ANTI-003
source: archive/anti-patterns-rejection-evidence.md (W23 partner verbatim feedback)
applies_to_questions: [Q-PROG-5/6, Q-PROG-7/8, Q-IDEA-1]
rule_type: anti-pattern (most common rejection)
when_triggers: No users + no revenue + no LOIs + no waitlist conversion + no named customer conversations.
why_it_kills: Verbatim YC partner phrasing of common rejection reason. Partners cannot fund pure-imagination at scale.
```

**Verbatim YC W23 partner feedback:**
> "From the partners' POV, it's a lack of social proof and traction."

**Application implication:** Application must surface SOME evidence even if modest. Anti-pattern: no users + no LOIs + no specific customer conversations + no concrete progress. Skill flags "imagination-only" applications and demands gap closure.

---

## ANTI-004 — Incumbent-Substitute Trap

```yaml
atom_id: ANTI-004
source: archive/anti-patterns-rejection-evidence.md (Lior Neu-ner — Slack alternative)
applies_to_questions: [Q-IDEA-1, Q-IDEA-2]
rule_type: anti-pattern (positioning)
when_triggers: Building "a better X" against deeply embedded incumbent (Slack, Salesforce, Zoom, etc.) without paradigm shift.
why_it_kills: Incumbent inertia is impassable for incremental challengers. Quote partners use: "completely new paradigm and no one saw coming."
```

**Verbatim YC feedback to Lior:**
> "Slack is now so deeply embedded into every company, it's incredibly hard to get users to pay attention to a new tool."
> Success requires "a product that creates a completely new paradigm and no one saw coming."

**Application implication:** Q-IDEA-1 / Q-IDEA-2 must articulate paradigm shift, not feature comparison. "Better Slack" framing = rejection-shaped. "Slack-replacement-because-Slack-is-architecturally-wrong-for-X" with paradigm justification = potentially fundable.

---

## ANTI-005 — "I Don't Have a Good Answer"

```yaml
atom_id: ANTI-005
source: archive/anti-patterns-rejection-evidence.md (Lior Neu-ner)
applies_to_questions: [Q-IDEA-1, Q-IDEA-3, Q-PROG-5/6]
rule_type: anti-pattern (written form)
when_triggers: Application contains an "I don't know" / "TBD" / "we'll figure out" answer in a high-leverage section.
why_it_kills: Conversational uncertainty is fine; written uncertainty in submitted application is fatal. Partners read submitted text as the founder's best work.
contradicts: SEIBEL-005 (be earnest in conversation) — resolution: skill flags gaps; founder closes them BEFORE submission.
```

**Application implication:** Skill fabrication-anti-pattern gate flags any answer containing hedging keywords ("we think," "we believe," "TBD," "to be determined," "we'll figure out," "we don't know yet"). User must resolve before submission.

---

## ANTI-006 — No Prototypes / Designs / Built Work

```yaml
atom_id: ANTI-006
source: archive/anti-patterns-rejection-evidence.md (Lior Neu-ner)
applies_to_questions: [Q-CO-4, Q-PROG-1, P-ACC-3]
rule_type: anti-pattern
when_triggers: Application has zero visible work artifacts. No demo, no mockups, no GitHub, no deployed prototype.
why_it_kills: Q-CO-4 demo upload is REQUIRED (1-3 min / 100 MB). Absent demo = serious flag. P-ACC-3 (things built) without URLs = anti-pattern.
```

**Application implication:** Skill demands at least mockup-level visual evidence for Q-CO-4. P-ACC-3 must include URLs or specific named work.

---

## ANTI-007 — Solo Founder Without Co-Founder Strategy

```yaml
atom_id: ANTI-007
source: archive/anti-patterns-rejection-evidence.md (Lior Neu-ner) + ALTMAN-005 corroboration
applies_to_questions: [Q-FOUND-3]
rule_type: anti-pattern
when_triggers: Solo applicant + Q-FOUND-3 marked No (not looking for co-founder) + no rationale for solo strength.
why_it_kills: FAQ-001 says solo OK but harder. No plan = signal that founder hasn't acknowledged the disadvantage.
```

**Application implication:** Solo applicants should mark Q-FOUND-3 = Yes OR provide explicit rationale (prior solo execution evidence, named technical advisor / contractor, etc.). Skill flags solo + No + no-rationale combination.

---

## ANTI-008 — Day-Job Hedging

```yaml
atom_id: ANTI-008
source: archive/anti-patterns-rejection-evidence.md (Founders Corner) + FAQ corroboration
applies_to_questions: [Q-PROG-2, P-ROLE-5]
rule_type: anti-pattern (commitment gate)
when_triggers: Application implies founders are not full-time, or P-ROLE-5 marked No / hedged.
why_it_kills: "Risk tolerance is precisely what YC is betting on." YC funds founders who go all-in.
```

**Application implication:** Q-PROG-2 / P-ROLE-5 require explicit full-time commitment from each founder. Hedging here = disqualification.

---

## ANTI-009 — Imprecise Problem Articulation

```yaml
atom_id: ANTI-009
source: archive/anti-patterns-rejection-evidence.md (Founders Corner)
applies_to_questions: [Q-IDEA-1]
rule_type: anti-pattern
when_triggers: Q-IDEA-1 doesn't precisely articulate (a) why problem exists, (b) who suffers, (c) why unsolved before, (d) why now.
why_it_kills: Vagueness on any of the four = rejection-shaped.
```

**Application implication:** Skill Q-IDEA-1 verification gate checks for all 4 elements present. Missing any = revise.

---

## ANTI-010 — Imaginary Demand

```yaml
atom_id: ANTI-010
source: archive/anti-patterns-rejection-evidence.md (Founders Corner) + ALTMAN-007 corroboration
applies_to_questions: [Q-PROG-5/6, Q-IDEA-1]
rule_type: anti-pattern
when_triggers: Application claims demand without concrete evidence (LOIs, pilots, waitlist conversions, named customer conversations, paid customers).
why_it_kills: "Imaginary problems" — partners cannot distinguish real demand from founder hopes.
```

**Application implication:** Q-PROG-5/6 strong answer cites at least one of: paying customer, LOI, pilot, waitlist with conversion rate, named customer interview transcripts, or organic referral. Skill flags absence.

---

## ANTI-011 — Product-Focused Founder Video

```yaml
atom_id: ANTI-011
source: archive/anti-patterns-rejection-evidence.md (Founders Corner) + ARC-029 corroboration
applies_to_questions: [Q-VIDEO-1]
rule_type: anti-pattern
when_triggers: Founder video focuses on product features instead of founders.
why_it_kills: Q-VIDEO-1 is structurally a founder-presence test, not a product demo. Product demo is Q-CO-4.
```

**Application implication:** Skill video-script template enforces founder-on-camera content; product demo content goes to Q-CO-4.

---

## ANTI-012 — Untested Problem

```yaml
atom_id: ANTI-012
source: archive/anti-patterns-rejection-evidence.md (Founders Corner)
applies_to_questions: [Q-IDEA-1, Q-PROG-5/6]
rule_type: anti-pattern
when_triggers: Application describes a problem the founders have not stress-tested with real humans (no customer interviews, no real conversations).
why_it_kills: Without real-human evidence, the problem is hypothetical.
```

**Application implication:** Q-IDEA-1 must show direct customer conversation evidence. Skill flags problem-articulation lacking specific named customer interactions.

---

## ANTI-013 — Performance Over Authenticity

```yaml
atom_id: ANTI-013
source: archive/anti-patterns-rejection-evidence.md (Founders Corner)
applies_to_questions: [Q-VIDEO-1, all written]
rule_type: anti-pattern (tone)
when_triggers: Application reads "constructed" / "rehearsed" rather than founder voice.
why_it_kills: Partners detect performance vs. genuine understanding.
```

**Application implication:** v-polished should retain founder voice (humanizer + executive-comms applied lightly, not aggressively). Skill validation: spawn fresh subagent reading drafts; ask "does this read like a person or a constructed pitch?"

---

## ANTI-014 — Marketing-Speak Vocabulary (structured by category)

Banned vocabulary compiled from HALE-005, SEIBEL-001, ARC-003/004 + `humanizer` cross-reference. Skill scans every draft and flags each occurrence by category.

### Category 1 — Corporate-speak / consultant register (HARD FLAG: violates PG-009b internal-language rule)

| Term | Source | Why banned |
|---|---|---|
| platform | Seibel (named) | Ambiguous — covers marketplace/API/infrastructure/app/suite indistinctly |
| ecosystem | aggregator | Substitutes for naming actual users + actual relationships |
| leverage (verb) | aggregator | Consultant-speak for "use" |
| seamless | aggregator | Promises frictionless v1 that doesn't exist |
| robust | aggregator | Adjective without specifics |
| best-in-class | aggregator | Self-aggrandizing without comparison anchor |
| next-generation | aggregator | Marketing replacement for "newer" |
| cutting-edge | aggregator | Same |
| empower | aggregator | What does the user actually do? |
| unlock | aggregator | Same |
| transform | aggregator | What concretely changes? |
| synergy | Seibel | Pure consultant-noise |

### Category 2 — Hype verbs (HARD FLAG: signals selling not describing)

| Term | Source | Why banned |
|---|---|---|
| revolutionize | Seibel (named) | Hype-verb; partners are immune |
| disrupt | Seibel (named) | Hype-verb |
| innovate | Seibel (named) | Empty signal — what specifically is new? |
| reimagine | aggregator | Empty signal |
| redefine | aggregator | Empty signal |

### Category 3 — Hedging (HARD FLAG: violates ANTI-005 written-uncertainty rule)

| Pattern | Why banned |
|---|---|
| "we think..." | Hedge — partners read submitted text as founder's best, not best-guess |
| "we believe..." | Hedge |
| "we hope..." | Hedge — replace with "we plan to" + specifics |
| "potentially" | Hedge |
| "probably" | Hedge |
| "TBD" / "to be determined" | Gap, not answer |
| "we'll figure out" | Confession of unfinished thinking |

### Category 4 — AI-tells (HUMANIZER OVERLAP — flag during v-polished pass)

| Pattern | Why flagged |
|---|---|
| Rule-of-three abuse ("X, Y, and Z" 3+ times in a paragraph) | AI-generated cadence |
| Em-dash overuse (>2 per paragraph) | AI-generated punctuation tic |
| "It's not just about X — it's about Y" | AI-generated false-contrast |
| Curly quotes (" " ' ') | Word/AI artifact, use straight quotes |
| Title-case headings ("How To Apply") | AI register; use sentence case |
| Emojis in headings or bullets | AI decoration |
| "I hope this helps" / "Let me know if..." | Chat-artifact leakage |

### Detection priority

1. **Categories 1 + 2 + 3** = HARD FLAGS — drafts containing these are rejected at the v-raw stage; require revision before polishing.
2. **Category 4** = handed off to `humanizer` skill during v-polished pass; not blocking for v-raw.

**Application implication:** Skill scans every draft against this table. v-raw fails on Category 1/2/3 hits; v-polished requires zero Category 4 patterns survive humanizer.
