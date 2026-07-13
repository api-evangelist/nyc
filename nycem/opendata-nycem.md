# NYC Open Data — NYCEM Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "NYC Emergency Management (NYCEM)"** (verified via the Socrata Discovery API, 2026-07-13; the alternate label "Office of Emergency Management (OEM)" returned zero). 13 assets, sorted by lifetime page views. Machine-readable: [opendata-nycem.json](opendata-nycem.json).

The shape of the corpus tells the story: it is **incident-, evacuation-, and hazard-heavy** — one very high-traffic incidents feed, hurricane inundation/evacuation zones and centers, and a large Hazard Mitigation Plan with four companion tables — plus a Notify NYC notifications archive and community-preparedness programs. The **real-time alert stream is not here**; it lives in the rented Everbridge CAP RSS feed. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 107,030 | dataset | `pasr-j7fb` | Emergency Response Incidents | 7 |
| 15,037 | map | `ayer-cga7` | Hurricane Evacuation Centers (Map) | 0 |
| 14,456 | dataset | `8vv7-7wx3` | NYCEM Emergency Notifications | 5 |
| 4,450 | dataset | `uk9f-6y9n` | Hurricane Inundation by Evacuation Zone | 5 |
| 3,390 | dataset | `hyur-qpyf` | Ready NY Events | 18 |
| 2,476 | dataset | `b2gb-nkrq` | Community Emergency Response Team (CERT) | 5 |
| 2,342 | dataset | `veqt-eu3t` | Hazard Mitigation Plan - Mitigation Actions Database | 28 |
| 2,072 | map | `2234-9r2y` | Hurricane Inundation by Evacuation Zone (Map) | 0 |
| 2,045 | dataset | `p5md-weyf` | Hurricane Evacuation Centers | 15 |
| 1,547 | dataset | `h4jn-x3ty` | Partners in Preparedness | 1 |
| 1,480 | dataset | `t7k8-wj6b` | Hazard Mitigation Plan – Mitigation Actions Database (People) | 2 |
| 860 | dataset | `cj2p-e3ej` | Hazard Mitigation Plan - Mitigation Actions Database (Places) | 4 |
| 715 | dataset | `hqhh-iv7p` | Hazard Mitigation Plan - Mitigation Actions Database (Lifelines) | 3 |

## Groupings

- **Incidents:** Emergency Response Incidents (`pasr-j7fb`, 7c) — NYCEM's most-viewed asset.
- **Notify NYC (archive):** NYCEM Emergency Notifications (`8vv7-7wx3`, 5c) — the archived alert log; the live stream is the Everbridge CAP RSS feed.
- **Hurricane / coastal storm:** Hurricane Inundation by Evacuation Zone (`uk9f-6y9n`) + map (`2234-9r2y`); Hurricane Evacuation Centers (`p5md-weyf`, 15c) + map (`ayer-cga7`).
- **Hazard Mitigation Plan:** Mitigation Actions Database (`veqt-eu3t`, 28c) with People (`t7k8-wj6b`), Places (`cj2p-e3ej`), and Lifelines (`hqhh-iv7p`) companion tables.
- **Community preparedness:** CERT teams (`b2gb-nkrq`), Ready NY Events (`hyur-qpyf`, 18c), Partners in Preparedness (`h4jn-x3ty`).
