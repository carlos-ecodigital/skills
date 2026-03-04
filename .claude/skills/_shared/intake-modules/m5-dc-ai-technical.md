# M5: DC/AI Infrastructure Technical Specifications

**Module metadata:**
- Questions: 50 (Q7.1-7.50)
- Priority: P0 (Q7.1-7.7, Q7.32-7.41, Q7.46-7.48) · P1 (Q7.8-7.31) · P2 (Q7.42-7.50)
- Track: `[BOTH]` — PF loads full; Seed loads P0 questions only
- Feeds: `PF` `SF` `DR`
- Dependencies: M6 (site selection)
- Parallel track: C (Site/Technical)
- Mini-deliverable trigger: After M4 + M5 + M6 → **Technical Asset Summary** (per-site one-pager)

**Seed mode note:** When loaded for seed track, only ask P0 questions (~17 of 50). Seed investors need headline specs and SLA structure, not cooling loop engineering.

**Critical insight:** DC/AI infrastructure investors read technical specifications like debt covenants — every number must be defensible. A founder could complete a generic intake and still lack sufficient detail to pass independent engineer review.

---

## Power Density & Racks

### 7.1 Power Density Target
`ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

Per-rack power density:
- Target density: kW/rack (average across facility)
- GPU generation mix driving the target (e.g., H100=700W, H200=700W, B200=1000W, GB200=1200W+)
- Number of racks per site
- Total IT load per site (MW)

**Gate:** Density must be stated with GPU generation assumptions.

---

### 7.2-7.7 Power Infrastructure Details

**7.2** Maximum density accommodation for next-gen GPUs (e.g., GB200 NVL72 = 240 kW/rack): is the facility designed to support this? If not, what retrofit is needed? `ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `SF`

**7.3** Design validation: engineering calculations supporting stated density (not just manufacturer datasheets). `DOC` | `P1` | `[DOC-REQUIRED]` | `[BOTH]` | Feeds: `PF` `DR`

**7.4** Rack configuration: DGX/HGX per rack, total racks, pre-built vs. custom. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.5** PDU redundancy per rack: N+1 or 2N? Justification for chosen level. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.6** UPS autonomy at stated density: minutes of backup power. BESS integration for extended backup? `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.7** Mixed GPU type accommodation: can the facility support multiple GPU generations simultaneously? Design implications? `ANS` | `P1` | `[BINARY]` | `[BOTH]` | Feeds: `PF`

---

## Cooling Design

### 7.8-7.16 Cooling Questions

**7.8** Cooling method selected: DLC (direct liquid cooling), RDHx (rear-door heat exchanger), or immersion? Rationale for selection. `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

**7.9** If DLC: loop redundancy, heat exchanger sizing, Delta-T across facility, CDU specifications. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.10** If immersion: dielectric fluid type, flash point, fire classification, tank specifications. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.11** PUE target: design PUE with realistic benchmark. For liquid-cooled facilities: 1.02-1.15 is achievable. What is your target and basis? `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF` `NP`

**7.12** WUE target and annual water footprint (m³/year per site). `CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP`

**7.13** Water supply: source, flow rate capacity, seasonal variability, water rights/permits. `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `NP`

**7.14** Coolant inventory and supply chain risk (for liquid cooling systems). `ANS` | `P2` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

**7.15** Leak detection: auto-shutoff capability, containment volume, alarm response SLA. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.16** Waste heat transfer to district heating or adjacent users: tertiary loop required? Interface temperature? Flow rates? Integration with BESS waste heat? `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `SF`

---

## Network Connectivity

### 7.17-7.23 Network Questions

**7.17** Network topology: InfiniBand vs. Ethernet for multi-node GPU training? Spine-leaf architecture? `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

**7.18** Carrier diversity: number of independent carriers, physically diverse paths, last-mile redundancy. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.19** Internet Exchange connectivity: distance to nearest IX, expected latency, direct peering capability. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

**7.20** Peering agreements: carrier-neutral or customer-provided? CDN connectivity? `ANS` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

**7.21** BGP routing: multi-homed customer support, prefix announcement capability. `ANS` | `P2` | `[BINARY]` | `[BOTH]` | Feeds: `PF`

**7.22** Network redundancy level: N+1 minimum for Tier III equivalent. What level is designed? `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.23** Port capacity: 400G spine, 100G per GPU node, total aggregate bandwidth per site. `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

---

## GPU/Accelerator Specifications

### 7.24-7.31 GPU Questions

**7.24** Supported platforms: NVIDIA H100/H200/B200/GB200 and/or AMD MI300X? Customer choice or operator-specified? `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

**7.25** Business model: customer-supplied GPUs (bare metal colo) vs. operator-supplied (GPU-as-a-service)? `ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `SF`

**7.26** GPU refresh cycle: expected lifecycle (18-36 months), depreciation model, replacement budget. `CAL` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.27** GPU refresh reserve: 8-15% of operating cash flow annually. Is this funded in the financial model? `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

**Gate for 7.27:** GPU refresh reserve MUST be funded. If not, DSCR collapses at Year 5 when GPUs need replacement and the model breaks.

**7.28** Heterogeneous GPU support: can the facility support mixed GPU types in different zones? `ANS` | `P1` | `[BINARY]` | `[BOTH]` | Feeds: `PF`

**7.29** GPU RMA SLA: vendor enterprise support guarantee (e.g., 48-hour replacement)? Alternative support arrangement? `ANS` | `P2` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.30** TDP variability: designed for current AND future power draw per GPU generation? `ANS` | `P0` | `[BINARY]` | `[BOTH]` | Feeds: `PF`

**7.31** Asset depreciation mismatch: GPUs (5 years) vs. building (15-20 years). How is this managed in the financial model? `CAL` | `P1` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

---

## SLA Structure for Customers

### 7.32-7.41 SLA Questions

**7.32** Uptime guarantee: 99.95% (Tier III) or 99.99% (Tier IV)? SLA credits structure? `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `SF`

**7.33** Power density SLA: contractual guarantee for kW/rack delivered 24/7? Penalty for under-delivery? `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.34** Temperature SLA: guaranteed server inlet temperature (< 27°C typical). Measurement and monitoring. `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.35** Seasonal derating: does cooling capacity reduce in summer? If so, by how much? How is this contractually handled? `ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

**7.36** MTTR per severity level: Sev1 (full outage), Sev2 (partial degradation), Sev3 (monitoring alert). `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.37** Planned maintenance windows: hours per month/quarter allocated for maintenance. Customer notification process. `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.38** Force majeure / grid congestion: how is grid-caused downtime treated contractually? `ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `LC`

**7.39** Penalties and termination rights on SLA breach: financial penalties, early termination triggers, cure periods. `ANS` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `LC`

**7.40** Network latency SLA: for multi-node training jobs, what intra-facility latency is guaranteed? `ANS` | `P1` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.41** Backup power scenario: if grid is lost, can BESS island the DC? For how long? At what load? `ANS` | `P0` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF`

---

## Physical Security, Moratorium, Fire Safety

### 7.42-7.50 Remaining DC Questions

**7.42** EN 50600 security classification: which tier? Physical security features (biometric, mantrap, CCTV, retention period). `ANS` | `P2` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `DR`

**7.43** Access control and guard force: 24/7 presence? Armed/unarmed? Alarm response SLA? `ANS` | `P2` | `[EXACT]` | `[BOTH]` | Feeds: `PF`

**7.44** Data residency compliance: EU data sovereignty, IP geolocation services, customer compliance requirements. `ANS` | `P2` | `[BINARY]` | `[BOTH]` | Feeds: `PF` `LC`

**7.45** Data residency certifications planned: ISO 27001, SOC 2 Type II, other? `ANS` | `P2` | `[NARRATIVE]` | `[BOTH]` | Feeds: `PF` `DR`

**7.46** DC Moratorium — IT load: total IT load across ALL sites vs. applicable national thresholds (e.g., Netherlands: 70 MW hyperscale threshold). `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP` `LC`

**7.47** DC Moratorium — floor area: total DC floor area across ALL sites vs. applicable thresholds (e.g., Netherlands: 100,000 m²). `CAL` | `P0` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP` `LC`

**7.48** Local DC restrictions: confirm ALL sites comply with any municipal or regional DC moratoriums or restrictions in your jurisdiction. `ANS` | `P0` | `[BINARY]` | `[BOTH]` | Feeds: `NP` `LC`

**Gate for 7.46-7.48:** Moratorium compliance is a **legal blocker**, not a risk factor. Must be confirmed with counsel opinion. If total load approaches a threshold, document growth plan and legal analysis.

**7.49** Fire suppression for DC: non-damaging agents (FM-200 or Novec 1230). System specifications. `ANS` | `P2` | `[EXACT]` | `[BOTH]` | Feeds: `PF` `NP`

**7.50** VESDA early-warning detection: installed in DC? Zoning separation between DC and BESS fire zones? `ANS` | `P2` | `[BINARY]` | `[BOTH]` | Feeds: `PF` `NP`

---

## Section 7 Gate Summary

| Criterion | Required For | Status |
|-----------|-------------|--------|
| Power density target with GPU assumptions | P0 | [ ] |
| PUE target with engineering basis | P0 | [ ] |
| GPU business model defined (colo vs. GaaS) | P0 | [ ] |
| GPU refresh reserve funded in model | P0 | [ ] |
| SLA terms specific enough for lender assessment | P0 | [ ] |
| Moratorium compliance confirmed | P0 | [ ] |
| BESS islanding for DC backup assessed | P0 | [ ] |
| Cooling system designed with validation | P1 | [ ] |
| Network redundancy level specified | P1 | [ ] |
| Waste heat integration designed | P1 | [ ] |
