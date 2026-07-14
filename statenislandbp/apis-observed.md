# APIs Observed While Crawling — Staten Island Borough President

Backend/service APIs the office's surface calls or exposes, surfaced during the crawl (2026-07-13). The finding is near-total absence: **the office exposes no API of its own, and its only machine-readable data is two trivial NYC Open Data assets it does not query itself.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | Just **2** BPSI assets: `3fes-huds` (BP Assist Helpline Requests — aggregate counts, ends FY20) and `mmut-uup9` (Category Master File — a zero-column blob). A SODA `/resource/<id>.json` endpoint exists for `3fes-huds`, but the office's site does not consume it. |
| **`weebly.com/weebly/apps/formSubmit.php`** | Form-relay endpoint | Weebly (Square) | Vendor | Where the Community Board Membership Application posts. Opaque `_u…` field names; not an API, not documented, not agent-usable. |
| `lp.constantcontactpages.com/su/wWLrBxD/sibp` | Email sign-up | Constant Contact | Vendor | Newsletter capture. |
| `statenislandusa.com/apps/search` | Site search | Weebly | Vendor | Weebly's built-in site search; no JSON contract. |
| Cloudflare edge | CDN | Cloudflare | Vendor | `cf-ray`, `__cf_bm`. |

## Takeaways

- **No owned API — and nothing to reverse-engineer.** Unlike NYCHA (a Siebel CRM) or DOE (a rented search backend), there is no hidden application here at all; it is a static Weebly site.
- **The one real dataset is an aggregate dead-end.** `BP Assist Helpline Requests` (`3fes-huds`) publishes annual complaint *counts* by request type and stops at FY20 — useful as a category vocabulary, useless for looking up or filing a request.
- **The charter work is invisible.** Land-use recommendations, community board appointments, discretionary funding, and borough board resolutions — the substance of the office — have no API and no Open Data twin; they exist only as PDFs and HTML.
- **No agent-native surface.** The [OpenAPI](openapi/statenislandbp.yaml) + [MCP artifact](mcp/statenislandbp-mcp.json) here propose the office's first machine-readable contract, and deliberately model it so it can **federate across all five borough-president offices** rather than being rebuilt five times.
