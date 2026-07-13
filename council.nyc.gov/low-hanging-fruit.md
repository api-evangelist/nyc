# Low-Hanging Fruit Index — council.nyc.gov

**Agency:** New York City Council (NYCC)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `Crawl-delay: 10`, `/wp-admin` disallowed). WordPress `wp-sitemap.xml` → 121 pages, custom types `nycc_committee` (40), `nycc_caucus` (9), `nycc_report` (47); member/district pages at `/district-1..51/`. Legislative data probed via the Legistar Web API (403) and cross-referenced to NYC Open Data.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-nycc.md](opendata-nycc.md).

## Headline findings

1. **Council is the most API-covered domain in the project.** Three real APIs already exist: the vendor **Legistar Web API** (`webapi.legistar.com/v1/nyc`), an **open WordPress REST API** (`council.nyc.gov/wp-json`), and the **11 NYCC Open Data datasets**.
2. **But none is owned, unified, or agent-native.** The legislative record depends on a **Granicus-branded, access-gated** vendor API (it 403'd our client); the WP REST API exposes CMS content, not legislative resources; the Open Data sets are flattened snapshots disconnected from Legistar and the site.
3. **Content in WordPress, record in Legistar.** 51 district/member pages, 40 committees, 9 caucuses, 47 reports are WordPress; bills, hearings, and votes are Legistar.
4. **Well-covered data, thin transactional surface.** The one citizen write-workflow — signing up to **testify at a hearing** — has no API.

> **Reframe (third distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* outsourced search + a hidden backend; **Council = consolidate + own three existing APIs** into one resource-oriented, agent-native contract. The work here is least about liberating data and most about **ownership and coherence**.

## The fruit

| # | Name | Entity | Scale | Where the data lives | Open Data twin |
|---|---|---|---|---|---|
| 1 | Members / District pages | `CouncilMember` | 51 | WP pages + Open Data | ✅ Members (`uvw5-9znb`), Committee Membership |
| 2 | Council Districts | `District` | 51 | CARTO maps; DCP geo | ✅ City Council Districts (DCP) |
| 3 | Committees | `Committee` | 40 | WP `nycc_committee` + Legistar | ✅ Committee Membership (`aabe-yfm9`) |
| 4 | Caucuses | `Committee` | 9 | WP `nycc_caucus` | ❌ gap |
| 5 | Legislation (bills/local laws) | `Legislation` | 10,000s | **Legistar** + Open Data | ✅ Bills & Local Laws (`6ctv-n46c`) |
| 6 | Meetings / Hearings | `Meeting` | ongoing | **Legistar** + Viebit video | ✅ Meetings (`m48u-yjt8`) |
| 7 | Discretionary Funding | `DiscretionaryFunding` | 27-col | Open Data | ✅ Discretionary Funding (`4d7f-74pe`) |
| 8 | Participatory Budgeting | `DiscretionaryFunding` | 20-col | Open Data | ✅ PB Projects (`wwhr-5ven`) |
| 9 | Reports | `Report` | 47 | WP `nycc_report` | ❌ gap |
| 10 | Testify at a hearing | `TestimonyRegistration` | — | sign-up form | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Legistar Web API** (Granicus) — legislative record; **WordPress REST API** (open) — content; **Socrata SODA** — 11 datasets.
- Platform: **WordPress on WP Engine** (third distinct platform after Parks' Smarty/PHP and DOE's Sitefinity).
- Vendors: CARTO (maps), Viebit (video), Livestream/Vimeo, StreamText (captions), essentialAccessibility, Font Awesome.

## Reverse-engineered entities

`CouncilMember` · `District` · `Committee` (incl. caucuses) · `Legislation` (bill/resolution/local law) · `Meeting`/hearing · `Vote` · `DiscretionaryFunding` · `Report` · `TestimonyRegistration` (net-new) — join keys: **councilMemberId**, **matterId** (Legistar), **district number**.

## Next

1. **JSON Schema** per entity, reconciling WP fields + Legistar fields + Open Data columns.
2. **OpenAPI** consolidating Legistar + WP + Open Data behind one owned contract (+ the net-new testimony sign-up).
3. **MCP** artifact: `find_members`, `get_member`, `find_legislation`, `get_legislation`, `find_meetings`, `find_discretionary_funding`, `register_testimony`.
