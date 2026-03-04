# Netherlands -- Entity Types

## Besloten Vennootschap (BV / Private Limited Company)

Standard vehicle for Dutch project finance and commercial operations. Flex-BV regime since 1 October 2012.

| Kenmerk (Feature) | Detail |
|---|---|
| Minimumkapitaal (minimum capital) | EUR 0.01 -- no meaningful minimum in practice (Art. 2:178 BW) |
| Notariskosten (notary fees) | EUR 500--1,500 standard; spoedoprichting (express incorporation) 3 werkdagen @ EUR 999 |
| KvK-registratie | EUR 82.25 (2025 tariff) |
| Totale oprichtingskosten | EUR 600--2,600 depending on complexity and urgency |
| Oprichting (formation) | Notariele akte van oprichting required (Art. 2:175 BW) |
| Register at KvK | Within 8 days of incorporation |

**Statuten (articles of association)** must include: naam (name), zetel (registered seat), doel (purpose), maatschappelijk kapitaal (authorised capital), bestuur (management), aandeelhoudersvergadering (general meeting), winstbestemming (profit allocation).

**Governance:**
- **Aandeelhoudersvergadering (AVA / general meeting):** sovereign body; appoints/dismisses bestuurders
- **Bestuur (management board):** manages day-to-day operations; minimum 1 bestuurder; fiduciary duties under Art. 2:239 BW
- **Raad van commissarissen (RvC / supervisory board):** optional unless structuurregime applies
- **Besluitvorming buiten vergadering (Art. 2:238 BW):** resolution without meeting; requires unanimous written consent unless statuten prohibit

**Aandelenlevering (share transfer):** must be by notariele akte (Art. 2:196 BW) + registration in aandeelhoudersregister.

**Blokkeringsregeling (Art. 2:195 BW):** since Flex-BV, aanbiedingsregeling (right of first offer) is default; freely excludable in statuten. Critical for change-of-control clauses.

**Uitkeringen (distributions, Art. 2:216 BW):** dual test:
1. Balanstest (balance sheet test): equity exceeds reserves required by statuten
2. Liquiditeitstest (liquidity test): bestuurder must approve; personally liable if knew/should have known company could not continue paying debts

## Naamloze Vennootschap (NV / Public Limited Company)

For larger, listed, or bond-issuing structures.

| Kenmerk | Detail |
|---|---|
| Minimumkapitaal | EUR 45,000 fully subscribed; minimum 25% paid up on issuance (Art. 2:67 BW) |
| Accountantsverklaring | Required for inbreng in natura (contribution in kind, Art. 2:94a BW) |
| Board structure | Two-tier mandatory for structuurvennootschap (Art. 2:152 BW) |
| Bearer shares | Abolished since 1 July 2019 (Wet omzetting aan toonder) |
| Prospectusplicht | Applicable if offering securities to public (see `overview.md`) |

## Commanditaire Vennootschap (CV / Limited Partnership)

Tax-transparent vehicle used in fund and cross-border structures.

| Kenmerk | Detail |
|---|---|
| Beherende vennoot (GP) | Unlimited liability for CV debts |
| Commanditaire vennoot (LP) | Limited liability -- loses protection if takes part in management (bestuursverbod, Art. 20 WvK) |
| Open CV | Freely transferable interests; treated as fiscaal non-transparant (opaque) for VPB |
| Gesloten CV (closed) | Transfer requires consent of all vennoten; fiscaal transparant -- income attributed to vennoten |
| Formation | No notarial deed required; CV-overeenkomst suffices; register at KvK |
| Use case | Fund structures, cross-border JVs, layered holding structures |

## Stichting (Foundation)

Orphan entity for structured finance and bankruptcy-remote security structures.

- **No shareholders, no members, no equity** -- bestuur (board) is sole governing body
- Creates **faillissementsbestendigheid (bankruptcy remoteness):** assets not part of sponsor's estate
- **Stichting administratiekantoor (STAK):** holds shares and issues certificaten van aandelen (depository receipts); separates legal ownership from economic interest
- **Security trustee role:** holds shares of project BV as zekerheidsagent (security agent) for lenders
- **Governance:** typically 1--3 independent bestuurders from trust companies (e.g., Intertrust, TMF, Vistra); governed by bestuursinstructie
- Stichtingen may make distributions if statuten permit (Art. 2:285 lid 3 BW)
- Formation: notariele akte required; register at KvK

## Cooperatie U.A. (Cooperative)

| Kenmerk | Detail |
|---|---|
| Dividendbelasting | No withholding tax on distributions to members (Art. 1 lid 1 Wet DB) |
| Profit distribution | Flexible via ledenovereenkomst (membership agreement) |
| Liability | U.A. = uitsluiting van aansprakelijkheid (exclusion of member liability) |
| Formation | Notariele akte required (Art. 2:53a jo. 2:27 BW); register at KvK |
| Use case | JV structures, fund vehicles, energiecooperaties (energy cooperatives) |
| Governance | Ledenvergadering (member meeting) + bestuur; optional RvC |

## UBO-register

- **Registratieplicht (mandatory registration)** at KvK for all Dutch legal entities
- **Public access restricted** since 15 July 2025 following CJEU privacy ruling (Case C-37/20 and C-601/20)
- Only Wwft/Wtt-obligated entities (banks, notarissen, tax advisers) retain access
- **UBO definition:** uiteindelijk belanghebbende = natural person with >25% ownership, >25% voting rights, or effective control (Art. 10a Wwft)
- **Sancties:** administrative fines up to EUR 22,500; criminal liability for non-compliance
- **Compliance rate:** ~80% of registered entities have filed UBO information

## Entity Selection Matrix

| Use Case | Recommended Entity | Key Reason |
|---|---|---|
| Single-asset project SPV | BV | Flex-BV simplicity, limited liability, fiscal unity eligible |
| Listed holding / bond issuer | NV | Public offering capability, market credibility |
| Fund / investor pooling | Gesloten CV or Cooperatie U.A. | Tax transparency (CV) or no dividend WHT (Cooperatie) |
| Security trustee / orphan | Stichting | Bankruptcy remoteness, no equity holders |
| Energy cooperative | Cooperatie U.A. | No dividend WHT, community governance |
| Cross-border JV | BV or CV | Depends on tax transparency needs |
