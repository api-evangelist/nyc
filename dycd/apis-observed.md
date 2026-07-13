# APIs Observed While Crawling — DYCD

Backend/service APIs the DYCD surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is a mismatch: **DYCD's supply-side data has a real, open API (Socrata SODA over 15 datasets), and DYCD even built a public program finder (DiscoverDYCD) — but that finder's backend is a private, undocumented `/api/`, and there is no public API to apply to a program.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 15 DYCD datasets: program sites (34c, the richest), contracts, contractors/providers, Neighborhood Development Areas, aggregate participant demographics (52c), SYEP-for-NYCHA and RHY reporting. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DYCD API — supply-side data only. |
| **`discoverdycd.dycdconnect.nyc/api`** | Program-finder backend | DYCD (Angular SPA on **Microsoft-IIS**) | **Internal, undocumented** | The DiscoverDYCD finder is a hashed-bundle Angular app (`runtime/polyfills/main.*.js`, `<title>discoverDYCD</title>`) that calls a private `/api/` backend — every public probe returns `404`. No docs, no OpenAPI, no JSON a developer can call. Embeds Google Maps + Places. |
| **`www.dycdconnect.nyc`** | Provider / participant portal | DYCD (Microsoft-IIS) | Login-walled UI; **no API** | The DYCD Connect ecosystem where providers manage contracts and where program application/enrollment flows live. No public API. |
| `www.nyc.gov/site/dycd/` | Informational site | NYC.gov shared platform ("Livesite" v22) | Public (HTML) | Content only — About, services, provider resources. nginx origin behind Akamai edge, Dynatrace RUM, AWS ALB. No content API. |
| `maps.googleapis.com` | Maps / Places API | Google | Vendor | DiscoverDYCD embeds Google Maps JS + Places for site location and search. |
| Google Translate widget | i18n API | Google | Vendor | `translate.google.com/translate_a/element.js` on the finder. |

## Takeaways

- **The finder is a UI, not an API.** DYCD already solved "help the public find a program" with DiscoverDYCD — but the capability is locked behind a private `/api/` and an Angular screen. There is no documented, agent-callable program-finder API.
- **Supply data is generously open; the offering catalog is not.** Program sites, contracts, providers, and NDAs are all on Socrata SODA, but there is no clean Open Data catalog of the program *offerings* themselves — that lives only in the finder.
- **No API for the core transaction.** Applying to a DYCD program — SYEP, COMPASS, Beacon — has no machine-readable contract; it is reachable only through a seasonal online form or the DYCD Connect apps.
- **No individual participant data, by design.** Participant demographics are published only in aggregate; per-participant records live inside DYCD Connect and provider systems.
- **No agent-native surface.** The [OpenAPI](openapi/dycd.yaml) + [MCP artifact](mcp/dycd-mcp.json) here propose one owned contract that surfaces the finder and the open supply data cleanly *and* unlocks the net-new `apply_to_program` write workflow.
