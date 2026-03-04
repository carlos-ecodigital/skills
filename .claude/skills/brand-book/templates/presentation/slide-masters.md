# Slide Master Layouts

8 master slide layouts for presentation generation. All measurements reference semantic tokens. Designed for 16:9 (1920x1080) as primary; 4:3 derivation rules included.

**Consumed by:** collateral-studio, seed-fundraising, any agent producing slide decks.

**Token dependency:** `semantic.tokens.json`, `component.tokens.json`.

---

## Global Slide Rules

### Canvas
- **Primary:** 1920 x 1080px (16:9)
- **4:3 derivation:** 1440 x 1080px. Same vertical layout; reduce horizontal margins by 25%. Reduce max columns from 4 to 3.
- **Background:** `semantic.color.surface.default` (#F8FAFC) unless overridden per master.

### Safe Zones
- **Outer margin:** `semantic.spacing.layout.page-margin` (64px) on all sides
- **Content area:** 1792 x 952px (1920 - 2x64, 1080 - 2x64)
- **Logo zone:** Top-left, 48px from top, 64px from left. Max height 40px.
- **Footer zone:** Bottom 48px of slide (y: 1032-1080)
- **Progress bar zone:** Top 3px of slide (y: 0-3)

### Header Strip (when present)
- **Height:** 80px (y: 0-80)
- **Background:** `semantic.color.surface.default`
- **Title:** `semantic.typography.h3` (24px, 700 weight, `semantic.color.text.heading`)
- **Position:** x: 64px, y: 28px (vertically centered in strip)
- **Section badge:** Right-aligned in header, x: 1856px (right-aligned), same y. Uses `component.badge.primary`.

### Footer Strip
- **Height:** 48px (y: 1032-1080)
- **Background:** `semantic.color.surface.subtle` (#F1F5F9)
- **Left:** Logo watermark (20px height, 50% opacity), x: 64px
- **Center:** Confidentiality text. `semantic.typography.caption` (12px, `semantic.color.text.caption`). Text: "{brand_name} Confidential" or custom.
- **Right:** Page number "N / Total". Same typography. x: 1856px (right-aligned).
- **Divider:** 1px `semantic.color.border.default` at y: 1032

### Progress Bar
- **Position:** x: 0, y: 0, full width
- **Height:** `component.header.slide.progressHeight` (3px)
- **Color:** `component.header.slide.progressColor` (`semantic.color.brand.secondary`)
- **Width:** (current_slide / total_slides) * 1920px
- **Background:** `semantic.color.border.default` (full width, behind progress)

### Grid System
- **Columns:** 12-column grid within content area
- **Column width:** (1792 - 11 * 24) / 12 = ~127px per column
- **Gutter:** `semantic.spacing.layout.gap` (24px)
- **Rows:** Not fixed; content flows top-to-bottom within content area

---

## Master 1: Title Slide

**Purpose:** Opening slide, section dividers, key reveals.

### Layout
```
┌─────────────────────────────────────────┐
│ [progress bar - full width, 3px]        │
│                                         │
│                                         │
│                                         │
│   ┌─────────────────────────────────┐   │
│   │         TITLE (centered)        │   │
│   │      max-width: 1200px          │   │
│   │                                 │   │
│   │       Subtitle (centered)       │   │
│   │      max-width: 900px           │   │
│   └─────────────────────────────────┘   │
│                                         │
│            [Presenter name]             │
│              [Date / Event]             │
│                                         │
│ [logo-left]  [confidential]  [page-num] │
└─────────────────────────────────────────┘
```

### Specifications
| Element | Token | Value |
|---|---|---|
| Background | `semantic.color.surface.default` | #F8FAFC |
| Title | `semantic.typography.hero` | 48px, 700 weight, Inter |
| Title color | `semantic.color.text.heading` | #142945 |
| Title max-width | -- | 1200px (centered) |
| Subtitle | `semantic.typography.body-lg` | 18px, 400 weight |
| Subtitle color | `semantic.color.text.secondary` | #64748B |
| Subtitle max-width | -- | 900px (centered) |
| Subtitle margin-top | `semantic.spacing.content.md` | 16px below title |
| Presenter/date | `semantic.typography.body-sm` | 14px, 400 weight |
| Presenter color | `semantic.color.text.secondary` | #64748B |
| Presenter margin-top | `semantic.spacing.layout.gap` | 24px below subtitle |
| Logo | Top-left safe zone | 48px from top, 64px from left |

### Variant: Dark Title Slide
- Background: `semantic.color.surface.inverse` (#0D1F30)
- Title color: `semantic.color.text.inverse` (#FFFFFF)
- Subtitle color: `semantic.color.text.caption` adjusted for dark (#9FB3C8)
- Accent stripe: 6px horizontal bar, `semantic.color.brand.secondary`, centered below subtitle, 200px wide

---

## Master 2: Content Slide

**Purpose:** Standard text + optional visual. The workhorse layout.

### Layout
```
┌─────────────────────────────────────────┐
│ [progress bar]                          │
│ [header strip: slide title + badge]     │
├─────────────────────────────────────────┤
│                                         │
│   ┌──────────────────┐  ┌──────────┐   │
│   │                  │  │          │   │
│   │   Text content   │  │  Visual  │   │
│   │   (8 columns)    │  │(4 cols)  │   │
│   │                  │  │          │   │
│   │                  │  │          │   │
│   └──────────────────┘  └──────────┘   │
│                                         │
│ [footer]                                │
└─────────────────────────────────────────┘
```

### Specifications
| Element | Token | Value |
|---|---|---|
| Content start y | -- | 104px (80px header + 24px gap) |
| Text column span | -- | Columns 1-8 (full width if no visual) |
| Visual column span | -- | Columns 9-12 |
| Body text | `semantic.typography.body` | 16px, 400 weight, 1.5 line-height |
| Body color | `semantic.color.text.primary` | #1E293B |
| Bullet style | -- | 6px circle, `semantic.color.brand.primary`, 8px left of text |
| Bullet indent | -- | 24px per nesting level |
| Bullet spacing | `semantic.spacing.content.sm` | 8px between items |
| Paragraph spacing | `semantic.spacing.content.md` | 16px between paragraphs |

### Variants
- **Text-only:** Single column spanning all 12 columns. Max line-width: 1400px.
- **Visual-left:** Swap text and visual columns. Visual columns 1-4, text 5-12.
- **Two-column text:** Even 6+6 split. Columns 1-6 and 7-12 with 24px gutter.

---

## Master 3: Data / Metrics Slide

**Purpose:** Key numbers, KPIs, financial highlights. High-impact data display.

### Layout
```
┌─────────────────────────────────────────┐
│ [progress bar]                          │
│ [header strip: slide title]             │
├─────────────────────────────────────────┤
│                                         │
│   ┌───────┐ ┌───────┐ ┌───────┐        │
│   │  KPI  │ │  KPI  │ │  KPI  │        │
│   │ card  │ │ card  │ │ card  │        │
│   └───────┘ └───────┘ └───────┘        │
│                                         │
│   ┌─────────────────────────────────┐   │
│   │     Supporting chart or text    │   │
│   └─────────────────────────────────┘   │
│                                         │
│   [Source: citation]                    │
│ [footer]                                │
└─────────────────────────────────────────┘
```

### Specifications
| Element | Token | Value |
|---|---|---|
| Metric cards | `component.card.metric` | See component.tokens.json. **Hero variant** is standalone (1 card, full-width). **Small/Default/Large** variants are used in 2-4 card grid layouts. |
| Card grid | -- | 2-4 cards, equal width, 24px gap. Hero variant: 1 card centered, max-width 800px. |
| Card min-width | -- | 300px |
| Card max per row | -- | 4 (3 preferred for emphasis) |
| Number | `semantic.typography.display` | 42px, 700 weight, `font.family.mono` |
| Number color | `semantic.color.brand.primary` | #1B365D |
| Label | `semantic.typography.caption` | 14px, 400 weight |
| Label color | `semantic.color.text.secondary` | #64748B |
| Unit/suffix | `semantic.typography.body` | 16px, appended to number |
| Trend indicator | -- | Arrow + percentage, colored by `data.positive`/`data.negative` |
| Chart zone | -- | Below cards, full width, max height 400px |
| Source citation | `semantic.typography.caption` | 12px, right-aligned, #94A3B8 |

### Variants
- **Full-width single metric:** One number centered, 72px font size, with context text below.
- **Before/After:** Two metric cards side by side with arrow between. Left = before (muted), right = after (branded).
- **Metric + table:** Cards on top, supporting data table below (using `component.table.*`).

---

## Master 4: Comparison / Table Slide

**Purpose:** Feature comparisons, competitor analysis, pricing tables.

### Layout
```
┌─────────────────────────────────────────┐
│ [progress bar]                          │
│ [header strip: slide title]             │
├─────────────────────────────────────────┤
│                                         │
│   ┌─────────────────────────────────┐   │
│   │  Table Header                   │   │
│   ├─────────────────────────────────┤   │
│   │  Row 1                          │   │
│   ├─────────────────────────────────┤   │
│   │  Row 2                          │   │
│   ├─────────────────────────────────┤   │
│   │  Row 3                          │   │
│   └─────────────────────────────────┘   │
│                                         │
│   [Source: citation]                    │
│ [footer]                                │
└─────────────────────────────────────────┘
```

### Specifications
| Element | Token | Value |
|---|---|---|
| Table | `component.table.*` | See component.tokens.json |
| Header bg | `component.table.header.bg` | #1B365D |
| Header text | `component.table.header.text` | #FFFFFF, 12px, 600 weight |
| Header text-transform | -- | uppercase, 1px letter-spacing |
| Row height | -- | Min 48px, auto-expand for content |
| Row bg | `component.table.row.bg` | #FFFFFF |
| Alt row bg | `component.table.rowAlt.bg` | #F8FAFC |
| Cell padding | -- | 12px horizontal, 10px vertical |
| Cell font | `semantic.typography.body-sm` | 14px, 400 weight |
| Numeric cells | `font.family.mono` | Right-aligned, tabular-nums |
| Highlight column | -- | Brand primary bg at 5% opacity on featured column |
| Check/cross icons | -- | Checkmark: `data.positive` (#22C55E). Cross: `data.negative` (#EF4444). 16px. |
| Max rows | -- | 8 visible rows (scroll/paginate beyond) |
| Max columns | -- | 6 for 16:9, 5 for 4:3 |

### Variants
- **Comparison matrix:** Column 1 = feature names, columns 2+ = options. Header badges for each option.
- **Pricing table:** Columns = tiers. Featured tier has brand border and "Recommended" badge.
- **Scorecard:** Numeric values with conditional formatting (green/amber/red).

---

## Master 5: Chart / Visualization Slide

**Purpose:** Charts, graphs, data visualizations.

### Layout
```
┌─────────────────────────────────────────┐
│ [progress bar]                          │
│ [header strip: slide title]             │
├─────────────────────────────────────────┤
│                                         │
│   ┌──────────────────────────────┐      │
│   │                              │      │
│   │         Chart Area           │      │
│   │      (max 1600 x 680)       │      │
│   │                              │      │
│   │                              │      │
│   └──────────────────────────────┘      │
│   [Legend: inline or below]             │
│   [Source: citation]                    │
│ [footer]                                │
└─────────────────────────────────────────┘
```

### Specifications
| Element | Token | Value |
|---|---|---|
| Chart area | -- | Max 1600 x 680px, centered |
| Chart bg | transparent | Chart renders on slide background |
| Axis | `component.chart.axis` | 1px, #64748B, 12px labels |
| Grid lines | `component.chart.grid` | 1px, #F1F5F9, horizontal only (default) |
| Data colors | `semantic.color.data.series-1` through `series-6` | See semantic.tokens.json |
| Positive/negative | `semantic.color.data.positive` / `negative` | #22C55E / #EF4444 |
| Legend | `component.chart.legend` | 12px, 16px gap, positioned below chart |
| Legend marker | -- | 12px circle/square matching series color |
| Tooltip | `component.chart.tooltip` | Dark bg (#0D1F30), white text, 8px radius |
| Data labels | `semantic.typography.data` | 14px, 600 weight, `font.family.mono` |
| Y-axis label | `semantic.typography.caption` | 12px, rotated -90deg |
| X-axis label | `semantic.typography.caption` | 12px, below axis |

### Chart Type Defaults
| Type | Grid | Legend Position | Label Style |
|---|---|---|---|
| Bar (vertical) | Horizontal only | Bottom center | Above bars |
| Bar (horizontal) | Vertical only | Top right | End of bars |
| Line | Horizontal + vertical | Top right | Point labels or tooltip |
| Pie/donut | None | Right side | Direct labels |
| Scatter | Both | Top right | Tooltip only |
| Area | Horizontal only | Bottom center | Tooltip |

---

## Master 6: Two-Up / Split Slide

**Purpose:** Side-by-side content, before/after, problem/solution.

### Layout
```
┌─────────────────────────────────────────┐
│ [progress bar]                          │
│ [header strip: slide title]             │
├──────────────────┬──────────────────────┤
│                  │                      │
│    Left panel    │    Right panel       │
│   (6 columns)    │   (6 columns)        │
│                  │                      │
│                  │                      │
│                  │                      │
│                  │                      │
├──────────────────┴──────────────────────┤
│ [footer]                                │
└─────────────────────────────────────────┘
```

### Specifications
| Element | Token | Value |
|---|---|---|
| Left panel | -- | Columns 1-6 (x: 64-884) |
| Right panel | -- | Columns 7-12 (x: 908-1856) |
| Gutter | `semantic.spacing.layout.gap` | 24px between panels |
| Divider (optional) | `component.divider` | 1px vertical, #E2E8F0, centered in gutter |
| Panel label | `semantic.typography.overline` | 11px, uppercase, 1.5px letter-spacing |
| Panel label color | `semantic.color.brand.primary` | #1B365D |

### Variants
- **Dark + Light:** Left panel: `surface.inverse` bg with inverse text. Right panel: default.
- **Image + Text:** Left = full-bleed image. Right = text content with 32px left padding.
- **Problem + Solution:** Left labeled "Challenge" (muted). Right labeled "Solution" (branded). Right panel has accent left border.

---

## Master 7: Quote / Testimonial Slide

**Purpose:** Customer quotes, expert endorsements, key statements.

### Layout
```
┌─────────────────────────────────────────┐
│ [progress bar]                          │
│                                         │
│                                         │
│         ┌───────────────────┐           │
│    "    │   Quote text      │           │
│   big   │   centered,       │           │
│   open  │   max 900px       │           │
│   quote │                   │           │
│         └───────────────────┘           │
│                                         │
│          -- Speaker Name                │
│             Title, Company              │
│                                         │
│ [footer]                                │
└─────────────────────────────────────────┘
```

### Specifications
| Element | Token | Value |
|---|---|---|
| Background | `semantic.color.surface.default` | #F8FAFC |
| Open quote mark | -- | 120px, `semantic.color.brand.secondary` at 20% opacity |
| Quote text | `semantic.typography.h2` | 30px, 500 weight (medium, not bold) |
| Quote color | `semantic.color.text.heading` | #142945 |
| Quote max-width | -- | 900px, centered |
| Quote line-height | `font.lineHeight.snug` | 1.25 |
| Attribution dash | -- | Em dash, same line as name |
| Speaker name | `semantic.typography.body` | 16px, 600 weight |
| Speaker title | `semantic.typography.body-sm` | 14px, 400 weight, secondary color |
| Attribution margin-top | `semantic.spacing.content.lg` | 24px below quote |

### Variants
- **Dark quote:** `surface.inverse` background. Inverse text colors.
- **Photo + quote:** Speaker photo (80px circle) left of attribution.
- **Brand accent:** Left vertical bar (6px, `brand.secondary`) instead of open quote mark.

---

## Master 8: Closing / CTA Slide

**Purpose:** Final slide with call to action, contact info, next steps.

### Layout
```
┌─────────────────────────────────────────┐
│ [progress bar - 100%]                   │
│                                         │
│                                         │
│         [Logo - large, centered]        │
│                                         │
│         Thank you / CTA headline        │
│                                         │
│         Contact info / Next steps       │
│         (centered, max 700px)           │
│                                         │
│                                         │
│                                         │
│ [footer]                                │
└─────────────────────────────────────────┘
```

### Specifications
| Element | Token | Value |
|---|---|---|
| Background | `semantic.color.surface.brand` | #1B365D |
| Logo | -- | Centered, max 200px wide, white/inverse variant |
| Logo margin-bottom | `semantic.spacing.layout.section` | 48px |
| CTA headline | `semantic.typography.h1` | 36px, 700 weight |
| CTA color | `semantic.color.text.inverse` | #FFFFFF |
| Contact text | `semantic.typography.body` | 16px, 400 weight |
| Contact color | -- | White at 80% opacity |
| Contact margin-top | `semantic.spacing.content.lg` | 24px |
| Contact items | -- | Email, phone, website -- centered, stacked with 8px gap |

### Variants
- **Light closing:** `surface.default` background, dark text. Less dramatic.
- **Next steps:** Replace contact info with 3 numbered steps. Each: circle number (branded) + text.
- **Dual CTA:** Two buttons side-by-side: primary CTA (filled) + secondary CTA (outlined).

---

## 4:3 Derivation Rules

When generating 4:3 (1440x1080) from 16:9 masters:

| Property | 16:9 Value | 4:3 Adjustment |
|---|---|---|
| Canvas width | 1920px | 1440px |
| Outer margin | 64px | 48px |
| Content area width | 1792px | 1344px |
| Max columns | 12 | 9 (proportional) |
| Gutter | 24px | 20px |
| Max table columns | 6 | 5 |
| Max metric cards | 4 | 3 |
| Chart area max-width | 1600px | 1200px |
| Two-up panels | 6+6 columns | 4+5 columns (slight asymmetry OK) |
| Title max-width | 1200px | 1000px |
| Quote max-width | 900px | 750px |
| Font sizes | No change | No change (same typographic scale) |

---

## Slide Transition Defaults

Between slides, not within-slide animations.

| Transition | Motion Token | Usage |
|---|---|---|
| Default | `motion.duration.default` (300ms), `motion.easing.default` | Standard slide transition |
| Section change | `motion.duration.slow` (500ms), `motion.easing.out` | Between major sections |
| Data reveal | `motion.duration.enter` (350ms), `motion.easing.out` | Metric card or chart appearance |
| None | 0ms | Title slide, closing slide |
