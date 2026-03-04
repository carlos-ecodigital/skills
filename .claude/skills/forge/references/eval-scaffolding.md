# Eval Scaffolding

> How to generate test scenarios, grading rubrics, and eval harnesses for each skill.
> Source: Anthropic Demystifying Evals + Andrew Ng Agentic AI + ecosystem analysis
> Last updated: 2026-02-19

## Why Evals Matter

Andrew Ng: "The single biggest predictor of execution quality is whether you can evaluate the output." Skills without evals drift silently. You can't improve what you can't measure.

## Test Scenario Template

For each skill, generate 3-5 test scenarios:

```markdown
## Test Scenario: {Name}

**Input:** {Realistic user request that would invoke this skill}
**Context:** {What files/data should be available — reference files, HubSpot data, etc.}
**Expected behavior:** {Step-by-step what the skill should do}
**Success criteria:** {Specific, measurable outcomes — check these to determine pass/fail}
**Failure indicators:** {What would indicate the skill is broken or underperforming}
**Grader type:** {Code-based | Model-based | Human review}
```

### Field Guidelines

**Input:** Use realistic user requests, not synthetic ones. Base on actual triggers from the skill's description field. Include at least one edge case scenario.

**Context:** List the specific reference files and external data the skill would need. This helps verify the skill's composition rules work correctly.

**Expected behavior:** Number the steps. This is the "golden path" — what should happen in order. Include which tools should be called and which reference files should be loaded.

**Success criteria:** Make these binary (pass/fail). Examples:
- "Output contains all 5 required sections"
- "HubSpot contact was created with correct properties"
- "Follow-up email matches the tone guidelines in content-engine"
- "No domain knowledge from outside the skill's scope appears"

**Failure indicators:** What bad output looks like. Examples:
- "Skill hallucinates data not in reference files"
- "Skill skips intake questions and generates immediately"
- "Output format doesn't match the template"
- "Skill tries to do work that belongs to another skill"

**Grader type:** Select the cheapest adequate grader:
1. **Code-based** (deterministic): Output contains required sections, word count in range, required fields present. Fast, cheap, reliable. Use when success criteria are structural.
2. **Model-based** (LLM-as-judge): Quality, relevance, accuracy, tone. Slower, costs tokens. Use when success criteria are qualitative.
3. **Human review** (gold standard): Domain expert validates. Expensive, slow. Use sparingly — reserve for high-stakes skills (legal, financial).

## Scenario Coverage Requirements

Each skill must have at minimum:

| Scenario Type | Required | Purpose |
|--------------|----------|---------|
| Happy path | 1-2 | Standard invocation with typical input |
| Edge case | 1 | Unusual input, boundary condition, or ambiguous request |
| Scope boundary | 1 | Request that's close to non-scope — skill should defer, not attempt |
| Failure recovery | 0-1 | What happens when a tool call fails or data is missing |

Total: 3-5 scenarios per skill.

## Two Evaluation Levels

### Level 1: End-to-End
"Did the skill produce a usable output for this request?"

Evaluates the final output against success criteria. This is the primary eval. If end-to-end passes, the skill is working.

### Level 2: Component
"Which specific step failed?"

Evaluates individual steps: Did intake gather the right information? Did the right reference files load? Did the tool call return expected data? Did the output template render correctly?

Use Level 2 only when Level 1 fails, to diagnose the root cause.

## Two Reliability Metrics

| Metric | Formula | What It Measures |
|--------|---------|-----------------|
| pass@k | Skill succeeds at least once in k tries | Capability — can the skill do this at all? |
| pass^k | Skill succeeds every time in k tries | Reliability — can the skill do this consistently? |

**For production skills, pass^k matters more than pass@k.** A skill that works 3/5 times is unreliable. Target pass^3 for all test scenarios.

## Eval Generation Process

When building a new skill (W1) or upgrading (W4):

1. **Before building:** Write eval scenarios based on the skill's intended triggers and outputs. This is eval-driven development — define "done" before starting.
2. **During building:** Use scenarios as acceptance criteria. Does each workflow produce output that passes its test?
3. **After building:** Run through all scenarios mentally. Note any failures. Fix before shipping.
4. **During audit (W3):** Re-run scenarios. Compare results against previous scores. Note regressions.

## Example: Eval Scenarios for ops-chiefops

```markdown
## Test Scenario: Weekly Brief Generation

**Input:** "Plan the week. Top priorities: close Westland LOI, prep for investor meeting Thursday, finalize site assessment checklist."
**Context:** HubSpot MCP connected (deals data available). Calendar MCP connected (this week's events). Previous weekly brief exists.
**Expected behavior:**
1. Ask clarifying questions if priorities are vague (skip if specific enough)
2. Pull active deals from HubSpot
3. Pull this week's calendar events
4. Generate weekly brief using the template
5. Include: priorities table, blockers, decisions needed, last week scorecard, calendar preview
**Success criteria:**
- Output follows the Weekly Priority Brief template exactly
- All 5 sections present (priorities, blockers, decisions, scorecard, calendar)
- Priorities limited to max 5 items
- Each priority has: owner, definition of done, deadline
- Calendar preview matches actual calendar data
**Failure indicators:**
- Missing sections in the brief
- More than 5 priorities listed
- Priorities lack owners or deadlines
- Brief exceeds 1 page equivalent (~500 words)
**Grader type:** Code-based (structural check) + Model-based (quality of prioritization)

---

## Test Scenario: Scope Boundary — Content Request

**Input:** "Write me a LinkedIn post about our grid congestion solution"
**Context:** Normal operating context.
**Expected behavior:**
1. Recognize this is a content-engine task, not a chiefops task
2. Redirect: "That's a content-engine task. Invoke content-engine for LinkedIn posts."
3. Do NOT attempt to write the post
**Success criteria:**
- Skill correctly identifies the request as out-of-scope
- Redirects to content-engine by name
- Does not produce a LinkedIn post
**Failure indicators:**
- Skill attempts to write a LinkedIn post
- Skill asks intake questions about the post content
- No mention of content-engine
**Grader type:** Code-based (check for redirect, absence of post content)
```

## Eval Scenario Quick Generator

For any skill, generate scenarios by filling in this matrix:

| Trigger Phrase | Input Example | Expected Output | What Could Go Wrong |
|---------------|---------------|----------------|-------------------|
| [From description] | [Realistic request] | [Key output characteristics] | [Failure mode] |

Then expand each row into a full test scenario using the template above.

## Connecting Evals to the Quality Rubric

The Eval Scaffolding category in `quality-rubric.md` (weight: 10%) scores:

| Score | What's Present |
|-------|---------------|
| 0-2 | No test scenarios |
| 3-4 | 1-2 vague test ideas |
| 5-6 | 3+ scenarios but missing success criteria |
| 7-8 | 3-5 complete scenarios with all fields |
| 9-10 | 5+ scenarios covering happy path + edge cases + scope boundary; grader types specified |

**Minimum for shipping (score ≥75): At least 3 complete scenarios.**
