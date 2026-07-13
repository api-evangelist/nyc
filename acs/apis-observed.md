# APIs Observed While Crawling — ACS

Backend/service APIs the ACS surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is a near-absence: **ACS has exactly one machine-readable API surface — a single Socrata SODA dataset (the Community Partners directory) — while its aggregate reports are static files and its public actions are delegated to the NY State Central Register and NYC 311.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Partly** | 21 ACS assets, but only **5 are queryable tabular datasets** and **1 is address-level** (Community Partners, `9hyh-zkx9`). The rest are `file` attachments with no SODA columns. The one genuinely useful ACS API surface. |
| **`ocfs.ny.gov` — Statewide Central Register (SCR)** | Statutory hotline / State case system | **NY State OCFS** (CONNECTIONS) | Phone (1-800-342-3720); no public API | Where **reporting child abuse/neglect** actually goes. Not an ACS system and not machine-readable — deliberately human-mediated. |
| **`portal.311.nyc.gov`** | Citywide service-request intake | NYC 311 | Public UI; no ACS-owned API | Where **child care / provider complaints** and other ACS-adjacent requests are filed. ACS defers to 311 rather than owning an intake. |
| `www.nyc.gov/site/acs/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, child welfare, youth justice, child care. No content API. |
| `maps.googleapis.com` | Maps JS API | Google | Vendor | Client-side program/locator maps on child-care and child-welfare pages. |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is near-absence, not a hidden backend.** ACS exposes one useful dataset via SODA; there is no secret transactional API to reveal, because the transactions belong to the State (SCR) or 311.
- **Most "datasets" are files.** 16 of 21 Open Data assets are uploaded report attachments (`columns = 0`) — not queryable. The aggregate accountability corpus is publish-as-PDF/Excel, not publish-as-data.
- **No case data, by statute.** Abuse investigations, foster-care placements, and detention are published only in aggregate; individual children, families, and cases are never exposed — correctly.
- **No agent-native surface.** The [OpenAPI](openapi/acs.yaml) + [MCP artifact](mcp/acs-mcp.json) here propose one owned contract that publishes the provider directory and the aggregate reports cleanly *and* insources the net-new `report_child_care_concern` write workflow ACS delegates today to 311 — while routing any suspected abuse to 1-800-342-3720.
