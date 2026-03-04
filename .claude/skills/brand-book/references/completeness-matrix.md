---
chunk_id: "completeness-matrix"
domain: "quality"
category: "scoring"
tags: ["completeness", "scoring", "thresholds", "quality-gate", "pre-flight"]
depends_on: ["intake-guide"]
token_count_approx: 1500
version: "1.0"
last_updated: "2026-02-21"
status: "active"
summary: >-
  Per-output-type scoring system. 10 output types (Figma, Tailwind, Remotion,
  Presentation, Document, DOCX, PDF, XLSX, HTML, Image) with minimum
  thresholds (50-80%), weighted token group requirements, and gap-impact
  assessments (blocking vs. degrading).
---

# Completeness Matrix

Scoring system for determining whether the brand-book has enough data to produce each output type. Used by agents before generating any visual deliverable.

## Per-Output-Type Scoring

Each output type has a minimum completeness threshold and weighted token group requirements.

### Figma UI Design

**Minimum threshold: 60%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors (primitives + semantic) | 30% | primary + secondary + neutral + feedback + surface + text | P1 |
| Typography (primitives + composites) | 25% | heading font, body font, size scale, weights, line-heights | P2 |
| Spacing (primitives + roles) | 15% | base unit, content gaps, layout margins, component padding | P3 |
| Components (buttons, cards, tables, callouts, badges) | 20% | button states, card variants, table styles, callout variants | P4 |
| Logo (specs + placement) | 10% | clear space, minimum size, placement rules | P6 |

### Claude Code HTML/React (Tailwind)

**Minimum threshold: 60%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors | 25% | primary + secondary + neutral + feedback | P1 |
| Typography | 25% | font families, size scale, weights, line-heights | P2 |
| Spacing | 20% | base unit, gap scale, padding scale | P3 |
| Tailwind config validity | 20% | All values valid Tailwind config entries | P1-P3 |
| Components | 10% | button styles, card styles | P4 |

### Remotion Video

**Minimum threshold: 70%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors | 20% | primary + secondary + neutral + surface + text | P1 |
| Typography | 20% | heading font, body font, display size, weights | P2 |
| Motion | 25% | durations, easing curves, transition type, animation personality | P5 |
| Video compositions | 25% | dimensions, fps, title card, lower third, text reveal | P5 |
| Logo | 10% | watermark variant, minimum size for video | P6 |

### Presentation (Slides)

**Minimum threshold: 70%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors | 20% | primary + secondary + neutral + surface + text + data viz | P1 |
| Typography | 20% | heading + body fonts, H1-H4 sizes, body sizes, caption | P2 |
| Slide masters | 25% | aspect ratio, grid, margins, alignment, cover layout | P3 |
| Components | 20% | header, footer, tables, metric cards, charts, progress indicator | P4 |
| Logo | 15% | placement, clear space, co-branding rules | P6 |

### Document (PDF/Print)

**Minimum threshold: 60%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors | 15% | primary + neutral + text + surface | P1 |
| Typography | 25% | heading + body fonts, full size scale, weights, line-heights | P2 |
| Document masters | 30% | cover page, content page, table page, appendix | P3 |
| Components | 15% | tables, callouts, headers, footers, citation format | P4 |
| Logo | 15% | placement, clear space, minimum print size | P6 |

### DOCX (Word Document)

**Minimum threshold: 60%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors | 15% | primary + secondary + neutral + feedback | P1 |
| Typography | 25% | heading + body + mono fonts, full size scale, weights | P2 |
| Document masters | 25% | cover page, margins, headers/footers, page breaks | P3 |
| Components | 20% | table styles, callout styles, badge styles, metric cards | P4 |
| Logo | 15% | clear space, minimum size, placement rules | P6 |

### PDF (Generated)

**Minimum threshold: 60%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors | 15% | primary + secondary + neutral + text + surface | P1 |
| Typography | 25% | heading + body fonts, full size scale, weights, line-heights | P2 |
| Document masters | 25% | cover page, content layout, margins, page sizes | P3 |
| Components | 15% | tables, callouts, headers, footers, charts | P4 |
| Logo | 10% | placement, clear space, minimum print size | P6 |
| Print/a11y | 10% | color space guidance, PDF/UA tagging | P3 |

### XLSX/CSV (Spreadsheet)

**Minimum threshold: 50%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors | 25% | primary + secondary + neutral + feedback + data series | P1 |
| Typography | 25% | heading + body + mono fonts, sizes for header/body/data | P2 |
| Components | 30% | table header, alternating rows, conditional formatting, chart | P4 |
| Cover sheet | 10% | brand name, accent color, metadata fields | P1-P3 |
| Logo | 10% | logo for cover sheet embedding | P6 |

### HTML Design System

**Minimum threshold: 80%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors (primitives + semantic + audience) | 20% | All 8 primitive hues, semantic mappings, audience accents, data viz palette | P1 |
| Typography (primitives + composites) | 15% | heading + body + mono fonts, full size scale, weights, line-heights | P2 |
| Spacing + Elevation + Breakpoints | 15% | base unit, spacing scale, z-index stack, 4 breakpoints, elevation philosophy | P3 |
| Components (all 13) | 25% | buttons, inputs, cards, tables, callouts, badges, modals, toasts, tooltips, toggles, skeleton, dividers, charts | P4 |
| Motion | 5% | durations, easing curves | P5 |
| Logo | 10% | logo files (SVG/PNG), clear space, variants, placement | P6 |
| Photography/imagery | 10% | image style, treatment, icon style | P7 |

### Image (Social Cards, Banners, Icons)

**Minimum threshold: 50%**

| Token Group | Weight | Tokens Required | Phase Source |
|---|---|---|---|
| Colors | 25% | primary + secondary + surface + text on brand | P1 |
| Typography | 20% | heading + body fonts, display/hero sizes, weights | P2 |
| Layout | 10% | margins, safe zones, spacing | P3 |
| Components | 10% | badge styles, accent bar styling | P4 |
| Logo | 20% | logo files, clear space, minimum size, color variants | P6 |
| Photography/imagery | 15% | image treatment, overlay opacity, background patterns | P7 |

---

## Threshold Definitions

| Score | Quality Level | What It Means |
|---|---|---|
| **100%** | Pixel-precise | All tokens specified. Agent produces exact-match output every run. |
| **80-99%** | Production-quality | Core complete. Minor gaps use sensible defaults derived from specified tokens. |
| **60-79%** | Usable | Major groups complete. Agent can produce output with clearly marked default areas. Review recommended. |
| **40-59%** | Draft-quality | Significant gaps. Output has placeholder decisions that need human review. |
| **<40%** | Insufficient | Do not generate output. Run more intake phases first. |

---

## Phase-to-Completeness Mapping

Shows which phases are needed to reach each threshold per output type.

| Output Type | Phase 0-1 only | + Phase 2 | + Phase 3 | + Phase 4 | + Phase 5 | + Phase 6 | + Phase 7 |
|---|---|---|---|---|---|---|---|
| **Figma UI** | 30% | 55% | 70% | 90% | 90% | 100% | 100% |
| **Claude Code** | 25% | 50% | 70% | 80% | 80% | 80% | 80% |
| **Remotion Video** | 20% | 40% | 40% | 40% | 90% | 100% | 100% |
| **Presentation** | 20% | 40% | 65% | 85% | 85% | 100% | 100% |
| **Document** | 15% | 40% | 70% | 85% | 85% | 100% | 100% |
| **DOCX** | 15% | 40% | 70% | 85% | 85% | 100% | 100% |
| **PDF** | 15% | 40% | 70% | 85% | 85% | 100% | 100% |
| **XLSX/CSV** | 20% | 45% | 60% | 80% | 80% | 80% | 80% |
| **Image** | 20% | 50% | 55% | 60% | 60% | 85% | 100% |
| **HTML Design System** | 20% | 35% | 50% | 75% | 80% | 90% | 100% |

**Key insight:** Phase 0-2 (identity + colors + typography) gets you to 40-55% for most outputs. Adding Phase 3 (layout) pushes to 65-70% -- enough to start generating usable presentations and documents. Image output depends heavily on Phase 6 (logo) and Phase 7 (photography).

---

## Gap Impact Assessment

For each token group, defines what happens when it's missing.

### Blocking Gaps (output cannot be generated)

| Gap | Affected Outputs | Minimum to Unblock |
|---|---|---|
| No primary color | All | At least Q1.1 answered |
| No heading font | All | At least Q2.1 answered |
| No slide aspect ratio | Presentation, Video | At least Q3.3 answered |
| No motion tokens | Video | At least Q5.1 + Q5.2 answered |

### Degrading Gaps (output works but quality suffers)

| Gap | Affected Outputs | What Degrades | Fallback |
|---|---|---|---|
| No secondary color | All | No visual hierarchy for CTAs/accents | Use primary at lighter shade |
| No monospace font | Figma, Presentation | Number alignment in data tables | Use body font |
| No audience accents | Presentation, Document | No per-audience visual adaptation | Use primary palette for all |
| No dark mode tokens | Presentation, Video | No dark background sections | Skip dark sections |
| No motion easing curves | Video | Animations feel mechanical | Use CSS `ease` default |
| No logo specs | All | Inconsistent logo treatment | Place logo top-left, estimate clear space |
| No photography style | Presentation, Document | Inconsistent image selection | Use no imagery or stock-neutral |
| No chart styling | Presentation, Figma | Charts don't match brand | Use minimal chart defaults |

---

## Pre-Flight Checklists per Deliverable

### Before Generating a Presentation
- [ ] Brand config loaded
- [ ] Primary + secondary + neutral colors defined
- [ ] Heading + body fonts defined
- [ ] Slide aspect ratio set (Q3.3)
- [ ] Layout alignment set (Q3.1)
- [ ] White space level set (Q3.2)
- [ ] Logo placement defined (Q4.3)
- [ ] Completeness ≥ 70%

### Before Generating a Document
- [ ] Brand config loaded
- [ ] Primary + neutral colors defined
- [ ] Full typography scale defined (heading, body, caption, footnote)
- [ ] Cover page style set (Q3.8)
- [ ] Table styling set (Q3.6)
- [ ] Source citation format set (Q4.5)
- [ ] Completeness ≥ 60%

### Before Generating Figma Variables
- [ ] Brand config loaded
- [ ] All 8 primitive color hues defined (or subset per Q1.6)
- [ ] Typography primitives complete
- [ ] Spacing primitives complete
- [ ] Completeness ≥ 60%

### Before Generating Tailwind Config
- [ ] Brand config loaded
- [ ] All color tokens have valid hex values
- [ ] Font families are Google Fonts or have fallbacks
- [ ] Spacing scale is internally consistent (harmonic)
- [ ] Completeness ≥ 60%

### Before Generating Remotion Theme
- [ ] Brand config loaded
- [ ] Video format(s) specified (Q5.3)
- [ ] Frame rate set (Q5.4)
- [ ] Animation personality set (Q5.2)
- [ ] All color values JSON-serializable
- [ ] Font files available for bundling
- [ ] Completeness ≥ 70%

### Before Generating HTML Design System
- [ ] Brand config loaded
- [ ] All 8 primitive color hues defined
- [ ] Full typography scale (heading, body, mono) defined
- [ ] All 13 component token groups populated
- [ ] Elevation z-index stack defined (Q3.12)
- [ ] Breakpoints defined (Q3.11)
- [ ] Dark mode tokens defined (Q1.9)
- [ ] Logo files available (SVG or PNG for base64 encoding)
- [ ] CSS variables file generated
- [ ] Completeness >= 80%

### Before Generating CSS Variables
- [ ] Brand config loaded
- [ ] All semantic tokens have resolved primitive references
- [ ] No circular references
- [ ] All values valid CSS
- [ ] Completeness ≥ 60%

---

## Scoring Calculation

For any output type, the completeness score is:

```
score = Σ (token_group_weight × group_completeness)
```

Where `group_completeness` for each token group is:

```
group_completeness = tokens_with_values / total_tokens_required × 100
```

A token "has a value" if:
1. It has a `$value` field in the token file, AND
2. The value is not `null`, `""`, or `"TODO"`, AND
3. If it references another token, that reference resolves to a concrete value
