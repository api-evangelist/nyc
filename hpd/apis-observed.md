# APIs Observed While Crawling — HPD

Backend/service APIs the HPD surfaces call or expose, surfaced during the crawl (2026-07-13). HPD is distinctive: an **owned, modern backend REST API already exists** (`mspwvw-hpdleov3.nyc.gov/hpdonline.api/1.0/api`) — but it is **private and undocumented**, serving only the HPD Online Angular SPA. The public machine-readable surface is 47 flattened Open Data datasets, and the transactional lottery (Housing Connect) has no public API at all. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`mspwvw-hpdleov3.nyc.gov/hpdonline.api/1.0/api`** | Backend REST API | **NYC HPD** | **No — private/undocumented** | The live HPD record (buildings, violations, complaints, registrations, litigation, charges, bedbug, vacate orders). Owned `.nyc.gov` host, versioned `/1.0`. Hard-coded as `apiBaseURL` in the HPD Online `main.js`; not published or agent-native. |
| `mspwvw-hpdleov3.nyc.gov/DocService/v1/api` | Document service API | NYC HPD | No — private | `documentApiBaseURL`; serves NOV/order PDFs via `/documents/content`. |
| `*.hpdnyc.org:8243` | API gateway | NYC HPD (**WSO2 API Manager**) | Vendor/internal | Port 8243 = WSO2 gateway default; whitelisted in the SPA's CSP `connect-src`. HPD already runs API-management infrastructure internally. |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata/Tyler) | **Yes** | **47 HPD datasets** — violations, complaints, registrations, litigation, affordable-housing production, Local Law 44. Flattened periodic snapshots (see [opendata-hpd.md](opendata-hpd.md)). |
| `geosearch.planninglabs.nyc/v2` | Geocoding API | NYC Planning Labs (Pelias) | Yes (open) | Address autocomplete → BBL/BIN/coordinates; used by HPD Online for property lookup. |
| `hpdgis-enterprise.hpdnyc.org/HPDMap4` | Map service (ArcGIS/Esri) | NYC HPD | Vendor/internal | Enterprise GIS map referenced by the SPA. |
| `housingconnect.nyc.gov/PublicWeb` | Lottery portal (ASP.NET SPA) | NYC HPD/HDC | HTML only — **no public API** | NYC Housing Connect 2; affordable-housing applications are UI-only. Read-only Open Data twins exist (`nibs-na6y`, `vy5i-a666`) but the transaction is closed. |
| `www.googletagmanager.com` | Analytics | Google | Vendor | GA4 `G-GYRKWPJBCL`. |

## Takeaways

- **The API problem here is not absence — it's exposure.** Unlike Council (three fragmented APIs) or DOE (rented search), HPD has already **built a modern, owned, versioned REST API behind a WSO2 gateway** — it just serves one Angular app privately, with no public contract.
- **Two descriptions of the same data.** The private `hpdonline.api` (live) and the 47 Open Data snapshots (batch) cover the same buildings/violations/complaints with the same keys — but a developer or agent sees only the flattened snapshots.
- **The transactional surface is a closed silo.** Applying to an affordable-housing lottery on Housing Connect — the highest-value citizen workflow HPD owns — has no API.
- **No agent-native surface anywhere.** The [OpenAPI](openapi/hpd.yaml) + [MCP artifact](mcp/hpd-mcp.json) here propose exposing the existing backend as one documented contract and adding the net-new lottery-application write.
