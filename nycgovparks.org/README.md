# nycgovparks.org — Low-Hanging Fruit Assessment

An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the NYC Department of Parks & Recreation web domain — the first domain profiled for the [NYC Modernization](../README.md) research. Same method used for the [University of Oklahoma](https://apievangelist.com/2014/10/12/an-outsidein-approach-to-jumpstarting-an-api-effort-at-the-university-of-oklahoma/) and the [Department of Veterans Affairs](https://skylight-hq.github.io/va-api-landscape/report/): if it's already published to the website as a table, list, form, or file, it should also be an API.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) — human-readable index of every table, listing, form, database, and file found (name, type, entity, URL, confirmed row counts, Open Data coverage).
- [fruit.json](fruit.json) — machine-readable index, enriched with `confirmed_rows`, `website_columns`, and `opendata_match`.
- [crosswalk.md](crosswalk.md) — **fruit ↔ NYC Open Data mapping** with per-resource coverage verdicts; the analytical centerpiece.
- [opendata-parks.md](opendata-parks.md) / [opendata-parks.json](opendata-parks.json) — index of all **237 DPR Open Data assets** (147 datasets, 51 maps, 36 links) with full column schemas.
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (nginx + CloudFront, legacy Smarty/PHP + jQuery, Cloudinary, the Next.js Tree Map island).
- [apis-observed.md](apis-observed.md) — backend/service APIs the site calls (Tree Map internal API, self-hosted `/search`, legacy `.php`, Cloudinary, Notify NYC, Socrata SODA).
- [schemas/](schemas/) — individual JSON Schema per object (`park` · `facility` · `capital-project` · `event` · `monument` · `tree` · `permit-application` + shared `_common`), reconciling website columns with Open Data column schemas.
- [openapi/nyc-parks.yaml](openapi/nyc-parks.yaml) — OpenAPI 3.1 contract that `$ref`s each object schema; reads over unified Open Data + the net-new permit-application write API.
- [mcp/nyc-parks-mcp.json](mcp/nyc-parks-mcp.json) — design-first MCP server definition: 15 agent tools whose input/output `$ref` the object schemas and map to the OpenAPI operations. See [mcp/README.md](mcp/README.md). (Artifact, not a deployment.)

## What was found

NYC Parks runs a **data-rich** domain: ~1,700 parks, ~42 citywide facility directories (row counts up to 1,275), a 535-row Capital Project Tracker, a faceted events calendar, a thousands-strong Historical Signs database, and a ~650k-record Tree Map. All public; on the domain, almost none is machine-readable.

But the confirmation pass added the decisive twist: **the machine-readable twins already exist** on NYC Open Data — **237 DPR assets** (147 datasets, 51 maps, 36 export links), covering **27 of the ~40 fruit resources**, including literal "Directory of Basketball Courts / Tennis Courts / Dog Runs / Recreation Centers / Playgrounds / Pools." The website just never links to or consumes them.

**The findings that make the case:**

1. **Zero machine-readable downloads on the domain** — all HTML tables, div listings, and PDFs.
2. **The twins exist on Open Data, unlinked** — two parallel worlds, separately maintained, free to drift.
3. **No unified API or MCP** — Open Data gives raw per-dataset SODA endpoints, but there is no resource-oriented Parks API (Park → facilities → events → capital projects) and no agent-native surface.
4. **Narrow, specific gaps** — ~12 facility types (Bocce, Horseback, Fishing, Barbecue, Historic Houses, Nature Centers, Media Labs, Pickleball, WiFi, Zoo…), the Rules, and **all permit *applications*** (login-gated; Open Data has only permit *areas* + granted logs).
5. **Supporting evidence of neglect** — the declared `sitemap.xml` returns the 404 page; legacy `.php` backends leak into URLs; no developer/open-data page exists on the domain.

**Reframe:** this is an **integration + API-productization** problem, not a data-liberation one. Unify the existing Open Data behind one Parks API + MCP, close the ~12 gaps, and build the missing permit-application API. See [crosswalk.md](crosswalk.md).

## Method & caveats

Bounded outside-in crawl with a browser user-agent, respecting `robots.txt` (`crawler4j` fully disallowed; admin/`/xml/` paths avoided), fetching section landing pages plus a representative sample of listing/form/database pages and analyzing markup for tables (>10 rows), record listings, forms, and file links. This is a **sample, not a full spider** — verified counts are marked in the index; the remaining facility/permit pages still need a per-page confirmation pass. No authenticated or disallowed content was accessed; requests were paced.

## Reverse-engineered entities

`Park` · `Facility` (≈42 subtypes) · `CapitalProject` · `Event` · `HistoricalSign`/`Monument` · `Tree` · `PermitApplication` (≈10 subtypes) · `Rule` · `Program` · `Concession` · `NewsItem`

These become the resource model for the API-first + MCP proposal.

## Status & next

- **Done (2026-07-13):** IA mapped; fruit index + entities; **confirmation pass** (facility row counts, column model, permit login-gating); **Open Data cross-reference** (237 DPR assets, 27 matched, 11 gaps); **JSON Schemas** for 7 objects + shared defs; **OpenAPI 3.1** contract `$ref`ing every object (15 paths, 17 operations); **MCP design artifact** (15 agent tools mapped to the OpenAPI ops). Full design-first artifact set: objects → API → agent surface.
- **Next:** (1) close the ~12 facility gaps + Rules by defining their schemas/endpoints; (2) an example implementation wiring the read endpoints to the existing SODA/Open Data sources; (3) move to the second domain from [../domains.md](../domains.md).
