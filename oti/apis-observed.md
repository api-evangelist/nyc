# APIs Observed While Crawling — OTI

Backend/service APIs the OTI surfaces call, expose, or **operate for the whole city**, surfaced during the crawl (2026-07-13). The finding is the inverse of every earlier domain: **OTI does not lack APIs — it runs the city's APIs.** It operates the NYC Open Data platform, the api.nyc.gov gateway, and the 311 pipeline. What it lacks is one **owned, unified contract** over them and a **self-service** way in. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`api.nyc.gov`** (GeoClient `/geo/geoclient/v1`, GeoSearch, agency APIs) | **API gateway** | NYC **OTI** (on Microsoft **Azure API Management**) | **Key-gated** | The citywide gateway OTI operates. `Request-Context: appId` + `401 "missing subscription key"` fingerprint Azure APIM. Hosts GeoClient (address/BBL/BIN geocoding) and other agency APIs. **No owned catalog of services, no self-service key API** — a 401 and a developer portal. |
| **`geosearch.planninglabs.nyc/v2/search`** | Geocoding API | NYC (DCP Planning Labs; wraps OTI **GeoSupport**) | **Yes — open** | Open Pelias/Mapzen geocoder over the same GeoSupport engine — returns coordinates + the geography spine. HTTP 200, no key. The **open twin of GeoClient**. |
| **`data.cityofnewyork.us`** (SODA + Discovery) | Open Data API | NYC **OTI** (**Socrata** / Tyler) | **Yes — open** | The open-data platform OTI operates **for the whole city**. SODA `/resource/<id>.json` per dataset + the Socrata Discovery/catalog API. OTI itself publishes **221** datasets — including the catalog of the entire 2,300+ asset corpus, and 311 (the city's most-viewed dataset). |
| `www.nyc.gov/content/oti` | Informational site | NYC.gov shared platform ("Livesite" v22) | Public (HTML) | Content only — About OTI, services, initiatives. Akamai edge, nginx, mPulse + Dynatrace RUM. No content API. |
| `on1.nyc.gov` | Citywide account / SSO | NYC **OTI** | Login | NYC.gov ID / citywide identity — itself an OTI-run platform. |
| Akamai edge | CDN | Akamai | Vendor | `server-timing ak_p` / mPulse on the OTI site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is abundance, not absence.** OTI operates a full open-data platform (Socrata SODA + Discovery), a real API gateway (Azure APIM: GeoClient/GeoSearch), an identity platform (NYC.gov ID), and the 311 pipeline. It is the plumbing under most of the other NYC domains in this project.
- **But there is no OWNED, UNIFIED contract.** To discover a dataset you use Socrata's generic catalog API; to call the gateway you meet a 401 and a portal; there is no single OTI API that spans "find a dataset → find a gateway service → geocode → register an asset."
- **No self-service write.** The two operator writes — **register a dataset** and **request a gateway key** — are internal or portal-only. No `POST` exists for either.
- **No agent-native surface.** The [OpenAPI](openapi/oti.yaml) + [MCP artifact](mcp/oti-mcp.json) here propose one owned contract that unifies the catalog + gateway + geocoder OTI already runs and adds the two net-new writes — the shape that would let an agent (or any of the other NYC domains) treat OTI as the citywide platform product it already is.
