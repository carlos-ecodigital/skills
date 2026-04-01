---
name: market-data
description: Canonical market data template with 7-category field schema and sector overlay hooks. Sector-agnostic — use as starting template for any fundraise.
type: reference
version: 2.0
last_updated: 2026-03-31
depends_on: [market-research-framework.md]
---

# Market Data Template v2.0

> **Sector-agnostic field schema for market research data.**
> This is a TEMPLATE — field definitions, types, freshness requirements, and benchmark ranges.
> Actual populated data lives in project-specific data stores (e.g., `Market_Research_v3/` for Digital Energy).
> Sector-specific benchmarks are provided by overlays at `_shared/overlays/{sector}-{category}.md`.

---

## How to Use This Template

1. **Copy this structure** into your project-specific market research data store
2. **Populate fields** following the methodology in `market-research-framework.md`
3. **Apply sector overlays** for sector-specific benchmark ranges and additional fields
4. **Track metadata** in the Metadata section at the bottom
5. **Run cross-reference validation** (9 tests from framework §11) after populating

---

## C1: Market Sizing & Value Chain

### Field Schema

| Field | Type | Unit | Source Req. | Freshness | Benchmark Range | Confidence | Notes |
|-------|------|------|-----------|-----------|-----------------|------------|-------|
| `c1_tam_value` | Currency | USD/EUR | Tier 1b+ | <18 months | Sector-dependent | H/M/L | Total addressable market |
| `c1_tam_source` | Citation | — | — | — | — | — | Full source citation with tier |
| `c1_tam_methodology` | Enum | top-down / bottom-up / both | — | — | "both" preferred | — | Dual methodology per framework §4.1 |
| `c1_tam_topdown_value` | Currency | USD/EUR | Tier 1b+ | <18 months | — | H/M/L | Top-down methodology result |
| `c1_tam_bottomup_value` | Currency | USD/EUR | Tier 2+ | <18 months | — | H/M/L | Bottom-up methodology result |
| `c1_tam_reconciliation_gap` | Percentage | % | — | — | <30% acceptable | — | Difference between top-down and bottom-up |
| `c1_sam_value` | Currency | USD/EUR | Tier 1b+ | <18 months | 10-40% of TAM typical | H/M/L | Serviceable addressable market |
| `c1_sam_filters` | Text | — | — | — | — | — | Explicit filters applied: geography, segment, capability |
| `c1_som_value` | Currency | USD/EUR | Tier 2+ | <18 months | 1-10% of SAM typical | H/M/L | Serviceable obtainable market |
| `c1_som_capture_rate` | Percentage | % | — | — | Seed <5%, Growth <10%, Inst <15% | — | SOM as % of SAM — cross-ref test #1 |
| `c1_som_gtm_justification` | Text | — | — | — | — | — | Required if capture rate >5% |
| `c1_market_cagr` | Percentage | % | Tier 1b+ | <18 months | Emerging 20-50%, Growth 10-20%, Mature 2-10% | H/M/L | Compound annual growth rate |
| `c1_market_cagr_period` | Text | — | — | — | — | — | Period covered (e.g., "2024-2030") |
| `c1_margin_pool_position` | Enum | high / mid / low | Tier 2+ | <18 months | — | H/M/L | Company position in value chain margin pool |
| `c1_margin_pool_analysis` | Text | — | — | — | — | — | JPM-standard value chain mapping |
| `c1_supply_constraint` | Text | — | Tier 2+ | <12 months | — | H/M/L | Primary supply-side constraint description |
| `c1_supply_constraint_value` | Currency/Number | Varies | Tier 2+ | <12 months | — | H/M/L | Quantified constraint (e.g., MW capacity, permit slots) |
| `c1_constrained_market_size` | Currency | USD/EUR | Derived | — | ≤ TAM | — | min(demand-side TAM, supply-side capacity) |
| `c1_hhi_index` | Number | 0-10000 | Tier 1a+ | <12 months | <1000 fragmented, 1000-2500 moderate, >2500 concentrated | H/M/L | Herfindahl-Hirschman Index |
| `c1_penetration_stage` | Enum | nascent / early / growth / mature / decline | Tier 2+ | <18 months | — | — | Current position on S-curve |
| `c1_growth_catalyst` | Text | — | Tier 2+ | <12 months | — | — | Key current inflection driving growth ("Why Now") |
| `c1_growth_risks` | Text | — | Tier 2+ | <18 months | — | — | Key risks to market growth thesis |
| `c1_geographic_breakdown` | Text/Table | — | Tier 1b+ | <18 months | — | H/M/L | Per-country/region TAM decomposition (Inst only) |

### Sector Overlay Hook — C1
<!-- Sector-specific skills inject data below this line -->
<!-- Format: one file per sector at _shared/overlays/{sector}-c1-sizing.md -->
<!-- Overlay must follow same field schema with sector-specific benchmarks -->

---

## C2: Competitive Landscape & Positioning

### Field Schema

| Field | Type | Unit | Source Req. | Freshness | Benchmark Range | Confidence | Notes |
|-------|------|------|-----------|-----------|-----------------|------------|-------|
| `c2_competitor_count_direct` | Number | count | Tier 2+ | <12 months | Seed 5+, Growth 10+, Inst 20+ | — | Direct competitor count |
| `c2_competitor_count_indirect` | Number | count | Tier 2+ | <12 months | — | — | Indirect competitors / substitutes |
| `c2_competitor_count_potential` | Number | count | Tier 2+ | <12 months | — | — | Potential entrants with capability/motivation |
| `c2_top_competitor_name` | Text | — | — | — | — | — | Strongest direct competitor |
| `c2_top_competitor_differentiator` | Text | — | — | — | — | — | Key differentiator vs. strongest competitor |
| `c2_market_share_leader` | Text | — | Tier 1b+ | <12 months | — | H/M/L | Name + % market share |
| `c2_market_share_company` | Percentage | % | Tier 2+ | <12 months | — | H/M/L | Company's current/projected market share |
| `c2_hhi_competitive` | Number | 0-10000 | Tier 1a+ | <12 months | Same as C1 HHI | H/M/L | Competitive HHI |
| `c2_moat_type` | Enum | network / switching / regulatory / IP / scale / brand / data / none | — | — | — | — | Primary moat classification per framework §5.3 |
| `c2_moat_quantification` | Text | bps / $/unit / months / % | Tier 2+ | <12 months | — | H/M/L | GIP standard: quantified advantage |
| `c2_positioning_axis_1` | Text | — | — | — | — | — | First axis of 2x2 positioning matrix |
| `c2_positioning_axis_2` | Text | — | — | — | — | — | Second axis of 2x2 positioning matrix |
| `c2_positioning_quadrant` | Text | — | — | — | — | — | Company's position on 2x2 |
| `c2_barrier_to_entry` | Text | — | Tier 2+ | <12 months | — | H/M/L | Primary barrier description + quantification |
| `c2_failed_competitors` | Text | — | Tier 2+ | <18 months | — | — | 2-3 failed competitors with failure analysis |
| `c2_porters_summary` | Text | — | Tier 2+ | <12 months | — | H/M/L | Porter's Five Forces summary (Inst only) |
| `c2_op_benchmark_cost` | Currency | $/unit | Tier 2+ | <12 months | — | H/M/L | Company cost/unit vs. best-in-class |
| `c2_op_benchmark_utilization` | Percentage | % | Tier 2+ | <12 months | — | H/M/L | Utilization rate vs. peer average |

### Sector Overlay Hook — C2
<!-- Sector-specific overlays at _shared/overlays/{sector}-c2-competitive.md -->

---

## C3: Pricing, Demand & Revenue Durability

### Field Schema

| Field | Type | Unit | Source Req. | Freshness | Benchmark Range | Confidence | Notes |
|-------|------|------|-----------|-----------|-----------------|------------|-------|
| `c3_pricing_model` | Enum | subscription / usage / per-unit / hybrid / auction / PPA / tariff | — | — | — | — | Primary pricing model |
| `c3_current_price` | Currency | $/unit or $/period | Tier 2+ | <12 months | Sector-dependent | H/M/L | Current price point |
| `c3_pricing_methodology` | Enum | cost-plus / value-based / competitive / WTP / auction | — | — | — | — | How price was determined |
| `c3_evidence_type` | Enum | binding / LOI / pilot / interview / survey / report | — | — | — | — | Strongest demand evidence available |
| `c3_evidence_ladder_position` | Number | 1-6 | — | — | 1=strongest, 6=weakest | — | Position on evidence ladder per framework §6.1 |
| `c3_evidence_detail` | Text | — | — | — | — | — | Description of demand evidence |
| `c3_cac` | Currency | $/customer | Tier 2+ | <12 months | Sector-dependent | H/M/L | Customer acquisition cost |
| `c3_ltv` | Currency | $/customer | Tier 2+ | <12 months | Sector-dependent | H/M/L | Customer lifetime value |
| `c3_ltv_cac_ratio` | Number | ratio | — | — | >3x healthy, <3x flag | — | LTV:CAC ratio |
| `c3_contracted_pct` | Percentage | % | Tier 2+ | <12 months | — | H/M/L | % of revenue under binding contract |
| `c3_merchant_pct` | Percentage | % | — | — | — | — | % of revenue at market/spot prices |
| `c3_quasi_contracted_pct` | Percentage | % | — | — | — | — | % under LOI/framework/tariff (not binding) |
| `c3_customer_concentration_top1` | Percentage | % | — | — | <30% healthy | — | Top customer as % of revenue |
| `c3_customer_concentration_top5` | Percentage | % | — | — | <60% healthy | — | Top 5 customers as % of revenue |
| `c3_customer_hhi` | Number | 0-10000 | — | — | <2500 | — | Customer base concentration |
| `c3_churn_rate` | Percentage | %/yr | Tier 2+ | <12 months | Sector-dependent | H/M/L | Annual customer churn |
| `c3_contract_duration_avg` | Number | months | — | — | Sector-dependent | — | Average contract length |
| `c3_renewal_rate` | Percentage | % | Tier 2+ | <12 months | >80% healthy | H/M/L | Contract renewal rate |
| `c3_revenue_stream_count` | Number | count | — | — | — | — | Number of distinct revenue streams |
| `c3_revenue_stream_list` | Text | — | — | — | — | — | Comma-separated stream names + % of total |
| `c3_revenue_correlation` | Enum | diversifying / neutral / correlated | — | — | "diversifying" preferred | — | Correlation between revenue streams |
| `c3_gross_revenue` | Currency | $/yr | — | — | — | H/M/L | Gross revenue potential (100%) |
| `c3_degradation_haircut` | Percentage | % | Tier 2+ | <12 months | Sector-dependent | H/M/L | Technology degradation haircut |
| `c3_downtime_haircut` | Percentage | % | Tier 2+ | <12 months | Sector-dependent | H/M/L | Availability / downtime haircut |
| `c3_curtailment_haircut` | Percentage | % | Tier 2+ | <12 months | Sector-dependent | H/M/L | Curtailment / congestion haircut |
| `c3_price_risk_haircut` | Percentage | % | — | — | Sector-dependent | H/M/L | Price risk: contracted vs merchant |
| `c3_credit_risk_haircut` | Percentage | % | — | — | Sector-dependent | H/M/L | Counterparty credit risk haircut |
| `c3_net_revenue` | Currency | $/yr | — | — | — | H/M/L | Net realizable revenue (after all haircuts) |
| `c3_gross_to_net_pct` | Percentage | % | — | — | >60% typical, <60% flag | — | Net as % of gross (revenue waterfall output) |
| `c3_demand_pipeline_value` | Currency | $ | — | — | — | H/M/L | Value of identified demand pipeline |
| `c3_waitlist_count` | Number | count | — | — | — | — | Customers/projects on waitlist |

### Sector Overlay Hook — C3
<!-- Sector-specific overlays at _shared/overlays/{sector}-c3-pricing.md -->

---

## C4: Comparable Transactions & Valuations

### Field Schema

| Field | Type | Unit | Source Req. | Freshness | Benchmark Range | Confidence | Notes |
|-------|------|------|-----------|-----------|-----------------|------------|-------|
| `c4_trading_comp_count` | Number | count | Tier 1b+ | <6 months | Seed 0+, Growth 3+, Inst 5+ | — | Public company trading comps |
| `c4_ma_comp_count` | Number | count | Tier 1b+ | <6 months | Seed 3+, Growth 5+, Inst 8+ | — | Precedent M&A transaction comps |
| `c4_asset_comp_count` | Number | count | Tier 1b+ | <6 months | Growth 3+, Inst 5+ | — | Asset-level transaction comps |
| `c4_funding_comp_count` | Number | count | Tier 2+ | <6 months | Seed 5+, Growth 5+, Inst 5+ | — | Private funding round comps |
| `c4_total_comp_count` | Number | count | — | — | Seed 5+, Growth 10+, Inst 15+ | — | Sum of all comp types |
| `c4_negative_precedent_count` | Number | count | Tier 2+ | <18 months | Min 2 | — | Failed/distressed/down-round comps |
| `c4_primary_multiple` | Text | — | — | — | — | — | Most relevant valuation multiple name |
| `c4_primary_multiple_range` | Text | range | Tier 1b+ | <6 months | Sector-dependent | H/M/L | Range of primary multiple across comps |
| `c4_comp_ev_ebitda_range` | Text | range | Tier 1b+ | <6 months | Sector-dependent | H/M/L | EV/EBITDA range from comps |
| `c4_comp_ev_revenue_range` | Text | range | Tier 1b+ | <6 months | Sector-dependent | H/M/L | EV/Revenue range from comps |
| `c4_comp_ev_unit_range` | Text | range | Tier 1b+ | <6 months | Sector-dependent | H/M/L | EV per physical unit (EV/MW, EV/kWh, $/sq ft) |
| `c4_implied_valuation_low` | Currency | USD/EUR | — | — | — | — | Bottom of implied valuation range |
| `c4_implied_valuation_high` | Currency | USD/EUR | — | — | — | — | Top of implied valuation range |
| `c4_implied_valuation_midpoint` | Currency | USD/EUR | — | — | — | — | Midpoint of implied range |
| `c4_development_discount` | Percentage | % | Tier 1b+ | <12 months | Dev 20-40%, Construction 10-20% | H/M/L | Macquarie standard discount |
| `c4_control_premium` | Percentage | % | Tier 1b+ | <12 months | 20-40% typical | H/M/L | Control premium in M&A comps |
| `c4_yield_comp_coe` | Percentage | % | Tier 1b+ | <6 months | Sector-dependent | H/M/L | Cost of equity from yield comps |
| `c4_yield_comp_irr` | Percentage | % | Tier 1b+ | <6 months | Sector-dependent | H/M/L | Project IRR from yield comps |
| `c4_yield_comp_dividend` | Percentage | % | Tier 1b+ | <6 months | Sector-dependent | H/M/L | Dividend yield from public comps |
| `c4_football_field_range` | Text | — | — | — | — | — | Summary: low-high across all methodologies |
| `c4_multiple_trend` | Enum | expanding / stable / compressing | Tier 1b+ | <6 months | — | H/M/L | 2-3 year trend direction |
| `c4_data_sources` | Text | — | — | — | — | — | Capital IQ, PitchBook, press, etc. |

### Sector Overlay Hook — C4
<!-- Sector-specific overlays at _shared/overlays/{sector}-c4-comps.md -->

---

## C5: FM Assumptions & Value Creation

### Field Schema

| Field | Type | Unit | Source Req. | Freshness | Benchmark Range | Confidence | Notes |
|-------|------|------|-----------|-----------|-----------------|------------|-------|
| `c5_revenue_growth_yr1` | Percentage | % | Tier 2+ | <12 months | Sector-dependent | H/M/L | Year 1 revenue growth rate |
| `c5_revenue_growth_yr5` | Percentage | % | Tier 2+ | <12 months | — | H/M/L | Year 5 revenue growth rate |
| `c5_revenue_growth_source` | Text | — | — | — | — | — | Source/justification for growth rate |
| `c5_gross_margin` | Percentage | % | Tier 2+ | <12 months | Sector-dependent | H/M/L | Projected gross margin |
| `c5_gross_margin_driver` | Text | — | — | — | — | — | What drives margin expansion/contraction |
| `c5_capex_total` | Currency | USD/EUR | Tier 2+ | <12 months | — | H/M/L | Total CAPEX |
| `c5_capex_per_unit` | Currency | $/unit | Tier 2+ | <12 months | Sector-dependent | H/M/L | CAPEX per unit ($/MW, $/kWh, $/sq ft) |
| `c5_capex_source` | Text | — | — | — | — | — | Source for unit cost basis |
| `c5_opex_annual` | Currency | $/yr | Tier 2+ | <12 months | — | H/M/L | Annual OPEX |
| `c5_opex_breakdown` | Text | — | — | — | — | — | Team, infrastructure, SGA, maintenance |
| `c5_discount_rate` | Percentage | % | Tier 1b+ | <6 months | Sector-dependent | H/M/L | Discount rate used |
| `c5_wacc` | Percentage | % | Tier 1b+ | <6 months | Sector-dependent | H/M/L | Weighted average cost of capital |
| `c5_wacc_derivation` | Text | — | — | — | — | — | Component build-up: cost of equity + cost of debt + weights |
| `c5_terminal_methodology` | Enum | exit-multiple / perpetuity-growth / NAV | — | — | — | — | Terminal value method |
| `c5_terminal_value` | Currency | USD/EUR | — | — | <50% of total NPV | H/M/L | Terminal value |
| `c5_terminal_pct_npv` | Percentage | % | — | — | <50% healthy | — | Terminal value as % of total NPV |
| `c5_base_case_irr` | Percentage | % | — | — | Sector-dependent | H/M/L | Base case IRR |
| `c5_bull_case_irr` | Percentage | % | — | — | — | H/M/L | Bull case IRR |
| `c5_bear_case_irr` | Percentage | % | — | — | — | H/M/L | Bear case IRR |
| `c5_top3_sensitivities` | Text | — | — | — | — | — | Top 3 assumptions that most affect output |
| `c5_value_creation_dev_margin` | Percentage | % of return | — | — | — | — | KKR bridge: development margin contribution |
| `c5_value_creation_opex` | Percentage | % of return | — | — | — | — | KKR bridge: operational improvement contribution |
| `c5_value_creation_fin_eng` | Percentage | % of return | — | — | — | — | KKR bridge: financial engineering contribution |
| `c5_value_creation_multiple` | Percentage | % of return | — | — | — | — | KKR bridge: multiple expansion contribution |
| `c5_value_creation_exit` | Percentage | % of return | — | — | — | — | KKR bridge: exit premium contribution |
| `c5_lender_case_irr` | Percentage | % | — | — | — | H/M/L | Lender/downside case IRR (Inst only) |
| `c5_dscr_base` | Number | ratio | — | — | >1.20x healthy | H/M/L | Base case DSCR |
| `c5_dscr_break_scenario` | Text | — | — | — | — | — | Assumptions at which DSCR breaks covenant |
| `c5_fm_revenue_vs_c1xc3` | Percentage | % | — | — | Within 20% | — | Cross-ref test #2: FM revenue vs SOM×ASP |
| `c5_fm_growth_vs_c1_cagr` | Enum | below / at / above | — | — | "at" or "below" | — | Cross-ref test #4 |
| `c5_fm_capex_vs_c4` | Percentage | % | — | — | Within 25% | — | Cross-ref test #6: FM CAPEX vs comp CAPEX |
| `c5_third_party_review` | Enum | none / advisor / audit / independent | — | — | Seed: none ok; Growth: advisor; Inst: audit | — | Model review status |
| `c5_inflation_assumption` | Percentage | % | Tier 1a+ | <6 months | ECB target 2%, actual varies | H/M/L | Inflation/escalation rate |
| `c5_refinancing_assumption` | Text | — | — | — | — | — | Refinancing terms at debt maturity (Inst only) |

### Sector Overlay Hook — C5
<!-- Sector-specific overlays at _shared/overlays/{sector}-c5-fm.md -->

---

## C6: Regulatory & Policy Risk

### Field Schema

| Field | Type | Unit | Source Req. | Freshness | Benchmark Range | Confidence | Notes |
|-------|------|------|-----------|-----------|-----------------|------------|-------|
| `c6_regulation_count` | Number | count | Tier 1a+ | Current | — | — | Number of applicable regulations |
| `c6_regulation_list` | Text | — | Tier 1a+ | Current | — | — | Names of key regulations with jurisdictions |
| `c6_key_tailwind` | Text | — | Tier 1a+ | Current | — | H/M/L | Primary regulatory tailwind |
| `c6_key_headwind` | Text | — | Tier 1a+ | Current | — | H/M/L | Primary regulatory headwind/risk |
| `c6_subsidy_dependency` | Boolean | yes/no | — | — | — | — | Does business model depend on subsidy? |
| `c6_subsidy_name` | Text | — | Tier 1a+ | Current | — | — | Name of subsidy program |
| `c6_subsidy_value` | Currency | $/unit | Tier 1a+ | Current | — | H/M/L | Subsidy amount per unit |
| `c6_subsidy_sunset_date` | Date | YYYY-MM-DD | Tier 1a+ | Current | — | — | When subsidy expires/reviews |
| `c6_subsidy_revenue_pct` | Percentage | % | — | — | <30% low dependency | — | Revenue dependent on subsidy |
| `c6_approval_pathway` | Text | — | Tier 1a+ | Current | — | — | Required approvals in order |
| `c6_approval_timeline_months` | Number | months | Tier 2+ | <12 months | Sector-dependent | H/M/L | Expected time from application to approval |
| `c6_approval_probability` | Percentage | % | Tier 2+ | <12 months | — | H/M/L | Estimated probability of approval |
| `c6_regulatory_moat` | Enum | strong / moderate / weak / none / negative | — | — | — | H/M/L | Net regulatory moat assessment |
| `c6_compliance_cost_annual` | Currency | $/yr | Tier 2+ | <12 months | — | H/M/L | Annual ongoing compliance cost |
| `c6_pending_changes_3yr` | Text | — | Tier 1a+ | Current | — | H/M/L | Regulatory changes expected in next 3 years |
| `c6_legal_review_status` | Enum | none / internal / external / opinion-obtained | — | — | Inst: opinion-obtained | — | Legal counsel review status |
| `c6_base_scenario_impact` | Text | — | — | — | — | — | Revenue/cost impact if regulation unchanged |
| `c6_upside_scenario_impact` | Text | — | — | — | — | — | Impact if regulation becomes more favorable |
| `c6_downside_scenario_impact` | Text | — | — | — | — | — | Impact if regulation becomes adverse |

### Sector Overlay Hook — C6
<!-- Sector-specific overlays at _shared/overlays/{sector}-c6-regulatory.md -->

---

## C7: Downside, Distress & Asset Recovery

### Field Schema

| Field | Type | Unit | Source Req. | Freshness | Benchmark Range | Confidence | Notes |
|-------|------|------|-----------|-----------|-----------------|------------|-------|
| `c7_liquidation_value` | Currency | USD/EUR | Tier 2+ | <12 months | — | H/M/L | Total liquidation value (orderly) |
| `c7_liquidation_forced_sale` | Currency | USD/EUR | Tier 2+ | <12 months | — | H/M/L | Forced/fire sale value |
| `c7_liquidation_pct_investment` | Percentage | % | — | — | >60% for senior debt comfort | — | Liquidation as % of total investment |
| `c7_replacement_cost` | Currency | USD/EUR | Tier 2+ | <12 months | — | H/M/L | Cost to replicate asset base from scratch |
| `c7_replacement_vs_valuation` | Enum | premium / at-par / discount | — | — | — | — | Current valuation vs replacement cost |
| `c7_distress_discount` | Percentage | % | Tier 1b+ | <18 months | 30-60% typical fire sale | H/M/L | Typical distress discount from going-concern |
| `c7_distress_comp_count` | Number | count | Tier 2+ | <18 months | 3-5 for institutional | — | Distress comp transactions identified |
| `c7_technology_trl` | Number | 1-9 | Tier 2+ | <12 months | >7 commercial, <7 pre-commercial | — | Technology Readiness Level |
| `c7_remaining_useful_life` | Number | years | Tier 2+ | <12 months | Must exceed financing tenor | H/M/L | Remaining productive life |
| `c7_obsolescence_risk` | Enum | low / medium / high | Tier 2+ | <12 months | — | H/M/L | Risk of technology becoming obsolete |
| `c7_obsolescence_horizon` | Number | years | Tier 2+ | <12 months | — | H/M/L | Years until potential obsolescence |
| `c7_repurpose_optionality` | Text | — | — | — | — | — | Can asset be repurposed if primary use becomes obsolete? |
| `c7_recovery_senior` | Percentage | % | — | — | ≥60% lender comfort per cross-ref #9 | — | Recovery rate for senior secured |
| `c7_recovery_mezz` | Percentage | % | — | — | — | — | Recovery rate for mezzanine |
| `c7_recovery_equity` | Percentage | % | — | — | — | — | Recovery rate for equity |
| `c7_tail_risk_count` | Number | count | — | — | — | — | Number of identified tail risks |
| `c7_tail_risk_inventory` | Text | — | Tier 2+ | <12 months | — | — | List of tail risks with probability and impact |
| `c7_insurance_coverage` | Text | — | Tier 2+ | <12 months | — | — | Insurance coverage for key operational risks |
| `c7_biggest_single_risk` | Text | — | — | — | — | H/M/L | Single biggest risk to investment |
| `c7_bear_case_narrative` | Text | — | — | — | — | — | What happens in the bear case? |

### Sector Overlay Hook — C7
<!-- Sector-specific overlays at _shared/overlays/{sector}-c7-downside.md -->

---

## Cross-Reference Validation Fields

These fields track the 9 cross-reference tests from `market-research-framework.md` §11:

| Field | Test | Value | Status |
|-------|------|-------|--------|
| `xref_1_som_capture` | C1 SOM capture rate | — | PASS / FAIL / NOT_RUN |
| `xref_2_revenue_match` | C1 SOM × C3 ASP vs C5 Revenue | — | PASS / FAIL / NOT_RUN |
| `xref_3_valuation_match` | C4 comps vs C5 FM valuation | — | PASS / FAIL / NOT_RUN |
| `xref_4_growth_match` | C5 growth vs C1 CAGR | — | PASS / FAIL / NOT_RUN |
| `xref_5_pricing_match` | C3 pricing vs C2 comp pricing | — | PASS / FAIL / NOT_RUN |
| `xref_6_capex_match` | C5 CAPEX vs C4 asset comps | — | PASS / FAIL / NOT_RUN |
| `xref_7_waterfall_match` | C3 waterfall → C5 net revenue | — | PASS / FAIL / NOT_RUN |
| `xref_8_timeline_match` | C6 timeline → C5 revenue start | — | PASS / FAIL / NOT_RUN |
| `xref_9_distress_match` | C7 distress → C5 debt sizing | — | PASS / FAIL / NOT_RUN |
| `xref_pass_count` | Total passing | — | X/9 |
| `xref_required_pass` | Track minimum | — | Seed 5, Growth 7, Inst 9 |

---

## Metadata

Track research completeness and freshness:

```
## Research Metadata
- last_updated: YYYY-MM-DD
- track: [Seed / Growth-Infra / Institutional]
- total_fields: [count of all fields across C1-C7]
- populated_fields: [count] ([X]%)
- tier_distribution:
    tier_0: [count]
    tier_1a: [count]
    tier_1b: [count]
    tier_2: [count]
    tier_3: [count]
- stale_fields: [list with field name and staleness duration]
- known_gaps: [list of empty required fields]
- active_overlays: [list of sector overlay files loaded]
- last_research_run: YYYY-MM-DD (research-engine)
- last_competitive_update: YYYY-MM-DD (competitive-intel)
- cross_ref_status: [X/9 passing]
- quality_gate_status: [X/11 gates met]
```

---

## Sector Overlay Specification

Any sector-specific skill can create overlays at `_shared/overlays/{sector}-{category}.md`.

### Overlay Requirements

Each overlay file must:

1. **Follow parent field schema**: Use the same field names, types, and units as defined above
2. **Override benchmark ranges**: Replace "sector-dependent" with specific ranges (e.g., BESS: CAPEX EUR 330-700K/MW)
3. **Add sector-specific fields**: Additional fields marked `[SECTOR-SPECIFIC]` at the end of the category section
4. **Add sector-specific sources**: Named Tier 1 sources for the sector (e.g., for energy: BNEF, IEA/IRENA, TenneT)
5. **Add sector-specific red flags**: Detection criteria unique to the sector
6. **Add sector-specific comp types**: Relevant multiples and asset metrics (e.g., for infra: EV/MW, EV/kWh)
7. **Include overlay frontmatter**: See format below

### Overlay Frontmatter

```yaml
---
sector: [sector-name]
category: [C1-C7]
last_updated: YYYY-MM-DD
maintainer_skill: [skill-name that maintains this overlay]
version: 1.0
parent_schema_version: 2.0
---
```

### Overlay File Naming Convention

`_shared/overlays/{sector}-{category}.md`

Examples:
- `energy-c1-sizing.md` — Energy sector market sizing benchmarks
- `dc-ai-c4-comps.md` — Data center / AI sector comparable transactions
- `bess-c3-pricing.md` — Battery storage pricing and revenue stacking
- `fintech-c2-competitive.md` — Fintech competitive landscape benchmarks

---

*Template version 2.0 — Last updated 2026-03-31*
*Field schema aligned with market-research-framework.md v2.0*
