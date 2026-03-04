# Brand Configuration Schema

Defines the structure for brand-specific configuration files. Each brand gets one config file at `brand-configs/{brand-slug}.md`. The config provides all brand-specific values that parameterize the universal brand-book skill.

## Schema Definition

```yaml
# ============================================================
# REQUIRED FIELDS
# ============================================================

brand_name: string
# Human-readable brand name. Used in intake questions, deliverables, and documentation.
# Example: "Digital Energy"

brand_slug: string
# URL-safe identifier. Used for file naming and config lookup.
# Format: lowercase, hyphens only. Example: "digital-energy"

industry: enum
# Industry classification. Drives design-recommendations-engine defaults.
# Options:
#   energy-infrastructure    — Energy, utilities, infrastructure, data centers, industrial
#   b2b-saas                — Software-as-a-service, cloud platforms, developer tools
#   fintech                 — Financial services, banking, payments, insurance, crypto
#   healthcare              — Medical, pharmaceutical, biotech, health services
#   consumer                — Consumer products, e-commerce, food & beverage, retail
#   deep-tech               — AI/ML, robotics, quantum, semiconductor, aerospace
#   professional-services   — Consulting, legal, accounting, advisory, real estate

geography: string
# Primary operating geography. Affects font language support, regulatory visual conventions,
# and design-recommendations-engine cultural defaults.
# Format: "{region}-{country}" or "{region}"
# Examples: "european-dutch", "north-american", "asia-pacific", "global"

tone_keywords: list[string]
# 3-6 adjectives describing the brand's communication style. These parameterize the
# design-recommendations-engine for typography, spacing, and color decisions.
# Examples: ["precise", "data-forward", "technically-confident", "honest"]
# Examples: ["playful", "bold", "accessible", "warm"]
# Examples: ["conservative", "trustworthy", "institutional", "measured"]

audience_segments: list[object]
# 1-10 distinct buyer/audience segments. Each segment may get a visual accent color
# and template adaptations. Ordered by priority (first = primary audience).
#
# Each segment:
#   id: string         — Unique identifier (lowercase, hyphens). Used in token naming.
#   name: string       — Human-readable name. Used in intake questions and templates.
#   description: string — One-line description. Used by design-recommendations-engine.
#
# Example:
#   - id: "grower"
#     name: "Grower"
#     description: "Dutch greenhouse BV owner/director"
#   - id: "neocloud"
#     name: "Neocloud"
#     description: "GPU cloud provider seeking European colocation"

# ============================================================
# OPTIONAL FIELDS
# ============================================================

verbal_brand_skill: string | null
# Path to the verbal brand skill (relative to .claude/skills/).
# If set, Phase 0C ingests brand-identity.md and buyer-personas.md from this skill.
# Validation check V.5 cross-references visual decisions against verbal brand rules.
# Example: "de-brand-bible"

competitor_names: list[string] | null
# 2-5 key competitors. Used for R0.4 (competitor visual analysis) in Phase 0B.
# If null, the intake asks the user to name competitors.
# Example: ["QTS", "Aligned Data Centers", "Vantage Data Centers"]

primary_language: string
# ISO 639-1 code. Default "en".
# Example: "en", "nl", "de", "fr"

secondary_language: string | null
# ISO 639-1 code. If set, triggers Q2.10 (bilingual visual distinction).
# Example: "nl"

domain_specific_accent: object | null
# If the brand has a key concept that deserves its own visual accent color
# (e.g., a product line, key differentiator, domain-specific concept).
#
# Fields:
#   context: string      — What the accent represents
#   temperature: enum    — "warm" | "cool" | "neutral"
#
# Example:
#   context: "heat-recovery"
#   temperature: "warm"

existing_skills: object | null
# Cross-references to other skills for Phase 0C system data ingestion.
# Each field is a skill name (relative to .claude/skills/).
# If null, Phase 0C is skipped and intake compensates with additional questions.
#
# Fields (all optional):
#   collateral: string   — Skill with presentation-frameworks.md and data-room-standards.md
#   content: string      — Skill with tone-and-style-guide.md
#   positioning: string  — Skill with competitive positioning
#   fundraising: string  — Skill with investor materials
#
# Example:
#   collateral: "collateral-studio"
#   content: "content-engine"
#   positioning: "positioning-expert"

# ============================================================
# POST-INTAKE RESOLVED FIELDS (populated after Create Brand mode completes)
# ============================================================

resolved_primary_color: string | null
# Hex code confirmed during intake Phase 1. Example: "#1B365D"

resolved_secondary_color: string | null
# Hex code confirmed during intake Phase 1. Example: "#22C55E"

resolved_heading_font: string | null
# Font family name confirmed during intake Phase 2. Example: "Inter"

resolved_body_font: string | null
# Font family name. Example: "Inter"

resolved_mono_font: string | null
# Monospace font. Example: "JetBrains Mono"

resolved_personality: object | null
# Five-axis personality scores from Q0.12.
# Fields: traditional_modern (1-5), serious_playful (1-5), conservative_bold (1-5),
#         corporate_startup (1-5), minimal_expressive (1-5)

resolved_emotional_response: list[string] | null
# Up to 2 emotional targets from Q0.10.
# Example: ["trust-stability", "precision-rigor"]

intake_completeness: number | null
# Overall completeness percentage after intake. Example: 85

intake_date: string | null
# ISO 8601 date of last intake completion. Example: "2026-02-18"
```

## Brand Selection Logic

When the brand-book skill is invoked, it MUST determine which brand to operate on:

### Detection Sequence

1. **Scan config directory:** Read all `.md` files in `brand-configs/` (excluding `schema.md`)
2. **Route based on count:**
   - **0 configs:** Prompt user: "I don't have a brand config yet. What brand should we set up?" Then create minimal config from Template below OR start Create Brand intake.
   - **1 config:** Load silently. Parse `brand_name` field and use throughout session.
   - **2+ configs:** Prompt user: "Which brand are you working on?" Show list with `brand_name`, `brand_slug`, and `intake_date` for each.
3. **Validate selection:** After loading, verify required fields are present per Validation Rules below.

### Never Assume

The system MUST NEVER:
- Default to any specific brand (including Digital Energy)
- Load a config based on file order or alphabetical sorting
- Assume the user wants the most recently edited config when multiple exist

Every brand is equal. Selection must be explicit or unambiguous (single config).

---

## Validation Rules

1. **brand_slug** must match the filename: `brand-configs/{brand_slug}.md`
2. **audience_segments** must have at least 1 and at most 10 entries
3. **audience_segments[].id** must be unique within the list
4. **tone_keywords** must have at least 3 entries
5. **industry** must be one of the 7 defined enum values
6. **verbal_brand_skill** if set, the skill directory must exist
7. **existing_skills** if set, each referenced skill directory must exist
8. **resolved_* fields** are only populated after intake; leave null in initial config

## Config Lifecycle

1. **Creation:** User identifies brand → agent creates config from schema with required fields
2. **Enrichment:** During Create Brand intake, resolved fields are populated as answers come in
3. **Completion:** After intake validation, `intake_completeness` and `intake_date` are set
4. **Reference:** Downstream skills and agents read the config to parameterize their output
5. **Update:** Re-running intake updates resolved fields; previous values are overwritten

## Template

```yaml
# Brand Configuration: {Brand Name}
# Created: {date}
# Last intake: {date or "pending"}

brand_name: ""
brand_slug: ""
industry: ""
geography: ""
tone_keywords: []
audience_segments: []

verbal_brand_skill: null
competitor_names: null
primary_language: "en"
secondary_language: null
domain_specific_accent: null
existing_skills: null

# Resolved after intake
resolved_primary_color: null
resolved_secondary_color: null
resolved_heading_font: null
resolved_body_font: null
resolved_mono_font: null
resolved_personality: null
resolved_emotional_response: null
intake_completeness: null
intake_date: null
```
