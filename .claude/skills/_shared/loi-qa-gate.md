# LOI QA Gate — Rule Catalogue

**Purpose:** Pre-output lint for every LOI produced by `legal-assistant`. Catches template regressions, anti-patterns, and editorial slippage before the .docx reaches the user.

**Enforced by:** `generate_loi.py` pre-save hook. Runs against the rendered document text (extracted post-build, pre-save). Produces `{output_filename}_qa.txt` alongside the .docx.

---

## Severity levels

| Severity | Behaviour |
|---|---|
| `fail` | Blocks output. Must be auto-fixed by the engine, or require explicit user acknowledgement via `--override {rule_id}` with a recorded reason. |
| `warn` | Produces output. Visible warning in the QA report and returned to the skill for user acceptance. |
| `info` | Logged to QA report only. No user surfacing. |

**Override invocation:**
```bash
python generate_loi.py intake.yaml \
  --override R-11,R-14 \
  --override-reason "ISO 27001 genuinely relevant for data-sovereignty pitch"
```
Override + reason are written to the QA report.

---

## Rule catalogue

| ID | Severity | Scope | Rule | Auto-fix? |
|---|---|---|---|---|
| R-1 | fail | Body | No `"minimum commitment term of 5 years"` | Yes — generator emits "approximately 5 (five) years, indicative only" |
| R-2 | fail | Recital A | No `"14 identified sites"` or fixed site-count language (regex: `\b\d+\s+identified\s+sites\b`) | Yes — falls back to `default` variant |
| R-3 | fail | Recital A | No `"12 months of commercial commitment"` | Yes — falls back to `default` variant |
| R-4 | fail | Cl. 3+ (customer-facing) | No `"DEC Block"` in customer-facing clauses. Exception: internal delivery-unit reference in annexes if `programme.reveal_blocks: true` (rarely). SS/EP never use. | Yes — capacity expressed in MW IT |
| R-5 | fail | Whole document | No `"We are confident that"` | No — reject bespoke closing, fall back |
| R-6 | fail | Whole document | No duplicated `"We look forward to working with you"` within 200 characters | Yes — lead-phrase stripping in bespoke_closing |
| R-7 | fail | Body | No Unicode arrows anywhere: `→` (U+2192), `⇒` (U+21D2), `➜` (U+279C), `⟶` (U+27F6), `↦` (U+21A6), `⟹` (U+27F9), `⇨` (U+21E8) | No — template bug, reject |
| R-8 | fail | Schedule titles | No `"(NON-BINDING)"` suffix in any schedule title | Yes — strip suffix, italic prefatory note is the governing signal |
| R-9 | fail | Closing block | Closing paragraph ≤ 2 sentences (bespoke + default together) | Yes — truncate bespoke to 1 sentence; if still > 2, reject bespoke |
| R-10 | fail | Cl. 4.2 (WS / SS) | Heading ≠ "Revenue Chain"; must be "Contractual Sequence" or "Project Engagement Sequence" (SS) | Yes — template-level header replacement |
| R-11 | warn | Recital B | `ISO \d{4,5}` pattern present, unless `choices.cert_relevant: true` | No — surface for user review |
| R-12 | warn | Recital B | Word count outside 60–180 | No — surface for user review |
| R-13 | warn | Recital B | More than 1 parenthetical `\(.*?\)` per sentence | No — surface for user review |
| R-14 | warn | Recital B | Salesy adjectives present: `\b(leading\|innovative\|cutting-edge\|world-class\|best-in-class)\b` (case-insensitive) | No — surface for user review |
| R-15 | warn | Whole document | `positioning (its\|itself) as` pattern | No — surface for user review |
| R-16 | info | YAML | `programme.recital_a_variant` not explicitly set (used `default`) | — |
| R-17 | info | YAML | No `choices.bespoke_closing` set (used default single-sentence closing) | — |
| R-18 | fail | YAML (pre-run) | Deprecated field `commercial.dec_block_count` present | No — emit migration error pointing to CHANGELOG |
| R-19 | warn | Whole document | Any clause heading contains `"(NON-BINDING)"` — style regression (per v3.2 Schedule 1 fix, the signal belongs in Cl. 5.1 only) | No — surface for user review |
| R-20 | fail | Body | "(Provider's) programme spans \d+" language regression | Yes — falls back to `default` |
| **R-21** | **warn** | **Body (v3.4 body-wide)** | **Marketing adjectives `"purpose-built"` or `"state-of-the-art"` anywhere in document. Broadens v3.2 R-14 scope from Recital B to body.** | **No — surface for user review** |
| **R-22** | **warn** | **Body (v3.4)** | **Meta-commentary patterns — sentences that explain the LOI's purpose rather than creating / modifying obligations. Regex catches: `Provider's ability to`, `depends in part on`, `is intended to evidence`, `while non-binding in its commercial terms`, `to support the Provider's financing`, `will require the exchange of`, `The Parties acknowledge that the Provider intends`, `is intended to form the basis`.** | **No — surface for user review (reviewer rewrites in operative register)** |
| **R-23** | **fail** | **Recital B (v3.4 fabrication gate)** | **Material numeric-metric claims (regex: `\b\d+[\d,]*\s*(MW\|GW\|customers\|clients\|sites\|deployments\|GPUs\|operations\|offices\|countries\|years\|employees\|%)\b`) in Recital B MUST be backed by (a) a tier-1 source URL in `counterparty.source_map` YAML, (b) a `[TBC]` marker in the description text, or (c) an explicit `--override R-23 --override-reason "..."` CLI flag. Prevents v3.3 InfraPartners-style fabrication (unsourced "90-day RFS" / "80% off-site" claims).** | **No — hard gate; resolve by adding source_map URLs, adding [TBC] markers, or overriding with recorded reason** |

Also updated in v3.4:
- **R-14 scope** broadened from "Recital B" to "Body" (salesy adjectives flagged anywhere).

---

## Report format

File: `{output_filename}_qa.txt`. Example:

```
LOI QA Report
File: 20260415_DEG_LOI-Wholesale_Cerebro_Cloud_FINAL.docx
Generated: 2026-04-15T14:32:17Z
Variant: programme.recital_a_variant=default
Overrides: none

Findings:
  [INFO]  R-16  YAML         Recital A variant not set, used 'default'
  [INFO]  R-17  YAML         No bespoke_closing, used default single-sentence
  [WARN]  R-12  Recital B    Word count 42 (below 60)

Status: PASS (warnings: 1, failures: 0)
```

On `fail`:

```
Status: FAIL
  [FAIL] R-4   Cl. 3.1      'DEC Block' detected in customer-facing clause: '17 DEC Blocks (20.4 MW IT)'
                            Auto-fix applied: '20.4 MW IT (across multiple Designated Sites)'
  [FAIL] R-7   Cl. 4.2      Unicode arrow detected: '→'
                            No auto-fix available. Template regression — block build.

Build blocked. Fix template or run with --override R-7 --override-reason "..."
```

---

## Generator integration

Pseudocode, embedded at the tail of `LOI.build()`:

```python
def build(self) -> Document:
    # ... existing sections ...
    self.signature()
    self.schedule()
    self.footer()
    report = qa_lint(self.doc, self.d, overrides=self.overrides)
    if report.fails and not report.all_overridden:
        raise QAFailure(report)
    report.write_to(self.qa_report_path)
    return self.doc
```

`qa_lint` extracts paragraph text from the built Document, runs each rule's regex / structural check, records findings, applies auto-fixes where the rule supports it (re-mutates the Document in place), and returns a `QAReport` object.

---

## Adding rules

New rule → add row to the table above + a check function in `generate_loi.py` `qa_lint()`. Rules are evaluated in declaration order. Auto-fixes run before severity evaluation, so a rule with an auto-fix typically downgrades itself to `info` after the fix applies.

**Naming:** R-{next-free-integer}. Do not renumber existing rules — external QA reports cite by ID.

---

## Rule review cadence

After every 10 generated LOIs, reviewer (skill owner) should:

1. Read the latest 10 QA reports end-to-end.
2. Identify any consistently-warned pattern that could be upgraded to `fail` with auto-fix.
3. Identify any `fail` that is frequently overridden — either the rule is wrong or the auto-fix logic needs work.
4. Update this file + generator `qa_lint()` + CHANGELOG.

Do not add rules speculatively. Every rule should correspond to an observed anti-pattern in produced output.
