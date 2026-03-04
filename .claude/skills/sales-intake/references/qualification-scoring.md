# Qualification Scoring Models

ICP-specific weighted scoring for lead qualification. Each lead receives a score from 1.0 to 5.0 based on 7 factors weighted differently per ICP.

---

## Scoring Scale

Each factor is scored 1-5:
- **5** = Ideal match, no concerns
- **4** = Strong fit, minor gaps
- **3** = Acceptable, some questions to resolve
- **2** = Marginal, significant gaps or risks
- **1** = Poor fit, likely not viable

## Tier Thresholds

| Tier | Score Range | Action |
|------|-----------|--------|
| **Tier 1: Hot** | >4.0 | Pursue immediately. Full deliverables. Priority scheduling. |
| **Tier 2: Warm** | 3.0-4.0 | Pursue with caveats. Full deliverables. Standard timeline. |
| **Tier 3: Monitor** | 2.0-3.0 | Park and monitor. Abbreviated deliverables. Set review date. |
| **Disqualified** | <2.0 | Waitlist. Waitlist Entry deliverable only. Set revisit trigger. |

---

## C-NEO: Neocloud Scoring

| Factor | Weight | Score 5 | Score 3 | Score 1 |
|--------|--------|---------|---------|---------|
| **Capacity need** | 25% | >5 MW, clear specs | 1-5 MW, partially defined | <0.5 MW or vague |
| **Timeline match** | 20% | Need within 12 months, DE can deliver | 12-24 months | >24 months or "eventually" |
| **Technical fit** | 15% | High density, liquid cooling, GPU-ready | Standard density, some custom | Low density, incompatible specs |
| **Budget/price fit** | 15% | Know their cost base, DE is competitive | Price-sensitive but viable | Looking for cheapest option only |
| **Decision authority** | 10% | Talking to founder/CTO, can sign | VP-level, needs board approval | Engineer exploring, no authority |
| **Strategic driver** | 10% | EU expansion mandate, capacity-constrained | Exploring EU, optional | No real EU driver |
| **Founder assessment** | 5% | Strong gut feel | Neutral | Bad feeling |

**Calibration example:**
- Voltage Park, Series B, needs 10 MW in 6 months, talked to CTO → Capacity 5, Timeline 5, Technical 4, Budget 4, Decision 5, Strategic 4, Founder 4 → **4.55 (Tier 1)**
- Small GPU startup, 500 kW "maybe next year", engineer asked → Capacity 2, Timeline 2, Technical 3, Budget 2, Decision 1, Strategic 2, Founder 2 → **2.00 (Tier 3)**

---

## C-ENT: Enterprise Scoring

| Factor | Weight | Score 5 | Score 3 | Score 1 |
|--------|--------|---------|---------|---------|
| **Capacity need** | 15% | >2 MW defined requirement | 0.5-2 MW, exploratory | <0.5 MW or undefined |
| **Timeline match** | 15% | RFP issued, decision within 6 months | 6-18 months | >18 months or "research phase" |
| **Technical fit** | 10% | Specs match DE capabilities, no compliance gap | Minor compliance gaps | Major compliance mismatch |
| **Budget/price fit** | 15% | Approved budget, know their cloud spend | Budget in planning | No budget, no cost baseline |
| **Decision authority** | 20% | CTO/CIO engaged, procurement aligned | VP-level, procurement not involved yet | IT manager, no exec sponsor |
| **Strategic driver** | 20% | Board-level sovereignty/cloud exit mandate | Department-level initiative | Personal project, no organizational driver |
| **Founder assessment** | 5% | Strong gut feel | Neutral | Bad feeling |

**Calibration example:**
- ING Bank, CTO office, sovereignty mandate, 5 MW, RFP in Q2 → Capacity 4, Timeline 4, Technical 4, Budget 4, Decision 5, Strategic 5, Founder 4 → **4.35 (Tier 1)**
- Startup, CTO curious about on-prem AI, no budget → Capacity 2, Timeline 1, Technical 3, Budget 1, Decision 3, Strategic 1, Founder 2 → **1.65 (DQ)**

---

## C-INS: Institution Scoring

| Factor | Weight | Score 5 | Score 3 | Score 1 |
|--------|--------|---------|---------|---------|
| **Capacity need** | 15% | >1 MW, specific GPU requirements | 0.2-1 MW, general compute | <0.2 MW or undefined |
| **Timeline match** | 15% | Grant approved, need within 12 months | Grant application pending | No funding timeline |
| **Technical fit** | 10% | Specs match, data classification compatible | Minor gaps in compliance | Classified data, incompatible requirements |
| **Budget/price fit** | 20% | Grant budget sufficient, academic pricing viable | Budget tight but possible | No budget, expecting free/SURF-level pricing |
| **Decision authority** | 15% | Department head, procurement authority | Researcher, needs department approval | PhD student, no authority |
| **Strategic driver** | 20% | Institutional AI strategy, SURF capacity reached | Department initiative | Individual project |
| **Founder assessment** | 5% | Strong gut feel | Neutral | Bad feeling |

---

## S-GRW: Grower Scoring

| Factor | Weight | Score 5 | Score 3 | Score 1 |
|--------|--------|---------|---------|---------|
| **Grid connection value** | 30% | >15 MVA, uncongested zone, expansion possible | 5-15 MVA, moderate congestion | <5 MVA or heavily congested |
| **Timeline match** | 10% | WKK expiring <3 years, ready to talk | WKK 3-5 years, interested | WKK >5 years, just exploring |
| **Technical fit** | 15% | Year-round heating, >5 ha, space for DC, fiber nearby | Seasonal heating, space constraints | Small operation, no space, no fiber |
| **Budget/price fit** | 10% | Gas bill >EUR 1M/year, open to long-term | Gas bill EUR 200K-1M | Gas bill <EUR 200K or unrealistic expectations |
| **Decision authority** | 10% | Owner-operator, owns the land | Family member, leased land (landlord willing) | Employee, leased land (landlord unknown) |
| **Strategic driver** | 15% | Gas cost unbearable, actively seeking alternatives, sustainability goals | Interested in alternatives, no urgency | No pain, no driver |
| **Founder assessment** | 10% | Strong gut feel, personal connection | Neutral | Bad feeling, difficult personality |

**Calibration example:**
- 20 ha tomato grower in Westland, 20 MVA grid, WKK expiring 2027, gas bill EUR 2M, owns land → Grid 5, Timeline 5, Technical 5, Budget 5, Decision 5, Strategic 5, Founder 4 → **4.90 (Tier 1)**
- 3 ha flower grower, seasonal, 3 MVA, new WKK, leased land → Grid 1, Timeline 1, Technical 2, Budget 2, Decision 2, Strategic 2, Founder 3 → **1.75 (DQ)**

---

## S-DHN: District Heating Scoring

| Factor | Weight | Score 5 | Score 3 | Score 1 |
|--------|--------|---------|---------|---------|
| **Baseload demand** | 20% | >20 MWth baseload, growing network | 5-20 MWth, stable | <5 MWth or declining |
| **Timeline match** | 10% | Active procurement, decision within 12 months | 12-24 months, planning phase | >24 months or "someday" |
| **Technical fit** | 15% | Low-temp network (<70C), connection point <5 km from viable DC site, grid access | Mid-temp, 5-10 km, grid constraints | High-temp (>90C), >10 km, no grid |
| **Budget/price fit** | 15% | DE waste heat price competitive with current sources | Marginal, needs subsidy to work | Way above current cost base |
| **Decision authority** | 20% | Board/director engaged, procurement mandate | Middle management, exploring | Staff member, no authority |
| **Strategic driver** | 15% | Wcw compliance gap, must add sustainable heat before deadline | Wcw aware, no immediate pressure | No regulatory driver |
| **Founder assessment** | 5% | Strong gut feel | Neutral | Bad feeling |

**Calibration example:**
- Ennaturlijk Arnhem, 30 MWth baseload, expanding, Wcw pressure, board engaged, low-temp network → Baseload 5, Timeline 4, Technical 4, Budget 4, Decision 5, Strategic 5, Founder 4 → **4.50 (Tier 1)**

---

## S-IND: Industrial Heat Scoring

| Factor | Weight | Score 5 | Score 3 | Score 1 |
|--------|--------|---------|---------|---------|
| **Capacity need** | 15% | >10 MWth continuous, process temp <60C | 5-10 MWth, temp 60-120C | <5 MWth or temp >120C |
| **Timeline match** | 15% | Active, decision within 12 months | 12-24 months | >24 months |
| **Technical fit** | 20% | Continuous load, temp match, site nearby, grid access | Partial match, heat pump needed | Mismatch on temp/load/site |
| **Budget/price fit** | 15% | Current energy cost high, DE competitive | Marginal economics | Not competitive |
| **Decision authority** | 15% | Energy director/plant manager, capex authority | Sustainability team, needs management buy-in | Individual exploring |
| **Strategic driver** | 15% | 2030 decarbonization target, board mandate, ETS2 exposure | ESG goals but no hard targets | No decarbonization pressure |
| **Founder assessment** | 5% | Strong gut feel | Neutral | Bad feeling |

---

## Score Calculation

```
Overall Score = SUM(Factor_Score * Factor_Weight)

Example (C-NEO):
= (Capacity * 0.25) + (Timeline * 0.20) + (Technical * 0.15) + (Budget * 0.15)
  + (Decision * 0.10) + (Strategic * 0.10) + (Founder * 0.05)
```

## Overrides

Certain conditions override the calculated score regardless of overall weighted result:

| Condition | Override |
|-----------|----------|
| No grid connection AND no viable site nearby | Cap at 2.0 (S-GRW, S-DHN, S-IND) |
| Process temp >150C with no preheating pathway | Cap at 2.0 (S-IND) |
| Founder says "do not pursue" (score 1) | Cap at 2.5 |
| Referral from Tier 1 advisor/investor | Floor at 3.0 (minimum Tier 3) |
| Capacity need >25 MW with confirmed funding | Floor at 3.5 (minimum Tier 2) for C-NEO |
| WKK contract >7 years remaining | Cap at 2.5 (S-GRW) unless other drivers |
