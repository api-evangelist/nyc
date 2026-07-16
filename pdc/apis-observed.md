# APIs Observed While Crawling — PDC

Backend/service APIs the PDC surfaces call or expose, surfaced during the crawl (2026-07-16). The finding: **PDC exposes no API of its own.** Its only machine-readable data is three NYC Open Data datasets (Socrata SODA) — better than a truly thin agency, and including one rich 43-column art inventory — but the meeting calendar/agendas, commissioners, and awards are HTML/PDF only, and the core transaction (submitting a project for design review) is a **manual PDF form emailed by a City agency liaison**, with no portal and no upload API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | The **3** PDC-attributed datasets: Monthly Design Review (`tfrc-rjtr`, 10c, current), Annual Report (`5fsv-ze7v`, 12c), and the Outdoor Public Art Inventory (`2pg3-gcaa`, 43c, frozen since 2021). Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable PDC data surface. |
| **Project submission** (email + PDF) | Manual intake | PDC | **No — not a system** | A signed PDF application form + category checklist emailed by the City agency's PDC liaison by the 12:00pm deadline; hard copies delivered to City Hall. No portal, no upload API, no machine-readable submission. |
| `www.nyc.gov/site/designcommission/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — About, Design Review, Publications, Awards, Archive. No content API. Akamai edge, nginx, Dynatrace RUM, AWS ALB. Bot UA → `403` (AkamaiGHost); browser UA → `200`. |
| `a836-acris.nyc.gov` (ACRIS) | Property records | NYC DOF | Public | Linked from the site so applicants can confirm which agency has jurisdiction over a parcel. Not PDC-owned. |
| YouTube / MS Teams | Video / conferencing | Google / Microsoft | Vendor | Meetings are livestreamed on YouTube and held/attended remotely via Teams. Not data surfaces. |

## Takeaways

- **PDC has no owned API — of any kind.** Not for projects, not for meetings/agendas, not for the collection, not for submissions. The only open data is three Socrata datasets.
- **The read is decent but lopsided.** The review log is kept current and the art inventory is genuinely rich (43 columns, with artist/architect credits, material, inscription, Block/Lot, lat/long) — but the inventory is frozen at 2021, and the calendar, agendas, minutes, commissioners, and awards are published only as HTML/PDF.
- **The write is not even a system.** Submitting a project for design review — PDC's core function — is a manual PDF application form emailed by an agency liaison, with paper hard copies delivered afterward. There is no portal (unlike LPC's Salesforce Portico) and no API.
- **No citizen surface at all.** PDC is agency-facing — only a City agency with jurisdiction over the property may submit; an artist or community works *through* the sponsoring agency. There is no citizen service or citizen write; the honest net-new write is **agency design-review submission** (B2G).
- **No agent-native surface.** The [OpenAPI](openapi/pdc.yaml) + [MCP artifact](mcp/pdc-mcp.json) here propose one owned contract that surfaces the review record, collection, commissioners, and awards *and* digitizes the manual submission with the net-new `submit_design_review` write workflow.
