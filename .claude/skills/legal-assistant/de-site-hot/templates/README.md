# DE Site HoT Templates — Git LFS Stubs (Not Yet Fetched)

## Status

The two `.docx` files in this directory are **Git LFS pointer files**, not real Word documents:

- `hot-grower-annex-a-v1.docx` — 130 B pointer (real binary ~20,491 B)
- `hot-grower-body-v1.docx` — 130 B pointer (real binary: unknown size)

They were copied from `digital-energy-ssot-main/contracts/templates/` during the 2026-04-13 `loi-generator → legal-assistant` restructure. The SSOT Obsidian vault is not a git checkout, so `git lfs pull` cannot be run in place.

## How to fetch the real binaries

One of:

1. Clone the SSOT repo with LFS enabled (assuming it's pushed to a remote that retains LFS objects), then `git lfs pull`, then copy the resolved binaries on top of these stubs.
2. Fetch the binaries directly from a teammate or cloud storage (Dropbox/Drive backup), then overwrite these stubs.
3. Re-export from the source Word files used to author v1.0 (see `template-version.md`).

After fetching, verify:

```bash
file hot-grower-annex-a-v1.docx
# Expected: Microsoft Word 2007+ (or "Zip archive data"), size >5 KB
```

## Dependency for `generate_site_hot.py`

The form-fill engine **cannot** be built or validated until real binaries are present. The engine opens the .docx as a zipfile and parses `word/document.xml` for yellow (`FFFF99`) and green (`CCFFCC`) cell shading — operations that fail on a 130-byte text pointer.

Engine build is tracked in the plan at `/Users/crmg/.claude/plans/temporal-dreaming-meerkat.md` Phase 1.5 (deferred).

## Reference intake data

Working reference intake JSON is available at:

```
../examples/reference-intakes/moerman_annex-a-data.json
../examples/reference-intakes/dec-thermal-7_annex-a-data.json
```

These are the structured field values gathered during the two pilot intakes. Once the engine exists, convert to YAML matching `field-registry.json` and use as smoke-test inputs.
