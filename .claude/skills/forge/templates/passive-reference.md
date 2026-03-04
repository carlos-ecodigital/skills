# Template: Passive Foundation

> Use this template for shared data sources that other skills reference. Not directly invoked.
> Exemplar: `de-brand-bible` (score: 86)
> Version: v1

```markdown
---
name: {skill-name}
description: >-
  Shared {domain} foundation for all Digital Energy {category} skills. Contains
  {data type 1}, {data type 2}, {data type 3}, and {data type 4}. This skill is
  referenced by {skill-1}, {skill-2}, {skill-3}, and {skill-4}. It is not typically
  invoked directly but provides the authoritative source of truth for {what it
  provides} produced by any {category} skill.
---

# {Title}

## Purpose

This skill is the single source of truth for {domain data}. Other skills reference these files to ensure consistency across all outputs.

**Not directly invoked by users.** Instead, other skills load specific reference files from this skill when they need {data type}.

## Contents Index

| File | Contains | Used By |
|------|----------|---------|
| `references/{file-1}.md` | {Description} | `{skill-1}`, `{skill-2}` |
| `references/{file-2}.md` | {Description} | `{skill-3}`, `{skill-4}` |
| `references/{file-3}.md` | {Description} | All {category} skills |
| `references/{file-4}.md` | {Description} | `{skill-5}` |

## Usage by Other Skills

### How to reference this skill's data:
Skills should load specific files from this skill's `references/` directory when they need authoritative {domain} data. Load only the files relevant to the current task.

### Which skills use this:
| Skill | What It Uses | When |
|-------|-------------|------|
| `{skill-1}` | {file-1}, {file-2} | {When/why} |
| `{skill-2}` | {file-3} | {When/why} |
| `{skill-3}` | All files | {When/why} |

## Update Protocol

- **Frequency:** {How often this data should be reviewed — monthly, quarterly, etc.}
- **Trigger:** Update when {specific event occurs — new data available, strategy changes, etc.}
- **Process:** {Who updates, how to validate, how to notify dependent skills}
- **Cascade check:** After updating, verify that dependent skills' outputs still align with new data.
```

## Reference File Requirements

Passive Foundation skills are ALL reference files. The SKILL.md is minimal (purpose, index, usage guide, update protocol). Reference files should be:

- **Authoritative:** Single source of truth — if two skills disagree, this one wins
- **Structured:** Tables, lists, matrices — not prose
- **Stable:** Data that changes infrequently (personas, brand guidelines, proof points)
- **Cross-referenced:** Each file notes which skills use it

## Usage Notes

- Description should explicitly state "not typically invoked directly"
- No workflows in SKILL.md — this is a data source, not an executor
- Keep reference files comprehensive but structured (tables > paragraphs)
- Update protocol prevents data staleness
- When changes cascade to dependent skills, note the impact
