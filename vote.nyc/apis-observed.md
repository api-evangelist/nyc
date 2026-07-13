# APIs Observed While Crawling — vote.nyc

Backend/service APIs the site calls or exposes, surfaced during the crawl (2026-07-13). The finding here is **near-absence**: vote.nyc exposes no site API and depends on two siloed apps plus PDFs. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| `vote.nyc/jsonapi` (Drupal JSON:API) | Would-be REST API | NYC BOE | **No — 404 (disabled)** | Drupal ships JSON:API but it is not enabled; the site has no content API. |
| `enr.boenyc.gov` (+ `/rcv/`) | Election Night Results viewer | NYC BOE | HTML app; no documented data API | Separate legacy results system on the old `boenyc.gov` domain. |
| `requestballot.vote.nyc` (+ `/tracking`) | Ballot request / tracking app | NYC BOE (vendor?) | Transactional app | Absentee/mail-ballot request + status tracking. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata/Tyler) | Yes | **Only 2 BOENY datasets** (Voting/Poll Sites, Election District Poll Sites). No results/candidates/contests. |
| `js-agent.newrelic.com` | Monitoring API | New Relic | Vendor | RUM telemetry. |
| `www.googletagmanager.com` | Analytics API | Google | Vendor | Tag management. |

## Takeaways

- **There is no BOE data API.** The Drupal JSON:API is disabled; the only machine-readable election data anywhere is two poll-site datasets on Open Data.
- **The two things voters most need at election time — who's running and what the results are — have no API and no dataset.** Candidates and contests are PDFs; results are PDFs plus a legacy viewer (`enr.boenyc.gov`).
- **The transactional workflow (ballot request/tracking) is a separate app** with no public API.
- This domain most sharply validates the project premise: *data liberation only partially worked* — at BOE, for the highest-stakes civic data, it barely happened. The [OpenAPI](openapi/nyc-elections.yaml) + [MCP artifact](mcp/nyc-elections-mcp.json) here propose the machine-readable election API that does not exist today.
