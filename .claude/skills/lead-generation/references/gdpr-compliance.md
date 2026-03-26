# GDPR Compliance — Data Protection Guidance for Lead Generation

> **Disclaimer**: This document provides practical guidance for B2B lead generation activities. It is NOT legal advice. Consult qualified legal counsel for binding compliance decisions.

---

## Legal Basis: Legitimate Interest — Art. 6(1)(f) GDPR

B2B lead generation relies on **legitimate interest** as the legal basis for processing personal data (names, titles, business email addresses, LinkedIn URLs) of business professionals.

### Article 6(1)(f)
Processing is lawful when it is "necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject."

### Recital 47
"The processing of personal data for direct marketing purposes may be regarded as carried out for a legitimate interest."

### Three-Part Test (Legitimate Interest Assessment)
1. **Purpose test**: Is there a legitimate interest? Yes — B2B business development and direct marketing to business professionals in their professional capacity.
2. **Necessity test**: Is processing necessary for this purpose? Yes — identifying and contacting decision-makers requires processing their professional data.
3. **Balancing test**: Do the data subject's rights override the interest? Generally no for B2B professional data — individuals acting in a business capacity have a lower expectation of privacy for their professional information.

---

## Data Collected vs. Not Collected

### Data We Collect (Permitted)
- Full name (professional context)
- Job title / role
- Business email address
- Business phone number
- LinkedIn profile URL (publicly available)
- Company name and details (not personal data)
- Professional biography / conference appearances

### Data We Do NOT Collect (Prohibited)
- Personal email addresses (gmail, hotmail, etc.)
- Personal phone numbers (unless also used as business number)
- Home addresses
- Date of birth
- Social media profiles (personal Facebook, Instagram, etc.)
- Political opinions, religious beliefs, health data, or other special category data
- Financial or salary information of individuals
- Family or relationship information
- Any data about individuals acting in a non-professional capacity

---

## Data Minimization — Art. 5(1)(c)

Only collect data that is adequate, relevant, and limited to what is necessary:
- Collect the minimum contacts needed per account (Tier 1=3, Tier 2=2, Tier 3=1)
- Do not stockpile contacts beyond what is needed for active outreach
- Remove or anonymize data that is no longer relevant to the business purpose
- Revenue and employee data are company-level (not personal data) — no GDPR restriction

---

## Retention Policy

### Active Pipeline (0-12 months)
- Data actively used for outreach and sales engagement
- Regular updates to maintain accuracy
- Review at 12-month mark

### Review Cycle (12 months)
- At 12 months, review all contact data:
  - Is there an active business relationship or ongoing outreach?
  - Has the contact responded (positively or negatively)?
  - Is the data still accurate?
- If no active purpose: either refresh for a new campaign cycle or delete

### Maximum Retention (24 months)
- Contact data without any engagement or refresh should be deleted at 24 months
- Company-level data (non-personal) can be retained indefinitely
- Document the retention review in Notes column or CRM

---

## Data Subject Rights

### Right to Erasure (Art. 17)
- If a contact requests deletion of their data, comply within 30 days
- Remove from xlsx, HubSpot, and any other storage
- Document the request and action taken
- Add to a suppression list to prevent re-collection

### Right to Object (Art. 21)
- Data subjects can object to processing based on legitimate interest
- If objection received, cease processing unless compelling legitimate grounds exist
- For direct marketing specifically, objection must always be honored (Art. 21(3))
- Add objecting contacts to a "do not contact" suppression list

### Right of Access (Art. 15)
- If a contact requests access to their data, provide within 30 days
- Include: what data is held, purposes, sources, recipients, retention period

### Right to Rectification (Art. 16)
- If a contact points out inaccurate data, correct it promptly

---

## Source Documentation

### Why Document Sources
- GDPR Art. 14 requires informing data subjects of the source of their data when not collected directly from them
- Maintaining source records enables compliance with access requests
- Source documentation supports the legitimate interest assessment

### How to Document
- The "Source" column (Z) in the output schema must list where data was obtained
- Acceptable source descriptions:
  - "Company website leadership page"
  - "KVK Handelsregister"
  - "LinkedIn public profile"
  - "NZa open data 2024"
  - "Royal FloraHolland annual report 2024"
  - "Conference speaker list — Zorg & ICT 2025"
- Every row must have a source; "unknown" is not acceptable

---

## Cross-Border Considerations (NL/BE/LU)

- All three countries are EU member states; GDPR applies uniformly
- **Netherlands**: Autoriteit Persoonsgegevens (AP) is the supervisory authority
- **Belgium**: Gegevensbeschermingsautoriteit (GBA) / Autorite de protection des donnees (APD)
- **Luxembourg**: Commission nationale pour la protection des donnees (CNPD)
- No additional data transfer restrictions within NL/BE/LU (all EU)
- If data is processed outside the EU (e.g., US-based tools), ensure adequate safeguards (Standard Contractual Clauses, adequacy decision)

---

## Output Metadata

Every xlsx output file should include a metadata tab or header row with:
- Date of data collection
- Legal basis: "Legitimate interest — Art. 6(1)(f) GDPR"
- Data controller: [Company name]
- Purpose: "B2B lead generation and direct marketing"
- Retention review date: [Collection date + 12 months]
- Sources: [Summary of primary sources used]

---

## Practical Guidance

### Do
- Only process business contact data in a professional context
- Document your sources for every data point
- Honor opt-out and erasure requests immediately
- Keep a suppression list of contacts who have objected
- Review and refresh data regularly
- Use business email addresses only
- Include an unsubscribe mechanism in all outreach emails

### Do Not
- Collect personal (non-business) contact details
- Retain data beyond 24 months without active purpose
- Ignore data subject requests (access, erasure, objection)
- Share contact data with third parties without a lawful basis
- Process data of individuals not acting in a business capacity
- Scrape data in ways that violate platform terms of service (e.g., bulk LinkedIn scraping)
- Assume consent — legitimate interest does not require consent, but it does require a balancing test

### Tool-Specific GDPR Notes
- **LinkedIn**: Using LinkedIn for targeted manual research is generally acceptable; automated scraping violates ToS and raises GDPR concerns
- **Apollo/ZoomInfo**: Verify that the tool provider has a valid legal basis for the data they provide; check their GDPR compliance documentation
- **Clay**: As an orchestration layer, GDPR responsibility extends to the underlying data providers Clay accesses
- **HubSpot**: Ensure HubSpot DPA (Data Processing Agreement) is signed; HubSpot acts as a data processor
- **Email verification tools**: Sending verification pings to email addresses constitutes processing; ensure the verification provider is GDPR-compliant
