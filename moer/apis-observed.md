# APIs Observed While Crawling — MOER/OER

Backend/service APIs the OER surfaces call or expose, surfaced during the crawl (2026-07-16). The finding differs from DDC: OER's data **is** open — the **OER Cleanup Sites** dataset (Socrata SODA) is updated Daily and BBL-keyed — but there is **no OER-owned REST API**. The public **SPEED** map is a CARTO/Leaflet app, not a documented API, and the whole remedial workflow is trapped inside the login-walled **EPIC** portal (`a002-epic.nyc.gov`). Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | **10** OER-labeled datasets. The flagship **OER Cleanup Sites** (`3279-pp7v`) is updated **Daily** and carries a full BBL/BIN geography spine — the one strong, live OER data surface and the backing of SPEED. Plus Historic Land Use, Clean Soil Bank, and the BOA planning suite. Each has a SODA `/resource/<id>.json` endpoint. |
| **SPEED** (`speed.cityofnewyork.us`) | Public map app | OER (hosted on Google Cloud) | Public UI; **no documented API** | "Searchable Property Environmental E-Designation." A **CARTO (cartodb.js v3.15) + Leaflet** front-end; pulls a JSONP `/clientData.json?callback=__getData` feed carrying a CARTO `apiKey`. Useful to humans, but not an API an agent can call — it fronts a CARTO SQL backend, undocumented. |
| **EPIC** (`a002-epic.nyc.gov`) | Project portal | **OER** | Login-walled; **no API** | The Environmental Project Information Center — **Microsoft-IIS/10.0 + ASP.NET 4.0 + AngularJS**, authenticated. Where the remedial process, documents, and OER determinations (Notice to Proceed, Notice of Satisfaction) live. OER-owned, but no machine-readable surface. |
| `data.cityofnewyork.us` — **E-Designations** (`hxm3-23vy`, `mzjp-98aw`, `jsrs-ggnx`) | Open Data API | **DCP** (not OER) | Public | The authoritative (E)-designation inventory — **published under the Department of City Planning label**, updated Monthly. OER administers resolving the (E) requirement but does not own this data. |
| `www.nyc.gov/site/oer/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, Remediation, E-Designation, Safe Land, Community Grants. No content API. nginx, Akamai edge, AWS ALB, Dynatrace, Webtrends. |
| `a002-epic.nyc.gov` document repository | Document links | OER (EPIC) | Public per-site pages | OER Cleanup Sites rows carry a "Project-Specific Document Repository page" URL into EPIC — public documents, but no structured/API access. |

## Takeaways

- **OER has open data but no owned API.** The cleanup data is genuinely good — daily, BBL-keyed, publicly mapped via SPEED — yet it reaches consumers only as a Socrata dataset ID and a CARTO map. There is no OER-branded, versioned REST API.
- **The authoritative (E) inventory belongs to DCP.** The most-demanded environmental record — whether a parcel carries an (E)-designation — is published by City Planning, not OER, even though OER is the office that clears it.
- **The workflow is trapped in EPIC.** Unlike DDC, OER *owns* its transaction system — but EPIC is a login-walled .NET/AngularJS app with no API, so the remedial process, the determinations, and the intake are all invisible to machines.
- **No agent-native surface.** The [OpenAPI](openapi/moer.yaml) + [MCP artifact](mcp/moer-mcp.json) here propose one owned contract that exposes the environmental-site / (E)-designation / cleanup data live, answers `getRemediationStatus`, and adds the net-new `requestNoticeToProceed` write workflow.
