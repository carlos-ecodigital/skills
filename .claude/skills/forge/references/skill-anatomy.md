# Skill Anatomy

> The complete structural specification for Digital Energy Claude skills.
> Source: Derived from analysis of 25+ production skills + Anthropic Agent Skills spec (agentskills.io)
> Last updated: 2026-02-19

## YAML Frontmatter Schema

Every SKILL.md starts with YAML frontmatter between `---` delimiters:

```yaml
---
name: skill-name                    # Required. kebab-case identifier
description: >-                     # Required. 3rd person, 150+ chars
  Description here. Include trigger phrases and keywords for routing.
  This skill should be used when the user asks to [trigger phrases].
  Also use for "[keyword1]", "[keyword2]", "[keyword3]".
allowed-tools:                      # Optional. Whitelist of tools the skill can use
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
  - WebSearch
  - mcp__hubspot__*                 # MCP tool patterns with wildcards
  - mcp__google_workspace__*
  - mcp__fireflies__*
  - mcp__clickup__*
---
```

### Field Rules

**name:**
- kebab-case (lowercase, hyphens)
- Ops skills prefix: `ops-` (e.g., `ops-chiefops`, `ops-dealops`)
- Domain skills: descriptive name (e.g., `legal-counsel`, `project-financing`)

**description:**
- Write in third person ("This skill provides..." not "You are...")
- Include 10+ trigger phrases/keywords for reliable routing
- Use "This skill should be used when the user asks to [verbs]"
- End with "Also use for [quoted keyword list]"
- Minimum 150 characters. Aim for 300-500.
- Include domain-specific terms (e.g., Dutch legal terms, engineering standards)

**allowed-tools:**
- Omit field entirely to allow all tools (most skills)
- Include only when restricting tool access for safety or focus
- MCP tools use wildcards: `mcp__hubspot__*` matches all HubSpot operations
- Common sets:
  - Read-only skills: `[Read, Grep, Glob, WebSearch]`
  - Full execution: `[Read, Write, Edit, Grep, Glob, Bash, AskUserQuestion, WebSearch, WebFetch]`
  - With MCP: Add specific `mcp__servername__*` patterns

## Directory Layout

```
.claude/skills/{skill-name}/
├── SKILL.md                    # Required. Instructions + orchestration
├── references/                 # Domain knowledge files
│   ├── {topic-1}.md
│   └── {topic-2}.md
├── examples/                   # Templates, sample outputs
│   ├── {example-1}.md
│   └── {example-2}.md
├── core/                       # Foundational files (Matrix Composer pattern only)
│   ├── {core-1}.md
│   └── {core-2}.md
├── specializations/            # Specialization axis (Matrix Composer only)
│   └── {spec-name}/
│       ├── overview.md
│       └── {detail}.md
└── jurisdictions/              # Jurisdiction axis (Matrix Composer only)
    └── {jurisdiction}/
        └── {topic}.md
```

### When to Use Each Directory

| Directory | When to Use | Example |
|-----------|------------|---------|
| `references/` | Default for all domain knowledge | Most skills |
| `examples/` | Sample outputs, templates, worked examples | content-engine, collateral-studio |
| `core/` | Foundational files shared across specializations | legal-counsel |
| `specializations/` | When skill has 3+ distinct sub-domains with own reference files | legal-counsel (10 specs) |
| `jurisdictions/` | When skill spans multiple legal/regulatory jurisdictions | legal-counsel (4 jurisdictions) |

**Rule:** Use `references/` unless the skill has combinatorial complexity (specialization x jurisdiction). Most skills only need `references/` and optionally `examples/`.

## File Naming Conventions

- All filenames: kebab-case, `.md` extension
- Descriptive names: `deal-economics.md` not `data-1.md`
- Reference files: topic-named (`grid-connection-guide.md`, `buyer-personas.md`)
- Example files: prefixed with what they exemplify (`example-audit-report.md`, `template-one-pager.md`)

## Cross-Referencing

- Reference other skills with backtick names: `legal-counsel`, `ops-dealops`
- Reference files with relative paths from SKILL.md: `references/quality-rubric.md`
- Reference shared resources: `_shared/ops-playbook.md`
- Never use absolute paths in skill files

## Size Guidelines

| Component | Target | Max | Warning Sign |
|-----------|--------|-----|-------------|
| SKILL.md body | 100-200 lines | 250 lines | >250 = extract to references |
| Single reference file | 50-200 lines | 300 lines | >300 = split into sub-files |
| Total reference files | 500-2000 lines | 5000 lines | >5000 = too complex, split skill |
| Description field | 300-500 chars | 1000 chars | <150 = too short for routing |
| Total skill token budget | ~5-15K tokens | ~20K tokens | >15K = context budget concern |

## The 75/25 Rule

- **75%** of a skill's intelligence belongs in reference files (domain knowledge, data tables, frameworks, scoring rubrics, named sources, comparison matrices)
- **25%** belongs in SKILL.md (workflow orchestration, routing logic, cross-references, quality gates, templates)
- If SKILL.md contains domain data (tables of standards, pricing benchmarks, regulatory details) → move to references
- If reference files contain workflow instructions → move to SKILL.md

## Progressive Disclosure (P7)

Token loading stages:

| Stage | What Loads | Token Budget | When |
|-------|-----------|-------------|------|
| Startup | SKILL.md frontmatter (name + description) | ~200 tokens | Always (for routing) |
| Activation | SKILL.md full body | ~2,000-4,000 tokens | When skill is invoked |
| On-demand | Specific reference files | ~500-3,000 per file | When workflow needs them |
| Just-in-time | External data via tool calls | Variable | During execution (HubSpot, web, etc.) |

**Rule:** Never load all reference files at once. Load the ones the current workflow needs.
