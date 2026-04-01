---
name: sector-overlay-specification
description: Specification for sector-specific market research overlays that extend the canonical market-data.md template
type: reference
version: 1.0
last_updated: 2026-03-31
---

# Sector Overlay Specification

## Purpose

Sector overlays extend the canonical `_shared/market-data.md` template with sector-specific benchmark ranges, additional fields, specialized sources, and domain-specific red flags. The core template is sector-agnostic; overlays add sector depth.

## File Naming Convention

```
_shared/overlays/{sector}-{category}.md
```

**Examples:**
- `energy-c1-sizing.md` — Energy sector market sizing benchmarks
- `dc-ai-c4-comps.md` — Data center / AI sector comparable transactions
- `bess-c3-pricing.md` — Battery storage pricing and revenue stacking
- `fintech-c2-competitive.md` — Fintech competitive landscape benchmarks
- `pharma-c6-regulatory.md` — Pharmaceutical regulatory risk benchmarks

## Required Frontmatter

```yaml
---
sector: [sector-name]            # e.g., "energy", "dc-ai", "bess", "fintech"
category: [C1-C7]               # Which category this overlay extends
last_updated: YYYY-MM-DD
maintainer_skill: [skill-name]   # Which skill maintains this overlay
version: 1.0
parent_schema_version: 2.0       # Version of market-data.md this is compatible with
---
```

## Overlay Structure

Each overlay file must contain these sections in order:

### 1. Sector Context
Brief (2-3 sentences) describing the sector and why standard benchmarks don't apply.

### 2. Benchmark Overrides
Replace "sector-dependent" benchmark ranges from the parent schema with specific values:

```markdown
## Benchmark Overrides

| Parent Field | Parent Range | Sector Range | Source | Notes |
|-------------|-------------|-------------|--------|-------|
| c1_market_cagr | Emerging 20-50% | NL DC: 8-12% constrained | CBRE NL 2025 | Moratorium impact |
| c5_capex_per_unit | Sector-dependent | DC: EUR 6-10M/MW; BESS: EUR 330-700K/MW | T&T DCCI 2025 | — |
```

### 3. Sector-Specific Fields
Additional fields not in the parent schema, marked `[SECTOR-SPECIFIC]`:

```markdown
## Sector-Specific Fields

| Field | Type | Unit | Source Req. | Freshness | Benchmark Range | Notes |
|-------|------|------|-----------|-----------|-----------------|-------|
| `c3_capacity_factor` | Percentage | % | Tier 2+ | <12 months | Solar 10-15%, Wind 25-40%, BESS varies | [SECTOR-SPECIFIC] |
| `c3_degradation_rate` | Percentage | %/yr | Tier 2+ | <12 months | LFP 2-3%, NMC 3-5% | [SECTOR-SPECIFIC] |
```

### 4. Sector-Specific Sources
Named Tier 1 sources specific to this sector:

```markdown
## Key Sector Sources

| Source | Tier | Coverage | Update Frequency |
|--------|------|----------|-----------------|
| BNEF | 1b | Global energy markets | Quarterly |
| IEA World Energy Outlook | 1b | Global energy projections | Annual |
| TenneT Grid Monitor | 1a | NL grid congestion | Monthly |
```

### 5. Sector-Specific Red Flags
Detection criteria unique to this sector:

```markdown
## Sector Red Flags

| Red Flag | Detection | Why It Matters |
|----------|-----------|---------------|
| Claiming moratorium exemption without evidence | No permit reference | NL DC moratorium is broadly applied |
| BESS revenue assuming 100% activation | Revenue > theoretical maximum | FCR/aFRR activation is probabilistic |
```

### 6. Sector-Specific Comp Types
Relevant multiples and asset metrics for the sector:

```markdown
## Sector Comp Metrics

| Metric | Formula | Typical Range | Notes |
|--------|---------|--------------|-------|
| EV/MW | Enterprise Value / Installed MW | DC: EUR 2-5M/MW | Standard for power infra |
| EV/kWh | Enterprise Value / Storage kWh | BESS: EUR 150-400/kWh | Standard for storage |
```

## Rules

1. **Follow parent schema**: Use the same field names, types, and units as `market-data.md`
2. **Override, don't duplicate**: Only include fields where sector benchmarks differ from generic
3. **Add, don't replace**: Sector-specific fields are ADDITIONAL to parent fields
4. **Version compatibility**: `parent_schema_version` must match `market-data.md` version
5. **Single maintainer**: Each overlay has one `maintainer_skill` responsible for updates
6. **No cross-overlay dependencies**: Each overlay is self-contained; overlays don't reference each other

## Loading Priority

When multiple overlays apply (e.g., both `energy-c3-pricing.md` and `bess-c3-pricing.md`), the more specific overlay takes priority:

```
Parent schema (market-data.md)
  └── Sector overlay (energy-c3-pricing.md)
        └── Sub-sector overlay (bess-c3-pricing.md)  ← takes priority
```

## Currently Available Overlays

None yet. First overlays will be created as part of Market Research v3 implementation.

---

*Specification version 1.0 — Last updated 2026-03-31*
