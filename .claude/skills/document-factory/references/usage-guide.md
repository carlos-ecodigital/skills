# Document Factory -- Usage Guide

## For Non-Technical Users (Google Drive)

### How to Use the .dotx Templates

1. Go to **Shared drives > NEW_Marketing > DE_Marketing > DE_Brand_Assets > 03_Templates > Document_Templates**
2. Double-click the `.dotx` file for the document type you need
3. Word opens a **new untitled document** (the template stays untouched)
4. Replace all `[placeholder text]` with your content
5. Save As your own file using the naming convention below

### Available Templates

| File | When to Use |
|------|-------------|
| `DE_Letter.dotx` | Formal business letters (DIN 5008 envelope-compatible) |
| `DE_Agreement.dotx` | Cover page for any agreement (LOI, NDA, HoT, MSA, SPA) |
| `DE_Seed_Memo.dotx` | Seed fundraising memo for angels and early-stage funds |
| `DE_Investor_Memo.dotx` | Institutional investor memorandum for Series A+ |
| `DE_Exec_Summary.dotx` | 2-page executive summary for meetings, deals, projects |

### File Naming Convention

Format: `YYYYMMDD_DE_[Type]_[Client]_v[N].docx`

Examples:
- `20260406_DE_Agreement_Younggrow_BV_v1.docx`
- `20260410_DE_Seed_Memo_Acme_Fund_v2.docx`
- `20260415_DE_Exec_Summary_PowerGrow_Update_v1.docx`

### What's Pre-Set in Each Template

- Digital Energy logo in header
- Company details in footer (DE Group AG, Baarerstrasse 43, Zug, CHE-408.639.320)
- A4 page size, correct margins
- Inter font (falls back to system font if not installed)
- "Confidential" classification (on agreements and investor docs)

---

## For Technical Users (CLI)

### Setup

```bash
# Install Python deps
pip install python-docx docx2pdf pyyaml

# Microsoft Word must be installed (macOS: Office 365; Windows: Office).
# On macOS, grant Terminal/Python AppleScript permission:
# System Settings → Privacy & Security → Automation

# Navigate to the skill
cd ~/skills/.claude/skills/document-factory

# Test
python3 document_factory.py --profile letter
# Opens output/YYYYMMDD_DE_Letter_v1.docx
```

### PDF conversion and tracked changes

```bash
# Generate + PDF in one step
python3 document_factory.py --profile agreement --agreement-type "Letter of Intent" \
  --client "FrontierOne" --pdf

# Convert an existing .docx (from any skill)
python3 docx_to_pdf.py /path/to/existing.docx
python3 docx_to_pdf.py doc.docx -o custom.pdf

# Accept all tracked changes in a redlined .docx
python3 accept_changes.py redlined.docx         # → redlined_accepted.docx
python3 accept_changes.py redlined.docx -o clean.docx
```

Both utilities are Word-only (no LibreOffice fallback).

### Generating Documents

```bash
# Agreement cover pages (new structured flags)
python3 document_factory.py --profile agreement \
  --agreement-type "Letter of Intent" \
  --subject "for AI Infrastructure Distribution" \
  --client "FrontierOne Ltd"

# Binding agreement (auto-detects formality, shows registration numbers)
python3 document_factory.py --profile agreement \
  --agreement-type "Master Service Agreement" \
  --subject "for Hosting Ethiopia Data Center" \
  --client "Acme Corp" \
  --client-address "123 Main St, Amsterdam" \
  --client-reg-type KvK --client-reg-number 12345678

# Using NL entity instead of default AG
python3 document_factory.py --profile agreement \
  --agreement-type "Letter of Intent" \
  --client "Partner BV" --entity nl

# Other profiles
python3 document_factory.py --profile letter
python3 document_factory.py --profile seed_memo --client "Acme Fund"
python3 document_factory.py --profile investor_memo --client "Infrastructure Partners"
python3 document_factory.py --profile exec_summary --title "PowerGrow Project Update"

# With specific date and version
python3 document_factory.py --profile seed_memo --client "Fund X" --date 2026-04-10 --version 2

# Also produce a .dotx template
python3 document_factory.py --profile agreement --agreement-type "NDA" --client "Partner" --dotx

# Custom output path
python3 document_factory.py --profile exec_summary --title "Board Update" --output ~/Documents/board_update.docx
```

### Converting Markdown to Branded DOCX

```bash
# Simple: just brand the markdown
python3 document_factory.py --md content.md --title "Report Title" --output report.docx

# With cover page
python3 document_factory.py --md content.md --title "Q1 Update" --client "Board" --cover --output update.docx
```

### Changing the Entity

Edit the `ENTITY` dict at the top of `document_factory.py`:

```python
ENTITY = {
    "legal_name": "Digital Energy Group AG",
    "address": "Baarerstrasse 43, 6300 Zug, Switzerland",
    "registration": "CHE-408.639.320",
    "website": "digital-energy.group",
    "return_address": "Digital Energy Group AG  •  Baarerstrasse 43  •  6300 Zug",
}
```

### Adding a New Profile

1. Define sections:
```python
MY_SECTIONS = [
    ("1. Section Title", "Guidance text explaining what to write here."),
    ("2. Another Section", "More guidance."),
]
```

2. Write the profile function:
```python
def profile_my_doc(title="My Document", client="[Client]", date_str="", version=1, **kw):
    doc = new_doc(diff_first=True)
    setup_first_page_header(doc.sections[0])
    setup_cont_header(doc.sections[0], title=title)
    setup_first_footer(doc.sections[0], classification="Confidential")
    setup_cont_footer(doc.sections[0], classification="Confidential")
    add_cover(doc, title=title, subtitle="Subtitle", metadata={
        "Prepared for": client, "Date": date_str, "Version": f"v{version}",
    })
    for t, g in MY_SECTIONS:
        add_section(doc, t, g)
    return doc
```

3. Register it:
```python
PROFILES["my_doc"] = profile_my_doc
PROFILE_CODES["my_doc"] = "My_Doc"
```

4. Run: `python3 document_factory.py --profile my_doc --client "Test"`
