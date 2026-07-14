# Crosswalk — Website/Product Fruit ↔ APIs ↔ NYC Open Data (Public Advocate)

Maps the low-hanging fruit on **advocate.nyc.gov** and the **Worst Landlord Watchlist** to (a) the **APIs that exist today** (the undocumented Watchlist route; Council's Legistar) and (b) **NYC Open Data — of which the Public Advocate has none**. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-pubadvocate.json](opendata-pubadvocate.json) (an empty array).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open (24 datasets), transactions locked in a vendor CRM → *unlock the service layer.*
- **Public Advocate:** **zero open data, a self-hosted main site that was down (502), one undocumented orphan API, and no intake surface** → **respond** — give the city's ombudsman an owned API to publish its work and take and track the public's complaints.

The Public Advocate inverts NYCHA. NYCHA's problem was *transactions locked behind data that was already open*. The Public Advocate's problem is that **almost nothing is machine-readable at all**: it publishes no Open Data, its site couldn't stay up during the crawl, and the one real API it has (the Watchlist) is undocumented and off-platform. A resident or agent asking "who are the worst landlords in my ZIP?", "what has the PA reported on HPD?", or "help me with a city agency" has, respectively, an undocumented endpoint, a PDF, and a web form.

Coverage: ✅ strong open twin · 🟡 partial/undocumented · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Product | API today | Open Data | Cov. |
|---|---|---|---|---|
| `WorstLandlord` | Worst Landlord Watchlist | **undocumented** `landlordwatchlist.com/api/landlords` | — (derived from HPD/DOB, not published under a PA label) | 🟡 undocumented |
| `WatchlistBuilding` | Watchlist (per landlord) | — (not exposed per building) | 🟡 HPD violations open citywide, not as a PA rollup | 🟡 partial |
| `Legislation` | — | **Legistar Web API** (owned by NYCC) | — | 🟡 not PA-owned |
| `Report` | `/reports` (PDF/HTML, 502) | — | — | ❌ gap |
| `PublicInterestRequest` | correspondence / reports | — | — | ❌ gap |
| **`OmbudsmanComplaint`** (help with a city agency) | web form / phone / email | **none** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Worst Landlord Watchlist** (`/api/landlords`) | A real, modern, data-backed product; ranked landlords with portfolio-level violation metrics | Undocumented, unversioned, off-platform (Vercel), disconnected from advocate.nyc.gov; no OpenAPI; per-building detail not exposed |
| **advocate.nyc.gov** | The office's official home for reports, help, and public interest content | Self-hosted nginx/Ubuntu; **502 during the crawl**; PDF/HTML only; no content API; no Open Data |
| **NYC Open Data** | The HPD/DOB/registration data underneath the Watchlist is open | Nothing under a Public Advocate label — the office contributes zero assets |

## Implications for the API-first + MCP proposal

1. **Document what already works.** The Watchlist's `/api/landlords` is a real product surface — promote it to an owned, versioned, documented contract ([OpenAPI](openapi/pubadvocate.yaml)) with `WorstLandlord` and `WatchlistBuilding` resources.
2. **Consolidate the office's scattered output.** Sponsored legislation (today in Council's Legistar), reports (today PDFs on a 502ing site), and public interest demands behind one PA-owned model — so consumers learn one contract, not three off-platform silos.
3. **Add the one net-new write workflow** — `file_complaint` (`OmbudsmanComplaint`): ask the ombudsman for help with a city agency, with `consentToContactAgency` so the office may act on the resident's behalf, and machine-trackable status.
4. **Publish, finally, to Open Data.** The Watchlist and the reports catalog are obvious first PA-owned datasets.
5. **MCP server** so an agent can answer "who are the worst landlords in the Bronx?", "what has the Public Advocate reported on HPD?", and — the point — "file a complaint about my agency problem and tell me its status."
