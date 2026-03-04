# United Kingdom -- Entity Types

## Private Company Limited by Shares (Ltd)

The standard commercial vehicle for UK businesses. Most NDA counterparties DE encounters will be Ltd companies.

| Feature | Detail |
|---|---|
| Legislation | Companies Act 2006, Part 2 |
| Minimum share capital | No statutory minimum (GBP 1 common) |
| Formation | Incorporation at Companies House; memorandum + articles of association |
| Formation time | Same-day digital incorporation; 2-5 days postal |
| Company number | Unique 8-digit identifier (e.g., 13779434 for Stelia) |
| Registered office | Must be in England & Wales, Scotland, or Northern Ireland |
| Suffix | "Limited" or "Ltd" |

**Governance:**
- **Directors:** Minimum 1 director (natural person required since October 2015). No requirement for a company secretary (optional for Ltd).
- **Shareholders:** Minimum 1. Annual confirmation statement required.
- **Articles of association:** Model articles apply by default (The Companies (Model Articles) Regulations 2008) unless bespoke articles adopted.
- **Accounts:** Must file at Companies House annually. Micro, small, and medium companies have abbreviated filing options.

**Share transfer:** No notarial requirement (contrast with NL BV). Transfer by stock transfer form + board approval (if articles restrict transfer). Many Ltd articles include pre-emption rights on transfer.

---

## Public Limited Company (PLC)

For larger, listed, or publicly traded companies.

| Feature | Detail |
|---|---|
| Legislation | Companies Act 2006, Parts 2 and 20 |
| Minimum share capital | GBP 50,000 (minimum 25% paid up on allotment, s.586) |
| Suffix | "Public Limited Company" or "PLC" |
| Company secretary | Mandatory (must be qualified, s.271) |
| Trading certificate | Required before trading (s.761) |
| Listing | May list on London Stock Exchange (Main Market or AIM) subject to Listing Rules |

**NDA relevance:** If the counterparty is a PLC, they will typically have an in-house legal team and standardised NDA templates. Their NDAs tend to be more polished but also more protective of their interests. Expect sophisticated terms.

---

## Limited Liability Partnership (LLP)

Hybrid vehicle combining partnership flexibility with limited liability.

| Feature | Detail |
|---|---|
| Legislation | Limited Liability Partnerships Act 2000 |
| Formation | Incorporation at Companies House |
| Members | Minimum 2 designated members (filing obligations) |
| Liability | Members' liability limited to contributions |
| Tax treatment | Tax-transparent — members taxed individually |
| Accounts | Must file at Companies House (similar requirements to Ltd) |

**NDA relevance:** Professional services firms (law firms, accounting firms, consultancies) are often LLPs. The NDA signatory will be a "member" or "designated member," not a "director." Signatory authority works differently — check the LLP agreement.

---

## Other Entity Types

| Type | Key Feature | NDA Relevance |
|---|---|---|
| **Sole trader** | Individual trading without limited liability | Not a separate legal entity — the individual signs personally |
| **General partnership** | Two+ persons in business together; no limited liability | Partners bind the firm; any partner can sign (Partnership Act 1890, s.5) |
| **Limited partnership (LP)** | General + limited partners; LP Act 1907 | Less common in UK commercial practice; verify which partner has authority |
| **Community Interest Company (CIC)** | Social enterprise with community benefit lock | Uncommon NDA counterparty |
| **Scottish Limited Partnership (SLP)** | Has separate legal personality (unlike English LP) | Verify carefully — sometimes used in fund structures |

---

## Companies House

The UK company registry. Critical for NDA review Phase 1 counterparty validation.

### What Companies House Provides

| Information | Where | NDA Review Use |
|---|---|---|
| Company name and number | Company overview | Match against NDA party name |
| Registered office address | Company overview | Match against NDA address |
| Company status | Company overview | Verify **Active** (not dissolved, liquidated, or in administration) |
| Date of incorporation | Company overview | Age of entity — context indicator |
| SIC codes | Company overview | Industry classification |
| Directors and officers | Officers tab | Verify NDA signatory is listed as director/officer |
| Persons with significant control (PSC) | PSC tab | Identify UBOs (>25% shares/voting/control) |
| Filing history | Filing history tab | Check if accounts and confirmation statements are up to date |
| Accounts | Filing history | Financial snapshot (for larger companies) |
| Charges | Charges tab | Registered security interests (liens, debentures) |

### Company Status Values

| Status | Meaning | NDA Action |
|---|---|---|
| **Active** | Normal trading entity | Proceed |
| **Active - Proposal to Strike Off** | Company or Companies House has initiated striking off | **FLAG:** Entity may cease to exist. Verify with counterparty before signing. |
| **In Administration** | Under insolvency proceedings | **RED FLAG:** Do not sign without understanding the context. Administrator may need to approve. |
| **In Liquidation** | Being wound up | **RED FLAG:** Entity is being dissolved. Signing an NDA is questionable. |
| **Dissolved** | No longer exists | **BLOCK:** Cannot contract with a dissolved entity. |
| **Dormant** | Not trading; filed dormant accounts | **FLAG:** Verify why the counterparty is a dormant company. |

### Verification Checklist (for NDA Review Phase 1, Step 1.2)

1. **Search** Companies House (https://find-and-update.company-information.service.gov.uk/) for the counterparty name
2. **Match** company number against NDA (if stated)
3. **Verify** status = Active
4. **Check** registered office matches NDA address (note: trading address may differ)
5. **Verify** NDA signatory appears in the Officers list as a current director
6. **Check** filing status: are confirmation statement and accounts up to date? Overdue filings may indicate a company in distress.
7. **Note** PSC entries for relationship context
8. **Check** charges register if relevant (e.g., assessing counterparty financial health)

---

## Director Authority

### Statutory Position (Companies Act 2006)

| Section | Rule | Practical Effect |
|---|---|---|
| **s.40** | In favour of a person dealing in good faith, the power of the directors to bind the company is deemed to be free of any limitation under the company's constitution | Third parties (including DE) can assume a director has authority to sign an NDA unless DE knows otherwise |
| **s.43** | A contract can be made on behalf of a company by any person acting under its authority | Does not need to be a director — anyone authorised can bind the company |
| **s.44** | A document is executed by a company by being signed by two directors, or one director + company secretary, or by affixing the common seal | For deeds. Simple contracts (including NDAs) only need one authorised signatory |

**Practical guidance for NDA review:**
- If the signatory is listed as a director on Companies House → authority can be assumed (s.40 protection).
- If the signatory is not a director → they may still have authority under s.43 (e.g., General Counsel, Head of Legal), but this is not independently verifiable. Flag with "[VERIFY: Signatory not listed as director — authority assumed under s.43 CA 2006]."
- For high-stakes NDAs, consider requesting confirmation of signatory authority.

---

## Registered Office vs Trading Address

| Concept | Legal Significance |
|---|---|
| **Registered office** | The official address on file at Companies House. Legal notices served to this address are valid (s.1139 CA 2006). |
| **Trading address / principal place of business** | Where the company actually operates. No legal significance for service of notices unless contractually specified. |

**NDA review note:** If the NDA address differs from the Companies House registered office, this is not necessarily a problem — many companies use their trading address in commercial agreements. However, if DE needs to serve a notice under the NDA, check whether the notice clause specifies the registered office or the address in the NDA.

---

## Entity Verification Quick Reference

| Check | Source | Pass | Fail |
|---|---|---|---|
| Entity exists | Companies House | Company number found | No match → verify name/number |
| Entity is active | Companies House status | "Active" | Dissolved/liquidation/administration → RED FLAG |
| Signatory is director | Companies House officers | Name appears as current director | Not listed → FLAG for verification |
| Filings current | Companies House filing history | Confirmation statement + accounts up to date | Overdue → FLAG (possible distress) |
| Registered office matches | Companies House vs NDA | Match (or explained trading address difference) | Major discrepancy → verify |
