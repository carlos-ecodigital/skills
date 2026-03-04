# Quality Rubric

> The scoring system for evaluating skill quality. 10 categories, weighted, 0-100 scale.
> Source: Derived from analysis of 25+ production skills + Anthropic/Ng/Tessl.io research
> Last updated: 2026-02-19

## Existence Test (W7 meta-gate)

Before scoring individual categories, apply this gate:

> If removing this skill creates a gap requiring 2+ hours/week of human work — it's a real skill. If it just reformats text — it's a prompt. Recommend merge or kill.

Skills that fail the existence test are flagged for W7 kill/merge review regardless of their rubric score. A skill can score 80/100 on the rubric and still fail the existence test if it doesn't save real founder hours.

## Scoring Categories

| # | Category | Weight | What 10/10 Looks Like |
|---|----------|--------|-----------------------|
| 1 | Domain Depth | 20% | Reference files contain practitioner-grade knowledge with specific numbers, named sources, comparison matrices, decision frameworks. Expert would recognize as peer-level. |
| 2 | Workflow Clarity | 12% | Clear intake → process → output for every trigger phrase. No ambiguity about what happens when the skill is invoked. Steps are numbered and sequenced. |
| 3 | Integration Design | 12% | Routing table to other skills with specific handoff triggers. Knows when to defer to another skill. Cross-references are bidirectional. |
| 4 | Context Engineering | 10% | Explicit context budget documented. Progressive disclosure: frontmatter for routing, body for instructions, references loaded on-demand. Total references <15K tokens. No context rot. |
| 5 | Tool Design Quality | 10% | Tools declared in allowed-tools match actual usage. MCP tools have documented patterns (search → process → update). Edge cases covered. Poka-yoke error prevention. |
| 6 | Eval Scaffolding | 10% | 3-5 test scenarios shipped with the skill. Each has: realistic input, expected behavior, success criteria, failure indicators. Grader type specified. |
| 7 | Scope Boundaries | 8% | Explicit "What You Own" and "What You Do NOT Own" sections with skill references. No ambiguity about where this skill ends and another begins. |
| 8 | Trigger Coverage | 8% | Description covers all realistic invocation phrases (10+). Includes domain-specific terms, synonyms, and natural language variations. Routing succeeds for 90%+ of relevant requests. |
| 9 | Anti-Pattern Guards | 5% | Documents what NOT to do. Checks against anti-patterns.md. Has explicit anti-patterns section or equivalent guardrails embedded in workflows. |
| 10 | Reference File Ratio | 5% | Follows 75/25 rule: 75%+ of intelligence in reference files, SKILL.md handles orchestration. SKILL.md <250 lines. Reference files have substance (>50 lines each, specific data). |

**Total: 100%**

## Scoring Scale

Each category is scored 0-10:

| Score | Meaning | Description |
|-------|---------|-------------|
| 0-2 | Missing | Category not addressed at all |
| 3-4 | Weak | Present but superficial, generic, or incomplete |
| 5-6 | Adequate | Functional but lacking depth or specificity |
| 7-8 | Strong | Well-executed, specific, and useful |
| 9-10 | Excellent | Gold-standard quality, could serve as exemplar |

**Weighted score** = Σ (category_score × weight × 10)

Example: Domain Depth scores 8/10 → 8 × 0.20 × 10 = 16 out of 20 possible.

## Grade Thresholds

| Grade | Score Range | Meaning | Action |
|-------|------------|---------|--------|
| A | 90-100 | Gold standard | Use as exemplar for other skills |
| B | 75-89 | Production ready | Ship as-is, minor improvements optional |
| C | 60-74 | Needs work | Usable but should be upgraded within 2 weeks |
| D | 40-59 | Significant gaps | Needs rebuild or major upgrade before production use |
| F | 0-39 | Not viable | Rebuild from scratch using appropriate template |

**Minimum shipping score: 75 (Grade B)**

## Gold Standards (Benchmarks)

| Skill | Type | Score | Why It's Good |
|-------|------|-------|---------------|
| `legal-counsel` | Matrix Composer | 94 | 10 specializations × 4 jurisdictions matrix. Deep reference files with specific statutes, case law, and templates. Clear composition rules for loading relevant subsets. |
| `project-financing` | Domain Executor | 91 | Practitioner-grade financial modeling knowledge. Named standards (DSCR, LLCR, PLCR). Dutch-specific reference data. Clear workflow from intake to output. |
| `seed-fundraising` | Domain Executor | 88 | 5 fundraiser archetypes with distinct communication styles. Rich reference files covering deck structure, objection handling, market sizing. |
| `ops-chiefops` | Ops Orchestrator | 85 | Clean coordination model. Templates for weekly brief, decision log, escalation. MCP integration for live data assembly. Clear non-scope. |
| `de-brand-bible` | Passive Foundation | 86 | Authoritative shared data source. 6 detailed buyer personas. Quantified proof points. Used by 4+ other skills. |

## Category Scoring Details

### 1. Domain Depth (20%)

**What to check:**
- Do reference files contain specific numbers, not just concepts?
- Are sources named (standards, regulations, benchmarks)?
- Would a domain expert find this useful or obvious?
- Are comparison matrices or decision frameworks included?
- Is the knowledge current and accurate?

**Scoring guide:**
- 0-2: No reference files, or reference files are empty placeholders
- 3-4: Reference files exist but contain generic information available in any textbook
- 5-6: Some specific data points and frameworks, but gaps in coverage
- 7-8: Practitioner-grade knowledge with named sources and specific numbers
- 9-10: Expert would recognize as peer-level; includes edge cases, exceptions, and nuance

### 2. Workflow Clarity (12%)

**What to check:**
- Does every trigger phrase map to a clear workflow?
- Are intake questions specific and sequenced?
- Is the output format defined (templates, examples)?
- Are quality gates explicit (what must be true before output is delivered)?
- Can you trace a user request from trigger to final output?

**Scoring guide:**
- 0-2: No defined workflows; skill is a blob of instructions
- 3-4: Workflows mentioned but not structured (no intake, no output format)
- 5-6: Some workflows defined but missing steps or output templates
- 7-8: All primary workflows have intake → process → output with templates
- 9-10: Every trigger phrase has a clear workflow; quality gates at each stage

### 3. Integration Design (12%)

**What to check:**
- Is there a routing table showing which skills to invoke for what?
- Are handoff triggers specific ("when X happens, invoke Y")?
- Are cross-references bidirectional (both skills reference each other)?
- Does the skill know when to defer vs when to act?
- Are MCP tool integrations documented with patterns?

**Scoring guide:**
- 0-2: No mention of other skills or integrations
- 3-4: References other skills by name but no routing logic
- 5-6: Basic routing table but handoff triggers are vague
- 7-8: Detailed routing table with specific handoff conditions
- 9-10: Full integration matrix with MCP patterns, fallbacks, and bidirectional references

### 4. Context Engineering (10%)

**What to check:**
- Is the context budget explicit (what loads when)?
- Does SKILL.md stay under 250 lines?
- Are reference files loaded on-demand (not all at once)?
- Is total reference file size under 15K tokens?
- Does the skill use just-in-time data retrieval (tool calls) for volatile data?

**Scoring guide:**
- 0-2: No awareness of context management; everything in one file
- 3-4: Some separation between SKILL.md and references, but no loading strategy
- 5-6: References exist and are separate, but no explicit loading rules
- 7-8: Clear loading rules (composition rules or decision tree for which files to load)
- 9-10: Explicit context budget with progressive disclosure stages documented

### 5. Tool Design Quality (10%)

**What to check:**
- Does allowed-tools match what the skill actually uses?
- Are MCP tool patterns documented (search → process → update)?
- Are edge cases handled (what if the tool call fails)?
- Is there poka-yoke design (preventing misuse)?
- Are tool calls used for volatile data instead of stale references?

**Scoring guide:**
- 0-2: No tools declared or tools don't match usage
- 3-4: Tools declared but no usage patterns documented
- 5-6: Basic tool usage but no edge case handling or fallbacks
- 7-8: Documented tool patterns with edge cases and manual fallbacks
- 9-10: Complete tool design with poka-yoke, fallbacks, and batch-friendly patterns

### 6. Eval Scaffolding (10%)

**What to check:**
- Are there 3-5 test scenarios?
- Does each scenario have: input, expected behavior, success criteria?
- Are failure indicators documented?
- Is the grader type specified (code-based, model-based, human)?
- Do scenarios cover both happy path and edge cases?

**Scoring guide:**
- 0-2: No test scenarios
- 3-4: 1-2 vague test ideas without structure
- 5-6: 3+ scenarios but missing success criteria or failure indicators
- 7-8: 3-5 complete scenarios with all required fields
- 9-10: 5+ scenarios covering happy path, edge cases, and failure modes; grader types specified

### 7. Scope Boundaries (8%)

**What to check:**
- Is there an explicit "What You Own" section?
- Is there an explicit "What You Do NOT Own" section?
- Do non-scope items reference the correct alternative skill?
- Is there clarity about boundary cases?

**Scoring guide:**
- 0-2: No scope definition
- 3-4: Implicit scope from workflow descriptions but nothing explicit
- 5-6: Basic scope defined but non-scope missing or vague
- 7-8: Both scope and non-scope with skill references
- 9-10: Scope and non-scope with boundary case clarification and routing rules

### 8. Trigger Coverage (8%)

**What to check:**
- Does the description field contain 10+ trigger phrases?
- Are domain-specific terms included?
- Are natural language variations covered?
- Would routing succeed for 90%+ of relevant user requests?
- Is the description 150+ characters?

**Scoring guide:**
- 0-2: Description is a generic sentence with no trigger phrases
- 3-4: A few trigger phrases but missing domain terms and synonyms
- 5-6: 5-8 trigger phrases covering main use cases
- 7-8: 10+ trigger phrases with domain terms and synonyms
- 9-10: Comprehensive phrase coverage; includes edge cases, domain jargon, and natural language

### 9. Anti-Pattern Guards (5%)

**What to check:**
- Does the skill document what NOT to do?
- Are common mistakes for this domain addressed?
- Are there guardrails against scope creep?
- Does the skill reference relevant anti-patterns from anti-patterns.md?

**Scoring guide:**
- 0-2: No mention of what to avoid
- 3-4: Generic "don't do X" without specificity
- 5-6: Some domain-specific warnings but not comprehensive
- 7-8: Dedicated anti-patterns section with 3-5 specific items
- 9-10: Anti-patterns tied to specific workflow steps with prevention mechanisms

### 10. Reference File Ratio (5%)

**What to check:**
- Is 75%+ of domain intelligence in reference files?
- Is SKILL.md focused on orchestration, not data?
- Are reference files substantive (>50 lines each)?
- Is SKILL.md under 250 lines?

**Scoring guide:**
- 0-2: All content in SKILL.md, no reference files
- 3-4: Reference files exist but are thin (<50 lines) or contain instructions instead of knowledge
- 5-6: Some domain data extracted to references but SKILL.md still bloated
- 7-8: Clear separation; SKILL.md orchestrates, references hold knowledge
- 9-10: Perfect 75/25 split; reference files are substantive; SKILL.md is lean

## Audit Report Template

```markdown
# Skill Audit: {skill-name}

**Date:** YYYY-MM-DD
**Audited by:** forge
**Skill type:** {composition pattern}

## Score Summary

| Category | Weight | Score (0-10) | Weighted |
|----------|--------|-------------|----------|
| Domain Depth | 20% | X | X.X |
| Workflow Clarity | 12% | X | X.X |
| Integration Design | 12% | X | X.X |
| Context Engineering | 10% | X | X.X |
| Tool Design Quality | 10% | X | X.X |
| Eval Scaffolding | 10% | X | X.X |
| Scope Boundaries | 8% | X | X.X |
| Trigger Coverage | 8% | X | X.X |
| Anti-Pattern Guards | 5% | X | X.X |
| Reference File Ratio | 5% | X | X.X |
| **TOTAL** | **100%** | | **XX.X** |

**Grade:** {A/B/C/D/F}

## Strengths
- [What this skill does well]

## Gaps
| Gap | Category | Impact | Effort | Priority |
|-----|----------|--------|--------|----------|
| [Gap] | [Category] | H/M/L | H/M/L | [1-N] |

## Upgrade Plan
1. [Highest priority fix]
2. [Second priority fix]
3. [Third priority fix]

## Integration Opportunities
- [Connections to other skills not yet made]
```
