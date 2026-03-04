---
chunk_id: "material-extraction-protocol"
domain: "intake"
category: "extraction"
tags: ["extraction", "materials", "website", "pitch-deck", "css", "chrome-mcp", "confidence"]
depends_on: ["intake-guide"]
token_count_approx: 2000
version: "1.0"
last_updated: "2026-02-21"
status: "active"
summary: >-
  How to extract design decisions from existing materials. 6 source types
  (website, pitch deck, social media, competitor, print, email signature).
  Chrome MCP CSS extraction commands. Confidence levels (High/Medium/Low).
  Maps extractions to token groups.
---

# Material Extraction Protocol

How to extract design decisions from existing brand materials. This protocol is executed by the agent during Phase 0B, not answered by the user. The user provides access to materials; the agent extracts, maps, and presents for validation.

## General Extraction Principles

1. **Extract, don't ask.** If a value is visible in materials, capture it rather than asking the user.
2. **Assign confidence levels.** Every extracted value gets High/Medium/Low confidence.
3. **Map to token groups.** Every extracted value maps to one or more token groups.
4. **Present for validation.** Extracted values are shown to the user in Q0.4 for confirmation.
5. **Note inconsistencies.** If the same element (e.g., heading font) differs across materials, flag it.

### Confidence Levels

| Level | Definition | Treatment |
|---|---|---|
| **High** | Consistent across 2+ materials. Clear, unambiguous value. | Use as default. Present for confirmation. |
| **Medium** | Found in one material. Reasonable assumption but unverified. | Use tentatively. Flag for user review. |
| **Low** | Implied or inferred (e.g., "looks like it might be Inter"). Inconsistent across materials. | Do not use without confirmation. Ask the user. |

---

## Source Type 1: Website

### What to Extract

| Element | How to Find | Token Group | Method |
|---|---|---|---|
| **Background colors** | `<body>`, `<main>`, `<section>` backgrounds | `semantic.color.surface.*` | Screenshot + inspect CSS `background-color` via Chrome MCP or WebFetch |
| **Text colors** | `<p>`, `<span>`, `<li>` color values | `semantic.color.text.*` | Inspect CSS `color` on body text elements |
| **Heading colors** | `<h1>` through `<h4>` color values | `semantic.color.text.heading` | Inspect CSS `color` on heading elements |
| **Link/CTA colors** | `<a>` color, button backgrounds | `semantic.color.brand.secondary`, `component.button.*` | Inspect link and button CSS |
| **Heading font family** | `<h1>` through `<h4>` font-family | `primitives.font.family.heading` | Inspect CSS `font-family` |
| **Body font family** | `<p>`, `<span>` font-family | `primitives.font.family.body` | Inspect CSS `font-family` |
| **Font sizes** | Various elements | `primitives.font.size.*` | Inspect computed `font-size` for h1, h2, h3, p, small |
| **Font weights** | Various elements | `primitives.font.weight.*` | Inspect computed `font-weight` |
| **Line heights** | Body text, headings | `primitives.font.lineHeight.*` | Inspect computed `line-height` |
| **Spacing patterns** | Section margins, padding, gaps | `primitives.space.*` | Inspect margins/padding. Look for harmonic scale. |
| **Border radius** | Cards, buttons, input fields | `primitives.radius.*` | Inspect `border-radius` on interactive elements |
| **Shadows** | Cards, dropdowns, modals | `primitives.shadow.*` | Inspect `box-shadow` |
| **Button styles** | CTAs, navigation, forms | `component.button.*` | Full CSS capture: bg, color, border, radius, padding, font |
| **Card styles** | Content cards, feature boxes | `component.card.*` | bg, border, radius, shadow, padding |
| **Logo** | Header, footer | Logo specs | Size, placement, variant (color/mono), surrounding space |
| **Navigation pattern** | Primary nav | Template reference | Structure (horizontal, hamburger, sidebar) |
| **Image style** | Hero images, section images | Photography direction | Subject matter, treatment (color, tinted, duotone) |

### Extraction Commands (Chrome MCP)

```javascript
// Extract primary computed styles
const styles = getComputedStyle(document.body);
const data = {
  bgColor: styles.backgroundColor,
  textColor: styles.color,
  fontFamily: styles.fontFamily,
  fontSize: styles.fontSize,
  lineHeight: styles.lineHeight
};
// Repeat for h1, h2, h3, a, button elements
```

### WebFetch Alternative
If Chrome MCP is unavailable, use WebFetch to get page HTML, then extract:
- `<link>` tags for font references (Google Fonts URLs reveal font families)
- Inline styles and `<style>` blocks for color values
- Class names that suggest frameworks (Tailwind classes reveal design system)

---

## Source Type 2: Pitch Deck / Presentation

### What to Extract

| Element | Where to Look | Token Group | Confidence |
|---|---|---|---|
| **Slide background** | First 3 slides, closing slide | `semantic.color.surface.*` | High (if consistent) |
| **Heading font** | Slide titles | `primitives.font.family.heading` | High |
| **Heading size** | Title text | `primitives.font.size.*` | Medium (may be slide-specific) |
| **Heading color** | Title text | `semantic.color.text.heading` | High (if consistent) |
| **Body font** | Bullet points, content text | `primitives.font.family.body` | Medium |
| **Body size** | Content text | `primitives.font.size.*` | Medium |
| **Accent/CTA color** | Highlights, buttons, colored elements | `semantic.color.brand.secondary` | High |
| **Chart colors** | Any data visualizations | `semantic.color.data.*` | High |
| **Chart style** | Axes, gridlines, labels | `component.chart.*` | Medium |
| **Table styling** | Comparison tables | `component.table.*` | High (if present) |
| **Logo placement** | Logo position on slides | `component.header.*`, `component.footer.*` | High |
| **Logo variant** | Color vs. mono vs. reversed | Logo specs | High |
| **Layout alignment** | Content alignment pattern | Slide master grid | Medium |
| **Aspect ratio** | Slide dimensions | Slide master dimensions | High |
| **Metric callout style** | Key numbers display | `component.card.metric` | Medium |
| **White space** | Margin density | `spacing.layout.*` | Medium |

### Analysis Approach
1. Read the file if it's in a readable format (PDF, PPTX text extraction)
2. If image-based, take screenshots and analyze visually
3. Focus on the first 5 slides (they establish the visual system)
4. Look for the "key metric" slide to understand data visualization approach
5. Check consistency between first and last slides (cover and closing often differ)

---

## Source Type 3: Social Media Profiles

### What to Extract

| Element | Where to Look | Token Group |
|---|---|---|
| **Profile avatar** | Profile picture | Logo variant (icon/square) |
| **Banner image** | Cover photo/banner | Color palette, photography style |
| **Post visual style** | Recent 5-10 posts | Color palette, typography in graphics |
| **Content tone** | Post text | Tone alignment with verbal brand |
| **Hashtag/branding** | Post text, graphics | Brand terminology |

### LinkedIn-Specific
- Company page banner reveals brand colors and composition preference
- Posts with branded graphics reveal the working design system
- Engagement patterns suggest what visual style resonates

### Analysis Approach
1. WebFetch the LinkedIn company page URL
2. Extract banner dominant colors
3. Analyze recent posts with graphics for color/font patterns
4. Note inconsistencies between profile branding and post graphics (common)

---

## Source Type 4: Competitor Websites

### What to Extract

| Element | Purpose | How It Feeds Brand-Book |
|---|---|---|
| **Color palette** | Visual landscape mapping | Differentiation: avoid competitor primary colors |
| **Typography** | Industry norm detection | Benchmark: same font = commodity, different = differentiated |
| **Visual personality** | Competitive positioning | Inform Q0.10 (emotional response) recommendations |
| **Photography style** | Category conventions | Inform Q7.1 (photography style) recommendations |
| **Layout patterns** | Industry expectations | Inform slide/document template defaults |

### Analysis Approach
1. Analyze 2-3 key competitors from brand-config `competitor_names` or ask user
2. For each: WebFetch homepage, extract primary color, font, and visual personality
3. Create comparison table: Brand vs. Competitor A vs. Competitor B vs. Competitor C
4. Identify: where does the brand look similar (risk of confusion) vs. different (differentiated)?

---

## Source Type 5: Print Materials

### What to Extract
- Paper stock and finish (reveals quality level: premium matte, standard gloss)
- Color accuracy (CMYK vs. RGB differences)
- Typography legibility at print size
- Logo print variant (single-color, full-color)
- Margin and bleed specifications

### Analysis Approach
If user provides scans/photos:
1. Extract dominant colors (note: photo capture may shift hues)
2. Identify font families by visual matching
3. Note print-specific elements (bleed, fold marks, registration marks)
4. Flag print colors that may differ from digital (Pantone/CMYK vs. hex)

---

## Source Type 6: Email Signatures / Templates

### What to Extract
| Element | Token Group |
|---|---|
| Logo variant used | Logo specs |
| Font in signature | Typography (may differ from brand font if email-safe) |
| Colors (links, dividers, background) | Color palette, component styles |
| Layout structure | Document template reference |
| Social media icons | Icon style preference |

---

## Extraction Output Format

After analyzing all available materials, produce an extraction summary table for Q0.4:

```markdown
## Extraction Summary for {brand_name}

### Colors
| Token | Extracted Value | Source | Confidence | Notes |
|---|---|---|---|---|
| Primary | #1B365D | Website header, Deck slides 1-5 | High | Consistent across 2 sources |
| Secondary | #22C55E | Website CTAs, Deck highlights | High | |
| Neutral | #64748B | Website body text | Medium | Only one source |
| Surface light | #F8FAFC | Website background | Medium | |
| Surface dark | #0F172A | Deck slide 1, 16 | Medium | Opening/closing slides only |

### Typography
| Token | Extracted Value | Source | Confidence | Notes |
|---|---|---|---|---|
| Heading font | Inter | Website h1-h3 | High | Google Fonts link confirmed |
| Body font | Inter | Website body text | High | Same family |
| Heading weight | 600 (Semibold) | Website h1 | Medium | May be 700 in deck |
| Body size | 16px | Website base | High | |

### Layout
| Token | Extracted Value | Source | Confidence | Notes |
|---|---|---|---|---|
| Slide aspect ratio | 16:9 | Deck | High | |
| Content alignment | Left-aligned | Website, Deck | High | Consistent |
| Border radius | 8px | Website buttons, cards | Medium | |
| Base spacing | 4px scale (16px, 24px, 32px visible) | Website | Low | Inferred from patterns |

### Components
| Token | Extracted Value | Source | Confidence | Notes |
|---|---|---|---|---|
| Button style | Filled, rounded corners | Website CTAs | High | |
| Table style | Minimal borders | Deck comparison slides | Medium | |
| Logo placement | Top-left | Website, Deck | High | |

### Gaps Identified
1. No monospace font found in materials
2. No data visualization colors (no charts in deck)
3. No dark mode variant on website
4. No video content to extract motion preferences from
5. No email signature template provided
```

### Presenting to User

Present the extraction summary at Q0.4 and ask:
> "From your [website/deck/materials], I've extracted these design decisions. For each row, tell me:
> (a) **Correct and keep** -- I'll lock this value into the token system
> (b) **Close but adjust** -- tell me how to change it
> (c) **Wrong** -- I want something different
>
> For gaps identified, I'll ask targeted questions in the relevant phase."

---

## Handling Material Conflicts

When the same element has different values across materials:

1. **Website vs. Deck:** Website usually has the more intentional design system. Deck may be older or created ad hoc.
2. **Professional design vs. DIY:** If one material was professionally designed and another was DIY, prioritize the professional version.
3. **Newer vs. older:** More recent materials likely reflect current brand direction.
4. **Present both:** "Your website uses Inter but your deck uses Arial. Which represents your intended brand?"

## No Materials Available

If the user has zero existing materials (brand-new company):
1. Skip Phase 0B research tasks (except R0.4 competitor analysis and R0.5 font check)
2. Skip Q0.3, Q0.4, Q0.5, Q0.6 (nothing to extract or validate)
3. Increase reliance on design-recommendations-engine
4. Q0.8 answer is likely (c) "No preferences -- recommend everything"
5. Proceed directly to Phase 1 with engine recommendations for every question
