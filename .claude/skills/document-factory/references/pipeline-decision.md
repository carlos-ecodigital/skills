# Pipeline Decision Guide

The document-factory has three pipelines. `document_factory.build()` routes to the correct one automatically based on the shape of your input. This page is the reference for which pipeline applies when, and why.

## TL;DR

| Your input | Pipeline | Entry point | Status |
|---|---|---|---|
| `.docx` on disk + counterparty details | **B** — Preserving rebrand | `build(path, rebrand_spec=...)` or `rebrand.rebrand(...)` | Ready (M3) |
| Markdown string / `.md` file (board memo, exec summary, report) | **C** — Markdown | `build(md_text, md_opts={...})` or `md_to_docx(...)` | Ready |
| Markdown string + profile `"agreement"` | **C, deprecated** | Same as above — emits `DeprecationWarning` | Deprecated (M5) |
| `dict` / `AgreementSpec` (YAML-loaded deal data) | **A** — Structured intake | `legal-assistant/colocation/generate_loi.py` | Interim — `build()` raises `NotImplementedError` with this pointer until M4 merges the builders into document-factory |

## Full decision table

| Input shape | Companion arg | Profile | Pipeline | Notes |
|---|---|---|---|---|
| `.docx` path, file exists | `rebrand_spec=RebrandSpec(...)` | — | **B** | Preserves body (numbering, lists, tables, track changes). Strips old cover + `THE UNDERSIGNED` block. Returns bytes. |
| `.docx` path, file exists | *missing* | — | **error** | `TypeError`: Pipeline B requires a `RebrandSpec`. |
| `.docx` path, file does **not** exist | `rebrand_spec=...` | — | **error** | `TypeError` at dispatcher; `FileNotFoundError` downstream. |
| Markdown string (`# Heading\n\n…`) | `md_opts={...}` | `None` / non-agreement | **C** | No warning. Returns `Document`. |
| Markdown string | `md_opts={...}` | `"agreement"` (or any in `AGREEMENT_PROFILES`) | **C**, warns | `DeprecationWarning` — markdown loses native numbering, lists, and QA. Use Pipeline A or B. |
| `.md` / `.markdown` path | `md_opts={...}` | same as above | **C** (same rules) | File is read; contents treated as markdown. |
| `dict` | (any) | — | **A — not implemented** | `NotImplementedError` pointing to `legal-assistant/colocation/generate_loi.py`. |
| `agreement_spec=...` explicit | (any) | — | **A — not implemented** | Same as above. |

## When to use which

### Pipeline A — Structured intake (dict / `AgreementSpec`)

**Use when:** You are drafting a new agreement from scratch (LOI, NDA, MSA, bespoke, …). You have structured data — parties, recitals, clauses, signatures — already validated.

**Why:** Deterministic. Same spec + same code → byte-identical `.docx` (after normalization). Build-time QA catches banned phrases, Unicode arrows, missing registrations, placeholder addresses, `THE UNDERSIGNED` duplication (R-21). Every deal can graduate into the template library.

**Today's entry point:** `legal-assistant/colocation/generate_loi.py` (YAML intake, 5 LOI types, extending to Bespoke in M4). The long-term home is `document_factory.build(dict)` / `build_agreement(spec)` once M4 lands and the builders move into `document-factory/builders/`.

**Example (today, via legal-assistant):**
```bash
cd ~/Claude/skills/.claude/skills/legal-assistant/colocation
python3 generate_loi.py --yaml deal.yaml --output ~/Downloads/deal.docx
```

### Pipeline B — Preserving rebrand (`.docx` → `.docx`)

**Use when:** You have an existing `.docx` drafted in Word, received from outside counsel, or supplied by a counterparty. The body is the deliverable; you need DE cover, headers, footers, and styling without re-authoring.

**Why:** Native numbering preserved. Lists preserved. Tables preserved. Defined-term bolding preserved. **Tracked changes preserved** (never touches `w:ins` / `w:del`). No markdown round-trip loss.

**Caveat:** Content QA is post-hoc, not build-time. The input's content is not schema-validated. Sloppy content in → prettier shell around sloppy content. Always run `audit_agreement()` after rebrand (the CLI has `--audit`).

**Example (dispatcher):**
```python
from pathlib import Path
from common import build, RebrandSpec

spec = RebrandSpec(
    agreement_type="Letter of Intent",
    client="Acme B.V.",
    client_address="123 Main St, 1000 AA Amsterdam",
    entity="nl",
)
out_bytes = build(Path("~/Downloads/counsel_draft.docx").expanduser(),
                  rebrand_spec=spec)
Path("~/Downloads/rebranded.docx").expanduser().write_bytes(out_bytes)
```

**Example (CLI):**
```bash
python3 rebrand.py ~/Downloads/counsel_draft.docx \
  --agreement-type "Letter of Intent" \
  --client "Acme B.V." \
  --client-address "123 Main St, 1000 AA Amsterdam" \
  --entity nl \
  --output ~/Downloads/rebranded.docx \
  --audit
```

### Pipeline C — Markdown (content skills → branded .docx)

**Use when:** A content skill produced markdown you need to brand. Typical cases: board memos, executive summaries, one-pagers, investor reports, permit drafts, proposals.

**Why:** Fast. Flexible. Content skills own the words; the factory owns the cover and chrome.

**Do not use for agreements.** Markdown cannot carry native Word numbering, cannot carry the `(A) / (B) / (C)` recital lettering scheme, and bypasses the build-time QA catalog that agreements require. As of M5 you will see a `DeprecationWarning` if you try; the warning will become an error in the next minor version.

**Example (dispatcher, non-agreement):**
```python
from common import build

md = Path("~/Downloads/board_memo.md").expanduser().read_text()
doc = build(md, md_opts={
    "title": "Q2 Board Memo",
    "client": "DE Board",
    "entity": "nl",
    "cover": True,
})
doc.save("~/Downloads/Q2_board_memo.docx")
```

## The deprecation, in detail

M5 adds a `DeprecationWarning` to **markdown + agreement profile**. The message names both alternative pipelines and explains the structural reasons:

> Markdown round-tripping loses native numbering, loses native list/recital lettering, and cannot carry the build-time QA that agreements require (R-11 banned phrases, R-21 no-undersigned-when-cover-has-parties, party-duplication checks, etc.).

- **M5 (now):** Warning — the path still works. Callers have one minor-version cycle to migrate.
- **M6+ (next minor):** Error — the path is removed. `build(md, profile="agreement")` raises.

If you hit this warning:
- **New drafts:** move to Pipeline A. YAML in, branded .docx out. Templates live in `legal-assistant/colocation/templates/`.
- **Existing Word drafts:** move to Pipeline B. `rebrand(input.docx, RebrandSpec(...))` gives you DE branding without rewriting.
- **Content skills that currently produce markdown agreement drafts:** redirect them to emit YAML for the legal-assistant instead, or hand off the `.docx` to rebrand.

## How routing is decided

Precedence in `build()` (see `dispatcher.py`):

1. If `input` is a `dict` **or** `agreement_spec` is provided → Pipeline A (currently `NotImplementedError`).
2. If `input` is a `.docx` path that exists → Pipeline B. Requires `rebrand_spec`.
3. If `input` is a `.md` / `.markdown` path that exists, **or** a `str` that isn't one of the above → Pipeline C. Emits `DeprecationWarning` if `profile` is in `AGREEMENT_PROFILES`.
4. Otherwise → `TypeError` with a pointer to each pipeline.

## `AGREEMENT_PROFILES`

Currently `{"agreement"}`. If new agreement-like profiles are added (e.g. `nda`, `msa_skeleton`), extend this set in `dispatcher.py`. The deprecation policy travels with the set — adding a profile means the markdown path emits a warning the same day the profile exists.

## Related

- `SKILL.md` — top-level overview, CLI reference, Quick Start.
- `rebrand.py` — Pipeline B implementation.
- `generate.py` — Pipeline C implementation (`md_to_docx`) and profile renderers.
- `legal-assistant/colocation/generate_loi.py` — Pipeline A (today's entry point).
- `validators.py` / `audit_profiles.py` — build-time gates (R-11, R-21, …).
