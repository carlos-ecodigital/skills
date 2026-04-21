---
title: "Legal Assistant — Staging Mirror Discipline"
domain: SKILL
tier: 2
owner: "@carlos-ecodigital"
status: active
confidentiality: internal
version: v3.7.2
created: 2026-04-21
updated: 2026-04-21
review-date: 2026-07-21
---

# Staging Mirror Discipline

The `legal-assistant` skill is developed upstream at
`carlos-ecodigital/skills` and mirrored to the staging monorepo at
`EcoDigital-Software/degitos-staging` under a `de-` prefix convention.
This doc captures the mirror invariants + known substitutions.

## Path map

| Upstream | Staging |
|---|---|
| `.claude/skills/legal-assistant/*` | `skills/de-legal-assistant/*` |
| `.claude/skills/_shared/*` | `skills/_shared/*` |
| `.claude/skills/de-executive-comms/*` | `skills/de-executive-comms/*` (staging had a pre-existing skill with this name; mirror adds NEW files only, does not overwrite `SKILL.md`) |
| `.claude/skills/document-factory/*` | `skills/de-document-factory/*` |

## Known substitutions in `sales/generate_loi.py`

The only code-level difference between upstream and staging is the
sibling-skill import line that adds `document-factory` to `sys.path`.
Staging must substitute `document-factory` → `de-document-factory`:

```python
# Upstream (canonical):
sys.path.insert(0, str(SCRIPT_DIR.parent.parent / "document-factory"))

# Staging (mirror):
sys.path.insert(0, str(SCRIPT_DIR.parent.parent / "de-document-factory"))
```

The upstream file carries a `⚠️ STAGING MIRROR SENTINEL` comment at that
line. Mirror scripts should grep for the sentinel and substitute the
path. Remove-the-comment-and-think-you-fixed-it is a bug — the comment
is load-bearing for future mirrors.

## Staging CI extras (not in upstream)

Staging runs additional CI checks that upstream does not:

1. **frontmatter-check** — every new `.md` file outside `SKILL.md`,
   `CHANGELOG.md`, `README.md`, etc. must carry YAML frontmatter with
   mandatory fields `title`, `domain`, `status`. Tier in `[0,1,2,3]`.
   Status from a closed set (`draft|active|deprecated|archived|pending|
   current|processed|pending-extraction|concept|final|decided|signed|
   expired`).
2. **binary-check**, **structure-check**, **sensitive-scan**,
   **index-check**, **test** — standard checks.

When mirroring v3.7.x upgrades, any new `.md` files in `_shared/`,
`docs/`, or `_shared/fireflies-integration.md`-class sibling files need
frontmatter added for staging. Upstream doesn't require it.

## Mirror flow (manual, until automated)

1. On upstream PR merge, create a parallel branch on staging:
   `carlos/loi-v{X.Y.Z}-{slug}`.
2. `cp` or `rsync` the changed files from upstream to staging with the
   path map above.
3. Apply the `document-factory` → `de-document-factory` substitution in
   `sales/generate_loi.py`. (Search-and-replace on the exact sentinel'd
   block.)
4. Add frontmatter to any newly-created `.md` files under
   `_shared/`, `legal-assistant/_shared/`, `legal-assistant/docs/`.
5. Regenerate goldens if content-rendering changed (`pytest
   tests/test_golden_files.py --update-goldens`).
6. Run `bash sales/tests/regen-mirror-manifest.sh` on upstream and copy
   the manifest verbatim to staging.
7. Verify `pytest sales/tests/ -q` green on staging.
8. Commit with `mirror` in the subject + open PR; squash-merge AFTER
   upstream PR is merged.

## Mirror-manifest scope (v3.7.0)

The `sales/tests/mirror-manifest.txt` file lists SHA256 hashes of the
test-infrastructure files that MUST be byte-identical between upstream
and staging. Current scope (v3.7.0+):

- `tests/_fingerprint.py`
- `tests/conftest.py`
- `tests/test_golden_files.py`
- `tests/test_visual_layout.py`
- `tests/test_intake_structural_shape.py`

Whenever one of these changes upstream, regenerate the manifest:

```bash
cd sales && bash tests/regen-mirror-manifest.sh
```

Then copy the manifest to staging verbatim; staging CI checks each hash
against the file content.

## Version-tag sentinels

Upstream `CHANGELOG.md` is the source of truth for skill-release
version numbers. Template filename version (`DE-LOI-{Type}-v3.2`)
tracks the template lineage, not the skill release. Staging CHANGELOG
is a byte-identical mirror of upstream (modulo mirror-specific prose
about staging adaptations).
