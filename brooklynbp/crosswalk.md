# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (Brooklyn Borough President)

Maps the low-hanging fruit on **www.brooklynbp.nyc.gov** (and the lapsed **brooklyn-usa.org**) to (a) the **existing APIs** (Socrata SODA; the WordPress + Events Calendar REST APIs) and (b) the **21 BPBK datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-brooklynbp.json](opendata-brooklynbp.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data open, service layer locked in a vendor CRM → *unlock the service layer.*
- **Brooklyn BP:** real-but-scattered open data (21 Socrata IDs) + a generic CMS API + a **lapsed domain**, structurally identical to four other Borough Presidents → **template one shared BP API across all five boroughs.**

Brooklyn BP inverts the scarcity assumption. The brief guessed *zero* Socrata datasets; there are in fact **21**, plus a live WordPress/Events-Calendar API. The problem is not that the data is trapped — it is that it is **fragmented and unowned**: 21 single-purpose dataset IDs, many thin or stale, a generic CMS API that exists only because the site runs WordPress, and no owned Borough-President contract. And the office let its own `.org` lapse into a domain-flip. Meanwhile the constituent action that matters most each year — **applying to serve on a community board** — has no API at all.

Coverage: ✅ strong open twin · 🟡 partial/thin/stale · ❌ gap (no API).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `LandUseRecommendation` (ULURP) | `/land-use`, `/uniform-land-use-review-procedure` | SODA | ULURP Recommendations (`4j6i-9rmr`, 6c) | ✅ |
| `CommunityBoard` | `/community-boards`, `/community-boards-hub` | SODA | Community Board Contact List (`dy27-rrad`, 16c) | ✅ |
| `BoardAppointment` | `/departments`, board pages | SODA | BIDS (`pvxf-9irb`, 23c); CECs (`5mxw-kxpt`); HHC CAB (`avh4-h5hx`); BPL (`q7f5-jwds`); DYCD NABs (`95u9-kyyu`); SWAB (`rbwa-m4iy`); Misc (`efdc-dxuz`) | 🟡 one thin table per board |
| `FundingAward` | `/budget`, `/capital-funding-application-fy23` | SODA | Tourism Grants (`rma9-fm39`, 19c); Capital Awards (`n6ej-pebd`); Discretionary (`tsb8-3rct`, `ubuy-v2nw`) | 🟡 thin/stale |
| `Report` (legislation/report/testimony/press) | `/reports`, `/bkbp-testimonies`, `/op-ed`, `/newsroom` | SODA + WordPress REST | Office Legislation - Passed (`e6ph-9uv7`, 4c) | 🟡 mostly CMS posts |
| `Event` | `/events` | **The Events Calendar REST (live)** | — | ✅ live API |
| Meeting request / assistance | contact forms | **web form only** | Meeting Requests (`gqzy-vhwd`); Requests for Assistance (`y6ds-67d5`) | ❌ form dump |
| **`CommunityBoardApplication`** (apply to a board) | `/community-boards` | **web form only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (21 datasets)** | Open, machine-readable; covers ULURP, appointments, awards, community boards | 21 single-purpose IDs; many thin (3-6 cols); several stale snapshots (2015-2018); no unifying model |
| **WordPress + Events Calendar REST** | Live, public, includes a genuinely useful events/hearings feed | Generic CMS plumbing; exists by platform accident, not design; not a BP-specific contract |
| **Constituent forms** | Where residents actually apply / request meetings | Unstructured web forms; no API, no OpenAPI, no JSON contract; not agent-accessible |
| **brooklyn-usa.org** | (former identity) | Lapsed; redirects offsite to a domain-flip — a live ownership failure |

## Implications for the API-first + MCP proposal

1. **Publish the open data as one clean resource model.** ULURP, community boards, appointments, funding awards, and publications behind one owned BP contract ([OpenAPI](openapi/brooklynbp.yaml)) — so consumers learn one model, not 21 Socrata IDs.
2. **Wrap the events feed.** Present The Events Calendar output through the same owned contract (`/events`) instead of a plugin endpoint.
3. **Add the one net-new write workflow** — `apply_to_community_board` (submit a `CommunityBoardApplication`), the counterpart to the read-only appointments and community-board datasets.
4. **Consolidate the appointment tables.** Fold the dozen 'BP Appointments' datasets into one `BoardAppointment` resource keyed on board + person + term.
5. **Template across all five boroughs.** Because every Borough President runs the same thin office with the same powers, define this contract once and instantiate it per borough — the highest-leverage move in the domain.
6. **MCP server** so an agent can answer "how did the Brooklyn BP vote on this ULURP application?", "who did the BP appoint to my Community Education Council?", "what tourism grants went to my community board?", and — the point — "help me apply to serve on my community board."
