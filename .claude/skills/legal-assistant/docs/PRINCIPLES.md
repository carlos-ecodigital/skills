# legal-assistant Skill — Engineering Principles

Written 2026-04-17 after v3.5.5 post-mortem (Carlos call-out: *"every change or addition breaks our work... house of cards"*). Purpose: codify the rules that prevent the recurring failure modes observed across v3.4 → v3.5.5 so future development compounds stability rather than fragility.

These principles are **enforceable** — each has a tripwire (test, linter rule, CI hook, or discipline rule) that catches violation at PR time, not after merge.

---

## 1. Mirror-edit discipline — never `cp` across path-layout boundaries

**Observed failure**: v3.5.5 staging test sweep failed 79/90 when I `cp`'d upstream `generate_loi.py` into staging. The file's relative imports assume upstream's `.claude/skills/legal-assistant/` layout; staging uses `skills/de-legal-assistant/`.

**Rule**: mirror edits to staging must be **targeted Edit-tool applications of the same conceptual change**, never `cp` or `rsync` of the full file. Every mirror edit is reviewed line-by-line.

**Tripwire**: pre-commit check in staging — if the hash of `generate_loi.py` matches the upstream hash exactly, fail (paths differ; contents cannot be byte-identical).

---

## 2. Static helpers for testable logic

**Observed failure**: v3.5-polish tests constructed a full `DocBuilder(data)` to test provider_term derivation. That triggered `_setup()` → document-factory image load → staging's LFS-gated PNG failed the test path. Upstream passed; staging failed. A 3-line logic check became env-dependent.

**Rule**: any logic that needs testing lives as a `@staticmethod` callable without constructing the full object. Tests import the helper and call it directly. Full-DocBuilder tests are reserved for integration tests that explicitly want the whole pipeline.

**Current helpers conforming**: `_is_tbc`, `_render_placeholder`, `_derive_footer_entity`, `_derive_provider_term`.
**Tripwire**: unit test that cannot be written as a static call = signal to refactor.

---

## 3. Additive-first for new features

**Observed failure**: Parties Preamble (v3.5.2 Scope A''') was added to `build()` unconditionally — every existing intake YAML instantly got a new body element without opt-in. Spacing bug in the new element caused every rendered doc to look wrong. No way to `--disable-parties-preamble` to bisect.

**Rule**: new render features ship as **additive** — gated by a YAML field or CLI flag that defaults to current behavior for one minor version. Once stable, flip the default. The Scope Q entities register did this correctly (optional `provider.entity` field; explicit-field path preserved).

**Tripwire**: every new render method must be reviewed against "what does an existing intake YAML produce with and without this change?" — if output differs unconditionally, scope is NOT additive and needs a gate.

---

## 4. Every render-logic change ships with a branch-specific test

**Observed failure**: the Parties Preamble spacing bug shipped undetected because the test asserted structural presence (`THIS LETTER OF INTENT` in doc) not visual layout (paragraph `space_after` values).

**Rule**: every new `self.p(...)`, `self.bp(...)`, `self.table(...)` call must have a test that asserts **both** content and visual attribute (alignment, space_after, font). Content-only tests are insufficient.

**Tripwire**: CI workflow adds a visual-layout sweep (`test_visual_layout.py`) that asserts known-good paragraph-format values for each render method. Currently 0 tests; target for v3.6.

---

## 5. Golden-file integration tests

**Observed failure**: QA PASS is a regex-pattern linter, not a "this document matches the intended output" check. The v3.4 Polarise LOI had 19 concrete defects, all passed QA.

**Rule**: each LOI type has a committed **golden** in `tests/goldens/<type>.docx.fingerprint.json` — a deterministic fingerprint (paragraph count, heading texts, table cells, section margins, footer content). Any change that moves the fingerprint requires explicit `pytest --update-goldens` with user approval in the PR description.

**Tripwire**: CI runs `test_golden_files.py`. Unexplained fingerprint diff = PR blocked.

**Status**: **not yet implemented** — committed deliverable for v3.6.

---

## 6. Visual layout invariants are testable

**Observed failure**: spacing bug in Parties Preamble; footer centre-alignment bug earlier (v3.5.1 A''''); footer entity-mismatch bug.

**Rule**: spacing, margins, alignment, font, color are all `paragraph_format` / `run.font` attributes readable on the rendered doc. Assert them. A `test_visual_layout.py` file asserts:
- Each named block's paragraphs have expected `space_before` / `space_after`
- Footer paragraph alignment matches expected
- Section margins match expected
- Cover-page vs body differentiation is preserved

**Tripwire**: new block added → visual test must be written in the same PR.

---

## 7. Cross-env parity explicitly documented

**Observed failure**: LFS checkout assumption caused staging CI to fail while upstream CI passed. No comment in the CI workflow explained the upstream/staging difference.

**Rule**: anywhere environment assumptions diverge (LFS, path layout, available binaries, file locations), the workflow/config/code must carry an **explanatory comment** and a **canary test** that would catch regression. The staging CI workflow now has both the `lfs: true` flag and a comment explaining why.

**Tripwire**: CI review checklist item — "any env-specific decision explained in a comment?"

---

## 8. Scope boundaries = commit boundaries

**Observed failure**: the v3.5 consolidation had 4 scopes in one commit; when CI failed it was unclear which scope introduced the bug. Separately, the sed-based brand rename touched 99 strings across the codebase in one commit — hard to bisect.

**Rule**:
- One scope per commit. Plan-file scope letters (A, A', A''', J3, etc.) become commit-message prefixes.
- Bulk sed-replaces must be atomic and reviewable (diff-first; apply with full audit trail in commit message).

**Tripwire**: commit-message format `<type>(<skill>): v<version> scope <letter> — <description>`. PR description requires a scope-table linking commits to scopes to files.

---

## 9. Every defect maps to a methodology gap + a rule

**Observed pattern**: each field-surfaced defect revealed a methodology hole. Jonathan memo 19 items → Signal Test methodology. Cohere mis-attribution → writer discipline rule. Spacing bug → visual invariants.

**Rule**: when fixing a defect, also fix the methodology gap that allowed it. PR description must answer: *"what rule or methodology guidance would have prevented this defect if it had existed?"* — and land that rule or doc update in the same PR.

**Tripwire**: PR template `### Methodology gap closed:` field. Empty = reviewer pushes back.

---

## 10. Layer contracts are public and versioned

**The five layers:**
1. **Engine** (`generate_loi.py`) — renders intake YAML to .docx
2. **Data** (intake YAML schema) — what the engine reads
3. **Rules** (linter R-1..R-28) — what the engine validates in output
4. **Methodology** (`_shared/counterpart-description-framework.md`) — how humans fill the YAML
5. **Callees** (`legal-counsel/.../loi-review-workflow.md`) — what downstream skills consume

**Rule**: each layer has a public contract documented at the top of its primary file. Contract changes require a version bump (v3.5 → v3.6) and a migration note. Non-contract changes (implementation details, test additions) are minor.

**Current contracts:**
- Engine: `DE-LOI-{Type}-v{version}` in filename; 5 types enumerated in `_AGREEMENT_TYPE_BY_LOI`
- Data: YAML schema in `intake_example_*.yaml` + config/entities.yaml register
- Rules: R-1..R-28 in `_FAIL_RULES` / `_WARN_RULES` with human-readable messages
- Methodology: Signal Test 3-gate + 5-pillar framework in counterpart-description-framework.md
- Callees: PASS/FLAG/REJECT envelope in loi-review-workflow.md

**Tripwire**: layer contract change without version bump = PR blocked.

---

## 11. Regression fixtures ARE operational truth

**Current state**: `colocation/regression/v3.5/` contains 4 fixtures (Polarise / Cudo / SAG / InfraPartners) that exercise every v3.5.x fix path. They're not examples — they're the **regression baseline**. Any change that flips any fixture's QA status is a signal.

**Rule**: regression fixtures are never deleted, only added. A fixture that becomes "obsolete" is still kept as a historical baseline (moved to `regression/v3.N/archive/`). Smoke-regen of all fixtures is in CI.

**Tripwire**: CI `Smoke-regen v3.5 regression fixtures` step — must QA PASS. Flip = PR blocked.

---

## 12. Breadth of coverage > depth of any single item

**Observed failure**: v3.5.2 had 1 intake example (`intake_example_wholesale.yaml`) updated with the new entities register pattern; the other 5 stayed v3.5.1. Jonathan ran into a gap because the wholesale-specific fix didn't document for other types.

**Rule**: changes that affect all LOI types must land in all 5 intake example YAMLs in the same PR. Partial coverage is worse than no coverage — it creates a silent trap.

**Tripwire**: linter check — if `intake_example_*.yaml` files have structurally different shapes (set of fields), fail PR.

---

## Applying these principles

- **Before each PR**: scan the "Tripwire" column of this doc. If your change touches an area covered by a principle, confirm the tripwire is satisfied.
- **At commit time**: commit message links to the relevant principle number(s).
- **At review time**: reviewer uses this doc as the checklist; any "not applicable" justifications are explicit in PR description.
- **At post-mortem** (after any field-surfaced defect): update this doc. New failure mode = new principle. This doc compounds; it does not shrink.

## Status of tripwires as of v3.5.5

| # | Principle | Tripwire implemented? |
|---|---|---|
| 1 | Mirror-edit discipline | ⏳ Pre-commit hash check pending |
| 2 | Static helpers | ✅ Current helpers conform |
| 3 | Additive-first | ⏳ No automated check yet (review discipline) |
| 4 | Branch-specific tests | 🟡 Partial (unit tests yes, visual tests no) |
| 5 | Golden-file tests | ⏳ v3.6 target |
| 6 | Visual invariants | ⏳ v3.6 target |
| 7 | Cross-env docs | ✅ LFS comment landed in CI workflow |
| 8 | Scope = commit | ✅ Commit-message convention enforced |
| 9 | Defect → methodology | ✅ PR template (to add to repo) |
| 10 | Layer contracts | 🟡 Contracts exist; versioning discipline partial |
| 11 | Regression fixtures | ✅ CI smoke-regen gates |
| 12 | Breadth coverage | ⏳ Structural-shape linter pending |

**Priority for v3.6**: close items 1 / 4 / 5 / 6 / 12 — that's the discipline gate we need to stop the "house of cards" pattern.
