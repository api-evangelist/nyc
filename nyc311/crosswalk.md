# Crosswalk — Website Fruit ↔ Open Data ↔ Open311 (NYC311)

Maps the low-hanging fruit on **portal.311.nyc.gov** to the 311 datasets on **NYC Open Data** and to the **Open311 GeoReport v2** standard. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-311.json](opendata-311.json).

## The reframe — the fifth pattern

The other four domains needed an API *invented* (from HTML, PDFs, or three fragmented sources). NYC311 is different: **the standard and the data already exist.**

- The **data** is the most open in the city — `erm2-nwe9` (1.26M views, 590k downloads), live SODA, tens of millions of records.
- The **standard** — Open311 GeoReport v2 — precisely defines the 311 API, and **NYC already ran it** before letting it lapse.

So the verb is **Standardize**: re-adopt the open contract rather than design a bespoke one. This is the cleanest case in the project — the modernization is mostly *reconnection and revival*, not invention.

| Domain | What's missing | Verb |
|---|---|---|
| Parks | a resource API over existing data | Replatform |
| DOE | ownership of rented/hidden capabilities | Reclaim |
| Council | one owned contract over three APIs | Consolidate & Own |
| Elections | machine-readable data at all | Digitize |
| **311** | **revival of the open standard it already had** | **Standardize** |

## Entity crosswalk

| Entity | Open311 object | Open Data twin | Coverage |
|---|---|---|---|
| `ServiceRequest` | `request` (`GET /requests`, `GET /requests/{id}`) | `311 Service Requests` (`erm2-nwe9`, 48c) + historical | ✅ data · ❌ live API |
| `ServiceRequest` (submit) | `POST /requests` | — | ❌ **retired** (net-new/revive) |
| `ServiceType` | `service` (`GET /services`) | `311 Web Content - Services` (`vwpc-kje2`, 10c) | ✅ |
| `ServiceType` (SLA) | — | `311 Service Level Agreements` (`cs9t-e3x8`) | ✅ |
| `ServiceDefinition` | `service definition` (`GET /services/{code}`) | (derivable from descriptors) | 🟡 derive |
| `Agency` | — (NYC extension) | agency fields in `erm2-nwe9` | ✅ |
| experience metrics | — | satisfaction + call-center + interpreter datasets | ✅ |

## Field alignment — `erm2-nwe9` → Open311 `request`

The dataset already carries the Open311 request fields (plus NYC extensions):

| Open311 `request` | `erm2-nwe9` field |
|---|---|
| `service_request_id` | `unique_key` |
| `status` | `status` (Open/Closed) |
| `service_name` / `service_code` | `complaint_type` / `descriptor` |
| `description` | `descriptor` |
| `requested_datetime` | `created_date` |
| `updated_datetime` | `resolution_action_updated_date` |
| `expected_datetime` | `due_date` (via SLA) |
| `address` | `incident_address` / `street_name` |
| `lat` / `long` | `latitude` / `longitude` |
| `agency_responsible` | `agency` / `agency_name` |
| `status_notes` | `resolution_description` |
| *(NYC ext)* | `community_board`, `council_district`, `bbl`, `borough`, `open_data_channel_type` |

The last row is exactly the [shared geography spine](../SYNTHESIS.md) again — `community_board`, `council_district`, `bbl`, `borough` — reinforcing the case for `nyc-commons`.

## Implications for the API-first + MCP proposal

1. **Revive Open311, don't reinvent.** Publish a modern **Open311 GeoReport v2** contract (this project's [OpenAPI](openapi/nyc-311.yaml)) backed by the existing 311 system + the `erm2-nwe9` record.
2. **Host it on `api.nyc.gov`.** The Azure APIM gateway already exists (GeoClient) — extend it to serve the 311 surface rather than standing up new infrastructure.
3. **Ship the write path.** `POST /requests` (submit) + `GET /requests/{id}` (track) is the highest-value, and it's exactly the piece that lapsed.
4. **MCP server** so an agent can look up service types, **submit a 311 request**, and track it — turning the city's most-used dataset into an actionable, agent-native civic service.
