# Forge Learnings

> Self-improvement journal. Updated by forge after every skill build, audit, or upgrade.
> Pattern observations accumulate here. After 3+ identical observations → update templates.
> Last updated: 2026-02-24

## Entry Template

```markdown
## [Date] -- [Action: built/audited/upgraded] [Skill Name]

### What the user asked for
[Original brief/request]

### What forge delivered
[Skill name, composition pattern, score, file count]

### What the user changed after delivery
[Any edits the user made — these are the highest-signal learning data]

### Pattern observations
- [What worked well that should be repeated]
- [What the user pushed back on or modified]
- [New pattern discovered that should be added to composition-patterns.md]

### Registry impact
[New skill count, overlap changes, governance implications]
```

## Build Log

## 2026-02-24 -- built research-engine

### What the user asked for
"Develop a skill for research. Go deep and wide. Take research tasks, break them down in the most logical granular block, identify keywords and the right research strategy. Master the use of sub-agents and make it massively effective, ultra accurate, extremely exhaustive. Use the latest and most edge AI setups."

### What forge delivered
- **Skill:** research-engine (Domain Executor)
- **Score:** 88/100 (Grade B)
- **Files:** 4 core + 8 references + 2 examples = 14 files
- **Context budget:** ~8.5K tokens max (under 15K limit)
- **Tools:** 6 (WebSearch, WebFetch, Read, Glob, Grep, Task)
- **Key innovation:** 8 cutting-edge agentic patterns from 2024-2026 research (iterative deepening, self-critique, adversarial debate, confidence calibration, citation agent, effort scaling, multi-hop discovery, stateful checkpointing)

### What the user changed after delivery
1. **Corrected DE overlay approach:** User rejected pre-loading ecosystem data as baseline. Corrected to: research finds fresh data independently, then compares post-synthesis. This is a general pattern — research skills should discover, not recite.
2. **Required forge governance integration:** User insisted the plan fit within W1 intake (simplicity gate, anti-pattern checklist, context budget). Not optional.

### Pattern observations
- **Subagent-driven development works well for reference-heavy skills.** Dispatching 2-3 file-writing agents in parallel with detailed specs produced consistent, high-quality output. Each agent was given: file path, purpose, content spec, line target, and cross-reference rules.
- **User pushback on pre-loading data is a recurring principle.** Research engines should find fresh data, not anchor to stale baselines. This likely applies to any skill that generates intelligence.
- **Plan v1 is never good enough.** User explicitly asked "What is missing? What could be improved?" — the self-critique step before plan approval is essential. Plan v3 was approved.
- **Anti-pattern AP-5 (tool count) catches real issues.** Original design had 7 tools (including Bash). Dropping Bash was the right call — research is read-only.

### Registry impact
Skill count: 25 → 26. No overlap with existing skills. Under 30 threshold.

---

## Active Patterns (confirmed across multiple builds)

*No patterns logged yet. This section will be populated as forge builds, audits, and upgrades skills.*

## Pending Observations (single occurrence — needs confirmation)

- **Subagent-driven development:** Effective for skills with 5+ reference files. Each agent gets one file with full spec. Parallel dispatch maximizes speed. Needs confirmation from next build.
- **"Research finds, then compares" principle:** Research/intelligence skills should not anchor to existing data. Discover independently, compare post-synthesis. Needs confirmation from next intelligence-type skill.
- **Plan self-critique is mandatory:** Always ask "what's missing?" before presenting the plan. Plan v1 is a draft, not a proposal.

## Template Version History

| Template | Version | Date | Change | Impact |
|----------|---------|------|--------|--------|
| ops-orchestrator | v1 | 2026-02-19 | Initial creation | — |
| domain-executor | v1 | 2026-02-19 | Initial creation | — |
| passive-reference | v1 | 2026-02-19 | Initial creation | — |
| engineering-discipline | v1 | 2026-02-19 | Initial creation | — |
| reference-file | v1 | 2026-02-19 | Initial creation | — |
| shared-resource | v1 | 2026-02-19 | Initial creation | — |

## Self-Improvement Rules

1. After every W1 (build) or W4 (upgrade), log an entry above.
2. If user invokes forge again later, diff previously-built skills against current state. User modifications are the highest-signal learning data.
3. After 3+ identical modifications across different skills → auto-update the relevant template. Present the proposed template change to the user for approval.
4. Every 5 skills built, review this file for repeated patterns. Update composition-patterns.md, quality-rubric.md, or templates if patterns have drifted.
5. Track which workflows (W1-W7) are most/least used. If a workflow is never invoked, consider simplifying or removing it.
6. Track which composition patterns users request most. If a new pattern emerges, document and add it.
7. If a template update degrades subsequent scores → rollback to previous version.
8. Prune individual log entries older than 3 months unless they contain active patterns.

## Aggregate Statistics

| Metric | Value |
|--------|-------|
| Total skills built by forge | 1 |
| Total skills audited | 0 |
| Total skills upgraded | 0 |
| Average build score | 88 |
| Most common composition pattern | Domain Executor |
| Most common user modification type | Data approach correction |
| Template updates triggered | 0 |
