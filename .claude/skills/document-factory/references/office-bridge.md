# Office Bridge — Anthropic Skill Integration

`office_bridge.py` discovers and wraps Anthropic's bundled office-skills toolchain (docx, pdf, xlsx, pptx) at runtime. These scripts live in session-scoped directories managed by Claude Code and **update automatically** with each Anthropic release — no manual syncing needed.

**Architecture:** Document Factory owns CREATION (python-docx, branded). Office Bridge adds VALIDATION, EDITING, and CONVERSION from Anthropic's toolchain.

```
Document Factory (create branded .docx)
    → office_bridge.validate()     — OOXML schema check before external send
    → office_bridge.unpack/pack()  — XML editing for tracked changes, comments
    → office_bridge.to_pdf()       — LibreOffice fallback when Word unavailable
    → office_bridge.fill_pdf()     — Permit form filling (RVO, gemeente)
```

## Quick Start

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

## Python API

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

## How it stays current

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

## Recommended workflow for external documents

```bash
# 1. Create branded .docx
python3 generate.py --profile agreement --entity nl --client "Arco Vreugdenhil" ...

# 2. Validate before sending
python3 office_bridge.py validate output.docx

# 3. Convert to PDF
python3 docx_to_pdf.py output.docx        # Word (preferred)
python3 office_bridge.py to-pdf output.docx  # LibreOffice (fallback)
```
