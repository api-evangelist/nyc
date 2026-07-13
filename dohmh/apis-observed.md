# APIs Observed While Crawling — nyc.gov/site/doh (DOHMH)

Backend/service APIs the DOHMH web properties call or expose, surfaced during the crawl (2026-07-13). DOHMH is unusual in the opposite direction from Council: its **read** data is thoroughly published (81 open Socrata datasets), but its **transactional** APIs are private, undocumented, or vendor-COTS — none is an owned, agent-native contract. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`a816-health.nyc.gov/ABCEatsRestaurants`** | Private Web API behind an AngularJS SPA | **DOHMH** (ASP.NET MVC 5.2 / IIS 10) | Undocumented | Public restaurant grade/inspection lookup. The SPA renders from an internal JSON API, but there is no documented, versioned contract — HTML5-routed paths fall back to the app shell. |
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC / Socrata (Tyler) | **Yes — open** | **81 DOHMH datasets**, incl. the famous Restaurant Inspection Results (`43nn-pn8j`), Rodent Inspection (`p937-wjvj`), Childcare Inspections (`dsg6-ifza`), Indoor Environmental Complaints (`9jgj-bmct`). Fully machine-readable. |
| **`a816-evital.nyc.gov/eVitalVRRTS`** | Transactional web app | DOHMH Office of Vital Records (ASP.NET MVC 5.2 / IIS 10) | App-only (session + CSRF gated) | Birth/death certificate request tracking. No API surface — anti-forgery token + server-rendered forms. |
| **`a816-hlst.nyc.gov/CitizenAccess`** | COTS permitting portal | **Accela** (IIS 8.5 / .NET) | App-only | Health permits & licenses. Vendor product; no open API exposed to the public. |
| `a816-health.nyc.gov/NYCHealthMap` | Facility finder | DOHMH | HTML/app | Clinic & service-site locator (redirects without params; likely ArcGIS/service backend). No documented API. |
| `portal.311.nyc.gov` | Service-request intake | NYC 311 (Salesforce) | HTML/app | Complaint intake routed to DOHMH; results surface on Open Data (`9jgj-bmct`). |
| `vitalchek.com` | Certificate ordering + payment | VitalChek (LexisNexis) | Vendor | Third-party online birth/death certificate ordering. |
| `maps.googleapis.com` | Maps API | Google | Vendor | Maps on DOH service pages. |
| Dynatrace RUM (`dtCookie`, `x-oneagent-js-injection`) | Monitoring | Dynatrace | Vendor | Real-user monitoring across NYC.gov + a816 apps. |

## Takeaways

- **The API problem here is transactions, not data.** Reads are solved twice over (open Socrata datasets *and*, for restaurants, a public SPA), while every **write/transaction** — order a certificate, apply for a permit — is a private .NET app or a vendor portal with no open contract.
- **The most famous dataset in the city is DOHMH's.** Restaurant Inspection Results (`43nn-pn8j`) is among the single most-viewed datasets in all of NYC Open Data, and it is fully open — reinforcing that the modernization gap is agent-native *service*, not data liberation.
- **No agent-native surface for doing anything.** The [OpenAPI](openapi/dohmh.yaml) + [MCP artifact](mcp/dohmh-mcp.json) here propose a single owned contract that fronts the open data for reads and adds the net-new **vital-record ordering** write workflow.
