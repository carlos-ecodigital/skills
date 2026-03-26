---
workflow: build-workflow
version: 1.0.0
owner: forge
trigger: "create a workflow", "new workflow", "document this process", "workflow for [X]"
frequency: ad-hoc
estimated-duration: 15-30 min
inputs:
  - workflow purpose
  - owner skill
  - trigger phrases
  - tools needed
  - output format
outputs:
  - completed workflow .md file
  - workflow library registration
  - owner skill SKILL.md update
tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
last-updated: 2026-03-25
---

# W9: Build Workflow

## Purpose

Self-service workflow creation tool for the DE team. Takes a process description and produces a production-ready workflow `.md` file following DE standards, then registers it in the workflow library.

Anyone on the team can use this to document a repeatable process as a skill workflow.

## Prerequisites

- User knows what process they want to document
- Owner skill exists (or will be created via forge W1 first)

## Steps

### Step 1: Intake

**Who:** User (via AskUserQuestion)
**Tool:** AskUserQuestion
**Input:** User's process description
**Action:** Gather answers to all 7 questions:
1. What does this workflow accomplish? (one sentence)
2. Who triggers it? (user phrase, scheduled event, or system event)
3. Which skill owns it? (existing skill name from ecosystem registry)
4. What tools/MCPs does it need? (Gmail, GCal, ClickUp, HubSpot, web search, etc.)
5. What's the output? (document, email draft, decision, report, data update, etc.)
6. What's the frequency? (daily, weekly, monthly, quarterly, ad-hoc)
7. Estimated duration per run?
**Output:** Completed intake answers
**If blocked:** If user can't answer all 7, proceed with available answers and mark gaps as TBD in the draft.

### Step 2: Collision Check

**Who:** Forge
**Tool:** Read `_shared/workflow-library.md`
**Input:** Proposed trigger phrases from Step 1
**Action:**
1. Search workflow library for matching or overlapping trigger phrases
2. If collision found: warn user, suggest alternative triggers or merging with existing workflow
3. If no collision: proceed
**Output:** Clear to proceed or collision warning
**If blocked:** If workflow library doesn't exist, skip collision check and flag for manual review.

### Step 3: Template Load

**Who:** Forge
**Tool:** Read `forge/templates/workflow.md`
**Input:** Template file
**Action:** Load the workflow template scaffold
**Output:** Template ready for filling
**If blocked:** Use this inline template structure:
```
---
workflow: [name]
version: 1.0.0
owner: [skill]
trigger: "[phrases]"
frequency: [freq]
estimated-duration: [min]
inputs: [list]
outputs: [list]
tools: [list]
last-updated: [date]
---
# [Workflow Name]
## Purpose
## Prerequisites
## Steps
### Step N: [Name]
**Who:** | **Tool:** | **Input:** | **Action:** | **Output:** | **If blocked:**
## Quality Gate
## Handoffs
## Failure Modes
```

### Step 4: Draft Workflow

**Who:** Forge
**Tool:** Write
**Input:** Intake answers + template
**Action:** Fill template from intake answers. For each step in the process:
- **Who:** Agent skill or human
- **Tool:** Specific MCP tool, file operation, or manual action
- **Input:** What data feeds this step
- **Action:** What happens (specific, not vague)
- **Output:** What's produced
- **If blocked:** Recovery path (always required)

Also generate:
- Quality gate with ≥3 measurable criteria
- ≥2 failure modes with detection and recovery
- Handoff table (what goes where after workflow completes)
**Output:** Complete workflow draft
**If blocked:** If intake answers are insufficient for detailed steps, draft skeleton and mark steps as "[DETAIL NEEDED]".

### Step 5: Quality Check

**Who:** Forge
**Tool:** Review (self-critique)
**Input:** Completed draft
**Action:** Verify against checklist:
- [ ] Every step has Who/Tool/Input/Action/Output/If-blocked (all 6 fields)
- [ ] Quality gate exists with ≥3 measurable criteria
- [ ] At least 2 failure modes with detection + recovery
- [ ] Handoffs to other skills are explicit (skill name + what's handed off)
- [ ] Frontmatter is complete (all required fields filled)
- [ ] Duration estimate is realistic for the steps described
- [ ] Trigger phrases don't collide with existing workflows
- [ ] Output format is specified (template or example)

Fix any gaps before proceeding.
**Output:** Quality-checked workflow
**If blocked:** If gaps can't be resolved, present draft to user with gaps flagged for their input.

### Step 6: Write File

**Who:** Forge
**Tool:** Write
**Input:** Quality-checked workflow
**Action:** Save to `{owner-skill}/workflows/{workflow-name}.md`
- Use kebab-case for filename
- Create workflows/ directory if it doesn't exist
**Output:** File written to disk
**If blocked:** If write fails, output the full content for user to save manually.

### Step 7: Register in Library

**Who:** Forge
**Tool:** Read + Edit
**Input:** Workflow metadata
**Action:**
1. Read `_shared/workflow-library.md`
2. Add row to Quick Reference table
3. Add entry to appropriate category section
4. Update total-workflows count in frontmatter
5. Update last-updated date
**Output:** Library updated
**If blocked:** If library doesn't exist, create it. If edit fails, output the row for manual addition.

### Step 8: Update Owner Skill

**Who:** Forge
**Tool:** Edit
**Input:** Workflow metadata
**Action:** Add workflow to owner skill's SKILL.md workflow table:
- New row with: number, workflow name, file path, trigger phrases
- Increment workflow numbering
**Output:** Owner skill SKILL.md updated
**If blocked:** If skill has no workflow table, note for user to add manually.

### Step 9: Present

**Who:** Forge
**Action:** Show user:
1. Complete workflow content (formatted)
2. Library registration confirmation (row added)
3. Owner skill update confirmation (SKILL.md edited)
4. Any TBD items or gaps that need user follow-up
**Output:** User review and approval

## Quality Gate

- [ ] Every step has all 6 fields (Who/Tool/Input/Action/Output/If-blocked)
- [ ] Quality gate checklist has ≥3 measurable criteria
- [ ] At least 2 failure modes documented with detection + recovery
- [ ] Handoff table complete
- [ ] Registered in `_shared/workflow-library.md`
- [ ] Owner skill's SKILL.md workflow table updated
- [ ] No trigger phrase collisions with existing workflows
- [ ] Frontmatter complete and valid

## Handoffs

| Destination | What | When |
|-------------|------|------|
| Owner skill `workflows/` dir | Completed workflow .md file | Step 6 |
| `_shared/workflow-library.md` | Registry entry (row in table) | Step 7 |
| Owner skill `SKILL.md` | Workflow table row | Step 8 |
| `forge/references/forge-learnings.md` | Build log entry | After completion (W8 auto) |

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Owner skill doesn't exist | Glob check for `{skill}/SKILL.md` returns empty | Ask user: create skill first (via forge W1) or assign to existing skill |
| Trigger collision | Library search finds matching trigger phrases | Present collision, suggest modified triggers or merge with existing workflow |
| Template unavailable | Read `forge/templates/workflow.md` fails | Use inline template from Step 3 |
| Intake incomplete | Missing required fields after Step 1 | Proceed with available info, mark gaps as `[TBD]`, flag for user |
| Workflow library missing | `_shared/workflow-library.md` doesn't exist | Create it fresh with this workflow as first entry |
| Write permission denied | Write tool fails | Output full file content for user to save manually |
