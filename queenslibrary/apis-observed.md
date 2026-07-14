# APIs Observed While Crawling — Queens Public Library (QPL)

Backend/service APIs the QPL surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is one of **fragmentation**: QPL has exactly **one open dataset** (branches), and every other patron surface is a **separate vendor SaaS platform** with its own API — none of them an owned QPL contract. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us` (SODA)** | Open Data API | NYC (Socrata / Tyler) | **Yes — open** | Exactly **one** QPL dataset — Queens Library Branches (`kh3d-xhq7`, 21c) under agency `Queens Library (QBPL)`. A SODA `/resource/kh3d-xhq7.json` endpoint. The only open QPL data; branch directory only. |
| **`queenslibrary.bibliocommons.com`** | Catalog / discovery layer | **BiblioCommons** (vendor) | Public search UI; **login** for account | The catalog, patron account, **holds**, checkouts, and **card**. `x-version: nerf15 9.35.0`, `/v2/search` route. A BiblioCommons partner API + widgets/RSS exist, but there is **no owned QPL API**. |
| **`queens.libnet.info` / `connect.queenslibrary.org`** | Events platform | **Communico** (vendor) | Public UI + vendor API | `Server: Communico`. All programs/events, embedded on the queenslibrary.org calendar. Communico exposes a vendor API — not an owned QPL contract. |
| **`queenslibrary.overdrive.com`** (+ Axis 360, hoopla) | Digital lending | **OverDrive/Libby**, Axis 360, hoopla (vendors) | Public UI; **login** to borrow | eBooks/eAudio/eMagazines/streaming across **three separate silos**, each with its own catalog and vendor API. Not federated by QPL. |
| `qpl.libanswers.com` | FAQ / chat / help | **Springshare** (vendor) | Public | LibAnswers (`x-backend-server: libanswers-us-7.springyaws.com`). Vendor-owned help knowledge base. |
| `www.queenslibrary.org` | Informational site | QPL (**Drupal**, behind **F5 BIG-IP**) | Public HTML (**WAF-gated**) | Content only. The F5 WAF rejects browser-UA crawls of content pages. **No content API.** |

## Takeaways

- **The API story is fragmentation, not absence.** QPL's catalog, events, and digital titles *are* machine-readable — but in five different vendor systems, with five different models and logins, and **no owned QPL surface** binding them.
- **Only branches are open.** Because QPL is a nonprofit rather than a mayoral agency, its NYC Open Data footprint is a single dataset.
- **No API for the core transaction.** Placing and tracking a **hold** — the most common patron interaction — has no owned public contract; it lives only behind the BiblioCommons login. Applying for a **card** is likewise login-walled.
- **No agent-native surface.** The [OpenAPI](openapi/queenslibrary.yaml) + [MCP artifact](mcp/queenslibrary-mcp.json) here propose one owned contract that federates the open branch data and the vendor-locked catalog/events/digital surfaces *and* unlocks the net-new `place_hold` (and `apply_for_library_card`) write workflows.
- **Bigger opportunity: a shared NYC library API.** Queens (QPL), Brooklyn (BPL), and NYPL are three separate nonprofits with separate catalogs, cards, and vendor stacks. No shared API exists across them.
