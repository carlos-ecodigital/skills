# DE Site HoT Templates — Git LFS Stubs (Not Yet Fetched)

## Status

The two `.docx` files in this directory are **Git LFS pointer files**, not real Word documents:

- `hot-grower-annex-a-v1.docx` — 130 B pointer (real binary ~20,491 B)
- `hot-grower-body-v1.docx` — 130 B pointer (real binary ~37,343 B)

The LFS objects are **missing from the GitHub remote** (`git@github.com:carlos-ecodigital/skills.git`) — all four LFS OIDs return 404 on `git lfs fetch --all` (verified 2026-04-16). The Obsidian SSOT vault at `digital-energy-ssot-main/contracts/templates/` also contains only 130-byte stubs (verified 2026-04-16) — the original binaries were added to LFS but the objects were never pushed to any reachable LFS server.

## Canonical location of the real binaries

As of 2026-04-16, the real Word documents are tracked in the sibling `degitos-staging` repo at `domains/legal/templates/` (the repo's `*.docx` .gitignore rule post-dates the commit that added them — `90530b9`):

- `domains/legal/templates/hot-grower-body-v1.docx` (37,343 B, Microsoft Word 2007+)
- `domains/legal/templates/hot-grower-annex-a-v1.docx` (20,491 B, Microsoft Word 2007+)

## How to fetch the real binaries

In order of convenience:

1. **From degitos-staging** (fastest):
   ```bash
   git clone --depth=1 git@github.com:EcoDigital-Software/degitos-staging.git /tmp/ds
   cp /tmp/ds/domains/legal/templates/hot-grower-body-v1.docx \
      /tmp/ds/domains/legal/templates/hot-grower-annex-a-v1.docx \
      "$(dirname "$0")/"
   rm -rf /tmp/ds
   ```
2. Ask a teammate to push the LFS objects to `carlos-ecodigital/skills` LFS server.
3. Re-export from the source Word files (see `template-version.md` for authoring chain).

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
