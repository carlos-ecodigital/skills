# MCP Server Setup Guide -- Digital Energy

> Follow this guide to connect external tools to your Claude Code skill ecosystem. Each server unlocks direct data access for the ops skills that reference it.

## Overview

| MCP Server | What It Connects | Skills That Use It | Auth Method |
|------------|-----------------|-------------------|-------------|
| Google Workspace | Gmail, Calendar, Drive, Sheets, Docs | meetingops, outreachops, chiefops, dataroomops, dealops | OAuth 2.0 (Google Cloud Console) |
| Fireflies | Meeting transcripts | meetingops, chiefops | API key |
| ClickUp | Tasks and projects | meetingops, chiefops, dealops | OAuth (first-party remote) |
| HubSpot | CRM (contacts, deals, pipeline) | dealops, outreachops, targetops, dataroomops, chiefops, meetingops | Already connected via Claude plugin |

**HubSpot is already connected** through the Claude plugin system. No `.mcp.json` config needed for it.

---

## 1. Google Workspace MCP

**Package:** `workspace-mcp` (PyPI) / `taylorwilsdon/google_workspace_mcp` (GitHub)
**Install:** `uvx workspace-mcp`
**Capabilities:** Gmail (read/send), Calendar (read events), Drive (list/create files), Sheets (read/write cells), Docs (create/edit), Slides, Contacts

### Step 1: Create Google Cloud OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use existing): e.g., "DE Claude MCP"
3. Enable these APIs:
   - Gmail API
   - Google Calendar API
   - Google Drive API
   - Google Sheets API
   - Google Docs API
4. Go to **Credentials** > **Create Credentials** > **OAuth 2.0 Client ID**
5. Application type: **Desktop app**
6. Name: "Claude Code MCP"
7. Download the JSON file -- save as `client_secret.json`
8. Go to **OAuth consent screen** > add your Gmail address as a test user

### Step 2: Configure in `.mcp.json`

Create or edit `/Users/crmg/Documents/DE Claude/.mcp.json`:

```json
{
  "mcpServers": {
    "google_workspace": {
      "command": "uvx",
      "args": ["workspace-mcp"],
      "env": {
        "GOOGLE_OAUTH_CREDENTIALS_PATH": "/path/to/client_secret.json",
        "GOOGLE_OAUTH_TOKEN_PATH": "/path/to/token.json"
      }
    }
  }
}
```

Replace `/path/to/` with the actual path where you saved `client_secret.json`. The `token.json` will be created automatically on first auth.

### Step 3: First Run Auth

1. Start Claude Code in the project directory
2. The server will open a browser window for Google OAuth consent
3. Sign in with the DE Gmail account
4. Grant permissions (Gmail, Calendar, Drive, Sheets, Docs)
5. Token is saved -- subsequent runs authenticate automatically

### Verification Test

Ask Claude Code:
- "What meetings do I have this week?" (tests Calendar)
- "List files in my Drive root" (tests Drive)
- "Show my recent emails" (tests Gmail)

---

## 2. Fireflies MCP

**Type:** Remote MCP server (Streamable HTTP)
**Endpoint:** `https://api.fireflies.ai/mcp`
**Capabilities:** Search transcripts, get full transcript details, generate summaries
**Tools available:** `fireflies_get_transcripts`, `fireflies_get_transcript_details`, `fireflies_search_transcripts`, `fireflies_generate_summary`

### Step 1: Get Your Fireflies API Key

1. Log into [Fireflies.ai](https://app.fireflies.ai/)
2. Go to **Settings** > **Integrations** > **API & Webhooks**
3. Click **Generate API Key** (or copy existing)
4. Copy the key

### Step 2: Configure in `.mcp.json`

Add to your `.mcp.json` (merge with existing config):

```json
{
  "mcpServers": {
    "fireflies": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://api.fireflies.ai/mcp",
        "--header",
        "Authorization: Bearer YOUR_FIREFLIES_API_KEY"
      ]
    }
  }
}
```

Replace `YOUR_FIREFLIES_API_KEY` with your actual key.

### Verification Test

Ask Claude Code:
- "Search my Fireflies transcripts from last week"
- "Get the details of my most recent meeting transcript"

---

## 3. ClickUp MCP

**Type:** First-party remote MCP server (Streamable HTTP)
**Endpoint:** `https://mcp.clickup.com/mcp`
**Capabilities:** Create tasks, update tasks, list tasks, manage spaces/lists
**Auth:** OAuth (handled by ClickUp's MCP server directly)

### Step 1: Configure in `.mcp.json`

Add to your `.mcp.json`:

```json
{
  "mcpServers": {
    "clickup": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.clickup.com/mcp"
      ]
    }
  }
}
```

### Step 2: First Run Auth

1. Start Claude Code
2. ClickUp's MCP server will prompt you to authenticate via browser
3. Sign in with your ClickUp account and authorize access

### Alternative: Community Package (More Tools)

If you need more granular control (54+ tools), use the community package instead:

```json
{
  "mcpServers": {
    "clickup": {
      "command": "npx",
      "args": ["-y", "@taazkareem/clickup-mcp-server"],
      "env": {
        "CLICKUP_API_KEY": "YOUR_CLICKUP_API_KEY"
      }
    }
  }
}
```

Get API key: ClickUp > Settings > Apps > Generate API Token.

### Verification Test

Ask Claude Code:
- "List my ClickUp spaces"
- "Show open tasks in [workspace name]"

---

## 4. Complete `.mcp.json`

Here's the full combined config with all three servers:

```json
{
  "mcpServers": {
    "google_workspace": {
      "command": "uvx",
      "args": ["workspace-mcp"],
      "env": {
        "GOOGLE_OAUTH_CREDENTIALS_PATH": "/path/to/client_secret.json",
        "GOOGLE_OAUTH_TOKEN_PATH": "/path/to/token.json"
      }
    },
    "fireflies": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://api.fireflies.ai/mcp",
        "--header",
        "Authorization: Bearer YOUR_FIREFLIES_API_KEY"
      ]
    },
    "clickup": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.clickup.com/mcp"
      ]
    }
  }
}
```

**Place this file at:** `/Users/crmg/Documents/DE Claude/.mcp.json` (project root).

---

## 5. Verification Tests

After connecting all servers, run these tests to confirm everything works:

### Individual Server Tests

| Test | Command to Claude | Expected Result | Server |
|------|------------------|-----------------|--------|
| Calendar | "What meetings do I have tomorrow?" | Lists calendar events | Google Workspace |
| Gmail | "Show my 5 most recent emails" | Lists email subjects/senders | Google Workspace |
| Drive | "List files in the Data Room folder" | Lists Drive files | Google Workspace |
| Fireflies | "Search transcripts from this week" | Lists recent transcripts | Fireflies |
| ClickUp | "List my open tasks" | Lists ClickUp tasks | ClickUp |
| HubSpot | "Show me active deals in the pipeline" | Lists CRM deals | HubSpot (plugin) |

### Skill Integration Tests

| Test | Invocation | What It Proves |
|------|-----------|----------------|
| Pipeline review | "Give me a pipeline review" | `ops-dealops` pulls from HubSpot directly |
| Meeting processing | "Process my last meeting" | `ops-meetings` pulls from Fireflies directly |
| Weekly brief | "Give me the weekly brief" | `ops-chiefops` assembles from Calendar + HubSpot + ClickUp |
| Outreach draft | "Draft an email to [contact]" | `ops-outreachops` pulls contact context from HubSpot |
| Data room audit | "Audit the data room" | `ops-dataroomops` checks Drive against template |

### End-to-End Chain Test

The ultimate integration test -- a single workflow that touches all servers:

1. "Process my last meeting with [investor name]"
   - Fireflies MCP: pulls transcript
   - `ops-meetings`: generates summary + action items
2. "Update HubSpot with the meeting outcomes"
   - HubSpot plugin: updates contact notes + deal stage
3. "Create follow-up tasks in ClickUp"
   - ClickUp MCP: creates tasks from action items
4. "Draft the follow-up email"
   - HubSpot plugin: pulls contact context
   - Gmail MCP: stages the draft (sends after approval)

If all four steps complete without manual paste or copy, MCP integration is fully operational.

---

## 6. Troubleshooting

### Google Workspace

| Issue | Fix |
|-------|-----|
| "Token expired" | Delete `token.json` and re-authenticate |
| "API not enabled" | Check Google Cloud Console > APIs & Services > enable the missing API |
| "Insufficient permissions" | Re-run OAuth flow, ensure all scopes are granted |
| "Rate limited" | Google APIs have per-minute quotas. Wait and retry. |

### Fireflies

| Issue | Fix |
|-------|-----|
| "Unauthorized" | Check API key is correct and active in Fireflies settings |
| "No transcripts found" | Verify Fireflies is recording meetings (check Fireflies dashboard) |
| "Connection refused" | Check `npx mcp-remote` is installed: `npm install -g mcp-remote` |

### ClickUp

| Issue | Fix |
|-------|-----|
| "OAuth failed" | Clear browser cookies for ClickUp and retry |
| "No workspaces" | Ensure you're authenticating with the correct ClickUp account |
| "Connection timeout" | ClickUp's MCP endpoint may be slow on first connection. Retry. |

### General

| Issue | Fix |
|-------|-----|
| Server not appearing in Claude | Check `.mcp.json` is in the project root, restart Claude Code |
| "Tool not found" | Server may not be connected. Check `/mcp` in Claude Code for status |
| Skill can't use MCP tool | Check skill's `allowed-tools` includes the MCP server pattern |
| Multiple servers failing | Check internet connection. Remote MCP servers need network access. |

---

## 7. Tool Naming in Skills

Skills reference MCP tools using the pattern `mcp__<server-name>__<tool-name>` or `mcp__<server-name>__*` (wildcard).

When MCP servers connect, the actual tool names registered may differ slightly from what's in skill files (e.g., HubSpot uses a UUID-based server ID like `mcp__2c81bf85-...`). Claude Code resolves these automatically for plugin-based servers.

For `.mcp.json`-based servers, the server name in the config becomes the `<server-name>` in the tool pattern:
- Config key `"google_workspace"` -> tools are `mcp__google_workspace__*`
- Config key `"fireflies"` -> tools are `mcp__fireflies__*`
- Config key `"clickup"` -> tools are `mcp__clickup__*`

**Keep the config keys matching what's in the skill files.**

---

## 8. Security Notes

- **Gmail sending:** All skills that use Gmail MCP require explicit user approval before sending any email. This is enforced in each skill's rules section.
- **HubSpot writes:** Any CRM data modification (deal stage changes, contact updates) requires user confirmation. Enforced by both Claude safety rules and skill instructions.
- **Credentials:** Never commit `.mcp.json` with API keys to git. Add it to `.gitignore`.
- **OAuth tokens:** `token.json` files contain refresh tokens. Store securely.
- **Fireflies API key:** Treat as a secret. Do not share or commit.
