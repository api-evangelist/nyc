# APIs Observed While Crawling — IBO

Backend/service APIs the IBO surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is unusual: **IBO already has two real machine-readable APIs — an undocumented NYC.gov content API and Socrata SODA — but neither is offered as a documented, versioned, agent-native contract, and IBO's one citizen transaction (Ask IBO) has no API at all.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`apps.nyc.gov/content-api/v2/custom-contents/ibo`** | Content CMS API | NYC (OTI) — NYC.gov Content API v2 | **Public JSON, undocumented** | Backs the client-side site. Returns ~1,145 IBO publications with structured metadata (Title, Publication Date, Topics, Publication Type, Fiscal Year, Author) and a `/nav/ibo` tree. A genuine API, but no OpenAPI, no versioned consumer contract. |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 20 IBO datasets under agency label `NYC Independent Budget Office (IBO)`. Each has a SODA `/resource/<id>.json` endpoint. Fiscal time-series, mostly **wide** (one column per fiscal year). |
| `www.ibo.nyc.gov` | Informational SPA | NYC.gov Content API v2 platform | Public (HTML shell) | Client-side jQuery/Bootstrap SPA; every route serves the same 36 KB shell. Formerly `ibo.nyc.ny.us` (301-redirect). |
| `ibomap.maps.arcgis.com` | Mapping (ArcGIS Online) | Esri (vendor) | Embed | Map interactives (CSP `frame-src`). |
| `airtable.com` | Interactive data tables | Airtable (vendor) | Embed | Some IBO interactives are Airtable embeds — data outside IBO's own contract. |
| `e.infogram.com` | Chart embeds | Infogram (vendor) | Embed | Charts / infographics. |
| `cse.google.com` / `adsensecustomsearchads.com` | Site search | Google (vendor) | Embed | On-site search is a Google Custom Search Engine — search rented, not owned. |
| Dynatrace (ruxit) + WebTrends | RUM / analytics beacons | Dynatrace / WebTrends (vendors) | Vendor | `ruxitagentjs` injection + `webtrends_v10.js`. |

## Takeaways

- **The API story is "undocumented," not "absent."** IBO's publications already move as JSON through the NYC.gov Content API, and its bulk fiscal data is open on Socrata. What is missing is a documented, versioned, consumer-facing contract over either.
- **The datasets are Excel-shaped.** The Socrata tables are pivoted to one column per fiscal year (`FY 1980` … `FY 2020`); consuming them means reshaping a spreadsheet. The proposed [OpenAPI](openapi/ibo.yaml) republishes them long-form.
- **No API for the one citizen transaction.** IBO is a reference agency with no payments/permits/applications; its single interactive input — **Ask IBO** — is a web form / email to `info@ibo.nyc.gov` with no machine-readable surface. That is the net-new `createDataRequest` write.
- **No agent-native surface.** The [OpenAPI](openapi/ibo.yaml) + [MCP artifact](mcp/ibo-mcp.json) here propose one owned contract that formalizes the existing content API and datasets *and* adds the Ask IBO write workflow.
