# APIs Observed While Crawling — schools.nyc.gov

Backend/service APIs the site itself calls (or exposes) that surfaced during the crawl (2026-07-13). These are the *existing* programmatic surfaces — none is a public, documented, productized DOE data API, which is exactly the gap this project addresses. Machine-readable index: recorded in [fruit.json](fruit.json) under `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| `lusearchapi-na.hawksearch.com/sites/nycdoe` | Search API | **HawkSearch** (vendor) | No (vendor-keyed) | Powers "Find a School" and site search. Proprietary; not a DOE data API. |
| `nycdoe.tracking-na.hawksearch.com` | Analytics/tracking API | HawkSearch | No | Search click tracking. |
| `/CustomApi/*` (on `www.schools.nyc.gov`) | Internal REST | DOE (Sitefinity) | **No** — `Disallow` in robots.txt | Internal API the CMS/pages call for content & school data. Not documented or public. |
| `pwsblobprd.schools.nyc/prd-pws/*` | Blob/object storage REST | DOE (Azure) | Read (assets) | Serves images, logos, and document blobs. |
| `js.arcgis.com` + Esri services | Mapping API | Esri (vendor) | Vendor-keyed | School locator maps. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata/Tyler) | **Yes** | The one genuinely open API — per-dataset SODA endpoints for the 638 DOE assets. Not resource-oriented; not linked from the site. |
| `pwsauth.nycenet.edu` (NYC Schools Account) | Auth / OAuth | DOE | Login | Identity for parent/student/staff apps. |
| `www.googletagmanager.com` / gtag | Analytics API | Google | Vendor | Tag management. |

## Takeaways

- **A backend API already exists** (`/CustomApi/*`) — the pages are data-driven — but it is internal, undocumented, and robots-blocked. Modernization is partly *exposing and productizing what's already there*.
- **Discovery is rented** from HawkSearch; DOE does not own a school-search API it could offer to developers or agents.
- **The only public API is Socrata SODA**, per-dataset and disconnected from the site — the same disconnect found at [nycgovparks.org](../nycgovparks.org/).
- **No agent-native surface** and **no public school API** — the [OpenAPI](openapi/nyc-schools.yaml) + [MCP artifact](mcp/nyc-schools-mcp.json) here propose exactly that.
