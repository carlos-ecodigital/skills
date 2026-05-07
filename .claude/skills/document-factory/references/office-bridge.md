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
| Accept tracked changes (LibreOffice) | docx | `accept_changes()` |
| .docx → PDF (Word, canonical) | — | `to_pdf_word()` (uses local docx2pdf) |
| .docx → PDF (LibreOffice, headless) | docx | `to_pdf_libreoffice()` |
| .docx → PDF (auto-fallback) | both | `to_pdf(prefer="word"\|"libreoffice")` |
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
| Branded .docx creation | `document_factory.py` | python-docx, DE brand, 5 profiles |
| Accept tracked changes (Word path) | `accept_changes.py` | Now delegates: `--engine word\|libreoffice` (default LibreOffice on macOS) |
| Visual regression QA | `tools/visual_qa.py` | docx → pdf → pHash → HTML report |

## Engine selection — Word vs LibreOffice

**Word (canonical, slower, fragile):**
- Higher fidelity for final user-facing output (kerning, font rendering, complex tables)
- On macOS uses AppleScript — hangs if Word has open docs or modal dialogs
- Use when shipping the final PDF to a client or counsel

**LibreOffice (reliable, fast, headless):**
- Session-independent — no dependency on Word state
- Used by `tools/visual_qa.py` pipeline (must be deterministic)
- Default for batch/CI work
- Acceptance semantics may diverge slightly from Word (rare; tested on real docs)

`bridge.to_pdf(prefer="word")` (default) tries Word first, automatically falls back to LibreOffice if Word fails. `bridge.to_pdf(prefer="libreoffice")` skips Word entirely.

## Out-of-scope wrappers (deliberately not implemented)

The bridge does NOT expose these even though Anthropic provides them, because document-factory's domain is .docx creation only:

| Anthropic provides | Why not in bridge |
|---|---|
| `pptx/scripts/thumbnail.py` (deck previews) | Belongs in `collateral-studio` — that skill creates .pptx |
| `pptx/scripts/add_slide.py` | Deck assembly is `collateral-studio`'s job |
| `xlsx/scripts/office/unpack.py` + `pack.py` | Spreadsheet editing is `financial-model-interpreter`'s job |
| `pdf/scripts/fill_pdf_form_with_annotations.py` | Permit forms are `permit-drafter`'s job |

If those skills need bridge access, they should add a thin wrapper or use a shared `_shared/office_bridge.py`. We don't pre-build wrappers nobody calls.

## Recommended workflow for external documents

```bash
# 1. Create branded .docx
python3 document_factory.py --profile agreement --entity nl --client "Arco Vreugdenhil" ...

# 2. Validate before sending
python3 office_bridge.py validate output.docx

# 3. Convert to PDF (auto-fallback)
python3 -c "from office_bridge import OfficeBridge; OfficeBridge().to_pdf('output.docx')"

# 4. If counsel returns a redlined version, accept the changes
python3 accept_changes.py output_redlined.docx -o output_clean.docx
# (uses LibreOffice on macOS; --engine word for canonical Word semantics)
```
