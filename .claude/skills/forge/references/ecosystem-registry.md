# Ecosystem Registry

> Living inventory of all Digital Energy skills. Updated by forge after every build, audit, or upgrade.
> Last updated: 2026-03-26

## Skill Inventory

### Ops Orchestrators (10 skills)

| Skill | Type | Score | Hrs/wk | Status | Dependencies | Key Integrations |
|-------|------|-------|--------|--------|-------------|-----------------|
| `ops-chiefops` | Ops Orchestrator | 85 | — | Active | — | HubSpot (read), Calendar, ClickUp, Fireflies |
| `ops-meetingops` | Ops Orchestrator | — | — | Active | — | Fireflies, Calendar, HubSpot, ClickUp |
| `ops-contextops` | Ops Orchestrator | — | — | Active | — | WhatsApp (manual), voice notes |
| `ops-dealops` | Ops Orchestrator | — | — | Active | — | HubSpot (read/write), ClickUp |
| `ops-storyops` | Ops Orchestrator | — | — | **DEPRECATED** → `carlos-ceo` | `de-brand-bible` | Absorbed into carlos-ceo (narrative-architecture ref) |
| `ops-targetops` | Ops Orchestrator | — | — | Active | — | HubSpot (read/write), WebSearch |
| `ops-outreachops` | Ops Orchestrator | — | — | Active | — | Gmail, HubSpot |
| `ops-dataroomops` | Ops Orchestrator | — | — | Active | — | Google Drive, HubSpot |
| `ops-irops` | Ops Orchestrator | — | — | **DEPRECATED** → `carlos-ceo` | — | Absorbed into carlos-ceo (investor-relations-playbook ref) |
| `contact-intake` | Ops Orchestrator | — | — | Active | — | HubSpot (via sales-intake), ClickUp (via delegation-engine), Gmail (via ops-outreachops), Calendar, Claude vision. Delegates to: counter-party-intel, sales-intake, ops-outreachops, ops-contextops, delegation-engine, vendor-lifecycle, competitive-intel, ops-targetops |

### Domain Executors (8 skills)

| Skill | Type | Score | Hrs/wk | Status | Dependencies | Referenced By |
|-------|------|-------|--------|--------|-------------|--------------|
| `legal-counsel` | Matrix Composer | 94 | — | Active | — | ops-dealops, ops-dataroomops |
| `project-financing` | Domain Executor | 91 | — | Active | — | ops-dealops, ops-dataroomops, seed-fundraising |
| `seed-fundraising` | Domain Executor | 88 | — | Active | `de-brand-bible` | ops-storyops, ops-dataroomops, ops-irops |
| `content-engine` | Domain Executor | — | — | Active | `de-brand-bible` | ops-outreachops, ops-storyops, ops-irops |
| `collateral-studio` | Domain Executor | — | — | Active | `de-brand-bible` | ops-storyops, ops-outreachops |
| `marketing-strategist` | Domain Executor | — | — | Active | `de-brand-bible` | ops-storyops |
| `positioning-expert` | Domain Executor | — | — | Active | `de-brand-bible` | ops-storyops |
| `research-engine` | Domain Executor | 88 | — | Active | — | seed-fundraising, project-financing, ops-dealops, marketing-strategist, content-engine, collateral-studio, legal-counsel, ops-targetops |
| `lead-generation` | Domain Executor | ~89 | — | Active | — | ops-targetops (warm paths), ops-outreachops (sequences), sales-intake (qualification), ops-dealops (CRM), counter-party-intel (deep profiling) |

### Panel of Experts (4 skills)

| Skill | Type | Score | Hrs/wk | Specialists | Status | Referenced By |
|-------|------|-------|--------|------------|--------|--------------|
| `netherlands-permitting` | Panel of Experts | — | — | 17 | Active | ops-dealops |
| `dc-engineering` | Panel of Experts | — | — | 15 | Active | ops-dealops |
| `ai-infrastructure` | Panel of Experts | — | — | 6 | Active | ops-dealops |
| `energy-markets` | Panel of Experts | — | — | 6 | Active | ops-dealops |

### Passive Foundations (2 skills)

| Skill | Type | Score | Hrs/wk | Status | Referenced By |
|-------|------|-------|--------|--------|--------------|
| `de-brand-bible` | Passive Foundation | 86 | — | Active | marketing-strategist, positioning-expert, content-engine, collateral-studio, seed-fundraising, ops-storyops |
| `brand-book` | Passive Foundation | — | — | Active | Visual design system (design tokens, templates) |

### Workflow Skills (1 skill)

| Skill | Type | Score | Hrs/wk | Status | Dependencies | Referenced By |
|-------|------|-------|--------|--------|-------------|--------------|
| `Intake_IM_institutional` | Intake Orchestrator | — | — | Active | `investor-memo-writer`, `project-financing`, `financial-model-interpreter` | ops-dataroomops, seed-fundraising |

### Specialized Skills (2 skills)

| Skill | Type | Score | Hrs/wk | Status | Referenced By |
|-------|------|-------|--------|--------|--------------|
| `sales-intake` | Domain Executor | — | — | Active | ops-dealops, ops-targetops |
| `humanizer` | Domain Executor | — | — | Active | ops-outreachops, ops-irops |

### CEO Operating System (1 skill)

| Skill | Type | Score | Hrs/wk | Status | Dependencies | Absorbs |
|-------|------|-------|--------|--------|-------------|---------|
| `carlos-ceo` | Domain Executor + Orchestrator | — | — | Active | `ops-weeklyops`, `ops-contextops`, `delegation-engine` | `ops-storyops`, `ops-irops`, `carlos-thought-leadership`, CEO portion of `executive-comms` and `ops-chiefops` |

### Deprecated Skills (3 skills — absorbed into carlos-ceo)

| Skill | Status | Absorbed Into | Date |
|-------|--------|-------------|------|
| `ops-storyops` | Deprecated | `carlos-ceo` (narrative-architecture ref) | 2026-03-25 |
| `ops-irops` | Deprecated | `carlos-ceo` (investor-relations-playbook ref) | 2026-03-25 |
| `carlos-thought-leadership` | Deprecated | `carlos-ceo` (social-strategy ref + social-content workflow) | 2026-03-25 |

### Meta Skills (1 skill)

| Skill | Type | Score | Hrs/wk | Status | Purpose |
|-------|------|-------|--------|--------|---------|
| `forge` | Meta / Builder | — | — | Active | Builds, audits, integrates, and governs the ecosystem |

### Shared Resources

| Resource | Location | Referenced By |
|----------|----------|--------------|
| `ops-playbook.md` | `_shared/ops-playbook.md` | All ops-* skills |

### Organizational References (5 files)

| Resource | Location | Referenced By |
|----------|----------|--------------|
| `TEAMS.md` | `_shared/org/TEAMS.md` | ops-chiefops, ops-meetingops, ops-contextops, ops-dealops |
| `WAYS-OF-WORKING.md` | `_shared/org/WAYS-OF-WORKING.md` | ops-chiefops, ops-contextops, all content-producing skills |
| `OKR-GUIDELINES.md` | `_shared/org/OKR-GUIDELINES.md` | ops-chiefops, ops-irops |
| `OKR-GLOSSARY.md` | `_shared/org/OKR-GLOSSARY.md` | ops-chiefops (on demand) |
| `OKR-PROJECT-MANAGEMENT.md` | `_shared/org/OKR-PROJECT-MANAGEMENT.md` | ops-chiefops, ops-dealops, ops-meetingops |

## Ecosystem Metrics

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Total skills (active) | 25 | Max 30 | OK (was 24, +1 contact-intake) |
| Ops orchestrators | 7 | — | OK (was 9, -2 deprecated) |
| Domain executors | 7 | — | OK |
| CEO operating system | 1 | — | NEW |
| Panel of Experts | 4 | — | OK |
| Passive foundations | 2 | — | OK |
| Specialized | 2 | — | OK |
| Deprecated | 3 | — | Absorbed into carlos-ceo |
| Meta skills | 1 | — | OK |
| Skills with scores | 5 | — | Needs audit |
| Average score (scored only) | 89.4 | ≥75 | OK |
| Orphan skills (no references) | TBD | 0 | Needs check |

## Overlap Map

| Overlap Area | Skills Involved | Resolution |
|-------------|----------------|------------|
| Brand/visual identity | `de-brand-bible` + `brand-book` | Intentional: de-brand-bible = content/messaging; brand-book = visual/design tokens |
| Investor materials | `seed-fundraising` + `ops-irops` + `ops-dataroomops` | Intentional: seed-fundraising = strategy; irops = ongoing relations; dataroomops = DD |
| CRM/pipeline | `ops-dealops` + `ops-targetops` | Intentional: dealops = active deal management; targetops = prospecting pipeline |
| Contact ingestion | `contact-intake` + `sales-intake` + `ops-contextops` | Intentional: contact-intake = orchestrator (bulk multi-format intake + scoring + routing); sales-intake = deep ICP qualification (called by contact-intake); ops-contextops = relationship intelligence storage (called by contact-intake) |
| Content/outreach | `content-engine` + `ops-outreachops` | Intentional: content-engine = writing; outreachops = orchestration + sequencing |

## Governance Notes

- **Existence test:** Every skill must pass the 2-hour test (see `quality-rubric.md`). The `Hrs/wk` column tracks estimated weekly hours saved per skill. Skills with blank or <2 values are flagged for W7 review.
- **Skill count:** 26 — approaching the 30-skill governance threshold. New skills need overlap audit.
- **Unscored skills:** 21 of 25 skills have not been formally audited. Priority: audit the most-used skills first.
- **Missing integrations:** Not all ops skills have MCP tool declarations in their frontmatter. `ops-chiefops` is the current gold standard for MCP integration.
- **Blueprint backlog:** `multi-agent-technical-drafting-system.md` contains 27 agent definitions. Converting these would exceed the 30-skill threshold — must merge/consolidate before converting.
- **Global availability:** All skills symlinked from `~/.claude/skills/` to canonical source at `/Users/crmg/Documents/DE Claude/.claude/skills/`. If symlinks break, re-run the linking script.
- **Framework name:** Forge — the skill ecosystem governed by the `forge` meta-skill.
- **Organizational references:** 5 org docs in `_shared/org/` (TEAMS, WAYS-OF-WORKING, OKR-GUIDELINES, OKR-GLOSSARY, OKR-PROJECT-MANAGEMENT). Not skills — shared reference files loaded on demand by ops skills.

## Update Protocol

This file is updated by forge:
- After every W1 (Build): Add new skill row
- After every W3 (Audit): Update score column
- After every W4 (Upgrade): Update score and status
- After every W7 (Ecosystem Review): Full refresh of all rows + metrics
