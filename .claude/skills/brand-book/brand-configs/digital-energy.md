# Brand Configuration: Digital Energy
# Purpose: Production configuration -- all values confirmed by brand owner.
# Created: 2026-02-18
# Last intake: 2026-02-24

brand_name: "Digital Energy"
brand_slug: "digital-energy"
industry: "energy-infrastructure"
geography: "european-dutch"
tone_keywords: ["brave", "sophisticated", "pioneering", "precise", "data-forward", "technically-confident", "honest", "numbers-first"]

tagline: "Fast. Sustainable. Flexible."
one_liner: "Digital Energy builds the infrastructure for abundant decentralised intelligence."
mission: "Build Europe's sovereign AI infrastructure by co-locating data centers on industrial sites, converting waste heat into value, and turning grid scarcity into structural competitive advantage."
vision: "Every megawatt of AI compute in Europe generates a megawatt of useful heat. Digital Energy makes this the default, not the exception."
values: ["Precision", "Speed", "Integration", "Honesty", "Partnership"]
personality: ["Brave", "Sophisticated", "Pioneering"]

audience_segments:
  # Persona 1: Site Partners (Heat Consumers)
  - id: "grower"
    name: "Large-Scale Greenhouse Grower"
    description: "Dutch greenhouse BV owner/director (5+ MW, high-heat crops), seeking free heat and energy cost reduction"
    persona: "site-partner"
  - id: "district-heat"
    name: "District Heating Network"
    description: "Municipal/regional warmtenet operator needing cost-based heat sources under Wcw"
    persona: "site-partner"
  - id: "bess"
    name: "BESS Partner"
    description: "Grid-connected battery energy storage co-location partner"
    persona: "site-partner"
  # Persona 2: Customers (AI Colocation)
  - id: "hyperscaler"
    name: "Hyperscaler"
    description: "Large cloud provider (Azure/AWS/GCP scale) seeking sovereign EU capacity"
    persona: "customer"
  - id: "neocloud"
    name: "Neocloud"
    description: "GPU cloud provider (CoreWeave, Lambda type) seeking affordable MW, low PUE, speed to deploy"
    persona: "customer"
  - id: "ai-enterprise"
    name: "AI Enterprise"
    description: "CTO/VP Infra needing dedicated AI compute with full EU data sovereignty"
    persona: "customer"
  - id: "local-buyer"
    name: "Local Buyer"
    description: "NL/EU enterprise needing local compute with data sovereignty and EU AI Act compliance"
    persona: "customer"
  # Persona 3: Investors
  - id: "seed-venture"
    name: "Seed Venture"
    description: "Early-stage VC for company growth capital"
    persona: "investor"
  - id: "project-equity"
    name: "Project Finance (Equity)"
    description: "Infrastructure equity investors for individual DEC projects"
    persona: "investor"
  - id: "project-debt"
    name: "Project Finance (Debt)"
    description: "Project debt providers for DEC deployment financing"
    persona: "investor"

verbal_brand_skill: "de-brand-bible"

competitor_names:
  - "QTS (hyperscale data centers)"
  - "Aligned Data Centers"
  - "Vantage Data Centers"
  - "Nordic colocation (Sweden/Finland)"
  - "Hyperscaler cloud (AWS/Azure/GCP)"

primary_language: "en"
secondary_language: "nl"

domain_specific_accent:
  context: "heat-recovery"
  temperature: "warm"

existing_skills:
  collateral: "collateral-studio"
  content: "content-engine"
  positioning: "positioning-expert"
  fundraising: "seed-fundraising"

# ============================================================
# Resolved after intake -- CONFIRMED VALUES (not defaults)
# ============================================================

resolved_primary_color: "#0034AF"       # DE Dark Blue -- primary brand color from brand book
resolved_secondary_color: "#63E234"     # DE Green -- energy accent from brand book
resolved_accent_color: "#16D3F2"        # DE Sky Blue -- technology accent from brand book
resolved_heading_font: "Saira SemiCondensed"  # Brand book confirmed heading font
resolved_subheading_font: "Orbitron"    # Brand book confirmed subheading font
resolved_body_font: "Inter"             # Brand book confirmed body font (confirmed by owner)
resolved_mono_font: "JetBrains Mono"    # Technical data contexts (kW/rack, PUE, EUR/MWh)
resolved_grey: "#64748B"                # Slate 500 -- resolved from incorrect #63E254

resolved_personality:
  traditional_modern: 4       # Modern-leaning but not trendy
  serious_playful: 2          # Serious -- infrastructure, investor trust
  conservative_bold: 4        # Bold -- "Brave" personality trait
  corporate_startup: 3        # Mix -- serious infrastructure but startup speed
  minimal_expressive: 4       # Minimal -- data-forward, clean, no decoration

resolved_emotional_response:
  - "trust-stability"
  - "precision-rigor"
  - "forward-momentum"

resolved_neutral_palette: "cool-gray"
# Slate-tinted grays (#F8FAFC to #020617). Blue undertone complements primary Dark Blue (#0034AF).
# Source: primitives.tokens.json color.neutral.* -- Tailwind Slate palette.
# Grey (brand-book-named): #64748B (Slate 500) -- resolved 2026-02-24.

intake_completeness: 95  # All 18 questionnaire items answered; grey resolved; mission locked
intake_date: "2026-02-24"

# ============================================================
# Brand Color Summary (from brand book PNG + corrections)
# ============================================================
# Green:          #63E234  (primary accent -- energy, sustainability)
# Sky Blue:       #16D3F2  (secondary accent -- technology, digital)
# Dark Blue:      #0034AF  (primary brand -- headers, CTAs, professional materials)
# Dark Blue Alt:  #0234AF  (near-identical variant)
# Grey:           #64748B  (Slate 500 -- resolved from incorrect #63E254)
# White:          #FFFFFF
# Black:          #000000
# Gradient:       #63E234 -> #16D3F2 -> #0034AF (3-stop linear, logo icon + hero sections)
#
# Fonts: Saira SemiCondensed (headings), Orbitron (subheadings), Inter (body)
# Tagline: "Fast. Sustainable. Flexible."
# Branding: Standalone "Digital Energy" -- no "Group", no "By EcoDigital Group"
