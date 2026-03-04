# Norway -- Entity Types

## Entity Comparison

| Type | Full Name | Min. Capital | Liability | Governance | Use Case |
|---|---|---|---|---|---|
| AS | Aksjeselskap (private limited company) | NOK 30,000 | Limited to paid-in capital | Styre (board) + daglig leder (CEO) | Standard commercial vehicle |
| ASA | Allmennaksjeselskap (public limited company) | NOK 1,000,000 | Limited to paid-in capital | Styre + daglig leder (mandatory); mandatory bedriftsforsamling if >200 employees | Listed companies, large enterprises |
| ANS | Ansvarlig selskap (general partnership) | None | Unlimited joint and several | Partners | Professional partnerships |
| DA | Ansvarlig selskap med delt ansvar (limited partnership) | None | Unlimited but divided pro rata | Partners | Investment partnerships |
| KS | Kommandittselskap (limited partnership with silent partners) | None | Komplementar: unlimited; Kommandittist: limited | Komplementar manages | Legacy structures (rarely used for new formations) |
| ENK | Enkeltpersonforetak (sole proprietorship) | None | Unlimited personal | Owner | Freelancers, small businesses |
| NUF | Norskregistrert utenlandsk foretak (Norwegian branch of foreign entity) | None (parent entity's capital) | Depends on parent entity type | Parent entity's governance | Foreign companies with NO operations |
| SA | Samvirkeforetak (cooperative) | Variable | Limited | Members; one member, one vote | Agricultural, housing cooperatives |
| Stiftelse | Foundation | Grundkapital (foundation capital) | No owners; limited to assets | Styre (board) | Charitable, holding structures |

## Aksjeselskap (AS) -- Detailed

### Stiftelse (Incorporation)
- Registration with Foretaksregisteret (Register of Business Enterprises) in Bronnoysund
- Stiftelsesdokument (memorandum of incorporation) signed by stifterne (founders)
- Vedtekter (articles of association) adopted
- Minimum aksjekapital (share capital): NOK 30,000 (reduced from NOK 100,000 in 2012)
- No notarisation required (unlike Dutch BV)

### Aksjekapital og aksjer (Share Capital and Shares)
- Shares may have different classes (aksjeklasser) with different rights
- Pålydende (par value): any amount (but total must equal NOK 30,000+)
- No bearer shares; all shares registered in aksjeeierboken (shareholders' register)
- Share transfers: no mandatory blokkeringsregeling (transfer restriction) unless in vedtektene; default is board samtykke (consent) -- asl. § 4-15

### Styre (Board of Directors)
- Mandatory for all AS: minimum 1 styremedlem (board member) if capital <NOK 3M; minimum 3 if capital >=NOK 3M
- Styreleder (chair) elected by generalforsamling (general meeting) or by the board
- Ansatterepresentasjon (employee representation): mandatory if >30 employees (1/3 of board members)
- Daglig leder (CEO/managing director): not mandatory for AS with capital <NOK 3M; otherwise mandatory

### Generalforsamling (General Meeting)
- Ordinaer generalforsamling (AGM): within 6 months after year-end
- Vedtak (resolutions): simple majority unless otherwise specified
- Vedtektsendring (articles amendment): 2/3 majority of both votes and capital represented
- Aksjonaerers rettigheter (shareholders' rights): information rights (asl. § 5-15), minority rights (asl. § 5-25 for 10%+ holders)

### Utdeling (Distributions)
- Utbytte (dividends): may only be distributed from distributable reserves (fri egenkapital) -- asl. § 8-1
- Forsvarlighetsvurdering (prudence test): the board must ensure the company retains sufficient egenkapital (equity) and likviditet (liquidity) for continued operations -- asl. § 3-4
- Konsernbidrag (group contributions): see `tax-framework.md`

## NUF (Norwegian Branch of Foreign Entity)

- Registration: Foretaksregisteret (same register as AS)
- Commonly used by foreign entities operating in Norway
- Tax treatment: taxed on Norwegian-source income; may create fast driftssted (permanent establishment) under tax treaties
- No separate legal personality from parent entity
- Reporting: annual accounts filed for the Norwegian branch; parent entity's accounts may also need filing

## Register over reelle rettighetshavere (UBO Register)

- Lov om register over reelle rettighetshavere (in force from 1 October 2024)
- All Norwegian juridiske personer (legal entities) must register reelle rettighetshavere (beneficial owners)
- Threshold: physical persons with >25% ownership or voting rights, or otherwise exercising control
- Deadline for existing entities: **31 July 2025**
- New entities: register within 14 days of incorporation
- Register maintained by Bronnoysundregistrene; access via Altinn

## Entity Selection Matrix

| Factor | AS | NUF | ANS/DA | ENK |
|---|---|---|---|---|
| Limited liability | Yes | Depends on parent | No | No |
| Min. capital | NOK 30,000 | None | None | None |
| Corporate tax rate | 22% | 22% (on NO-source) | Pass-through | Pass-through |
| Fritaksmetoden eligible | Yes | If qualifying | No (pass-through) | No |
| Audit opt-out | Yes (if small) | Yes (if small) | Yes (if small) | Yes (if small) |
| Foreign ownership | Unrestricted | N/A | Unrestricted | N/A |
| SPV suitability | High | Medium | Low | None |
