# Dedup & Matching Rules

> Deduplication algorithm and merge protocol for W2 (normalization & dedup).
> Applied after W1 extraction, before W3 CRM sync.

## Matching Cascade

Ordered by confidence. Run top-to-bottom; stop at first match.

| Priority | Match Type | Confidence | Method |
|----------|-----------|------------|--------|
| 1 | Exact email match | 100% | Lowercase both. Exact string comparison. |
| 2 | LinkedIn URL match | 95% | Normalize URL (strip trailing slash, query params, protocol). Compare path. |
| 3 | Name + company (fuzzy) | 90% | See fuzzy rules below. |
| 4 | Phone number (normalized) | 85% | See normalization rules below. |
| 5 | Name + conversation context | 70% | Same name discussed in overlapping context. Flag for human review. |

### Email Match Details
- Normalize: lowercase, trim whitespace.
- `jan.devries@vattenfall.com` == `Jan.DeVries@Vattenfall.com` --> match.
- Do NOT match across domains (personal vs. work email) without secondary confirmation.

### LinkedIn URL Normalization
```
Input:  https://www.linkedin.com/in/jandevries/
        https://linkedin.com/in/jandevries
        http://www.linkedin.com/in/jandevries?locale=en_US
Output: linkedin.com/in/jandevries
```
Strip: protocol, `www.`, trailing `/`, query parameters.

### Fuzzy Name + Company Rules

**Name normalization:**
1. Strip diacritics: "Muller" == "Mueller" == "Muller" (with umlaut).
2. Normalize prefixes: "de Vries" == "De Vries" == "de vries". Treat "de", "van", "von", "di", "el", "al" as case-insensitive.
3. First-initial match: "J. de Vries" matches "Jan de Vries" at same company.
4. Name order tolerance: "Jan de Vries" matches "de Vries, Jan".
5. Hyphenated names: "Anna-Maria" matches "Anna Maria" (strip hyphen).
6. Nickname tolerance: NOT automatic. "Bob" does NOT auto-match "Robert". Flag as potential match (70% confidence) for review.

**Company normalization:**
1. Strip suffixes: "GmbH", "AG", "Inc.", "Ltd.", "B.V.", "S.A.", "Corp.", "Co.", "SE", "NV", "PLC".
2. Normalize spacing: "Digital Energy" == "DigitalEnergy" == "Digital  Energy".
3. Known aliases: maintain a lookup for common variations (e.g., "Google" == "Alphabet" for matching purposes).
4. Subsidiary awareness: "Google Cloud" and "Google" are related but distinct. Match at parent level, flag for review.

### Phone Number Normalization
```
Step 1: Remove all non-digit characters: +, -, (, ), spaces, dots
Step 2: Handle country codes:
        - Starts with "00"  --> replace with "+"
        - Starts with "0"   --> context-dependent (NL: +31, DE: +49, CH: +41)
        - Starts with "31"  --> prepend "+"
        - Starts with "49"  --> prepend "+"
Step 3: Store in E.164 format: +[country][number]
Step 4: Compare last 9 digits if full normalization is ambiguous
```

Example: `+31 (0)6 1234 5678` == `0031612345678` == `06-1234-5678` (NL context) --> all normalize to `+31612345678`.

### Name + Conversation Context Match (70%)
When names match but no email/phone/LinkedIn overlap:
- Check if conversation summaries reference the same topics, events, or companies.
- Check if `source_detail` overlaps (same event/meeting).
- If both conditions met --> 70% confidence match. Flag for human review.
- Present both records side-by-side in review CSV with `row_review: needs_fix`.

---

## Merge Protocol

When a duplicate is detected, merge fields using the priority rules below.

### Per-Field Priority

| Field | Priority Source | Rationale |
|-------|---------------|-----------|
| `name` | Business card > LinkedIn > other | Most formal/accurate spelling. |
| `title` | LinkedIn > business card > notes | LinkedIn is most current; cards may be outdated. |
| `company` | Business card > LinkedIn > notes | Card reflects current role at time of meeting. |
| `email` | Business card (work) > email forward > WhatsApp | Work email preferred for B2B follow-up. |
| `secondary_email` | Any source not used for primary | Store personal/alternate. |
| `phone` | WhatsApp > business card > notes | WhatsApp = confirmed mobile/direct line. |
| `secondary_phone` | Any source not used for primary | Store office/alternate. |
| `linkedin` | LinkedIn screenshot > business card > notes | Most accurate from LinkedIn itself. |
| `conversation_summary` | **MERGE ALL** | Concatenate with source attribution. See format below. |
| `conversation_quality` | Take highest | Best interaction reflects true relationship quality. |
| `interest_signal` | Take highest | Strongest signal is most relevant. |
| `promises_we_made` | **MERGE ALL** | Combine all promises from all touchpoints. Deduplicate exact matches. |
| `promises_they_made` | **MERGE ALL** | Same as above. |
| `source_type` | List all | Record all source types encountered. |
| `source_detail` | List all | Record all source details. |
| `source_date` | Take earliest | First encounter date. |
| `confidence` | Take highest per field | Best reading across sources wins. |

### Conversation Summary Merge Format
```
[card photo] Contact information captured.
[handwritten notes] Discussed 50MW load forecast for Amsterdam data center.
  Interested in heat recovery model. Asked about timeline for Q3.
[WhatsApp] Followed up re: heat recovery model. Shared preliminary specs.
  Confirmed meeting at DCW next week.
[LinkedIn] Connected post-conference. Mentioned sharing with internal team.
```

Each entry prefixed with `[source]` on its own line.

---

## Company Grouping

After person-level dedup, group contacts by normalized company name.

### Grouping Algorithm
1. Normalize all company names (strip suffixes, lowercase, trim).
2. Group contacts sharing the same normalized company.
3. Flag groups with 2+ contacts as "multi-threaded".
4. Check HubSpot for additional existing contacts at the same company.

### Company Summary (generated per group)

| Field | Value |
|-------|-------|
| Company | Normalized name |
| Contacts in batch | Count + names |
| Existing HubSpot contacts | Count + names (if any) |
| Roles covered | List of titles |
| Aggregate conversation quality | Highest quality across all contacts |
| Multi-threaded flag | Yes if 2+ contacts |
| Account strategy note | Auto-generated: "Multiple entry points at [Company]. Consider coordinated outreach." |

---

## Cross-Reference Protocol

Before creating new HubSpot records in W3, check for existing data across all systems.

### Search Order

| Step | System | Search Method | Match Action |
|------|--------|--------------|-------------|
| 1 | HubSpot | Search by email (exact) | If found: MERGE new data into existing record. Flag "returning contact". |
| 2 | HubSpot | Search by name + company (fuzzy) | If found: present candidate match for human review. |
| 3 | HubSpot | Search by phone (normalized) | If found: MERGE. |
| 4 | ops-contextops | Search relationship records by name/company | If found: enrich with relationship history. Note prior interactions. |
| 5 | Fireflies | Search transcripts by person name | If found: note prior meetings. Add to `parse_notes`: "X prior Fireflies transcripts found." |

### Returning Contact Handling
When an existing record is found:
- Do NOT create a new HubSpot contact.
- MERGE new fields into existing record (using per-field priority above).
- Append new conversation_summary entries (do not overwrite).
- Update `source_date` only if new encounter is more recent.
- Add note to HubSpot activity timeline: "Re-encountered at [event] on [date]."
- Boost score: +0.5 (repeat encounter override from scoring-framework).

---

## Merge Presentation Format

For the review CSV and human review in W2, merged contacts are presented as follows:

```
MERGED: Jan de Vries -- CTO @ Vattenfall
  Email: j.devries@vattenfall.com [card photo]
  Phone: +31 6 1234 5678 [WhatsApp]
  LinkedIn: linkedin.com/in/jandevries [screenshot]
  Context: "Discussed 50MW load forecast for Amsterdam" [notes] +
           "Followed up re: heat recovery model" [WhatsApp]
  Sources: card photo, handwritten notes, WhatsApp, LinkedIn
  Prior history: Met at DCW 2025, 2 prior Fireflies transcripts
  -> MERGE into existing HubSpot contact #12345
```

### Merge Decision Labels

| Label | Meaning |
|-------|---------|
| `MERGED` | Two or more input sources combined into one record. |
| `MERGED + EXISTING` | Merged inputs AND matched to existing HubSpot record. |
| `NEW` | No duplicates found. Fresh contact. |
| `REVIEW` | Potential match detected (70-85% confidence). Human must confirm. |

### Review CSV Columns for Merge Cases
Add these columns when duplicates are present:
- `Merge Status`: NEW / MERGED / MERGED + EXISTING / REVIEW
- `Merge Sources`: Comma-separated list of input sources that were combined.
- `Existing HubSpot ID`: If matched to existing record.
- `Merge Confidence`: Percentage from matching cascade.
