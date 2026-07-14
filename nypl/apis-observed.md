# APIs Observed While Crawling — NYPL

Backend/service APIs the NYPL surfaces call or expose, surfaced during the crawl (2026-07-13). The finding here is the opposite of every other domain: **NYPL already has real, mature, public APIs.** It is an independent nonprofit that built and open-sourced its own Digital Collections API, Locations API, and Research Catalog API. The only gaps are unification (three separate contracts) and one clean write surface (placing a hold). Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`api.repo.nypl.org/api/v2`** | Public REST API (token) | NYPL | **Yes — token-authenticated** | **Digital Collections API.** `items/search`, `items/{uuid}`, `items/mods/{uuid}`, `items/rights/{uuid}`, `collections`, `collections/{uuid}`. Returns `401 HTTP Basic: Access denied` without a registered token. Ruby on Rails + Phusion Passenger. Millions of digitized items, MODS metadata, captures, rights. |
| **`refinery.nypl.org/api/nypl/locations/v1.0`** | Public REST API (open, hypermedia) | NYPL | **Yes — open** | **Locations API.** `locations`, `locations/{id}`, plus HAL `_links` to `/events`, `/exhibitions`, `/alerts`, `/amenities`, `/blogs`. Rich: `hours_data`, `geolocation`, `access`, `contacts`, `fundraising`. PHP Slim (`NYPL\Refinery\Server`). Verified live. |
| **`github.com/NYPL/discovery-api`** | Open-source API + service | NYPL | **Yes — open source** | The primary API behind the **Research Catalog**. Node/AWS, backed by the Sierra ILS (`ruby-sierra-api-client`). |
| `github.com/NYPL` (org) | Open-source org | NYPL | **Yes — open source** | `nypl-design-system` (accessibility-first React), `web-reader` (ebooks), `nypl-core` (ontology), `on-site-hold-request-service`, `nypl-hold-request-consumer`, `patron-eligibility-service`, `dgx-patron-creator-service`, `nypl-library-card-app`, `barcode-service`. |
| `www.nypl.org` | Web app | NYPL (behind Imperva Incapsula) | Public (HTML) | Patron site + Research Catalog UI where holds are placed today, inside an authenticated account. Edge-obscured by Incapsula. |
| `data.cityofnewyork.us` (SODA) | Open data API | NYC (Socrata/Tyler) | Yes — open | Only 6 NYPL datasets, mostly stale 2010-2011 branch-services stats + a facilities layer. Not where NYPL's real data lives. |

## Takeaways

- **NYPL is the counter-example.** Most NYC domains in this project have zero owned APIs; NYPL has three good ones and open-sources the code behind them. The modernization verb is **lead**, not liberate.
- **The Digital Collections API is the flagship.** A token-authenticated, versioned Rails API over the entire digitized repository — search, MODS metadata, captures, and rights. Exactly the kind of API this project keeps wishing agencies had.
- **The Locations API is quietly excellent.** Open, hypermedia, self-describing, with hours, amenities, accessibility, and cross-links to events and exhibitions. It is genuinely agent-friendly already.
- **The one real gap is the write.** Placing a **hold** (reservation) runs on real internal services (`on-site-hold-request-service`, `patron-eligibility-service`, `nypl-hold-request-consumer`) but is reachable only through the patron's account UI — there is no clean, documented, agent-native public hold API. Library-card application is similar: a real open-source app (`nypl-library-card-app`), but a UI workflow, not a documented public write API.
- **The proposal is unification + agent-native packaging.** The [OpenAPI](openapi/nypl.yaml) + [MCP artifact](mcp/nypl-mcp.json) here fold NYPL's three good APIs into one resource model and add `place_hold` — turning an already-strong API footprint into a single agent-native contract.
