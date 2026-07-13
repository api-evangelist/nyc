# Low-Hanging Fruit Index — NYCEM

**Agency:** NYC Emergency Management (NYCEM / OEM)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/em` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace) and the **Notify NYC** subscription host `a858-nycnotify.nyc.gov`. Probed Notify NYC and found a real machine-readable alert feed — the **Notify NYC CAP (Common Alerting Protocol) RSS feed** on the rented **Everbridge** platform (`feeds.everbridge.net/feeds/453003085617722/rss/rss.xml`), multilingual with per-message CAP XML. Verified the NYC Open Data agency label `NYC Emergency Management (NYCEM)` via the Socrata Discovery API (the alternate `Office of Emergency Management (OEM)` returned zero) and pulled all **13** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-nycem.md](opendata-nycem.md).

## Headline findings

1. **NYCEM is a rented-alerting domain.** An informational site on the shared NYC.gov chassis, and its flagship product — **Notify NYC** — running on a rented **Everbridge** mass-notification SaaS.
2. **The alert stream IS machine-readable — a first for this project.** Notify NYC emits a genuine **CAP RSS feed** on Everbridge, republishing each alert across ~14 languages with a per-message CAP XML document. But the feed — and the subscription — are **vendor-hosted, not an owned city API**.
3. **Reference and situational data is well published.** **13 NYC Open Data datasets** cover emergency response incidents (107k views), hurricane inundation/evacuation zones and centers, the Emergency Notifications archive, the Hazard Mitigation Plan, and community preparedness (CERT, Ready NY, Partners).
4. **The gap is the write side.** Enrolling in Notify NYC has no public API — a resident subscribes only through the Everbridge Member Portal, an SMS keyword, or a call to 311. Live cooling-center / shelter status is a seasonal Finder map only.

> **Reframe (sixth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* fragmented APIs; NYCHA = *unlock* a vendor CRM; FDNY = *front* a rented permitting cloud; **NYCEM = syndicate a rented alert stream.** Here the read is already machine-readable — the work is least about liberating datasets and most about **owning the distribution** (a versioned, city-controlled alert contract) and giving the **subscription** an owned, agent-native write API instead of a vendor portal form.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Notify NYC Emergency Alerts | `EmergencyNotification` | Everbridge CAP RSS + SODA | 🟡 archive (`8vv7-7wx3`); live feed rented |
| 2 | Hurricane Evacuation Zones | `HurricaneEvacuationZone` | SODA + finder | ✅ Inundation by Evacuation Zone (`uk9f-6y9n`) |
| 3 | Hurricane Evacuation Centers | `EvacuationCenter` | SODA + map | ✅ Evacuation Centers (`p5md-weyf`, 15c) |
| 4 | Emergency Response Incidents | `EmergencyIncident` | SODA | ✅ Incidents (`pasr-j7fb`, 7c) |
| 5 | Hazard Mitigation Plan Actions | `MitigationAction` | SODA (×4) | ✅ Mitigation Actions (`veqt-eu3t`, 28c) |
| 6 | Preparedness — CERT / Ready NY / Partners | `PreparednessResource` | SODA (×3) | ✅ CERT (`b2gb-nkrq`), Ready NY (`hyur-qpyf`) |
| 7 | **Subscribe to Notify NYC** | `NotifyNYCSubscription` | Everbridge portal + SMS + 311 | ❌ **net-new** |
| 8 | Find an open cooling center | `EvacuationCenter` | Finder map | ❌ gap (no live-status API) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Everbridge CAP RSS feed** — the one live, machine-readable NYCEM alert API; rented, read-only, no subscription write.
- **Socrata SODA** — 13 NYCEM datasets (open reference & situational data).
- **Everbridge Member Portal** (`a858-nycnotify.nyc.gov`) — the subscription system; web UI, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM).

## Reverse-engineered entities

`EmergencyNotification` (NotifyNYCMessage / EmergencyAlert) · `HurricaneEvacuationZone` · `EvacuationCenter` · `EmergencyIncident` · `MitigationAction` · `PreparednessResource` (CERT / Ready NY / Partners) · `NotifyNYCSubscription` (net-new write) — join keys: **Evac_Zone**, **BOROCODE**, **BBL/BIN**, community/council district.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Evac_Zone, BOROCODE, EC_Name, HMP Index) and the CAP feed fields — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open data + alert stream as clean resources + the net-new `POST /subscriptions` (subscribe to Notify NYC) — done ([openapi/nycem.yaml](openapi/nycem.yaml)).
3. **MCP** artifact: `find_notifications`, `get_notification`, `find_evacuation_zones`, `find_evacuation_centers`, `find_incidents`, `find_mitigation_actions`, `find_preparedness_resources`, `subscribe_notify_nyc`, `get_subscription` — done ([mcp/nycem-mcp.json](mcp/nycem-mcp.json)).
