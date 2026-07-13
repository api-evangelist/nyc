# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (DSNY)

Maps the low-hanging fruit on **nyc.gov/site/dsny** to (a) the **existing first-party backend APIs** (the collection-schedule geocoder, the ePickups scheduling API, the CFC appointment API) and (b) the **51 DSNY datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-dsny.json](opendata-dsny.json).

## The reframe — fourth distinct pattern

- **Parks:** data-rich HTML, machine-readable twins on Open Data, legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** three APIs — a *vendor* legislative API (Legistar), an open WP REST API, Open Data — none owned or coherent → *consolidate + own.*
- **DSNY:** the lookup and scheduling APIs **already exist and are first-party** — but they're undocumented, unversioned, and hidden behind React forms → **expose + document.**

DSNY is the least about *building* or *reclaiming* an API and the most about **surfacing** one that already runs in production. A resident or agent who wants "when is my compost collected, and can you schedule a bulk pickup for my old couch?" is answered today only by a JavaScript form calling a private backend — never by a documented, agent-native contract.

Coverage: ✅ strong twin/API · 🟡 partial · ❌ gap.

## Entity crosswalk

| Entity | Website | First-party backend API | Open Data | Cov. |
|---|---|---|---|---|
| `CollectionSchedule` | collection-schedule form | **`geocoder/DSNYCollection`** (undocumented) | DSNY Frequencies (`rv63-53db`), DSNY Districts (`i6mn-amj2`) | 🟡 API hidden |
| `SanitationDistrict` | garage/district pages | `geocoder/BCW` (zones) | DSNY Districts, Zones (`ak2e-nbe8`), Frequencies, District Map (`uqhg-h4at`) | ✅ |
| `DropOffSite` | special-waste / recycling pages | `cfc/api/appointment` (special waste) | Electronics (`wshr-5vic`), Food Scrap (`if26-z6xq`), Special Waste (`242c-ru4i`), Recycling Bins (`sxx4-xhzg`), DonateNYC (`gkgs-za6m`) | ✅ |
| `LitterBasket` | sidewalks/gutters page | — | Litter Basket Inventory (`8znf-7b2c`, 19c), Litter Basket Map (`d6m8-cwh9`) | ✅ |
| `Tonnage` | what-we-do page | — | Monthly Tonnage (`ebb7-mvp5`, 58K views), Recycling Rates (`gaq9-z3hz`), Other Organics (`6yag-pnij`) | ✅ |
| Commercial waste zones | rate-calculator form | `geocoder/BCW` + ArcGIS | Commercial Waste Zones (`8ev8-jjxq`, `a7bv-5698`) | ✅ |
| `BulkPickupRequest` | collection-schedule form | **`ePickupsAPI/api/PickupRequest/AddUpdatePickUpRequest`** (undocumented) | — | 🟡 **net-new contract over existing backend** |
| `Complaint` (missed collection) | links to 311 | NYC 311 (separate system) | — | ❌ off-surface |
| `Violation` (enforcement) | illegal-dumping page | — | OATH/ECB, not a DSNY dataset | ❌ gap |

## The hidden-API problem, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Collection-schedule geocoder** | Live, first-party, authoritative address→schedule lookup | Undocumented; forms-only; 500s any client that doesn't send the exact params the React bundle does |
| **ePickups API** | Already schedules bulk/large-item pickups end-to-end | No docs, no OpenAPI, no versioning; the write capability is invisible to any developer or agent |
| **CFC appointment API** | Books special-waste drop-off appointments | Same — a private form backend |
| **Open Data (SODA)** | 51 open datasets, 356K views; rich geography | Flat exports disconnected from the live geocoder/scheduling APIs and from each other |

## Implications for the API-first + MCP proposal

1. **Expose and document the existing backends.** Publish one DSNY API ([OpenAPI](openapi/dsny.yaml)) that fronts the collection-schedule geocoder, the ePickups scheduling API, and the CFC appointment API as versioned, documented resources — instead of leaving them as reverse-engineerable form internals.
2. **Promote the write surface.** `AddUpdatePickUpRequest` already works; give it a first-class **`BulkPickupRequest`** resource (schedule a bulk / CFC-appliance / e-waste / special-waste pickup) with an owned contract.
3. **Join Open Data to the live geography.** Districts, frequencies, drop-off sites, litter baskets, and tonnage all describe the geography the geocoder resolves to — surface them behind the same resource model.
4. **Note the off-surface flows.** Missed-collection complaints (311) and enforcement violations (OATH/ECB) live in other systems — documented here as boundaries, not modeled.
5. **MCP server** so an agent can answer "when's my collection / where do I drop off electronics / schedule a bulk pickup for me" in one place.
