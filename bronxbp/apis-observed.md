# APIs Observed While Crawling — Bronx Borough President

Backend/service APIs the Bronx Borough President surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is one of **near-absence**: the office exposes **no API of its own**, and only **two** of its entities are machine-readable at all — as NYC Open Data datasets. Everything else is a vendor widget or a server-rendered CMS page. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | Exactly **2** datasets under `Bronx Borough President (BPBX)`: **Capital Funding** (`mdgu-ar69`, 20c) and **Bronx Community Boards** (`wbau-xy7g`, 7c). SODA `/resource/<id>.json` endpoints. The only real, machine-readable Bronx BP surface. |
| **`bronxboropres.nyc.gov`** | Brochure website (Revize CMS) | Office of the Bronx BP (on **Revize** SaaS) | Public HTML; **no API** | PHP front end (`index.php`, `news_detail_T4_R<n>.php`, `calendar.php`), Revize `document_center` (ULURP PDFs) + `revize_calendar` plugins; JSP CMS admin at `cms2.revize.com/revize/security`. No JSON/OpenAPI. On Oracle Cloud (`129.153.208.86`). |
| Google Calendar (via `revize_calendar`) | Events feed | Google / office | Embedded | Two imported calendars — `Events` and `Meetings` — rendered by the Revize calendar plugin on `calendar.php`. Not an owned API. |
| `cdn.curator.io` | Social media aggregator | Curator.io (vendor) | Widget | Social wall embedded on the homepage. |
| `visitor.r20.constantcontact.com` | Newsletter / email signup | Constant Contact (vendor) | Widget | The "Subscribe for eNotifications" (`enotify`) flow. |
| `googletagmanager.com` (GA4 `G-DMD6JC0H5S`) · `userway.org` | Analytics / accessibility widgets | Google / UserWay (vendors) | Beacon / widget | GA4 analytics and the UserWay accessibility overlay. |

## Takeaways

- **The office has no API and almost no machine-readable data.** Two small Socrata datasets (funding, community-board appointments) are the entire structured footprint; both are essentially by-hand exports, not a live contract.
- **Its core charter work is unstructured.** ULURP land-use recommendations are PDFs in a document center; the newsroom is PHP pages; events are a borrowed Google Calendar. None has a feed, an API, or an Open Data twin.
- **No inbound surface.** The most natural constituent transaction — **applying to serve on a community board** — is a downloadable PDF or an email, with no confirmation and no status. That is the net-new write surface.
- **No agent-native surface.** The [OpenAPI](openapi/bronxbp.yaml) + [MCP artifact](mcp/bronxbp-mcp.json) here propose one owned contract that publishes the two open datasets cleanly, gives the recommendations/newsroom/events a machine-readable shape, and adds `apply_to_community_board` — and, because all five Borough Presidents share this exact shape, is written to be **templatized across the boroughs** rather than built once for the Bronx.
