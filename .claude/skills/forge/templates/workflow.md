---
workflow: {{workflow-name}}
version: 1.0.0
owner: {{skill-name}}
trigger: "{{natural language trigger phrase}}"
frequency: {{daily | weekly | monthly | quarterly | ad-hoc}}
estimated-duration: {{minutes}}
inputs:
  - {{input description with source}}
outputs:
  - {{output description with destination}}
tools:
  - {{MCP tool or skill name needed}}
last-updated: {{YYYY-MM-DD}}
---

# {{Workflow Name}}

## Purpose

{{One sentence: what this workflow accomplishes and why it matters.}}

## Prerequisites

- [ ] {{What must be true before starting}}
- [ ] {{Data/access/tools needed}}

## Steps

### Step 1: {{Action Verb + Object}}

**Who:** {{Role or skill}}
**Tool:** {{MCP tool, skill, or manual action}}
**Input:** {{What you need}}
**Action:** {{Exactly what to do — specific enough for someone unfamiliar to execute}}
**Output:** {{What this step produces}}
**If blocked:** {{Recovery path or fallback}}

### Step 2: {{Action Verb + Object}}

**Who:** {{Role or skill}}
**Tool:** {{MCP tool, skill, or manual action}}
**Input:** {{Output from Step 1 or other source}}
**Action:** {{What to do}}
**Output:** {{What this produces}}
**If blocked:** {{Recovery path}}

### Step N: {{Final Action}}

**Who:** {{Role or skill}}
**Tool:** {{MCP tool, skill, or manual action}}
**Input:** {{What you need}}
**Action:** {{What to do}}
**Output:** {{Final deliverable}}
**If blocked:** {{Recovery path}}

## Quality Gate

- [ ] {{Checklist item that must be true before output is considered done}}
- [ ] {{Another quality check}}

## Handoffs

| Output | Destination | Skill/Person |
|--------|-------------|-------------|
| {{What}} | {{Where it goes}} | {{Who receives}} |

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| {{What can go wrong}} | {{How you know}} | {{What to do}} |
