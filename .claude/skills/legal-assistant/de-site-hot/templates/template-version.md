# HoT Grower Template — Version Tracking

| Version | Date | Body Hash | Annex Hash | Changes | Approved By |
|---------|------|-----------|------------|---------|-------------|
| 1.0 | 2026-03-13 | — | — | Initial version: body v1 + annex A v1 | Jelmer (pending) |

## Current Active Version: **1.0**

### Files
- **Body:** `hot-grower-body-v1.docx` — LOCKED, bilingual EN/NL, 9 sections, ~35 clauses
- **Annex A:** `hot-grower-annex-a-v1.docx` — 48 input fields (35 required, 13 conditional)

### Rules
1. The body template is **never modified** by the `hot-intake` skill
2. Only Annex A input fields (yellow/green highlighted cells) are populated
3. Any body update requires legal review and a new version entry here
4. The `hot-intake` skill checks this file at startup to ensure correct template version
