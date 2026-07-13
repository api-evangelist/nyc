# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (NYCC)

Maps the low-hanging fruit on **council.nyc.gov** to (a) the **existing APIs** (Legistar, WordPress REST) and (b) the **11 NYCC datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-nycc.json](opendata-nycc.json).

## The reframe — third distinct pattern

- **Parks:** data-rich HTML, machine-readable twins on Open Data, legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data **already has three APIs** — a vendor legislative API (Legistar), an open WordPress REST API, and Open Data SODA — but none is owned, coherent, or agent-native → **consolidate + own.**

Council is the least about *liberating* data and the most about **API ownership and coherence**. A resident or agent who wants "which bills did my council member sponsor, and when's the next hearing?" must today stitch together Legistar (vendor, gated), a WordPress site, and flattened Open Data snapshots.

Coverage: ✅ strong twin/API · 🟡 partial · ❌ gap.

## Entity crosswalk

| Entity | Website | Legistar API | Open Data | Cov. |
|---|---|---|---|---|
| `CouncilMember` | `/district-N/` pages | persons | Members 1999–present (`uvw5-9znb`, 6c) | ✅ |
| `District` | `/districts/`, CARTO maps | — | City Council Districts (DCP geo) | ✅ |
| `Committee` (+caucus) | WP `nycc_committee`/`nycc_caucus` | bodies | Committee Membership (`aabe-yfm9`, 11c) | ✅ / 🟡 caucus |
| `Legislation` | links out to Legistar | **matters** (full) | Bills & Local Laws (`6ctv-n46c`, 15c — flattened) | ✅ |
| `Meeting` / hearing | Legistar calendar + Viebit video | **events** | Meetings 1999–2024 (`m48u-yjt8`, 10c) | ✅ |
| `Vote` | — | **votes** | (folded into legislation snapshot) | 🟡 API-only |
| `DiscretionaryFunding` | `/budget/` | — | Discretionary Funding (`4d7f-74pe`, 27c) | ✅ |
| Participatory Budgeting | `/pb/` | — | PB Projects (`wwhr-5ven`, 20c) + Tracker | ✅ |
| Constituent services | member offices | — | Constituent Services 2015–2025 (`b9km-gdpy`, 11c) | ✅ |
| Capital budget | `/budget/` | — | City Council Capital Budget (`t474-a92g`) | ✅ |
| `Report` | WP `nycc_report` (47) | — | — | ❌ gap |
| `TestimonyRegistration` | sign-up form | — | — | ❌ **net-new** |

## The three-API problem, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Legistar Web API** | The authoritative live legislative record (matters, votes, events, persons) | Granicus-branded; access-gated (403 to our client); OData shape, not a Council product; no agent surface |
| **WordPress REST API** | Open; members/committees/reports as content | CMS content, not legislative resources; no `Legislation`/`Vote` |
| **Open Data (SODA)** | Open; discretionary funding, PB, snapshots | Flattened, periodic snapshots; disconnected from the live Legistar record and from the site |

## Implications for the API-first + MCP proposal

1. **Own the contract.** Publish one NYC Council API (this project's [OpenAPI](openapi/nyc-council.yaml)) that fronts Legistar for the live record, WordPress for member/committee content, and Open Data for funding/PB — so consumers learn one resource model, not three vendor systems.
2. **Make votes and hearings first-class** — they exist in Legistar but are absent from the flattened Open Data and hard to reach; surface them as `Vote` and `Meeting` resources.
3. **Close the small gaps** — publish caucuses and reports as resources.
4. **Add the one missing write workflow** — `register_testimony` (sign up to speak at a hearing).
5. **MCP server** so an agent can answer "what did my member sponsor / when's the next hearing / how much discretionary funding went to my district?" in one place.
