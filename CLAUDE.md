# Digital Energy Claude Skills

This repository contains the Digital Energy skill ecosystem — 29 custom skills + shared references for Claude Code and Claude.ai.

## Usage

Skills are loaded automatically when this repo is added as an additional directory:

```bash
claude --add-dir ~/claude-skills
```

All skills in `.claude/skills/` are discovered by Claude Code. Type `/` to see available skills, or let Claude invoke them automatically based on your conversation.

## Shared references

The `_shared/` directory contains cross-skill resources:
- `_shared/org/` — team structure, ways of working, OKR framework
- `_shared/intake-modules/` — modular intake system (m0-m9)
- `_shared/market-data.md`, `_shared/investor-landscape.md` — market intelligence
- `_shared/equity-structures.md` — equity and financing structures
- `_shared/ops-playbook.md`, `_shared/marketing-ops-guide.md` — operational guides

Skills reference these files by path. Do not rename or move them without updating references.

## MCP connectors

Several ops skills require MCP connectors for full functionality:
- **HubSpot** — ops-chiefops, ops-dealops, ops-dataroomops, ops-meetingops, ops-outreachops, sales-intake
- **Google Workspace** — ops-chiefops, ops-dataroomops, ops-dealops, ops-meetingops, ops-outreachops
- **Fireflies** — ops-meetingops
- **ClickUp** — ops-chiefops, ops-dealops, ops-meetingops

Configure these in your `.mcp.json` or at `claude.ai/settings/connectors`.
