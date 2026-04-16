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

Content skills produce the words. Document Factory produces the file — including cover pages, headers, and footers. Any skill that generates a `.docx` with a cover page delegates to Document Factory; no skill renders its own.

```
content skill → structured content (markdown / sections / clauses)
    → document-factory
        → branded .docx with logo, headers, footers, cover page, entity details
```

## Upstream Skills (content producers)

| Skill | Produces | Factory Profile |
|-------|----------|-----------------|
| `legal-assistant` (colocation stream) | LOI/NCNDA clauses | `agreement` (has its own `colocation/generate_loi.py` with DE branding integrated) |
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
| `agreement` | LOI, NDA, HoT, MSA, SPA cover page | Yes | Confidential |
| `seed_memo` | Seed fundraising memo (8 sections) | Yes | Confidential |
| `investor_memo` | Institutional IM (10 sections) | Yes | Confidential |
| `exec_summary` | 2-page standalone summary | No | None |

## Cover Page System

Agreement cover pages follow an IB-standard hierarchy:
1. **Agreement type** (28pt) — e.g. "Letter of Intent", "Master Service Agreement"
2. **Subject** (14pt) — deal description, e.g. "for AI Infrastructure Distribution"
3. **Date** — document-level, below title block
4. **Party blocks** — legal name, address, registration (binding only)
5. **Metadata** — reference, version, classification

### Formality levels
- **Non-binding** (LOI, NDA, HoT, MoU): party labels "Between: / And:", no registration numbers
- **Binding** (MSA, SPA, JVA, SHA): party labels "By and between: / And:", registration numbers shown

### Entity selection
- `--entity ag` → Digital Energy Group AG (default)
- `--entity nl` → Digital Energy Netherlands B.V.

## Quick Start

```bash
cd /path/to/skills/.claude/skills/document-factory

# Non-binding LOI cover
python3 generate.py --profile agreement \
  --agreement-type "Letter of Intent" \
  --subject "for AI Infrastructure Distribution" \
  --client "FrontierOne Ltd"

# Binding MSA cover (auto-detects binding from type)
python3 generate.py --profile agreement \
  --agreement-type "Master Service Agreement" \
  --subject "for Hosting Ethiopia Data Center" \
  --client "Acme Corp" \
  --client-address "123 Main St, Amsterdam" \
  --client-reg-type KvK --client-reg-number 12345678

# With NL entity
python3 generate.py --profile agreement \
  --agreement-type "Letter of Intent" \
  --subject "for AI Colocation Services" \
  --client "Partner BV" --entity nl

# Other profiles (unchanged)
python3 generate.py --profile letter
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
| `--agreement-type` | Agreement name (e.g. "Letter of Intent") | Placeholder |
| `--subject` | Deal description sub-header | None |
| `--title` | Document title (legacy; maps to --agreement-type for agreement) | Auto per profile |
| `--client` | Client/counterparty name | Placeholder |
| `--client-address` | Counterparty address | Placeholder |
| `--client-reg-type` | Registration type (KvK, CHE, EIN) | None |
| `--client-reg-number` | Registration number | None |
| `--entity` | DE contracting entity: ag, nl | ag |
| `--formality` | Override: binding, non_binding | Auto-detected |
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

## Utilities

| Script | Purpose |
|--------|---------|
| `generate.py` | Generate branded .docx for all profiles (primary entry point) |
| `docx_to_pdf.py` | Standalone CLI: convert any .docx → .pdf via Microsoft Word |
| `accept_changes.py` | Accept all tracked changes in a .docx via Word |

```bash
# PDF conversion (any .docx)
python3 docx_to_pdf.py path/to/document.docx
python3 docx_to_pdf.py doc.docx -o out.pdf

# Accept tracked changes
python3 accept_changes.py redlined.docx
python3 accept_changes.py redlined.docx -o clean.docx

# Generate + immediately produce PDF
python3 generate.py --profile agreement --agreement-type "Letter of Intent" --client "FrontierOne" --pdf
```

**Word-only:** Both utilities drive Microsoft Word (AppleScript on macOS, COM on Windows). No LibreOffice fallback — Word's rendering of .docx is canonical; LibreOffice drift was deemed worse than a clean error.

## Office Bridge — Anthropic Skill Integration

`office_bridge.py` discovers and wraps Anthropic's bundled office-skills toolchain (docx, pdf, xlsx, pptx) at runtime. These scripts live in session-scoped directories managed by Claude Code and **update automatically** with each Anthropic release — no manual syncing needed.

**Architecture:** Document Factory owns CREATION (python-docx, branded). Office Bridge adds VALIDATION, EDITING, and CONVERSION from Anthropic's toolchain.

```
Document Factory (create branded .docx)
    → office_bridge.validate()     — OOXML schema check before external send
    → office_bridge.unpack/pack()  — XML editing for tracked changes, comments
    → office_bridge.to_pdf()       — LibreOffice fallback when Word unavailable
    → office_bridge.fill_pdf()     — Permit form filling (RVO, gemeente)
```

### Quick Start

```bash
# Check what's available
python3 office_bridge.py status

# Validate before sending externally
python3 office_bridge.py validate output.docx

# Convert to PDF (LibreOffice, no Word needed)
python3 office_bridge.py to-pdf output.docx

# Unpack for tracked changes / comments
python3 office_bridge.py unpack output.docx unpacked/
# ... edit XML in unpacked/word/ ...
python3 office_bridge.py pack unpacked/ output_edited.docx output.docx
```

### Python API

```python
from office_bridge import OfficeBridge

bridge = OfficeBridge()
bridge.validate("output.docx")                          # Schema check
bridge.unpack("doc.docx", "unpacked/")                  # For XML editing
bridge.add_comment("unpacked/", 0, "Review this")       # Insert comment
bridge.pack("unpacked/", "edited.docx", original="doc.docx")
bridge.to_pdf_libreoffice("doc.docx")                   # PDF without Word
bridge.fill_pdf_form("template.pdf", {"field": "val"})  # PDF forms
```

### How it stays current

Anthropic deploys skill scripts fresh each Claude Code session to:
`~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/*/`

The bridge discovers the latest session's scripts via glob, never copies them. When Anthropic ships updates (new validators, bug fixes, new capabilities), the bridge picks them up automatically next session. No maintenance required.

**Capabilities sourced from Anthropic (auto-updating):**

| Capability | Anthropic Skill | Bridge Method |
|---|---|---|
| OOXML schema validation | docx | `validate()` |
| Unpack .docx to XML | docx | `unpack()` |
| Repack XML to .docx | docx | `pack()` |
| Insert comments | docx | `add_comment()` |
| .docx → PDF (LibreOffice) | docx | `to_pdf_libreoffice()` |
| .doc → .docx conversion | docx | `doc_to_docx()` |
| PDF → images | pdf | `pdf_to_images()` |
| PDF form field check | pdf | `check_pdf_form()` |
| PDF form filling | pdf | `fill_pdf_form()` |
| .xlsx validation | xlsx | `validate_xlsx()` |
| .xlsx recalculation | xlsx | `recalc_xlsx()` |
| .pptx validation | pptx | `validate_pptx()` |

**Capabilities owned by Document Factory (DE-controlled):**

| Capability | Script | Notes |
|---|---|---|
| Branded .docx creation | `generate.py` | python-docx, DE brand, 5 profiles |
| .docx → PDF (Word) | `docx_to_pdf.py` | Higher fidelity than LibreOffice |
| Accept tracked changes | `accept_changes.py` | Word-only (canonical rendering) |

### Recommended workflow for external documents

```bash
# 1. Create branded .docx
python3 generate.py --profile agreement --entity nl --client "Arco Vreugdenhil" ...

# 2. Validate before sending
python3 office_bridge.py validate output.docx

# 3. Convert to PDF
python3 docx_to_pdf.py output.docx        # Word (preferred)
python3 office_bridge.py to-pdf output.docx  # LibreOffice (fallback)
```

## Requirements

- Python 3.9+ with `python-docx`, `docx2pdf` (for `--pdf` and `docx_to_pdf.py`), `pyyaml` (for LOI generator)
- **Microsoft Word** (macOS: Office 365; Windows: Office) — required for PDF conversion and tracked-changes acceptance
- On macOS, AppleScript automation must be permitted: System Settings → Privacy & Security → Automation
- **Office Bridge additionally requires:** `defusedxml` (for Anthropic's validator), LibreOffice (for headless PDF conversion fallback). Install: `pip install defusedxml` + `brew install --cask libreoffice`
- Inter font (optional — falls back to Arial)

## Technical Note

Uses **only native python-docx API**. No `OxmlElement` or raw XML manipulation -- this corrupts .docx files on Word for Mac.
