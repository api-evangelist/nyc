# NYC Open Data — Public Advocate Datasets

All NYC Open Data assets whose **Dataset-Information_Agency** matches the NYC Public Advocate (checked via the Socrata Discovery API, 2026-07-13).

## Result: zero

**There are none.** No NYC Open Data asset carries a Public Advocate agency label. This was verified by querying `data.cityofnewyork.us` through the Socrata Discovery API for every plausible label:

| Agency label tested | Assets |
|---|--:|
| `Public Advocate (PA)` | 0 |
| `Office of the Public Advocate` | 0 |
| `Public Advocate` | 0 |
| `Office of the Public Advocate (PA)` | 0 |

A broader `q=advocate` scan of the NYC domain surfaced only datasets belonging to **other** agencies — Campaign Finance Board (CFB), City Council (NYCC), Civilian Complaint Review Board (CCRB), Department of Education (DOE), Department of Probation (DOP), and the Office of the City Clerk (OCC) — matched on the word "advocate" in titles/descriptions, not ownership.

The machine-readable index [opendata-pubadvocate.json](opendata-pubadvocate.json) is therefore an **empty array** — an honest record of the gap.

## Why this matters

The Public Advocate is the city's ombudsman and watchdog, yet it is the **least open** domain assessed so far. Where NYCHA publishes 24 datasets and Council exposes three APIs, the Public Advocate contributes **nothing** to NYC Open Data. Its output lives instead in three off-platform, mostly non-machine-readable places:

- **The Worst Landlord Watchlist** — real data, but on an orphan Next.js/Vercel app with an *undocumented* `/api/landlords` endpoint, not on Open Data. See [apis-observed.md](apis-observed.md).
- **Reports & investigations** — PDFs and HTML on the self-hosted `advocate.nyc.gov` site (which returned 502 during the crawl). No index, no metadata.
- **Sponsored legislation** — in the City Council's Legistar system, owned by NYCC, not the PA.

The underlying data the office *uses* — HPD Housing Maintenance Code violations, DOB violations, building registrations — **is** open on `data.cityofnewyork.us`, but under HPD/DOB, never under the Public Advocate. See [crosswalk.md](crosswalk.md).
