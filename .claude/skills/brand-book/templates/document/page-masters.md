# Document Page Masters

Page layout templates for generated documents: reports, one-pagers, proposals, memos, data room materials. All measurements reference semantic tokens. Designed for A4 (210x297mm) as primary; US Letter derivation rules included.

**Consumed by:** collateral-studio, ops-dataroomops, legal-counsel, any agent producing documents.

**Token dependency:** `semantic.tokens.json`, `component.tokens.json`.

---

## Global Document Rules

### Page Setup
- **Primary:** A4 (210 x 297mm / 595 x 842pt)
- **US Letter derivation:** 216 x 279mm (612 x 792pt). Same margins; reduce bottom content area by 18mm.
- **Orientation:** Portrait (default). Landscape for data-heavy appendix pages.

### Margins
| Edge | Measurement | Notes |
|---|---|---|
| Top | 25mm (first page with header: 40mm) | Header occupies 25-40mm |
| Bottom | 25mm (with footer: 35mm) | Footer occupies 10mm |
| Left | 25mm | Binding margin if needed: 30mm |
| Right | 20mm | Slightly narrower for asymmetric balance |
| Content width | 165mm (A4) | 210 - 25 - 20 |
| Content height | 237mm (A4, no header/footer) | 297 - 25 - 35 |

### Typography Scale (Document Context)
Document typography is slightly larger than screen to account for print/PDF reading distance.

| Role | Size | Weight | Line-Height | Token Reference |
|---|---|---|---|---|
| Document title (cover) | 36pt | 700 | 1.1 | `semantic.typography.hero` |
| Section heading (H1) | 24pt | 700 | 1.2 | `semantic.typography.h1` |
| Subsection (H2) | 18pt | 600 | 1.25 | `semantic.typography.h2` |
| Sub-subsection (H3) | 14pt | 600 | 1.3 | `semantic.typography.h3` |
| Body text | 11pt | 400 | 1.5 | `semantic.typography.body` |
| Body large (intro paragraphs) | 12pt | 400 | 1.5 | `semantic.typography.body-lg` |
| Caption / footnotes | 9pt | 400 | 1.4 | `semantic.typography.caption` |
| Table body | 9pt | 400 | 1.3 | `semantic.typography.data` |
| Table header | 9pt | 600 | 1.3 | `semantic.typography.label` |
| Page number | 9pt | 400 | -- | `semantic.typography.caption` |

### Heading Spacing
| Before Heading | After Heading | Rule |
|---|---|---|
| 18pt (H1) | 8pt | Keep-with-next: always |
| 14pt (H2) | 6pt | Keep-with-next: always |
| 10pt (H3) | 4pt | Keep-with-next: always |
| 8pt (paragraph) | 4pt | -- |

### Color Usage in Documents
Documents use a restrained palette compared to presentations:
- **Body text:** `semantic.color.text.primary` (#1E293B)
- **Headings:** `semantic.color.text.heading` (#142945)
- **Secondary text:** `semantic.color.text.secondary` (#64748B)
- **Links:** `semantic.color.text.link` (#243B53), underlined
- **Accent (sparingly):** `semantic.color.brand.primary` for horizontal rules, callout borders
- **Tables:** Full component palette from `component.table.*`
- **Charts:** Full data palette from `semantic.color.data.*`

---

## Master 1: Cover Page

**Purpose:** First page of any document. Sets professional tone.

### Layout
```
┌─────────────────────────────────┐
│                                 │
│  [Logo -- top-left, 30mm from  │
│   top, 25mm from left]         │
│                                 │
│                                 │
│                                 │
│                                 │
│  ─────────────────────────      │
│  (accent stripe: 3px,          │
│   brand.primary, 80mm wide)    │
│                                 │
│  DOCUMENT TITLE                 │
│  (36pt, bold, heading color)    │
│                                 │
│  Subtitle / Description         │
│  (14pt, secondary color)        │
│                                 │
│                                 │
│                                 │
│                                 │
│  Prepared for: [Client]         │
│  Prepared by: {brand_name}      │
│  Date: [Date]                   │
│  Version: [Version]             │
│  Classification: [Confidential] │
│                                 │
└─────────────────────────────────┘
```

### Specifications
| Element | Position | Style |
|---|---|---|
| Logo | x: 25mm, y: 30mm | Max height: 15mm. Full-color variant. |
| Accent stripe | x: 25mm, y: 130mm | 3px height, 80mm width, `brand.primary` (#1B365D) |
| Title | x: 25mm, y: 140mm | 36pt, 700 weight, `text.heading` |
| Title max-width | -- | 140mm |
| Subtitle | x: 25mm, y: title + 10mm | 14pt, 400 weight, `text.secondary` |
| Metadata block | x: 25mm, y: 230mm (bottom zone) | 10pt, 400 weight, `text.secondary` |
| Metadata label | -- | 10pt, 600 weight (slightly bolder than value) |
| Metadata spacing | -- | 5mm between entries |

### Variants
- **Full-color cover:** `surface.brand` (#1B365D) background. White text and logo. Accent stripe in `brand.secondary`.
- **Photographic cover:** Full-bleed image with 60% dark overlay. White text overlaid.
- **Minimal cover:** No accent stripe. Logo + title + metadata only. Maximum white space.

---

## Master 2: Content Page

**Purpose:** Standard body content with optional sidebar or margin notes.

### Layout
```
┌─────────────────────────────────┐
│ [Header: logo-left, title-right]│
│ ──────────────────────────────  │
│                                 │
│  H2 Section Heading             │
│                                 │
│  Body text in single column,    │
│  165mm wide. Paragraph style    │
│  with 8pt spacing between       │
│  paragraphs.                    │
│                                 │
│  ┌────────────────────────┐     │
│  │ Callout or figure      │     │
│  │ (full content width)   │     │
│  └────────────────────────┘     │
│                                 │
│  More body text continues...    │
│                                 │
│ ──────────────────────────────  │
│ [Footer: page#, classification] │
└─────────────────────────────────┘
```

### Header
| Element | Position | Style |
|---|---|---|
| Logo | x: 25mm, y: 10mm | Max height: 10mm. Monochrome or full-color. |
| Document title | Right-aligned, y: 12mm | 9pt, 400 weight, `text.caption` |
| Header border | x: 25mm, y: 22mm, full content width | 1px, `border.default` (#E2E8F0) |

### Footer
| Element | Position | Style |
|---|---|---|
| Footer border | x: 25mm, y: 282mm, full content width | 1px, `border.default` |
| Page number | Right-aligned, y: 286mm | 9pt, `text.caption` |
| Classification | Left-aligned, y: 286mm | 9pt, `text.caption`, italic |
| Company name | Centered, y: 286mm | 9pt, `text.caption` |

### Content Rules
- **Single column** default (165mm wide)
- **Paragraph indent:** None (use spacing between paragraphs instead)
- **First paragraph after heading:** No extra top spacing (heading spacing handles it)
- **Bulleted lists:** 5mm indent, 2.5mm circle bullet, `brand.primary` color, 3pt spacing between items
- **Numbered lists:** 5mm indent, numbers in `brand.primary`, period after number
- **Block quotes:** 10mm left indent, 3px left border (`brand.primary`), italic body text

### Variants
- **Two-column:** 80mm + 80mm with 5mm gutter. For dense reference material.
- **Sidebar:** 120mm main + 40mm sidebar (right). Sidebar: callouts, key facts, pull quotes. Sidebar bg: `surface.subtle` with 5mm padding.
- **Margin notes:** 135mm main content + 30mm right margin for annotations. Margin text: 8pt, `text.caption`.

---

## Master 3: Table Page

**Purpose:** Data-heavy pages with large tables or comparison matrices.

### Layout
```
┌─────────────────────────────────┐
│ [Header]                        │
│ ──────────────────────────────  │
│                                 │
│  Table Title (H3)               │
│                                 │
│  ┌────────────────────────────┐ │
│  │ Table Header               │ │
│  ├────────────────────────────┤ │
│  │ Row 1                      │ │
│  ├────────────────────────────┤ │
│  │ Row 2                      │ │
│  ├────────────────────────────┤ │
│  │ Row 3                      │ │
│  ├────────────────────────────┤ │
│  │ ...                        │ │
│  └────────────────────────────┘ │
│                                 │
│  Source: [citation]             │
│  Notes: [footnotes]            │
│                                 │
│ ──────────────────────────────  │
│ [Footer]                        │
└─────────────────────────────────┘
```

### Table Specifications
| Property | Value |
|---|---|
| Max width | Full content width (165mm) |
| Header bg | `component.table.header.bg` (#1B365D) |
| Header text | `component.table.header.text` (#FFFFFF), 9pt, 600 weight, uppercase |
| Header letter-spacing | 0.03em |
| Row text | 9pt, 400 weight, `text.primary` |
| Alt row bg | `component.table.rowAlt.bg` (#F8FAFC) |
| Cell padding | 3mm H, 2mm V |
| Borders | 0.5pt, `border.default` (#E2E8F0), horizontal only |
| Numeric alignment | Right-aligned, tabular-nums, `font.family.mono` |
| Max rows per page | ~25 (auto-paginate with header repeat) |
| Table title | H3 style, 6pt above table |
| Table source | Caption style, 4pt below table, right-aligned |

### Special Formatting
- **Totals row:** Bold, top border 2px `border.strong`
- **Subtotal rows:** Medium weight, subtle bg `surface.subtle`
- **Highlighted cells:** `brand.primary` at 5% opacity background
- **Conditional formatting:** Green/amber/red cell text for status values

### Landscape Table Page
For tables exceeding 6 columns, rotate to landscape (297 x 210mm):
- Margins: 20mm all sides
- Content width: 257mm
- Reduce font to 8pt body if needed
- Always include "Table continues on next page" notation if split

---

## Master 4: Appendix Page

**Purpose:** Reference material, detailed data, supporting information.

### Layout
Same as Content Page with these modifications:

| Modification | Value |
|---|---|
| Header prefix | "Appendix [Letter]: [Title]" |
| Page numbering | "A-1, A-2..." format |
| Font size body | 10pt (slightly smaller than main content) |
| Table font size | 8pt (denser packing) |
| Margins | Same as content page |
| Two-column default | Yes (for reference lists, glossaries) |

### Appendix-Specific Components
- **Glossary:** Term (bold) + definition (regular). 3pt between entries. Alpha dividers.
- **Reference list:** Numbered, hanging indent (7mm). APA-style citation formatting.
- **Index:** Two-column, 8pt, comma-separated page references.

---

## Master 5: One-Pager

**Purpose:** Single-page summary document. Front and back (2 sides max).

### Layout (Front)
```
┌─────────────────────────────────┐
│ [Logo-left]        [Audience tag]│
│ ══════════════════════════════  │
│                                 │
│  HEADLINE (H1, max 2 lines)    │
│  Subhead (body-lg, 2 lines)    │
│                                 │
│  ┌──────────┐  ┌──────────┐    │
│  │  Metric  │  │  Metric  │    │
│  │  Card 1  │  │  Card 2  │    │
│  └──────────┘  └──────────┘    │
│                                 │
│  ┌──────────┐  ┌──────────┐    │
│  │  Metric  │  │  Metric  │    │
│  └──────────┘  └──────────┘    │
│                                 │
│  Key paragraph (body, max 4    │
│  lines for scanability)        │
│                                 │
│  ┌────────────────────────────┐ │
│  │  Table or comparison (5    │ │
│  │  rows max)                 │ │
│  └────────────────────────────┘ │
│                                 │
│  CTA text + contact             │
│ ──────────────────────────────  │
│ [Footer: classification + URL]  │
└─────────────────────────────────┘
```

### One-Pager Rules
| Property | Value |
|---|---|
| Margin | 15mm all sides (tighter than full documents) |
| Content width | 180mm |
| Max sections | 4-5 visual blocks |
| Headline | 24pt, 700 weight, `text.heading` |
| Body text | 10pt (slightly smaller for density) |
| Metric cards | Small variant (see slide-components.md) |
| Table | Max 5 rows, no alt-row coloring (too dense) |
| CTA | 11pt, 600 weight, `brand.primary` |
| White space | Minimum 5mm between blocks |
| Header rule | 2px, `brand.primary`, full width |

---

## Document Component Reference

Components shared across all page masters:

### Horizontal Rule
| Variant | Style |
|---|---|
| Section break | 1px, `border.default`, full content width |
| Strong break | 2px, `brand.primary`, 60mm width, left-aligned |
| Accent break | 3px, `brand.secondary`, 40mm width |

### Figure Container
| Property | Value |
|---|---|
| Image max-width | Content width (165mm) |
| Caption | Below image, 9pt, `text.caption`, italic |
| Figure number | "Figure N: " prefix, 9pt, 600 weight |
| Border | Optional 1px `border.default` around image |
| Spacing | 8pt above, 4pt below image, 4pt below caption |

### Pull Quote
| Property | Value |
|---|---|
| Left border | 3px, `brand.primary` |
| Indent | 10mm from left |
| Font | 14pt, 500 weight, `text.heading` |
| Line-height | 1.3 |
| Max-width | 130mm |
| Attribution | 10pt, `text.secondary`, em-dash prefix |

### Page Break Rules
| Content | Rule |
|---|---|
| Before H1 | Always page break |
| Before H2 | Page break if < 60mm remaining |
| Tables | Keep together when table fits on current page; split with header repeat when table exceeds page height (~25 rows at default spacing; ~10 rows for tables with multi-line cells or wide content requiring landscape rotation) |
| Figures | Keep with caption; allow page break before figure |
| Callouts | Keep together; page break before if < 40mm remaining |
| Lists | Keep first 3 items with heading; break allowed after item 3 |

---

## Print Considerations

### Color Management
- Body text: Use `text.primary` (#1E293B) not pure black (#000000) for softer print appearance
- Brand colors: Provide Pantone equivalents in brand-config if print fidelity critical
- Charts: Ensure all series distinguishable in grayscale (backup to pattern/shape encoding)

### Font Embedding
- All fonts must be embedded in PDF output
- Subsetting allowed for file size reduction
- Fallback stack: brand font -> system sans -> Arial

### Bleed (for professional printing)
- Add 3mm bleed on all sides if full-bleed elements present
- Crop marks: 0.25pt, 5mm from trim edge
- Safe zone: Keep all text/logos 5mm inside trim edge
