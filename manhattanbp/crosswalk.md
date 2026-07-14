# Crosswalk — Website/Forms Fruit ↔ APIs ↔ NYC Open Data (Manhattan BP)

Maps the low-hanging fruit on **manhattanbp.nyc.gov** to (a) the **existing APIs** (Socrata SODA; the generic WordPress REST API) and (b) the **21 MBPO datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-manhattanbp.json](opendata-manhattanbp.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, resident transactions locked in a vendor CRM → *unlock the service layer.*
- **Manhattan BP:** the data is **open but fragmented** (one Socrata dataset per program per fiscal year), the site is a **generic WordPress/Divi template**, and the office is **one of five near-identical borough presidents** → **federate into one shared Borough President API.**

The Manhattan BP inverts the "trapped in HTML" problem in a new way. The civic data — ULURP recommendations, appointments, community-board leadership, funding awards, constituent cases — is already on Open Data. But it is scattered across **21 one-off datasets** (five separate `Capital Grant Awards` datasets, 2014–2018), the public site is an off-the-shelf WordPress/Divi build whose only API is generic WordPress, and the office's flagship citizen action — **applying to serve on a community board** — is a Forminator web form with no contract at all. And every one of the five borough presidents looks the same, which is the argument for building the API once.

Coverage: ✅ strong open twin · 🟡 partial/PDF/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Form | API today | Open Data | Cov. |
|---|---|---|---|---|
| `CommunityBoard` | `/community-boards` | SODA / WP REST | Community Board Leadership (`3gkd-ddzn`, 26c) | ✅ |
| `LandUseRecommendation` (ULURP) | `/land-use` | SODA | ULURP Recommendations (`gt5i-dmde`, 4c) — body is a **PDF link** | 🟡 PDF |
| `BoardAppointment` | `/community-boards` | SODA | BP Appointments (`nr9n-yqxr`, 3c) | ✅ |
| `FundingAward` | `/funding` | SODA | Capital Grant Awards 2014–2018 (`9umc-3b2y`,`6wee-b7wf`,`83z6-smyr`,`k84j-firu`,`66yh-nemi`); Tourism (`x4ud-jhxu`); Community Grants (`rsnd-bbih`); MCAP (`y3ea-en4q`); Police-Community (`w38c-pyzq`) | ✅ but **fragmented** |
| `Legislation` | `/policy` | SODA | Legislation (`uf8p-ervp`, 4c) — body is an **external URL** | 🟡 link |
| `ConstituentCase` | — | SODA | Constituent Services (`39qw-754y`); Historical (`kpjg-ubxi`) — **de-identified** | 🟡 de-identified |
| **`CommunityBoardApplication`** (serve on a board) | Forminator form + PDF | **WP form only** | — (appointments appear later in `nr9n-yqxr`) | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (21 datasets)** | Open, machine-readable; genuinely covers the office's core outputs (land use, appointments, funding, constituents) | Fragmented into one dataset per program per year; some historical/stale; ULURP + legislation substance is only a linked PDF/URL |
| **WordPress REST API** | Exists by default; publishes site content as JSON | Generic CMS surface; nothing purpose-built for the office's civic entities; the community-board application is a Forminator form with no contract |

## Implications for the API-first + MCP proposal

1. **Unify the per-year datasets into one resource.** Collapse the five `Capital Grant Awards` datasets plus Tourism/Community/MCAP/Police-Community into a single `FundingAward` resource ([OpenAPI](openapi/manhattanbp.yaml)) — so a consumer asks "who did the Manhattan BP fund?" once, not across five Socrata IDs.
2. **Add the one net-new write workflow** — `apply_to_community_board` (submit a `CommunityBoardApplication`), replacing the Forminator form / PDF.
3. **Keep constituents de-identified.** Constituent cases stay type/subject/status/geography only; the API never exposes an individual's identity.
4. **Federate across the five boroughs.** Because every BP office is structurally identical, this contract is written to be deployed per office rather than rebuilt five times.
5. **MCP server** so an agent can answer "what did the BP recommend on this ULURP application?", "who did the BP fund in Council District 3?", and — the point — "apply for me to serve on Community Board 5."
