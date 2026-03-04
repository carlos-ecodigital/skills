# Brand Intake Example: Digital Energy

Complete intake walkthrough using Digital Energy as the subject brand. Demonstrates Create Brand mode end-to-end: Phase 0 material extraction, founder answers, design-recommendations-engine activations, validation checks, and token decisions.

**Purpose:** Reference for agents running the intake. Shows expected question flow, answer processing, assumption validation, and output format.

---

## Phase 0: Material Ingestion & Triage

### Q0.1 Material Existence Checklist

**Agent asks:** "For each item, mark exists / in progress / doesn't exist..."

**Founder answers:**
| Material | Status |
|---|---|
| Logo files (SVG, PNG) | Exists |
| Brand guidelines document | Doesn't exist |
| Pitch deck | Exists (v3, Jan 2026) |
| Website (live URL) | Exists: digitalenergy.nl |
| LinkedIn company page | Exists |
| Business cards | Doesn't exist |
| Email signature template | Exists (basic) |
| One-pagers | In progress |
| Proposal templates | Doesn't exist |
| Video content | Doesn't exist |
| Previous design work | Exists (Canva pitch deck) |
| Competitor references | Doesn't exist |

### Q0.2 Priority Materials Shared

**Founder provides:**
1. Pitch deck v3 (Google Slides link)
2. Logo files (SVG + PNG, dark and light variants)
3. Website URL: digitalenergy.nl
4. Email signature screenshot

### R0.1-R0.5 Agent Research (Parallel Execution)

**R0.1 Website extraction (digitalenergy.nl):**

| Extracted Value | Source | Confidence | Token Target |
|---|---|---|---|
| Background: #F8FAFC | Computed CSS, body | High | `surface.default` |
| Primary text: #1E293B | Computed CSS, p elements | High | `text.primary` |
| Heading font: Inter 700 | Computed CSS, h1-h3 | High | `font.family.heading` |
| Body font: Inter 400 | Computed CSS, p | High | `font.family.body` |
| Primary color: #1B365D | Logo, nav active, buttons | High | `brand.primary` |
| Secondary color: #22C55E | CTA buttons, icons | Medium | `brand.secondary` |
| Border color: #E2E8F0 | Card borders, dividers | High | `border.default` |
| Border radius: 8px | Cards, buttons | High | `radius.md` |
| Nav style: top-fixed | Layout observation | High | -- |
| Spacing base: ~16px | Gap analysis | Medium | `space.4` |

**R0.2 LinkedIn company page:**
- Banner: dark navy (#1B365D) with white text overlay
- Logo: matches SVG provided
- Post style: text-heavy, minimal imagery, professional tone
- Observation: consistent use of navy + green accent

**R0.3 Pitch deck extraction:**

| Extracted Value | Source | Confidence | Token Target |
|---|---|---|---|
| Slide bg: #FFFFFF | Slide backgrounds | High | Cover slides use white |
| Title font: Inter Bold | Slide titles | High | Confirms heading font |
| Title color: ~#1B365D | Dark navy titles | High | `text.heading` |
| Body size: ~16pt | Slide body text | Medium | Larger for presentation |
| Chart colors: navy, green, orange | Data slides | Medium | `data.series-1,2,3` |
| Accent: warm amber on heat slides | Heat recovery section | Medium | `brand.accent` candidate |
| Logo placement: top-left | All slides | High | `component.header` |
| Metric style: large bold numbers | Financial slides | High | `component.card.metric` |

**R0.4 Competitor extraction (QTS, Aligned, Vantage):**

| Competitor | Primary Color | Typography | Visual Style |
|---|---|---|---|
| QTS | Dark blue #003366 | Sans-serif, corporate | Enterprise, heavy imagery |
| Aligned | Teal #0D9488 | Modern sans | Tech-forward, clean |
| Vantage | Red #DC2626 | Bold sans | High-impact, aggressive |

**Differentiation notes:** DE's navy is similar to QTS but warmer. Green accent differentiates from all three. No competitor uses amber/warm accent. Typography (Inter) is modern vs. competitors' more corporate fonts.

**R0.5 Font check:**
- Inter: Google Fonts, freely available. Excellent number rendering. Variable font supported.
- JetBrains Mono: Google Fonts, freely available. Good for data tables.

### Q0.4 Extraction Validation

**Agent presents:**
> "From your website and pitch deck, I've extracted these design decisions. For each, confirm: (a) correct and keep, (b) close but adjust, (c) wrong."

| # | Decision | Extracted Value | Confidence | Founder Response |
|---|---|---|---|---|
| 1 | Primary brand color | #1B365D (deep navy) | High | (a) Correct |
| 2 | Secondary/accent | #22C55E (green) | Medium | (a) Correct -- "green = energy" |
| 3 | Heading font | Inter Bold | High | (a) Correct |
| 4 | Body font | Inter Regular | High | (a) Correct |
| 5 | Background | #F8FAFC (off-white) | High | (a) Correct |
| 6 | Border radius | 8px | High | (a) Correct |
| 7 | Heat accent color | Amber/warm | Medium | (b) Adjust -- "make it more orange for heat" |
| 8 | Chart palette | Navy, green, blue | Medium | (b) "Add orange for heat-related data" |

### Q0.5-Q0.12 Foundation Questions

**Q0.5 What to KEEP:** "The navy + green combination. The clean, data-forward look. The Inter font."

**Q0.6 What to CHANGE:** "Need more visual distinction between audiences. Current deck looks the same for every audience."

**Q0.7 Most urgent output:** (a) Pitch deck -- "investor deck is the priority."

**Q0.8 Visual identity strength:** (b) Instincts but nothing formal.

**Q0.9 Admired brands:** "Stripe (clean data presentation), Vantage (bold metrics), Nord Pool (energy market authority)."

**Q0.10 Emotional responses:** (a) trust and stability + (c) precision and rigor.

**Q0.11 Primary audience for first output:** Neocloud (investor deck targets neocloud understanding).

**Q0.12 Brand personality spectrum:**
| Axis | Rating | Notes |
|---|---|---|
| Traditional ↔ Modern | 4 | Modern but not bleeding edge |
| Serious ↔ Playful | 2 | Serious -- infrastructure deals |
| Conservative ↔ Bold | 3 | Middle -- data speaks boldly |
| Corporate ↔ Startup | 3 | "Startup energy, corporate rigor" |
| Minimal ↔ Expressive | 2 | Clean, data-forward, not decorative |

**Engine classification:** "Modern Professional" archetype (from design-recommendations-engine).

---

## Phase 1: Color Identity

### Q1.1-Q1.10 (Abridged)

| Q# | Answer | Engine Activation? |
|---|---|---|
| 1.1 Primary | Confirmed: #1B365D | No (extracted) |
| 1.2 Shade range | (a) Neutral-leaning | No |
| 1.3 Secondary | Confirmed: #22C55E | No (extracted) |
| 1.4 Domain accent | (a) Warm tones -- "#EA580C area for heat" | Q1.4 adjusted from amber to orange |
| 1.5 Neutral palette | (a) Cool grays | No |
| 1.6 Palette breadth | (c) Full: 8 hues -- "each audience needs distinction" | Triggers Q1.6a |
| 1.7 Audience accents | Yes -- each segment gets accent | Triggers Q1.7a |
| 1.8 Data viz palette | (b) Multi-hue (6 series) | No |
| 1.9 Dark backgrounds | (a) Yes -- hero sections, key reveals | Triggers Q1.9a |
| 1.10 Color exclusions | "No red as primary -- too aggressive. Red for errors only." | Logged |

### Q1.7a Audience Accent Mapping (Engine-Assisted)

**Engine generates proposal based on audience segments from brand-config:**

| Segment | Proposed Color | Rationale | Founder Response |
|---|---|---|---|
| Grower | #65A30D (lime green) | Agricultural, growth, natural | Approved |
| District Heat | #EA580C (orange) | Heat, warmth, energy | Approved |
| Industrial Heat | #B45309 (dark amber) | Industrial, heavy, warm | Approved |
| Neocloud | #2563EB (bright blue) | Tech, cloud, compute | Approved |
| Enterprise | #4338CA (indigo) | Corporate, established | Approved |
| Institution | #0F766E (teal) | Government, stable, trustworthy | Approved |

**Engine note:** All 6 colors pass pairwise distinctiveness test (minimum deltaE > 25). All pass CVD simulation for protanopia and deuteranopia.

---

## Phase 2: Typography (Abridged)

| Q# | Answer | Decision |
|---|---|---|
| 2.1 Heading font | Confirmed: Inter (extracted) | `font.family.heading`: Inter |
| 2.2 Body font | Same as heading | `font.family.body`: Inter |
| 2.3 Monospace | (a) Yes -- "critical for MW, EUR, % data" | `font.family.mono`: JetBrains Mono |
| 2.4 Heading weight | (a) Bold 700 | `font.weight.bold`: 700 |
| 2.5 Text density | (b) Balanced (1.5) | `font.lineHeight.normal`: 1.5 |
| 2.6 Min font size | (b) 12px | `font.size.xs`: 12 |
| 2.7 Heading case | (a) Sentence case | Transform rule logged |
| 2.8 Font size scale | (b) Standard (12-48) | 10-step scale: 12-48px |
| 2.9 Number formatting | (a) Tabular -- "numbers must align in columns" | `font-variant-numeric: tabular-nums` |
| 2.10 Bilingual | (c) Different weight -- "Dutch in regular, English in medium" | Language weight mapping logged |

---

## Phase 3-7: Abbreviated

Phases 3-7 followed the same pattern. Key decisions:

| Phase | Key Decisions |
|---|---|
| Phase 3 (Layout) | Left-aligned, moderate white space, 16:9 primary, 8px radius, 4px base spacing, bordered+alt tables |
| Phase 4 (Components) | Filled buttons, left-accent callouts, top-left logo, colored progress bar, below-chart citations |
| Phase 5 (Motion) | Future video need, moderate animation, 30fps, defaults accepted |
| Phase 6 (Logo) | SVG + PNG provided, 2 variants (full color, white), clear space = logo height, min 24px |
| Phase 7 (Imagery) | Industrial/facilities style, no brand tint, 40% image ratio, outline icons, technical diagrams |

---

## Validation Framework Results

### V.1 Internal Consistency

| Check | Status | Detail |
|---|---|---|
| Q0.10 (trust+precision) ↔ colors | PASS | Deep navy = trust, cool grays = precision |
| Q0.12 (Modern 4, Serious 2) ↔ typography | PASS | Inter modern; bold weight = serious |
| Q0.12 (Minimal 2) ↔ spacing | PASS | Balanced density, clean layout |
| Q5.2 (moderate) ↔ motion tokens | PASS | 300ms default, no bounce |
| Q1.10 (no red primary) ↔ palette | PASS | Red reserved for error only |

### V.2 Accessibility Compliance

| # | Pairing | Ratio | Required | Status |
|---|---|---|---|---|
| 1 | text.primary (#1E293B) on surface.default (#F8FAFC) | 12.4:1 | 4.5:1 | PASS |
| 2 | text.secondary (#64748B) on surface.default (#F8FAFC) | 4.7:1 | 4.5:1 | PASS (marginal) |
| 3 | text.heading (#142945) on surface.default (#F8FAFC) | 13.1:1 | 3:1 | PASS |
| 7 | white on brand.primary (#1B365D) | 10.2:1 | 4.5:1 | PASS |
| 8 | white on brand.secondary (#22C55E) | 2.8:1 | 4.5:1 | **FAIL** |
| 15 | text.caption (#94A3B8) on surface.default (#F8FAFC) | 3.0:1 | 4.5:1 | **FAIL** |

**Remediation applied:**
1. **brand.secondary with white text:** Use #15803D (green-700) for button backgrounds with white text. Reserve #22C55E for accents, borders, non-text indicators only.
2. **text.caption on surface.default:** Darken caption color from #94A3B8 to #64748B for text contexts. Keep #94A3B8 for decorative/non-essential captions only.

### V.3 Benchmark Comparison

| Property | DE Value | Industry Norm (energy-infra) | Status |
|---|---|---|---|
| Primary color temp | Cool navy | Deep cool (navy/dark teal) | MATCH |
| Secondary | Vibrant green | Vibrant warm (green/amber) | MATCH |
| Typography | Inter, balanced | Sans-serif, medium density | MATCH |
| Radius | 8px (moderate) | 4-8px typical | MATCH |
| White space | Balanced | Moderate-generous | MATCH |
| Animation | Moderate | Minimal-moderate | MATCH |

No outliers flagged.

### V.4 Completeness Assessment

| Output Context | Score | Threshold | Status |
|---|---|---|---|
| Presentation (Figma/Slides) | 95% | 70% | READY |
| Document (PDF) | 90% | 60% | READY |
| Claude Code HTML/React | 92% | 60% | READY |
| Remotion Video | 75% | 70% | READY (marginal -- no video content yet) |
| Figma UI | 88% | 60% | READY |

**Missing for 100%:** Actual video content examples (Phase 5 was "future"), photography asset library (Q7.1 answered but no actual photos).

### V.5 Cross-Reference Alignment

Checked against `de-brand-bible` verbal brand skill:

| Verbal Brand Rule | Visual Decision | Status |
|---|---|---|
| "Technically confident" tone | Mono font for data, tabular numbers | ALIGNED |
| "Not salesy" | No aggressive CTAs, muted secondary for text | ALIGNED |
| "Data-forward" | Metric card component, chart-heavy templates | ALIGNED |
| 6 buyer personas | 6 audience accent colors | ALIGNED |

### V.6 Material Extraction Validation

| Token | Source | Confidence | Confirmed by User |
|---|---|---|---|
| brand.primary: #1B365D | Website + pitch deck + logo | High | Yes (Q0.4, #1) |
| brand.secondary: #22C55E | Website CTA buttons | Medium | Yes (Q0.4, #2) |
| font.family.heading: Inter | Website computed CSS | High | Yes (Q0.4, #3) |
| surface.default: #F8FAFC | Website body background | High | Yes (Q0.4, #5) |
| radius.md: 8px | Website card + button borders | High | Yes (Q0.4, #6) |
| brand.accent: #F59E0B -> #EA580C | Pitch deck heat slides | Medium | Adjusted (Q0.4, #7) -- changed to more orange |

All extracted tokens confirmed or adjusted. No unconfirmed extractions remain.

### V.7 Tool Compatibility

| Check | Status |
|---|---|
| Token JSON: valid JSON, parseable | PASS |
| Tailwind config: valid JS module | PASS |
| CSS variables: valid CSS, no syntax errors | PASS |
| Remotion theme: valid TypeScript, JSON-serializable values | PASS |
| Figma variables: valid collection format | PASS |
| All color values: valid 6-digit hex | PASS |
| All number values: finite, positive | PASS |

---

## Output Summary

### Interaction Stats
| Metric | Value |
|---|---|
| Total questions asked | 62 (of 103 possible) |
| Questions skipped (extracted) | 13 (answered by material extraction) |
| Conditional questions triggered | 8 (of 28 possible) |
| Conditional questions not triggered | 20 |
| Engine activations ("recommend") | 3 (audience accent mapping, dark surface scope, data viz approach) |
| Interaction rounds (batches of 2-4 Qs) | 26 |
| Validation issues found | 2 (both accessibility, both remediated) |
| Cross-reference conflicts | 0 |

### Deliverables Produced
1. `tokens/primitives.tokens.json` -- 200+ tokens, DE defaults
2. `tokens/semantic.tokens.json` -- 90+ tokens, audience accents for 6 segments
3. `tokens/component.tokens.json` -- ~440 tokens, full state coverage (13 component types)
4. `exports/tailwind-config.js` -- Complete Tailwind v3 config
5. `exports/css-variables.css` -- CSS custom properties
6. `exports/remotion-theme.ts` -- TypeScript theme with interfaces
7. `exports/figma-variables.json` -- 3 Figma variable collections
8. `brand-configs/digital-energy.md` -- Resolved brand config

### Key Design Rationale Chain
```
Founder input: "trust + precision" + "data-forward" + "Modern 4, Serious 2, Minimal 2"
  → Engine classifies: "Modern Professional" archetype
    → Color: deep cool primary (navy), vibrant warm secondary (green)
      → Extracted #1B365D confirmed, #22C55E confirmed
    → Typography: Inter (modern sans), balanced density
      → Extracted Inter confirmed, JetBrains Mono added for data
    → Spacing: 4px base, moderate white space
      → Extracted 8px radius confirmed
    → Motion: moderate (300ms default), no bounce
      → Defaults accepted
    → Components: data-forward (metric cards prominent, mono numbers, tables with headers)
      → Aligned with "precision + rigor" emotional target
```

This rationale chain shows every design decision traceable to either: (a) extracted material, (b) founder answer, or (c) engine recommendation accepted by founder. No unsupported decisions.
