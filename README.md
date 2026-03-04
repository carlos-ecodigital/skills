# Digital Energy Skills

Shared skill repository for the Digital Energy team. Contains 29 custom Claude skills + shared references.

## Setup

### Claude Code (full capability)

```bash
# Clone once
git clone --recurse-submodules git@github.com:carlos-ecodigital/skills.git ~/claude-skills

# Use with any project
claude --add-dir ~/claude-skills
```

Skills auto-discover from `.claude/skills/`. Type `/` in Claude Code to see all available skills.

To update:
```bash
cd ~/claude-skills && git pull --recurse-submodules
```

### Claude.ai web/app

Skills are provisioned org-wide via organization settings. All team members see them automatically in Settings > Capabilities > Skills.

For full functionality of ops skills (CRM, calendar, transcripts), configure MCP connectors at `claude.ai/settings/connectors`:
- HubSpot
- Google Workspace
- Fireflies
- ClickUp

## Skills overview

### Strategy & content
- `positioning-expert` — April Dunford positioning framework
- `marketing-strategist` — Hormozi-inspired B2B growth strategy
- `content-engine` — B2B marketing writing (all content types)
- `content-atomizer` — Long-form to multi-platform repurposing
- `carlos-thought-leadership` — CEO personal brand on LinkedIn/X
- `collateral-studio` — B2B decks, one-pagers, case studies
- `ops-storyops` — Unified narrative across all audiences
- `de-brand-bible` — Brand identity, voice, buyer personas, proof points
- `humanizer` — Remove AI writing patterns

### Domain expertise
- `ai-infrastructure` — GPU, cluster networking, inference, storage
- `dc-engineering` — Data center design, cooling, electrical, fire safety
- `energy-markets` — Wholesale trading, PPA, BESS revenue, carbon
- `netherlands-permitting` — Omgevingswet, BESS, district heating, data centers
- `project-financing` — NL project finance, SPV, debt sizing
- `site-development` — DEC co-location, grower interface, site selection

### Legal & finance
- `legal-counsel` — Multi-jurisdictional contracts, M&A, tax, compliance
- `seed-fundraising` — Pitch decks, investment memos, cap tables

### Operations
- `ops-chiefops` — Cross-functional coordination, priorities, blockers
- `ops-dealops` — Deal lifecycle, pipeline, HubSpot CRM
- `ops-meetingops` — Agenda, prep, summary, action items (Fireflies)
- `ops-outreachops` — Outbound sequences for all audiences
- `ops-targetops` — Prospecting, scoring, target lists
- `ops-contextops` — Founder brain capture, institutional memory
- `ops-dataroomops` — Data room structure, DD readiness
- `ops-irops` — Investor updates, relationship tracking
- `sales-intake` — Lead qualification, ICP routing, HubSpot

### Infrastructure
- `brand-book` — Design token system, visual exports
- `forge` — Skill ecosystem builder and governance
- `research-engine` — Parallel research with source scoring
