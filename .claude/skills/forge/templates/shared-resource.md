# Template: Shared Resource

> Use this template for files in the `_shared/` directory that multiple skills reference.
> Exemplar: `_shared/ops-playbook.md`
> Version: v1

```markdown
# {Resource Name}

> Referenced by: {list of skills that use this resource}
> Update frequency: {weekly | monthly | quarterly | as-needed}
> Last updated: {YYYY-MM-DD}

## Purpose

{What this shared resource provides and why it exists as a shared file rather than inside a single skill.}

## Content

{The structured data, framework, or configuration that multiple skills need.}

### {Section 1}

{Content organized by topic. Use tables for structured data.}

| {Column 1} | {Column 2} | {Column 3} |
|------------|------------|------------|
| {Data} | {Data} | {Data} |

### {Section 2}

{Content}

### {Section 3}

{Content}

## Usage Guide

### How skills should reference this file:
{Instructions for how skills load and use this data.}

### What NOT to do:
- Do not duplicate this data inside individual skills
- Do not modify this file without checking impact on dependent skills
- Do not add skill-specific data here (keep it genuinely shared)

## Dependent Skills

| Skill | What It Uses | How |
|-------|-------------|-----|
| `{skill-1}` | {Section/data} | {How it references this resource} |
| `{skill-2}` | {Section/data} | {How it references this resource} |
| `{skill-3}` | {Section/data} | {How it references this resource} |

## Update Protocol

- **Who updates:** {Which skill or person is responsible}
- **When:** {Trigger events for updates}
- **How:** {Process: edit file → verify dependent skills → update "Last updated" date}
- **Cascade check:** {After updating, what needs to be verified in dependent skills}
```

## When to Create a Shared Resource

Create a `_shared/` resource when:
1. **3+ skills** need the same data
2. The data would otherwise be **duplicated** across skill directories
3. Changes to this data should **cascade** to all dependent skills automatically
4. The data is about **cross-skill coordination** (not domain-specific)

Examples:
- Operating playbook (cadence, governance, tool integration)
- MCP setup guide (shared configuration for all MCP-connected skills)
- Engineering disciplines guide (how engineering agents compose)

## Do NOT create shared resources for:
- Data used by only 1-2 skills (put it in the skill's `references/`)
- Domain-specific knowledge (put it in the relevant domain skill)
- Templates used by only one skill type (put it in forge's `templates/`)
