# Slide Components

Reusable presentation components that compose into slide masters. Each component is self-contained with complete token references and can be placed anywhere within the slide content area.

**Consumed by:** collateral-studio, seed-fundraising, any agent producing slide decks.

**Token dependency:** `semantic.tokens.json`, `component.tokens.json`.

---

## Component 1: Metric Card

A standalone KPI display unit. Used in Master 3 (Data/Metrics) and as inline elements.

### Structure
```
┌─────────────────────────────────┐
│  [optional trend arrow + %]     │
│                                 │
│       42 MW                     │
│    (big number + unit)          │
│                                 │
│    IT Load Capacity             │
│    (label text)                 │
│                                 │
│  [optional context line]        │
└─────────────────────────────────┘
```

### Specifications
| Property | Token | Value |
|---|---|---|
| Background | `component.card.metric.bg` | #FFFFFF |
| Border | `component.card.default.border` | 1px solid #E2E8F0 |
| Border-radius | `component.card.default.radius` | 12px |
| Padding | `component.card.default.padding` | 24px |
| Number font | `component.card.metric.numberSize` + `font.family.mono` | 42px, JetBrains Mono |
| Number weight | `component.card.metric.numberWeight` | 700 |
| Number color | `semantic.color.brand.primary` | #1B365D |
| Unit | -- | Appended to number, 24px, 400 weight |
| Label | `component.card.metric.labelSize` | 14px |
| Label color | `component.card.metric.labelColor` | #64748B |
| Label margin-top | `semantic.spacing.content.sm` | 8px |
| Trend arrow (up) | -- | Triangle + percentage, `semantic.color.data.positive` (#22C55E) |
| Trend arrow (down) | -- | Triangle + percentage, `semantic.color.data.negative` (#EF4444) |
| Trend position | -- | Top-right of card, 12px font size |
| Context line | `semantic.typography.caption` | 12px, #94A3B8, below label with 4px gap |

### Size Variants
| Variant | Dimensions | Number Size | Label Size |
|---|---|---|---|
| Small | 200 x 140px | 30px | 12px |
| Default | 300 x 180px | 42px | 14px |
| Large | 420 x 220px | 54px | 16px |
| Hero (single) | Full width x 260px | 72px | 18px |

---

## Component 2: Data Table

Structured tabular data display. Used in Master 4 (Comparison/Table).

### Structure
```
┌──────────────────────────────────────────┐
│  Header  │  Header  │  Header  │ Header  │
├──────────┼──────────┼──────────┼─────────┤
│  Cell    │  Cell    │  Cell    │  Cell   │
├──────────┼──────────┼──────────┼─────────┤
│  Cell    │  Cell    │  Cell    │  Cell   │
├──────────┼──────────┼──────────┼─────────┤
│  Cell    │  Cell    │  Cell    │  Cell   │
└──────────┴──────────┴──────────┴─────────┘
```

### Specifications
| Property | Token | Value |
|---|---|---|
| Header bg | `component.table.header.bg` | #1B365D |
| Header text | `component.table.header.text` | #FFFFFF |
| Header font | `component.table.header.fontSize` | 12px, 600 weight, uppercase |
| Header letter-spacing | -- | 0.05em |
| Header padding | -- | 12px H, 10px V |
| Header border-radius | -- | 8px top-left + top-right on first/last |
| Row bg | `component.table.row.bg` | #FFFFFF |
| Alt row bg | `component.table.rowAlt.bg` | #F8FAFC |
| Row text | `component.table.row.text` | #1E293B, 14px |
| Row padding | -- | 12px H, 10px V |
| Row min-height | -- | 44px |
| Border | `component.table.border` | 1px solid #E2E8F0 (horizontal only) |
| Numeric cells | -- | `font.family.mono`, right-aligned, font-variant-numeric: tabular-nums |
| Hover row | `component.table.rowHover.bg` | #F0F4F8 (interactive contexts only) |

### Special Cell Types
| Type | Rendering |
|---|---|
| **Currency** | Mono font, right-aligned, `$` or `EUR` prefix |
| **Percentage** | Mono font, right-aligned, `%` suffix |
| **Status** | Badge component (pill), semantic color per status |
| **Check/Cross** | Icon 16px. Check: #22C55E. Cross: #EF4444. Dash: #94A3B8 |
| **Bar** | Horizontal progress bar in cell, height 6px, brand primary fill |
| **Highlighted** | Cell bg: brand primary at 5% opacity |

---

## Component 3: Callout Box

Colored notification/emphasis block. 5 semantic variants + brand.

### Structure
```
┌─ ────────────────────────────────────┐
│ │  [Icon]  Title text                │
│ │                                    │
│ │  Body text that provides context   │
│ │  and supporting detail.            │
│ │                                    │
└─ ────────────────────────────────────┘
  ^-- accent border (4px)
```

### Specifications
| Property | Token | Value |
|---|---|---|
| Border-left width | `component.callout.borderWidth` | 4px |
| Border-radius | `component.callout.radius` | 8px |
| Padding | `component.callout.padding` | 16px (all sides); 20px left (to clear border) |
| Title font | `semantic.typography.label` | 14px, 600 weight |
| Body font | `semantic.typography.body-sm` | 14px, 400 weight |
| Title margin-bottom | `semantic.spacing.content.xs` | 4px |

### Variants
| Variant | Background | Border | Text | Icon |
|---|---|---|---|---|
| Info | `component.callout.info.bg` (#EFF6FF) | `component.callout.info.border` (#1D4ED8) | #1D4ED8 | Info circle |
| Success | `component.callout.success.bg` (#F0FDF4) | `component.callout.success.border` (#15803D) | #15803D | Check circle |
| Warning | `component.callout.warning.bg` (#FFFBEB) | `component.callout.warning.border` (#B45309) | #B45309 | Warning triangle |
| Error | `component.callout.error.bg` (#FEF2F2) | `component.callout.error.border` (#B91C1C) | #B91C1C | X circle |
| Brand | primary-50 (#F0F4F8) | brand.primary (#1B365D) | #1B365D | Brand mark |
| Audience | audience accent-50 bg | audience accent color | accent-800 | Audience icon |

---

## Component 4: Comparison Matrix

Side-by-side comparison for 2-4 options. Used in Master 4 and standalone.

### Structure
```
┌──────────┬───────────┬───────────┬───────────┐
│          │  Option A │ Option B  │ Option C  │
│          │  (badge)  │ (featured)│  (badge)  │
├──────────┼───────────┼───────────┼───────────┤
│ Feature  │    ✓      │    ✓      │    -      │
├──────────┼───────────┼───────────┼───────────┤
│ Feature  │    -      │    ✓      │    ✓      │
├──────────┼───────────┼───────────┼───────────┤
│ Feature  │   text    │   text    │   text    │
└──────────┴───────────┴───────────┴───────────┘
```

### Specifications
| Property | Token | Value |
|---|---|---|
| Feature column width | -- | 30-40% of total width |
| Option column width | -- | Equal distribution of remaining space |
| Featured column | -- | Brand primary border (2px), header: brand primary bg with white text |
| Non-featured header | -- | `surface.subtle` bg, `text.heading` color |
| "Recommended" badge | `component.badge.primary` | Positioned below option name in header |
| Feature label | `semantic.typography.body-sm` | 14px, left-aligned, `text.primary` |
| Feature group separator | -- | 2px border-top, `border.strong`, bold group label |

---

## Component 5: Timeline / Process Flow

Horizontal or vertical step sequence.

### Horizontal Layout
```
  ①──────────②──────────③──────────④
  Step 1     Step 2     Step 3     Step 4
  Desc       Desc       Desc       Desc
```

### Specifications
| Property | Token | Value |
|---|---|---|
| Node circle | -- | 32px diameter, `brand.primary` bg, white number (16px, 700 weight) |
| Connector line | -- | 2px, `border.default` (#E2E8F0), centered vertically through nodes |
| Active node | -- | `brand.secondary` bg instead of primary |
| Step label | `semantic.typography.label` | 14px, 600 weight, centered below node |
| Step description | `semantic.typography.caption` | 12px, 400 weight, centered, max 150px width |
| Node spacing | -- | Equal distribution across available width |
| Label margin-top | `semantic.spacing.content.sm` | 8px below node |
| Description margin-top | `semantic.spacing.content.xs` | 4px below label |

### Variants
- **Vertical:** Nodes stacked vertically, connector on left. Labels right of nodes.
- **Completed state:** Checkmark replaces number in completed nodes. Node bg: `data.positive`.
- **Branching:** Connector splits. Dotted line for optional/conditional paths.

---

## Component 6: Logo Block

Brand logo placement with clear space enforcement.

### Specifications
| Property | Token | Value |
|---|---|---|
| Clear space | -- | Minimum 50% of logo height on all sides |
| Max height (header) | -- | 40px |
| Max height (title slide) | -- | 80px |
| Max height (closing slide) | -- | 200px wide or 80px tall, whichever constrains first |
| Watermark opacity | `brandTheme.logo.watermarkOpacity` | 0.15 |
| Watermark size | `brandTheme.logo.watermarkSize` | 48px |
| Watermark position | `brandTheme.logo.watermarkPosition` | Bottom-right |
| Watermark margin | `brandTheme.logo.watermarkMargin` | 24px from edge |

### Logo Variants Expected
| Variant | Usage |
|---|---|
| Full color (primary bg) | On light backgrounds |
| White / inverse | On dark or brand-colored backgrounds |
| Icon only (mark) | Small contexts, favicons, watermarks |
| Monochrome (dark) | Formal documents, fax, B&W printing |

---

## Component 7: Section Divider Badge

Inline badge marking section boundaries within a deck.

### Specifications
| Property | Token | Value |
|---|---|---|
| Style | `component.badge.primary` | Pill shape (9999px radius) |
| Background | -- | primary-50 (#F0F4F8) |
| Text | -- | primary-700 (#1B365D), 12px, 600 weight, uppercase |
| Padding | `component.badge.paddingX/Y` | 8px H, 4px V |
| Positioning | -- | Right-aligned in header strip |

---

## Component 8: Source Citation

Attribution line for data, quotes, and referenced materials.

### Specifications
| Property | Token | Value |
|---|---|---|
| Font | `semantic.typography.caption` | 12px, 400 weight |
| Color | `semantic.color.text.caption` | #94A3B8 |
| Prefix | -- | "Source: " in 500 weight (slightly bolder) |
| Position | -- | Below the referenced content, right-aligned |
| Margin-top | `semantic.spacing.content.sm` | 8px above citation |
| Max-width | -- | Match parent content width |
| Multiple sources | -- | Semicolon-separated on same line, or stacked if > 100 chars |

---

## Component 9: Icon + Label Pair

Used in feature lists, benefit blocks, contact info.

### Structure
```
[icon]  Label text
        Optional description
```

### Specifications
| Property | Token | Value |
|---|---|---|
| Icon size | -- | 20px (inline with label) or 32px (stacked/block) |
| Icon color | `semantic.color.brand.primary` | #1B365D |
| Icon-to-label gap | `semantic.spacing.content.sm` | 8px |
| Label | `semantic.typography.body` | 16px, 500 weight |
| Label color | `semantic.color.text.primary` | #1E293B |
| Description | `semantic.typography.body-sm` | 14px, 400 weight, secondary color |
| Description margin-top | `semantic.spacing.content.xs` | 4px |

### Icon Style
- Outline/stroke style preferred (not filled)
- Consistent 1.5px stroke weight
- Rounded corners/caps
- From standard icon set (Lucide, Phosphor, or Heroicons)

---

## Component 10: Audience Tag

Visual marker identifying which audience segment content targets.

### Structure
```
[●  Neocloud]  or  [audience-colored dot + label]
```

### Specifications
| Property | Token | Value |
|---|---|---|
| Dot | -- | 8px circle, audience accent color |
| Label | `semantic.typography.caption` | 12px, 500 weight |
| Label color | -- | Audience accent color (dark variant for readability) |
| Gap (dot to label) | -- | 6px |
| Background | -- | Audience accent color at 10% opacity |
| Padding | -- | 6px H, 3px V |
| Border-radius | -- | 9999px (pill) |

### Audience Colors (DE defaults)
| Segment | Color Token | Value |
|---|---|---|
| Grower | `semantic.color.audience.grower` | #65A30D |
| District Heat | `semantic.color.audience.district-heat` | #EA580C |
| Industrial Heat | `semantic.color.audience.industrial-heat` | #B45309 |
| Neocloud | `semantic.color.audience.neocloud` | #2563EB |
| Enterprise | `semantic.color.audience.enterprise` | #4338CA |
| Institution | `semantic.color.audience.institution` | #0F766E |

---

## Component Composition Rules

### Spacing Between Components
| Context | Gap | Token |
|---|---|---|
| Components in same content block | 16px | `semantic.spacing.content.md` |
| Components in different sections | 24px | `semantic.spacing.layout.gap` |
| Component and its citation | 8px | `semantic.spacing.content.sm` |
| Metric cards in a row | 24px | `semantic.spacing.layout.gap` |
| Stacked callouts | 12px | `semantic.spacing.content.md` - 4px |

### Z-Order (layering)
1. Background (slide master bg)
2. Grid/guidelines (invisible in final output)
3. Content blocks (body text, tables, charts)
4. Cards and callouts (elevated above content)
5. Header/footer strips
6. Progress bar (topmost)
7. Tooltips/overlays (interactive only)

### Responsive Scaling (for different aspect ratios)
- Components maintain **minimum** dimensions (don't shrink below specified min)
- Horizontal spacing compresses first (gutter: 24px -> 16px -> 12px)
- Then column count reduces (4 -> 3 -> 2)
- Font sizes never change between aspect ratios
- Vertical spacing compresses last
