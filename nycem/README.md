# nycem — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of **NYC Emergency Management (NYCEM / OEM)**, through the full design-first method: assessment → tech/vendor inventory → APIs-observed → Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (Notify NYC alerts, evacuation zones/centers, incidents, hazard mitigation, preparedness, and the locked subscription).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (NYC.gov "Livesite" + Akamai + Dynatrace; the **Everbridge** Notify NYC alerting platform).
- [apis-observed.md](apis-observed.md) — the **rented alert feed** (Everbridge CAP RSS) + Socrata SODA vs. the **Everbridge portal with no subscription API**.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ Open Data mapping (13 NYCEM datasets) with coverage verdicts.
- [opendata-nycem.md](opendata-nycem.md) / [opendata-nycem.json](opendata-nycem.json) — all 13 NYCEM Open Data assets + column schemas, sorted by page views.
- [schemas/](schemas/) — individual JSON Schema per object: `emergency-notification` · `hurricane-evacuation-zone` · `evacuation-center` · `emergency-incident` · `mitigation-action` · `preparedness-resource` · `notify-nyc-subscription` (+ shared `_common`).
- [openapi/nycem.yaml](openapi/nycem.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/nycem-mcp.json](mcp/nycem-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the sixth distinct pattern

NYCEM is a **rented-alerting domain**, and that is the finding:

1. **The alert stream is already machine-readable.** Notify NYC — the city's flagship emergency-alert product — emits a genuine **CAP (Common Alerting Protocol) RSS feed** on the rented **Everbridge** platform, republishing each alert across ~14 languages with a per-message CAP XML document.
2. **But it is rented, and the write side is locked.** The feed and the **subscription** both live on Everbridge (`a858-nycnotify.nyc.gov` / `feeds.everbridge.net`). There is no owned API contract, and **enrolling** in Notify NYC has no public write API — only the Everbridge Member Portal, an SMS keyword, or a call to 311.
3. **Reference and situational data is open.** 13 NYC Open Data datasets publish incidents (107k views), hurricane evacuation zones and centers, the Hazard Mitigation Plan, and community preparedness.

**The gap here is ownership and subscription, not raw data.** A resident or agent asking "subscribe me to alerts for my address" has nothing city-owned to call.

**Reframe (vs. the earlier domains):**

| | NYCHA | FDNY | **NYCEM** |
|---|---|---|---|
| Platform | NYC.gov Livesite + Oracle Siebel portal | NYC.gov Livesite + rented Accela cloud | **NYC.gov Livesite + rented Everbridge alerting** |
| Core problem | data open, service layer locked in a CRM | incident data open, transactions in rented SaaS | **data open + alert stream machine-readable, but feed & subscription rented** |
| Modernization verb | **unlock** | **front** | **syndicate** |

## Reverse-engineered entities

`EmergencyNotification` · `HurricaneEvacuationZone` · `EvacuationCenter` · `EmergencyIncident` · `MitigationAction` · `PreparednessResource` · `NotifyNYCSubscription` (net-new write) — join keys **Evac_Zone**, **BOROCODE**, **BBL/BIN**, community/council district.

## Method & caveats

Outside-in crawl (browser UA; `nyc.gov/robots.txt` only disallows `/html/misc/`). The informational site was fingerprinted from headers (Akamai, nginx, Livesite, Dynatrace); Notify NYC was identified as Everbridge from the CAP RSS feed's host and `<generator>` tag, and the subscription host's API probes were confirmed to 302-redirect without exposing a write endpoint. Open Data agency label verified via the Socrata Discovery API; all 13 assets pulled with columns. A sample, not a full spider; the Everbridge subscription workflow is inferred from NYCEM's documented enrollment options, not scraped behind login.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (13 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (9 paths/9 ops) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation fronting the Everbridge feed and adding `subscribe_notify_nyc`; then the next domain from [../domains.md](../domains.md).
