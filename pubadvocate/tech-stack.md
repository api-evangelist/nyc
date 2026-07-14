# Technology & Vendor Inventory — NYC Public Advocate

What the Office of the Public Advocate's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). The Public Advocate is a **fragmented, off-platform domain**: a self-hosted main site that was **down** during the crawl, and one modern product — the **Worst Landlord Watchlist** — running on a completely separate commercial stack.

## Three front doors, none joined up

| Surface | URL | What it does | Status at crawl |
|---|---|---|---|
| Informational site | `advocate.nyc.gov` (← `www.pubadvocate.nyc.gov`) | About, reports, "help with a city agency", public interest content | **HTTP 502 Bad Gateway** |
| **Worst Landlord Watchlist** | **`landlordwatchlist.com`** | Ranks NYC's ~100 worst landlords on HPD/DOB violation data | 200 OK (modern) |
| Sponsored legislation | `legistar.council.nyc.gov` | Bills the PA introduces — **owned by the City Council** | live (NYCC) |

## Informational site (advocate.nyc.gov)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Web server | **nginx/1.18.0 (Ubuntu)** | `Server: nginx/1.18.0 (Ubuntu)` on the 301 chain and the 502 page |
| Hosting | **Self-hosted origin** (not NYC.gov shared platform) | Own domain apex, own nginx; no `livesite-version`, no Akamai edge headers |
| Redirect chain | `www.pubadvocate.nyc.gov` → `http://advocate.nyc.gov` → `https://advocate.nyc.gov` | successive 301s |
| Availability | **Down during crawl** | every path (`/`, `/reports`, `/legislation`, `/sitemap.xml`) returned **502 Bad Gateway** |

This is the finding, not an accident of timing: the city's watchdog does **not** sit on the shared NYC.gov "Livesite" chassis that Parks, DOE, NYCHA, and most agencies use. It runs its **own** nginx/Ubuntu box — and that box was serving 502s to every request throughout the assessment. A self-run origin with no visible edge/CDN is both a resilience risk and the reason there is no content API.

## Worst Landlord Watchlist (landlordwatchlist.com) — the important part

The office's one modern, data-backed product is **not** on advocate.nyc.gov at all:

| Property | Value | Evidence |
|---|---|---|
| Framework | **Next.js / React** | `__NEXT_DATA__` script, `/_next/...` chunks, `buildId` |
| Hosting / CDN | **Vercel** | `server: Vercel`, `x-vercel-cache: HIT`, `x-vercel-id: iad1::…` |
| Canonical host | `www.landlordwatchlist.com` (308 from apex) | redirect headers |
| Data endpoint | **`/api/landlords`** (undocumented) | `200 application/json`, `{ results: [ …99 landlords… ] }` |

There **is** a real API here — but it is **undocumented**: no OpenAPI, no versioning, no docs page (`/methodology`, `/faq`, `/data` all 404). It is a Next.js data route, not a governed contract. See [apis-observed.md](apis-observed.md).

## Open Data footprint

**Zero.** No NYC Open Data asset carries a Public Advocate agency label. Verified via the Socrata Discovery API against `data.cityofnewyork.us` for `Public Advocate (PA)`, `Office of the Public Advocate`, `Public Advocate`, and `Office of the Public Advocate (PA)` — all returned **0** — and a `q=advocate` scan surfaced only CFB, NYCC, CCRB, DOE, DOP, and OCC. See [opendata-pubadvocate.md](opendata-pubadvocate.md).

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open (24 datasets), service layer locked in a vendor CRM → *unlock*.
- **Public Advocate** = **zero open data, a self-hosted main site that was down, one undocumented orphan API, and no intake surface** → **respond** — give the ombudsman an owned API to take and answer the public.

## Modernization implications

1. **The office is barely machine-readable.** No Open Data, a fragile self-run site, and its best product on a disconnected PaaS with an undocumented endpoint. There is almost nothing for an agent or an integrator to call.
2. **Consolidate the office's own output.** The Watchlist, sponsored legislation (today in Council's Legistar), reports (today PDFs on a 502ing site), and public interest demands belong behind one owned, documented contract ([OpenAPI](openapi/pubadvocate.yaml)).
3. **Give the ombudsman an intake API.** The core function — "help me with a city agency" — has no machine-readable way to file or track a case. An owned write surface plus an agent-native contract ([MCP artifact](mcp/pubadvocate-mcp.json)) is the low-hanging fruit.
