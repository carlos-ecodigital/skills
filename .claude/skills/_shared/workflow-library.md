---
name: DE Workflow Library
description: Searchable catalog of all workflows across the Digital Energy skill ecosystem
type: shared-resource
last-updated: 2026-03-25
total-workflows: 35
---

# DE Workflow Library

> Living index of all workflows in the Digital Energy skill ecosystem.
> Updated by forge after every skill build (W1), workflow build (W9), or ecosystem review (W7).

## Quick Reference (All Workflows)

| # | Workflow | Owner Skill | Trigger Phrases | Frequency | Duration | Location |
|---|---------|-------------|-----------------|-----------|----------|----------|
| 1 | Daily Scan | carlos-ceo | "morning brief", "daily scan", "what's today" | Daily | 10m | workflows/daily-scan.md |
| 2 | Weekly Business Review | carlos-ceo | "WBR", "weekly review", "CEO weekly" | Weekly | 45m | workflows/weekly-business-review.md |
| 3 | Monthly Review (extended WBR) | carlos-ceo | "monthly review" | Monthly | 90m | workflows/weekly-business-review.md (extended) |
| 4 | Investor Update | carlos-ceo | "investor update", "monthly update for investors" | Monthly | 30m | workflows/stakeholder-update.md (--investor) |
| 5 | Board Update | carlos-ceo | "board update", "board pack", "board brief" | Quarterly | 30m | workflows/stakeholder-update.md (--board) |
| 6 | CEO Decision Advisory | carlos-ceo | "should we X", "one-way door?", "big decision" | Ad-hoc | 20m | ref: ceo-decision-framework.md |
| 7 | Deal Involvement Triage | carlos-ceo | "should I join this", "should I be in this meeting" | Ad-hoc | 10m | ref: deal-involvement-triggers.md |
| 8 | Time & Energy Audit | carlos-ceo | "time audit", "calendar audit", "where's my time going" | Ad-hoc | 15m | ref: time-energy-architecture.md + GCal |
| 9 | CEO Email Drafting | carlos-ceo | "draft email to", "write to", "email", "reply to" | Ad-hoc | 10m | workflows/ceo-email.md |
| 10 | CEO Blocker Resolution | carlos-ceo | "unblock", "escalation", "what's stuck", "blocker" | Ad-hoc | 15m | workflows/ceo-blocker.md |
| 11 | Social Content | carlos-ceo | "LinkedIn post", "what should I post", "social content" | Ad-hoc | 15m | workflows/social-content.md |
| 12 | Narrative Check | carlos-ceo | "story consistency", "how should we frame this", "narrative check" | Ad-hoc | 10m | ref: narrative-architecture.md |
| 13 | Build from Brief | forge | "build a skill for...", "new agent that...", "create a skill" | Ad-hoc | 45-90m | SKILL.md (inline W1) |
| 14 | Convert Blueprint | forge | "convert [blueprint] to skills", "implement the [X] agents" | Ad-hoc | 120m+ | SKILL.md (inline W2) |
| 15 | Audit & Score | forge | "audit [skill]", "skill quality check", "score [skill]" | Ad-hoc | 30-60m | SKILL.md (inline W3) |
| 16 | Upgrade Skill | forge | "upgrade [skill]", "improve [skill]", "fill gaps in [skill]" | Ad-hoc | 60m+ | SKILL.md (inline W4) |
| 17 | Design Architecture | forge | "design a team for...", "skill architecture for..." | Ad-hoc | 45-90m | SKILL.md (inline W5) |
| 18 | Wire Integration & Automate | forge | "connect [skill] to HubSpot", "automate [workflow]" | Ad-hoc | 60m+ | SKILL.md (inline W6) |
| 19 | Ecosystem Review | forge | "ecosystem health", "skill review", "what should we kill/merge" | Ad-hoc | 90m+ | SKILL.md (inline W7) |
| 20 | Self-Improvement | forge | Automatic (runs inside W1-W7) | Continuous | — | SKILL.md (inline W8) |
| 21 | Build Workflow | forge | "create a workflow", "new workflow", "document this process" | Ad-hoc | 15-30m | workflows/build-workflow.md |
| 22 | Sensitivity Analysis | scenario-simulator | "what if colo fee drops to EUR [X]", "sensitivity on [param]" | Ad-hoc | 10-20m | SKILL.md (inline W1) |
| 23 | Stress Test | scenario-simulator | "stress test the deal", "worst case scenario" | Ad-hoc | 15-25m | SKILL.md (inline W2) |
| 24 | Binary Event | scenario-simulator | "what if we lose Westland", "go/no-go on [decision]" | Ad-hoc | 10-15m | SKILL.md (inline W3) |
| 25 | Timeline Scenario | scenario-simulator | "what if grid takes 18 months", "cost of 6-month delay" | Ad-hoc | 15-20m | SKILL.md (inline W4) |
| 26 | Portfolio Reconfiguration | scenario-simulator | "what if we drop [project/region]", "add [project]" | Ad-hoc | 20-30m | SKILL.md (inline W5) |
| 27 | Standard Brief | research-engine | "research [topic]", "investigate [market]" | Ad-hoc | 20-30m | SKILL.md (inline W1) |
| 28 | Quick Lookup | research-engine | "what is [specific fact]", "find the number for [X]" | Ad-hoc | 5-10m | SKILL.md (inline W2) |
| 29 | Deep Dive | research-engine | "deep dive into [X]", "comprehensive research on [X]" | Ad-hoc | 45-90m | SKILL.md (inline W3) |
| 30 | Standard Dossier | counter-party-intel | "who is [person/company]", "dossier on [X]", "meeting prep" | Ad-hoc | 15-20m | SKILL.md (inline W1) |
| 31 | Quick Profile | counter-party-intel | "quick look at [X]", "meeting in 1 hour with [X]" | Ad-hoc | 5-10m | SKILL.md (inline W2) |
| 32 | Deep Diligence | counter-party-intel | "deep diligence on [X]", "full background check" | Ad-hoc | 30-60m | SKILL.md (inline W3) |
| 33 | Monthly Competitive Update | competitive-intel | "monthly update", "competitive landscape update" | Monthly | 30-45m | SKILL.md (inline W1) |
| 34 | NDA Review (8-Phase) | legal-counsel | "review this NDA", "NDA from [counterparty]" | Ad-hoc | 30-120m | specializations/contract-review/nda-review-workflow.md |
| 35 | Market Positioning | positioning-expert | "positioning for [segment]", "how should we position" | Ad-hoc | 30m | SKILL.md (inline) |

## By Category

### CEO & Leadership (12)
| # | Workflow | Trigger | Frequency |
|---|---------|---------|-----------|
| 1 | Daily Scan | "morning brief" | Daily |
| 2 | Weekly Business Review | "WBR" | Weekly |
| 3 | Monthly Review | "monthly review" | Monthly |
| 4 | Investor Update | "investor update" | Monthly |
| 5 | Board Update | "board update" | Quarterly |
| 6 | CEO Decision Advisory | "should we X" | Ad-hoc |
| 7 | Deal Involvement Triage | "should I join this" | Ad-hoc |
| 8 | Time & Energy Audit | "time audit" | Ad-hoc |
| 9 | CEO Email Drafting | "draft email to" | Ad-hoc |
| 10 | CEO Blocker Resolution | "unblock" | Ad-hoc |
| 11 | Social Content | "LinkedIn post" | Ad-hoc |
| 12 | Narrative Check | "narrative check" | Ad-hoc |

### Meta / Ecosystem Governance (9)
| # | Workflow | Trigger | Frequency |
|---|---------|---------|-----------|
| 13 | Build from Brief | "build a skill for" | Ad-hoc |
| 14 | Convert Blueprint | "convert blueprint" | Ad-hoc |
| 15 | Audit & Score | "audit [skill]" | Ad-hoc |
| 16 | Upgrade Skill | "upgrade [skill]" | Ad-hoc |
| 17 | Design Architecture | "design a team for" | Ad-hoc |
| 18 | Wire Integration | "connect to HubSpot" | Ad-hoc |
| 19 | Ecosystem Review | "ecosystem health" | Ad-hoc |
| 20 | Self-Improvement | Automatic | Continuous |
| 21 | Build Workflow | "create a workflow" | Ad-hoc |

### Intelligence & Research (6)
| # | Workflow | Trigger | Frequency |
|---|---------|---------|-----------|
| 27 | Standard Brief | "research [topic]" | Ad-hoc |
| 28 | Quick Lookup | "what is [fact]" | Ad-hoc |
| 29 | Deep Dive | "deep dive into [X]" | Ad-hoc |
| 30 | Standard Dossier | "who is [person]" | Ad-hoc |
| 31 | Quick Profile | "quick look at [X]" | Ad-hoc |
| 32 | Deep Diligence | "full background check" | Ad-hoc |

### Financial Modeling (5)
| # | Workflow | Trigger | Frequency |
|---|---------|---------|-----------|
| 22 | Sensitivity Analysis | "what if [param] changes" | Ad-hoc |
| 23 | Stress Test | "stress test" | Ad-hoc |
| 24 | Binary Event | "what if we lose [X]" | Ad-hoc |
| 25 | Timeline Scenario | "cost of delay" | Ad-hoc |
| 26 | Portfolio Reconfiguration | "drop [project]" | Ad-hoc |

### Competitive Intelligence (1)
| # | Workflow | Trigger | Frequency |
|---|---------|---------|-----------|
| 33 | Monthly Competitive Update | "competitive landscape" | Monthly |

### Legal (1)
| # | Workflow | Trigger | Frequency |
|---|---------|---------|-----------|
| 34 | NDA Review (8-Phase) | "review this NDA" | Ad-hoc |

### Marketing & Positioning (1)
| # | Workflow | Trigger | Frequency |
|---|---------|---------|-----------|
| 35 | Market Positioning | "how should we position" | Ad-hoc |

## By Frequency

### Daily (1)
- **Daily Scan** → carlos-ceo

### Weekly (1)
- **Weekly Business Review** → carlos-ceo

### Monthly (3)
- **Monthly Review** (extended WBR) → carlos-ceo
- **Investor Update** → carlos-ceo
- **Monthly Competitive Update** → competitive-intel

### Quarterly (1)
- **Board Update** → carlos-ceo

### Continuous (1)
- **Self-Improvement** → forge (automatic)

### Ad-hoc (28)
All remaining workflows are triggered on demand.

## Cross-Skill Pipelines

These are multi-workflow chains that span multiple skills:

### 1. Meeting Processing Pipeline
`Fireflies transcript` → `ops-meetingops` (extract) → `ops-contextops` (archive) → `delegation-engine` (route) → `carlos-ceo daily-scan` (surface CEO items)

### 2. Brain Dump Pipeline
`Voice note / raw input` → `ops-contextops` (structure) → `delegation-engine` (route tasks) → `carlos-ceo` (CEO decisions)

### 3. Content Publishing Pipeline
`WBR insight / market event` → `carlos-ceo social-content` (draft) → `content-atomizer` (derivatives) → publish

### 4. Investor Update Pipeline
`ops-weeklyops` (scan) → `carlos-ceo WBR` (decisions) → `carlos-ceo stakeholder-update` (frame) → `carlos-ceo ceo-email` (draft) → send

### 5. Prospect Research Pipeline
`ops-targetops` (identify) → `counter-party-intel` (dossier) → `pre-meeting-brief` (prep) → `sales-intake` (qualify)

### 6. Skill Build Pipeline
`User brief` → `forge W1` (build) → `forge W3` (audit) → `forge W9` (register workflows) → `_shared/workflow-library.md` (catalog)

## Update Protocol

- **Forge W1 (Build from Brief):** Register any new workflows created during skill build
- **Forge W7 (Ecosystem Review):** Full reconciliation — glob all `*/workflows/*.md`, verify all are cataloged
- **Forge W9 (Build Workflow):** Register immediately after writing workflow file
- **Any skill author:** When adding a workflow manually, add a row to Quick Reference + category section
- **Format:** Add row to Quick Reference table, add to category section, increment total-workflows in frontmatter
