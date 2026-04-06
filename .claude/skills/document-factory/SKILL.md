---
name: document-factory
description: >-
  Single entry point for all branded Digital Energy .docx production. Any skill
  that produces content (investor memos, LOIs, exec summaries, board papers,
  permit documents, proposals) hands off to document-factory for final branded
  .docx output. Produces DIN 5008 letters, agreement covers, seed memos,
  institutional IMs, executive summaries, and converts markdown to branded
  documents. This skill should be used when the user asks to "generate a
  document", "create a letterhead", "produce an agreement", "make an investor
  memo", "branded docx", "convert markdown to docx", "final document",
  "produce the deliverable", or any request for a branded .docx file.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# Document Factory

**The single production line for all branded Digital Energy .docx output.**

Content skills produce the words. Document Factory produces the file.

```
content skill → structured content (markdown / sections / clauses)
    → document-factory
        → branded .docx with logo, headers, footers, cover page, entity details
```

## Upstream Skills (content producers)

| Skill | Produces | Factory Profile |
|-------|----------|-----------------|
| `loi-generator` | LOI/NCNDA clauses | `agreement` (has its own generate_loi.py with DE branding integrated) |
| `investor-memo-writer` | Investment memoranda, DD responses | `investor_memo` or `seed_memo` |
| `seed-fundraising` | Pitch content, fundraising materials | `seed_memo` |
| `document-writer` | Board papers, exec summaries, memos | `exec_summary` or markdown mode |
| `document-presenter` | HTML documents (when .docx needed instead) | markdown mode with `--cover` |
| `permit-drafter` | Dutch permit applications | `agreement` cover or markdown mode |
| `collateral-studio` | One-pagers, proposals, whitepapers | markdown mode with `--cover` |
| `executive-comms` | Formal memos, letters | `letter` |

## Profiles

| Profile | Use | Cover Page | Classification |
|---------|-----|------------|----------------|
| `letter` | Formal correspondence (DIN 5008) | No | None |
| `agreement` | LOI, NDA, HoT, MSA cover page | Yes | Confidential |
| `seed_memo` | Seed fundraising memo (8 sections) | Yes | Confidential |
| `investor_memo` | Institutional IM (10 sections) | Yes | Confidential |
| `exec_summary` | 2-page standalone summary | No | None |

## Quick Start

```bash
cd /path/to/skills/.claude/skills/document-factory

# From a profile
python3 generate.py --profile letter
python3 generate.py --profile agreement --title "Colocation Agreement" --client "Younggrow BV"
python3 generate.py --profile seed_memo --client "Acme Fund"
python3 generate.py --profile investor_memo --client "Infrastructure Partners"
python3 generate.py --profile exec_summary --title "PowerGrow Project Update"

# From markdown (any content skill's output)
python3 generate.py --md content.md --title "Report Title" --output report.docx
python3 generate.py --md content.md --title "Report" --client "Board" --cover --output report.docx

# Add --dotx for Word template
python3 generate.py --profile seed_memo --client "Fund X" --dotx
```

## CLI Reference

| Flag | Description | Default |
|------|-------------|---------|
| `--profile` | Document profile | Required (unless --md) |
| `--title` | Document title | Auto per profile |
| `--client` | Client/counterparty name | Placeholder |
| `--date` | Date (YYYY-MM-DD) | Today |
| `--version` | Version number | 1 |
| `--output` | Output file path | Auto-named in output/ |
| `--dotx` | Also save as .dotx Word template | Off |
| `--md` | Input markdown file | None |
| `--cover` | Add cover page (markdown mode) | Off |

## Auto-Naming

`YYYYMMDD_DE_[Type]_[Client]_v[N].docx`

## Entity Configuration

Edit `ENTITY` dict at top of `generate.py`.

## Adding New Profiles

1. Define sections as `(title, guidance_text)` tuples
2. Write `profile_xyz()` function
3. Add to `PROFILES` and `PROFILE_CODES` dicts
4. See `references/usage-guide.md`

## Non-Technical Users

.dotx Word templates available in Google Drive:
`NEW_Marketing/DE_Marketing/DE_Brand_Assets/03_Templates/Document_Templates/`

## Requirements

- Python 3.9+ with `python-docx`
- Inter font (optional -- falls back to Arial)

## Technical Note

Uses **only native python-docx API**. No `OxmlElement` or raw XML manipulation -- this corrupts .docx files on Word for Mac.
