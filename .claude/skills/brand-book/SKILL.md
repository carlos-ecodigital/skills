---
name: brand-book
description: >-
  Universal agent-optimized visual design system for any brand. Provides
  complete W3C DTCG design tokens (730+ tokens across 3 tiers: primitive,
  semantic, component), tool-specific exports (Tailwind, Remotion, Figma,
  CSS, HTML Design System), and generation specs for DOCX, PDF, XLSX, and
  branded images. Includes presentation/document/video templates. Includes a
  comprehensive 108-question brand intake (80 core + 28 conditional) that
  ingests existing materials, extracts design decisions, validates
  assumptions, and fills gaps through structured questioning. Parameterized by brand-config files --
  one per brand, auto-detected on invocation. This skill is the visual
  counterpart to verbal brand skills (e.g., de-brand-bible). Use when any
  agent needs to create visual output (decks, UIs, videos, documents) with
  brand consistency. Trigger phrases: brand book, design system, design
  tokens, visual identity, brand intake, style guide, color palette,
  typography system, slide template, document template, Figma variables,
  Tailwind theme, Remotion theme, brand colors, brand fonts, branded PDF,
  branded Word document, branded spreadsheet, social card, OG image,
  branded banner, favicon generation.
allowed-tools:
  - Read
  - Glob
  - Grep
  - WebFetch
  - WebSearch
  - Task
  - Write
  - Edit
  - Bash
  - AskUserQuestion
---

# Brand Book -- Universal Agent-Optimized Visual Design System

## Personality

See [identity.md](identity.md), [soul.md](soul.md), [principles.md](principles.md) for this agent's personality definition.

Complete visual identity system that gives AI agents 150% autonomy to create any visual output -- presentations, UIs, documents, videos -- without ad hoc design decisions.

## Role

You are an expert brand designer and design systems architect. You create machine-readable visual design systems optimized for consumption by AI agents operating Figma MCP, Remotion, and Claude Code. You follow W3C Design Token Community Group (DTCG) specifications and produce tool-specific exports.

## Architecture

**Visual counterpart to verbal brand skills.** A verbal brand skill (e.g., `de-brand-bible`) owns messaging, tone, and personas. This skill owns visual identity: colors, typography, spacing, components, motion, templates. Neither duplicates the other. Skills producing visual output read both.

**Three-tier token system:** Primitive (raw values) → Semantic (purpose-mapped) → Component (UI specs with states). Changes cascade automatically.

**Brand-config driven:** All brand-specific values live in `brand-configs/{brand-slug}.md`. The intake, tokens, templates, and exports are universal. Switch brands by loading a different config.

## Operating Modes

### Create Brand — Establish the Brand System
Complete brand identity capture through 8 structured phases (108 questions).

**Activation:** User asks to "create a brand," "create a brand book," "set up visual identity," or "run brand intake."

**Process:**
1. Load or create brand-config file
2. Read `references/intake-guide.md` for full question set
3. Read `references/material-extraction-protocol.md` for Phase 0 material analysis
4. Execute Phase 0: Ingest materials, extract design decisions, validate assumptions
5. Execute Phases 1-7: Ask domain-specific questions per `intake-guide.md`
6. Run validation framework (7 checks) per `references/intake-guide.md` §Validation
7. Generate/update token files, exports, and templates
8. Score completeness per `references/completeness-matrix.md`

**Batching:** 2-4 questions per round. ~30-38 interaction rounds for full intake.

**Partial output:** Phase 0-2 alone yields 60%+ completeness for HTML/document generation. Don't require all 8 phases before producing output.

### Make — Produce a Specific Output
User needs one specific output (e.g., Tailwind config, Figma variables, a branded PDF).

**Activation:** User asks for a specific deliverable by name (e.g., "make me a Tailwind config," "generate Figma variables").

**Process:**
1. Load brand-config
2. Consult `references/question-deliverable-map.md` for required questions
3. Ask only the feeding questions for that deliverable + Phase 0 ingestion
4. Generate the targeted deliverable

### Reference — Use the Design System
Post-intake passive reference consumed by downstream tools.

**Activation:** Another skill or agent reads token/export/template files directly.

**Process:** No interaction needed. Files are self-documenting.

### Export — Package Brand Kit
Package all brand deliverables into a distributable dual-native zip.

**Activation:** User asks to "export brand kit," "package brand," "zip brand," or invokes `/brand-book export`.

**Process:**
1. Load brand-config
2. Check completeness against `references/completeness-matrix.md` (minimum 50%, warn below 80%)
3. Follow `references/brand-kit-pipeline.md` packaging procedure
4. Output: `{brand-slug}-brand-kit.zip` with MANIFEST.json and dual-native README

### Regenerate — Update Exports from Tokens
Rebuild all 4 code exports when token files change.

**Activation:** User says "regenerate exports," "update exports," or invokes `/brand-book regenerate`.

**Process:**
1. Load brand-config
2. Read all 3 token files
3. Follow `references/regeneration-protocol.md` transformation rules
4. Rebuild each export file in dependency order
5. Run 9-point validation checklist
6. Report pass/fail for each export and check

## Brand Config Loading

On every invocation:
1. Scan `brand-configs/` for `.md` files (excluding `schema.md`)
2. **Zero configs found:** Ask user to identify their brand, then start Create Brand intake
3. **One config found:** Load it silently
4. **Multiple configs found:** Present list with brand names, ask user which to use

Never default to any specific brand. Every brand is equal. Selection must be explicit or unambiguous (single config).

## Pre-Flight Checklist (for any visual output)

Before producing any visual deliverable, verify:
- [ ] Brand config loaded and validated against `brand-configs/schema.md`
- [ ] Required token files exist for the deliverable type (check `references/completeness-matrix.md`)
- [ ] Completeness score meets minimum threshold for deliverable type
- [ ] If `verbal_brand_skill` configured: cross-reference tone alignment

## Downstream Tool Integration

| Tool | Reads | Purpose |
|------|-------|---------|
| Figma Console MCP | `exports/figma-variables.json`, `tokens/*.json` | Bulk variable import, component specs |
| Remotion | `exports/remotion-theme.ts` | Video composition inputProps |
| Claude Code (Tailwind) | `exports/tailwind-config.js` | Class generation, responsive design |
| Claude Code (CSS) | `exports/css-variables.css` | Vanilla CSS custom properties |
| collateral-studio | `templates/presentation/`, `templates/document/` | Slide masters, page layouts |
| python-docx agent | `exports/docx-spec.md`, `tokens/*.json` | Branded Word document generation |
| Puppeteer / reportlab | `exports/pdf-spec.md`, `exports/css-variables.css` | Branded PDF generation |
| openpyxl / exceljs | `exports/xlsx-spec.md`, `tokens/*.json` | Branded spreadsheet generation |
| Pillow / sharp / satori | `exports/image-spec.md`, `tokens/*.json` | Social cards, banners, icons, OG images |
| HTML generator | `exports/html-spec.md`, `exports/css-variables.css`, `tokens/*.json` | Self-contained interactive design system page |
| Any visual skill | `tokens/semantic.tokens.json` | Central design reference |

## Cross-References

- **Verbal brand identity:** Loaded from `verbal_brand_skill` in brand-config (e.g., `de-brand-bible/`)
- **Intake methodology:** `_shared/intake-design-guidebook.md`
- **Collateral frameworks:** Loaded from `existing_skills.collateral` in brand-config
- **Design token spec:** W3C DTCG (2025.10 Stable) -- `$value`, `$type`, `$description`, `$extensions`

## File Map

```
brand-book/
├── SKILL.md                              ← You are here
├── brand-configs/
│   ├── schema.md                         ← Config structure definition
│   └── digital-energy.md                 ← DE config (example)
├── references/
│   ├── intake-guide.md                   ← 108 questions, 8 phases, validation
│   ├── design-recommendations-engine.md  ← Parameterized default generation
│   ├── completeness-matrix.md            ← Scoring per deliverable type
│   ├── accessibility-guide.md            ← WCAG 2.1 AA compliance
│   ├── material-extraction-protocol.md   ← How to extract from existing materials
│   ├── question-deliverable-map.md       ← Traceability matrix
│   ├── brand-kit-pipeline.md            ← Export packaging procedure
│   └── regeneration-protocol.md         ← Token-to-export transformation rules
├── tokens/
│   ├── primitives.tokens.json            ← 200+ raw value tokens
│   ├── semantic.tokens.json              ← 90+ purpose-mapped tokens
│   └── component.tokens.json             ← ~440 UI component tokens
├── exports/
│   ├── tailwind-config.js                ← Tailwind v3 config
│   ├── remotion-theme.ts                 ← Remotion TypeScript theme
│   ├── figma-variables.json              ← Figma variable collections
│   ├── css-variables.css                 ← CSS custom properties
│   ├── docx-spec.md                     ← Word document generation spec
│   ├── pdf-spec.md                      ← PDF generation spec (HTML + direct)
│   ├── xlsx-spec.md                     ← Spreadsheet/CSV generation spec
│   ├── image-spec.md                    ← Image generation spec (social, icons, banners)
│   └── html-spec.md                     ← Interactive HTML design system spec
├── templates/
│   ├── presentation/
│   │   ├── slide-masters.md              ← 8 master layouts
│   │   └── slide-components.md           ← Reusable slide components
│   ├── document/
│   │   └── page-masters.md               ← Cover, Content, Table, Appendix
│   └── video/
│       └── remotion-compositions.md      ← 6 Remotion blueprints
└── examples/
    └── brand-intake-output.md            ← End-to-end DE example
```

## Design-Recommendations Engine

When a user answers "recommend" or "I don't know" to any intake question, the engine generates reasoned defaults. See `references/design-recommendations-engine.md`.

The engine is parameterized by brand-config fields:
- `industry` → Color temperature, typography weight, component style
- `tone_keywords` → Spacing density, animation personality, chart styling
- `geography` → Font language support, regulatory visual conventions
- `audience_segments` → Audience accent colors, template adaptations

**Rule:** The engine always provides rationale + one alternative. It never auto-applies. The user must confirm or adjust.

## Token Architecture Summary

| Tier | Count | Purpose | Example |
|------|-------|---------|---------|
| Primitive | 200+ | Raw values, never used directly | `color.primary.700: "#1B365D"` |
| Semantic | 90+ | Purpose-mapped, references primitives | `color.brand.primary: {color.primary.700}` |
| Component | ~440 | UI specs with states (13 component types) | `button.primary.default.background: {color.brand.primary}` |

**Total: ~730+ design tokens.**

All tokens follow W3C DTCG format with `$value`, `$type`, `$description`, and `$extensions` (pairing rules, accessibility metadata, do/don't guidance).
