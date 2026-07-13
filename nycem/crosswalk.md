# Crosswalk — Website/Feed Fruit ↔ APIs ↔ NYC Open Data (NYCEM)

Maps the low-hanging fruit on **nyc.gov/site/em** and **Notify NYC** to (a) the **existing APIs** (the Everbridge CAP RSS feed; Socrata SODA) and (b) the **13 NYCEM datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-nycem.json](opendata-nycem.json).

## The reframe — a rented alert stream

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data open, resident transactions locked in a vendor CRM → *unlock.*
- **FDNY:** incident data open, business transactions trapped in a rented Accela cloud → *front.*
- **NYCEM:** reference data open **and** the alert stream already machine-readable — but the **feed and the subscription both live on a rented Everbridge platform** → **syndicate** the stream through an owned contract and add the subscribe write.

NYCEM is the first domain here whose flagship product is *already* a machine-readable feed. The Notify NYC CAP RSS feed is real and multilingual. But it is Everbridge's, not the city's — read-only, unversioned, and with no companion write API. A resident or agent asking "subscribe me to alerts for my address" has nothing to call.

Coverage: ✅ strong open twin · 🟡 partial/snapshot · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Feed | API today | Open Data | Cov. |
|---|---|---|---|---|
| `EmergencyNotification` | Notify NYC | **Everbridge CAP RSS** (read) + SODA | NYCEM Emergency Notifications (`8vv7-7wx3`, 5c) | 🟡 read-only, rented |
| `HurricaneEvacuationZone` | Know Your Zone | SODA | Hurricane Inundation by Evacuation Zone (`uk9f-6y9n`); map (`2234-9r2y`) | ✅ |
| `EvacuationCenter` | center finder | SODA | Hurricane Evacuation Centers (`p5md-weyf`, 15c); map (`ayer-cga7`) | ✅ (live status ❌) |
| `EmergencyIncident` | — | SODA | Emergency Response Incidents (`pasr-j7fb`, 7c) | ✅ |
| `MitigationAction` | Hazard Mitigation Plan | SODA | Mitigation Actions Database (`veqt-eu3t`, 28c) + `t7k8-wj6b`/`cj2p-e3ej`/`hqhh-iv7p` | ✅ |
| `PreparednessResource` | Ready NY / CERT | SODA | CERT (`b2gb-nkrq`); Ready NY Events (`hyur-qpyf`, 18c); Partners (`h4jn-x3ty`) | ✅ |
| **`NotifyNYCSubscription`** (subscribe) | Notify NYC portal | **Everbridge UI / SMS / 311 only** | — | ❌ **net-new** |
| Open cooling center (live status) | Finder map | **Finder UI only** | — | ❌ gap |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Everbridge CAP RSS feed** | Real-time, machine-readable, multilingual, standards-based (CAP) | Rented / vendor-owned; read-only; unversioned; no subscription write; no owned SLA |
| **Socrata SODA (13 datasets)** | Open, machine-readable; strong on incidents, evacuation zones/centers, hazard mitigation, preparedness | Reference & situational snapshots; nothing about live activation status or resident enrollment |
| **Everbridge Member Portal** | The real subscription system — channels, locations, categories | Web UI / SMS / phone only; no API, no OpenAPI, no JSON; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Republish the alert stream and the open data as one clean, owned resource model.** Notifications, evacuation zones/centers, incidents, mitigation actions, and preparedness resources behind one owned NYCEM contract ([OpenAPI](openapi/nycem.yaml)) — so consumers learn one model, not a vendor RSS URL plus 13 Socrata IDs.
2. **Own the distribution.** Front the Everbridge feed with a city-owned API so the alert stream has a versioned, machine-readable contract the city controls.
3. **Add the one net-new write workflow** — `subscribe_notify_nyc` (create a `NotifyNYCSubscription`) with channels, locations, categories, and coastal-storm evacuation-zone alerts on by default.
4. **Expose live status.** A follow-on should surface which cooling / evacuation centers are open now, replacing the seasonal Finder map.
5. **MCP server** so an agent can answer "what is my evacuation zone?", "what emergency alerts are active for Brooklyn?", and — the point — "subscribe me to Notify NYC for my home and work addresses."
