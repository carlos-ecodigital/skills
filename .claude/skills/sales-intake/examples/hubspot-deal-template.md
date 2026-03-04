# HubSpot Deal Template -- CRM Output Examples

Examples of the CRM records created by sales-intake after founder confirmation.

---

## Example 1: Colocation Track (C-NEO)

### Proposed HubSpot Updates

| Object Type | ID | Property | Current Value | New Value |
|-------------|-----|----------|---------------|-----------|
| Contact | NEW | firstname | -- | Jake |
| Contact | NEW | lastname | -- | Thompson |
| Contact | NEW | email | -- | jake@voltagepark.com |
| Contact | NEW | jobtitle | -- | CTO |
| Contact | NEW | phone | -- | +1 415 XXX XXXX |
| Contact | NEW | hs_lead_status | -- | NEW |
| Company | NEW | name | -- | Voltage Park |
| Company | NEW | domain | -- | voltagepark.com |
| Company | NEW | industry | -- | GPU Cloud / Neocloud |
| Company | NEW | city | -- | San Francisco |
| Company | NEW | country | -- | United States |
| Company | NEW | numberofemployees | -- | 50 |
| Company | NEW | description | -- | GPU cloud provider, Series B (~$120M). EU expansion for AI inference. |
| Deal | NEW | dealname | -- | Voltage Park - Neocloud Colocation |
| Deal | NEW | pipeline | -- | Sales |
| Deal | NEW | dealstage | -- | Lead |
| Deal | NEW | amount | -- | 3600000 |
| Deal | NEW | deal_currency_code | -- | EUR |
| Deal | NEW | closedate | -- | 2025-06-15 |
| Deal | NEW | description | -- | 5-10 MW GPU-ready colocation. Tier 1 (4.55). Referred by [advisor]. EU expansion driver. |

**Associations:**
- Contact (Jake Thompson) → Company (Voltage Park)
- Deal (Voltage Park - Neocloud Colocation) → Company (Voltage Park)
- Deal (Voltage Park - Neocloud Colocation) → Contact (Jake Thompson)

**Additional contact (if second contact):**

| Object Type | ID | Property | Current Value | New Value |
|-------------|-----|----------|---------------|-----------|
| Contact | NEW | firstname | -- | Sarah |
| Contact | NEW | lastname | -- | Chen |
| Contact | NEW | email | -- | sarah@voltagepark.com |
| Contact | NEW | jobtitle | -- | VP Infrastructure |

**Association:** Contact (Sarah Chen) → Company (Voltage Park), Deal

Approve? [Yes / No]

---

## Example 2: Site Track (S-GRW)

### Proposed HubSpot Updates

| Object Type | ID | Property | Current Value | New Value |
|-------------|-----|----------|---------------|-----------|
| Contact | NEW | firstname | -- | Pieter |
| Contact | NEW | lastname | -- | van der Berg |
| Contact | NEW | email | -- | pieter@kwekerijvanderberg.nl |
| Contact | NEW | jobtitle | -- | Eigenaar-directeur |
| Contact | NEW | phone | -- | +31 6 XX XXX XXX |
| Contact | NEW | hs_lead_status | -- | NEW |
| Company | NEW | name | -- | Kwekerij Van der Berg |
| Company | NEW | domain | -- | kwekerijvanderberg.nl |
| Company | NEW | industry | -- | Glastuinbouw / Greenhouse Horticulture |
| Company | NEW | city | -- | Westland |
| Company | NEW | state | -- | Zuid-Holland |
| Company | NEW | country | -- | Netherlands |
| Company | NEW | description | -- | 18 ha glastuinbouw (tomaat), Westland. 12 MVA Stedin. Gasrekening EUR 1.8M/jaar. WKK aan vervanging toe. |
| Deal | NEW | dealname | -- | Van der Berg - Grower Site Partnership |
| Deal | NEW | pipeline | -- | Project |
| Deal | NEW | dealstage | -- | Identified |
| Deal | NEW | description | -- | S-GRW Tier 1 (4.10). 18 ha Westland, 12 MVA grid. Heat partnership + ground lease. Referred by fellow grower. |

**Associations:**
- Contact (Pieter van der Berg) → Company (Kwekerij Van der Berg)
- Deal (Van der Berg - Grower Site Partnership) → Company (Kwekerij Van der Berg)
- Deal (Van der Berg - Grower Site Partnership) → Contact (Pieter van der Berg)

Approve? [Yes / No]

---

## Example 3: Site Track (S-DHN) -- Existing Company in CRM

When the company already exists in HubSpot (found during Phase 0 CRM lookup):

### Proposed HubSpot Updates

| Object Type | ID | Property | Current Value | New Value |
|-------------|-----|----------|---------------|-----------|
| Contact | NEW | firstname | -- | Marloes |
| Contact | NEW | lastname | -- | de Vries |
| Contact | NEW | email | -- | m.devries@ennaturlijk.nl |
| Contact | NEW | jobtitle | -- | Manager Business Development |
| Company | 28451 | description | District heating operator | District heating operator, Arnhem/Nijmegen/Purmerend. ~40K connections. Exploring DC waste heat for Arnhem-Zuid expansion. Wcw driver. |
| Deal | NEW | dealname | -- | Ennaturlijk - Arnhem DH Partnership |
| Deal | NEW | pipeline | -- | Project |
| Deal | NEW | dealstage | -- | Identified |
| Deal | NEW | closedate | -- | 2026-03-01 |
| Deal | NEW | description | -- | S-DHN Tier 2 (3.65). 10-25 MWth baseload for Arnhem-Zuid warmtenet. Wcw compliance driven. Met at Dutch Heat Conference. |

**Associations:**
- Contact (Marloes de Vries) → Company (Ennaturlijk, ID: 28451)
- Deal (Ennaturlijk - Arnhem DH Partnership) → Company (Ennaturlijk, ID: 28451)
- Deal (Ennaturlijk - Arnhem DH Partnership) → Contact (Marloes de Vries)

**Note:** Company record already exists (ID 28451). Updated description only. No duplicate company created.

Approve? [Yes / No]

---

## Key CRM Conventions

| Track | Pipeline | Default Stage | Contact Tags |
|-------|----------|---------------|--------------|
| Colocation (C-NEO) | Sales | Lead | `neocloud-buyer`, `active`, `tier-[N]` |
| Colocation (C-ENT) | Sales | Lead | `neocloud-buyer`, `active`, `tier-[N]` |
| Colocation (C-INS) | Sales | Lead | `neocloud-buyer`, `active`, `tier-[N]` |
| Site (S-GRW) | Project | Identified | `grower`, `active`, `tier-[N]` |
| Site (S-DHN) | Project | Identified | `dso`, `active`, `tier-[N]` |
| Site (S-IND) | Project | Identified | `neocloud-buyer`, `active`, `tier-[N]` |

**Rules:**
- Always search CRM before creating -- avoid duplicates
- Always present proposed changes table and wait for founder confirmation
- Use `manage_crm_objects` with `confirmationStatus: "CONFIRMED"` only after explicit approval
- Associate all contacts with their company AND the relevant deal
- Deal name format: `[Company] - [ICP Description]`
- Amount in EUR, use annual contract value estimate where available
