# Template: Domain Executor

> Use this template for deep-expertise skills that produce specialized outputs.
> Exemplar: `project-financing` (score: 91), `seed-fundraising` (score: 88)
> Version: v1

```markdown
---
name: {skill-name}
description: >-
  {Domain expertise description}. This skill should be used when the user asks to
  {verb phrase 1}, {verb phrase 2}, {verb phrase 3}, {verb phrase 4}, or {verb phrase 5}.
  Also use for "{keyword 1}", "{keyword 2}", "{keyword 3}", "{keyword 4}",
  "{keyword 5}", "{keyword 6}", "{keyword 7}", "{keyword 8}", "{keyword 9}",
  "{keyword 10}".
---

# {Title}

{One paragraph: what this skill provides and its domain authority. Written in second person.}

## Composition Rules

Load reference files based on the user's request:

| If the request involves... | Load these references |
|---------------------------|---------------------|
| {Topic area 1} | `references/{file-1}.md`, `references/{file-2}.md` |
| {Topic area 2} | `references/{file-3}.md` |
| {Topic area 3} | `references/{file-4}.md`, `references/{file-5}.md` |
| Any request | `references/{always-loaded}.md` (core framework) |

## Standard Workflows

### W1: {Primary Workflow} (Intake → Analysis → Output)

**Triggers:** "{trigger 1}", "{trigger 2}", "{trigger 3}"

**Intake:**
1. {Question to understand scope}
2. {Question to understand constraints}
3. {Question to understand desired output}

**Process:**
1. Load relevant reference files per composition rules
2. {Analysis step 1}
3. {Analysis step 2}
4. {Generation step}
5. Quality check against {criteria}

**Output format:**
```markdown
{Template for this workflow's output}
```

### W2: {Advisory Workflow}

**Triggers:** "{trigger 1}", "{trigger 2}"

**Process:**
1. {Step 1}
2. {Step 2}
3. {Step 3}

### W3: {Review Workflow}

**Triggers:** "{trigger 1}", "{trigger 2}"

**Process:**
1. {Step 1}
2. {Step 2}
3. {Step 3}

## Cross-References

| When this comes up... | Defer to... |
|----------------------|-------------|
| {Adjacent domain 1} | `{skill-name}` |
| {Adjacent domain 2} | `{skill-name}` |
| {Ops coordination} | `{ops-skill-name}` |

## Quality Bar

- {Quality criterion 1 — specific, measurable}
- {Quality criterion 2}
- {Quality criterion 3}

## Disclaimers / Limitations

- {Limitation 1 — what this skill cannot do}
- {Limitation 2 — when to seek external expertise}
```

## Reference File Requirements

Domain Executor skills should have 3-8 reference files totaling 500-3000 lines:

| File Type | Purpose | Example |
|-----------|---------|---------|
| Core framework | The central methodology or analytical framework | `deal-structuring-framework.md` |
| Data tables | Specific numbers, benchmarks, standards | `dutch-grid-tariffs.md`, `dscr-benchmarks.md` |
| Decision frameworks | When to use approach A vs B | `equity-vs-debt-decision-tree.md` |
| Templates | Output templates for each workflow | `financial-model-template.md` |
| Named sources | Regulations, standards, benchmarks with citations | `dutch-energy-regulations.md` |

**The 75/25 rule:** 75%+ of the skill's intelligence should be in these reference files. SKILL.md handles routing and quality gates only.

## Usage Notes

- Composition rules are critical — they prevent loading all references at once (context rot).
- Each workflow should have distinct triggers that don't overlap with other skills.
- Cross-references should point to actual existing skills in the ecosystem.
- Disclaimers are important for skills giving advice (legal, financial, technical).
