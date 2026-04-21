# Visual-Regression Corpus Extension — Design (Deferred from Rebuild)

> **Status:** design-only. Implementation deferred per rebuild plan. Landing this requires per-baseline human visual review that code-level tooling cannot replace.

## Context

The existing `tools/visual_qa.py` pipeline (added in PR #5, `8a315d8`) drives:

```
markdown (on disk)  →  md_to_docx  →  audit  →  PDF (LibreOffice)  →  page PNGs  →  pHash
                                                                                      │
                                                                  committed: tests/visual/golden.json
                                                                  archived:  Drive QA/visual_golden/{date}/
```

The default corpus is 8 markdown files in Drive (Arco + Corporate SAR program + HAB).

The rebuild plan's M4 (Bespoke LOI) and M6 (MDCS verification) added visual-layer coverage as "deferred" explicitly because the pipeline assumes markdown inputs. M4 produces docx from YAML via `generate_loi.py`; M6's Pipeline B produces docx from an existing docx via `rebrand.py`. Neither fits the current corpus schema.

## What's missing

- Visual regression for **Pipeline A Bespoke output** (YAML → docx). Needs a YAML corpus type.
- Visual regression for **Pipeline B rebrand output** (docx + RebrandSpec → docx). Needs a rebrand corpus type.
- Visual regression for document-factory **profile outputs** (agreement, seed_memo, investor_memo, exec_summary, letter). Currently the corpus contains only markdown inputs; profiles aren't exercised visually even though they render distinct covers.

## Why this is deferred (honest accounting)

1. **Architectural rework in `visual_qa.py`.** The pipeline's `render_docx(md_path, docx_path)` is tightly coupled to `md_to_docx`. Supporting YAML and rebrand inputs requires factoring that function into a `_render_<type>` dispatch. Roughly 100 LOC plus test updates.

2. **Corpus fixtures.** Markdown corpus entries live in Drive; YAML fixtures could live in-repo (already committed as `examples/intake_example_*.yaml`). Mixing in-repo + Drive corpus entries requires changes to `resolve_corpus()` path resolution.

3. **Per-baseline human visual review.** The whole point of the tool is that a human confirms the rendered page is correct before approval writes `golden.json`. Adding 2 new profiles × ~12 pages each = ~24 pages requiring visual review. This is not a 30-minute code task; it's a content-review ritual that belongs on a reviewer's desk with time budgeted.

4. **LibreOffice + Word asymmetry.** The pipeline uses LibreOffice for regression (fast, session-independent) but Word for final delivery. Rebrand outputs may render subtly differently between the two engines; baselining on LibreOffice means a Word-rendered PDF to a counterparty may drift from the approved baseline. Acceptable for regression-detection purposes, but worth flagging.

5. **Machine-specific baselines.** Inter font rendering drifts between macOS versions and brew updates. The current corpus's golden was approved on one machine; adding new baselines on a different machine compounds that drift. A CI-runner-as-ground-truth setup would fix this but isn't wired today.

## Implementation plan (when approved)

### 1. Extend corpus schema

```json
// tests/visual/corpus.json
[
  { "type": "md",     "input": "{BASE}/path/to/file.md",        "slug": "01_..." },
  { "type": "md",     "input": "{BASE}/.../..., "slug": "..." },
  { "type": "profile", "profile": "agreement",
    "args": { "agreement_type": "Letter of Intent", "client": "...",
              "client_address": "...", "entity": "nl" },
    "slug": "10_profile_agreement_loi_nl" },
  { "type": "yaml",   "input": "examples/intake_example_bespoke_mdcs.yaml",
    "slug": "11_bespoke_mdcs" },
  { "type": "rebrand", "input_docx": "tests/visual/fixtures/counsel_msa_stub.docx",
    "spec": { "agreement_type": "Master Service Agreement",
              "client": "Party B Limited", "client_address": "10 Old Bailey, London",
              "entity": "ag", "client_reg_type": "CRN", "client_reg_number": "99999999" },
    "slug": "12_rebrand_counsel_msa" }
]
```

`{BASE}` substitution continues as today. `examples/...` resolves against `legal-assistant/colocation/examples/` for in-repo YAML fixtures.

### 2. Dispatch in `render_docx`

```python
def render_docx(entry: dict, docx_path: Path) -> tuple[str, list[str]]:
    t = entry["type"]
    if t == "md":
        return _render_md(entry, docx_path)
    if t == "profile":
        return _render_profile(entry, docx_path)
    if t == "yaml":
        return _render_yaml(entry, docx_path)
    if t == "rebrand":
        return _render_rebrand(entry, docx_path)
    raise ValueError(f"Unknown corpus entry type: {t!r}")
```

Each `_render_*` runs the appropriate pipeline and returns `(title, audit_violations)` same as today.

- `_render_md`: unchanged from current `render_docx`.
- `_render_profile`: calls `builders.build_<profile>(**entry["args"])` → save_doc → audit.
- `_render_yaml`: shells out to `generate_loi.py <path>`, opens the produced docx, runs audit on it.
- `_render_rebrand`: reads docx input + builds RebrandSpec from `entry["spec"]`, calls `rebrand.rebrand()`, saves bytes to docx_path, runs audit.

### 3. New fixture assets

- `tests/visual/fixtures/` — holds rebrand input docx fixtures (counsel MSA stub, counterparty NDA). Built from the synthetic helpers in `tests/test_rebrand.py` via a one-off script, committed as small binaries.
- `tests/visual/corpus.json` — new corpus definition (see §1). Becomes the default instead of the hard-coded `DEFAULT_CORPUS` list.

### 4. Approval workflow

On a machine with Inter installed + LibreOffice + Word:

```bash
python3 tools/visual_qa.py generate --corpus tests/visual/corpus.json
python3 tools/visual_qa.py report --open
# Human reviews every page of every new corpus entry.
# If all pages are correct:
python3 tools/visual_qa.py approve
git add tests/visual/golden.json tests/visual/corpus.json tests/visual/fixtures/
git commit -m "visual QA: extend corpus to profile + yaml + rebrand pipelines"
```

### 5. CI gating

The existing pytest marker pattern:

```bash
pytest --visual
```

fails if anything regresses. No change to CI config; the extended corpus just increases coverage of what `--visual` catches.

## Estimated effort

- Code: ~2 hours (100 LOC rework in visual_qa.py + test updates).
- Fixture creation: ~1 hour (synthetic rebrand inputs + one-off build script).
- Human visual review: **variable** — 30–90 minutes depending on how rigorous the reviewer is per page. This is the gating factor.
- Total: ~half-day of focused work.

## Risks flagged

1. **Drive dependency.** Adding profile + yaml + rebrand entries doesn't need Drive, but the existing markdown corpus still does. A CI environment without Drive access runs a partial corpus. Not new — already the case today.

2. **Rebrand fixture size.** Committing a small (< 50 KB) synthetic MSA stub as a binary test fixture is OK; a real MDCS docx (6+ MB) is not. Fixture must be hand-crafted / minimal.

3. **pHash threshold sensitivity.** Profile outputs with dynamic dates (the `date_str` arg) render with today's date by default. Baselines must pin dates to a fixed value (e.g. `2026-04-17`) or hashes drift every test run. Trivial but easy to miss.

4. **Rebrand + Word asymmetry.** Pipeline B's `rebrand.py` is used on real counsel/counterparty docx inputs. LibreOffice-rendered PDFs for these may look subtly different from Word-rendered ones. For visual regression this is acceptable (we compare LO output to LO output). For production delivery it's a separate concern handled by `generate.docx_to_pdf` which uses Word.

## Decision record

This design is the handoff artefact for completing the deferred Layer 4 coverage. A follow-up PR implementing sections 1–3, plus an approval session following section 4, closes the rebuild's deferred scope fully.

Until then: Layers 1 (byte-diff + fingerprint JSON), 2 (structural audit + R-24), and 3 (content QA catalogue) provide genuine regression gating. Layer 4 (visual) is covered for the existing Drive corpus and remains deferred for profile / yaml / rebrand.
