# Crosswalk — Website Fruit ↔ NYC Open Data

Maps every low-hanging-fruit resource found on **nycgovparks.org** to its existing machine-readable dataset(s) on **NYC Open Data** (`data.cityofnewyork.us`), attributed to Department of Parks and Recreation (DPR). Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-parks.json](opendata-parks.json).

## The reframe

The first-pass finding was "data everywhere, machine-readable nowhere." The Open Data index flips it: **most of the website's data already exists as machine-readable Open Data** — DPR publishes 147 datasets, 51 maps, and 36 "Directory of X" export links. NYC Parks even publishes a **Directory of Basketball Courts**, **Directory of Tennis Courts**, **Directory of Dog Runs**, **Directory of Recreation Centers**, **Directory of Playgrounds**, and **Directory of Indoor/Outdoor Swimming Pools** — the exact machine-readable twins of the website's facility directories.

So the problem isn't missing data. It's three things:

1. **Disconnection** — the website renders its own separate HTML and **never links to or consumes** the Open Data twin. Two parallel worlds, maintained separately, that can drift.
2. **No product API/MCP** — Open Data gives you raw SODA endpoints per dataset, but there is **no unified, resource-oriented Parks API** (Park → its facilities → its events → its capital projects) and **no agent-native (MCP) surface**.
3. **Real gaps remain** — a set of facility types and all **permit *applications*** (write/workflow) have **no** Open Data equivalent.

Coverage legend: ✅ strong twin · 🟡 partial/related · ❌ no Open Data equivalent (true gap).

## Core entities

| Website fruit | Site cols/rows | Open Data match (id) | OD cols | Coverage |
|---|---|---|---|---|
| **Park** directory `/parks` | 1,700+ | [Parks Properties](https://data.cityofnewyork.us/d/enfh-gkve) `enfh-gkve`; [OpenData_ParksProperties](https://data.cityofnewyork.us/d/ghu2-eden) `ghu2-eden` | 33 / 36 | ✅ |
| **CapitalProject** tracker | 535 rows · Project/Location/Phase | [Capital Project Tracker](https://data.cityofnewyork.us/d/4hcv-tc5r) `4hcv-tc5r` (+ href `qiwj-i2jk`) | 29 | ✅ |
| **Event** calendar `/events` | borough/date/category facets | [NYC Parks Events Listing – Event Listing](https://data.cityofnewyork.us/d/fudw-fgrp) `fudw-fgrp` + Locations/Categories/Images/Organizers/Links; [Upcoming 14 Days](https://data.cityofnewyork.us/d/w3wp-dpdi) `w3wp-dpdi` | 15 (+related) | ✅ (normalized set) |
| **HistoricalSign / Monument** DB | thousands (legacy `.php`) | [NYC Parks Monuments](https://data.cityofnewyork.us/d/6rrm-vxj9) `6rrm-vxj9`; [Parks Signs](https://data.cityofnewyork.us) | 34 | ✅ |
| **Tree** map (subdomain) | ~650k | [2015 Street Tree Census – Tree Data](https://data.cityofnewyork.us/d/uvpi-gqnh) `uvpi-gqnh` (45 col, 140k views); [Forestry Tree Points](https://data.cityofnewyork.us/d/hn5i-inap) `hn5i-inap`; 2005/1995 census | 45 / 20 | ✅ (richest twin) |
| **Rule** `/rules` | HTML + PDF | — | — | ❌ |

## Facility subtypes (`/facilities/<type>`)

| Website facility | Rows (confirmed) | Open Data match | Coverage |
|---|---|---|---|
| Tennis | 116 | [Directory of Tennis Courts](https://data.cityofnewyork.us/d/dies-sqgi) `dies-sqgi`; [Athletic Facilities](https://data.cityofnewyork.us/d/qnem-b8re) `qnem-b8re` (45col) | ✅ |
| Basketball | 582 | [Directory of Basketball Courts](https://data.cityofnewyork.us/d/b937-zdky) `b937-zdky` | ✅ |
| Handball | 552 | Athletic Facilities `qnem-b8re` | 🟡 |
| Baseball | 249 | Athletic Facilities; [Synthetic Turf Fields](https://data.cityofnewyork.us); Natural Turf Site List | 🟡 |
| Soccer | 405 | Athletic Facilities; Synthetic/Natural Turf | 🟡 |
| Football | 60 | Athletic Facilities | 🟡 |
| Cricket | 20 | Athletic Facilities | 🟡 |
| Fitness Equipment | 192 | [Parks Closure … Adult Exercise Equipment](https://data.cityofnewyork.us) (partial) | 🟡 |
| Running Tracks | 41 | Athletic Facilities | 🟡 |
| Volleyball | 49 | Athletic Facilities | 🟡 |
| Dog Areas | citywide | [Directory of Dog Runs & Off-Leash Areas](https://data.cityofnewyork.us/d/ipbu-mtcs) `ipbu-mtcs`; [Dog Runs](https://data.cityofnewyork.us/d/hxx3-bwgv) `hxx3-bwgv` | ✅ |
| Outdoor Pools | 11 | [NYC Parks Pools](https://data.cityofnewyork.us/d/y5rm-wagw) `y5rm-wagw`; [Directory of Outdoor Swimming Pools](https://data.cityofnewyork.us/d/fx7a-24mf) `fx7a-24mf` | ✅ |
| Indoor Pools | — | [Directory of Indoor Swimming Pools](https://data.cityofnewyork.us/d/x57r-az25) `x57r-az25` | ✅ |
| Recreation Centers | 73 | [Directory of Recreation Centers](https://data.cityofnewyork.us/d/ydj7-rk56) `ydj7-rk56`; Active & Passive Recreation | ✅ |
| Playgrounds | — | [Directory of Playgrounds](https://data.cityofnewyork.us/d/59gn-q4ai) `59gn-q4ai`; [DPR_PlayAreas_001](https://data.cityofnewyork.us/d/at6q-ktig) `at6q-ktig` | ✅ |
| Restrooms | 1,275 | [Directory Of Toilets In Public Parks](https://data.cityofnewyork.us/d/hjae-yuav) `hjae-yuav` | ✅ |
| Spray Showers | 594 | [NYC Parks Spray Showers](https://data.cityofnewyork.us); Cool It! NYC Spray Showers | ✅ |
| Water Fountains | (404 on site) | [NYC Parks Drinking Fountains](https://data.cityofnewyork.us); Cool It! NYC Drinking Fountains | ✅ |
| Beaches | div-listing | [Beaches](https://data.cityofnewyork.us); DPR_Beaches_001 | ✅ |
| Golf | 16 | [Golf Courses](https://data.cityofnewyork.us); DPR_GolfCourses_001 | ✅ |
| Skate Parks | div-listing | [NYC Parks SkateParks](https://data.cityofnewyork.us) | ✅ |
| Model Aircraft | div-listing | DPR_ModelAircraftFields_001 | ✅ |
| Ice Skating | 11 | IceSkatingRinks_20190417 | ✅ |
| Kayak/Canoe | 27 | KayakCanoeLaunch_20190417 | ✅ |
| Great Trees | 124 | 2015 Street Tree Census (partial) | 🟡 |
| Bocce | 41 | — | ❌ |
| Hockey | 24 | Athletic Facilities (partial) | 🟡 |
| Horseback | 12 | — | ❌ |
| Fishing | 33 | — | ❌ |
| Hiking Trails | div-listing | [Parks Trails](https://data.cityofnewyork.us) (partial) | 🟡 |
| Bikeways/Greenways | div-listing | [Greenstreets](https://data.cityofnewyork.us) (partial) | 🟡 |
| Barbecue | 78 | — | ❌ |
| Food/Concessions | div-listing | [Parks Concessions](https://data.cityofnewyork.us) | ✅ |
| Historic Houses | div-listing | — | ❌ |
| Nature Centers | div-listing | — | ❌ |
| Media Labs | div-listing | — | ❌ |
| Pickleball | div-listing | — | ❌ |
| WiFi | 205 | — | ❌ |
| Zoo | div-listing | — | ❌ |

## Permits / applications

| Website form | Open Data match | Coverage |
|---|---|---|
| Field & Court, Tennis, Film/Photo, Metal Detector, Summer Camp, Boating, Farmers Market, Construction (all **login-gated application forms**) | [Parks Permit Areas](https://data.cityofnewyork.us/d/c5vm-g2dk) `c5vm-g2dk` = permit *areas*, not applications | ❌ (no application API) |
| Research permit | [Research Permits](https://data.cityofnewyork.us/d/nnf6-km2a) `nnf6-km2a` (log of granted permits) | 🟡 |
| Construction/interagency | [Interagency Coordination & Construction Permits (MOSYS)](https://data.cityofnewyork.us/d/wye7-nyek) `wye7-nyek` | 🟡 |

**Permitting is the clearest net-new opportunity:** the website has ~10 permit workflows behind a login, Open Data only exposes granted-permit logs and permittable areas — there is **no read/write permit API**.

## Bonus: operational datasets with no website surface at all

DPR also publishes rich **operational** data that never appears on the public site — inverse low-hanging fruit (data without a web face): Parks Inspection Program (18 datasets), Asset Management Parks System / AMPS (5), Forestry Work Orders/Inspections/Service Requests, Daily Tasks cleaning records, Syringe disposal data, Programming attendance (Swim for Life, Kids in Motion, Summer Sports). These argue for the same unified API to serve internal + public consumers.

## Coverage tally

- **✅ Strong Open Data twin:** ~22 of ~40 facility types + all 5 core non-permit entities.
- **🟡 Partial / rolled-up:** athletic field/court types (folded into one *Athletic Facilities* dataset rather than per-sport), trails/greenways, great trees.
- **❌ True gaps (on website, not in Open Data):** Bocce, Horseback, Fishing, Barbecue, Historic Houses, Nature Centers, Media Labs, Pickleball, WiFi, Zoo, **Rules**, and **all permit applications**.

## Implications for the API-first + MCP proposal

1. **Don't re-liberate data — unify and productize it.** Wrap the existing DPR Open Data assets in one resource-oriented Parks API (`/parks/{id}`, `/parks/{id}/facilities`, `/parks/{id}/events`, `/trees`, `/monuments`, `/capital-projects`) and have the website consume that API instead of maintaining parallel HTML.
2. **Close the ❌ gaps** by publishing the ~12 missing facility directories + Rules as datasets/endpoints (they already exist as HTML tables — trivial to harvest).
3. **Build the permit application API** (read: statuses/areas; write: submit/track) — the one place with no machine-readable surface and the highest citizen value.
4. **MCP server** exposes the same resources as agent tools (`find_park`, `list_facilities`, `find_events`, `check_permit_status`), turning a fragmented site into an agent-native civic service.
