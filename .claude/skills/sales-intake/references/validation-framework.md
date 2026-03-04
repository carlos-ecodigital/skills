# Validation Framework

Five automated checks run post-intake before generating deliverables. Each check produces pass/warn/fail per item.

---

## Check 1: Internal Consistency

Cross-reference answers for contradictions. Flag any mismatches.

### Colocation Track Consistency Checks

| Check | Logic | Flag If |
|-------|-------|---------|
| Capacity vs funding | Large capacity (>10 MW) requires significant capital | Unfunded startup asking for >10 MW |
| Timeline vs procurement | Enterprise RFP processes take 6-12 months minimum | Enterprise claims decision in <3 months with no prior contact |
| Power density vs workload | Training = high density; inference can be lower | Claims low-density need but describes GPU training workloads |
| Scale vs contract term | Large deployments justify long terms | Wants >5 MW but only 1-year commitment |
| Location vs latency | Inference serving EU users needs EU proximity | Claims latency matters but has no EU end users |
| Sovereignty vs cloud | Can't claim sovereignty need while staying on hyperscaler | Says sovereignty is critical but plans to keep 90% on AWS |

### Site Track Consistency Checks

| Check | Logic | Flag If |
|-------|-------|---------|
| Heat demand vs grid | Heat output is proportional to IT load (roughly 1 MWth per 1 MW IT) | Claims massive heat demand but tiny grid connection |
| Gas cost vs hectares | Larger greenhouses have higher gas bills | Claims 2 ha but EUR 3M gas bill (implausible) |
| WKK age vs timeline | New WKK means 10+ year delay | Says urgent need but WKK installed last year |
| Land ownership vs authority | Leased land requires landlord consent | Claims full authority but land is leased, landlord not contacted |
| Network temp vs DC heat | DC waste heat is 30-50C base | Network runs at >90C, no heat pump discussion |
| Baseload vs network size | Small networks have small baseload | Claims 50 MWth baseload for 2,000 household network |
| Process temp vs "full replacement" | >120C process cannot be fully supplied by DC waste heat | Claims DC can replace all gas for 180C process |

---

## Check 2: Benchmark Comparison

Compare stated values against DE's operational ranges. Flag outliers.

### Colocation Track Benchmarks

| Metric | DE Range | Flag If Below | Flag If Above |
|--------|----------|---------------|---------------|
| Capacity need (C-NEO) | 1-50 MW | <0.5 MW (too small) | >50 MW (beyond current scope) |
| Capacity need (C-ENT) | 0.5-10 MW | <0.2 MW | >15 MW (unusual for enterprise) |
| Capacity need (C-INS) | 0.2-5 MW | <0.1 MW | >10 MW (unusual for institution) |
| Power density | 10-80 kW/rack | <5 kW/rack (not AI workload) | >100 kW/rack (beyond current design) |
| Price per kW/month | EUR 100-250 | <EUR 80 (unsustainable) | -- |
| Contract term | 3-15 years | <1 year | >20 years (unusual for colo) |
| PUE expectation | 1.1-1.4 | -- | >1.5 (DE can do better) |
| Deployment timeline | 6-24 months | -- | -- |

### Site Track Benchmarks

| Metric | DE Range | Flag If Below | Flag If Above |
|--------|----------|---------------|---------------|
| Grower gas bill | EUR 500K-5M/year | <EUR 200K (too small) | >EUR 10M (very large, verify) |
| Grower land area | 5-50 hectares | <3 ha (too small) | >100 ha (very large, verify) |
| Grid connection (S-GRW) | 5-25 MVA | <3 MVA (insufficient) | >50 MVA (unusual, verify) |
| Ground rent | EUR 5-15/m2/year | <EUR 3 (unrealistic) | >EUR 25 (too expensive) |
| DH baseload demand | 5-100 MWth | <3 MWth (too small) | >200 MWth (very large) |
| DH supply temperature | 30-70C (direct), 70-90C (with heat pump) | -- | >90C (expensive heat pump) |
| DH heat price | EUR 10-25/MWh | <EUR 5 (unsustainable) | >EUR 35 (uncompetitive) |
| Industrial process temp | 30-120C (viable range) | -- | >150C (largely out of scope) |
| Contract term (Site Track) | 15-30 years | <10 years (project finance issue) | -- |
| Heat pipe distance | <5 km (ideal), 5-10 km (marginal) | -- | >10 km (likely uneconomic) |

---

## Check 3: Red Flag Scan

9 specific conditions that threaten deal viability. Each red flag has severity (High/Medium/Low) and recommended action.

| # | Red Flag | Applies To | Severity | Trigger | Recommended Action |
|---|----------|-----------|----------|---------|-------------------|
| 1 | **Scale mismatch** | All | High | Need <50% of DE minimum or >200% of DE maximum for ICP | Disqualify or park |
| 2 | **Timeline gap** | All | High | Need >3 years out with no interim commitment | Park with revisit trigger |
| 3 | **No grid access** | S-GRW, S-DHN, S-IND | High | No existing grid connection AND heavily congested zone | Disqualify unless grid solution identified |
| 4 | **No viable land** | S-GRW, S-IND | High | No available land for DC within 5 km of heat demand | Disqualify |
| 5 | **Price gap** | All | Medium | Expectation >30% below DE pricing range | Flag in Opportunity Brief, discuss pricing flexibility |
| 6 | **Decision drag** | C-ENT, C-INS, S-DHN | Medium | No decision authority engaged after initial contact; committee-only decision with no champion | Requires stakeholder mapping and champion identification |
| 7 | **Competitor lock** | All | Medium | Existing contract with competitor that doesn't expire for >2 years | Park with contract-expiry revisit trigger |
| 8 | **Temperature mismatch** | S-IND | Medium | Process temp >120C with no preheating pathway identified | Scope partial supply; may reduce value proposition significantly |
| 9 | **Zoning block** | S-GRW, S-IND | Medium | Current zoning explicitly prohibits data centers AND no restwarmteplicht pathway | Route to `netherlands-permitting` for assessment before proceeding |

---

## Check 4: Completeness Assessment

Score each deliverable on % of primary source questions answered. Questions marked `[CAPTURED FROM: ...]` count as answered.

| Deliverable | Minimum for Generation | Primary Source Questions |
|-------------|----------------------|------------------------|
| Lead Qualification Score | 60% | All 7 scoring factors must have at least estimated scores |
| Opportunity Brief | 70% | All 10 sections need at least partial content |
| Pre-Meeting Prep | 50% | Can generate with company identity + ICP type + research |
| HubSpot Contact/Deal | 40% | Need: name, company, email/phone, ICP type, pipeline, stage |
| Recommended Next Actions | 60% | Need: ICP type, score, key gaps identified |
| Waitlist Entry | 30% | Need: name, company, ICP type, disqualification reason |

### Completeness Scoring

```
Completeness = (Questions answered or captured) / (Total questions for this ICP)

High: >80% -- all deliverables producible at full quality
Medium: 60-80% -- most deliverables producible, some gaps flagged
Low: 40-60% -- abbreviated deliverables, flag gaps prominently
Critical: <40% -- only Lead Qualification Score and HubSpot entry producible
```

---

## Check 5: Output Recommendation

Based on completeness, meeting status, and urgency, recommend which deliverables to produce first.

### Decision Matrix

| Scenario | Priority Deliverables | Secondary | Skip |
|----------|----------------------|-----------|------|
| Mode A, Tier 1, high completeness | All 5 (Score, Brief, HubSpot, Actions, Pre-Meeting if needed) | -- | Waitlist |
| Mode A, Tier 2-3, high completeness | Score, Brief, HubSpot, Actions | Pre-Meeting (only if meeting scheduled) | Waitlist |
| Mode A, DQ | Score, Waitlist, HubSpot (cold) | -- | Brief, Pre-Meeting, Actions |
| Mode B, meeting imminent | Pre-Meeting Prep (priority), abbreviated Score | Brief (abbreviated) | Full Score, Waitlist |
| Mode C, portal submission | Score, HubSpot, Actions | Brief (if sufficient data) | Pre-Meeting, Waitlist |
| Low completeness (<60%) | Score (estimated), HubSpot (partial), gap list to founder | -- | Brief, Pre-Meeting |

### Gap Reporting

When completeness is <80%, append a gap report to the deliverable output:

```markdown
## Information Gaps

| Gap | Impact | How to Resolve |
|-----|--------|----------------|
| [Missing information] | [Which deliverable section affected] | [Research task / founder question / meeting agenda item] |
```
