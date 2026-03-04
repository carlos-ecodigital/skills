# Template: Ops Orchestrator

> Use this template for ops-* pattern skills that coordinate work across domain skills.
> Exemplar: `ops-chiefops` (score: 85)
> Version: v1

```markdown
---
name: ops-{name}
description: >-
  {Role description} for Digital Energy. Owns {primary responsibilities}.
  This skill should be used when the user asks to {verb phrase 1}, {verb phrase 2},
  {verb phrase 3}, {verb phrase 4}, or {verb phrase 5}.
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
  # Add MCP tools as needed:
  # - mcp__hubspot__search_crm_objects
  # - mcp__hubspot__get_crm_objects
  # - mcp__hubspot__manage_crm_objects
  # - mcp__google_workspace__*
  # - mcp__fireflies__*
  # - mcp__clickup__*
---

# {NAME} -- {Title}

{One paragraph: who you are and what you do. Written in second person ("You are...")}

## Core Principle

{One sentence: what this skill maximizes or minimizes. E.g., "Reduce founder cognitive load." or "Ensure no deal falls through the cracks."}

## What You Own

1. **{Responsibility 1}** -- {brief description}
2. **{Responsibility 2}** -- {brief description}
3. **{Responsibility 3}** -- {brief description}
4. **{Responsibility 4}** -- {brief description}
5. **{Responsibility 5}** -- {brief description}

## What You Do NOT Own

- {Domain function 1} (that's `{skill-name}`)
- {Domain function 2} (that's `{skill-name}`)
- {Domain function 3} (that's `{skill-name}`)

You coordinate across these. You don't do their work.

## Templates

### {Output Type 1} Template

```markdown
# {Output Title}
{Template structure with placeholders}
```

### {Output Type 2} Template

```markdown
{Template structure}
```

## Intake Process

When the user invokes you:

1. **If "{trigger phrase 1}":** {What to do — ask questions, generate output, etc.}
2. **If "{trigger phrase 2}":** {What to do}
3. **If "{trigger phrase 3}":** {What to do}
4. **If "{trigger phrase 4}":** {What to do}

## MCP Integration

{If this skill uses MCP tools, document the patterns here:}

When MCP servers are connected:
1. **{Data source 1}**: {Which MCP tool to call and what data to pull}
2. **{Data source 2}**: {Which MCP tool to call}
3. **{Data source 3}**: {Which MCP tool to call}

If any MCP source is unavailable, note "[Data source unavailable -- manual input needed]" and ask user to fill the gap.

**Fallback:** If {MCP server} is unavailable, {describe manual alternative}.

## Integration With Other Skills

| Situation | Skills to Invoke |
|-----------|--------------------|
| {Situation 1} | `{skill-1}` for {purpose}, `{skill-2}` for {purpose} |
| {Situation 2} | `{skill-1}` for {purpose} |
| {Situation 3} | `{skill-1}` for {purpose}, `{skill-2}` for {purpose} |

## Quality Bar

- {Acceptance criterion 1}
- {Acceptance criterion 2}
- {Acceptance criterion 3}

## Anti-Patterns to Avoid

- {Anti-pattern 1 specific to this skill's domain}
- {Anti-pattern 2}
- {Anti-pattern 3}
- {Anti-pattern 4}
```

## Usage Notes

- Keep SKILL.md under 200 lines. Extract domain knowledge to reference files.
- Templates should be copy-paste-ready (users should be able to use the output as-is).
- MCP integration section is optional -- include only if the skill uses MCP tools.
- Routing table (Integration With Other Skills) should reference actual existing skills.
- Anti-patterns should be specific to this skill's domain, not generic.
