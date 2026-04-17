# Visual Regression QA

> Closed-loop quality gate for Document Factory: catches layout/rendering issues that `audit_document()` can't see.

## What it is

Pipeline: **markdown → docx → audit → pdf → page PNGs → perceptual hash**. The output is an HTML report for human review, a `golden.json` of approved page hashes, and a pixel-level PDF archive in Drive for deep diffs.

Three layers of quality, each catching what the others miss:

| Layer | What it catches | Where it lives |
|-------|-----------------|----------------|
| `audit_document()` | OOXML structure: missing `w:numPr`, wrong colors, missing `keep_with_next`, bad page margins | `generate.py` |
| Visual regression | Rendered layout: overflow, wrong fonts, clipped tables, bad spacing | `tools/visual_qa.py` |
| Human review | Taste / IB-grade aesthetics | HTML report + Drive archive |

## When to run it

| Trigger | Command |
|---------|---------|
| Before committing formatting changes in `generate.py` | `visual_qa.py diff` |
| After any change to `_SP`, abstractNum definitions, `_format_table`, cover logic | `visual_qa.py all` + review |
| Adding a new document type to the corpus | `visual_qa.py generate` → `approve` |
| Debugging a layout issue on real files | `visual_qa.py generate --corpus my_one_doc.json` |

In CI / pytest: `pytest --visual` runs the full pipeline against the corpus and fails the build if anything regresses.

## Commands

```bash
# Pre-flight: check Python deps, LibreOffice, corpus files
python3 tools/visual_qa.py doctor

# Generate current artifacts (md → docx → pdf → PNGs → hashes)
python3 tools/visual_qa.py generate [--corpus FILE.json]

# Build HTML report; if golden.json exists, show Δ annotations
python3 tools/visual_qa.py report [--open]

# Default: doctor + generate + report
python3 tools/visual_qa.py all --open

# Diff current run vs committed golden.json; exit 1 if any page changed
python3 tools/visual_qa.py diff [--threshold N] [--open]

# Promote current run: write golden.json (git) + archive PNGs to Drive
python3 tools/visual_qa.py approve [--force]
```

### Important flags

- `--output DIR` — scratch dir for current run (default `/tmp/docfactory_qa/`)
- `--corpus FILE.json` — custom corpus (default: 8 Arco + Corporate files)
- `--threshold N` — max hash distance (0-64) before flagging as changed (default 5)
- `--force` — bypass safety checks (overwrite same-day archive, approve despite violations)
- `--skip-pdf` — audit-only, no PDF/PNG (fast sanity check)

## Storage architecture (hybrid)

Three locations, each with a clear purpose:

| Location | Contents | Size | Git | Purpose |
|----------|----------|------|-----|---------|
| `tests/visual/golden.json` | pHash per page per slug | ~1 KB | ✅ committed | Regression source of truth |
| `{Drive}/QA/visual_golden/{YYYY-MM-DD}/` | Full-res PNGs per approved state | ~8 MB | ❌ Drive only | Human review + historical reference |
| `/tmp/docfactory_qa/` | Current run's docx/pdf/PNGs/results.json | variable | ❌ gitignored | Scratch for each run |

**Why hybrid?** Git stays small (hashes only); binaries go where binaries belong (Drive). `diff` runs with just git (no Drive needed); human visual review uses the Drive archive.

## Interpreting the HTML report

- Green **CLEAN** badge → no audit violations, no visual regressions
- Red **VIOLATIONS** badge → `audit_document()` flagged issues (listed below the doc title)
- Orange **N PAGES CHANGED** badge → pHash exceeded threshold vs golden
- Orange-bordered page thumbnail → that specific page changed (with Δ score)
- Click any thumbnail for full-size modal view

Hash distance (Δ) interpretation (out of 64):
- **0–3**: sub-pixel antialiasing noise (ignore)
- **4–5**: minor spacing/rendering drift (threshold default)
- **6–15**: real but small change (e.g., 1–2 lines reflowed)
- **16+**: significant change (layout shift, new content, missing page)

## Approving a new baseline

1. Make the code changes you want baselined.
2. Run `visual_qa.py generate --open` → browser opens the report.
3. Review every page of every document. For each orange page, confirm the change is intentional.
4. If all changes are deliberate: `visual_qa.py approve`
5. The command:
    - Refuses to approve if any doc has audit violations or errors (pass `--force` to override — rarely correct)
    - Writes `tests/visual/golden.json` (~40 hashes)
    - Copies all current PNGs to `{Drive}/QA/visual_golden/{YYYY-MM-DD}/`
    - Prints the `git add` / `git commit` commands
6. Commit the `golden.json` change in a PR so someone else can spot-check the diff before it merges.

## CI / pytest integration

```bash
# Standard test run — visual tests auto-skip (no LibreOffice required)
pytest

# Full regression suite — requires LibreOffice, ~1 minute
pytest --visual
```

`TestVisualRegression` covers:
- `test_doctor_passes` — pre-flight check
- `test_corpus_clean_audit` — every corpus doc audit-clean
- `test_corpus_renders_pdfs_and_hashes` — end-to-end pipeline produces PNGs + hashes
- `test_no_regression_vs_golden` — if `golden.json` exists, current run matches within threshold (skipped if no golden yet)

Gate merges on `pytest --visual` when the baseline is stable.

## Troubleshooting

### `Pre-flight FAILED: LibreOffice (soffice) not found`

```bash
brew install --cask libreoffice
```

Why not Word? `docx2pdf`/Word automation hangs on AppleEvent timeouts when Word has open documents or modal dialogs. LibreOffice headless is reliable, fast, and session-independent. For canonical PDF rendering (user-facing output), `generate.docx_to_pdf()` still uses Word — this tool uses LibreOffice only for the regression pipeline.

### `Corpus file missing`

Markdown files live in Drive; Drive may be paused or offline. Check:

```bash
ls "{Drive}/Shared drives/NEW_Ops/Projects Benelux_Ops/Digital Energy/"
```

### Many pages flagged as changed after a minor edit

Two common causes:

1. **Font drift** — macOS Inter has multiple weight files; a brew update can replace them. Re-approve baseline once.
2. **Page reflow** — adding 2 words in Section 1 can push every subsequent page down by a line. Legitimate; approve.

If either, re-generate, review, approve.

### LibreOffice rendering differs from Word

Possible. LibreOffice and Word share the same OOXML format but rendering engines differ subtly (line-breaking heuristics, kerning, margin accounting). For visual regression we don't care about absolute fidelity — we care about *change detection*. As long as the corpus is rendered by the same engine both at approval and at diff time, regressions are reliably flagged. If you need Word-rendered golden (for more accurate baseline), run approval on a machine where Word automation works without timeout.

### Archive already exists for today

`approve` refuses to overwrite today's Drive archive without `--force`. Wait until tomorrow or pass `--force` (will destroy the previous archive for that day).

## Known limitations

- **Machine-specific baseline** — Inter on your Mac may render differently than on a colleague's. Golden is calibrated for the approver's machine. Multi-approver workflows need either a CI runner as ground truth, or per-machine golden folders.
- **No page-delta visualization** — we report distance; we don't show the pixel diff overlay. Use the Drive archive + OS image compare (Preview's difference tool) for deep forensics.
- **Linear pipeline** — 8 docs × ~50s LibreOffice each = ~7 min serial. Parallelizing soffice calls is possible but complicates error surfacing.
