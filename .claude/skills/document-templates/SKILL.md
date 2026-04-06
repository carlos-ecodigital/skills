---
name: document-templates
description: >-
  Branded document template generator for Digital Energy. Produces DIN 5008 letters,
  agreement cover pages, seed investment memos, institutional investor memoranda,
  and executive summaries as .docx/.dotx files. Also converts markdown to branded
  documents. This skill should be used when the user asks to "generate a letterhead",
  "create an agreement template", "make an investor memo", "produce an executive summary",
  "convert markdown to docx", "branded document", "document template", or "dotx template".
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# Document Templates

Generates branded Digital Energy .docx and .dotx documents using `python-docx`.

## Requirements

- Python 3.9+
- `python-docx` (`pip install python-docx`)
- Inter font installed (optional but recommended -- falls back to system fonts)

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
# Navigate to skill directory
cd /path/to/skills/.claude/skills/document-templates

# Generate a letter
python3 generate.py --profile letter

# Generate an agreement cover
python3 generate.py --profile agreement --title "Colocation Agreement" --client "Younggrow BV"

# Generate a seed memo
python3 generate.py --profile seed_memo --client "Acme Fund"

# Generate an investor memo
python3 generate.py --profile investor_memo --client "Infrastructure Partners"

# Generate an executive summary
python3 generate.py --profile exec_summary --title "PowerGrow Project Update"

# Convert markdown to branded document
python3 generate.py --md input.md --title "Report Title" --output report.docx

# Convert markdown with cover page
python3 generate.py --md input.md --title "Report" --client "Board" --cover --output report.docx

# Add --dotx to any command to also produce a Word template
python3 generate.py --profile seed_memo --client "Fund X" --dotx
```

## CLI Reference

| Flag | Description | Default |
|------|-------------|---------|
| `--profile` | Document profile (letter/agreement/seed_memo/investor_memo/exec_summary) | Required (unless --md) |
| `--title` | Document title | Auto per profile |
| `--client` | Client/counterparty name | Placeholder |
| `--date` | Date (YYYY-MM-DD) | Today |
| `--version` | Version number | 1 |
| `--output` | Output file path | Auto-named in output/ |
| `--dotx` | Also save as .dotx Word template | Off |
| `--md` | Input markdown file (markdown mode) | None |
| `--cover` | Add cover page (markdown mode only) | Off |

## Auto-Naming

Output: `YYYYMMDD_DE_[Type]_[Client]_v[N].docx`

Example: `20260406_DE_Seed_Memo_Acme_Fund_v1.docx`

## Entity Configuration

Edit the `ENTITY` dict at the top of `generate.py` to change the legal entity details shown in footers and cover pages.

## Adding New Profiles

1. Define sections as a list of `(title, guidance_text)` tuples
2. Write a `profile_xyz()` function following the existing pattern
3. Add to the `PROFILES` dict
4. Add to `PROFILE_CODES` for auto-naming

See `references/usage-guide.md` for detailed instructions.

## Cross-References

- **Brand source:** `de-brand-bible` skill (colors, fonts, voice rules)
- **Brand tokens:** `brand-book` skill (design tokens, page masters)
- **Drive templates:** `NEW_Marketing/DE_Marketing/DE_Brand_Assets/03_Templates/Document_Templates/`
- **Content skills:** `document-writer` (content production), `document-presenter` (HTML rendering)
