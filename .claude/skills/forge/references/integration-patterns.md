# Integration Patterns

> How to wire skills into external tools: HubSpot MCP, Chrome browser, and manual bridges.
> Source: Production MCP configurations + Chrome MCP capabilities + ops-playbook.md
> Last updated: 2026-02-19

## Available Integration Channels

| Channel | Status | Capabilities | Skills Using It |
|---------|--------|-------------|----------------|
| HubSpot MCP | Live (Claude plugin) | Search/create/update contacts, deals, tickets; search properties; search owners | `ops-dealops`, `ops-targetops`, `ops-outreachops`, `ops-dataroomops`, `ops-chiefops`, `ops-meetings` |
| Chrome Browser MCP | Live | Navigate, click, type, screenshot, read page, find elements, fill forms, read console/network | Any skill needing browser automation |
| Google Workspace MCP | Planned/Partial | Gmail send/read, Calendar events, Drive files, Sheets data, Docs creation | `ops-meetings`, `ops-outreachops`, `ops-chiefops`, `ops-dataroomops`, `ops-dealops` |
| Fireflies MCP | Planned/Partial | Search transcripts, pull full transcript, generate summary | `ops-meetings`, `ops-chiefops` |
| ClickUp MCP | Planned/Partial | Create tasks, update status, list tasks | `ops-meetings`, `ops-chiefops`, `ops-dealops` |
| WhatsApp | No MCP | Manual export only — paste into Claude | `ops-contextops` |

## HubSpot MCP Patterns

### Available Tools

```
mcp__hubspot__get_user_details      # Check permissions, get owner ID
mcp__hubspot__search_crm_objects    # Search contacts, deals, tickets with filters
mcp__hubspot__get_crm_objects       # Fetch specific objects by ID
mcp__hubspot__manage_crm_objects    # Create/update objects (requires confirmation)
mcp__hubspot__search_properties     # Discover property definitions
mcp__hubspot__get_properties        # Get detailed property schemas
mcp__hubspot__search_owners         # List/search owners
```

### Standard HubSpot Workflow

```
1. get_user_details → verify permissions, get ownerId
2. search_properties → discover property names for the object type
3. search_crm_objects → find records matching criteria
4. get_crm_objects → fetch full details for specific records
5. manage_crm_objects → create or update (REQUIRES user confirmation)
```

### HubSpot Recipes

**Contact upsert after meeting:**
```
search_crm_objects(contacts, query=email) → found?
  → Yes: get_crm_objects(contactId) → manage_crm_objects(update, add note)
  → No: manage_crm_objects(create, properties={email, name, company, source})
Associate contact with deal if deal context exists.
```

**Pipeline snapshot for weekly brief:**
```
search_crm_objects(deals, filters=[stage != closed], properties=[dealname, dealstage, amount, closedate, hubspot_owner_id])
Sort by close date. Flag: overdue, stale (>14 days no update), missing data.
```

**Stale deal detection:**
```
search_crm_objects(deals, filters=[
  dealstage NOT IN [closedwon, closedlost],
  notes_last_updated < 14_days_ago
])
Flag for review. Update hs_next_step property if user provides input.
```

**Bulk contact enrichment:**
```
search_crm_objects(contacts, filters=[company HAS_PROPERTY, jobtitle NOT_HAS_PROPERTY])
For each: WebSearch for LinkedIn profile → update jobtitle, notes.
Max 10 per batch. Confirm before updating.
```

### HubSpot Gotchas

- **Confirmation flow:** `manage_crm_objects` requires `confirmationStatus: "CONFIRMED"` or `"CONFIRMATION_WAIVED_FOR_SESSION"`. Always show proposed changes table first.
- **Property discovery:** Property names are NOT intuitive. Always use `search_properties` first. Example: deal stage is `dealstage`, not `stage` or `deal_stage`.
- **Association patterns:** Use `associatedWith` in `search_crm_objects` filterGroups, not pseudo-properties like `associations.contacts`.
- **Pagination:** Check `total` count. Default limit is 100; max 200. Use `offset` for next page.
- **Owner vs User:** HubSpot owner IDs ≠ user IDs. Use `search_owners` to find owner IDs for assignment.
- **chatInsights required:** `search_crm_objects` requires a `chatInsights` field with `userIntent` and `satisfaction`.

### Declaring HubSpot Tools in SKILL.md

```yaml
allowed-tools:
  # Read-only HubSpot access (for skills that only query):
  - mcp__hubspot__search_crm_objects
  - mcp__hubspot__get_crm_objects
  - mcp__hubspot__search_properties
  - mcp__hubspot__get_properties
  - mcp__hubspot__search_owners

  # Full HubSpot access (for skills that create/update):
  - mcp__hubspot__*    # Wildcard includes manage_crm_objects
```

Use the specific tool names (not wildcard) for read-only skills to prevent accidental writes.

## Chrome Browser MCP Patterns

### Available Tools

```
mcp__Claude_in_Chrome__tabs_context_mcp    # Get tab context (MUST call first)
mcp__Claude_in_Chrome__tabs_create_mcp     # Create new tab
mcp__Claude_in_Chrome__navigate            # Go to URL
mcp__Claude_in_Chrome__read_page           # Accessibility tree of page
mcp__Claude_in_Chrome__find                # Find elements by description
mcp__Claude_in_Chrome__computer            # Click, type, screenshot, scroll
mcp__Claude_in_Chrome__form_input          # Fill form fields
mcp__Claude_in_Chrome__get_page_text       # Extract page text
mcp__Claude_in_Chrome__javascript_tool     # Execute JS in page context
```

### Standard Chrome Workflow

```
1. tabs_context_mcp → get available tabs
2. tabs_create_mcp → create new tab (if needed)
3. navigate → go to target URL
4. read_page or find → locate elements
5. computer(screenshot) → verify visual state
6. form_input or computer(left_click/type) → interact
7. USER CONFIRMATION → before any send/post/submit/delete
8. computer(left_click) → execute confirmed action
```

### Chrome Recipes

**Gmail compose and send:**
```
navigate(mail.google.com) → find("compose button") → click →
find("to field") → form_input(recipient) →
find("subject field") → form_input(subject) →
find("message body") → form_input(body) →
screenshot → SHOW USER FOR CONFIRMATION →
find("send button") → click (only after user confirms)
```

**LinkedIn post:**
```
navigate(linkedin.com/feed) → find("start a post") → click →
find("text editor") → type(content) →
screenshot → SHOW USER FOR CONFIRMATION →
find("post button") → click (only after user confirms)
```

**ClickUp task creation:**
```
navigate(app.clickup.com) → find("add task") → click →
form_input(task name, description, assignee, due date) →
screenshot → SHOW USER FOR CONFIRMATION →
find("create task") → click (only after user confirms)
```

### Chrome Gotchas

- **Security rules:** MUST get user confirmation before send, post, submit, purchase, delete actions. This is a hard requirement enforced by the system.
- **Tab context first:** Always call `tabs_context_mcp` before any other Chrome tool. Call `tabs_create_mcp` for new tabs rather than reusing existing ones.
- **No 2FA bypass:** Chrome MCP cannot complete 2FA or CAPTCHA. If encountered, tell the user to complete it manually.
- **No password entry:** Never enter passwords or sensitive credentials via Chrome MCP.
- **No file downloads:** File downloads require explicit user confirmation.
- **Screenshot before action:** Always screenshot before user-confirmation steps to show what will happen.

### Declaring Chrome Tools in SKILL.md

Chrome tools do NOT need to be declared in `allowed-tools`. They are available to all skills by default when the Chrome MCP is connected. However, skills that rely on Chrome workflows should document the workflow patterns in their instructions.

## Manual Bridge Patterns

For tools without MCP integration, use these patterns to minimize friction.

### Paste-and-Process

**Pattern:** User pastes content into Claude → skill processes → outputs formatted result.

**Best for:** WhatsApp exports, email threads, meeting notes, screenshots.

**Design rules:**
- Accept messy input (the user won't clean it up)
- Parse intelligently (extract structure from unstructured text)
- Output in the format needed for the next step (Markdown, email draft, HubSpot-ready fields)

### Output-to-Clipboard

**Pattern:** Skill produces output formatted for the target tool. User copies and pastes.

**Best for:** Email drafts, social media posts, task descriptions, CRM field updates.

**Design rules:**
- Format output exactly as it should appear in the target tool
- Use headers/sections that map to target tool fields
- Include copy-paste instructions ("Copy the above into the Subject field")
- For HubSpot: output property name → value pairs ready for manual entry

### Screenshot-and-Analyze

**Pattern:** User screenshots a tool state → skill reads and processes the image.

**Best for:** Dashboard reviews, form analysis, error debugging, UI state checks.

**Design rules:**
- Accept screenshots via file path (Read tool can read images)
- Extract structured data from visual layout
- Provide recommendations based on what's visible

## Automation Level Selection

| Level | Name | When to Use | Example |
|-------|------|-------------|---------|
| L1 | Paste-and-process | No tool access; user mediates all I/O | WhatsApp → ops-contextops → formatted output |
| L2 | Chrome-assisted | Tool accessible via browser; user confirms actions | Gmail compose → user confirms → send |
| L3 | Full MCP | Direct API access; skill reads/writes programmatically | HubSpot search → update deal stage |

**Selection rule:** Use the highest available level. Fall back gracefully:
- L3 unavailable → fall back to L2 (Chrome)
- L2 unavailable → fall back to L1 (manual bridge)

**Every skill should document its automation level per workflow.** Example:
```
## Automation Levels
| Workflow | L3 (MCP) | L2 (Chrome) | L1 (Manual) |
|----------|----------|-------------|-------------|
| Pipeline review | HubSpot MCP read | Navigate to HubSpot | User pastes export |
| Follow-up email | Gmail MCP draft+send | Chrome Gmail compose | Output email text |
| CRM update | HubSpot MCP update | Chrome HubSpot form | Output field values |
```

## Fallback Principle

**Every MCP-dependent workflow has a manual fallback.** If an MCP server is disconnected, skills revert to paste-and-process or output-as-Markdown. No skill breaks without MCP.

Skills should include a note in their SKILL.md:
```
**Fallback:** If [MCP server] is unavailable, [describe manual alternative].
```

## MCP Declaration Checklist

When adding MCP integration to a skill:

1. [ ] Add MCP tool names to `allowed-tools` in frontmatter
2. [ ] Use specific tool names for read-only access, wildcard for full access
3. [ ] Document the standard workflow pattern (tool call sequence)
4. [ ] Document edge cases and error handling
5. [ ] Document the L1 manual fallback for when MCP is unavailable
6. [ ] Add user confirmation points for any write/send/delete operations
7. [ ] Test the workflow end-to-end with a real example
