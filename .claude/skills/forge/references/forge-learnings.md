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

## 2026-03-25 -- built + upgraded carlos-ceo

### What the user asked for
"Create a new skill only for me called carlos-ceo" — CEO operating system with daily/weekly/monthly scans, email drafting, blocker resolution, social media, investor relations, unified narrative. Also: workflow library, workflow builder (forge W9), redundancy audit.

### What forge delivered
- **Skill:** carlos-ceo (Domain Executor + Ops Orchestrator hybrid)
- **Initial score:** 77.9/100 (Grade B) — then upgraded to ~85+ same session
- **Files:** 1 SKILL.md + 6 workflows + 9 references + 3 examples + 1 eval = 20 files
- **Absorbed:** ops-storyops, ops-irops, carlos-thought-leadership, CEO portions of executive-comms and ops-chiefops
- **Context budget:** ~14.5K tokens across 9 references (under 15K limit)
- **Upgrades applied same session:** Safety header, integration map fixes, reverse mapping, expanded investor-relations-playbook (4 engagement archetypes, ask funnel, escalation criteria), expanded social-strategy (5 engagement archetypes, pillar-to-trigger map), WBR enhancement (competitive-intel + financial-model-interpreter wired in, explicit ops-weeklyops fallback), 5 eval test scenarios
- **Bonus deliverables:** _shared/workflow-library.md (35 workflows cataloged), forge W9 Build Workflow

### What the user changed after delivery
- Directed carlos-ceo to personal repo (CRMG-Personal), NOT shared skills repo. CEO skill is personal, not team-wide.
- Skills repo gets shared infra only (workflow library, forge W9, deprecation notices).

### Pattern observations
- **Personal vs team skill separation matters.** CEO operating systems contain personal voice, growth areas, blind spots — not appropriate for team repos. Design for this split from the start.
- **Audit-then-upgrade is faster than build-from-scratch.** Running W3 (audit) before W4 (upgrade) in the same session produced targeted fixes. The audit identified eval scaffolding (4/10) as the bottleneck — one file fixed the biggest gap.
- **Background agents hit permission issues.** Agents spawned in background couldn't get Write/Bash permissions. Workaround: main thread creates directories and writes files directly. Consider designing around this limitation.
- **Subagent-driven development confirmed.** Second build using parallel agents. Same pattern: effective but permission-constrained. Main thread as fallback writer is reliable.
- **"Plan self-critique" confirmed.** Audit found 5 gaps; all fixed in the upgrade pass. Without the audit, these would have shipped as technical debt.

### Registry impact
Skill count: 26 → 27 (carlos-ceo). 5 skills deprecated/partially absorbed. Net active skills: ~24. Forge gains W9. _shared/ gains workflow-library.md.

---

## 2026-03-25 -- built forge W9 (Build Workflow)

### What the user asked for
"Create new type of skill file, called workflows, to help anyone create new workflows on the DE team."

### What forge delivered
- **New workflow:** forge/workflows/build-workflow.md (W9)
- **Simplicity gate:** NOT a new skill — added as workflow inside forge (P1: can this be a sub-function of an existing skill? Yes.)
- **9-step process:** Intake → collision check → template → draft → quality check → write → register → update owner → present
- **Auto-registers** in _shared/workflow-library.md

### Pattern observations
- **Simplicity gate works.** User asked for "a new skill file type." Forge correctly identified this as a forge workflow, not a standalone skill. Prevented unnecessary skill proliferation.
- **Workflow library as shared infrastructure is a new pattern.** First _shared/ resource that isn't domain content — it's ecosystem metadata. May need more of these.

---

## Active Patterns (confirmed across multiple builds)

- **Subagent-driven development:** Effective for skills with 5+ reference files. Confirmed in research-engine and carlos-ceo builds. Permission-constrained — main thread as fallback writer.
- **Plan self-critique is mandatory:** Confirmed in both builds. Always audit/critique before finalizing. Plan v1 is a draft.
- **Personal vs team separation:** CEO/personal skills belong in personal repos. Team skills in team repos. Design for this from intake.

## Pending Observations (single occurrence — needs confirmation)

- **"Research finds, then compares" principle:** Research/intelligence skills should not anchor to existing data. Discover independently, compare post-synthesis. Needs confirmation from next intelligence-type skill.
- **Audit-then-upgrade workflow:** Running W3 → W4 in same session is efficient. One more confirmation needed.
- **_shared/ as ecosystem metadata:** workflow-library.md is the first non-domain shared resource. If more emerge, may need a shared resource governance pattern.

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
| Total skills built by forge | 2 |
| Total skills audited | 1 |
| Total skills upgraded | 1 |
| Average build score | 83 |
| Most common composition pattern | Domain Executor |
| Most common user modification type | Repo separation (personal vs team) |
| Template updates triggered | 0 |
| Workflows built (W9) | 1 (forge W9 itself) |
| Shared resources created | 1 (_shared/workflow-library.md) |
