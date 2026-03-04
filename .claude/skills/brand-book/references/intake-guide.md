---
chunk_id: "intake-guide"
domain: "intake"
category: "methodology"
tags: ["intake", "questions", "phases", "onboarding", "brand-creation"]
depends_on: []
token_count_approx: 4000
version: "1.0"
last_updated: "2026-02-21"
status: "active"
summary: >-
  Complete 108-question brand intake across 8 phases. Phase 0: material
  ingestion. Phases 1-7: domain questions (color, typography, spacing,
  components, motion, logo, photography). Includes batching rules,
  research task execution, and validation framework.
---

# Brand Intake Guide

Complete structured intake for building a visual design system from scratch or from existing materials. 8 phases, 80 core + 28 conditional = 108 questions. Follows the `_shared/intake-design-guidebook.md` methodology.

## How to Use This Guide

### Operating Modes

**Create Brand mode:** Run all 8 phases sequentially. Ingest materials first (Phase 0), extract implicit design decisions, ask targeted gap questions, validate, produce all deliverables. ~30-38 interaction rounds.

**Make mode:** User needs one specific output. Look up the deliverable in `question-deliverable-map.md` Format B, identify feeding questions, run Phase 0 + only those questions. Typically 10-15 rounds.

**Reference mode:** Deliverables already exist. Skill is passive reference consumed by downstream tools.

### Conventions

- `{brand_name}` = resolved from `brand-configs/{brand-slug}.md` field `brand_name`
- `{industry}` = resolved from brand-config `industry`
- `{audience_N}` = resolved from brand-config `audience_segments[N].name`
- `{tone}` = resolved from brand-config `tone_keywords`
- Questions marked **[CONDITIONAL]** only fire when their trigger condition is met
- Questions marked **[ENGINE]** activate the design-recommendations-engine when user says "recommend" or "I don't know"
- **Feeds** = deliverable sections this question populates (see `question-deliverable-map.md` for full traceability)

### Batching Rules

Present 2-4 questions per interaction round. Group by:
1. Same domain (e.g., all color questions together)
2. Same decision type (e.g., all "choose from options" together)
3. Dependency order (e.g., primary color before shade range)

Never present more than 4 questions at once. Never present conditional questions in the same batch as their trigger.

### Research Task Execution

Phase 0B research tasks (R0.1-R0.5) run in parallel with user interaction. The agent:
1. Starts research tasks immediately after receiving Phase 0A answers
2. Continues asking Phase 0D questions while research runs
3. Incorporates research results into Q0.4 extraction summary
4. Does NOT wait for research completion to ask questions -- research informs but doesn't block

---

## Phase 0: Material Ingestion & Triage

**Purpose:** Ingest everything that exists. Extract implicit design decisions. Determine the gap list. Set priorities. Understand the founder's aesthetic instincts.

**Phase 0 total:** 12 questions + 5 research tasks + 0-5 system data points (conditional).

### Phase 0A: Document Checklist (Q0.1-Q0.3)

**Batch 1 (Q0.1-Q0.2)**

---

#### Q0.1 -- Material Existence Checklist

**Question:** For each item below, tell me: **exists** / **in progress** / **doesn't exist**.

| # | Material | Status |
|---|----------|--------|
| a | Logo files (SVG, PNG, AI/EPS) | |
| b | Brand guidelines document | |
| c | Pitch deck (any version) | |
| d | Website (live URL) | |
| e | Social media profiles (LinkedIn, X/Twitter) | |
| f | Business cards or stationery | |
| g | Email signature template | |
| h | One-pagers or brochures | |
| i | Proposal or report templates | |
| j | Video content | |
| k | Previous design work (Figma files, Canva, Adobe) | |
| l | Competitor reference materials you've collected | |

**Why:** Existing materials reduce intake by 30-40%. A styled pitch deck reveals implicit color/font/layout decisions already made. Every "exists" triggers an agent extraction task in Phase 0B.

**Feeds:** All token files, all templates, material-extraction-protocol routing.

---

#### Q0.2 -- Share Priority Materials

**Question:** For websites, provide URL(s). For files, share or describe. Prioritize:
1. Any styled deck or presentation
2. Logo files
3. Website URL
4. Any brand/style document

**Why:** The agent will READ each material and extract design parameters following `material-extraction-protocol.md`. A single pitch deck can answer 15-20 intake questions automatically.

**Feeds:** All deliverables (via extraction).

---

**Batch 2 (Q0.3)**

#### Q0.3 -- Material Recency

**Question:** For each material shared:
- When was it last updated?
- Has anything changed since?
- Are there elements you **like** vs. elements you want to **change**?

**Why:** Outdated materials may encode decisions already abandoned. "I like the colors but hate the font" is critical context that saves time and prevents wrong extraction.

**Feeds:** Extraction confidence levels, assumption validation.

---

### Phase 0B: Agent Research Tasks

Executed by the agent in parallel with user interaction. Results feed Q0.4 extraction summary.

| R# | Source | Data Points to Extract | Feeds | Method |
|---|---|---|---|---|
| R0.1 | {brand_name}'s website (if URL provided in Q0.2) | Color palette (bg, text, headings, links, CTAs), font families (heading, body), logo (size, placement, variants), spacing patterns, component styles (buttons, cards), navigation pattern, image style | All token files | Chrome MCP (`javascript_tool` for computed CSS) or WebFetch. Follow `material-extraction-protocol.md` Source Type 1. |
| R0.2 | {brand_name}'s LinkedIn company page | Banner image colors/style, avatar/logo version, post visual style, tone alignment | Logo variants, social templates | WebFetch + visual analysis. Follow `material-extraction-protocol.md` Source Type 3. |
| R0.3 | {brand_name}'s pitch deck (if shared in Q0.2) | Slide background colors, heading font/size/color, body font/size, accent/CTA color, logo placement, chart colors, table styling, metric callout style, layout grid, aspect ratio | All token files, all templates | Read file + visual analysis. Follow `material-extraction-protocol.md` Source Type 2. |
| R0.4 | Competitor websites (from brand-config `competitor_names` or ask user) | Color palettes, typography, visual personality, photography style, layout patterns | Design differentiation decisions | WebFetch 2-3 competitor homepages. Follow `material-extraction-protocol.md` Source Type 4. |
| R0.5 | Font availability check | Verify extracted/recommended fonts available on Google Fonts. Check weight coverage. Confirm Remotion bundling compatibility. | Typography tokens, Remotion theme | WebSearch for Google Fonts availability. |

**Research task rules:**
- Start R0.1-R0.3 immediately after Q0.2 answers arrive
- Start R0.4 using `competitor_names` from brand-config (or ask user if not configured)
- Start R0.5 after font names are extracted from R0.1/R0.3
- If a source is unavailable (no website, no deck), skip that task
- All results feed the extraction summary in Q0.4

---

### Phase 0C: System Data Ingestion

**Conditional on brand-config fields.** If the brand-config has `verbal_brand_skill` or `existing_skills`, the agent reads those files for context. If not configured, this phase is skipped entirely.

#### If `verbal_brand_skill` is configured:

| D# | Data Point | Source Path | Feeds |
|---|---|---|---|
| D0.1 | Existing brand identity | `{verbal_brand_skill}/references/brand-identity.md` | Baseline visual identity, tone alignment, banned words |
| D0.2 | Buyer persona profiles | `{verbal_brand_skill}/references/buyer-personas.md` | Audience accent color decisions, template persona adaptations |

#### If `existing_skills.collateral` is configured:

| D# | Data Point | Source Path | Feeds |
|---|---|---|---|
| D0.3 | Existing collateral frameworks | `{skills.collateral}/references/presentation-frameworks.md` | Slide master requirements, component needs |
| D0.4 | Data room standards | `{skills.collateral}/references/data-room-standards.md` | Document template requirements |

#### If `existing_skills.content` is configured:

| D# | Data Point | Source Path | Feeds |
|---|---|---|---|
| D0.5 | Tone and style guide | `{skills.content}/references/tone-and-style-guide.md` | Typography density, layout spacing preferences |

**If no existing skills:** Skip Phase 0C entirely. The intake compensates with additional context from Phase 0D questions.

---

### Phase 0D: Extraction Processing & Gap List (Q0.4-Q0.12)

After all materials are processed and research tasks complete, the agent:
1. Extracts design parameters following `material-extraction-protocol.md`
2. Maps extracted values to token groups with confidence levels (High/Medium/Low)
3. Generates an extraction summary table
4. Presents assumptions to user for validation

**Batch 3 (Q0.4)**

---

#### Q0.4 -- Extraction Validation

**Question:** "From your [materials], I've extracted these design decisions:

[Extraction summary table per `material-extraction-protocol.md` output format -- colors, typography, layout, components, with confidence levels and sources]

For each row, tell me:
- **(a) Correct and keep** -- I'll lock this value into the token system
- **(b) Close but adjust** -- tell me how to change it
- **(c) Wrong** -- I want something different"

**Why:** Validates assumptions before they propagate through all 488 tokens. Single most important validation question in the entire intake.

**Feeds:** All token files (single most important validation).

**Special handling:**
- If Q0.1 = all "doesn't exist" → skip Q0.4 (nothing to extract)
- If only some materials exist → extraction summary only covers available sources
- High-confidence extractions default to (a) unless user says otherwise
- Low-confidence extractions are flagged and asked explicitly

---

**Batch 4 (Q0.5-Q0.6)**

#### Q0.5 -- What to KEEP

**Question:** What do you want to **keep** from your current visual identity? What's working well?

**Why:** Positive constraints are stronger than preferences. "Keep" decisions lock values and reduce future questions.

**Feeds:** Extraction confidence boost, design-recommendations scope narrowing.

---

#### Q0.6 -- What to CHANGE

**Question:** What do you want to **change** about your current visual identity? What's not working?

**Why:** Negative constraints prevent perpetuating problems. "Change" decisions exclude values from the token system.

**Feeds:** Extraction exclusion list.

**Special handling:**
- If Q0.1 = all "doesn't exist" → skip Q0.5 and Q0.6 (no existing identity to keep/change)

---

**Batch 5 (Q0.7-Q0.8)**

#### Q0.7 -- Most Urgent Output

**Question:** What is the most urgent visual output you need?
- (a) Pitch deck / investor presentation
- (b) Website / landing page
- (c) Social media content
- (d) Video / animation
- (e) One-pager / leave-behind document
- (f) Full brand system (all of the above)
- (g) Other: ___

**Why:** Determines which completeness thresholds to prioritize. A "pitch deck" answer means Presentation threshold (70%) is the target; Phase 3 (layout) becomes critical path.

**Feeds:** Completeness matrix priority ordering, deliverable generation sequence.

---

#### Q0.8 -- Preference Strength

**Question:** How strong are your visual identity preferences?
- (a) **Clear preferences and decisions** -- I know what I want
- (b) **Instincts but nothing formal** -- I'll know it when I see it
- (c) **No preferences** -- recommend everything for me

**Why:** Controls questioning depth and engine activation:
- (a) = ask all questions, expect specific answers
- (b) = ask all questions, provide options with recommendations
- (c) = design-recommendations-engine generates defaults for every domain; user confirms/rejects

**Feeds:** Phase routing, conditional branching, engine activation level.

---

**Batch 6 (Q0.9-Q0.10)**

#### Q0.9 -- Admired Brands

**Question:** Name 1-3 brands (any industry) whose **visual style** you admire. For each, tell me what specifically you like about their look.

**Why:** Design-by-reference is the fastest aesthetic capture for non-designers. "I like Stripe's clean typography" immediately informs font weight, spacing, and color decisions.

**Feeds:** Color direction, typography direction, overall aesthetic compass.

---

#### Q0.10 -- Emotional Response

**Question:** Choose **up to 2** emotional responses you want people to have when they first see {brand_name} materials:
- (a) Trust and stability
- (b) Innovation and energy
- (c) Precision and rigor
- (d) Warmth and partnership
- (e) Speed and momentum
- (f) Authority and scale

**Why:** Maps directly to design variables. This is the design direction compass:
- Trust + Precision → deep cool colors, serif or clean sans, generous spacing
- Innovation + Speed → bright accents, bold weights, tighter spacing
- Warmth + Partnership → warm palette, rounded shapes, relaxed spacing
- Authority + Scale → dark surfaces, heavy weights, wide margins

**Feeds:** Color temperature, typography weight, spacing density, design-recommendations-engine calibration.

---

**Batch 7 (Q0.11-Q0.12)**

#### Q0.11 -- Primary Audience

**Question:** Who is the primary audience for your **first** visual output?

Options generated dynamically from brand-config `audience_segments`:
- (a) {audience_segments[0].name} -- {audience_segments[0].description}
- (b) {audience_segments[1].name} -- {audience_segments[1].description}
- ... (one option per segment)
- (n) Mixed / all audiences equally

**Why:** Primary audience expectations shape the default aesthetic. A government buyer expects conservative. A startup buyer expects modern.

**Feeds:** Template priority, default component styling, data density.

---

#### Q0.12 -- Brand Personality Spectrum

**Question:** Rate {brand_name} on each axis (1-5):

| Axis | 1 | 5 |
|------|---|---|
| (a) | Traditional | Modern |
| (b) | Serious | Playful |
| (c) | Conservative | Bold |
| (d) | Corporate | Startup |
| (e) | Minimal | Expressive |

**Why:** Five-axis personality mapping = quantitative backbone of the design-recommendations-engine. Every design decision can be traced back to these scores:
- Typography: serious (1-2) → heavier weights; playful (4-5) → lighter weights
- Spacing: minimal (4-5) → generous white space; expressive → tighter, more content
- Color: conservative (1-2) → muted; bold (4-5) → saturated
- Radius: traditional (1-2) → sharp corners; modern (4-5) → rounded

**Feeds:** All design-recommendations-engine decisions, every token group.

---

## Phase 1: Color Identity

**Purpose:** Define the complete color system. 10 core + 6 conditional = 16 questions.

**Prerequisite:** Phase 0 complete. Extracted colors validated in Q0.4. Personality scores from Q0.12.

### Core Questions

**Batch 8 (Q1.1-Q1.2)**

---

#### Q1.1 -- Primary Brand Color **[ENGINE]**

**Question:**
- [If extracted from materials and confirmed in Q0.4:] "Your primary color is {extracted_hex}. Confirmed."
- [If not extracted:] "What is {brand_name}'s primary brand color? Provide a hex code, describe it (e.g., 'deep navy'), or say 'recommend.'"

**Why:** The primary color drives 60% of the visual system. Every surface, heading, accent, and data visualization derives from this single decision.

**Feeds:** `primitives.color.primary.*`, `semantic.color.brand.primary`, Tailwind `primary`, CSS `--color-primary-*`, Figma `primary` collection.

**Engine trigger:** If user says "recommend" → activate `design-recommendations-engine.md` Section "Primary Color Recommendation" using brand-config `industry` + `tone_keywords` + Q0.10 emotional response + Q0.12 personality scores.

---

#### Q1.2 -- Primary Shade Range

**Question:** I'll generate a 10-shade scale (50-950) from your primary color. Should the shades be:
- (a) **Neutral-leaning** -- lighter shades desaturate toward gray (corporate, understated)
- (b) **Saturated** -- lighter shades keep color intensity (vibrant, energetic)
- (c) **Recommend** based on personality

**Why:** 10 shades enable backgrounds (50-100), borders (200-300), body text (700-800), and headings (900-950) from one hue family. The saturation curve affects the entire feel.

**Feeds:** `primitives.color.primary.50` through `primitives.color.primary.950`, Tailwind shade scale, CSS shade variables.

---

**Batch 9 (Q1.3-Q1.4)**

#### Q1.3 -- Secondary/Accent Color **[ENGINE]**

**Question:**
- [If extracted and confirmed:] "Your secondary color is {extracted_hex}. Confirmed."
- [If not:] "What secondary/accent color should {brand_name} use for CTAs, highlights, and key actions? Hex code, description, or 'recommend.'"

**Why:** Creates visual hierarchy. Primary = identity; secondary = action. Without a distinct secondary, CTAs blend into content.

**Feeds:** `primitives.color.secondary.*`, `semantic.color.brand.secondary`, all exports secondary values.

**Engine trigger:** If "recommend" → engine generates 2 options contrasting with primary, informed by industry and domain accent context.

---

#### Q1.4 -- Domain-Specific Accent

**Question:**
- [If brand-config has `domain_specific_accent`:] "{brand_name}'s {accent.context} concept needs visual distinction. Should it get:
  - (a) Its own warm/cool accent tone (separate from secondary)
  - (b) Use the secondary color for this context
  - (c) No separate color needed"
- [If no `domain_specific_accent` in config:] "Does {brand_name} have a key concept, product line, or differentiator that deserves its own visual accent color? (e.g., a service tier, product category, key technology). If yes, describe it."

**Why:** Domain accents create instant visual associations in data visualization, infographics, and templates. They add semantic meaning beyond decorative use.

**Feeds:** `semantic.color.brand.accent`, `primitives.color.accent.*`, template context-specific zones.

---

**Batch 10 (Q1.5-Q1.6)**

#### Q1.5 -- Neutral Palette

**Question:** For backgrounds, borders, and body text, should {brand_name}'s neutral palette be:
- (a) **Cool grays** -- blue-tinted (tech, corporate)
- (b) **Warm grays** -- yellow/brown-tinted (approachable, human)
- (c) **True grays** -- no color tint (universal, clean)

**Why:** Neutrals occupy 60-70% of any page. The temperature of your grays is one of the most impactful sub-conscious design decisions.

**Feeds:** `primitives.color.neutral.*` (10 shades), background/border defaults in all exports.

---

#### Q1.6 -- Palette Breadth

**Question:** How many color families does {brand_name} need?
- (a) **Tight (3 hues):** primary, secondary, neutral only. Clean and focused.
- (b) **Moderate (5 hues):** + accent + error. Covers most UI needs.
- (c) **Full (8 hues):** + tertiary, info, success. Needed if each audience gets a visual accent or if complex UI states are required.

**Why:** Determines primitive color hue count. Full palette needed if each audience segment gets a visual accent (Q1.7). Tight palette keeps things simpler but limits flexibility.

**Feeds:** Number of primitive hue families, Figma variable collections scope.

---

**Batch 11 (Q1.7-Q1.8)**

#### Q1.7 -- Audience-Specific Accents

**Question:** Should each audience segment have a subtle accent color for audience-specific materials?
- (a) **Yes** -- each segment gets a visual accent (enables per-audience template styling)
- (b) **No** -- same palette for everyone
- (c) **Primary audiences only** -- accents for top 2-3, neutral for others

**Why:** Different audiences have different expectations. Color coding helps agents automatically adapt materials per audience without manual intervention.

**Feeds:** `semantic.color.audience.*` (dynamic count from brand-config `audience_segments`).

---

#### Q1.8 -- Data Visualization Palette

**Question:** For charts, graphs, and data tables, should the palette be:
- (a) **Monochromatic** -- shades of primary color (simple, cohesive, works for <4 series)
- (b) **Multi-hue (6 series)** -- primary + 5 harmonious distinct colors (best for complex charts)
- (c) **Audience-matched** -- each data series uses the audience accent it represents

**Why:** Charts must be distinguishable, accessible (color-blind safe), and on-brand. The wrong chart palette breaks visual consistency.

**Feeds:** `semantic.color.data.*` (9 tokens: 6 series + positive + negative + neutral).

---

**Batch 12 (Q1.9-Q1.10)**

#### Q1.9 -- Dark Backgrounds

**Question:** Should {brand_name} materials use dark background sections?
- (a) **Yes** -- for hero sections, key reveals, dramatic emphasis
- (b) **No** -- all light backgrounds
- (c) **Presentations only** -- dark slides for key moments, light documents

**Why:** Dark sections signal importance and create visual rhythm. But they need inverse surface tokens, inverse text colors, and adjusted component variants. Scope matters.

**Feeds:** `semantic.color.surface.inverse`, `semantic.color.text.inverse`, dark slide masters.

---

#### Q1.10 -- Color Exclusions

**Question:** Are there any colors {brand_name} should **never** use? (e.g., competitor's signature color, culturally inappropriate, negative association)

**Why:** Prevents accidental competitor association or brand confusion. Exclusion rules propagate through all token tiers and the design-recommendations-engine.

**Feeds:** Exclusion rules in design-recommendations-engine, validation check V.3.

---

### Conditional Questions (Phase 1)

#### Q1.1a -- Primary Color Recommendation **[CONDITIONAL]**

**Trigger:** Q1.1 answer = "recommend"

**Action:** Design-recommendations-engine generates 2 options based on `{industry}` + `{tone_keywords}` + Q0.10 + Q0.12. Present as:

"Based on {brand_name}'s {industry} positioning and {tone} voice, I recommend:
- **Option A:** {hex} ({color_name}) -- {rationale}
- **Option B:** {hex} ({color_name}) -- {rationale}
Which do you prefer, or would you like something different?"

**Feeds:** `primitives.color.primary` base value.

---

#### Q1.3a -- Secondary Color Recommendation **[CONDITIONAL]**

**Trigger:** Q1.3 answer = "recommend"

**Action:** Engine generates 2 options contrasting with confirmed primary, informed by industry profile and domain accent temperature.

**Feeds:** `primitives.color.secondary` base value.

---

#### Q1.7a -- Audience Accent Mapping **[CONDITIONAL]**

**Trigger:** Q1.7 = (a) yes or (c) primary only

**Action:** Engine generates proposed accent mapping from brand-config `audience_segments`:

"Proposed audience accent colors:
| Audience | Accent | Rationale |
|---|---|---|
| {segment_1.name} | {hex} | {why this color for this audience type} |
| {segment_2.name} | {hex} | ... |
...

Confirm, adjust, or reject each."

**Feeds:** `semantic.color.audience.*` (all segments).

---

#### Q1.9a -- Dark Mode Scope **[CONDITIONAL]**

**Trigger:** Q1.9 = (a) yes

**Action:** "Dark surfaces will use {primary-900}. Which contexts should use dark mode?
- (a) All outputs (presentations, documents, video, web)
- (b) Presentations only
- (c) Social media + video only"

**Feeds:** Dark mode token variants, dark slide master inclusion/exclusion.

---

#### Q1.6a -- Full Palette Hues **[CONDITIONAL]**

**Trigger:** Q1.6 = (c) full

**Action:** "Confirm these 8 hue families:
1. Primary: {confirmed}
2. Secondary: {confirmed}
3. Neutral: {confirmed}
4. Accent: {from Q1.4}
5. Error: {engine recommendation -- typically red-based}
6. Tertiary: {engine recommendation}
7. Info: {engine recommendation -- typically blue-based}
8. Success: {engine recommendation -- typically green-based}

Adjust any?"

**Feeds:** Additional primitive hue families beyond primary/secondary/neutral.

---

#### Q1.10a -- Exclusion Confirmation **[CONDITIONAL]**

**Trigger:** Q1.10 = specific colors named

**Action:** "Confirmed exclusions: {list}. These will be:
- Blocked from all generated palettes
- Flagged if any token value falls within hue range
- Noted in validation check V.3

Correct?"

**Feeds:** Exclusion validation propagation across all tiers.

---

## Phase 2: Typography

**Purpose:** Define the complete type system. 10 core + 4 conditional = 14 questions.

**Prerequisite:** Phase 1 complete (colors inform typography contrast needs).

### Core Questions

**Batch 13 (Q2.1-Q2.2)**

---

#### Q2.1 -- Heading Font Family **[ENGINE]**

**Question:**
- [If extracted and confirmed in Q0.4:] "Your heading font is {extracted_font}. Confirmed."
- [If not:] "What font should {brand_name} use for headings? Name a specific font, describe what you want (e.g., 'clean geometric sans-serif'), or say 'recommend.' Must be available on Google Fonts or freely licensable."

**Why:** The heading font establishes brand personality in every document, presentation, and video. Must render numbers well for data-heavy brands. Must support all required languages.

**Feeds:** `primitives.font.family.heading`, Tailwind `fontFamily.heading`, Remotion font config, Figma text styles.

**Engine trigger:** If "recommend" → engine uses industry profile + Q0.12 personality scores + Q0.10 emotional response to recommend 2 options with rationale.

---

#### Q2.2 -- Body Text Font

**Question:** For body text (paragraphs, bullets, descriptions), should {brand_name} use:
- (a) **Same font as headings** (different weights) -- single-family system, cohesive
- (b) **Separate body font** -- adds contrast, more traditional typographic hierarchy
- (c) **Recommend**

[If (b):] Name the font or say "recommend."

**Why:** Single-family is simpler to maintain and looks clean. Dual-family adds visual richness but requires careful pairing. The right answer depends on personality scores.

**Feeds:** `primitives.font.family.body`, Tailwind `fontFamily.body`, Remotion font config.

---

**Batch 14 (Q2.3-Q2.4)**

#### Q2.3 -- Monospace Font **[ENGINE]**

**Question:** Does {brand_name} need a monospace font for data contexts (tables, technical specs, code snippets)?
- (a) **Yes** -- name it or say "recommend"
- (b) **No** -- body font handles all contexts
- (c) **Recommend**

**Why:** Monospace aligns numbers in columns and signals "data" context. Critical for brands that present financial models, technical specs, or performance metrics.

**Feeds:** `primitives.font.family.mono`, `semantic.typography.data`, Tailwind `fontFamily.mono`.

---

#### Q2.4 -- Heading Weight

**Question:** How heavy should {brand_name}'s headings be?
- (a) **Bold (700)** -- strong authority, commands attention
- (b) **Semibold (600)** -- confident but approachable
- (c) **Medium (500)** -- understated, elegant, modern

**Why:** Weight directly maps to personality axis (b) Serious ↔ Playful and (c) Conservative ↔ Bold. Heavier weights signal authority; lighter weights signal sophistication.

**Feeds:** `primitives.font.weight.*`, `semantic.typography.h1-h4` weight values.

---

**Batch 15 (Q2.5-Q2.6)**

#### Q2.5 -- Text Density

**Question:** How much breathing room should text have?
- (a) **Airy (1.75 line-height)** -- generous, premium feel, easy scanning
- (b) **Balanced (1.5)** -- standard readability, efficient use of space
- (c) **Dense (1.25)** -- compact, data-rich, maximum information per page

**Why:** Line-height cascades to paragraph spacing, section margins, and overall layout density. This single decision affects 30+ spacing tokens.

**Feeds:** `primitives.font.lineHeight.*`, `spacing.layout.*`, Tailwind `lineHeight`.

---

#### Q2.6 -- Minimum Font Size

**Question:** What's the smallest acceptable text in {brand_name} materials?
- (a) **10px** -- legal footnotes, dense data tables
- (b) **12px** -- readable footnotes, comfortable captions
- (c) **14px** -- accessibility-first, no small text

**Why:** Sets the floor for footnotes, citations, source attributions, and legal disclaimers. Directly impacts the font size scale (how many steps between minimum and display size).

**Feeds:** `primitives.font.size.xs`, template footnote/citation styles.

---

**Batch 16 (Q2.7-Q2.8)**

#### Q2.7 -- Heading Case Treatment

**Question:** How should {brand_name} headings be capitalized?
- (a) **Sentence case** -- "Our energy solutions" (modern, conversational)
- (b) **Title Case** -- "Our Energy Solutions" (traditional, formal)
- (c) **ALL CAPS for H1 only** -- "OUR ENERGY SOLUTIONS" for main titles, sentence case for sub-headings
- (d) **Other** -- describe your preference

**Why:** Consistent capitalization is one of the most noticeable (and most commonly violated) brand rules. Must be defined once and enforced everywhere.

**Feeds:** Typography transform rules in all templates.

---

#### Q2.8 -- Font Size Scale

**Question:** What range of font sizes does {brand_name} need?
- (a) **Compact (12-36px)** -- suited for dense documents, data-heavy presentations
- (b) **Standard (12-48px)** -- balanced range for most materials
- (c) **Dramatic (12-60px)** -- impact numbers, hero statements, big metrics

**Why:** The scale range determines how many size steps exist and how dramatic the contrast between body text and display headings. Data-forward brands often need dramatic scales to make key metrics visually dominant.

**Feeds:** `primitives.font.size.*` (all 10 sizes), Tailwind `fontSize`, Remotion text sizes.

---

**Batch 17 (Q2.9-Q2.10)**

#### Q2.9 -- Number Formatting

**Question:** How should numbers appear in tables and data displays?
- (a) **Tabular figures** -- all digits same width for column alignment (recommended for data-heavy brands)
- (b) **Proportional figures** -- natural spacing, looks better in body text
- (c) **Old-style figures** -- varying heights, traditional/editorial feel

**Why:** Every table, chart, metric card, and financial model uses numbers. Tabular figures align perfectly in columns; proportional look better in sentences. This setting propagates to font feature settings (`font-variant-numeric`) across all templates.

**Feeds:** Font feature settings in typography composites, table cell formatting, CSS `font-variant-numeric`.

---

#### Q2.10 -- Bilingual Visual Distinction **[CONDITIONAL on brand-config]**

**Trigger:** Brand-config has `secondary_language` set.

**Question:** {brand_name} produces materials in both {primary_language} and {secondary_language}. When both languages appear together, how should they be distinguished?
- (a) **No visual distinction** -- same styling for both
- (b) **Language badge** -- small label indicating language (e.g., "EN" / "NL")
- (c) **Different weight** -- secondary language in lighter weight
- (d) **Different accent color** -- secondary language uses accent tint

**Why:** Bilingual materials need clear visual parsing. Without distinction, readers can't quickly identify which language they're reading.

**Feeds:** Language-aware template rules, language badge component spec.

---

### Conditional Questions (Phase 2)

#### Q2.1a -- Font Recommendation **[CONDITIONAL]**

**Trigger:** Q2.1 = "recommend"

**Action:** Engine recommends 2 options based on industry + personality + emotional response:
"Based on {brand_name}'s profile, I recommend:
- **Option A:** {font_name} -- {rationale}
- **Option B:** {font_name} -- {rationale}
Both are on Google Fonts with full weight range."

**Feeds:** `primitives.font.family.heading`.

---

#### Q2.2a -- Body Font Pairing **[CONDITIONAL]**

**Trigger:** Q2.2 = (b) separate, and body font = "recommend"

**Action:** Engine recommends pairing based on heading font + personality.

**Feeds:** `primitives.font.family.body`.

---

#### Q2.3a -- Monospace Recommendation **[CONDITIONAL]**

**Trigger:** Q2.3 = "recommend" or (c)

**Action:** Engine recommends monospace font. Default: JetBrains Mono (excellent at small sizes, free, wide language support). Alternative: Fira Code, Source Code Pro.

**Feeds:** `primitives.font.family.mono`.

---

#### Q2.10a -- Language Badge Specification **[CONDITIONAL]**

**Trigger:** Q2.10 = (b) language badge

**Action:** "Language badge spec:
- Position: top-right of content block
- Size: `font.size.xs` with `font.weight.medium`
- Background: `neutral-100`
- Border: `neutral-300`, `radius.sm`
- Text: ISO 639-1 code uppercase (e.g., 'EN', 'NL')

Confirm or adjust?"

**Feeds:** Language badge component specification.

---

## Phase 3: Layout, Spacing & Grid

**Purpose:** Define spatial relationships, grid systems, and page structure. 10 core + 4 conditional = 14 questions.

**Prerequisite:** Phase 2 complete (typography sizes inform spacing scale).

### Core Questions

**Batch 18 (Q3.1-Q3.2)**

---

#### Q3.1 -- Layout Alignment

**Question:** What's {brand_name}'s default content alignment?
- (a) **Left-aligned** -- standard, professional, good for data-heavy content
- (b) **Centered** -- dramatic, works for minimal content slides
- (c) **Mixed** -- left-aligned body text, centered headings/hero sections

**Why:** Fundamental grid decision that affects every slide master, document page, and video composition. Consistency here prevents layout chaos across materials.

**Feeds:** Slide master grid system, content alignment in all templates.

---

#### Q3.2 -- White Space Level

**Question:** How much white space should {brand_name} materials have?
- (a) **Generous** -- premium feel, breathing room, fewer elements per page (multiplier 1.5x)
- (b) **Moderate** -- balanced density, standard spacing (multiplier 1.0x)
- (c) **Tight** -- data-dense, maximum content per page (multiplier 0.75x)

**Why:** This single answer sets spacing multipliers across ALL templates. Generous white space signals premium/luxury; tight spacing signals data-density and efficiency.

**Feeds:** `spacing.layout.*`, `spacing.component.*`, template margin multipliers.

---

**Batch 19 (Q3.3-Q3.4)**

#### Q3.3 -- Slide Aspect Ratio

**Question:** What slide format does {brand_name} primarily use?
- (a) **16:9** -- standard widescreen, modern, best for screen presentations
- (b) **4:3** -- traditional, still used in some corporate/government contexts
- (c) **Both** -- primary 16:9 with 4:3 variant

**Why:** Determines slide master dimensions, Remotion composition dimensions, and content safe zones. Cannot be changed retroactively without re-laying-out every slide.

**Feeds:** Slide master dimensions (width/height), Remotion composition dimensions.

---

#### Q3.4 -- Border Radius

**Question:** What corner style should {brand_name} components use?
- (a) **Sharp (0px)** -- precise, technical, authoritative
- (b) **Slight (4-8px)** -- modern professional, clean
- (c) **Rounded (12-16px)** -- friendly, approachable, consumer-feel
- (d) **Mixed** -- sharp for data/tables, rounded for CTAs/cards

**Why:** Border radius is a strong personality signal. Sharp corners = technical precision. Round corners = friendly approachability. Must be consistent to avoid visual chaos.

**Feeds:** `primitives.radius.*` (6 tokens), Tailwind `borderRadius`, component radius values.

---

**Batch 20 (Q3.5-Q3.6)**

#### Q3.5 -- Base Spacing Unit

**Question:** What base spacing unit should {brand_name} use?
- (a) **4px** -- finer control, more spacing options, best for complex UIs
- (b) **8px** -- simpler scale, more consistent, best for documents/presentations

The full scale is derived harmonically: base, 2x, 3x, 4x, 6x, 8x, 12x, 16x, 24x.

**Why:** Every margin, padding, gap, and offset in the entire system is a multiple of this base unit. 4px gives 4/8/12/16/24/32/48/64/96. 8px gives 8/16/24/32/48/64/96/128/192.

**Feeds:** `primitives.space.*` base, harmonic scale derivation, Tailwind `spacing`.

---

#### Q3.6 -- Table Styling

**Question:** How should tables look in {brand_name} materials?
- (a) **Bordered + alternating rows** -- traditional, easy to read, structured
- (b) **Minimal borders** -- header line only, clean, modern
- (c) **Card-style rows** -- each row is a card with shadow/radius, very modern

**Why:** Tables are central for comparison-heavy, data-forward brands. The table style must work in presentations, documents, and web/UI contexts.

**Feeds:** `component.table.*`, slide table component, document table layout.

---

**Batch 21 (Q3.7-Q3.8)**

#### Q3.7 -- Metric Display Style

**Question:** When {brand_name} presents key numbers (revenue, performance metrics, statistics), how should they appear?
- (a) **Large bold inline** -- number is part of the text flow, just bigger/bolder
- (b) **Metric card** -- number in a bordered/shaded card with label below
- (c) **Full-width banner** -- number spans full width with dramatic size
- (d) **Mixed** -- cards for groups of metrics, banners for single hero numbers

**Why:** How key numbers LOOK is one of the highest-visibility design decisions. Every investor deck, performance report, and landing page displays metrics.

**Feeds:** `component.card.metric`, `semantic.typography.display`, metric template zones.

---

#### Q3.8 -- Document Cover Page

**Question:** For documents (reports, one-pagers, proposals), what cover page style?
- (a) **Full-color background** -- brand color fills the page, white text
- (b) **White with accent stripe** -- clean with colored strip/bar
- (c) **Minimal** -- logo + title + date, maximum white space
- (d) **Photographic with overlay** -- photo background with brand color overlay + text

**Why:** First page = first impression. The cover style sets expectations for the entire document.

**Feeds:** `templates/document/page-masters.md` cover definition.

---

**Batch 22 (Q3.9-Q3.10)**

#### Q3.9 -- Content Safe Area

**Question:** How much margin should surround content on slides and pages?
- (a) **Standard (10%)** -- content fills most of the frame
- (b) **Generous (15%)** -- noticeable breathing room around edges
- (c) **Tight (5%)** -- maximum content area, data-dense

**Why:** Safe areas prevent content clipping on different screens/projectors and create consistent breathing room. Too tight = cramped; too generous = wasted space.

**Feeds:** `spacing.layout.slide-margin`, template safe zones.

---

#### Q3.10 -- Grid Columns

**Question:** What grid system should templates use?
- (a) **12-column** -- maximum flexibility, standard web grid, complex layouts
- (b) **6-column** -- simpler, best for presentations and documents
- (c) **No explicit grid** -- free-form layout, content-driven

**Why:** The column count determines how agents lay out multi-element slides and pages. 12-column enables halves, thirds, quarters, sixths. 6-column enables halves and thirds.

**Feeds:** Grid definitions in slide masters, multi-column layout rules.

---

### Conditional Questions (Phase 3)

#### Q3.3a -- 4:3 Derivation **[CONDITIONAL]**

**Trigger:** Q3.3 = (c) both

**Action:** "16:9 is primary. The 4:3 variant will:
- Use same token values
- Adjust grid to 4:3 proportions (1024x768)
- Content safe zones proportionally adjusted
- Which is the priority format for generation?" → determines completeness target

**Feeds:** 4:3 variant specs, template priority.

---

#### Q3.6a -- Table Row Limits **[CONDITIONAL]**

**Trigger:** Q3.6 = (c) card-style

**Action:** "Card-style tables need row limits (cards take more vertical space). Maximum rows per page/slide:
- Slides: recommend 5-6 rows
- Documents: recommend 8-10 rows
- Overflow: (a) paginate, (b) switch to minimal borders for overflow

Confirm?"

**Feeds:** `component.table.*` conditional rules.

---

#### Q3.8a -- Cover Color **[CONDITIONAL]**

**Trigger:** Q3.8 = (a) full-color

**Action:** "Full-color cover will use:
- (a) Primary color (`primary-800` or `primary-900`)
- (b) Dark neutral (`neutral-900`)
- (c) Custom color: ___

Text will be white. Logo variant should be reversed/white."

**Feeds:** `templates/document/page-masters.md` cover color.

---

#### Q3.2a -- Data-Slide Spacing Override **[CONDITIONAL]**

**Trigger:** Q3.2 = (a) generous AND brand needs data-dense slides

**Action:** "Generous spacing is set globally. For data-heavy slides (comparison tables, financial models), should spacing:
- (a) Stay generous (fewer rows/columns per slide, more slides)
- (b) Override to tight for data slides only (different spacing context)
- (c) Use moderate as compromise"

**Feeds:** Contextual spacing overrides for data-dense slides.

---

#### Q3.11 -- Responsive Breakpoints

**Question:** What screen size breakpoints should {brand_name} templates use?
- (a) **Mobile-first (320, 768, 1024, 1440px)** -- start with phone, scale up (recommended for web-heavy brands)
- (b) **Desktop-primary (768, 1024, 1440px)** -- assume desktop, scale down (recommended for B2B/enterprise)
- (c) **Tablet-optimized (640, 768, 1024, 1280px)** -- all form factors treated equally
- (d) **Custom** -- specify breakpoints

**Why:** Breakpoints determine responsive behavior in HTML exports, Tailwind config, and web templates.

**Feeds:** `primitives.breakpoint.*`, responsive behavior in html-spec, tailwind-config.js breakpoints.

**Recommendation engine:** B2B + enterprise audiences → (b). Consumer/SaaS → (a). Data-heavy dashboards → (c).

---

#### Q3.12 -- Elevation Philosophy

**Question:** How should {brand_name} create visual hierarchy and depth?
- (a) **Shadow-based** -- box-shadows create elevation (Material Design approach, most common)
- (b) **Background-based** -- darker/lighter backgrounds create depth (Carbon Design approach, minimal)
- (c) **Hybrid** -- shadows for floating elements (modals, tooltips), background shifts for sections

**Why:** Elevation strategy affects all layered components: cards, modals, dropdowns, tooltips.

**Feeds:** `primitives.elevation.philosophy`, component shadow defaults, card/modal/tooltip z-index usage.

**Recommendation engine:** Minimal personality (score 4-5) → (b). Standard → (a). Corporate + modern → (c).

---

## Phase 4: Components & UI Elements

**Purpose:** Define reusable UI components. 13 core + 4 conditional = 17 questions.

**Prerequisite:** Phases 1-3 complete (components use colors, typography, and spacing).

### Core Questions

**Batch 23 (Q4.1-Q4.2)**

---

#### Q4.1 -- Button/CTA Style

**Question:** How should buttons and calls-to-action look?
- (a) **Filled** -- solid background color, white text (strong, clear)
- (b) **Outlined** -- border only, transparent background (subtle, secondary)
- (c) **Text-only** -- no background or border, just colored text with underline/arrow

**Why:** Button style sets the interaction personality. Filled = assertive. Outlined = restrained. Text-only = minimal. This applies to CTAs in presentations, documents, and web.

**Feeds:** `component.button.primary`, `component.button.secondary`, `component.button.ghost`.

---

#### Q4.2 -- Callout/Alert Style

**Question:** For callout boxes (tips, warnings, important notes), what style?
- (a) **Left accent border** -- colored left bar, subtle background
- (b) **Full background tint** -- entire box has light color background
- (c) **Icon-led** -- icon floats left, text right, minimal box styling
- (d) **Combination** -- left border + icon + tinted background

**Why:** Callouts appear in documents, presentations, and web content. 5 semantic variants (info, success, warning, error, brand) all need consistent styling.

**Feeds:** `component.callout.*` (5 variants x 6 properties).

---

**Batch 24 (Q4.3-Q4.4)**

#### Q4.3 -- Logo Placement

**Question:** Where should {brand_name}'s logo appear on pages and slides?
- (a) **Top-left on all pages/slides**
- (b) **Bottom-left on all pages/slides**
- (c) **Top-left on first/cover, bottom on subsequent**
- (d) **Top-right on all pages/slides**

**Why:** Logo placement drives the header/footer component design and affects the usable content area on every template.

**Feeds:** `component.header.*`, `component.footer.*`, all template logo zones.

---

#### Q4.4 -- Slide Progress Indicator

**Question:** How should slide decks indicate position/progress?
- (a) **Colored bar** -- thin bar at top or bottom showing progress
- (b) **Section title** -- current section name in header/footer
- (c) **Number only** -- "12 / 24" in corner
- (d) **Section + number** -- "Market Opportunity | 12 / 24"
- (e) **None** -- no progress indicator

**Why:** Progress indicators help audiences track position in long decks. The style must integrate with the header/footer without competing with content.

**Feeds:** `component.header.slide`, slide master header zones.

---

**Batch 25 (Q4.5-Q4.6)**

#### Q4.5 -- Source Citation Format

**Question:** When citing sources or attributing data, what format?
- (a) **Below chart/element** -- "Source: [name], [year]" directly under the data
- (b) **Page footnote** -- numbered footnotes at bottom of page/slide
- (c) **Superscript + footnote block** -- academic style with superscript numbers

**Why:** Standardizes proof point attribution across all materials. Data-forward brands cite sources frequently; inconsistent citation breaks credibility.

**Feeds:** Citation zone in footers, `semantic.typography.caption`.

---

#### Q4.6 -- Chart Styling

**Question:** How should charts and data visualizations look?
- (a) **Minimal** -- no gridlines, no borders, data only (Tufte-inspired)
- (b) **Standard** -- light gridlines, axis labels, clean
- (c) **Branded** -- chart elements use brand colors, custom styling, bold

**Why:** Chart styling must match the overall brand personality. Minimal = precision. Standard = professional. Branded = distinctive.

**Feeds:** `component.chart.*` (axis, grid, tooltip, legend).

---

**Batch 26 (Q4.7-Q4.8)**

#### Q4.7 -- Partner Logo Treatment

**Question:** When showing partner/client logos in {brand_name} materials, how should they appear?
- (a) **Original color** -- logos shown as-is
- (b) **Greyscale** -- all partner logos converted to grey
- (c) **Context-dependent** -- color on partner-focused slides, greyscale in brand-focused contexts

**Why:** Partner logo treatment affects visual consistency. Greyscale ensures the brand's own colors dominate. Original color shows partner respect.

**Feeds:** Logo treatment rules in templates.

---

#### Q4.8 -- Card Elevation

**Question:** How should cards (content containers) show depth?
- (a) **Flat** -- no shadow, distinguished by border or background color only
- (b) **Subtle shadow** -- light shadow for gentle lift
- (c) **Pronounced shadow** -- clear elevation, strong depth
- (d) **Mixed** -- flat for content cards, elevated for metric/interactive cards

**Why:** Card elevation creates visual hierarchy and affects the perceived dimensionality of the design. Flat = modern/minimal. Shadow = depth/richness.

**Feeds:** `component.card.*`, `primitives.shadow.*`.

---

**Batch 27 (Q4.9-Q4.10)**

#### Q4.9 -- Divider Style

**Question:** How should content sections be separated?
- (a) **Thin line (1px)** -- subtle, clean
- (b) **Thick accent line (4px)** -- bold, branded (uses secondary/accent color)
- (c) **White space only** -- no visible divider, sections separated by spacing
- (d) **Brand mark / icon** -- small logo mark or decorative element

**Why:** Dividers control reading flow and visual rhythm. Too many thick dividers = cluttered. No dividers = ambiguous sections.

**Feeds:** `component.divider` tokens, template section break zones.

---

#### Q4.10 -- Badge/Tag Style

**Question:** For status labels, category tags, and audience markers, what shape?
- (a) **Rounded pill** -- fully rounded ends (modern, friendly)
- (b) **Rounded rectangle** -- slight radius (professional, standard)
- (c) **Square** -- no radius (technical, precise)
- (d) **Tinted text** -- no background shape, just colored text

**Why:** Badges appear in tables, cards, lists, and headers. They tag audiences, statuses, categories, and versions. Consistent badge styling prevents visual noise.

**Feeds:** `component.badge.*`.

---

**Batch 28 (Q4.11-Q4.13)**

#### Q4.11 -- Form Input Style

**Question:** For text inputs, selects, and textareas, which visual style?
- (a) **Outlined** -- visible border, transparent background (most common, clear affordance)
- (b) **Filled** -- subtle background fill, border on focus only (Material-inspired, modern)
- (c) **Underlined** -- bottom border only (minimal, editorial)

**Why:** Inputs are the primary interaction surface in forms, filters, and search. Style choice cascades to all form elements (checkbox, radio, select) for consistency. This also determines error/focus ring approach.

**Feeds:** `component.input.*`, `component.checkbox.*`, `component.radio.*`, `component.select.*`.

---

#### Q4.12 -- Modal/Dialog Style

**Question:** For modals and overlay dialogs, which presentation?
- (a) **Centered card** -- floating card with backdrop overlay (standard, works at all sizes)
- (b) **Full-screen on mobile, card on desktop** -- adaptive approach (mobile-friendly)
- (c) **Slide-in panel** -- enters from right or bottom (app-like, preserves context)
- (d) **No modals** -- all interactions inline or page-based

**Why:** Modals handle confirmations, forms, detail views, and alerts. The style choice determines backdrop treatment, animation direction, z-index stacking, and mobile behavior. Must align with elevation philosophy (Q3.12).

**Feeds:** `component.modal.*`.

---

#### Q4.13 -- Loading State Style

**Question:** For loading and skeleton states, which approach?
- (a) **Skeleton shimmer** -- gray placeholder shapes with shimmer animation (content-aware, smooth)
- (b) **Pulse/fade** -- placeholder shapes that pulse in opacity (subtle, low-motion)
- (c) **Spinner only** -- centered spinner, no skeleton shapes (simple, universal)
- (d) **Progress bar** -- determinate or indeterminate bar at top of container

**Why:** Loading states appear during data fetches, page transitions, and lazy-loaded sections. The choice affects perceived performance and motion budget. Skeleton shimmer requires shape definitions for each content type; spinner is simplest to implement.

**Feeds:** `component.skeleton.*`.

---

### Conditional Questions (Phase 4)

#### Q4.1a -- Button Color **[CONDITIONAL]**

**Trigger:** Q4.1 = (a) filled

**Action:** "Filled buttons will use:
- **Primary button:** `primary-600` background, white text
- **Secondary button:** `secondary-500` background, white text
- **Ghost button:** transparent background, `primary-600` text

Adjust any?"

**Feeds:** `component.button.primary.default.background`.

---

#### Q4.2a -- Icon Set **[CONDITIONAL]**

**Trigger:** Q4.2 = (c) icon-led or (d) combination

**Action:** "Callout icons needed. Recommend:
- Info: circle-info (ℹ)
- Success: circle-check (✓)
- Warning: triangle-alert (⚠)
- Error: circle-x (✕)
- Brand: {brand_name} mark or star

Icon style: (a) Outlined, (b) Filled, (c) Duotone?"

**Feeds:** Icon specification in component tokens.

---

#### Q4.10a -- Dark Mode Components **[CONDITIONAL]**

**Trigger:** Q1.9 = (a) yes or (c) presentations only

**Action:** "Dark mode component adjustments:
- Buttons: invert to light text on dark bg
- Cards: `neutral-800` background, `neutral-700` border
- Tables: `neutral-800` header, `neutral-850` alternating rows
- Callouts: darker tint backgrounds

Confirm these dark variants?"

**Feeds:** Dark mode token variants for all components.

---

#### Q4.8a -- Elevation Scope **[CONDITIONAL]**

**Trigger:** Q4.8 = (c) pronounced or (d) mixed

**Action:** "Elevation levels:
- **Default cards:** `shadow.sm` (subtle)
- **Metric cards:** `shadow.md` (moderate)
- **Interactive/hover:** `shadow.lg` (pronounced)
- **Modals/overlays:** `shadow.xl` (maximum)

Confirm hierarchy?"

**Feeds:** `component.card.elevated.shadow` vs `component.card.default.shadow`.

---

## Phase 5: Motion, Animation & Video

**Purpose:** Define motion tokens and video composition specs. 8 core + 4 conditional = 12 questions.

**Prerequisite:** Phases 1-4 complete. Skip detailed questions if Q5.1 = (c) none.

### Core Questions

**Batch 28 (Q5.1-Q5.2)**

---

#### Q5.1 -- Video Content Need

**Question:** Does {brand_name} currently or plan to produce video content?
- (a) **Active** -- currently producing videos, need full motion specs
- (b) **Future** -- planning video content, set sensible defaults now
- (c) **None** -- no video plans, skip detailed motion questions

**Why:** Routes Phase 5 depth. (a) = full 8-question phase. (b) = set defaults, skip details. (c) = skip to Phase 6 with minimal motion tokens.

**Feeds:** Phase 5 routing, completeness matrix video threshold.

---

#### Q5.2 -- Animation Personality **[ENGINE]**

**Question:** How should animations and transitions feel?
- (a) **Minimal** -- subtle fades, quick transitions (200-300ms), almost invisible
- (b) **Moderate** -- smooth entrances, standard timing (300-500ms), noticeable but not flashy
- (c) **Dynamic** -- expressive motion, longer sequences (400-800ms), character and personality

**Why:** Maps directly to motion tokens (durations + easing curves). Also informs video composition timing, slide transitions, and loading states.

**Feeds:** `primitives.duration.*`, `primitives.easing.*`, Remotion animation defaults.

---

**[If Q5.1 = (c) none, skip to Phase 6. If Q5.1 = (b) future, set engine defaults and skip to Phase 6.]**

**Batch 29 (Q5.3-Q5.4)**

#### Q5.3 -- Video Formats

**Question:** What video formats does {brand_name} produce?
- (a) **Social media (1080x1080, 1080x1920, 1920x1080)** -- Instagram/LinkedIn/YouTube
- (b) **Presentation recordings (1920x1080)** -- recorded decks, webinars
- (c) **All formats** -- full range of social + presentation + custom
- (d) **Custom:** specify dimensions

**Why:** Each format needs a Remotion composition with correct dimensions, safe zones, and typography scaling.

**Feeds:** `exports/remotion-theme.ts` dimensions, video template variants.

---

#### Q5.4 -- Frame Rate

**Question:** Default video frame rate:
- (a) **30fps** -- standard, smaller file size, good for most content
- (b) **60fps** -- smoother motion, better for animations and technical content

**Why:** Frame rate affects Remotion composition config and motion token calibration. Higher fps = smoother but larger files.

**Feeds:** `exports/remotion-theme.ts` fps.

---

**Batch 30 (Q5.5-Q5.6)**

#### Q5.5 -- Title Card Design

**Question:** How should video title cards (opening frames) look?
- (a) **Full-color background** -- brand color with centered white text
- (b) **Logo + text on dark** -- dark background, logo top, title center
- (c) **Animated reveal** -- text types/slides in over background
- (d) **Match document cover** -- use same style as Q3.8 answer

**Why:** Title cards are the first frame of every video. Consistency with document covers creates cross-format brand coherence.

**Feeds:** `templates/video/remotion-compositions.md` Title Card spec.

---

#### Q5.6 -- Lower Third Design

**Question:** For speaker names, captions, and labels, how should lower thirds look?
- (a) **Simple bar** -- colored rectangle with white text
- (b) **Glassmorphic** -- frosted glass effect over video
- (c) **Minimal text** -- just text with subtle shadow, no background
- (d) **Branded bar** -- accent color bar with logo mark

**Why:** Lower thirds appear in interviews, recorded presentations, and social content. Must be legible over varied backgrounds.

**Feeds:** `templates/video/remotion-compositions.md` Lower Third spec.

---

**Batch 31 (Q5.7-Q5.8)**

#### Q5.7 -- Text Reveal Animation

**Question:** How should text appear in videos?
- (a) **Fade in** -- opacity 0→1 (subtle, professional)
- (b) **Slide up** -- text enters from below (dynamic, modern)
- (c) **Type on** -- character by character (technical, engaging)
- (d) **Wipe reveal** -- text revealed by a colored wipe (branded, bold)

**Why:** Text reveal is the most common video animation. Must feel consistent with Q5.2 animation personality.

**Feeds:** `templates/video/remotion-compositions.md` text animation.

---

#### Q5.8 -- Transition Style

**Question:** How should scenes transition in videos?
- (a) **Cut** -- instant, no transition (minimal)
- (b) **Cross-fade** -- gradual blend (smooth, professional)
- (c) **Branded wipe** -- brand color sweeps across (distinctive)
- (d) **Push/slide** -- new scene pushes old one out (dynamic)

**Why:** Transition style must match animation personality and be used consistently. Too many different transitions = amateur feel.

**Feeds:** Motion tokens for transitions, template transition specs.

---

### Conditional Questions (Phase 5)

#### Q5.1a -- Future Video Defaults **[CONDITIONAL]**

**Trigger:** Q5.1 = (b) future

**Action:** "Setting video defaults for future use:
- Animation: Moderate (300-500ms, ease curves)
- Format: 1920x1080 primary
- FPS: 30
- Title card: Full-color background
- Lower third: Simple bar
- Text reveal: Fade in
- Transitions: Cross-fade

These are stored but won't block other deliverables. Adjust any?"

**Feeds:** Completeness matrix adjustment.

---

#### Q5.2a -- Dynamic Calibration **[CONDITIONAL]**

**Trigger:** Q5.2 = (c) dynamic

**Action:** "Dynamic animation calibration:
- Entrance: 500ms with bounce easing
- Exit: 300ms with ease-out
- Hover/interactive: 200ms with ease
- Complex sequences: up to 800ms total
- Stagger delay between elements: 50-100ms

Confirm or adjust?"

**Feeds:** Motion token calibration.

---

#### Q5.3a -- Format Derivation **[CONDITIONAL]**

**Trigger:** Q5.3 = (c) all

**Action:** "Full format matrix:
| Format | Dimensions | Use Case |
|---|---|---|
| Landscape | 1920x1080 | YouTube, presentations, webinars |
| Portrait | 1080x1920 | Instagram Stories, TikTok, Reels |
| Square | 1080x1080 | Instagram feed, LinkedIn feed |
| Shorts | 1080x1920 @ 60fps | YouTube Shorts, TikTok |

Each gets its own Remotion composition. Confirm?"

**Feeds:** Video template variant specs.

---

#### Q5.4a -- FPS Per-Composition **[CONDITIONAL]**

**Trigger:** Q5.4 = (b) 60fps

**Action:** "60fps is set as default. Override for specific formats?
- Social media shorts: keep 60fps (smooth scrolling)
- Presentation recordings: downgrade to 30fps (smaller files)?
- Confirm or adjust per-format."

**Feeds:** fps settings per-composition.

---

## Phase 6: Logo & Brand Assets

**Purpose:** Define logo specifications and brand asset rules. 8 core + 3 conditional = 11 questions.

**Prerequisite:** Phases 1-5 complete (logo placement already set in Q4.3).

### Core Questions

**Batch 32 (Q6.1-Q6.2)**

---

#### Q6.1 -- Logo File Inventory

**Question:** What logo file formats does {brand_name} have?
- [ ] SVG (vector, scalable)
- [ ] PNG (raster, transparent background)
- [ ] PNG (raster, on colored background)
- [ ] AI/EPS (Adobe Illustrator source)
- [ ] Figma source file
- [ ] None -- logo not yet designed

**Why:** Determines what variants are available for templates. SVG is preferred for all digital. PNG as fallback. If none, enter placeholder mode.

**Feeds:** All template logo zones, exports, Remotion watermark.

---

#### Q6.2 -- Logo Variants

**Question:** What logo variants exist or are needed?
- [ ] Full logo (mark + wordmark)
- [ ] Mark only (icon/symbol without text)
- [ ] Wordmark only (text without icon)
- [ ] White/reversed (for dark backgrounds)
- [ ] Single-color (for fax, stamp, watermark)
- [ ] Horizontal layout
- [ ] Stacked/vertical layout

**Why:** Different contexts need different variants: mark-only for favicons and watermarks, reversed for dark slides, horizontal for headers, stacked for covers.

**Feeds:** Logo treatment rules, dark/light template variants.

---

**Batch 33 (Q6.3-Q6.4)**

#### Q6.3 -- Logo Clear Space

**Question:** How much clear space (minimum empty area) should surround the logo?
- (a) **Set a rule** -- e.g., "height of the mark" or "width of the 'D'" as minimum padding
- (b) **Generous** -- 2x the mark height
- (c) **Set for me** -- I'll recommend based on logo proportions

**Why:** Clear space prevents the logo from being crowded by other elements. This rule is enforced in every template.

**Feeds:** Template logo padding zones.

---

#### Q6.4 -- Minimum Logo Size

**Question:** What's the smallest the {brand_name} logo should appear?
- (a) **No minimum** -- scale as needed
- (b) **Set minimum** -- specify in pixels or mm
- (c) **Recommend** based on legibility testing

**Why:** Below a certain size, logos become illegible. The minimum size affects favicon specs, watermark sizing, and footer logo sizing.

**Feeds:** Template minimum logo sizing, favicon constraints.

---

**Batch 34 (Q6.5-Q6.6)**

#### Q6.5 -- Favicon / Social Avatar

**Question:** What should {brand_name} use as its favicon and social media avatar?
- (a) Logo mark (icon only)
- (b) First letter(s) in brand font
- (c) Custom icon
- (d) Already have one -- provide file

**Why:** Favicons appear at 16x16 to 512x512px. They must be recognizable at the smallest size. This also feeds video watermarks and social media profile pictures.

**Feeds:** Social media templates, video watermark.

---

#### Q6.6 -- Co-Branding Rules

**Question:** When {brand_name} appears alongside partner logos:
- (a) **Equal sizing** -- both logos same height
- (b) **Brand dominant** -- {brand_name} logo 20-30% larger
- (c) **Context-dependent** -- dominant in own materials, equal in joint materials
- (d) **Specific rules:** describe

**Why:** Co-branding situations are common in partnerships, investor decks, and joint proposals. Clear rules prevent awkward logo sizing.

**Feeds:** Template partner logo zones.

---

**Batch 35 (Q6.7-Q6.8)**

#### Q6.7 -- Logo Misuse Rules

**Question:** What should {brand_name}'s logo NEVER be subjected to? Common rules include:
- [ ] No stretching or distortion
- [ ] No rotation
- [ ] No color changes (beyond approved variants)
- [ ] No effects (shadows, gradients, glows)
- [ ] No placement on busy backgrounds without overlay
- [ ] No cropping
- [ ] Other: ___

Select all that apply, or say "all of the above."

**Why:** Misuse rules are negative constraints that prevent agents from making bad logo decisions. They're enforced in validation check V.6.

**Feeds:** Logo usage constraints (negative rules for agents).

---

#### Q6.8 -- Brand Mark / Icon

**Question:** Does {brand_name} have or need a standalone brand mark (abstract symbol, not the logo)?
- (a) **Have one** -- provide file
- (b) **Part of the logo** -- the mark in the logo works standalone
- (c) **Need one designed** -- I'll create a brief for a designer
- (d) **Don't need one** -- logo is sufficient

**Why:** A standalone mark is used for watermarks, favicons, pattern fills, and decorative elements. It's smaller and simpler than the full logo.

**Feeds:** Video watermark specs, favicon derivation.

---

### Conditional Questions (Phase 6)

#### Q6.1a -- Placeholder Mode **[CONDITIONAL]**

**Trigger:** Q6.1 = none (no logo files)

**Action:** "No logo files available. Templates will use:
- Placeholder: {brand_name} set in heading font, primary color
- Mark placeholder: First letter of {brand_name} in a `primary-600` circle
- All logo zones will have `[LOGO PLACEHOLDER]` markers

When logo files are ready, re-run Phase 6 to populate."

**Feeds:** Template logo zones (placeholder mode).

---

#### Q6.3a -- Clear Space Rule **[CONDITIONAL]**

**Trigger:** Q6.3 = (c) set for me

**Action:** Engine analyzes logo proportions and recommends:
"Recommended clear space: 1x the height of the logo mark on all sides. This provides enough breathing room without wasting space. Applied to all templates."

**Feeds:** Template logo padding calculation.

---

#### Q6.8a -- Brand Mark Brief **[CONDITIONAL]**

**Trigger:** Q6.8 = (c) need one designed

**Action:** "Brand mark design brief:
- **Concept:** Abstract symbol representing {brand_name}'s core value proposition
- **Style:** Match personality scores from Q0.12 (traditional/modern: {score}, etc.)
- **Colors:** Primary color, with reversed variant
- **Size:** Must work at 16x16px (favicon) through 512x512px (social avatar)
- **Usage:** Watermarks, favicons, pattern fills, document decorative elements

This brief is for an external designer. Proceed with placeholder mode for now."

**Feeds:** Brand mark requirements document.

---

## Phase 7: Photography, Imagery & Illustration

**Purpose:** Define visual content guidelines. 7 core + 3 conditional = 10 questions.

**Prerequisite:** Phases 1-6 complete. Photography style must align with color palette and overall personality.

### Core Questions

**Batch 36 (Q7.1-Q7.2)**

---

#### Q7.1 -- Photography Style

**Question:** What photography style fits {brand_name}?

[Options adapt to industry from brand-config:]

For `energy-infrastructure`:
- (a) **Industrial/technical** -- facilities, equipment, infrastructure close-ups
- (b) **Aerial/landscape** -- drone shots, site overviews, scale
- (c) **People at work** -- engineers, operators, professionals in context
- (d) **Abstract/detail** -- textures, patterns, macro shots of technology
- (e) **Mix** -- different styles for different contexts

For `b2b-saas`:
- (a) **Abstract/tech** -- gradients, geometric patterns, screen interfaces
- (b) **People using product** -- team collaboration, screen interaction
- (c) **Conceptual** -- metaphorical imagery (growth, connection, speed)
- (d) **Minimal/none** -- illustrations and graphics only
- (e) **Mix**

For `professional-services`:
- (a) **Corporate portraiture** -- team headshots, office environments
- (b) **Lifestyle** -- professionals in modern work settings
- (c) **Abstract** -- geometric, minimal backgrounds
- (d) **Mix**

[Similar adaptations for other industries]

**Why:** Photography style must match brand personality and audience expectations. Wrong imagery undermines credibility regardless of how good the design system is.

**Feeds:** Image selection guidelines in templates.

---

#### Q7.2 -- Image Treatment

**Question:** Should photos in {brand_name} materials be:
- (a) **Full color** -- no treatment, natural
- (b) **Brand tint** -- semi-transparent brand color overlay
- (c) **Duotone** -- two-color treatment using brand palette
- (d) **Black & white** -- desaturated for sophistication
- (e) **Context-dependent** -- different treatment per material type

**Why:** Image treatment ensures visual consistency even when source photos vary in quality, lighting, and composition.

**Feeds:** Image treatment specifications in templates.

---

**Batch 37 (Q7.3-Q7.4)**

#### Q7.3 -- Image-to-Content Ratio

**Question:** How prominent should imagery be in {brand_name} materials?
- (a) **Image-heavy (60%+)** -- large hero images, full-bleed photos
- (b) **Balanced (30-50%)** -- images support text content
- (c) **Text-heavy (<20%)** -- minimal imagery, data and text dominate
- (d) **Context-dependent** -- image-heavy for marketing, text-heavy for technical

**Why:** Determines how templates allocate space between image zones and content zones. Data-forward brands typically lean text-heavy; consumer brands lean image-heavy.

**Feeds:** Template image zones, slide layout variants.

---

#### Q7.4 -- Icon Style

**Question:** What icon style should {brand_name} use?
- (a) **Outlined** -- line-drawn, modern, clean (Lucide, Heroicons Outline)
- (b) **Filled** -- solid, bold, strong (Heroicons Solid, Phosphor Fill)
- (c) **Duotone** -- two-layer, branded (Phosphor Duotone)
- (d) **Custom illustration** -- unique to brand (requires design)

**Why:** Icons appear in callouts, navigation, feature lists, and diagrams. Consistency in icon style is a strong brand signal.

**Feeds:** Icon specifications, diagram styling rules.

---

**Batch 38 (Q7.5-Q7.6)**

#### Q7.5 -- Diagram Style

**Question:** When {brand_name} uses diagrams (process flows, org charts, architecture diagrams), what style?
- (a) **Clean boxes + arrows** -- minimal, functional, engineering feel
- (b) **Rounded nodes + curves** -- softer, more approachable
- (c) **Isometric / 3D** -- technical illustration style
- (d) **Branded** -- shapes filled with brand colors, custom connectors

**Why:** Diagrams are common in technical presentations and documents. A consistent diagram style prevents the "every-slide-a-different-Lucidchart-export" problem.

**Feeds:** Diagram styling rules in templates.

---

#### Q7.6 -- Background Patterns

**Question:** Should {brand_name} materials use background patterns or textures?
- (a) **None** -- solid colors only, clean and minimal
- (b) **Subtle geometric** -- faint grid, dots, or lines on backgrounds
- (c) **Brand pattern** -- custom repeating pattern derived from brand elements
- (d) **Gradient** -- subtle gradients using brand palette

**Why:** Background treatments add visual interest without competing with content. But overuse creates visual noise.

**Feeds:** Background treatment in slide masters.

---

**Batch 39 (Q7.7)**

#### Q7.7 -- Facility/Product Renders

**Question:** Does {brand_name} use or plan to use rendered images (3D renders, architectural visualizations, product mockups)?
- (a) **Yes, currently** -- provide examples or describe style
- (b) **Planned** -- set style guidelines for future renders
- (c) **No** -- not applicable

**Why:** Renders need style alignment with photography (lighting, angle, color grading) to feel cohesive when mixed in the same materials.

**Feeds:** Render specifications (future reference).

---

### Conditional Questions (Phase 7)

#### Q7.2a -- Brand Tint Opacity **[CONDITIONAL]**

**Trigger:** Q7.2 = (b) brand tint

**Action:** "Brand tint overlay:
- Color: `primary-600` at opacity:
  - (a) 10% -- barely visible, subtle warmth
  - (b) 20% -- noticeable brand color, image still clear
  - (c) 40% -- strong brand presence, image becomes secondary
- Apply to: (a) all images, (b) hero/background images only"

**Feeds:** Image treatment overlay specs.

---

#### Q7.1a -- Photo Context Mapping **[CONDITIONAL]**

**Trigger:** Q7.1 = (e) mix

**Action:** "Photo style mapping per context:
| Context | Style | Rationale |
|---|---|---|
| Cover/hero | {user choice} | First impression |
| Team/about | {user choice} | Human connection |
| Technical | {user choice} | Credibility |
| Case study | {user choice} | Proof |
| Social media | {user choice} | Engagement |

Confirm mapping?"

**Feeds:** Context-specific image selection rules.

---

#### Q7.4a -- Illustration Brief **[CONDITIONAL]**

**Trigger:** Q7.4 = (d) custom illustration

**Action:** "Custom illustration brief for designer:
- **Style direction:** aligned with personality (Q0.12 scores)
- **Color palette:** uses brand primary + secondary + neutral
- **Line weight:** matches border width tokens
- **Minimum set needed:** 20-30 core icons covering common UI needs
- **Format:** SVG, current-color (color controlled by CSS)

Placeholder: use Lucide icons until custom set is ready."

**Feeds:** Illustration brief specifications.

---

## Validation Framework

**Runs after all phases are complete (or after sufficient phases for targeted deliverable).**

7 automated checks verify internal consistency, accessibility, industry benchmarks, completeness, cross-references, extraction validation, and tool compatibility.

---

### V.1 -- Internal Consistency Check

**Method:** Cross-reference answers across phases for contradictions.

| Check | Left Side | Right Side | Contradiction Signal |
|---|---|---|---|
| Emotion ↔ Color | Q0.10 "trust" | Q1.1 bright orange primary | Trust usually requires deep cool tones |
| Personality ↔ Typography | Q0.12 serious=2 | Q2.4 weight=500 (medium) | Serious brands typically use heavier weights |
| Personality ↔ Spacing | Q0.12 minimal=4 | Q3.2 tight | Minimal personality wants generous white space |
| Density ↔ Motion | Q2.5 airy | Q5.2 dynamic | Airy text density usually pairs with subtle motion |
| Cover ↔ Aesthetic | Q3.8 photographic | Q7.3 text-heavy | Photo cover contradicts text-heavy ratio |

**Action:** Surface mismatches to user: "I noticed [contradiction]. These choices may feel inconsistent. Which takes priority?" Resolve before generating deliverables.

---

### V.2 -- Accessibility Compliance Check

**Method:** WCAG 2.1 AA verification on all color pairings.

| Pairing | Required Ratio | Check Against |
|---|---|---|
| Body text on light surface | 4.5:1 | `text.primary` on `surface.default` |
| Body text on dark surface | 4.5:1 | `text.inverse` on `surface.inverse` |
| Heading on light surface | 3:1 | `text.heading` on `surface.default` |
| Small text on light surface | 7:1 (AAA) | `text.secondary` on `surface.default` |
| Button text on primary | 4.5:1 | white on `brand.primary` |
| Button text on secondary | 4.5:1 | white on `brand.secondary` |
| Link text on surface | 4.5:1 | `brand.secondary` on `surface.default` |

Additional:
- Simulate protanopia, deuteranopia, tritanopia on data visualization palette
- Verify each data series remains distinguishable
- Check minimum font size (Q2.6) meets accessibility floor (12px minimum for WCAG)

**Action:** Flag failing pairs with current ratio and required ratio. Propose adjusted hex values that pass while staying close to brand intent. See `accessibility-guide.md` for detailed compliance reference.

---

### V.3 -- Benchmark Comparison Check

**Method:** Compare token values against industry norms from `design-recommendations-engine.md`.

| Token | Brand Value | Industry Norm | Flag If |
|---|---|---|---|
| Primary color temperature | {value} | {industry default} | More than 2 temperature steps away |
| Heading font weight | {value} | {industry default} | Lighter than norm for serious brands |
| Base spacing | {value} | {industry default} | More than 2x difference |
| Border radius | {value} | {industry default} | Sharp corners in consumer context |
| Animation duration | {value} | {industry default} | >2x longer than norm |

**Action:** Flag outliers: "Your [token] is [value], while typical {industry} brands use [norm]. This is [intentional differentiation / potential mismatch]. Keep or adjust?"

---

### V.4 -- Completeness Assessment

**Method:** Score per `completeness-matrix.md` formula.

For each output type:
1. Count tokens with values (not null, not "TODO", references resolved)
2. Calculate group completeness per token group
3. Apply weights per output type
4. Report: Ready (≥threshold) / Partial (40-threshold) / Blocked (<40%)

**Action:** Present completeness table:

| Output Type | Score | Status | Missing |
|---|---|---|---|
| Figma UI | {%} | {Ready/Partial/Blocked} | {list of missing token groups} |
| Claude Code | {%} | ... | ... |
| Remotion Video | {%} | ... | ... |
| Presentation | {%} | ... | ... |
| Document | {%} | ... | ... |

---

### V.5 -- Cross-Reference Alignment Check

**Condition:** Only runs if brand-config has `verbal_brand_skill` set.

**Method:** Read verbal brand references and verify visual decisions align.

| Visual Decision | Verbal Brand Rule | Check |
|---|---|---|
| Color temperature | Tone keywords | Cool palette + "warm" tone = flag |
| Typography formality | Communication style | Playful font + "technically-confident" = flag |
| Spacing density | Content strategy | Dense spacing + "long-form" content = flag |
| Case treatment (Q2.7) | Style guide capitalization | ALL CAPS + "conversational" tone = flag |

**Action:** Flag contradictions: "Your visual system uses [choice] but your verbal brand guide says [rule]. These may conflict. Resolve?"

---

### V.6 -- Material Extraction Validation

**Method:** Review all tokens that originated from material extraction (Phase 0B/0C).

For each extracted token:
- Source: where it was extracted from
- Confidence: High/Medium/Low
- Confirmation status: confirmed in Q0.4 / not confirmed / rejected

**Action:**
- Flag any Medium/Low confidence tokens that weren't explicitly confirmed
- Flag any tokens still using extracted values that the user said "wrong" to in Q0.4
- Report: "{N} tokens were auto-extracted. {X} confirmed, {Y} need review."

---

### V.7 -- Tool Compatibility Check

**Method:** Verify all token values are valid for their target tools.

| Format | Validation | Applies To |
|---|---|---|
| JSON-serializable | All values can be `JSON.stringify()`'d | Remotion theme, Figma variables |
| Valid CSS | All values are valid CSS property values | CSS variables, Tailwind config |
| Valid Tailwind | All values work in Tailwind config | Tailwind config |
| Figma variable types | Color = hex, Number = number, String = string | Figma variables |
| Font availability | All fonts available on Google Fonts or bundled | All typography tokens |
| No circular references | Semantic → Primitive resolution terminates | All token tiers |

**Action:** Flag incompatible values with the specific tool and required format.

---

## Post-Intake Actions

After all phases complete and validation passes:

### 1. Update Brand Config

Write resolved values back to `brand-configs/{brand-slug}.md`:
- `resolved_primary_color`
- `resolved_secondary_color`
- `resolved_heading_font`
- `resolved_body_font`
- `resolved_mono_font`
- `resolved_personality`
- `resolved_emotional_response`
- `intake_completeness` (from V.4)
- `intake_date` (today's date)

### 2. Generate Token Files

Populate `tokens/primitives.tokens.json`, `tokens/semantic.tokens.json`, `tokens/component.tokens.json` with all resolved values.

### 3. Generate Exports

Derive `exports/tailwind-config.js`, `exports/remotion-theme.ts`, `exports/figma-variables.json`, `exports/css-variables.css` from token files.

### 4. Generate Templates

Populate `templates/presentation/slide-masters.md`, `templates/presentation/slide-components.md`, `templates/document/page-masters.md`, `templates/video/remotion-compositions.md` with token references.

### 5. Completeness Report

Present final completeness matrix with per-output scores and any remaining gaps.

---

## Quick Reference: Phase Summary

| Phase | Questions | Domain | Key Outputs |
|---|---|---|---|
| 0A | Q0.1-Q0.3 | Material ingestion | Material inventory, shared files |
| 0B | R0.1-R0.5 | Agent research | Extracted design parameters |
| 0C | D0.1-D0.5 | System data | Skill cross-references |
| 0D | Q0.4-Q0.12 | Triage & direction | Personality, emotion, priorities |
| 1 | Q1.1-Q1.10 (+6) | Color identity | Complete color system |
| 2 | Q2.1-Q2.10 (+4) | Typography | Complete type system |
| 3 | Q3.1-Q3.10 (+4) | Layout & spacing | Grid, spacing, page structure |
| 4 | Q4.1-Q4.13 (+4) | Components | UI element specifications |
| 5 | Q5.1-Q5.8 (+4) | Motion & video | Animation tokens, video specs |
| 6 | Q6.1-Q6.8 (+3) | Logo & assets | Logo specs, brand marks |
| 7 | Q7.1-Q7.7 (+3) | Photography & imagery | Visual content guidelines |
| V | V.1-V.7 | Validation | Consistency, a11y, completeness |

**Total: 80 core + 28 conditional = 108 questions. 5 research tasks. 0-5 system data points. 7 validation checks. ~30-38 interaction rounds.**
