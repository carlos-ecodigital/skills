# Phase 5 — Validation Protocol

**Purpose:** Validate the yc-application-helper skill against three independent surfaces before declaring v1.0 production-ready.

**Per the plan:** This is the "exceptional standard" gate. Path C (thinner skill ship now, validate iteratively) is the chosen direction; this protocol documents what to run during iteration.

---

## 5A — Track A pattern-rubric validation (corpus-internal)

**What:** For each YC question, build a per-question rubric from corpus atoms (required elements + anti-pattern triggers + concreteness thresholds). Run skill on test facts files. Score drafts against rubric.

**Pass criteria:**
- Required-element match: ≥85% of required elements present per question
- Anti-pattern absence: 0 ANTI-* atom flags triggered
- Concreteness density: ≥1 specific anchor (name/number/date) per 30 words
- Brevity: drafts within partner-stated word budgets (Q-CO-2 ≤50 chars; total ≤3-min read)

**Implementation:** Skill's gate-report.md output is the Track A scorecard. Failures are surfaced at draft time, not Phase 5.

---

## 5B — Track A adversarial test battery

**What:** 10 adversarial facts-file fixtures designed to trigger specific failure modes. Skill must detect each and produce expected behavior.

**Fixtures (location: `assets/test-fixtures/adversarial/`):**

| # | Fixture | Expected behavior |
|---|---|---|
| 1 | `01-vague-no-evidence.md` | Skill flags ANTI-003 (lack of social proof + traction); refuses to fabricate; surfaces rejection risk |
| 2 | `02-contradictory-equity.md` | Skill detects equity adds to >100% inconsistency between Q-EQ-3 and per-founder profiles; flags contradiction |
| 3 | `03-foreign-language.md` | Skill flags non-English input; demands translation; does NOT auto-translate |
| 4 | `04-reapplicant.md` | Skill activates Q-PROG-11 handler; demands "what's changed" answer with specific YC feedback addressed (CALDWELL-011) |
| 5 | `05-solo-founder-no-strategy.md` | Skill flags ANTI-007 (solo + Q-FOUND-3=No + no rationale); demands solo-strength rationale |
| 6 | `06-hardware-no-shipped-product.md` | Skill applies hardware/deep-tech atoms; doesn't penalize for absence of demo; LOI-substitute logic invoked |
| 7 | `07-international-team.md` | Skill applies SF-relocation language per HALE/PG; addresses Q-CO-9 with explicit commitment |
| 8 | `08-pivoted-twice.md` | Skill drafts pivot narrative honestly via PG-011/PG-011b; doesn't paper over instability |
| 9 | `09-over-polished.md` | Skill detects ANTI-013 (performance-not-authenticity); flags as anti-pattern; suggests dialing down |
| 10 | `10-prompt-injection.md` | Skill ignores embedded prompt-injection attempts; drafts only what the schema permits |

**Pass criteria:** Every fixture produces the expected behavior. Any failure halts validation; backfill the corpus or tighten the gate.

**Run command (placeholder — implementation depends on skill orchestration):**
```
For each fixture in assets/test-fixtures/adversarial/:
  Invoke yc-application-helper with facts file = fixture
  Inspect output gate-report.md + flagged anti-patterns
  Compare to expected behavior in this file
  Pass or fail per fixture
```

---

## 5C — Partner-simulation review

**What:** Fresh subagent (no leaked Phase 1-4 context) role-plays a YC group partner reading the application. Scores it against the partner-evaluation-criteria rubric. Identifies top-3-rejection-reasons.

**Subagent prompt template (use verbatim, do not soften):**

```
You are a YC group partner with 10 years of experience reading application essays. You read 100+ applications per day; your average attention budget per app is 5 minutes. You decide today which applications get an interview slot — you have 5 slots and 100 applications. Approval bar: would you stake your reputation on this team?

Read the attached YC application drafts (raw + polished variants per question). DO NOT read the company facts file or atom files; you are working from the application alone, as a real partner would.

Score the application against these dimensions (1-10 each):
1. Founder formidability (PG-010): does the team look like they'll get what they want regardless of obstacles?
2. Idea quality (HALE-001 3-component check): are problem, solution, insight all visible?
3. Traction evidence (SEIBEL-007 signal-filter): is there a survival signal in the first 2 minutes?
4. Concreteness density (ARC-021/025): specific anchors per word, ≥1 per 30 words?
5. Caldwell story-framework (CALDWELL-008): can you tell a coherent story about this company after one read?
6. Anti-pattern absence: 0 ANTI-* triggers detected?
7. Caldwell extraordinary-claims test (CALDWELL-012): every big claim backed by specific evidence?

Then identify your top-3-rejection-reasons. These are the partner-stated objections you would raise in the partnership meeting if asked to defend a "no" decision. Be specific, brutal, and use partner vocabulary.

Output:
- Per-dimension scores (1-10 with one-line justification)
- Aggregate score (sum)
- Top-3-rejection-reasons (specific, brutal)
- One-sentence verdict: would you give this team an interview slot?
```

**Pass criteria:**
- Aggregate score ≥50/70
- Top-3-rejection-reasons either non-substantive OR addressed in current drafts
- v-polished does not score lower than v-raw on substance dimensions (1, 2, 5, 7) — polish should not sacrifice substance

**Run cadence:** Every batch of major skill changes. Required pre-submit run for any real application.

---

## 5D — Forward-test per skill-creator protocol

**What:** Pass a real raw facts file to a fresh subagent unaware of validation context. Prompt: "Use yc-application-helper at [path] to draft an application from this facts file." Observe whether the skill triggers correctly via description, executes the full workflow, produces output without intervention, surfaces actionable gap flags.

**Pass criteria:**
- Skill triggered without prompting
- Workflow executed without subagent intervention
- Output meets gate criteria
- Gap flags actionable + clearly labeled
- No leaked Phase 1-4 internal context in output

**Run:** ≥3 fresh forward-tests with different facts files. Clean up artifacts between tests.

---

## 5E — Regression battery

**What:** Persistent test suite at `references/validation/regression/`. After every corpus or skill change, re-run all prior-passing fixtures + adversarial cases + forward-tests.

**Pass criteria:** No regression on prior-passing cases. If a fix to one issue breaks another, halt and reconcile.

**Files:**
- `regression/fixtures-passing.txt` — list of facts-file names that passed last validation
- `regression/last-run.md` — timestamp + skill version + corpus snapshot at last pass
- `regression/changelog.md` — what changed and why for each version

---

## 5F — Held-out oracle

**What:** Reserve ≥2 published successful applications NOT used in atom extraction. Validate skill against held-out only AFTER 5A-5E pass on training set.

**Recommended held-out set:**
- One published successful application from a recent batch (2024-2025) — minimal contamination from training corpus
- One published successful application from an off-mainstream batch (e.g., a YC Climate or YC Fintech batch that's stylistically different)

**Pass criteria:** Held-out scores within 10% of training-set scores. Wider gap → corpus is overfitted; broaden source coverage.

**Caveat:** The Phase 5 strategy revision (path A → revised) accepted that full successful-application text isn't publicly available for training comparison. Held-out oracle therefore uses synthetic gold standards (Track B) reverse-engineered from public materials.

---

## 5G — Continuous calibration

**Post-v1.0 spec:**
- Every real submission outcome (accept/reject + partner feedback if available) captured in `references/validation/real-outcomes/`
- Quarterly review: do real outcomes correlate with skill's pre-submit verification scores?
- Where they don't correlate, root-cause: missing atom? Wrong gate threshold? Outdated rule? Update corpus accordingly.

---

## Run order for a full Phase 5 pass

1. 5A: skill self-checks during draft (always running)
2. 5B: adversarial battery — 10 fixtures, expected behaviors
3. 5C: partner-simulation on draft outputs
4. 5D: forward-test with fresh subagents
5. 5E: regression suite if prior validations exist
6. 5F: held-out oracle
7. 5G: capture results for continuous calibration

**Time budget:** ~3-4 hours for full pass. Adversarial battery + partner-simulation are the load-bearing components.
