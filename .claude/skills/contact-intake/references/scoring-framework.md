# Scoring Framework

> Complete scoring rubric for W4. Source-agnostic base scoring + context modifiers + tier thresholds.
> Produces: tier, score (0.0-5.0), urgency (1-5), relevance (1-5).

## Base Scoring (5 Dimensions)

All sources are scored on the same 5 dimensions. Each dimension is rated 1-5, then weighted.

### 1. Conversation Quality (30%)

| Score | Label | Descriptors |
|-------|-------|-------------|
| 5 | Exceptional | 15+ min deep dive on a specific use case. Named pain points. Asked for pricing/timeline. Discussed internal decision process. |
| 4 | Deep | 10+ min substantive discussion. Explored DE's offering in detail. Asked technical questions. |
| 3 | Substantive | 5-10 min genuine exchange. Understood what DE does. Showed curiosity. |
| 2 | Brief | 2-5 min polite conversation. Surface-level interest. Generic questions. |
| 1 | Card-swap / None | Exchanged cards only. No real conversation. Or no interaction at all (attendee list only). |

### 2. ICP Fit (25%)

| Score | Label | Descriptors |
|-------|-------|-------------|
| 5 | Bullseye | Matches a primary ICP track (C-NEO, C-ENT, C-INS) AND has budget authority or is a known buyer. |
| 4 | Strong fit | Matches a primary ICP track. Right industry, right role, plausible buyer. |
| 3 | Adjacent | Matches a strategic track (S-GRW, S-DHN, S-IND) or is in a related industry. |
| 2 | Tangential | Energy sector but not a clear buyer. Or right role but wrong industry. |
| 1 | No fit | Completely outside DE's target market. Press, academic, competitor, personal. |

### 3. Urgency Signals (20%)

| Score | Label | Descriptors |
|-------|-------|-------------|
| 5 | Immediate | Active RFP/tender. "We need this by Q2." Existing budget allocated. Decision in weeks. |
| 4 | Near-term | Planning phase. "We're evaluating vendors." Timeline within 6 months. |
| 3 | Medium-term | Expressed future need. "Interesting for next year." No active process. |
| 2 | Exploratory | General curiosity. "We should stay in touch." No timeline. |
| 1 | None | No urgency signal detected. Information-gathering only. |

### 4. Strategic Value (15%)

| Score | Label | Descriptors |
|-------|-------|-------------|
| 5 | Transformative | C-suite at a marquee account. Could unlock an entire market segment. Board-level connector. |
| 4 | High access | VP+ at a target account. Connected to multiple decision-makers. Industry thought leader. |
| 3 | Useful network | Director-level. Some useful connections. Could facilitate intros. |
| 2 | Limited network | Manager-level. Limited strategic reach beyond own team. |
| 1 | Individual | No strategic network value. Junior, narrow role. |

### 5. Commitment Density (10%)

| Score | Label | Descriptors |
|-------|-------|-------------|
| 5 | Mutual locked | Both sides made specific promises with dates. Follow-up meeting scheduled. |
| 4 | We committed | We made specific promises (send deck, schedule call, make intro). |
| 3 | They committed | They offered to make intros, share info, or take a next step. |
| 2 | Soft intent | "Let's keep in touch" or "Send me your info." No specifics. |
| 1 | None | No commitments from either side. |

### Base Score Calculation

```
base_score = (conversation_quality * 0.30)
           + (icp_fit * 0.25)
           + (urgency_signals * 0.20)
           + (strategic_value * 0.15)
           + (commitment_density * 0.10)
```

---

## Base Score Overrides (All Sources)

Applied after base score calculation. Cumulative.

| Override | Modifier | Condition |
|----------|----------|-----------|
| Introduction chain | +0.5 | Introduced by a current Tier A contact. |
| Promise floor | min Tier B | We made a specific, named promise to this person. Score cannot drop below 2.5. |
| Repeat encounter | +0.5 | We have met this person before (prior HubSpot record or Fireflies transcript). |
| Multi-threaded company | +0.5 | 2+ contacts from the same organization in this batch. |

**Cap:** Final score after overrides is capped at 5.0.

---

## Context Modifiers (Source-Specific)

Applied after overrides. These reflect the signal inherent in how the contact was acquired.

| Source Context | Modifier | Rationale |
|----------------|----------|-----------|
| Conference speaker/panelist | +0.3 | We sought them out after their talk; higher intent. |
| Conference booth visitor | +0.3 | They came to us; self-selected interest. |
| Conference sponsor | +0.2 | Fellow sponsor; peer relationship, potential partner. |
| Event host-introduced | +0.3 | Curated introduction; host vouched for relevance. |
| Inbound (they reached out) | +0.5 | Strongest signal: they found us and initiated contact. |
| Referral from partner | +0.4 | Warm intro with context; higher conversion likelihood. |
| Referral from investor | +0.3 | Investor network intro; strategic but may lack specificity. |
| Random / serendipitous | +0.0 | No source signal; score on conversation merit only. |
| WhatsApp first-contact | +0.1 | Slight signal: they shared personal number or initiated chat. |
| LinkedIn inbound message | +0.2 | They reached out on LinkedIn; moderate intent signal. |

**Cap:** Final score after all modifiers is capped at 5.0.

---

## Tier Thresholds

| Tier | Score Range | Follow-up Deadline | Pipeline Action |
|------|-------------|-------------------|-----------------|
| **A** | 4.0 - 5.0 | 24 hours | Full pipeline entry. Personalized email. Schedule call/meeting. Carlos reviews. |
| **B** | 2.5 - 3.9 | 48-72 hours | Warm follow-up email. Add to nurture sequence if no response. |
| **C** | 1.0 - 2.4 | 1 week | Brief acknowledgment email. Add to newsletter/nurture. |
| **V** | Any | 1 week | Vendor track. Route to procurement / ops. Not a sales lead. |
| **X** | Any | None | Competitor. Log for intelligence. No follow-up. |
| **-** | Any | None | No action warranted. Insufficient data or irrelevant. |
| **N** | Any | Varies | Non-sales relationship. Personal, advisor, press. Relationship follow-up only. |

### Tier Override Rules

- `contact_type = competitor` always maps to Tier X regardless of score.
- `contact_type = vendor` always maps to Tier V regardless of score.
- `contact_type = press` maps to Tier N unless conversation_quality >= 4 and strategic_value >= 4.
- `contact_type = personal` always maps to Tier N.
- Promise floor: any contact with a specific `promises_we_made` entry cannot be below Tier B.

---

## Worked Scoring Examples

### Example 1: Conference Tier A

**Input:** Deep conversation at the DE booth with VP Infrastructure at a neocloud.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Conversation Quality | 5 | 20-min discussion about 50MW deployment. Asked for pricing model. |
| ICP Fit | 5 | C-NEO track. VP with budget authority at a known target account. |
| Urgency Signals | 4 | "Evaluating vendors for Q3 build-out." Active timeline. |
| Strategic Value | 4 | VP-level. Connected to CEO. Could unlock full account. |
| Commitment Density | 5 | We promised a custom proposal by Friday. They promised internal intro to CTO. |

```
base = (5*0.30) + (5*0.25) + (4*0.20) + (4*0.15) + (5*0.10)
     = 1.50 + 1.25 + 0.80 + 0.60 + 0.50
     = 4.65
+ 0.3 (booth visitor modifier)
= 4.95 → capped at 5.0
Tier: A | Urgency: 5 | Relevance: 5
Deadline: 24 hours. Send custom proposal. Schedule CTO intro call.
```

### Example 2: Random Meeting Tier B

**Input:** Brief intro at a dinner via an existing partner (Tier A contact).

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Conversation Quality | 2 | 5-min polite chat. Surface-level. |
| ICP Fit | 4 | Head of Sustainability at a large enterprise. C-ENT track. |
| Urgency Signals | 2 | "Interesting, we should explore." No timeline. |
| Strategic Value | 3 | Director-level. Some network access within the org. |
| Commitment Density | 2 | "Send me your deck." No specific date. |

```
base = (2*0.30) + (4*0.25) + (2*0.20) + (3*0.15) + (2*0.10)
     = 0.60 + 1.00 + 0.40 + 0.45 + 0.20
     = 2.65
+ 0.5 (introduced by Tier A contact)
+ 0.0 (random/serendipitous, no source modifier)
= 3.15
Tier: B | Urgency: 2 | Relevance: 4
Deadline: 48-72 hours. Send deck with personal note referencing the dinner.
```

### Example 3: Conference Tier C

**Input:** Card swap with a journalist at a conference.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Conversation Quality | 1 | Exchanged cards only. 30-second interaction. |
| ICP Fit | 1 | Press. Not a buyer. N/A track. |
| Urgency Signals | 1 | None. |
| Strategic Value | 2 | Writes for an energy trade publication. Some PR value. |
| Commitment Density | 1 | None. |

```
base = (1*0.30) + (1*0.25) + (1*0.20) + (2*0.15) + (1*0.10)
     = 0.30 + 0.25 + 0.20 + 0.30 + 0.10
     = 1.15
+ 0.0 (no modifiers apply)
= 1.15
contact_type = press → Tier N override (conversation_quality < 4)
Tier: N | Urgency: 1 | Relevance: 2
Deadline: 1 week. Add to press contact list. Brief acknowledgment if warranted.
```
