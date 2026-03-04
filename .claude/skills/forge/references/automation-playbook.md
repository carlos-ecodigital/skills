# Automation Playbook

> Deep automation guide: browser recipes, HubSpot MCP recipes, manual bridges, and friction-killing patterns.
> This is the friction-killer — the guide for eliminating copy-paste, context-switching, and manual data entry.
> Last updated: 2026-02-19

## Browser Automation Recipes (Chrome MCP)

### Recipe: Gmail Compose and Send

**Prerequisites:** Chrome MCP connected, user logged into Gmail
**Automation level:** L2 (user confirms send)

```
Step 1: tabs_context_mcp → get tab context
Step 2: tabs_create_mcp → new tab
Step 3: navigate(url="https://mail.google.com", tabId=tab)
Step 4: computer(action="wait", duration=3, tabId=tab)  # Wait for Gmail to load
Step 5: find(query="compose button", tabId=tab) → get ref
Step 6: computer(action="left_click", ref=compose_ref, tabId=tab)
Step 7: computer(action="wait", duration=2, tabId=tab)  # Wait for compose window
Step 8: find(query="to field", tabId=tab) → get ref
Step 9: form_input(ref=to_ref, value=recipient, tabId=tab)
Step 10: find(query="subject field", tabId=tab) → get ref
Step 11: form_input(ref=subject_ref, value=subject, tabId=tab)
Step 12: find(query="message body", tabId=tab) → get ref
Step 13: form_input(ref=body_ref, value=email_body, tabId=tab)
Step 14: computer(action="screenshot", tabId=tab)  # Show user what will be sent
Step 15: ASK USER: "Here's the email. Confirm send?"
Step 16: find(query="send button", tabId=tab) → get ref
Step 17: computer(action="left_click", ref=send_ref, tabId=tab)  # Only after confirmation
```

**Error recovery:** If Gmail doesn't load → retry once. If compose window doesn't open → screenshot and show user. If send fails → screenshot error state.

---

### Recipe: LinkedIn Post

**Prerequisites:** Chrome MCP connected, user logged into LinkedIn
**Automation level:** L2 (user confirms post)

```
Step 1: tabs_context_mcp → get tab context
Step 2: tabs_create_mcp → new tab
Step 3: navigate(url="https://www.linkedin.com/feed/", tabId=tab)
Step 4: computer(action="wait", duration=3, tabId=tab)
Step 5: find(query="start a post button", tabId=tab) → get ref
Step 6: computer(action="left_click", ref=post_ref, tabId=tab)
Step 7: computer(action="wait", duration=2, tabId=tab)
Step 8: find(query="text editor or post field", tabId=tab) → get ref
Step 9: computer(action="left_click", ref=editor_ref, tabId=tab)
Step 10: computer(action="type", text=post_content, tabId=tab)
Step 11: computer(action="screenshot", tabId=tab)  # Show user what will be posted
Step 12: ASK USER: "Here's the post. Confirm publish?"
Step 13: find(query="post button", tabId=tab) → get ref
Step 14: computer(action="left_click", ref=post_ref, tabId=tab)  # Only after confirmation
```

**Error recovery:** If LinkedIn requires login → tell user to log in manually. If post editor doesn't open → try alternative selector.

---

### Recipe: Google Doc Creation

**Prerequisites:** Chrome MCP connected, user logged into Google
**Automation level:** L2 (user confirms content)

```
Step 1: navigate(url="https://docs.google.com/document/create", tabId=tab)
Step 2: computer(action="wait", duration=3, tabId=tab)
Step 3: find(query="document title", tabId=tab) → get ref
Step 4: computer(action="triple_click", ref=title_ref, tabId=tab)  # Select default title
Step 5: computer(action="type", text=document_title, tabId=tab)
Step 6: find(query="document body", tabId=tab) → get ref
Step 7: computer(action="left_click", ref=body_ref, tabId=tab)
Step 8: computer(action="type", text=document_content, tabId=tab)
Step 9: computer(action="screenshot", tabId=tab)
```

**Note:** Google Docs auto-saves. No explicit save/confirm needed for content creation, but sharing requires user action (prohibited action per security rules).

---

### Recipe: HubSpot Manual Navigation

**When:** HubSpot MCP is unavailable for a specific operation, or user prefers visual confirmation.

```
Step 1: navigate(url="https://app.hubspot.com/contacts/{hubId}/contact/{contactId}", tabId=tab)
Step 2: computer(action="wait", duration=3, tabId=tab)
Step 3: read_page(tabId=tab) → verify correct contact loaded
Step 4: find(query="note or activity field", tabId=tab) → get ref
Step 5: form_input(ref=note_ref, value=note_content, tabId=tab)
Step 6: computer(action="screenshot", tabId=tab)
Step 7: ASK USER: "Confirm save?"
Step 8: find(query="save button", tabId=tab) → click
```

## HubSpot MCP Automation Recipes

### Recipe: Contact Upsert After Meeting

```python
# 1. Search for existing contact
search_crm_objects(
  objectType="contacts",
  query=attendee_email,
  properties=["firstname", "lastname", "email", "company", "jobtitle"]
)

# 2a. If found → update with meeting notes
manage_crm_objects(
  confirmationStatus="CONFIRMED",  # After user confirms
  updateRequest={
    objects: [{
      objectType: "contacts",
      objectId: contact_id,
      properties: { "notes_last_updated": today, "hs_lead_status": "IN_PROGRESS" }
    }]
  }
)

# 2b. If not found → create new contact
manage_crm_objects(
  confirmationStatus="CONFIRMED",
  createRequest={
    objects: [{
      objectType: "contacts",
      properties: {
        "email": attendee_email,
        "firstname": first_name,
        "lastname": last_name,
        "company": company_name,
        "hs_lead_status": "NEW"
      }
    }]
  }
)
```

### Recipe: Pipeline Snapshot

```python
# Pull all active deals
search_crm_objects(
  objectType="deals",
  filterGroups=[{
    filters: [{
      propertyName: "dealstage",
      operator: "NOT_IN",
      values: ["closedwon", "closedlost"]
    }]
  }],
  properties=["dealname", "dealstage", "amount", "closedate",
              "hubspot_owner_id", "notes_last_updated"],
  sorts=[{ propertyName: "closedate", direction: "ASCENDING" }]
)

# Flag deals needing attention:
# - Close date in the past
# - No notes update in 14+ days
# - Missing amount or close date
```

### Recipe: Stale Deal Detection

```python
search_crm_objects(
  objectType="deals",
  filterGroups=[{
    filters: [
      { propertyName: "dealstage", operator: "NOT_IN",
        values: ["closedwon", "closedlost"] },
      { propertyName: "notes_last_updated", operator: "LT",
        value: fourteen_days_ago_timestamp }
    ]
  }],
  properties=["dealname", "dealstage", "hubspot_owner_id", "notes_last_updated"]
)
# Present stale deals to user for action
```

### Recipe: Property Discovery

```python
# When you don't know the exact property name:
search_properties(objectType="deals", keywords=["stage", "status", "pipeline"])
# Returns: dealstage, pipeline, hs_deal_stage_probability, etc.

# When you need the valid values for an enum property:
get_properties(objectType="deals", propertyNames=["dealstage"])
# Returns: option values with labels (e.g., "appointmentscheduled" → "Appointment Scheduled")
```

## Manual Bridge Accelerators

For tools without MCP or Chrome access.

### Voice Note → Action Pipeline

```
User records WhatsApp voice note → transcribes via WhatsApp → pastes into Claude:

"Process this voice note: [paste transcript]"

ops-contextops processes:
  → Decisions → decision journal
  → People mentioned → relationship intel
  → Action items → formatted for ClickUp or weekly brief
  → Deal updates → formatted for HubSpot (property: value pairs)

Output: structured capture + ready-to-paste formatted blocks for each target tool
```

### Email → CRM Bridge

```
User forwards email to Claude or pastes email thread:

"Process this email thread: [paste]"

ops-meetingops or ops-contextops processes:
  → Extract: contacts (name, email, company), commitments, action items
  → Format as HubSpot update: contact properties + note text
  → If HubSpot MCP available: create/update directly
  → If not: output formatted for manual entry
```

### Calendar → Prep Bridge

```
User mentions: "I have a meeting with [person] tomorrow"

ops-meetingops:
  → If Calendar MCP available: pull meeting details
  → If not: ask user for attendee names, company, meeting purpose
  → ops-targetops: research attendees (WebSearch)
  → ops-contextops: pull prior relationship context
  → Output: pre-meeting brief as formatted Markdown
```

## Friction Reduction Patterns

### One-Paste Principle
User should never need to paste the same content into Claude twice. Each input is processed once and routed to all relevant outputs.

**Implementation:** Skill intake should parse the input comprehensively. If a transcript contains deal updates AND relationship intel AND action items, extract ALL of them in one pass and route to the appropriate destinations.

### Output-Ready Formatting
Every skill output should be formatted for its target destination. No reformatting needed by the user.

| Target | Format |
|--------|--------|
| Email (Gmail) | Subject line + body with greeting/closing |
| LinkedIn | Post text with hashtags, 1300 char max |
| HubSpot note | Plain text, max 500 words, structured |
| HubSpot properties | Property name → value pairs |
| ClickUp task | Title + description + assignee + due date |
| Google Doc | Markdown with headings/lists |
| Investor update | Email format with metrics table |

### Batch Processing Windows
Design workflows for 2x/day processing to reduce context switching:

**Morning batch (5 min):**
- Pull today's calendar → generate meeting preps
- Check stale deals → flag for attention
- Review overnight emails → extract action items

**Evening batch (10 min):**
- Process today's meetings → summaries + follow-ups
- Update HubSpot with day's interactions
- Draft tomorrow's priorities

### Progressive Automation Ladder

```
Start here:
  L1: Paste-and-process (always works, zero setup)
  ↓ When comfortable:
  L2: Chrome-assisted (browser automation, user confirms actions)
  ↓ When MCP available:
  L3: Full MCP (direct API, programmatic read/write)
```

**Rule:** Every L3 workflow must have an L1 fallback. Every L2 workflow must have an L1 fallback. Automations degrade gracefully.

## Workflow Design Template

When creating a new automated workflow:

```markdown
## Workflow: {Name}

**Trigger:** {What invokes this workflow}
**Automation level:** {L1 / L2 / L3}
**Skills involved:** {Ordered list of skills}
**Tools used:** {MCP tools, Chrome sequences, manual bridges}

### Steps
1. {Step with tool call}
2. {Step with tool call}
3. USER CONFIRMATION: {What needs approval}
4. {Step after confirmation}

### Error Handling
- If {tool} unavailable: {fallback}
- If {data} missing: {recovery}

### Output
- {Where the result goes}
- {Format of the output}
```
