# APIs Observed While Crawling — MOME

Backend/service APIs the MOME surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is an inversion: **MOME's flagship output has a real, open API (Socrata SODA over the famous Film Permits dataset), but the permit *application* has none** — it runs on a login-walled ASP.NET Core portal ("MOME E-Apply") with no documented API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | 2 MOME datasets. **Film Permits** (`tg4x-b46p`) is the flagship — one of the most-viewed datasets in the whole catalog (~530k views), automated, updated daily; every issued permit as a public record. **MARCH Inspections** (`b84a-xy2t`) via the Office of Nightlife. Each has a SODA `/resource/<id>.json` endpoint. This is the one real, machine-readable MOME API. |
| **`nyceventpermits.nyc.gov/film`** | Film-permit application portal | MOME (ASP.NET Core "E-Apply") | Login-walled UI; **no API** | Where productions apply for and track permits. `Microsoft-IIS/10.0`, `X-Powered-By: ASP.NET`, `.AspNetCore.Antiforgery` cookie, `/Web/Login` redirect, title `MOME E-Apply`. JavaScript (jQuery), no JSON/OpenAPI surface. Shared platform also serves CECM/DOT event permits. |
| `www.nyc.gov/site/mome/` | Informational site | NYC.gov shared platform ("Livesite") | Public (HTML) | Content only — permit instructions, programs, Public Access Media, Nightlife. No content API exposed. |
| `data.cityofnewyork.us` (DOT twin) | Open Data API | NYC DOT | Yes — open | `Filming Permits - Transportation Department` (`c2az-nhru`, ~90k views) — the same permits from DOT's street-work angle, **with the applicant contacts, fees, and lat/long MOME's own feed omits.** |
| Akamai edge | CDN API | Akamai | Vendor | `x-akamai-transformed` on the informational site. |
| Dynatrace RUM | Monitoring beacon | Dynatrace | Vendor | `x-oneagent-js-injection` real-user monitoring. |

## Takeaways

- **The API story is an inversion, not an absence.** The *output* of the permit workflow is generously open through Socrata SODA; the *application* that productions live in is a closed, login-walled ASP.NET portal.
- **No API for the core transaction.** Applying for a permit — the single most common MOME production interaction — has no machine-readable contract at all; it is reachable only via the E-Apply portal or an email.
- **The applicant is never published, by design.** Film Permits publishes the issued permit and its geography, never the production company; that identity lives only inside E-Apply (and partially on DOT's twin).
- **No agent-native surface.** The [OpenAPI](openapi/mome.yaml) + [MCP artifact](mcp/mome-mcp.json) here propose one owned contract that publishes the open output cleanly *and* unlocks the net-new `apply_for_film_permit` write workflow.
