# Handoff Protocol

**Purpose:** When and how the yc-application-helper invokes other skills.

## Handoff inventory

| Skill | Status | When invoked | What we pass | What we expect back |
|---|---|---|---|---|
| `humanizer` | Confirmed installed (~/.claude/skills/humanizer/) | v-polished generation only; never v-raw | v-raw text per question | Humanized version with 29 anti-AI patterns removed |
| `executive-comms` | Status uncertain (symlink may be broken at ~/.claude/skills/) | v-polished generation only; after humanizer | Humanized text | Voice-tuned text (calm, factual, founder-confident register) |
| `competitive-intel` | Status uncertain | Q-IDEA-2 only, when facts file lists competitors but lacks differentiation framing | Competitor list + product context | Differentiation framing per competitor |
| `positioning-expert` | Status uncertain | Q-IDEA-1 / Q-IDEA-2, when facts file lacks insight articulation | Idea + market context | Insight articulation in HALE-001 mechanism format |
| `gstack/office-hours` | External (gstack.org) — not installed locally | Pre-draft fuzziness gate (workflow step 4) | Company-facts atoms relevant to current question | 6 forcing-question evaluations: demand reality / status quo / desperate specificity / narrowest wedge / observation / future-fit |

## Default behavior on missing handoff

If a handoff skill is not installed or returns an error:
- The yc-application-helper does NOT block.
- Note in `verification-report.md`: "Polish stage skipped — install [skill]" or "Pre-draft gate skipped — office-hours unavailable; manual fuzziness review recommended."
- v-polished may equal v-raw if humanizer + executive-comms both unavailable (still fine — user picks v-raw).

## Invocation pattern (Claude Code skills)

When the helper needs a handoff:

1. Check skill availability via `Skill` tool listing or by attempting to invoke.
2. If available, invoke with the expected input.
3. If unavailable, fall through to default behavior above.
4. Log the handoff outcome in the gate report.

## Manual fallback for office-hours fuzziness gate

If gstack/office-hours isn't installed, apply the 6 forcing questions manually to facts-atoms. For each Q in the application:

1. **Demand reality:** Has a real person paid you / committed money / urgently asked for this? Quote them.
2. **Status quo:** What do users do today instead of this? Why is it bad enough that they'd switch?
3. **Desperate specificity:** Who specifically (named) cares enough to use the v1?
4. **Narrowest wedge:** What's the smallest, most specific use case where you start?
5. **Observation:** What did you watch a real user do that surprised you about the problem?
6. **Future-fit:** In 5 years, why do you have an unfair advantage that compounds?

If facts fail any of these, surface as `[FUZZY: needs X]` flag before drafting.

## Versioning

This protocol is v1.0. Update when handoff skills change interfaces or when new handoff skills are added.
