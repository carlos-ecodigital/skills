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
# Ensure python-docx is installed
pip install python-docx

# Navigate to the skill
cd ~/skills/.claude/skills/document-factory

# Test
python3 generate.py --profile letter
# Opens output/YYYYMMDD_DE_Letter_v1.docx
```

### Generating Documents

```bash
# Each profile
python3 generate.py --profile letter
python3 generate.py --profile agreement --title "Colocation Agreement" --client "Younggrow BV"
python3 generate.py --profile seed_memo --client "Acme Fund"
python3 generate.py --profile investor_memo --client "Infrastructure Partners"
python3 generate.py --profile exec_summary --title "PowerGrow Project Update"

# With specific date and version
python3 generate.py --profile seed_memo --client "Fund X" --date 2026-04-10 --version 2

# Also produce a .dotx template
python3 generate.py --profile agreement --title "NDA" --client "Partner" --dotx

# Custom output path
python3 generate.py --profile exec_summary --title "Board Update" --output ~/Documents/board_update.docx
```

### Converting Markdown to Branded DOCX

```bash
# Simple: just brand the markdown
python3 generate.py --md content.md --title "Report Title" --output report.docx

# With cover page
python3 generate.py --md content.md --title "Q1 Update" --client "Board" --cover --output update.docx
```

### Changing the Entity

Edit the `ENTITY` dict at the top of `generate.py`:

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

4. Run: `python3 generate.py --profile my_doc --client "Test"`
