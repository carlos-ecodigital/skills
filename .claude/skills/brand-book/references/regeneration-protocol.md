---
chunk_id: "regeneration-protocol"
domain: "export"
category: "automation"
tags: ["regeneration", "export", "tokens", "transform", "validation"]
depends_on: ["completeness-matrix", "accessibility-guide"]
token_count_approx: 3000
version: "1.0"
last_updated: "2026-02-21"
status: "active"
summary: >-
  Token-to-export transformation rules for rebuilding all 4 code exports
  (Tailwind, CSS, Figma, Remotion) from token source files. Includes
  reference resolution algorithm, per-export mapping tables, and 9-point
  validation checklist. Agent follows this when tokens change.
---

# Export Regeneration Protocol

## Activation

**Triggers:**
- User says "regenerate exports," "update exports," or invokes `/brand-book regenerate`
- After any Create Brand intake phase completes (agent should offer: "Tokens updated. Regenerate exports?")
- After manual token file edits

**Pre-conditions:**
1. Brand config loaded
2. All 3 token files exist and parse as valid JSON

---

## Regeneration Sequence

Strict order — later exports may depend on patterns established in earlier ones.

1. **Load sources:** Read `primitives.tokens.json`, `semantic.tokens.json`, `component.tokens.json`
2. **Build resolution index:** Flatten all tokens into a lookup map (token path → concrete value)
3. **Regenerate** `exports/tailwind-config.js` (depends on primitives + semantic)
4. **Regenerate** `exports/css-variables.css` (depends on semantic + primitives)
5. **Regenerate** `exports/figma-variables.json` (depends on all 3 tiers)
6. **Regenerate** `exports/remotion-theme.ts` (depends on semantic + primitives + brand-config)
7. **Run validation checklist** (9 checks)
8. **Report results** to user

---

## Reference Resolution Algorithm

Token `$value` fields contain either literals or references. Resolve all references before writing exports.

### Resolution Rules

1. **Literal value** — starts with `#` (hex), is a number, or is a CSS string (e.g., `"Inter"`, `"0 1px 3px..."`):
   - Use directly. No resolution needed.

2. **Reference** — format `{group.subgroup.key}`:
   - Look up in the resolution index
   - If the target is also a reference, resolve recursively (max depth 3)
   - If unresolvable after 3 levels: flag as `BROKEN_REF:{original_path}`

3. **Mixed value** — contains both literals and references (e.g., gradients: `"linear-gradient(135deg, {color.primary.700} 0%, ...)"`):
   - Resolve each `{...}` reference inline, keep surrounding literal text

### Building the Resolution Index

```
For each tier (primitives → semantic → component):
  Walk the JSON tree depth-first
  For each leaf node with "$value":
    key = dot-separated path from root (e.g., "color.primary.700")
    value = the "$value" content
    Add to index: { key → value }

Then resolve all reference values:
  For each entry where value matches /{[^}]+}/:
    Replace {ref} with index[ref]
    If index[ref] is also a reference, resolve again
    Track depth, abort at 3
```

---

## Transformation Rules: Tailwind Config

**Source:** `primitives.tokens.json` + `semantic.tokens.json`
**Output:** `exports/tailwind-config.js`
**Wrapper:** `module.exports = { ... }` with JSDoc header

### Color Mappings

| Tailwind Key | Source Token Path | Transform |
|---|---|---|
| `colors.primary.{shade}` | `color.primary.{shade}.$value` | Direct hex string |
| `colors.secondary.{shade}` | `color.secondary.{shade}.$value` | Direct hex string |
| `colors.neutral.{shade}` | `color.neutral.{shade}.$value` | Direct hex string |
| `colors.accent.{shade}` | `color.accent.{shade}.$value` | Direct hex string |
| `colors.error.{shade}` | `color.error.{shade}.$value` | Direct hex string |
| `colors.tertiary.{shade}` | `color.tertiary.{shade}.$value` | Direct hex string |
| `colors.info.{shade}` | `color.info.{shade}.$value` | Direct hex string |
| `colors.success.{shade}` | `color.success.{shade}.$value` | Direct hex string |

Shades: `50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950` (11 per family)

| Tailwind Key | Source Token Path | Transform |
|---|---|---|
| `colors['data-1']` through `['data-6']` | `semantic: color.data.series-{N}` | Resolve ref → hex |
| `colors['audience-{id}']` | `semantic: color.audience.{id}` | Resolve ref → hex. IDs from brand-config `audience_segments[].id` |
| `colors.white` | `color.white.$value` | Direct hex |
| `colors.black` | `color.black.$value` | Direct hex |

### Typography Mappings

| Tailwind Key | Source Token Path | Transform |
|---|---|---|
| `fontFamily.heading` | `font.family.heading.$value` | `['{value}', 'system-ui', 'sans-serif']` |
| `fontFamily.body` | `font.family.body.$value` | `['{value}', 'system-ui', 'sans-serif']` |
| `fontFamily.mono` | `font.family.mono.$value` | `['{value}', 'monospace']` |
| `fontSize.{key}` | `font.size.{key}.$value` + `font.lineHeight.{key}.$value` | `['{size}px', { lineHeight: '{lh}' }]` |
| `fontWeight.{key}` | `font.weight.{key}.$value` | Direct number |
| `lineHeight.{key}` | `font.lineHeight.{key}.$value` | Direct number string |
| `letterSpacing.{key}` | `font.letterSpacing.{key}.$value` | Direct em string |

Font size keys: `xs, sm, base, lg, xl, 2xl, 3xl, 4xl, 5xl`
Font weight keys: `light, regular, medium, semibold, bold`

### Spacing & Layout Mappings

| Tailwind Key | Source Token Path | Transform |
|---|---|---|
| `spacing.{key}` | `space.{key}.$value` | `'{value}px'` |
| `borderRadius.{key}` | `radius.{key}.$value` | `'{value}px'` (or `'9999px'` for `full`) |
| `boxShadow.{key}` | `shadow.{key}.$value` | Direct CSS shadow string |
| `transitionDuration.{key}` | `duration.{key}.$value` | `'{value}ms'` |
| `transitionTimingFunction.{key}` | `easing.{key}.$value` | Direct CSS timing function |
| `zIndex.{key}` | `elevation.zindex.{key}.$value` | Direct number |
| `screens.{key}` | `breakpoint.{key}.$value` | `'{value}px'` |

Spacing keys: `0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48`
Radius keys: `none, sm, md, lg, xl, full`
Shadow keys: `xs, sm, md, lg, xl`
Duration keys: `fast, normal, slow, slower, slowest`
Easing keys: `default, in, out, bounce`
Z-index keys: `base, dropdown, sticky, fixed, modal-backdrop, modal, popover, tooltip, toast, max`
Breakpoint keys: `sm, md, lg, xl`

### Preservation Rules

- Keep the `module.exports = { ... }` wrapper
- Keep the JSDoc header (lines 1-12), update the date comment
- Keep section comments (`// --- ... ---` and `// primitives.color...`)
- Regenerate all values from tokens; do not preserve old values

---

## Transformation Rules: CSS Variables

**Source:** `semantic.tokens.json` + `primitives.tokens.json`
**Output:** `exports/css-variables.css`
**Wrapper:** `:root { ... }` with section headers

### Semantic Color Variables

| CSS Variable | Source (semantic) | Transform |
|---|---|---|
| `--color-brand-primary` | `color.brand.primary` | Resolve → hex |
| `--color-brand-secondary` | `color.brand.secondary` | Resolve → hex |
| `--color-brand-accent` | `color.brand.accent` | Resolve → hex |
| `--color-surface-default` | `color.surface.default` | Resolve → hex |
| `--color-surface-subtle` | `color.surface.subtle` | Resolve → hex |
| `--color-surface-strong` | `color.surface.strong` | Resolve → hex |
| `--color-surface-inverse` | `color.surface.inverse` | Resolve → hex |
| `--color-surface-brand` | `color.surface.brand` | Resolve → hex |
| `--color-text-primary` | `color.text.primary` | Resolve → hex |
| `--color-text-secondary` | `color.text.secondary` | Resolve → hex |
| `--color-text-heading` | `color.text.heading` | Resolve → hex |
| `--color-text-link` | `color.text.link` | Resolve → hex |
| `--color-text-inverse` | `color.text.inverse` | Resolve → hex |
| `--color-text-caption` | `color.text.caption` | Resolve → hex |
| `--color-border-default` | `color.border.default` | Resolve → hex |
| `--color-border-strong` | `color.border.strong` | Resolve → hex |
| `--color-border-brand` | `color.border.brand` | Resolve → hex |
| `--color-feedback-{type}-fg` | `color.feedback.{type}.fg` | Resolve → hex |
| `--color-feedback-{type}-bg` | `color.feedback.{type}.bg` | Resolve → hex |
| `--color-data-series-{N}` | `color.data.series-{N}` | Resolve → hex |
| `--color-audience-{id}` | `color.audience.{id}` | Resolve → hex |

Feedback types: `error, success, warning, info`
Data series: `1` through `6`
Audience IDs: from brand-config `audience_segments[].id`

### Typography Variables (from primitives)

| CSS Variable | Source (primitives) | Transform |
|---|---|---|
| `--font-family-heading` | `font.family.heading` | `'{value}', system-ui, sans-serif` |
| `--font-family-body` | `font.family.body` | `'{value}', system-ui, sans-serif` |
| `--font-family-mono` | `font.family.mono` | `'{value}', monospace` |
| `--font-weight-{key}` | `font.weight.{key}` | Direct number |
| `--font-size-{key}` | `font.size.{key}` | `{value}px` |
| `--line-height-{key}` | `font.lineHeight.{key}` | Direct decimal |
| `--letter-spacing-{key}` | `font.letterSpacing.{key}` | Direct em value |

### Layout Variables (from primitives)

| CSS Variable | Source (primitives) | Transform |
|---|---|---|
| `--space-{key}` | `space.{key}` | `{value}px` |
| `--radius-{key}` | `radius.{key}` | `{value}px` |
| `--shadow-{key}` | `shadow.{key}` | Direct CSS shadow string |
| `--duration-{key}` | `duration.{key}` | `{value}ms` |
| `--easing-{key}` | `easing.{key}` | Direct CSS timing function |
| `--z-{key}` | `elevation.zindex.{key}` | Direct number |
| `--breakpoint-{key}` | `breakpoint.{key}` | `{value}px` |

### Preservation Rules

- Keep `:root { ... }` wrapper
- Keep JSDoc header, update date
- Keep section comment blocks (`/* ====... */`)
- Keep `@media (prefers-reduced-motion: reduce)` block at end (override durations to 0ms)
- Regenerate all values from resolved tokens

---

## Transformation Rules: Figma Variables

**Source:** All 3 token tiers
**Output:** `exports/figma-variables.json`
**Wrapper:** `{ "$schema": "figma-variable-collections", "collections": [...] }`

### Three Collections

**1. Primitives Collection**
- Mode: `["Default"]`
- Path transform: dots → slashes (`color.primary.50` → `color/primary/50`)
- Type mapping: `$type "color"` → `"COLOR"`, numeric → `"FLOAT"`, string → `"STRING"`
- Values: all literal (no references in primitives)
- Include: all 8 color families, typography, spacing, radius, shadows, duration, easing, z-index, breakpoints

**2. Semantic Collection**
- Modes: `["Light", "Dark"]`
- Path transform: same dot-to-slash
- Values: resolve all `$value` references to final hex/number
- Dark mode: use `dark.*` token variants if present in semantic tokens; otherwise invert Light values
- Include: brand colors, surface, text, border, feedback, data series, audience, focus, typography composites, spacing roles

**3. Component Collection**
- Mode: `["Default"]`
- Path transform: dots → slashes
- Values: resolve all references through semantic → primitives chain
- Include: button (3 variants × 5 states × 8 props), card, input, table, callout, badge
- Format: `{component}/{variant}/{state}/{property}`

### Variable Entry Format

```json
{
  "name": "color/primary/700",
  "type": "COLOR",
  "value": "#1B365D",
  "description": "Brand primary -- core identity color"
}
```

For semantic with modes:
```json
{
  "name": "color/surface/default",
  "type": "COLOR",
  "resolvedValue": { "Light": "#F8FAFC", "Dark": "#0D1F30" },
  "description": "Default page background"
}
```

### Preservation Rules

- Keep `$schema` and `$description` fields
- Keep `$usage` instructions
- Regenerate all collections and variables from tokens
- Maintain alphabetical sort within each collection

---

## Transformation Rules: Remotion Theme

**Source:** `semantic.tokens.json` + `primitives.tokens.json` + brand-config
**Output:** `exports/remotion-theme.ts`
**Wrapper:** TypeScript interfaces + `export const brandTheme: BrandTheme = { ... }`

### Interface → Token Mapping

| Theme Path | Source | Transform |
|---|---|---|
| `colors.brand.primary` | `semantic: color.brand.primary` | Resolve → hex |
| `colors.brand.secondary` | `semantic: color.brand.secondary` | Resolve → hex |
| `colors.brand.accent` | `semantic: color.brand.accent` | Resolve → hex |
| `colors.surface.*` | `semantic: color.surface.*` | Resolve → hex |
| `colors.text.*` | `semantic: color.text.*` | Resolve → hex |
| `colors.border.*` | `semantic: color.border.*` | Resolve → hex |
| `colors.feedback.{type}.fg/bg` | `semantic: color.feedback.{type}.fg/bg` | Resolve → hex |
| `colors.data.series` | `semantic: color.data.series-1..6` | Array of resolved hex strings |
| `colors.audience.{id}` | `semantic: color.audience.{id}` | Resolve → hex, keyed by segment ID |
| `typography.fontFamily.*` | `primitives: font.family.*` | Direct string |
| `typography.fontSize.*` | `primitives: font.size.*` | Direct number (px) |
| `typography.fontWeight.*` | `primitives: font.weight.*` | Direct number |
| `typography.lineHeight.*` | `primitives: font.lineHeight.*` | Direct decimal |
| `typography.letterSpacing.*` | `primitives: font.letterSpacing.*` | Direct string (em) |
| `spacing.*` | `primitives: space.*` | Direct number (px) |
| `elevation.*` | `primitives: elevation.zindex.*` | Direct number |
| `breakpoints.*` | `primitives: breakpoint.*` | Direct number (px) |

### Motion Tokens (special transform)

| Theme Path | Source | Transform |
|---|---|---|
| `motion.duration.{key}` | `primitives: duration.{key}` | `Math.round(ms / 1000 * fps)` where fps=30 |
| `motion.easing.{key}` | `primitives: easing.{key}` | Direct CSS string |
| `motion.spring.*` | Static defaults | Keep existing values (no token source) |

### Preservation Rules

- **Keep TypeScript interfaces verbatim** — do not regenerate interfaces
- Regenerate only the `export const brandTheme: BrandTheme = { ... }` object values
- Keep helper functions (`getAudienceColor`, `getDataColor`, etc.) — regenerate their lookup values
- Keep `compositions` and `logo` objects as static defaults (updated via intake Q5/Q6)

---

## Validation Checklist

Run all 9 checks after regeneration. Report as pass/fail table to user.

### 1. Reference Resolution Complete
Scan all 4 export files for unresolved `{...}` patterns. **Pass:** zero matches. **Fail:** list each unresolved reference with file and line.

### 2. Hex Code Validity
Regex check all hex values match `#[0-9A-Fa-f]{6}` (or `#[0-9A-Fa-f]{3}` shorthand). **Pass:** all valid. **Fail:** list invalid values.

### 3. No Duplicate CSS Variables
In `css-variables.css`, check for duplicate `--{name}:` declarations. **Pass:** all unique. **Fail:** list duplicates.

### 4. No Duplicate Tailwind Keys
In `tailwind-config.js`, check for duplicate object keys at each level. **Pass:** all unique. **Fail:** list duplicates.

### 5. Figma Name Convention
In `figma-variables.json`, all `name` fields use `/` separators (not `.` or `-`). **Pass:** all names use slashes. **Fail:** list violations.

### 6. Remotion Type Completeness
Verify `brandTheme` object has all fields required by TypeScript interfaces: `colors`, `typography`, `spacing`, `elevation`, `breakpoints`, `motion`. **Pass:** all present. **Fail:** list missing fields.

### 7. WCAG Contrast Check
Check 16 critical contrast pairings from `references/accessibility-guide.md`:
- text-primary on surface-default (≥ 4.5:1)
- text-heading on surface-default (≥ 4.5:1)
- text-inverse on surface-inverse (≥ 4.5:1)
- brand-primary on white (≥ 3:1 for large text)
- brand-secondary on white (≥ 3:1 for large text)
- feedback colors on their backgrounds (≥ 4.5:1)
**Pass:** all pairings meet WCAG AA. **Fail:** list failing pairings with actual ratio.

### 8. File Size Sanity
Compare regenerated file sizes to previous versions:
- Not empty (> 0 bytes)
- Not wildly larger (< 2x previous size)
- Not wildly smaller (> 0.5x previous size)
**Pass:** all within range. **Fail:** list anomalies.

### 9. Token Count Consistency
Count token entries in source JSON files. Compare to variable count in exports:
- Tailwind: color families × shades + font entries + spacing entries ≈ expected
- CSS: semantic variable count ≈ expected
- Figma: total variables across collections ≈ expected
**Pass:** counts within 10% of expected. **Fail:** list mismatches.

---

## Reporting

After all exports regenerated and validated, report to user:

```
## Export Regeneration Complete

| Export | Status | Notes |
|--------|--------|-------|
| tailwind-config.js | ✅ Pass | {N} tokens mapped |
| css-variables.css | ✅ Pass | {N} variables generated |
| figma-variables.json | ✅ Pass | {N} variables across 3 collections |
| remotion-theme.ts | ✅ Pass | All interfaces satisfied |

### Validation (9/9 passed)
| Check | Result |
|-------|--------|
| Reference resolution | ✅ |
| Hex validity | ✅ |
| CSS uniqueness | ✅ |
| Tailwind uniqueness | ✅ |
| Figma naming | ✅ |
| Remotion completeness | ✅ |
| WCAG contrast | ✅ |
| File size sanity | ✅ |
| Token count consistency | ✅ |
```

If any check fails, list the specific failures and recommend corrective action.
