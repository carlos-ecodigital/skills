---
chunk_id: "design-recommendations-engine"
domain: "intake"
category: "defaults"
tags: ["recommendations", "defaults", "industry-profiles", "decision-trees", "design-suggestions"]
depends_on: ["intake-guide"]
token_count_approx: 3000
version: "1.0"
last_updated: "2026-02-21"
status: "active"
summary: >-
  Parameterized default generation for 7 industry profiles. Decision trees
  for color, typography, spacing, motion, and components. Always provides
  rationale + one alternative. Never auto-applies.
---

# Design Recommendations Engine

Decision trees for generating reasoned design defaults when the user says "recommend," "I don't know," or "set for me." Parameterized by brand-config fields: `industry`, `tone_keywords`, `geography`, `audience_segments`, `domain_specific_accent`, and Q0.10/Q0.12 personality inputs.

## Activation Rules

1. **Never auto-apply.** Always present as "I recommend X because Y. Alternative: Z. Which do you prefer?"
2. **Always provide rationale.** Trace recommendation to brand-config values and personality scores.
3. **Always provide one alternative.** Never present a single option.
4. **Respect exclusions.** Never recommend a color in the Q1.10 exclusion list.
5. **Respect extractions.** If material extraction produced a High-confidence value, recommend keeping it.
6. **Log decisions.** Every engine recommendation records: question ID, recommended value, rationale, alternative, user choice.

---

## Industry Profiles

### Energy & Infrastructure (`energy-infrastructure`)

| Dimension | Default | Rationale |
|---|---|---|
| Primary color temp | Deep cool (navy, dark teal, dark blue-gray) | Institutional trust, European energy conventions, infrastructure gravitas |
| Secondary color temp | Vibrant warm (green, amber, coral) | Sustainability signal, energy/heat associations, contrast with cool primary |
| Neutral temp | Cool grays | Tech alignment, clean backgrounds |
| Heading font style | Geometric sans-serif (Inter, DM Sans) | Technical precision, excellent tabular numbers for data-heavy materials |
| Body font | Same as heading (single family) | Cohesion in data-dense documents |
| Heading weight | Semibold (600) | Confident but not aggressive |
| Text density | Balanced (1.5) | Mix of narrative and data content |
| Border radius | Slight (4-8px) | Modern professional without being playful |
| White space | Moderate | Balance between data density and readability |
| Animation | Moderate | Professional, not flashy |
| Photography | Industrial + aerial mix | Physical infrastructure is the product |

### B2B SaaS (`b2b-saas`)

| Dimension | Default | Rationale |
|---|---|---|
| Primary color temp | Neutral cool (slate blue, indigo, violet) | Modern tech conventions, calm professionalism |
| Secondary color temp | Bright accent (purple, electric blue, teal) | Action/CTA emphasis, feature highlights |
| Neutral temp | Cool grays | Clean, digital-native feel |
| Heading font style | Geometric or humanist sans-serif (Inter, Plus Jakarta Sans, Satoshi) | Clean, modern, approachable |
| Body font | Same or paired humanist sans | Readability in product interfaces |
| Heading weight | Semibold (600) | Modern standard |
| Text density | Balanced to airy (1.5-1.75) | Content marketing, product pages |
| Border radius | Rounded (8-12px) | Friendly, approachable, modern product feel |
| White space | Moderate to generous | Clean product aesthetics |
| Animation | Moderate to dynamic | Product feature showcases |
| Photography | Abstract/screen + people using product | Technology + human element |

### Fintech (`fintech`)

| Dimension | Default | Rationale |
|---|---|---|
| Primary color temp | Deep blue or deep green | Trust, security, financial conventions |
| Secondary color temp | Subtle gold or amber | Premium, success, financial growth |
| Neutral temp | Cool grays | Clean, trustworthy backgrounds |
| Heading font style | Clean sans-serif (Inter, Switzer, General Sans) | Trustworthy, legible at all sizes |
| Body font | Same family or serif pairing for editorial | Trust signals, reading comfort |
| Heading weight | Bold (700) | Authority, financial confidence |
| Text density | Balanced (1.5) | Mix of marketing and data |
| Border radius | Slight (4-8px) | Professional, not casual |
| White space | Moderate | Balance trust and information density |
| Animation | Minimal to moderate | Security feel, no unnecessary flash |
| Photography | Abstract + corporate | Trust and technology |

### Healthcare (`healthcare`)

| Dimension | Default | Rationale |
|---|---|---|
| Primary color temp | Teal, soft blue, or calming green | Healing, trust, medical conventions |
| Secondary color temp | Warm coral, soft orange, or rose | Empathy, warmth, care |
| Neutral temp | Warm grays | Approachable, less clinical |
| Heading font style | Humanist sans-serif (Plus Jakarta Sans, Nunito, Source Sans) | Warm, accessible, friendly |
| Body font | Same or paired humanist | Reading comfort, accessibility |
| Heading weight | Semibold (600) | Friendly but professional |
| Text density | Airy (1.75) | Readability, accessibility focus |
| Border radius | Rounded (12-16px) | Warm, approachable, non-threatening |
| White space | Generous | Calm, uncluttered, healing feel |
| Animation | Minimal | Calm, no anxiety-inducing motion |
| Photography | People-focused + clinical clean | Empathy + expertise |

### Consumer (`consumer`)

| Dimension | Default | Rationale |
|---|---|---|
| Primary color temp | Bright, saturated (depends on sub-category) | Attention, shelf impact, brand recognition |
| Secondary color temp | Complementary warm or contrasting | Energy, action, impulse |
| Neutral temp | True grays or warm grays | Neutral base for colorful palette |
| Heading font style | Bold display sans or custom (Clash Display, Cabinet Grotesk) | Personality, differentiation |
| Body font | Clean sans-serif | Readability at scale |
| Heading weight | Bold (700) | Impact, shelf presence |
| Text density | Balanced (1.5) | Marketing + product info |
| Border radius | Rounded (12-16px) | Friendly, tactile, consumer-grade |
| White space | Moderate | Balance between personality and information |
| Animation | Dynamic | Engagement, personality, social media |
| Photography | Lifestyle + product hero | Aspiration + product showcase |

### Deep Tech (`deep-tech`)

| Dimension | Default | Rationale |
|---|---|---|
| Primary color temp | Dark, desaturated (dark navy, charcoal, deep blue-gray) | Technical authority, depth |
| Secondary color temp | Neon or bright accent (electric blue, cyan, lime, magenta) | Technical energy, futurism, data viz |
| Neutral temp | Cool grays tending dark | Dark mode preference, terminal feel |
| Heading font style | Geometric sans-serif or mono-influenced (Space Grotesk, IBM Plex Sans) | Technical, precise, engineering |
| Body font | Same or clean geometric | Code-adjacent readability |
| Heading weight | Medium (500) to Semibold (600) | Understated precision |
| Text density | Dense (1.25) to balanced | Data-heavy, technical documentation |
| Border radius | Sharp (0-4px) | Technical precision |
| White space | Tight to moderate | Information density |
| Animation | Moderate to dynamic | Technical demonstrations |
| Photography | Abstract/rendered + technical detail | Technology as aesthetic |

### Professional Services (`professional-services`)

| Dimension | Default | Rationale |
|---|---|---|
| Primary color temp | Traditional navy, dark green, or burgundy | Authority, tradition, trust |
| Secondary color temp | Minimal -- muted gold, subtle teal | Restrained elegance |
| Neutral temp | Warm grays | Professional warmth |
| Heading font style | Serif (Playfair Display, Lora) or clean sans (Inter) | Tradition + authority OR modern professionalism |
| Body font | Paired serif/sans or single family | Editorial quality |
| Heading weight | Bold (700) | Authority |
| Text density | Airy (1.75) | Premium, editorial feel |
| Border radius | Sharp (0px) to slight (4px) | Conservative, precise |
| White space | Generous | Premium, exclusive feel |
| Animation | Minimal | Conservative, understated |
| Photography | Corporate portraiture + lifestyle | People and trust |

---

## Decision Trees

### Primary Color Recommendation (Q1.1a)

```
INPUT: industry, tone_keywords, Q0.10 emotional_response, Q0.12 personality

1. Get industry default color temperature (from profile above)
2. Adjust for emotional response:
   - "trust-stability" → push toward deeper, cooler tones (+10% darker)
   - "innovation-energy" → push toward brighter, more saturated (+15% saturation)
   - "precision-rigor" → push toward desaturated, neutral-toned
   - "warmth-partnership" → push toward warmer tones (add yellow/red shift)
   - "speed-momentum" → push toward saturated, energetic
   - "authority-scale" → push toward darker, more muted
3. Adjust for personality:
   - traditional (1-2) → more muted, darker
   - modern (4-5) → more saturated, contemporary hues
   - conservative (1-2) → desaturated, safe
   - bold (4-5) → saturated, distinctive
4. Check exclusion list (Q1.10) -- never recommend excluded hues
5. Check competitor colors (R0.4) -- avoid exact competitor matches
6. Generate 2 options:
   - Option A: Best match for all inputs
   - Option B: Intentional departure (different hue, similar feel)
7. Present with hex values, color names, and rationale
```

### Secondary Color Recommendation (Q1.3a)

```
INPUT: confirmed primary, industry, domain_specific_accent, tone_keywords

1. Get industry default secondary temperature
2. Calculate contrast with primary:
   - If primary is cool → secondary should be warm (complementary energy)
   - If primary is warm → secondary can be cool or analogous
   - Minimum hue distance: 60° on color wheel
3. If domain_specific_accent exists:
   - If accent.temperature = "warm" → secondary should include warm tones
   - If accent.temperature = "cool" → secondary can be cool
4. Generate 2 options:
   - Option A: Complementary to primary
   - Option B: Analogous but distinguishable
5. Verify WCAG contrast of secondary-on-white ≥ 3:1
```

### Heading Font Recommendation (Q2.1a)

```
INPUT: industry, personality (Q0.12), emotional_response (Q0.10), geography

1. Get industry default font style (from profile above)
2. Adjust for personality axes:
   - serious (1-2) → heavier weights, more structured (Inter, DM Sans)
   - playful (4-5) → lighter, more character (Plus Jakarta Sans, Nunito)
   - traditional (1-2) → serif consideration (Playfair Display, Lora)
   - modern (4-5) → geometric sans (Space Grotesk, Satoshi)
   - corporate (1-2) → safe choices (Inter, Source Sans Pro)
   - startup (4-5) → distinctive choices (Cabinet Grotesk, General Sans)
3. Check requirements:
   - If brand has number-heavy content → must have excellent tabular figures
   - If secondary_language set → must support both language character sets
   - If geography includes Asian characters → must have CJK support
4. Verify Google Fonts availability (R0.5)
5. Generate 2 options:
   - Option A: Best personality match
   - Option B: Contrasting but valid alternative
6. Include: font name, weight range, Google Fonts URL, rationale
```

### Body Font Pairing (Q2.2a)

```
INPUT: confirmed heading font, personality

1. If personality minimal ≥ 3 → recommend same family (single-family system)
2. If personality expressive ≥ 4 or traditional ≤ 2 → recommend pairing:
   - Serif heading + sans body (classic editorial)
   - Geometric heading + humanist body (modern readable)
3. Pairing compatibility rules:
   - Same x-height range
   - Compatible stroke contrast
   - Different enough to distinguish, similar enough to harmonize
4. Generate 2 options with pairing rationale
```

### Monospace Recommendation (Q2.3a)

```
Default recommendation: JetBrains Mono
  - Rationale: excellent at small sizes, distinctive (≠ Courier), good tabular figures,
    free, wide language support, designed for data display

Alternative: Fira Code
  - Rationale: excellent coding font, ligatures, slightly warmer personality

Fallback: Source Code Pro
  - Rationale: Adobe's neutral mono, safe choice, good at small sizes
```

### Neutral Palette (Q1.5 if "recommend")

```
INPUT: primary color, personality, industry

1. If primary is cool (blue/teal/purple) → default cool grays
2. If primary is warm (red/orange/amber) → default warm grays
3. If personality minimal ≥ 4 → true grays (no tint)
4. If industry = healthcare → warm grays (approachable)
5. If industry = deep-tech → cool grays tending dark
```

### Audience Accent Mapping (Q1.7a)

```
INPUT: audience_segments from brand-config, confirmed primary, confirmed secondary

For each segment, recommend accent based on audience type:

Mapping rules:
- Technical buyers (engineers, IT) → cool tones (blue, teal, slate)
- Business buyers (executives, finance) → deep tones (navy, dark green, charcoal)
- Operational buyers (managers, operators) → warm tones (amber, coral, earth)
- Government/institutional → muted, conservative (muted blue, gray-blue)
- Consumer/individual → bright, energetic (warm, saturated)
- Partner/channel → neutral, non-competing (muted secondary)

Constraints:
- No accent can be identical to primary or secondary
- All accents must be WCAG distinguishable from each other
- Maximum 6 distinct accent colors (beyond that, reuse with modifiers)
```

### Animation Personality Calibration (Q5.2)

```
Minimal (personality serious ≤ 2 OR minimal ≥ 4):
  durations: { fast: 100ms, default: 200ms, slow: 300ms, enter: 250ms, exit: 200ms }
  easings: { default: "ease", in: "ease-in", out: "ease-out", bounce: "ease-out" }

Moderate (balanced personality):
  durations: { fast: 150ms, default: 300ms, slow: 500ms, enter: 350ms, exit: 250ms }
  easings: { default: "cubic-bezier(0.4, 0, 0.2, 1)", in: "cubic-bezier(0.4, 0, 1, 1)", out: "cubic-bezier(0, 0, 0.2, 1)", bounce: "cubic-bezier(0.34, 1.56, 0.64, 1)" }

Dynamic (personality bold ≥ 4 OR startup ≥ 4):
  durations: { fast: 200ms, default: 400ms, slow: 700ms, enter: 500ms, exit: 300ms }
  easings: { default: "cubic-bezier(0.4, 0, 0.2, 1)", in: "cubic-bezier(0.55, 0, 1, 0.45)", out: "cubic-bezier(0, 0.55, 0.45, 1)", bounce: "cubic-bezier(0.34, 1.56, 0.64, 1)" }
```

### Spacing Multiplier (Q3.2)

```
Generous (personality minimal ≥ 4 OR industry = healthcare/professional-services):
  multiplier: 1.5
  layout_margin: base * 8 (generous)
  section_gap: base * 12
  component_padding: base * 6

Moderate (balanced or unspecified):
  multiplier: 1.0
  layout_margin: base * 6
  section_gap: base * 8
  component_padding: base * 4

Tight (personality expressive ≥ 4 OR industry = deep-tech, data-heavy):
  multiplier: 0.75
  layout_margin: base * 4
  section_gap: base * 6
  component_padding: base * 3
```

### Border Radius Scale (Q3.4)

```
Sharp (personality traditional ≤ 2 OR industry = professional-services):
  { none: 0, sm: 0, md: 0, lg: 2, xl: 4, full: 9999 }

Slight (personality score 2-3 balanced OR industry = energy/fintech):
  { none: 0, sm: 2, md: 4, lg: 8, xl: 12, full: 9999 }

Rounded (personality modern ≥ 4 OR industry = consumer/healthcare/b2b-saas):
  { none: 0, sm: 4, md: 8, lg: 12, xl: 16, full: 9999 }
```

---

## Personality-to-Token Mappings

### Q0.12 Score Interpretation Table

**Score 3 = balanced center.** Apply moderate/standard defaults for that axis. Only diverge from standard when the score is ≤2 or ≥4. When no personality score is provided for an axis, treat it as 3.

| Axis | Score 1-2 | Score 3 (balanced center) | Score 4-5 |
|---|---|---|---|
| **Traditional ↔ Modern** | Serif-friendly, muted colors, generous spacing, sharp corners | Standard sans-serif, moderate saturation, slight radius | Geometric sans, saturated colors, rounded corners |
| **Serious ↔ Playful** | Heavy weights, dark palette, minimal animation | Semibold weights, balanced palette, moderate animation | Light weights, bright palette, dynamic animation |
| **Conservative ↔ Bold** | Desaturated, safe hues, thin borders | Moderate saturation, standard hues, medium borders | Saturated, distinctive hues, thick accents |
| **Corporate ↔ Startup** | Established font choices (Inter, Helvetica), traditional layouts | Standard professional fonts, conventional layouts | Distinctive fonts (Space Grotesk, Clash Display), creative layouts |
| **Minimal ↔ Expressive** | Generous white space, few colors, no patterns | Balanced density, standard color count, no patterns | Dense content, many colors, patterns/textures |

### Composite Personality Archetypes

Common personality score combinations and their design implications:

**The Institution** (traditional 1-2, serious 1-2, conservative 1-2, corporate 1-2, minimal 3-4):
- Deep navy/dark green primary, muted secondary
- Serif or established sans (Inter, Source Sans)
- Bold weights, generous spacing, sharp corners
- Minimal animation, corporate photography
- *Think: McKinsey, Goldman Sachs, law firms*

**The Modern Professional** (modern 4, serious 2-3, conservative 3, corporate 2-3, minimal 4):
- Cool primary, bright secondary accent
- Clean geometric sans (Inter, DM Sans)
- Semibold weights, generous spacing, slight radius
- Moderate animation, clean photography
- *Think: Stripe, Linear, Notion*

**The Bold Innovator** (modern 5, serious 3, bold 4-5, startup 4-5, expressive 3-4):
- Distinctive primary, vibrant secondary
- Characterful sans (Space Grotesk, Cabinet Grotesk)
- Variable weights, moderate spacing, rounded radius
- Dynamic animation, conceptual photography
- *Think: Vercel, Figma, Framer*

**The Warm Expert** (traditional 3, serious 2, conservative 2-3, corporate 2-3, minimal 3):
- Deep warm primary, subtle secondary
- Humanist sans (Plus Jakarta Sans, Nunito)
- Semibold weights, balanced spacing, slight radius
- Moderate animation, people-focused photography
- *Think: Atlassian, HubSpot, Slack*

**The Technical Authority** (modern 3-4, serious 2, conservative 3, corporate 2-3, minimal 4-5):
- Dark desaturated primary, neon accent secondary
- Mono-influenced sans (Space Grotesk, IBM Plex)
- Medium weights, tight spacing, sharp corners
- Minimal animation, technical/abstract photography
- *Think: GitHub, Datadog, Cloudflare*

---

## Font Recommendation Library

### Heading Fonts by Personality

| Personality Profile | Font | Why | Google Fonts | Tabular Figures |
|---|---|---|---|---|
| Serious + Corporate | Inter | Industry standard, excellent numbers | Yes | Yes |
| Serious + Modern | DM Sans | Clean, contemporary geometric | Yes | Yes |
| Modern + Bold | Space Grotesk | Distinctive, technical feel | Yes | Yes |
| Modern + Startup | Plus Jakarta Sans | Friendly geometric, wide range | Yes | Yes |
| Bold + Expressive | Cabinet Grotesk | Characterful, stands out | Yes (Fontshare) | No |
| Traditional + Corporate | Source Serif 4 | Classic editorial, trustworthy | Yes | N/A |
| Traditional + Warm | Lora | Elegant serif, readable | Yes | N/A |
| Minimal + Technical | IBM Plex Sans | Neutral, excellent mono pairing | Yes | Yes |
| Healthcare + Warm | Nunito | Rounded, friendly, accessible | Yes | No |
| Consumer + Playful | Rubik | Rounded geometric, warm | Yes | No |

### Body Font Pairings

| Heading Font | Recommended Body | Pairing Type |
|---|---|---|
| Inter | Inter (same family) | Single-family |
| DM Sans | DM Sans or Inter | Single-family or compatible geometric |
| Space Grotesk | Inter or IBM Plex Sans | Geometric contrast |
| Plus Jakarta Sans | Plus Jakarta Sans | Single-family |
| Source Serif 4 | Source Sans 3 | Serif/sans superfamily |
| Lora | Source Sans 3 or Inter | Classic serif/sans |
| IBM Plex Sans | IBM Plex Sans | Single-family |
| Cabinet Grotesk | Inter | Distinctive heading, neutral body |

### Monospace Fonts

| Font | Best For | Google Fonts |
|---|---|---|
| JetBrains Mono | Data tables, technical specs, small sizes | Yes |
| Fira Code | Code snippets, developer content | Yes |
| Source Code Pro | General purpose, neutral | Yes |
| IBM Plex Mono | IBM Plex family match | Yes |
| DM Mono | DM Sans family match | Yes |

---

## Data Visualization Palette Generation

### Monochromatic (Q1.8 = a)

```
INPUT: primary color

Generate 4 shades of primary:
  series_1: primary-700
  series_2: primary-500
  series_3: primary-300
  series_4: primary-100 (with primary-700 border)

positive: primary-600
negative: error-500
neutral: neutral-400
```

### Multi-Hue (Q1.8 = b)

```
INPUT: primary color, secondary color

Generate 6 hue-distinct series:
  series_1: primary-500
  series_2: secondary-500
  series_3: generated complementary (180° from primary)
  series_4: generated split-complementary A (150° from primary)
  series_5: generated split-complementary B (210° from primary)
  series_6: generated triadic (120° from primary)

Validation:
  - All 6 must be distinguishable under protanopia
  - All 6 must be distinguishable under deuteranopia
  - Minimum deltaE of 20 between any two adjacent series
  - All must be WCAG distinguishable (3:1 contrast between each other on white)

positive: success-500 (green-based)
negative: error-500 (red-based)
neutral: neutral-400
```

### Audience-Matched (Q1.8 = c)

```
INPUT: audience accent colors (from Q1.7a)

Each data series uses the accent color for the audience it represents:
  series_1: audience_1_accent
  series_2: audience_2_accent
  ... (up to 6)

Same validation as multi-hue.
```

---

## Shade Scale Generation

### 10-Shade Scale Algorithm

Given a base color (e.g., primary confirmed at Q1.1):

```
INPUT: base_hex, saturation_mode (neutral-leaning | saturated)

For neutral-leaning (Q1.2 = a):
  50:  lightness 97%, saturation 15%
  100: lightness 94%, saturation 20%
  200: lightness 88%, saturation 25%
  300: lightness 78%, saturation 35%
  400: lightness 64%, saturation 50%
  500: base color (saturation 100%)
  600: lightness -8%, saturation 100%
  700: lightness -16%, saturation 95%
  800: lightness -24%, saturation 85%
  900: lightness -32%, saturation 75%
  950: lightness -38%, saturation 65%

For saturated (Q1.2 = b):
  50:  lightness 97%, saturation 40%
  100: lightness 94%, saturation 55%
  200: lightness 88%, saturation 65%
  300: lightness 78%, saturation 75%
  400: lightness 64%, saturation 85%
  500: base color (saturation 100%)
  600: lightness -8%, saturation 100%
  700: lightness -16%, saturation 100%
  800: lightness -24%, saturation 95%
  900: lightness -32%, saturation 90%
  950: lightness -38%, saturation 85%

All percentages are relative to the base color's HSL values.
```

### Font Size Scale Generation

```
INPUT: min_size (Q2.6), max_size (Q2.8), steps = 10

Scale options:
  Compact (12-36): [12, 13, 14, 16, 18, 20, 24, 28, 32, 36]
  Standard (12-48): [12, 14, 16, 18, 20, 24, 30, 36, 42, 48]
  Dramatic (12-60): [12, 14, 16, 18, 21, 24, 32, 40, 48, 60]

Token mapping:
  xs = scale[0]    (footnotes, legal)
  sm = scale[1]    (captions, labels)
  base = scale[2]  (body text)
  md = scale[3]    (lead text)
  lg = scale[4]    (H4)
  xl = scale[5]    (H3)
  2xl = scale[6]   (H2)
  3xl = scale[7]   (H1)
  4xl = scale[8]   (Display)
  5xl = scale[9]   (Hero)
```

---

## Geography Adjustments

### European (`european-*`)
- Longer words → slightly wider line lengths preferred
- Formal by default → corporate personality boost +0.5
- GDPR conventions → cookie/consent patterns in UI components
- A4 document format (210x297mm) as default print size

### North American (`north-american`)
- US Letter document format (8.5x11in) as default print size
- More informal default → startup personality boost +0.5
- Brighter color defaults accepted

### Asia-Pacific (`asia-pacific`)
- CJK font support required → check heading font has CJK glyphs
- Higher information density expected → tight spacing boost
- Red has positive associations (not just error)

### Global (`global`)
- Most conservative defaults
- Ensure all color associations are culturally neutral
- Default to US Letter AND A4 support

---

## Tone Keyword Adjustments

Tone keywords from brand-config `tone_keywords` apply fine-grained adjustments on top of industry defaults:

| Keyword | Adjustment |
|---|---|
| `precise` | Tabular figures required, sharp or slight radius, dense or balanced spacing |
| `data-forward` | Monospace font required, dramatic font scale, tight table styling |
| `technically-confident` | Medium to semibold weights, cool neutral, minimal animation |
| `honest` | No decorative elements, minimal radius, straightforward photography |
| `numbers-first` | Dramatic font scale, tabular figures, metric card display |
| `playful` | Rounded radius, lighter weights, dynamic animation, warm neutrals |
| `bold` | Heavy weights, saturated colors, pronounced shadows |
| `accessible` | Airy spacing, rounded radius, larger minimum font, generous white space |
| `warm` | Warm neutrals, rounded radius, humanist fonts |
| `conservative` | Sharp corners, heavy weights, muted colors, traditional photography |
| `trustworthy` | Deep cool primary, clean sans or serif, generous spacing |
| `institutional` | Dark primary, bold weights, minimal animation, corporate photography |
| `measured` | Medium weights, balanced spacing, moderate everything |
| `clean` | Generous white space, minimal radius, true grays |
| `modern` | Geometric sans, cool palette, slight radius, subtle animation |
| `premium` | Generous spacing, serif or clean sans, minimal palette, subtle shadows |
| `innovative` | Bright accent, dynamic animation, distinctive font |
| `sustainable` | Green secondary, warm accent, natural photography |
