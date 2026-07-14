# Low-Hanging Fruit Index — NYC Public Advocate

**Agency:** New York City Public Advocate (Office of the Public Advocate)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, robots-respecting). Attempted to fingerprint `www.pubadvocate.nyc.gov` / `advocate.nyc.gov` — the site 301-redirects to `advocate.nyc.gov` and returned **HTTP 502 Bad Gateway** from a self-hosted `nginx/1.18.0 (Ubuntu)` origin (the office runs its own server, **not** the shared NYC.gov "Livesite" platform, and it was down at assessment time). Verified via the Socrata Discovery API that **no** NYC Open Data asset carries a Public Advocate agency label (tested `Public Advocate (PA)`, `Office of the Public Advocate`, `Public Advocate`, `Office of the Public Advocate (PA)` — all **0**). Fingerprinted the flagship product, the **Worst Landlord Watchlist** (`landlordwatchlist.com`), as a **Next.js/React app on Vercel** and discovered an **undocumented** `/api/landlords` JSON endpoint returning 99 ranked landlords.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-pubadvocate.md](opendata-pubadvocate.md).

## Headline findings

1. **Zero Open Data.** Unlike NYCHA (24 datasets), the city's ombudsman publishes **nothing** machine-readable to NYC Open Data. Its output is reports/PDFs, its own website, and one product.
2. **The main site was down.** `advocate.nyc.gov` runs on the office's **own** nginx/Ubuntu box — not the shared NYC.gov chassis — and returned **502 Bad Gateway** on every path throughout the crawl.
3. **The one modern surface is an orphan.** The **Worst Landlord Watchlist** (`landlordwatchlist.com`) is a separate Next.js/Vercel app with an **undocumented** `/api/landlords` endpoint (99 landlords: org, officer, buildings, units, DOB violations, avg open HPD violations, tax liens, evictions, rank) — real data, no docs, no OpenAPI, disconnected from the main site.
4. **No intake API.** "Help with a city agency" — the office's constitutional reason for existing — is a web form, phone call, or email. There is no machine-readable way to file or track an `OmbudsmanComplaint`.
5. **Its legislation lives elsewhere.** The Public Advocate introduces bills through the City Council; those files live in Council's **Legistar**, owned by NYCC.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **Public Advocate = respond.** Here there is barely anything machine-readable at all — the work is to give the city's watchdog an **owned API** that documents the Watchlist, consolidates its reports/legislation/public-interest output, and above all lets residents **file and track a complaint** against a city agency.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Worst Landlord Watchlist | `WorstLandlord` | undocumented `/api/landlords` (Vercel) | ❌ none under PA label |
| 2 | Watchlist Buildings | `WatchlistBuilding` | derived from HPD/DOB | 🟡 HPD violations open citywide, not as PA rollup |
| 3 | Sponsored Legislation | `Legislation` | Council Legistar (owned by NYCC) | ❌ none |
| 4 | Reports & Investigations | `Report` | PDFs/HTML on advocate.nyc.gov (502) | ❌ none |
| 5 | Public Interest Requests | `PublicInterestRequest` | correspondence / reports | ❌ none |
| 6 | **Help with a city agency** | **`OmbudsmanComplaint`** | web form / phone / email | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **`landlordwatchlist.com/api/landlords`** — the one real API; undocumented Next.js data route on Vercel.
- **advocate.nyc.gov** — self-hosted `nginx/1.18.0 (Ubuntu)`; **502 during crawl**; no content API; the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Siebel.
- **Legistar (Council)** — where the PA's bills live; owned by NYCC.
- **NYC Open Data** — hosts the HPD/DOB data underneath the Watchlist, but **zero** assets under a Public Advocate label.

## Reverse-engineered entities

`WorstLandlord` · `WatchlistBuilding` · `Legislation` · `Report` · `PublicInterestRequest` · `OmbudsmanComplaint` (net-new write) — join keys: **landlord id** (Watchlist), **BBL/BIN** (buildings), **Legistar file / Intro #** (legislation), **agency** (complaints, reports, public-interest demands).

## Next

1. **JSON Schema** per entity, reconciling the real `/api/landlords` field names and the NYC geography spine — done ([schemas/](schemas/)).
2. **OpenAPI** promoting the undocumented Watchlist route to an owned contract, consolidating legislation/reports/public-interest, and adding the net-new `POST /ombudsman-complaints` (help with a city agency) — done ([openapi/pubadvocate.yaml](openapi/pubadvocate.yaml)).
3. **MCP** artifact: `find_worst_landlords`, `get_worst_landlord`, `get_worst_landlord_buildings`, `find_watchlist_buildings`, `find_legislation`, `find_reports`, `find_public_interest_requests`, `list_my_complaints`, `file_complaint`, `get_complaint` — done ([mcp/pubadvocate-mcp.json](mcp/pubadvocate-mcp.json)).
