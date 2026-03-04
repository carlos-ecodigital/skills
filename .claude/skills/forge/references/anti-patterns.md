# Anti-Patterns

> 16 documented failure modes with detection rules and guardrails.
> Source: Anthropic, Devin/Cognition, Tessl.io, CrewAI, Swyx, ecosystem analysis
> Last updated: 2026-02-19

## How to Use This File

During every skill build (W1), audit (W3), or upgrade (W4), run through these anti-patterns as an active checklist. For each one, ask the detection question. If the answer is "yes," apply the guardrail before shipping.

## The 16 Anti-Patterns

### AP-1: Premature Complexity
**Source:** Anthropic ("Most successful implementations use simple, composable patterns")
**Description:** Building multi-agent orchestration when a single-agent skill with tools would work. Over-engineering the composition pattern.
**Detection question:** Could this be solved with a single-agent skill? Would a prompt chain (fixed steps) work instead of dynamic orchestration?
**Guardrail:** Run the simplicity gate in W1 BEFORE designing. Default to the simplest composition pattern. Justify complexity in writing.
**Real example:** Building an "ops-researchops" orchestrator when `ops-targetops` could just add a research workflow.

### AP-2: Framework Opacity
**Source:** Anthropic
**Description:** Skill references frameworks, patterns, or methodologies without explaining the underlying logic. The user (or future skill editor) can't understand WHY the skill does what it does.
**Detection question:** Could someone unfamiliar with the referenced framework understand and modify this skill?
**Guardrail:** Every framework reference must include a brief explanation of the underlying principle. Don't just name-drop "Evaluator-Optimizer" — explain the generate-critique-refine loop.

### AP-3: Poor Tool Design
**Source:** Anthropic ("Multiplicative impact on performance")
**Description:** Tools in `allowed-tools` lack documentation. No example usage, no edge case handling, no poka-yoke error prevention. Tool names are unclear.
**Detection question:** For each tool in allowed-tools: is there a documented usage pattern in the skill's instructions? Are edge cases covered?
**Guardrail:** Tool design checklist: (1) clear name, (2) documented parameters, (3) example usage in instructions, (4) edge case handling, (5) fallback if tool fails.

### AP-4: Missing Evaluation
**Source:** Andrew Ng ("Single biggest predictor of execution quality")
**Description:** Skill ships without test scenarios. No way to verify if the skill works correctly or has regressed.
**Detection question:** Does the skill include 3-5 test scenarios with inputs, expected behavior, and success criteria?
**Guardrail:** Eval scaffolding is REQUIRED for a score ≥75. Use `eval-scaffolding.md` to generate test scenarios during W1.

### AP-5: Bloated Tool Sets
**Source:** Anthropic
**Description:** Skill declares >7 tools in allowed-tools, many with overlapping functionality. Too many tools confuses the model about which to use when.
**Detection question:** Are there >7 tools declared? Do any tools have overlapping functionality? Can any tools be removed without losing capability?
**Guardrail:** Consolidation review: for each tool, justify why it's needed. Merge overlapping tools. Prefer specific tool names over wildcards unless all tools in a group are needed.

### AP-6: Context Rot
**Source:** Anthropic + Harrison Chase
**Description:** Reference files exceed 15K tokens total. SKILL.md exceeds 250 lines. The skill tries to load too much context, degrading performance.
**Detection question:** What's the total token count of all reference files? Is SKILL.md over 250 lines? Are all reference files loaded at once, or on-demand?
**Guardrail:** Context budget check: SKILL.md <250 lines, total references <15K tokens, progressive disclosure (load what's needed per workflow). If over budget, split the skill or extract to on-demand loading.

### AP-7: One-Shotting
**Source:** Anthropic harness
**Description:** Skill tries to solve everything in one pass — no intake, no intermediate steps, no quality gate. Goes straight from user request to final output.
**Detection question:** Does the skill have distinct intake → process → output stages? Are there intermediate checkpoints?
**Guardrail:** Break every workflow into at least: (1) intake (understand the request), (2) process (do the work), (3) output (deliver with quality check). For complex workflows, add more stages.

### AP-8: Over-Autonomy
**Source:** Devin/Cognition
**Description:** Skill takes irreversible actions (sends emails, updates CRM, posts publicly) without explicit user confirmation.
**Detection question:** Does the skill take any actions that affect external systems? Are all such actions gated by user confirmation?
**Guardrail:** Human-in-the-loop checkpoint before ANY: send, post, submit, purchase, delete, publish. Document confirmation points in the workflow.

### AP-9: Stutter-Step Problem
**Source:** Swyx
**Description:** Skill asks for user approval at every micro-step, creating tedious friction. Opposite of AP-8 but equally harmful.
**Detection question:** Does the skill pause for confirmation on low-risk, reversible actions? Are there more than 3 confirmation points in a single workflow?
**Guardrail:** Strategic action exemptions: only confirm at high-stakes moments (external actions, irreversible changes). Internal processing, file reads, and analysis should proceed autonomously.

### AP-10: Model-Specific Coupling
**Source:** Cognition (rebuilt Devin for Sonnet 4.5 due to behavioral differences)
**Description:** Skill assumes model behaviors that vary across Claude versions. Relies on specific output formats, token counting accuracy, or behavioral quirks.
**Detection question:** Would this skill work identically on Claude Opus vs Sonnet vs Haiku? Does it depend on specific model behaviors?
**Guardrail:** Model-aware design: test on both Opus and Sonnet. Avoid relying on exact token counts. Use explicit formatting instructions rather than assuming format compliance.

### AP-11: Vague Instructions
**Source:** Devin/Cognition
**Description:** Skill instructions lack specificity. Uses phrases like "add tests" instead of "add pytest tests for the auth module covering login, logout, and session expiry."
**Detection question:** Could two different instances of Claude interpret these instructions differently? Are there ambiguous phrases?
**Guardrail:** Specificity test: replace every instruction with the most specific version possible. Replace "comprehensive" with exact scope. Replace "thorough" with specific criteria.

### AP-12: Context Anxiety
**Source:** Cognition (Sonnet 4.5 behavior)
**Description:** Skill prompts trigger premature summarization near context limits. The model rushes to finish rather than maintaining quality.
**Detection question:** Is SKILL.md front-loaded with the most important instructions? Are reference files small enough to load without context pressure?
**Guardrail:** Put critical instructions early in SKILL.md. Keep reference files modular (<300 lines each). Use progressive disclosure so the model never feels "full."

### AP-13: Peer-to-Peer Chaos
**Source:** CrewAI
**Description:** Skills communicate directly with each other without a hub-and-spoke structure. No clear orchestration hierarchy.
**Detection question:** Does this skill invoke other skills directly, or does it route through an ops orchestrator? Is the invocation hierarchy clear?
**Guardrail:** Hub-and-spoke: ops skills orchestrate, domain skills execute. Domain skills NEVER invoke other domain skills directly. Cross-domain coordination goes through an ops skill.

### AP-14: Knowledge Cutoff Ignorance
**Source:** Devin/Cognition
**Description:** Skill assumes outdated library patterns, regulations, or standards because the training data has a cutoff.
**Detection question:** Does this skill reference specific versions, dates, or regulations that might change? Is WebSearch available for verification?
**Guardrail:** Point to current docs via WebSearch for volatile information. Include "last updated" dates in reference files. Flag time-sensitive data with review dates.

### AP-15: Scope Creep
**Source:** Ecosystem analysis
**Description:** Skill expands beyond its original brief without explicit approval. Absorbs responsibilities that belong to other skills.
**Detection question:** Is the skill doing anything that overlaps with another skill's "What You Own" section? Has the scope expanded since the original brief?
**Guardrail:** Non-scope section is REQUIRED. Review scope against the ecosystem registry. If overlap is detected, resolve by either: (a) merging the skills, (b) clarifying boundaries, or (c) splitting the overlapping function into a shared resource.

### AP-16: Orphan Skill
**Source:** Ecosystem analysis
**Description:** Skill exists in isolation — not referenced by any other skill, not part of any workflow chain, not used by any ops orchestrator.
**Detection question:** Is this skill referenced in any other skill's routing table? Does any ops skill invoke it? Is it part of any workflow chain?
**Guardrail:** Integration table is REQUIRED. Every skill must be connected to at least one other skill. If a skill is truly standalone, it should at minimum be listed in an ops skill's routing table.

## Quick Checklist Format

Use this checklist during skill builds and audits:

```
## Anti-Pattern Checklist for {skill-name}

- [ ] AP-1: Simplicity gate passed (simplest pattern that works)
- [ ] AP-2: No unexplained framework references
- [ ] AP-3: All tools have documented usage patterns
- [ ] AP-4: 3-5 eval scenarios included
- [ ] AP-5: ≤7 tools declared, no overlapping functionality
- [ ] AP-6: SKILL.md <250 lines, references <15K tokens total
- [ ] AP-7: All workflows have intake → process → output stages
- [ ] AP-8: User confirmation for all external actions
- [ ] AP-9: No unnecessary confirmation pauses
- [ ] AP-10: Works across Claude model versions
- [ ] AP-11: Instructions are specific, not vague
- [ ] AP-12: Critical instructions front-loaded in SKILL.md
- [ ] AP-13: No peer-to-peer skill invocation (hub-and-spoke)
- [ ] AP-14: Time-sensitive data flagged with review dates
- [ ] AP-15: Non-scope section present, no overlap with existing skills
- [ ] AP-16: Skill connected to at least one other skill
```
