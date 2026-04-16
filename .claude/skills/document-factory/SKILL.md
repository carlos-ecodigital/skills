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

## Scope

### What You Own
- Branded .docx creation (all profiles: letter, agreement, seed_memo, investor_memo, exec_summary)
- Cover page rendering (entity details, party blocks, formality detection, metadata)
- Markdown-to-docx conversion with brand formatting (headers, tables, lists, inline styles)
- OOXML validation via Office Bridge
- PDF conversion via Word (canonical) or LibreOffice (fallback)
- Tracked-changes acceptance

### What You Do NOT Own
- **Content creation** — content skills (legal-assistant, seed-fundraising, collateral-studio) produce the words; document-factory only formats them
- **Legal review** — formality detection is mechanical (dict lookup), not legal advice. Counsel reviews the content.
- **Design** — visual identity is governed by `de-brand-bible` (messaging) and `de-brand-book` (design tokens). Document-factory implements their decisions, does not make them.
- **PDF-only workflows** — if the deliverable is PDF-native (permit forms, RVO applications), use office_bridge.fill_pdf() directly
- **Slide decks / presentations** — .pptx is out of scope; use collateral-studio or Gamma

## Anti-Patterns

1. **Do not use OxmlElement or raw XML string parsing.** Use `lxml.etree` + `docx.oxml.ns.qn` through the same tree python-docx builds. OxmlElement creates orphaned elements that corrupt .docx on Word for Mac.
2. **Do not use LibreOffice for final PDF output.** Word is canonical — LO rendering drifts (table widths, font substitution, page breaks). LO is fallback only.
3. **Do not embed logos as base64 or inline data.** Always reference the file from `assets/`. python-docx handles the packaging.
4. **Do not hardcode entity details in profile functions.** Use `DE_ENTITIES` dict and `ENTITY_FOOTERS` — one source of truth for all profiles.
5. **Do not skip OOXML validation before external send.** Use `--validate` or `office_bridge.validate()`. A single missing attribute (like `w:percent` on `w:zoom`) causes Word to repair the file, which can strip formatting.

## Office Bridge

`office_bridge.py` wraps Anthropic's bundled office-skills toolchain (docx, pdf, xlsx, pptx) via runtime discovery. Auto-updates with each Claude Code session.

See `references/office-bridge.md` for full API, capabilities table, and workflow examples.

## Eval Scenarios

### 1. Binding NL agreement cover
**Input:** `--profile agreement --agreement-type "Master Service Agreement" --client "Test BV" --client-reg-type KvK --client-reg-number 12345678 --entity nl`
**Expected:** Cover shows "By and between:", NL entity with KvK number, client with KvK, no "subsidiary of" text. Footer single line with `·` separators.
**Success:** `office_bridge.validate()` passes. No literal `**` markers. Registration renders as `KvK: 98580086` not `KvK: KvK 98580086`.

### 2. Non-binding LOI cover (AG entity)
**Input:** `--profile agreement --agreement-type "Letter of Intent" --client "FrontierOne Ltd" --subject "for AI Infrastructure Distribution"`
**Expected:** Cover shows "Between:" / "And:". No registration numbers. Subject line at 14pt slate.
**Success:** Parties have names + addresses only. Subject renders below title.

### 3. Markdown-to-docx with tables and bold
**Input:** `--md sample.md --title "Test Report" --cover --entity nl --strip-review`
**Expected:** Tables have Cobalt headers, proportional columns, fit within margins. `**bold**` renders as bold, not literal asterisks. `[REVIEW REQUIRED...]` markers stripped with count printed.
**Success:** All tables within 165mm width. Header row has `0034AF` fill. Bold runs have `b=True`.

### 4. Formality auto-detection (prefix match)
**Input:** `md_to_docx(text, title="Board Resolution — SAR Program Adoption", cover=True, entity="nl")`
**Expected:** `_detect_formality()` returns `"binding"` via prefix match on `"Board Resolution"`. Cover shows "By and between:".
**Success:** formality == "binding". Registration numbers shown.

### 5. OOXML validation (zoom fix)
**Input:** Generate any document, inspect `w:zoom` element.
**Expected:** `save_doc()` ensures `w:percent="100"` attribute exists on `w:zoom`.
**Success:** `office_bridge.validate()` returns "All validations PASSED". No Word repair dialog on open.

## Requirements

- Python 3.9+ with `python-docx`, `docx2pdf` (for `--pdf` and `docx_to_pdf.py`), `pyyaml` (for LOI generator)
- **Microsoft Word** (macOS: Office 365; Windows: Office) — required for PDF conversion and tracked-changes acceptance
- On macOS, AppleScript automation must be permitted: System Settings → Privacy & Security → Automation
- **Office Bridge additionally requires:** `defusedxml` (for Anthropic's validator), LibreOffice (for headless PDF conversion fallback). Install: `pip install defusedxml` + `brew install --cask libreoffice`
- Inter font (optional — falls back to Arial)

## Technical Note

Uses **only native python-docx API**. No `OxmlElement` or raw XML manipulation -- this corrupts .docx files on Word for Mac.
