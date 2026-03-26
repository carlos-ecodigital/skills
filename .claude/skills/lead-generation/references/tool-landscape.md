# Tool Landscape — Sales Intelligence & Enrichment Tools

## Overview

This reference compares the major sales intelligence and enrichment platforms. The lead generation skill is designed to be **tool-agnostic** — it can work with any combination of these tools or with purely manual research. Start with manual research and public sources; layer in tools as needed.

---

## Platform Comparison

### 1. Clay

**Category**: Waterfall enrichment orchestration

**What It Does**:
- Connects 100+ data providers through a single interface
- Waterfall enrichment: tries Provider A, falls back to B, then C
- AI-powered research agent (Claygent) for custom lookups
- Table-based workflow builder
- Integrates with CRM (HubSpot, Salesforce)

**Pricing (approximate, as of 2025)**:
- Starter: $149/mo (2,000 credits)
- Explorer: $349/mo (10,000 credits)
- Pro: $800/mo (50,000 credits)
- Enterprise: Custom

**Strengths**:
- Best-in-class waterfall enrichment (try multiple providers automatically)
- Flexible workflow builder
- AI agent for custom research tasks
- Good for Benelux due to multi-provider coverage
- Reduces dependency on any single data provider

**Weaknesses**:
- Credit-based pricing can be expensive at scale
- Learning curve for workflow builder
- Data quality depends on underlying providers
- Limited native European data (relies on provider integrations)

**Best For**: Enrichment workflows after initial company list is built

---

### 2. Apollo.io

**Category**: Sales intelligence + engagement

**What It Does**:
- Database of ~275M contacts and ~73M companies
- Email finding and verification
- Sequences (email outreach automation)
- Chrome extension for LinkedIn prospecting
- Intent data signals

**Pricing (approximate)**:
- Free: 10,000 records/mo (limited)
- Basic: $49/user/mo
- Professional: $79/user/mo
- Organization: $119/user/mo

**Strengths**:
- Large contact database
- Good email finding accuracy for US/UK
- Built-in outreach sequences
- Affordable for small teams
- Decent company data

**Weaknesses**:
- European coverage (especially Benelux) is weaker than US
- Email accuracy for NL/BE/LU lower than for English-speaking markets
- Contact data can be outdated
- Phone numbers for European contacts are sparse
- Job title standardization is US-centric

**Best For**: Initial prospecting and email finding, supplemented by manual verification

---

### 3. ZoomInfo

**Category**: Enterprise sales intelligence

**What It Does**:
- Comprehensive company and contact database
- Intent data and buying signals
- Technographic data (what tech companies use)
- Org charts and reporting structures
- Website visitor identification

**Pricing (approximate)**:
- Starts at ~$15,000/year
- Enterprise plans: $25,000-60,000+/year
- Per-seat and credit-based components

**Strengths**:
- Deepest company data (technographics, org charts, intent)
- Best accuracy for large enterprises
- Good integration ecosystem
- Websights for website visitor identification
- Strong US and UK coverage

**Weaknesses**:
- Very expensive; not suitable for small teams or early-stage
- Benelux coverage is adequate for large enterprises but thin for mid-market
- Annual contracts with auto-renewal
- Can be overkill if only doing targeted research
- GDPR compliance has been questioned by some EU DPAs

**Best For**: Enterprise-focused teams with budget; best for Finance and Healthcare verticals where targets are large, well-known companies

---

### 4. Cognism

**Category**: EU-focused sales intelligence

**What It Does**:
- European-first contact database
- Phone-verified mobile numbers (Diamond Data)
- GDPR-compliant by design
- Intent data (via Bombora partnership)
- Chrome extension for LinkedIn

**Pricing (approximate)**:
- Custom pricing; typically $15,000-30,000+/year
- Flat-rate access (no per-credit charges for some plans)

**Strengths**:
- Best European phone number coverage
- GDPR-compliant data collection
- Phone-verified mobiles reduce bounce risk
- Good for Benelux, DACH, Nordics
- Diamond Data program provides manually verified numbers

**Weaknesses**:
- Expensive (enterprise pricing)
- Smaller total database than ZoomInfo or Apollo
- Email accuracy is good but not best-in-class
- Limited technographic data
- Company data less deep than ZoomInfo

**Best For**: When phone outreach is part of the strategy; best GDPR-first option for European prospecting

---

### 5. Instantly

**Category**: Email deliverability and cold outreach

**What It Does**:
- Email warmup (automated inbox warming)
- Email sending infrastructure
- Campaign management
- Deliverability analytics
- Lead database (Instantly B2B Lead Finder)

**Pricing (approximate)**:
- Growth: $30/mo (5,000 emails/mo)
- Hypergrowth: $77.6/mo (25,000 emails/mo)
- Light Speed: $286.3/mo (500,000 emails/mo)
- B2B Lead Finder: $47-197/mo

**Strengths**:
- Best-in-class email warmup and deliverability
- Affordable
- Simple to use
- Good for scaling cold outreach
- Email verification built in

**Weaknesses**:
- Not a data/intelligence platform (limited contact discovery)
- Lead Finder database is smaller and less accurate than dedicated platforms
- No phone numbers
- No technographic or intent data
- Email-only (no multi-channel)

**Best For**: Email outreach execution after leads are identified and enriched

---

### 6. 6sense

**Category**: ABM (Account-Based Marketing) and intent

**What It Does**:
- AI-powered account identification
- Intent data from web behavior
- Predictive analytics (which accounts are in-market)
- Advertising orchestration
- CRM integration and scoring

**Pricing (approximate)**:
- Enterprise pricing: $50,000-150,000+/year
- Typically sold as platform license

**Strengths**:
- Best intent data and predictive scoring
- Identifies anonymous website visitors at account level
- AI-driven prioritization
- Good for complex, long-cycle B2B sales
- Integrates with major CRMs and MAPs

**Weaknesses**:
- Very expensive; enterprise-only pricing
- Requires significant website traffic to generate insights
- US-centric intent data (Benelux coverage limited)
- Complex implementation
- Long time-to-value

**Best For**: Large organizations with high website traffic and complex ABM programs; not recommended for initial lead generation research

---

## Selection Matrix

| Criteria | Clay | Apollo | ZoomInfo | Cognism | Instantly | 6sense |
|----------|------|--------|----------|---------|-----------|--------|
| Benelux Coverage | Medium | Low-Med | Medium | High | Low | Low |
| Email Finding | High | High | High | Medium | Medium | Low |
| Phone Numbers | Medium | Low | Medium | High | None | Low |
| Company Data | Medium | Medium | High | Medium | Low | High |
| Intent Data | Low | Medium | High | Medium | None | High |
| GDPR Focus | Medium | Low | Low | High | Medium | Medium |
| Price (Small Team) | $$ | $ | $$$$ | $$$$ | $ | $$$$$ |
| Ease of Use | Medium | High | Medium | High | High | Low |
| Integration w/ HubSpot | High | High | High | High | Medium | High |

---

## Integration Guidance with HubSpot

### Direct Integrations
- **Apollo**: Native HubSpot integration; sync contacts and companies bidirectionally
- **Clay**: Native HubSpot integration; push enriched data to HubSpot properties
- **ZoomInfo**: Native HubSpot integration; enrich existing records or push new ones
- **Cognism**: Native HubSpot integration; sync contacts with phone numbers
- **6sense**: Native HubSpot integration; push intent scores and account data

### CSV Import (Tool-Agnostic)
When using manual research or tools without direct integration:
1. Export from xlsx using the output-schema.md column mapping
2. Split into Company and Contact CSVs
3. Import Companies first, then Contacts with company association
4. Map custom properties (Account Tier, Confidence Level, etc.)
5. Set import as "Create and update" to avoid duplicates
6. Use company domain as dedup key

### HubSpot Workflow Recommendations
- Auto-assign leads based on Account Tier
- Trigger notification when Tier 1 lead is created
- Auto-create tasks for Champion outreach on new leads
- Set lifecycle stage based on HubSpot Status (New vs. Enriched)

---

## Recommendation: Start Tool-Agnostic

### Why
1. Manual research produces higher-quality, more contextual data for Benelux
2. Public registries (KVK, DNB, CBS, etc.) are free and authoritative
3. Tool databases have weaker Benelux coverage than US/UK
4. Starting manual builds research skills that improve tool usage later
5. Avoids premature tool investment before process is validated

### When to Add Tools
- **Clay**: When enrichment volume exceeds manual capacity (>50 companies/batch)
- **Apollo**: When email finding becomes a bottleneck
- **Cognism**: When phone outreach is added to the playbook
- **ZoomInfo**: When targeting enterprise accounts and need technographic data
- **Instantly**: When cold email campaigns are ready to launch
- **6sense**: When ABM program is mature and website traffic justifies investment

### Recommended Progression
1. **Phase 1 (Now)**: Manual research + public registries + LinkedIn
2. **Phase 2**: Add Clay or Apollo for enrichment acceleration
3. **Phase 3**: Add Cognism if phone outreach is prioritized
4. **Phase 4**: Evaluate 6sense/ZoomInfo for enterprise ABM

---

## Cost Considerations

### Budget Tiers

**Minimal (<$100/mo)**:
- Manual research only
- Free Apollo tier (10K records/mo)
- LinkedIn free search
- Public registries (free)

**Growth ($200-500/mo)**:
- Clay Starter ($149/mo)
- Apollo Basic ($49/user/mo)
- Instantly Growth ($30/mo)

**Professional ($500-2,000/mo)**:
- Clay Pro ($800/mo)
- Apollo Professional ($79/user/mo)
- Instantly Hypergrowth ($77/mo)

**Enterprise ($2,000+/mo)**:
- ZoomInfo ($15K+/yr)
- Cognism ($15K+/yr)
- 6sense ($50K+/yr)

### ROI Calculation
- Average deal value for compute/infrastructure services: typically 50K-500K EUR/year
- If one Tier 1 deal closes per quarter, most tool investments pay for themselves
- Focus tool spend on enrichment accuracy rather than volume
