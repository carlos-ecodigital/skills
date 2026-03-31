---
last-reviewed: 2026-03-30
---

# Input Format Handlers

> Per-format extraction instructions for W1 (raw input processing).
> Each handler specifies: what to extract, how to extract it, and how to flag confidence.

## Confidence Indicators

Used across all handlers to flag extraction certainty per field:

| Indicator | Meaning | Action |
|-----------|---------|--------|
| high | Field clearly readable/parseable. High certainty. | Accept as-is. |
| medium | Field partially visible or inferred. Likely correct. | Flag for review in W2. |
| low | Field illegible, ambiguous, or guessed. May be wrong. | Flag for manual correction in W2. |

---

## Business Card Photos

### Extraction Method
Claude vision analysis of card image.

### Vision Prompt Template
```
Analyze this business card image. Extract the following fields exactly as printed.
If a field is not present, return null. If partially obscured, provide your best
reading and flag confidence as "medium" or "low".

Extract:
- Full name
- Job title / role
- Company name
- Email address(es)
- Phone number(s) with any labels (mobile, office, fax)
- LinkedIn URL (if printed or QR code resolves to one)
- Website URL
- Physical address (if present)

For each field, rate confidence: high, medium, or low.
Return as structured JSON.
```

### Fields to Extract
`name`, `title`, `company`, `email`, `secondary_email`, `phone`, `secondary_phone`, `linkedin`, website (stored in `parse_notes`)

### Common OCR Challenges
- **Creased/bent cards:** Letters at fold lines may be distorted. Flag affected fields as medium confidence.
- **Small print:** Phone numbers and email in fine print. Zoom/enhance if possible. Flag as medium if under 6pt equivalent.
- **Non-Latin characters:** Chinese, Japanese, Korean, Arabic names. Extract both native script and any romanized version. Flag if uncertain about romanization.
- **QR codes:** Note presence in `parse_notes`. Cannot resolve QR from image alone; flag as "QR code present, manual scan needed."
- **Metallic/embossed cards:** Low contrast text. Flag all fields as medium confidence.
- **Double-sided cards:** If only one side photographed, note "card may have additional info on reverse" in `parse_notes`.

### Confidence Flagging Rules
- Email partially obscured or contains ambiguous characters (l/1, O/0) --> medium
- Name fully readable --> high
- Phone number with 1-2 digits unclear --> medium
- Title abbreviations (VP, SVP, MD) --> high (standard abbreviations)
- Company name partially hidden by finger/shadow --> medium

---

## Handwritten / Napkin Notes

### Extraction Method
Claude vision for handwriting recognition + NLP extraction for structured fields.

### Vision Prompt Template
```
This is a handwritten note (possibly on a napkin, notebook page, or scrap paper).
Transcribe ALL text as accurately as possible, preserving layout and structure.

Then extract structured data:
- People mentioned: names (look for capitalized words, titles before names)
- Companies mentioned: look for corporate suffixes, known brands, or context clues
- Action items: phrases starting with "send", "call", "schedule", "email", "follow up",
  "introduce", "connect", "share"
- Promises: "I'll", "we'll", "let me", "I promised", "agreed to"
- Stars, underlines, circles, arrows: note which text they emphasize

For illegible words, provide [best guess?] with a question mark.
Rate overall legibility: high, medium, low.
Return as structured JSON.
```

### NLP Extraction Rules
- **Names:** Capitalized words not at sentence start. Title + Name patterns ("Dr. Schmidt", "CEO Jan").
- **Companies:** Words followed by "GmbH", "AG", "Inc.", "Ltd.", "B.V." or known company names.
- **Action items:** Verbs: send, call, schedule, email, connect, introduce, share, demo, present.
- **Promises:** First person future: "I'll", "we'll", "let me", "I promised", "agreed to".

### Emphasis Signals
- Stars/asterisks next to a name or company --> boost `interest_signal` to high.
- Underlined text --> boost `interest_signal` by one level.
- Circled items --> treat as high-priority action items.
- Exclamation marks --> boost `interest_signal` by one level.
- Multiple mentions of same person/company --> boost `interest_signal`.

### Confidence Flagging
- Illegible words --> low. Record best guess in `parse_notes` as `"[word?]"`.
- Partially legible --> medium. Record reading with note.
- Clear handwriting --> high.

---

## Voice Memos / Transcripts

### Extraction Method
NLP analysis of transcript text (from Fireflies, Otter, or manual transcription).

### NLP Extraction Rules

**Speaker identification:**
- Look for speaker labels in transcript format ("Carlos:", "Speaker 1:").
- If unlabeled, infer from context (our team vs. external based on DE references).

**Company mentions:**
- Extract all company names mentioned in conversation.
- Map to contacts if speakers discuss "their company" or "we at [Company]".

**Name mentions:**
- All proper nouns in conversational context.
- "I spoke with Jan from Vattenfall" --> name: Jan, company: Vattenfall.
- "Their CTO, Maria" --> name: Maria, title: CTO.

**Promise detection keywords:**
- We promise: "I'll send", "we'll follow up", "let me connect you", "I'll schedule", "I promised".
- They promise: "I'll share", "let me introduce", "I'll send you", "we'll set up".

**Conversation quality inference:**
- Length proxy: <2 min discussion per topic = brief; 2-5 min = substantive; 5+ min = deep.
- Specificity: generic praise = low signal; named pain points = high signal.
- Questions asked: more questions from them = higher interest_signal.

### Confidence Flagging
- Clear transcript with speaker labels --> high.
- Auto-transcription with [inaudible] markers --> medium for affected segments.
- Names spelled phonetically --> medium. Add phonetic spelling to `parse_notes`.

---

## WhatsApp Screenshots / Exports

### Screenshot Extraction (Claude Vision)

```
This is a WhatsApp conversation screenshot. Extract:
- Contact name (from header or contact info)
- Phone number (if visible in contact info or message header)
- All message text with timestamps if visible
- Any shared media descriptions (photos, documents, voice notes)
- Who sent which messages (incoming vs outgoing)

Return as structured JSON with messages in chronological order.
```

### Text Export Extraction
WhatsApp exports follow the format: `[DD/MM/YYYY, HH:MM:SS] Name: Message`

Parse rules:
- Split on timestamp pattern.
- Extract contact name from non-"You" speaker.
- Concatenate all messages per speaker for conversation_summary.

### Phone Number Normalization
Strip and normalize to E.164:
1. Remove: `+`, spaces, dashes, parentheses, dots.
2. If starts with `00`, replace with `+`.
3. If starts with `0` and context suggests NL: prepend `+31`, drop leading `0`.
4. If starts with `0` and context suggests DE: prepend `+49`, drop leading `0`.
5. Store normalized form in `phone` field; original in `parse_notes`.

### Confidence Flagging
- Name from contact header --> high.
- Phone from contact info screen --> high.
- Phone inferred from message metadata --> medium.
- Name from message content only --> medium.

---

## LinkedIn Screenshots / Messages

### Extraction Method
Claude vision for screenshots; text parse for copied message threads.

### Fields to Extract
- **Name:** From profile header.
- **Headline:** Maps to `title`. LinkedIn headline often includes title + company.
- **Company:** From headline or "Experience" section if visible.
- **Shared connections:** Count and names if visible. Potential `introduction_chain`.
- **Message content:** Full thread for conversation_summary.
- **Connection request note:** Often contains context for why they reached out.

### Parsing Rules
- Headline format: typically "Title at Company" or "Title | Company" --> split on "at" or "|".
- Mutual connections: "X mutual connections" --> note count. Named mutuals --> potential intro chain.
- "Open to work" badge --> may indicate job transition; note in `classification_notes`.
- Profile URL: extract from browser address bar if visible, or construct from name slug.

### Confidence Flagging
- Name and headline from profile --> high.
- Company parsed from headline --> high if clear delimiter; medium if ambiguous.
- Title parsed from headline --> medium (headlines are often creative, not literal titles).

---

## Text / Markdown Brain Dump

### Extraction Method
NLP extraction from unstructured text.

### NLP Extraction Rules

**Names:**
- Capitalized words in non-sentence-start positions.
- Patterns: "Met [Name]", "Spoke with [Name]", "Talked to [Name]", "[Name] from [Company]".
- Title + Name: "CEO John", "Dr. Mueller", "Prof. Singh".

**Companies:**
- Words with corporate suffixes (GmbH, AG, Inc., Ltd., B.V., S.A., Corp.).
- Known energy/tech companies by name.
- Pattern: "[Name] from [Company]", "the [Company] team", "[Company]'s booth".

**Topics discussed:**
- Technical terms: MW, GW, load forecast, heat recovery, grid connection, PPA, etc.
- Business terms: pricing, contract, proposal, RFP, tender, budget, timeline.

**Action items:**
- Same verb detection as handwritten notes.
- Bullet points or numbered lists often indicate action items.

**Signal density:**
- More words written about a person = higher interest_signal.
- Specific numbers (MW, EUR, dates) = higher urgency.
- Generic mentions ("also met some people from X") = low signal.

### Confidence Flagging
- Clearly structured notes with names and companies --> high.
- Stream-of-consciousness text --> medium for individual fields.
- Ambiguous references ("that guy from the panel") --> low.

---

## Email Forwards

### Extraction Method
Parse email headers and body text.

### Parse Rules
- **From header:** Extract sender name and email. Map to `name` and `email`.
- **To/CC headers:** Note recipients for context but focus on sender as primary contact.
- **Subject line:** Often contains context: "Re: Meeting at [Event]", "Follow-up: [Topic]".
- **Body:** Extract conversation context, any mentioned promises or next steps.
- **Signature block:** Secondary source for title, company, phone, LinkedIn.
- **Attachments referenced:** Note in `parse_notes` (e.g., "attached proposal mentioned").

### Confidence Flagging
- Email address from From header --> high.
- Name from From header --> high.
- Title/company from signature --> high.
- Phone from signature --> high.
- Context from body --> medium (interpretation required).

---

## CSV / Spreadsheet (Attendee Lists)

### Extraction Method
Structured column mapping.

### Parse Rules
1. **Header detection:** Read first row. Map columns to `contact-record-schema` fields by name similarity.
2. **Common column names and mappings:**
   - "First Name" + "Last Name" --> concatenate to `name`.
   - "Full Name" / "Name" --> `name`.
   - "Organization" / "Company" / "Employer" --> `company`.
   - "Job Title" / "Position" / "Role" --> `title`.
   - "Email" / "E-mail" --> `email`.
   - "Phone" / "Mobile" / "Telephone" --> `phone`.
3. **Unmapped columns:** Preserve in `parse_notes` with original header name.

### Cross-Reference with Other Inputs
- After parsing attendee list, cross-reference names/companies against contacts extracted from other inputs (notes, cards, voice memos).
- If a match is found: merge attendee list data into the existing record. Set `source` to include both.
- If no match: create record with `conversation_quality: none` and `interest_signal: low`.

### Engagement Flagging
| Status | Criteria | Default Tier |
|--------|----------|-------------|
| Met + discussed | Matched in notes/cards with conversation data | Score normally |
| Met briefly | Matched in notes but minimal data | Score normally (low conversation_quality) |
| Listed but not met | On attendee list, no other source match | Tier `-` unless manually promoted |

### Confidence Flagging
- All fields from structured CSV --> high.
- Name matching across sources --> medium (could be different "John Smith").
- Company matching with slight name variation --> medium.

---

## European Business Card Conventions

### NL (Netherlands)
- "dhr./mw." prefixes
- Phone format: +31 6 XXXX XXXX for mobile, +31 XX XXX XXXX for landline
- KvK number on cards (chamber of commerce registration -- capture but do not use as contact field)
- "ir./drs./mr." academic titles

### DE (Germany)
- "Dipl.-Ing.", "Dr.", "Prof. Dr." title prefixes (preserve in record, they matter culturally)
- Phone format: +49 XXX XXXXXXX
- "GmbH/AG/e.V." company suffixes

### FR (France)
- "Mme/M." prefixes
- Phone format: +33 X XX XX XX XX
- "SAS/SARL/SA" company suffixes

### Nordic (SE/DK/NO/FI)
- Phone formats: +46/+45/+47/+358
- Minimal title culture -- first names are standard even in formal contexts

### CH (Switzerland)
- Multi-lingual cards common (DE/FR/IT on same card)
- Phone format: +41 XX XXX XX XX
- "AG/GmbH/SA/Sarl" depending on language region

---

## QR Code Handling

- Modern business cards increasingly include QR codes linking to vCard data, LinkedIn profiles, or digital business card platforms (HiHello, Blinq, Popl, CamCard)
- **Protocol:** Instruct user to scan QR code with phone camera. If it resolves to:
  - **vCard (.vcf):** Parse vCard fields directly -- this is the richest source
  - **LinkedIn profile URL:** Extract URL, use as `linkedin` field, delegate to `counter-party-intel` for profile enrichment
  - **Digital business card platform (HiHello, Blinq, etc.):** Ask user to open the link and screenshot or copy the contact details. These platforms often have richer data than the physical card.
  - **Company website URL:** Capture as company reference, not as contact data
- Claude cannot scan QR codes from photos -- always ask the user to scan with their phone first
