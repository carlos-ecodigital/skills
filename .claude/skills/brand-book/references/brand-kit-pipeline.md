---
chunk_id: "brand-kit-pipeline"
domain: "export"
category: "packaging"
tags: ["export", "zip", "brand-kit", "dual-native", "packaging", "delivery"]
depends_on: ["completeness-matrix"]
token_count_approx: 1800
version: "1.0"
last_updated: "2026-02-21"
status: "active"
summary: >-
  Step-by-step procedure for packaging all brand deliverables into a
  portable, dual-native zip. Defines kit structure, MANIFEST.json schema,
  README template (human quickstart + agent API), and error handling.
  Agent follows this procedure using Read, Write, and Bash tools.
---

# Brand Kit Export Pipeline

## Activation

**Triggers:** User asks to "export brand kit," "package brand," "zip brand," or invokes `/brand-book export`.

**Pre-conditions:**
1. Brand config loaded (scan `brand-configs/` per Brand Config Loading rules)
2. Completeness score calculated per `completeness-matrix.md`
   - **≥ 80%:** Full kit. Proceed without warning.
   - **50–79%:** Partial kit. Warn user: "Brand completeness is {N}%. Some exports may have placeholder values. Proceed?"
   - **< 50%:** Block. "Brand completeness is {N}%, below the 50% minimum for export. Run `/brand-book` to complete more intake phases first."

---

## Kit Structure

```
{brand-slug}-brand-kit/
├── README.md                              ← Dual-native: human quickstart + agent API reference
├── MANIFEST.json                          ← File inventory, checksums, generation metadata
│
├── config/
│   └── {brand-slug}.md                    ← Brand config (all resolved fields)
│
├── tokens/
│   ├── primitives.tokens.json             ← Tier 1: raw values (colors, fonts, spacing, motion)
│   ├── semantic.tokens.json               ← Tier 2: purpose-mapped tokens (roles, modes, composites)
│   └── component.tokens.json              ← Tier 3: UI component specs (buttons, cards, inputs)
│
├── exports/
│   ├── tailwind-config.js                 ← Tailwind v3 theme extension
│   ├── css-variables.css                  ← CSS custom properties (:root block)
│   ├── figma-variables.json               ← Figma variable collections (3 collections)
│   ├── remotion-theme.ts                  ← Remotion TypeScript theme + interfaces
│   └── specs/
│       ├── docx-spec.md                   ← Word document generation spec
│       ├── pdf-spec.md                    ← PDF generation spec
│       ├── xlsx-spec.md                   ← Spreadsheet generation spec
│       ├── image-spec.md                  ← Image generation spec
│       └── html-spec.md                   ← Interactive HTML design system spec
│
├── templates/
│   ├── slide-masters.md                   ← 8 presentation master layouts
│   ├── slide-components.md                ← Reusable slide components
│   ├── page-masters.md                    ← 7 document page templates
│   └── remotion-compositions.md           ← 6 video composition blueprints
│
└── references/
    └── accessibility-guide.md             ← WCAG 2.1 AA compliance checklist
```

**Excluded from kit** (internal-only methodology docs):
- `intake-guide.md` — intake questions are internal process, not deliverable
- `design-recommendations-engine.md` — internal decision logic
- `material-extraction-protocol.md` — internal extraction process
- `question-deliverable-map.md` — internal traceability
- `completeness-matrix.md` — internal scoring
- `brand-kit-pipeline.md` — this file (meta-procedure)
- `regeneration-protocol.md` — internal regeneration logic

---

## MANIFEST.json Schema

```json
{
  "brand_name": "Digital Energy",
  "brand_slug": "digital-energy",
  "generated_at": "2026-02-21T14:30:00Z",
  "generator": "brand-book-skill v1.0",
  "completeness_score": 65,
  "token_counts": {
    "primitives": 200,
    "semantic": 90,
    "component": 440
  },
  "files": [
    {
      "path": "tokens/primitives.tokens.json",
      "size_bytes": 98304,
      "sha256": "abc123...",
      "description": "Tier 1 raw value tokens: 8 color families, typography, spacing, motion"
    }
  ],
  "gaps": [
    "Phase 5 (motion/video) incomplete",
    "Phase 7 (photography/patterns) incomplete"
  ]
}
```

**Field definitions:**
- `brand_name` / `brand_slug`: from brand-config
- `generated_at`: ISO 8601 UTC timestamp at time of packaging
- `generator`: fixed string identifying the producing skill and version
- `completeness_score`: integer 0-100 from completeness-matrix calculation
- `token_counts`: count of top-level token entries per tier file
- `files[]`: one entry per file in the kit
  - `path`: relative to kit root
  - `size_bytes`: from `wc -c` via Bash
  - `sha256`: from `shasum -a 256` via Bash
  - `description`: human-readable purpose (one line)
- `gaps[]`: string array of known incomplete areas (from completeness-matrix)

---

## Agent Procedure

Follow these steps exactly. Use Bash for file operations, Write for generated files.

### Step 1: Validate Pre-Conditions

1. Confirm brand config is loaded (brand_name and brand_slug populated)
2. Calculate completeness score per `completeness-matrix.md`
3. Apply threshold check (block < 50%, warn 50-79%, proceed ≥ 80%)

### Step 2: Create Temp Directory

```bash
BRAND_SLUG="digital-energy"  # from config
KIT_DIR=$(mktemp -d /tmp/brand-kit-XXXXXX)
KIT_NAME="${BRAND_SLUG}-brand-kit"
mkdir -p "${KIT_DIR}/${KIT_NAME}"/{config,tokens,exports/specs,templates,references}
```

### Step 3: Copy Source Files

```bash
SKILL_DIR="/path/to/skills/brand-book"

# Tokens
cp "${SKILL_DIR}/tokens/"*.json "${KIT_DIR}/${KIT_NAME}/tokens/"

# Code exports
cp "${SKILL_DIR}/exports/tailwind-config.js" "${KIT_DIR}/${KIT_NAME}/exports/"
cp "${SKILL_DIR}/exports/css-variables.css" "${KIT_DIR}/${KIT_NAME}/exports/"
cp "${SKILL_DIR}/exports/figma-variables.json" "${KIT_DIR}/${KIT_NAME}/exports/"
cp "${SKILL_DIR}/exports/remotion-theme.ts" "${KIT_DIR}/${KIT_NAME}/exports/"

# Spec exports
cp "${SKILL_DIR}/exports/"*-spec.md "${KIT_DIR}/${KIT_NAME}/exports/specs/"

# Templates (flatten from subdirectories)
cp "${SKILL_DIR}/templates/presentation/"*.md "${KIT_DIR}/${KIT_NAME}/templates/"
cp "${SKILL_DIR}/templates/document/"*.md "${KIT_DIR}/${KIT_NAME}/templates/"
cp "${SKILL_DIR}/templates/video/"*.md "${KIT_DIR}/${KIT_NAME}/templates/"

# Config
cp "${SKILL_DIR}/brand-configs/${BRAND_SLUG}.md" "${KIT_DIR}/${KIT_NAME}/config/"

# References (accessibility only)
cp "${SKILL_DIR}/references/accessibility-guide.md" "${KIT_DIR}/${KIT_NAME}/references/"
```

### Step 4: Generate MANIFEST.json

1. For each file in the kit directory, run:
   ```bash
   wc -c < "${file_path}"          # size_bytes
   shasum -a 256 "${file_path}"    # sha256 (take first field)
   ```
2. Count top-level tokens in each JSON file (count keys at depth 1 inside the root object)
3. Assemble the JSON structure per schema above
4. Write to `${KIT_DIR}/${KIT_NAME}/MANIFEST.json` using Write tool

### Step 5: Generate README.md

Use the dual-native template below. Replace all `{placeholders}` with actual values from brand-config and MANIFEST.

Write to `${KIT_DIR}/${KIT_NAME}/README.md` using Write tool.

### Step 6: Create Zip

```bash
cd "${KIT_DIR}" && zip -r "${KIT_NAME}.zip" "${KIT_NAME}/"
```

### Step 7: Deliver

Move the zip to the user's current working directory (or ask for destination):

```bash
mv "${KIT_DIR}/${KIT_NAME}.zip" "/path/to/destination/"
```

Report to user: "Brand kit exported: `{brand-slug}-brand-kit.zip` ({N} files, {size} KB, completeness {score}%)"

### Step 8: Cleanup

```bash
rm -rf "${KIT_DIR}"
```

---

## Dual-Native README Template

```markdown
# {Brand Name} Brand Kit

Generated: {date} | Completeness: {score}% | Generator: brand-book-skill v1.0

---

## For Humans

### What's Inside
This kit contains the complete visual identity system for {Brand Name}:
- **Design tokens** — every color, font, spacing, and component value in the system
- **Code exports** — ready-to-use files for Tailwind, CSS, Figma, and Remotion
- **Generation specs** — instructions for creating Word docs, PDFs, spreadsheets, images, and HTML
- **Templates** — master layouts for presentations, documents, and videos
- **Accessibility guide** — WCAG 2.1 AA compliance rules for this brand's palette

### Quick Start
| Tool | File | How to Use |
|------|------|-----------|
| Tailwind | `exports/tailwind-config.js` | `require('./exports/tailwind-config')` in your tailwind.config.js `extend` |
| CSS | `exports/css-variables.css` | `<link>` or `@import` into your stylesheet |
| Figma | `exports/figma-variables.json` | Import via Figma Variables panel |
| Remotion | `exports/remotion-theme.ts` | `import { brandTheme } from './exports/remotion-theme'` |

### Brand at a Glance
| Property | Value |
|----------|-------|
| Primary Color | {resolved_primary_color} |
| Secondary Color | {resolved_secondary_color} |
| Heading Font | {resolved_heading_font} |
| Body Font | {resolved_body_font} |
| Mono Font | {resolved_mono_font} |

---

## For Agents

### Token System
Three-tier W3C DTCG token architecture:

| Tier | File | Count | Purpose |
|------|------|-------|---------|
| Primitives | `tokens/primitives.tokens.json` | {N} | Raw values: hex colors, px sizes, font names |
| Semantic | `tokens/semantic.tokens.json` | {N} | Purpose-mapped: brand.primary, surface.default, text.heading |
| Component | `tokens/component.tokens.json` | {N} | UI specs: button.primary.hover.background, card.default.shadow |

### Reference Resolution
Tokens use `$value` references in `{group.path}` format:
- Literal values: `"$value": "#1B365D"` — use directly
- References: `"$value": "{color.primary.700}"` — resolve through primitives
- Max reference depth: 3

### Reading Component Tokens
Component tokens follow: `{component}.{variant}.{state}.{property}`
- Example: `button.primary.hover.background` → resolved hex for primary button hover state
- States: `default`, `hover`, `active`, `disabled`, `focus`
- Properties: `background`, `text`, `border`, `border-width`, `border-radius`, `padding-x`, `padding-y`, `shadow`

### Completeness
Score: {score}%
Gaps: {gaps list or "None — full coverage"}

### Config Reference
Brand config at `config/{brand-slug}.md` contains:
- `audience_segments[]` — target personas with IDs for audience-specific tokens
- `tone_keywords[]` — brand voice adjectives
- `resolved_personality` — 5-axis personality scores driving design defaults
- `resolved_emotional_response[]` — target emotional reactions
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Source file missing | Skip file, add entry to MANIFEST `gaps[]`, log warning to user |
| Completeness < 50% | Block export, explain which phases need completion |
| Completeness 50-79% | Warn user, list specific gaps, ask for confirmation to proceed |
| `shasum` not available | Fall back to `md5` or skip checksums, note in MANIFEST |
| `zip` command fails | Try `tar -czf` as fallback, adjust filename to `.tar.gz` |
| Destination not writable | Ask user for alternative path |
| Token file malformed | Skip that tier's JSON, note in MANIFEST gaps, proceed with remaining |
