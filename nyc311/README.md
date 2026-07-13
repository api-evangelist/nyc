# NYC311 — Low-Hanging Fruit Assessment

Fifth domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of **NYC311** (`portal.311.nyc.gov`) — the citizen-services front door, and the one domain with an **open standard already made for it**.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index.
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (Dynamics 365, Azure, the api.nyc.gov gateway).
- [apis-observed.md](apis-observed.md) — the flagship SODA dataset, the api.nyc.gov gateway, and the **retired Open311** endpoints.
- [crosswalk.md](crosswalk.md) — fruit ↔ Open Data ↔ **Open311**, incl. a field-by-field `erm2-nwe9` → Open311 `request` mapping.
- [opendata-311.md](opendata-311.md) / [opendata-311.json](opendata-311.json) — the 15-dataset 311 family.
- [schemas/](schemas/) — Open311-aligned JSON Schema per object: `service-request` · `service-type` · `service-definition` · `agency` (+ shared `_common`).
- [openapi/nyc-311.yaml](openapi/nyc-311.yaml) — OpenAPI 3.1 reviving **Open311 GeoReport v2** (services, definitions, requests) on the existing api.nyc.gov gateway.
- [mcp/nyc-311-mcp.json](mcp/nyc-311-mcp.json) — design-first MCP server definition (6 agent tools; artifact, not a deployment).

## What was found — the fifth (and cleanest) pattern

- **Fifth distinct platform: Microsoft Dynamics 365** — the city's front door is a vendor CRM.
- **The 311 data is the most-used in the city** — `311 Service Requests` (`erm2-nwe9`): **1.26M views / 590k downloads**, live SODA, tens of millions of records.
- **The interactive service API is retired** — NYC was an early **Open311 (GeoReport v2)** adopter; the endpoints no longer resolve. The open standard exists; NYC ran it and let it lapse.
- **A real API gateway exists** (`api.nyc.gov`, Azure APIM) but is scoped to **GeoClient** geocoding and key-gated — not 311.
- **Five-for-five on the universal gap** — submitting/tracking a request has no public API.

**Reframe — the fifth verb: Standardize.** Unlike the others, NYC311 doesn't need an API invented — **Open311 already defines it**. The work is to **revive the open standard** for the flagship civic service and host it on the gateway that already exists.

| Domain | The gap | Verb |
|---|---|---|
| Parks | resource API over existing data | Replatform |
| DOE | ownership of rented/hidden capabilities | Reclaim |
| Council | one owned contract over three APIs | Consolidate & Own |
| Elections | machine-readable data at all | Digitize |
| **NYC311** | **revival of the open standard it had** | **Standardize** |

## Reverse-engineered entities

`ServiceRequest` · `ServiceType` · `ServiceDefinition` · `Agency` — aligned to **Open311 GeoReport v2**, not invented. The `erm2-nwe9` extension fields (`community_board`, `council_district`, `bbl`, `borough`) are the recurring [geography spine](../SYNTHESIS.md) again — more evidence for the planned [`nyc-commons`](../ROADMAP.md) shared schemas.

## Method & caveats

Outside-in crawl (browser UA, robots-respecting). Portal is Dynamics 365; Open311 endpoints probed and found retired; `api.nyc.gov` probed (401, GeoClient). Open Data checked under the 311 dataset family (agency OTI). A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (15 datasets) + Open311 mapping ✅ · JSON Schemas (5) ✅ · OpenAPI 3.1 / Open311 (6 paths/7 ops) ✅ · MCP artifact (6 tools) ✅.
- **Next:** a reference implementation of `POST /requests` on `api.nyc.gov`; and factor the recurring geography fields into [`nyc-commons`](../ROADMAP.md).
