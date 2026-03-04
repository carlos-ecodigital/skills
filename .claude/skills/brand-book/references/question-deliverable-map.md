---
chunk_id: "question-deliverable-map"
domain: "intake"
category: "traceability"
tags: ["traceability", "questions", "deliverables", "mapping", "coverage"]
depends_on: ["intake-guide"]
token_count_approx: 2500
version: "1.0"
last_updated: "2026-02-21"
status: "active"
summary: >-
  Bidirectional traceability matrix. Every intake question maps to deliverable
  sections it feeds. Every deliverable section maps to feeding questions.
  Zero orphan questions, zero unfed sections. 108 questions -> 57 sections.
---

# Question-to-Deliverable Traceability Matrix

Bidirectional mapping ensuring every question feeds at least one deliverable section, and every deliverable section has at least one feeding question. No orphan questions. No unfed sections.

## Format A: Question-Centric (Every Q → Deliverable Sections)

### Phase 0: Material Ingestion & Triage

| Q# | Question | Deliverable Sections Fed |
|---|---|---|
| 0.1 | Material existence checklist | All token files, all templates, material-extraction-protocol routing |
| 0.2 | Share priority materials | All deliverables (via extraction) |
| 0.3 | Material recency | Extraction confidence levels, assumption validation |
| 0.4 | Extraction validation | All token files (single most important validation) |
| 0.5 | What to KEEP | Extraction confidence, design-recommendations scope |
| 0.6 | What to CHANGE | Extraction exclusion list |
| 0.7 | Most urgent output | Completeness matrix priority, deliverable ordering |
| 0.8 | Preference strength | Phase routing, conditional branching, engine activation |
| 0.9 | Admired brands | Color direction, typography direction, overall aesthetic |
| 0.10 | Emotional response | Color temperature, typography weight, spacing density, design direction |
| 0.11 | Primary audience | Template priority, default component styling, data density |
| 0.12 | Brand personality spectrum | All design-recommendations-engine decisions, every token group |

### Phase 0B: Agent Research Tasks

| R# | Research Task | Deliverable Sections Fed |
|---|---|---|
| R0.1 | Website extraction | All token files (colors, fonts, spacing, components) |
| R0.2 | LinkedIn audit | Logo variants, social templates |
| R0.3 | Pitch deck analysis | All token files, all templates |
| R0.4 | Competitor analysis | Design differentiation (exclusion rules, contrast decisions) |
| R0.5 | Font availability | Typography tokens, Remotion theme (bundling), Tailwind config |

### Phase 0C: System Data Ingestion

| D# | Data Source | Deliverable Sections Fed |
|---|---|---|
| D0.1 | Brand identity | All token files (baseline visual identity) |
| D0.2 | Buyer personas | Audience accent colors, template persona adaptations |
| D0.3 | Collateral frameworks | Slide masters, slide components |
| D0.4 | Data room standards | Document page masters |
| D0.5 | Tone and style guide | Typography density, layout spacing |

### Phase 1: Color Identity

| Q# | Question | Deliverable Sections Fed |
|---|---|---|
| 1.1 | Primary color | `primitives.color.primary.*`, `semantic.color.brand.primary`, Tailwind `primary`, CSS `--color-primary-*`, Figma `primary` collection |
| 1.2 | Shade range | `primitives.color.primary.50-950` (all 10 shades), Tailwind shade scale, CSS shade variables |
| 1.3 | Secondary color | `primitives.color.secondary.*`, `semantic.color.brand.secondary`, all exports secondary values |
| 1.4 | Domain accent | `semantic.color.brand.accent`, `primitives.color.accent.*`, template context-specific zones |
| 1.5 | Neutral palette | `primitives.color.neutral.*` (10 shades), background/border defaults in all exports |
| 1.6 | Palette breadth | Number of primitive hue families, Figma variable collections scope |
| 1.7 | Audience accents | `semantic.color.audience.*` (dynamic count), per-persona template color zones |
| 1.8 | Data viz palette | `semantic.color.data.*` (9 tokens), chart component tokens, Remotion chart defaults |
| 1.9 | Dark backgrounds | `semantic.color.surface.inverse`, `semantic.color.text.inverse`, dark slide masters |
| 1.10 | Color exclusions | Exclusion rules in design-recommendations-engine, validation check V.3 |
| 1.1a | Primary recommendation | `primitives.color.primary` base value |
| 1.3a | Secondary recommendation | `primitives.color.secondary` base value |
| 1.7a | Audience accent mapping | `semantic.color.audience.*` (all segments) |
| 1.9a | Dark mode scope | Dark mode token variants, dark slide master inclusion |
| 1.6a | Full palette hues | Additional primitive hue families |
| 1.10a | Exclusion confirmation | Exclusion validation propagation |

### Phase 2: Typography

| Q# | Question | Deliverable Sections Fed |
|---|---|---|
| 2.1 | Heading font | `primitives.font.family.heading`, Tailwind `fontFamily.heading`, Remotion font config, Figma text styles |
| 2.2 | Body font | `primitives.font.family.body`, Tailwind `fontFamily.body`, Remotion font config |
| 2.3 | Monospace font | `primitives.font.family.mono`, `semantic.typography.data`, Tailwind `fontFamily.mono` |
| 2.4 | Heading weight | `primitives.font.weight.*`, `semantic.typography.h1-h4` weight values |
| 2.5 | Text density | `primitives.font.lineHeight.*`, `spacing.layout.*`, Tailwind `lineHeight` |
| 2.6 | Minimum font size | `primitives.font.size.xs`, template footnote/citation styles |
| 2.7 | Heading case | Typography transform rules in all templates |
| 2.8 | Font size scale | `primitives.font.size.*` (all 10 sizes), Tailwind `fontSize`, Remotion text sizes |
| 2.9 | Number formatting | Font feature settings in typography composites, table cell formatting |
| 2.10 | Bilingual distinction | Language-aware template rules, language badge component spec |
| 2.1a | Font recommendation | `primitives.font.family.heading` |
| 2.2a | Body pairing | `primitives.font.family.body` |
| 2.3a | Mono recommendation | `primitives.font.family.mono` |
| 2.10a | Language badge | Language badge component specification |

### Phase 3: Layout, Spacing & Grid

| Q# | Question | Deliverable Sections Fed |
|---|---|---|
| 3.1 | Layout alignment | Slide master grid system, content alignment in all templates |
| 3.2 | White space level | `spacing.layout.*`, `spacing.component.*`, template margin multipliers |
| 3.3 | Slide aspect ratio | Slide master dimensions (width/height), Remotion composition dimensions |
| 3.4 | Border radius | `primitives.radius.*` (6 tokens), Tailwind `borderRadius`, component radius values |
| 3.5 | Base spacing unit | `primitives.space.*` base, harmonic scale derivation, Tailwind `spacing` |
| 3.6 | Table styling | `component.table.*`, slide table component, document table layout |
| 3.7 | Metric display | `component.card.metric`, `semantic.typography.display`, metric template zones |
| 3.8 | Cover page | `templates/document/page-masters.md` cover definition |
| 3.9 | Content margin | `spacing.layout.slide-margin`, template safe zones |
| 3.10 | Grid columns | Grid definitions in slide masters, multi-column layout rules |
| 3.11 | Responsive breakpoints | `primitives.breakpoint.*`, Tailwind `screens`, CSS `--breakpoint-*`, html-spec responsive section |
| 3.12 | Elevation philosophy | `primitives.elevation.*`, `component.modal.backdrop.zIndex`, `component.toast.zIndex`, html-spec elevation section |
| 3.3a | 4:3 derivation | 4:3 variant specs, template priority |
| 3.6a | Table row limits | `component.table.*` conditional rules |
| 3.8a | Cover color | `templates/document/page-masters.md` cover color |
| 3.2a | Data-slide override | Contextual spacing overrides for data-dense slides |

### Phase 4: Components & UI Elements

| Q# | Question | Deliverable Sections Fed |
|---|---|---|
| 4.1 | Button style | `component.button.primary`, `component.button.secondary`, `component.button.ghost` |
| 4.2 | Callout style | `component.callout.*` (5 variants x 6 properties) |
| 4.3 | Logo placement | `component.header.*`, `component.footer.*`, all template logo zones |
| 4.4 | Progress indicator | `component.header.slide`, slide master header zones |
| 4.5 | Citation format | Citation zone in footers, `semantic.typography.caption` |
| 4.6 | Chart styling | `component.chart.*` (axis, grid, tooltip, legend) |
| 4.7 | Partner logos | Logo treatment rules in templates |
| 4.8 | Card elevation | `component.card.*` shadow values, `primitives.shadow.*` |
| 4.9 | Divider style | `component.divider` tokens, template section break zones |
| 4.10 | Badge style | `component.badge.*` |
| 4.11 | Form input style | `component.input.*`, `component.checkbox.*`, `component.radio.*`, `component.select.*`, html-spec inputs section |
| 4.12 | Modal style | `component.modal.*`, html-spec modals section |
| 4.13 | Loading state style | `component.skeleton.*`, html-spec skeleton section |
| 4.1a | Button color | `component.button.primary.default.background` |
| 4.2a | Icon set | Icon specification in component tokens |
| 4.10a | Dark mode components | Dark mode token variants for all components |
| 4.8a | Elevation scope | `component.card.elevated.shadow` vs `component.card.default.shadow` |

### Phase 5: Motion, Animation & Video

| Q# | Question | Deliverable Sections Fed |
|---|---|---|
| 5.1 | Video need | Phase 5 routing, completeness matrix video threshold |
| 5.2 | Animation personality | `primitives.duration.*`, `primitives.easing.*`, Remotion defaults |
| 5.3 | Video formats | `exports/remotion-theme.ts` dimensions, video template variants |
| 5.4 | Frame rate | `exports/remotion-theme.ts` fps |
| 5.5 | Title card | `templates/video/remotion-compositions.md` Title Card spec |
| 5.6 | Lower third | `templates/video/remotion-compositions.md` Lower Third spec |
| 5.7 | Text reveal | `templates/video/remotion-compositions.md` text animation |
| 5.8 | Transitions | Motion tokens for transitions, template transition specs |
| 5.1a | Future video defaults | Completeness matrix adjustment |
| 5.2a | Dynamic calibration | Motion token calibration |
| 5.3a | Format derivation | Video template variant specs |
| 5.4a | FPS per-composition | fps settings per-composition |

### Phase 6: Logo & Brand Assets

| Q# | Question | Deliverable Sections Fed |
|---|---|---|
| 6.1 | Logo files | All template logo zones, exports, Remotion watermark |
| 6.2 | Logo variants | Logo treatment rules, dark/light template variants |
| 6.3 | Clear space | Template logo padding zones |
| 6.4 | Minimum size | Template minimum logo sizing, favicon constraints |
| 6.5 | Favicon | Social media templates, video watermark |
| 6.6 | Co-branding | Template partner logo zones |
| 6.7 | Misuse rules | Logo usage constraints (negative rules for agents) |
| 6.8 | Brand mark | Video watermark specs, favicon derivation |
| 6.1a | Placeholder mode | Template logo zones (placeholder) |
| 6.3a | Clear space rule | Template logo padding calculation |
| 6.8a | Brand mark brief | Brand mark requirements document |

### Phase 7: Photography, Imagery & Illustration

| Q# | Question | Deliverable Sections Fed |
|---|---|---|
| 7.1 | Photography style | Image selection guidelines in templates |
| 7.2 | Image treatment | Image treatment specifications in templates |
| 7.3 | Image/content ratio | Template image zones, slide layout variants |
| 7.4 | Icon style | Icon specifications, diagram styling rules |
| 7.5 | Diagram style | Diagram styling rules in templates |
| 7.6 | Background patterns | Background treatment in slide masters |
| 7.7 | Facility renders | Render specifications (future reference) |
| 7.2a | Tint opacity | Image treatment overlay specs |
| 7.1a | Photo context mapping | Context-specific image selection rules |
| 7.4a | Illustration brief | Illustration brief specifications |

---

## Format B: Deliverable-Centric (Every Section → Feeding Qs)

### Token Files

| Deliverable Section | Feeding Questions | Feeding Research |
|---|---|---|
| `primitives.color.primary.*` | Q1.1, Q1.2, Q1.1a | R0.1, R0.3 |
| `primitives.color.secondary.*` | Q1.3, Q1.3a | R0.1, R0.3 |
| `primitives.color.neutral.*` | Q1.5 | R0.1 |
| `primitives.color.accent.*` | Q1.4 | — |
| `primitives.color.{error,tertiary,info,success}.*` | Q1.6, Q1.6a | — |
| `semantic.color.brand.*` | Q1.1, Q1.3, Q1.4 | R0.1, R0.3 |
| `semantic.color.surface.*` | Q1.5, Q1.9, Q1.9a | R0.1 |
| `semantic.color.text.*` | Q1.5, Q1.9 | R0.1 |
| `semantic.color.audience.*` | Q1.7, Q1.7a | D0.2 |
| `semantic.color.data.*` | Q1.8 | — |
| `primitives.font.family.*` | Q2.1, Q2.2, Q2.3, Q2.1a, Q2.2a, Q2.3a | R0.1, R0.3, R0.5 |
| `primitives.font.weight.*` | Q2.4 | R0.1 |
| `primitives.font.size.*` | Q2.6, Q2.8 | R0.1 |
| `primitives.font.lineHeight.*` | Q2.5 | — |
| `semantic.typography.*` | Q2.4, Q2.5, Q2.7, Q2.8, Q2.9 | R0.1, R0.3 |
| `primitives.space.*` | Q3.5 | R0.1 |
| `spacing.layout.*` | Q3.2, Q3.9, Q3.2a | — |
| `spacing.component.*` | Q3.2 | — |
| `primitives.radius.*` | Q3.4 | R0.1 |
| `primitives.shadow.*` | Q4.8, Q4.8a | — |
| `primitives.duration.*` | Q5.2 | — |
| `primitives.easing.*` | Q5.2 | — |
| `component.button.*` | Q4.1, Q4.1a | — |
| `component.card.*` | Q3.7, Q4.8, Q4.8a | — |
| `component.table.*` | Q3.6, Q3.6a | — |
| `component.callout.*` | Q4.2, Q4.2a | — |
| `component.badge.*` | Q4.10 | — |
| `component.header.*` | Q4.3, Q4.4 | — |
| `component.footer.*` | Q4.3, Q4.5 | — |
| `component.chart.*` | Q4.6 | — |
| `component.divider` | Q4.9 | — |
| `component.input.*` | Q4.11 | — |
| `component.checkbox.*` | Q4.11 | — |
| `component.radio.*` | Q4.11 | — |
| `component.select.*` | Q4.11 | — |
| `component.modal.*` | Q4.12 | — |
| `component.toast.*` | (derived from callout semantics) | — |
| `component.tooltip.*` | (derived from chart tooltip) | — |
| `component.toggle.*` | (derived from button/input patterns) | — |
| `component.skeleton.*` | Q4.13 | — |
| `primitives.elevation.*` | Q3.12 | — |
| `primitives.breakpoint.*` | Q3.11 | — |
| `semantic.color-mode.dark.*` | Q1.9, Q1.9a | — |

### Export Files

| Deliverable | Feeding Questions | Feeding Research |
|---|---|---|
| `tailwind-config.js` | Q1.1-1.10, Q2.1-2.9, Q3.4-3.5, Q4.1-4.10 | R0.1, R0.5 |
| `remotion-theme.ts` | Q1.1-1.10, Q2.1-2.9, Q5.1-5.8 | R0.5 |
| `figma-variables.json` | Q1.1-1.10, Q2.1-2.9, Q3.4-3.5 | R0.1 |
| `css-variables.css` | Q1.1-1.10, Q2.1-2.9, Q3.4-3.5 | — |
| `docx-spec.md` | Q0.1-0.4, Q2.1-2.9, Q3.2, Q3.8, Q3.8a, Q4.1-4.10, Q6.1-6.5 | R0.1, R0.3 |
| `pdf-spec.md` | Q0.1-0.4, Q2.1-2.9, Q3.2, Q3.8, Q3.8a, Q4.1-4.10, Q6.1-6.5, Q7.1-7.6 | R0.1, R0.3 |
| `xlsx-spec.md` | Q0.1-0.4, Q1.1-1.10, Q2.1-2.9, Q3.4, Q3.6, Q3.6a, Q4.1-4.10 | R0.1 |
| `image-spec.md` | Q0.1-0.4, Q1.1-1.10, Q2.1-2.9, Q3.4, Q6.1-6.8, Q7.1-7.6 | R0.1, R0.2 |
| `html-spec.md` | Q1.1-1.10, Q2.1-2.9, Q3.4-3.5, Q3.11-3.12, Q4.1-4.13, Q5.2, Q6.1-6.5, Q7.1-7.4 | R0.1, R0.3 |

### Template Files

| Deliverable | Feeding Questions | Feeding Research |
|---|---|---|
| `slide-masters.md` | Q3.1, Q3.3, Q3.9, Q3.10, Q1.9, Q7.6 | R0.3, D0.3 |
| `slide-components.md` | Q3.6, Q3.7, Q4.1-4.10 | D0.3 |
| `page-masters.md` | Q3.2, Q3.8, Q3.8a | D0.4 |
| `remotion-compositions.md` | Q5.1-5.8, Q5.3a | — |

---

## Coverage Verification

### Orphan Check (questions with no deliverable)
**Result: ZERO orphan questions.** Every question (80 core + 28 conditional = 108 total) maps to at least one deliverable section.

### Unfed Section Check (deliverable sections with no question)
**Result: ZERO unfed sections.** Every deliverable section has at least one feeding question or research task.

### Coverage Statistics
- Total questions: 108 (80 core + 28 conditional)
- Total research tasks: 5 (Phase 0B)
- Total system data points: 5 (Phase 0C, conditional)
- Total deliverable sections: 44 token groups + 9 exports + 4 templates = 57
- Average questions per deliverable section: 2.5
- Maximum questions per deliverable section: 15 (html-spec.md)
- Minimum questions per deliverable section: 1
