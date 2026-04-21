---
name: de-executive-comms
description: Draft executive-voice communications for Digital Energy — cover emails for LOI delivery, partner updates, board communications. Anchored to CEO-level voice markers. Use after legal-assistant generates an LOI to draft the accompanying cover email, or standalone for any executive-voice outbound message.
allowed-tools: [Read, Edit, Write, Glob, Grep, mcp__d5290535-5069-4a7a-901b-388e4154e283__create_draft, mcp__d5290535-5069-4a7a-901b-388e4154e283__search_threads, mcp__d5290535-5069-4a7a-901b-388e4154e283__get_thread]
---

# de-executive-comms

Executive-voice drafting skill. Handles the cover-email half of LOI delivery (invoked right after `legal-assistant` emits the `.docx`) and any adjacent outbound communication that needs to match the DE house voice.

## When to use

- LOI cover-email delivery (most common)
- Partner-relationship check-ins where the voice register matters
- Board updates with a narrative arc (not data dumps — use `wbr-system` for those)
- Any outbound where the operator supplies tone-tokens ("short, powerful, collaborative") and needs those tokens mapped to concrete drafting rules

## How it works

1. Operator provides: subject, recipient, optional tone-tokens, optional reference context (LOI path, prior thread, Fireflies transcript).
2. Skill loads `_shared/tone-markers.md` to map tokens → concrete rules.
3. Skill loads the appropriate template from `templates/` (e.g., `loi-cover-email.md`).
4. Skill drafts; emits both the draft AND a tone-audit showing which rules were applied.
5. Operator iterates; skill re-applies tone-markers on each iteration.

## Key files

- `_shared/tone-markers.md` — qualitative tokens → concrete drafting rules
- `templates/loi-cover-email.md` — LOI delivery cover-email template
- `templates/loi-cover-email-tone-audit.md` — self-check grid operator applies to any draft

## Gmail MCP fallback protocol

On any Gmail MCP schema error during a session:

1. Log error type + tool name in an inline session note (not a file).
2. Skip all further Gmail MCP calls this turn.
3. For inbound data (threads): request paste or PDF export from user.
4. For outbound drafts: emit formatted email block with `To:`, `Cc:`, `Subject:`, `Attach:` and a code-fenced body for copy-paste.
5. Include explicit note: "Gmail MCP degraded this session — please paste into Gmail manually and attach {path}."
6. Offer to retry at next turn.

This protocol is enforced by convention, not by a linter. If it fires during an LOI delivery session, `legal-assistant` and `de-executive-comms` both default to the paste-into-Gmail fallback and surface the degradation in the session log.

## Relationship to other skills

- `legal-assistant` — this skill's most common invoker. After `legal-assistant` Phase 7 delivery, the operator pivots to `de-executive-comms` for the cover email.
- `wbr-system` — distinct domain (internal weekly business review). Do not route executive-voice outbound through WBR templates.
- `contact-intake` — CRM creation flows through `contact-intake`; this skill assumes the counterparty already exists in CRM.
