# APIs Observed While Crawling — NYPD

Backend/service APIs the NYPD's public surfaces call or expose, surfaced during the crawl (2026-07-13). NYPD's pattern is distinct: an enormous volume of data on **NYC Open Data (SODA)**, but the department's own interactive tools run on a **bespoke Angular application tier backed by an undocumented Azure Government API** — no owned, documented, agent-native NYPD API exists. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler Technologies) | **Yes — open** | **42 NYPD datasets** — complaints, arrests, shootings, summonses, use of force, officer profiles, sectors, NCO directory. Flattened periodic snapshots, not a live incident API. The de-facto NYPD data API today. |
| **`officer.search.azure.us`** | Officer-search backend API | NYPD (on **Azure Government**) | **Undocumented** | Powers the `nypdonline.org` Officer Profile app (names, shields, commands, arrests, **discipline history**). Referenced in the Angular bundle; no public contract, no docs, no agent surface. |
| `nypdonline.org` | Angular / Kendo SPA | NYPD | HTML/JS | Officer Profile + transparency app; consumes the Azure Gov backend client-side. |
| `compstat.nypdonline.org` | Angular / Kendo SPA (CompStat 2.0) | NYPD | HTML/JS | Interactive weekly crime stats by precinct; data rendered client-side, no documented API. |
| `nyc.gov/site/nypd` (Oracle WebCenter Sites) | CMS-rendered HTML | NYPD / NYC DoITT | HTML | Informational site (bureaus, precincts, careers, stats landing, publications). No content API. |
| Akamai edge | CDN | Akamai (vendor) | Vendor | Caching/edge for nyc.gov. |
| Dynatrace RUM | Monitoring beacon | Dynatrace (vendor) | Vendor | `x-oneagent-js-injection` on nyc.gov. |

## Takeaways

- **The problem here is not scarcity — it's exposure and shape.** NYPD has the *most* open data of any domain in the project, but it is published as periodic CSV/JSON snapshots on a third-party portal, not as a live, queryable, owned NYPD API.
- **The interactive record is app-trapped.** CompStat 2.0 and the Officer Profile discipline search hold real, current data behind Angular SPAs talking to an **undocumented Azure Government backend** (`officer.search.azure.us`) — reachable by a browser, not by an agent or an integrator.
- **No owned, documented, agent-native contract.** The [OpenAPI](openapi/nypd.yaml) + [MCP artifact](mcp/nypd-mcp.json) here propose one — consolidating the SODA snapshots and the app-trapped operational record, plus a net-new records/FOIL request workflow.
