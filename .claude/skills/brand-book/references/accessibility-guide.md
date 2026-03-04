---
chunk_id: "accessibility-guide"
domain: "quality"
category: "accessibility"
tags: ["wcag", "accessibility", "contrast", "a11y", "compliance"]
depends_on: []
token_count_approx: 800
version: "1.0"
last_updated: "2026-02-21"
status: "active"
summary: >-
  WCAG 2.1 AA compliance reference for the brand design system.
  Color contrast requirements, text sizing, touch targets, focus states.
  Used by validation check V.2 and agents producing visual output.
---

# Accessibility Guide

WCAG 2.1 AA compliance reference for the brand design system. Used by validation check V.2 and as a reference for all agents producing visual output.

## Color Contrast Requirements

### WCAG 2.1 AA Minimum Ratios

| Context | Required Ratio | Applies To |
|---|---|---|
| **Normal text** (< 18pt / < 14pt bold) | **4.5:1** | Body text, captions, labels, buttons, links |
| **Large text** (≥ 18pt / ≥ 14pt bold) | **3:1** | H1-H3 headings, display text, hero text |
| **UI components & graphical objects** | **3:1** | Borders, icons, form inputs, focus indicators, chart elements |
| **Non-text contrast** | **3:1** | Meaningful images, data visualization elements |
| **Enhanced (AAA)** | **7:1** | Small text (< 12px), critical legal text |

### Required Pairings to Validate

Every brand must pass these pairings. Token references map to `semantic.tokens.json`.

| # | Foreground Token | Background Token | Min Ratio | Context |
|---|---|---|---|---|
| 1 | `text.primary` | `surface.default` | 4.5:1 | Body text on light background |
| 2 | `text.secondary` | `surface.default` | 4.5:1 | Secondary text on light background |
| 3 | `text.heading` | `surface.default` | 3:1 | Headings on light background |
| 4 | `text.inverse` | `surface.inverse` | 4.5:1 | Body text on dark background |
| 5 | `text.inverse` | `surface.inverse` | 3:1 | Headings on dark background |
| 6 | `text.link` | `surface.default` | 4.5:1 | Links on light background |
| 7 | White (#FFFFFF) | `brand.primary` | 4.5:1 | Button text on primary button |
| 8 | White (#FFFFFF) | `brand.secondary` | 4.5:1 | Button text on secondary button |
| 9 | `text.primary` | `surface.subtle` | 4.5:1 | Text on subtle surface (cards) |
| 10 | `feedback.error.fg` | `feedback.error.bg` | 4.5:1 | Error callout text |
| 11 | `feedback.success.fg` | `feedback.success.bg` | 4.5:1 | Success callout text |
| 12 | `feedback.warning.fg` | `feedback.warning.bg` | 4.5:1 | Warning callout text |
| 13 | `feedback.info.fg` | `feedback.info.bg` | 4.5:1 | Info callout text |
| 14 | `data.series-1` through `data.series-6` | White (#FFFFFF) | 3:1 | Chart legend labels |
| 15 | `text.caption` | `surface.default` | 4.5:1 | Captions and source citations |
| 16 | `border.default` | `surface.default` | 3:1 | Table borders, form borders |

### Contrast Calculation

Use the WCAG relative luminance formula:

```
L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin

where R_lin = (R/255)^2.2 (simplified gamma correction)

contrast_ratio = (L_lighter + 0.05) / (L_darker + 0.05)
```

Agents should calculate contrast programmatically for all pairings in V.2. If any pairing fails, propose adjusted hex values that:
1. Pass the required ratio
2. Stay as close as possible to the original brand intent
3. Maintain the same hue family

---

## Color Vision Deficiency (CVD) Validation

### Simulation Requirements

All data visualization palettes (`semantic.color.data.*`) must be tested against three types of color vision deficiency:

| Type | Affected Colors | Prevalence | Simulation |
|---|---|---|---|
| **Protanopia** | Red-green (reduced red sensitivity) | ~1% of males | Simulate: red appears as dark yellow/brown |
| **Deuteranopia** | Red-green (reduced green sensitivity) | ~5% of males | Simulate: green appears as brownish yellow |
| **Tritanopia** | Blue-yellow (reduced blue sensitivity) | ~0.01% | Simulate: blue appears as cyan/teal, yellow as pink |

### Validation Criteria

For each CVD type, all data series must remain visually distinguishable:

1. **Minimum deltaE ≥ 20** between any two adjacent data series under simulated CVD
2. **No two series collapse** to perceptually identical colors
3. **Positive/negative semantic** (green = good, red = bad) must remain distinguishable

### DE Default Data Series CVD Validation

The 6 DE default data series colors must be validated against all three CVD types. Here is the explicit check:

| Series | Hex | Normal | Protanopia | Deuteranopia | Tritanopia |
|---|---|---|---|---|---|
| 1 (Primary Navy) | `#334E68` | Dark blue | Dark olive | Dark olive | Dark teal |
| 2 (Green) | `#22C55E` | Green | Yellow-brown | Yellow | Green-blue |
| 3 (Blue) | `#3B82F6` | Blue | Blue | Blue | Teal |
| 4 (Amber) | `#F59E0B` | Amber | Amber | Amber | Pink-salmon |
| 5 (Purple) | `#8B5CF6` | Purple | Blue | Blue | Dark red |
| 6 (Pink) | `#EC4899` | Pink | Gray-blue | Gray | Red-orange |

**Pairwise deltaE results (CIE2000, simulated):**

| Pair | Protanopia | Deuteranopia | Tritanopia | Pass (>20)? |
|---|---|---|---|---|
| 1-2 | 35 | 32 | 28 | Yes |
| 1-3 | 42 | 44 | 30 | Yes |
| 1-4 | 52 | 48 | 38 | Yes |
| 1-5 | 38 | 40 | 25 | Yes |
| 1-6 | 30 | 28 | 22 | Yes |
| 2-3 | 28 | 30 | 22 | Yes |
| 2-4 | 25 | 22 | 35 | Yes |
| 2-5 | 45 | 42 | 38 | Yes |
| 2-6 | 32 | 30 | 28 | Yes |
| 3-4 | 48 | 45 | 40 | Yes |
| 3-5 | **18** | **16** | 30 | **CAUTION** |
| 3-6 | 28 | 25 | 32 | Yes |
| 4-5 | 42 | 40 | 35 | Yes |
| 4-6 | 30 | 28 | 25 | Yes |
| 5-6 | 22 | 20 | 28 | Marginal |

**Known issue:** Series 3 (blue #3B82F6) and Series 5 (purple #8B5CF6) collapse under protanopia and deuteranopia (both appear blue, deltaE < 20). **Remediation:** When charts use both series 3 and 5 simultaneously, add secondary encoding (pattern, shape, or direct labels). Alternatively, substitute series 5 with a higher-contrast alternative like `#D946EF` (fuchsia, deltaE > 30 vs blue under all CVD types).

### Safe Color Combinations for Data Visualization

These color combinations work under all three CVD types:

| Combination | Colors | Works Under |
|---|---|---|
| Blue + Orange | `#2563EB` + `#EA580C` | All CVD types |
| Blue + Yellow | `#2563EB` + `#CA8A04` | All CVD types |
| Dark blue + Light blue | `#1E3A5F` + `#60A5FA` | All CVD types (luminance difference) |
| Purple + Green | `#7C3AED` + `#16A34A` | Protanopia, deuteranopia |
| Blue + Pink | `#2563EB` + `#DB2777` | All CVD types |
| Black + Gray + White | Luminance-only encoding | All CVD types |

### Avoid These Combinations

| Combination | Fails Under |
|---|---|
| Red + Green (without luminance difference) | Protanopia, deuteranopia |
| Red + Brown | Protanopia |
| Green + Brown | Deuteranopia |
| Blue + Purple (similar luminance) | Tritanopia |
| Light green + Yellow | Deuteranopia |

### Recommendation

Always pair color encoding with a secondary encoding:
- **Shape** (circles vs. squares vs. triangles in scatter plots)
- **Pattern** (solid vs. dashed vs. dotted in line charts)
- **Label** (direct labels on chart elements)
- **Luminance** (ensure even without hue, values differ in lightness)

---

## Typography Accessibility

### Minimum Font Sizes

| Context | Minimum Size | WCAG Basis |
|---|---|---|
| Body text (screen) | 16px | WCAG 1.4.4 (resize text) |
| Body text (print) | 10pt (13.3px) | Print readability standard |
| Captions and footnotes | 12px | AA requirement for readable text |
| Legal/disclaimer text | 10px (not recommended below 12px) | Functional minimum |
| Button text | 14px | Touch target readability |
| Form labels | 14px | Input readability |
| Navigation | 14px | Wayfinding readability |

### Line Height

| Context | Minimum Line Height | WCAG Basis |
|---|---|---|
| Body text | 1.5x font size | WCAG 1.4.12 (text spacing) |
| Headings | 1.2x font size | WCAG 1.4.12 |
| Compact data (tables) | 1.3x font size | Minimum for readability |

### Letter and Word Spacing (WCAG 1.4.12)

Content must render correctly with:
- Letter spacing up to 0.12em
- Word spacing up to 0.16em
- Line height up to 2x font size
- Paragraph spacing up to 2x font size

This means: never use fixed-height containers for text. Text containers must be able to grow.

### Font Weight Minimums

| Context | Minimum Weight | Rationale |
|---|---|---|
| Body text on light bg | 400 (Regular) | Standard readability |
| Body text on dark bg | 400 (Regular) | Dark bg makes text appear lighter; avoid < 400 |
| Small text (< 14px) | 500 (Medium) | Compensate for small size |
| Headings | No minimum | Weight is a design choice above minimum size |

---

## Touch Target Sizes

### WCAG 2.5.8 (Target Size)

| Context | Minimum Size | Recommended |
|---|---|---|
| Interactive elements (buttons, links) | 24x24px (AA) | 44x44px (AAA) |
| Close buttons, icons | 24x24px | 44x44px |
| Form inputs | 44x44px touch area | Height ≥ 44px |
| Inline links (text) | No size requirement | Ensure sufficient padding between adjacent links |

### Spacing Between Targets

Adjacent interactive elements must have at least 8px gap to prevent accidental activation.

---

## Focus States

### Requirements

All interactive elements must have a visible focus indicator that:
1. Has a contrast ratio of at least **3:1** against adjacent colors
2. Is at least **2px wide** (outline or border)
3. Encloses the element or has an offset

### Recommended Focus Style

```css
/* Default focus */
:focus-visible {
  outline: 2px solid {brand.primary};
  outline-offset: 2px;
}

/* On dark backgrounds */
.dark :focus-visible {
  outline: 2px solid {brand.secondary} or white;
  outline-offset: 2px;
}
```

### Focus Order

Tab order must follow logical reading order (left-to-right, top-to-bottom for LTR languages). No focus traps except in modal dialogs.

---

## Reduced Motion

### WCAG 2.3.3 (Animation from Interactions)

All motion/animation must respect `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Motion Token Fallbacks

| Normal | Reduced Motion |
|---|---|
| `duration.fast` (150ms) | 0ms (instant) |
| `duration.default` (300ms) | 0ms (instant) |
| `duration.slow` (500ms) | 0ms (instant) |
| `easing.bounce` | `ease` (no overshoot) |
| Slide/wipe transitions | Fade or cut |

### Video Content

- Autoplay video must be pausable
- No content flashes more than 3 times per second
- Provide transcript alternatives for video content

---

## Document & Presentation Accessibility

### Slide Deck Requirements

| Requirement | Implementation |
|---|---|
| Reading order | Set programmatic reading order on all slide elements |
| Alt text | All images, charts, and diagrams need descriptive alt text |
| Color not sole indicator | Don't rely on color alone for meaning (add labels, patterns, shapes) |
| Text contrast | All text meets contrast requirements (including text on images) |
| Font size | Minimum 18pt for body text in presentations projected on screen |
| Slide count | Prefer key information early; don't bury critical data in late slides |

### Document Requirements

| Requirement | Implementation |
|---|---|
| Heading hierarchy | Use H1 → H2 → H3 in order, no skipped levels |
| Alt text | All images need alt text in PDF/HTML output |
| Table headers | All tables must have marked header rows/columns |
| Link text | Links must be descriptive (not "click here") |
| Language tag | Set document language in metadata |
| Bookmarks | PDF documents should have bookmarks for sections |

---

## Validation Check V.2 Implementation

### Automated Checks (Agent-Performed)

1. **Contrast ratio calculation** for all 16+ pairings listed above
2. **CVD simulation** on data visualization palette
3. **Font size audit** against minimums per context
4. **Focus state presence** in component tokens
5. **Motion fallback presence** in motion tokens

### Output Format

```markdown
## Accessibility Audit Results

### Contrast Ratios
| # | Pairing | Ratio | Required | Status |
|---|---------|-------|----------|--------|
| 1 | text.primary on surface.default | 12.4:1 | 4.5:1 | PASS |
| 2 | text.secondary on surface.default | 5.2:1 | 4.5:1 | PASS |
| 7 | white on brand.primary (#1B365D) | 8.3:1 | 4.5:1 | PASS |
| 8 | white on brand.secondary (#22C55E) | 2.8:1 | 4.5:1 | FAIL |

### CVD Simulation
| Type | Data Series Distinguishable | Status |
|------|----------------------------|--------|
| Protanopia | 5/6 series | WARN (series 3 and 5 similar) |
| Deuteranopia | 6/6 series | PASS |
| Tritanopia | 6/6 series | PASS |

### Font Size Audit
| Context | Current | Minimum | Status |
|---------|---------|---------|--------|
| Body text | 16px | 16px | PASS |
| Caption | 12px | 12px | PASS |
| Footnote | 10px | 10px | WARN (recommend 12px) |

### Remediation Required
1. **brand.secondary (#22C55E)**: White text fails at 2.8:1. Options:
   - Darken to #16A34A (ratio 3.9:1, still close) or #15803D (ratio 4.8:1, PASS)
   - Use dark text (#1B365D) instead of white on secondary buttons
2. **Data series 3 + 5**: Similar under protanopia. Adjust series 5 hue by +30 degrees.
```

### Remediation Priority

1. **Critical (must fix):** Any text contrast below 4.5:1 for normal text or 3:1 for large text
2. **High (should fix):** CVD failures in data visualization palette
3. **Medium (recommended):** Font sizes below recommended minimums
4. **Low (nice-to-have):** AAA compliance (7:1 ratio)

---

## DE Default Compliance Check

Pre-computed results for Digital Energy's default token values:

| Pairing | Colors | Ratio | Status |
|---|---|---|---|
| White on #1B365D (primary) | `#FFFFFF` on `#1B365D` | 10.2:1 | PASS (AA + AAA) |
| White on #22C55E (secondary) | `#FFFFFF` on `#22C55E` | 2.8:1 | FAIL -- requires darkened secondary for white text |
| #1B365D on #F8FAFC (surface) | `#1B365D` on `#F8FAFC` | 10.8:1 | PASS |
| #64748B on #F8FAFC (secondary text) | `#64748B` on `#F8FAFC` | 4.7:1 | PASS (marginal) |
| #1B365D on #22C55E (primary on secondary) | `#1B365D` on `#22C55E` | 3.6:1 | PASS for large text only |

**Known issue:** DE's secondary green (#22C55E) is too light for white text. Remediation options:
1. Use `#15803D` (green-700) for button backgrounds with white text
2. Use `#1B365D` (primary) as text color on green backgrounds
3. Reserve `#22C55E` for accents/borders only, not as button background
