# Low-Hanging Fruit Index — NYC311 (portal.311.nyc.gov)

**Agency:** NYC311 (Office of Technology and Innovation / 311)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, robots-respecting). Portal is Microsoft Dynamics 365; probed the Open311 GeoReport v2 endpoints (retired), the `api.nyc.gov` gateway (401, GeoClient only), and the 311 dataset family on NYC Open Data (agency OTI).

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-311.md](opendata-311.md).

## Headline findings

1. **Fifth distinct platform: Microsoft Dynamics 365** (Power Apps Portals on Azure). The city's non-emergency front door is a vendor CRM.
2. **The 311 data is the most-used in the city.** `311 Service Requests` (`erm2-nwe9`) has **1.26M views / 590k downloads** and a live SODA endpoint over tens of millions of records — one of the largest open datasets anywhere.
3. **The interactive service API is retired.** NYC was an early **Open311 (GeoReport v2)** adopter; the endpoints (`311api.cityofnewyork.us`) no longer resolve. The open standard exists — NYC ran it and let it lapse.
4. **A real API gateway exists** (`api.nyc.gov`, Azure APIM) but is scoped to **GeoClient** geocoding and key-gated (401) — not 311.
5. **Five-for-five on the universal gap:** submitting/tracking a 311 request has **no public API** — the same write-workflow gap as every other domain, sharper here because a standard for exactly this once ran.

> **Reframe (fifth distinct verb): Standardize.** Parks = replatform; DOE = reclaim; Council = consolidate & own; Elections = digitize; **311 = re-adopt the open standard.** 311 doesn't need a bespoke API invented — **Open311 already defines it** and NYC already implemented it. The work is to revive the standard contract for the flagship civic service and host it on the gateway that already exists.

## The fruit

| # | Name | Entity | Machine-readable? | Open Data / standard |
|---|---|---|---|---|
| 1 | 311 Service Requests | `ServiceRequest` | ✅ (data) | `erm2-nwe9` (48c) + historical — Open311 *request* |
| 2 | Report a Problem (submit) | `ServiceRequest` | ❌ (no write API) | Open311 `POST /requests` — **retired** |
| 3 | Service Catalog (types) | `ServiceType` | ✅ | `vwpc-kje2` — Open311 *services* |
| 4 | SLAs (by type) | `ServiceType` | ✅ | `cs9t-e3x8` |
| 5 | Responding Agencies | `Agency` | ✅ | agency fields in `erm2-nwe9` |
| 6 | Satisfaction / call-center | `ServiceRequest` | ✅ | surveys + call-center datasets |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — the flagship 311 dataset (live). **`api.nyc.gov`** — Azure APIM gateway (GeoClient, key-gated). **Open311 GeoReport v2** — retired. **Dynamics 365 Web API** — internal portal backend.
- Platform: **Microsoft Dynamics 365** on Azure. Fifth distinct platform; first full vendor-SaaS front door.

## Reverse-engineered entities

`ServiceRequest` · `ServiceType` · `ServiceDefinition` (Open311 attributes) · `Agency` — aligned to the **Open311 GeoReport v2** object model rather than invented.

## Next

1. **JSON Schema** per entity, aligned to Open311 (request/service/service-definition) and reconciled with the `erm2-nwe9` field set.
2. **OpenAPI** that revives Open311 GeoReport v2 (`GET /services`, `GET /services/{code}`, `POST /requests`, `GET /requests`, `GET /requests/{id}`, `GET /discovery`) as a modern, owned contract.
3. **MCP** artifact: `find_service_types`, `submit_service_request`, `check_request_status`, `find_service_requests`, `get_agency`.
