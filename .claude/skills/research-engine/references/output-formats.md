# Output Formats

> Brief templates per query type. Every research output follows one of these formats.
> Loaded for Standard Brief and Deep Dive workflows.

## Core Brief Template (Always Present)

Every research brief contains these sections in this order:

```
# Research Brief: {Title}

**Date:** {YYYY-MM-DD}
**Requested by:** {requester or skill name}
**Effort level:** {Quick Lookup / Standard Brief / Deep Dive}
**DE overlay:** {Active — [domains] / Inactive}

## Executive Summary

{3-5 sentences. Lead with the single most important finding. Include confidence context. End with the primary knowledge gap or uncertainty. No claims not supported by Key Findings below.}

## Key Findings

| # | Finding | Confidence | Source Summary |
|---|---------|------------|----------------|
| 1 | {Specific factual claim} | **HIGH** | {Source name} (Tier 1, {date}) + 2 supporting |
| 2 | {Specific factual claim} | **MEDIUM** | {Source name} (Tier 2, {date}) |
| 3 | ... | ... | ... |

## Evidence Table

| Finding # | Source | Tier | Date | URL | Specificity | Quote/Data Point |
|-----------|--------|------|------|-----|-------------|-----------------|
| 1 | {Full source name} | 1 | {YYYY-MM} | {url} | Exact + methodology | "{verbatim quote, max 30 words}" |
| 1 | {Supporting source} | 2 | {YYYY-MM} | {url} | Exact, no methodology | "{data point}" |
| 2 | ... | ... | ... | ... | ... | ... |

## Contradictions & Uncertainties

| Topic | Claim A | Source A | Claim B | Source B | Assessment |
|-------|---------|----------|---------|----------|------------|
| {topic} | {claim} | {source} (Tier {N}) | {claim} | {source} (Tier {N}) | {which is more credible and why} |

{If no contradictions: "No contradictions identified in this research."}

## Knowledge Gaps

| Gap | What Was Searched | Why Unavailable | How to Fill |
|-----|-------------------|-----------------|-------------|
| {description} | {queries tried} | {paywalled / not public / doesn't exist} | {paid report / interview / FOIA} |

{If no gaps: "No significant gaps identified. All sub-questions answered at MEDIUM or higher confidence."}

## Source Bibliography

### Tier 1 Sources
- {Author/Org}. "{Title}." {Date}. {URL}

### Tier 2 Sources
- {Author/Org}. "{Title}." {Date}. {URL}

### Tier 3 Sources (supporting only)
- {Author/Org}. "{Title}." {Date}. {URL}

## Methodology

**Research question:** {original question}
**Decomposition:** {N} dimensions, {N} sub-questions, {N} search blocks
**Execution:** Phase 1: {N} agents. Phase 2: {N} agents. {Phase 3: N agents if Deep Dive.}
**Tool calls:** {N} total
**Critique:** {Self-critique ran / Debate triggered on {topic} / No critique (Quick Lookup)}
**DE overlay:** {Active — compared against {files}. {N} ecosystem updates flagged. / Inactive}

## Recommended Next Steps

1. {Specific, actionable step — e.g., "Commission BNEF BESS report for NL-specific CAPEX data behind paywall"}
2. {Specific, actionable step}
3. {Specific, actionable step}
```

## Quick Lookup Template (Abbreviated)

For Quick Lookup workflows, use this shortened format:

```
# Quick Lookup: {Question}

**Date:** {YYYY-MM-DD}

## Answer

{Direct answer to the question, 1-3 sentences}

**Confidence:** {HIGH/MEDIUM/LOW/PRELIMINARY}
**Source:** {Source name} (Tier {N}, {date}) — {URL}
**Supporting:** {Additional source if available}

## Caveats

{Any important caveats, limitations, or context. If none: omit this section.}
```

## Adaptive Sections Per Query Type

In addition to the core template, add these sections based on query type:

### Market Sizing

Insert after Key Findings:

```
## Market Size Breakdown

| Segment | TAM | SAM | SOM | Growth Rate | Source | Confidence |
|---------|-----|-----|-----|-------------|--------|------------|
| {segment} | {value} | {value} | {value} | {CAGR %} | {source} | {HIGH/MED/LOW} |

### Key Assumptions
- {Assumption 1 with source}
- {Assumption 2 with source}

### Growth Projections
| Year | Low Case | Base Case | High Case | Key Driver |
|------|----------|-----------|-----------|------------|
| {year} | {value} | {value} | {value} | {driver} |
```

### Competitive Intelligence

Insert after Key Findings:

```
## Entity Profiles

### {Company/Entity Name}
- **Founded:** {year} | **HQ:** {location} | **Employees:** {N}
- **Relevant products/services:** {description}
- **Market position:** {description}
- **Key differentiator:** {what sets them apart}
- **Recent moves:** {last 12 months of relevant activity}
- **Source quality:** {Tier 1-2 sources available / Tier 3 only}

{Repeat per entity}

## Competitive Comparison Matrix

| Dimension | {Entity 1} | {Entity 2} | {Entity 3} | Source |
|-----------|------------|------------|------------|--------|
| {dimension 1} | {value} | {value} | {value} | {source} |
| {dimension 2} | ... | ... | ... | ... |

## Strategic Implications
- {Implication 1}
- {Implication 2}
```

### Technology Assessment

Insert after Key Findings:

```
## Technical Comparison

| Dimension | {Tech A} | {Tech B} | {Tech C} | Winner | Source |
|-----------|----------|----------|----------|--------|--------|
| {spec 1} | {value} | {value} | {value} | {which} | {source} |

## Maturity Assessment

| Technology | TRL | Commercial Deployments | Key Vendors | Trajectory |
|-----------|-----|----------------------|-------------|------------|
| {tech} | {1-9} | {count/scale} | {vendors} | {growing/stable/declining} |
```

### Regulatory / Permitting

Insert after Key Findings:

```
## Statute Reference Table

| Regulation | Article/Section | Key Requirement | Effective Date | Source |
|-----------|----------------|-----------------|----------------|--------|
| {law name} | {article} | {what it requires} | {date} | {URL} |

## Process Timeline

| Step | Authority | Typical Duration | Key Risks | Source |
|------|-----------|-----------------|-----------|--------|
| {step} | {who} | {weeks/months} | {risks} | {source} |
```

### Cross-Domain Synthesis

Insert after Key Findings:

```
## Domain Intersection Map

| Domain A | Domain B | Connection | Implication | Confidence |
|----------|----------|------------|-------------|------------|
| {domain} | {domain} | {how they connect} | {what it means} | {HIGH/MED/LOW} |

## Multi-Stakeholder Implications

| Stakeholder | Impact | Opportunity | Risk |
|-------------|--------|-------------|------|
| {stakeholder} | {impact} | {opportunity} | {risk} |
```

## Research Update Template (W4)

For Research Update workflows, use this delta format:

```
# Research Update: {Topic}

**Date:** {YYYY-MM-DD}
**Previous brief date:** {YYYY-MM-DD}
**Update scope:** {what was checked for updates}

## Changes Since Last Brief

| # | Finding | Previous | Updated | Source | Confidence |
|---|---------|----------|---------|--------|------------|
| 1 | {what changed} | {old data} | {new data} | {source} | {label} |

## Confirmed (No Change)

{List of key findings that remain valid}

## New Findings

{Findings discovered in update that weren't in the original brief}

## Updated Knowledge Gaps

{Gaps that were filled + new gaps discovered}
```

## Fact Check Template (W5)

For Fact Check workflows:

```
# Fact Check: {Topic or Claims}

**Date:** {YYYY-MM-DD}

## Verdicts

| # | Claim | Verdict | Evidence | Source | Confidence |
|---|-------|---------|----------|--------|------------|
| 1 | {claim text} | **Confirmed** | {supporting evidence} | {source} (Tier {N}) | HIGH |
| 2 | {claim text} | **Disputed** | {contradicting evidence} | {source} (Tier {N}) | MEDIUM |
| 3 | {claim text} | **Unverifiable** | {no public sources found} | — | — |

## Details

### Claim 1: {claim}
{2-3 sentences of evidence and reasoning for the verdict}

### Claim 2: ...
```

## Ecosystem Data Updates Appendix (DE Overlay Only)

When DE overlay is active and research found newer/better data than ecosystem files:

```
## Appendix: Ecosystem Data Updates

| Data Point | Current Ecosystem Value | Ecosystem Source | Research Value | Research Source | Recommendation |
|---|---|---|---|---|---|
| {metric} | {old} | {_shared/file.md, line N} | {new} | {source} (Tier {N}, {date}) | Update / Keep / Review |

**Note:** Updates to `_shared/` files require explicit user approval.
```
