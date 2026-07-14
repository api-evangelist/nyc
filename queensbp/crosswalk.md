# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (Queens Borough President)

Maps the low-hanging fruit on **www.queensbp.nyc.gov** (where `queensbp.org` redirects) to (a) the **APIs actually present** (the empty WordPress REST API; the two Socrata datasets) and (b) NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-queensbp.json](opendata-queensbp.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, service layer locked in a vendor CRM → *unlock.*
- **Queens BP:** a thin WordPress/Divi brochure whose **REST API is switched on but empty**, with **almost no open data** (two community-board datasets) → **standardize.**

QBP is the thinnest domain yet. It is not that the data is trapped in a legacy system or a CRM — it is that there is barely any structured data at all, and the one API the platform already ships (WordPress REST) is dormant because everything is authored as Divi page-builder Pages. The borough president's substantive acts — advisory **land-use (ULURP) recommendations**, tens of millions in **discretionary funding**, and **community-board appointments** — have essentially no machine-readable contract, except two community-board rosters on Open Data. And the office's flagship participatory act, **applying to serve on a community board**, is an HTML/PDF form.

Because all five borough presidents run near-identical thin sites, the move is not a fifth one-off API — it is **one shared Borough President API standard**.

Coverage: ✅ strong open twin · 🟡 partial · ❌ gap (no API).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `CommunityBoard` | `/community-boards` | SODA | Community Board District Managers & Chairs (`8z5h-tzdr`, 20c) | ✅ |
| `CommunityBoardAppointment` | `/community-boards` | SODA | Community Board Members (`rps4-dwwk`, 4c) + chairs/DMs (`8z5h-tzdr`) | ✅ |
| `LandUseRecommendation` (ULURP) | `/land-use` | **HTML only** | — | ❌ gap |
| `DiscretionaryFundingAward` | `/budget`, `/major-budget` | **HTML only** | — | ❌ gap |
| `Event` | `/newsroom` | WordPress REST **returns 0** | — | ❌ gap |
| `PressRelease` | `/newsroom`, `/press-release` | WordPress REST **returns 0** (authored as Pages) | — | 🟡 API exists but empty |
| **`CommunityBoardApplication`** (apply to a board) | 2026 CB application process | **HTML/PDF form only** | — | ❌ **net-new** |
| Constituent services request | `/constituent-services` | **HTML form only** | — | ❌ gap |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **WordPress REST API (`wp/v2`)** | Real, standard, already enabled and public | **Empty** — 0 posts, 0 `project` entries; content lives in Divi Pages, so it serves almost none of the office's content |
| **Socrata SODA (2 datasets)** | Open, machine-readable; clean community-board rosters with the full NYC geography spine | Community boards only; nothing on land use, funding, events, or applications |
| **The Divi site** | Covers every function as a readable page | Page-builder HTML; no structured data behind it; the substantive BP acts have no contract |

## Implications for the API-first + MCP proposal

1. **Light up the API you already own.** Move Newsroom items and events into WordPress posts / a custom post type so the enabled-but-empty `wp/v2` REST API actually serves them — the cheapest possible win.
2. **Give the core BP acts a contract.** Publish community boards + appointments (twinning the two Socrata datasets), land-use (ULURP) recommendations, and discretionary funding as clean resources behind one owned [OpenAPI](openapi/queensbp.yaml).
3. **Add the one net-new write workflow** — `apply_to_community_board` (submit a community board application), replacing the HTML/PDF form; carry a constituent-services request as a companion write later.
4. **Standardize, don't one-off.** Design the contract as a **shared Borough President API** that all five boroughs implement, rather than a Queens-only build — the finding of this assessment.
5. **MCP server** so an agent can answer "who chairs Queens Community Board 7?", "what did the Borough President recommend on this ULURP application?", and — the point — "help me apply to serve on my community board."
