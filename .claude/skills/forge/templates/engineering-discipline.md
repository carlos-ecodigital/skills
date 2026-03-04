# Template: Engineering Discipline

> Use this template for technical calculation/analysis agents from engineering blueprints.
> Source pattern: multi-agent-technical-drafting-system.md (27 agent definitions)
> Version: v1

```markdown
---
name: {discipline-id}
description: >-
  {Engineering discipline} specialist for Digital Energy. Covers {scope summary}.
  Provides standards-referenced calculations, design checks, and technical analysis
  for {application context}. This skill should be used when the user asks about
  {topic 1}, {topic 2}, {topic 3}, {topic 4}, or {topic 5}.
  Also use for "{keyword 1}", "{keyword 2}", "{keyword 3}", "{keyword 4}",
  "{keyword 5}", "{keyword 6}", "{keyword 7}", "{keyword 8}".
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - WebSearch
  - Bash
---

# {ID}: {NAME} -- {Discipline Title}

## Mission

{One sentence: what this discipline agent does and why it matters.}

## Scope

This discipline covers:
- {Scope item 1 with specific technical domain}
- {Scope item 2}
- {Scope item 3}
- {Scope item 4}
- {Scope item 5}

## Non-Scope

| Topic | Handled By |
|-------|-----------|
| {Adjacent discipline 1} | `{other-discipline}` |
| {Adjacent discipline 2} | `{other-discipline}` |
| {Non-engineering topic} | `{domain-skill}` |

## Standards & Methods

| Standard | Scope | Version |
|----------|-------|---------|
| {Standard 1, e.g., NEN 1010} | {What it covers} | {Edition/year} |
| {Standard 2} | {What it covers} | {Edition/year} |
| {Standard 3} | {What it covers} | {Edition/year} |
| {Method 1} | {What it covers} | — |

## Calculation Templates

### {Calculation Type 1}

**When to use:** {Trigger condition}
**Inputs:** {Required data points}
**Method:** {Step-by-step calculation process}
**Output:** {What the calculation produces}
**Validation:** {How to check the result}

### {Calculation Type 2}

**When to use:** {Trigger condition}
**Inputs:** {Required data points}
**Method:** {Step-by-step}
**Output:** {Result format}
**Validation:** {Check method}

## Failure Modes

| Failure Mode | Root Cause | Detection | Prevention |
|-------------|-----------|-----------|------------|
| {Failure 1} | {Why it happens} | {How to detect} | {How to prevent} |
| {Failure 2} | {Why it happens} | {How to detect} | {How to prevent} |
| {Failure 3} | {Why it happens} | {How to detect} | {How to prevent} |

## Resource Ladder

| Accuracy Grade | Required Detail Level | Typical Use |
|---------------|----------------------|-------------|
| Feasibility | Order-of-magnitude, ±30% | Initial site screening |
| Preliminary | Sized components, ±15% | Investment decision |
| Permit-grade | Full engineering, ±5% | Permit application, construction |

## Interface with Domain Agents

| When domain agent asks... | This discipline provides... |
|--------------------------|---------------------------|
| `{domain-skill}`: {request type} | {What this discipline calculates/delivers} |
| `{domain-skill}`: {request type} | {What this discipline calculates/delivers} |

## Quality Bar

- All calculations reference specific standard sections
- Assumptions are explicitly stated
- Results include units and accuracy grade
- Failure mode check completed for every calculation
```

## Reference File Requirements

Engineering Discipline skills need:

| File Type | Purpose | Example |
|-----------|---------|---------|
| Standards tables | Detailed standard references with section numbers | `nen-1010-reference.md` |
| Calculation worksheets | Formulas, worked examples, input/output specs | `cable-sizing-worksheet.md` |
| Equipment specs | Manufacturer data, rated values, selection criteria | `transformer-specifications.md` |
| Code compliance | Checklist format per applicable code | `fire-safety-compliance.md` |
| Failure mode library | Expanded failure modes with root causes | `electrical-failure-modes.md` |

## Usage Notes

- Standards references must include specific section/clause numbers, not just standard names
- Calculation templates are the core value — make them step-by-step reproducible
- Resource ladder ensures appropriate detail level for the project phase
- Interface section prevents discipline agents from doing each other's work
- Bash tool is included for computational tasks (unit conversions, simple calculations)
