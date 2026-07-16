# moer — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **NYC Mayor's Office of Environmental Remediation (MOER/OER)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (environmental/cleanup sites, (E)-designations, VCP cleanup projects, OER determinations, remediation status, and the net-new Notice-to-Proceed request write).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" site + the public SPEED map on CARTO/Leaflet + OER's login-walled EPIC portal on ASP.NET/AngularJS).
- [apis-observed.md](apis-observed.md) — the **open data surface** (Socrata SODA over 10 datasets) + SPEED (CARTO, not an API) vs. the workflow trapped in EPIC and the DCP-owned (E)-designation inventory — and no OER API.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (10 OER datasets + 3 DCP E-Designation assets) with coverage verdicts.
- [opendata-moer.md](opendata-moer.md) / [opendata-moer.json](opendata-moer.json) — all 10 OER Open Data assets + column schemas (plus the related DCP E-Designation assets), sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `environmental-site` · `e-designation` · `cleanup-project` (VCP) · `notice-to-proceed` · `remediation-status` · `notice-to-proceed-request` (net-new write) (+ shared `_common`). BBL/geography `$ref`'d from [nyc-commons](../nyc-commons/).
- [openapi/moer.yaml](openapi/moer.yaml) — OpenAPI 3.1 contract `$ref`ing each object, with `getRemediationStatus` and the net-new `requestNoticeToProceed`.
- [mcp/moer-mcp.json](mcp/moer-mcp.json) — design-first MCP server definition (10 agent tools; artifact, not a deployment).

## What was found

OER **inverts the DDC data problem**:

1. **The data is open — and even live.** OER publishes **10** Open Data datasets, led by **OER Cleanup Sites** (`3279-pp7v`) updated **Daily** with a full BBL/BIN geography spine, and it runs a genuinely useful public **SPEED** map (Searchable Property Environmental E-Designation). The rows are good.
2. **But nothing is exposed as an API.** SPEED is a CARTO/Leaflet **map app** over a JSONP feed, not a documented API, and there is no OER-branded REST surface at all.
3. **The whole regulatory workflow is trapped in EPIC.** OER *owns* its project portal (`a002-epic.nyc.gov`) — but it is a login-walled ASP.NET/AngularJS system with no API, so the OER Remedial Process, the determinations (Notice to Proceed, Notice of Satisfaction, Notice of No Objection), live status, and the intake are all invisible to machines.
4. **The authoritative (E) inventory isn't OER's.** The most-demanded environmental record — whether a parcel carries an (E)-designation — is published under the **DCP** label (`hxm3-23vy`, `mzjp-98aw`, `jsrs-ggnx`).

**The gap here is exposure, not data.** A developer or agent asking "does this Brooklyn lot carry an E, is its cleanup cleared for a building permit, and how do I request a Notice to Proceed?" has open data for the first clause, a DCP dataset for the second, and **no API at all** for the workflow.

**Reframe (vs. DDC):**

| | **DDC** | **OER** |
|---|---|---|
| Platform | NYC.gov Livesite + citywide PASSPort/MOCS, City Record, Checkbook | NYC.gov Livesite + public SPEED map (CARTO) + OER-owned EPIC portal (ASP.NET/AngularJS) |
| Core problem | data thin & historical, transactions on systems DDC doesn't own | data open & partly live, but no API — the workflow is trapped in an owned-but-locked legacy portal |
| Modernization verb | **surface** | **expose** |

## Reverse-engineered entities

`EnvironmentalSite` · `EDesignation` (DCP-published, OER-resolved) · `CleanupProject` (VCP) · `NoticeToProceed` · `RemediationStatus` (`getRemediationStatus`) · `NoticeToProceedRequest` (net-new B2G write; `requestNoticeToProceed`) — join keys **BBL** (nyc-commons) and **OER Project Number**.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov` returns Akamai `403` to non-browser agents). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, AWS ALB, Dynatrace, Webtrends); **SPEED** was fingerprinted from markup (CARTO cartodb.js v3.15 + Leaflet, Google Cloud, JSONP feed); **EPIC** from headers (Microsoft-IIS/10.0, ASP.NET 4.0) and its AngularJS bootstrap. Open Data agency label verified via the Socrata Discovery API; all 10 OER assets pulled with columns, and the E-Designation assets confirmed as **DCP**-owned. A sample, not a full spider; the EPIC portal's internal workflow is inferred from OER's documented Remedial Process pages, not scraped behind login. There is **no general citizen write** in this domain — the net-new write is honestly B2G (owner/developer requesting a Notice to Proceed / VCP enrollment).

## Status & next

- **Done (2026-07-16):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (10 datasets) ✅ · JSON Schemas (6 + common) ✅ · OpenAPI 3.1 (11 paths/ops) ✅ · MCP artifact (10 tools) ✅.
- **Next:** an example implementation fronting EPIC for `requestNoticeToProceed` and `getRemediationStatus`; then the next domain from [../domains.md](../domains.md).
