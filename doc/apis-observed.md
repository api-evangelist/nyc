# APIs Observed While Crawling — DOC

Backend/service APIs the DOC surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is asymmetric: **DOC's accountability data has a real, open API (Socrata SODA over 15 datasets), and it runs a live person-in-custody lookup — but that lookup is a legacy JavaServer Faces app with no API, and every public transaction has none at all.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 15 DOC datasets: daily in-custody population, admissions/discharges, deaths, slashings/stabbings, fights, assaults on staff, staff injuries, emergency lock-ins, Local Law 33/85 indicators, staffing, Hart Island burials. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable DOC API. |
| **`a073-ils-web.nyc.gov/inmatelookup`** | Live person-in-custody lookup ("P.I.C. Lookup") | DOC (Apache **MyFaces / JSF**) | Public UI; **no API** | Real-time search by NYSID / Book & Case number / name. Server-rendered JavaServer Faces (`javax.faces.ViewState`, `myfaces`), WebSphere-style `JSESSIONID`, postback-driven, JavaScript-only. No JSON/OpenAPI surface. |
| `www.nyc.gov/site/doc/` | Informational site | NYC.gov shared platform ("Livesite" v22) | Public (HTML) | Content only — About, facilities, inmate-info, visiting rules, forms. No content API. |
| `a860-openrecords.nyc.gov` | Citywide records-request portal | NYC (OpenRecords) | Web form | FOIL / records requests are routed here; no DOC-specific API or status contract. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is a mismatch, not an absence.** Accountability/statistics data is generously open through Socrata SODA, and a real-time custody lookup already exists — but the lookup is a closed legacy JSF screen and the public transactions have no contract.
- **The live lookup has no API.** The "P.I.C. Lookup" is the obvious thing to front with an owned API: the search already runs, it just cannot be called by a system or an agent.
- **No write surface anywhere.** Scheduling a **visit** and filing a **complaint / records request** — the things the public actually needs to *do* — are phone/mail/in-person or vendor/OpenRecords portals, with no machine-readable contract or status.
- **Two disconnected views of the same person.** Open Data publishes an anonymized daily snapshot (`INMATEID` only); the live lookup returns a named record keyed on NYSID / Book & Case — neither is an API, and nothing joins them.
- **No agent-native surface.** The [OpenAPI](openapi/doc.yaml) + [MCP artifact](mcp/doc-mcp.json) here propose one owned contract that publishes the open accountability data and the live lookup cleanly *and* adds the net-new `schedule_visit` and `file_complaint` write workflows — with person-in-custody data treated as sensitive.
