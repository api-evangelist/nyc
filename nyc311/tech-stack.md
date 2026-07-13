# Technology & Vendor Inventory — NYC311 (portal.311.nyc.gov)

What NYC's 311 citizen-services front door runs on — fingerprinted from response headers and page markup during the crawl (2026-07-13). NYC311 is the **fifth distinct platform** in this project — and the first built entirely on a vendor SaaS.

## Platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Portal platform | **Microsoft Dynamics 365 / Power Apps Portals** | `Dynamics365PortalAnalytics` cookie; portal markup |
| Hosting | **Microsoft Azure App Service** | `ARRAffinity` cookies; `server-timing` correlationId |
| Caching | Azure edge (`WebPageCaching` cookie) | response headers |
| Analytics | Google Tag Manager | script ref |

The entire citizen-facing service — reporting a problem, checking status — is a **Microsoft Dynamics 365 CRM portal**. The city's front door for non-emergency services is a vendor CRM, not a custom application.

## The NYC API gateway (notable)

| System | Domain | Role |
|---|---|---|
| **NYC API gateway** | **`api.nyc.gov`** | A live **Azure API Management** gateway. `api.nyc.gov/geoclient/v2` returns **401** (key-gated) — it fronts **GeoClient** (address geocoding), not 311. This is the closest thing NYC has to a central API gateway (an open question flagged in [domains.md](../domains.md)) — but it is narrow and authenticated. |

## The open standard NYC walked away from

NYC was an early adopter of **Open311 (GeoReport v2)** — the open standard for 311 service requests. The historical endpoints (`311api.cityofnewyork.us`, `api.311.nyc.gov`) **no longer resolve**. The standard exists; the city let its implementation lapse. Meanwhile the *data* is published to Open Data at massive scale (see [crosswalk.md](crosswalk.md)) — so NYC kept the reporting feed and dropped the interactive standard.

## Contrast with the first four domains

| | Parks | DOE | Council | Elections | **311** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity | WordPress | Drupal 9 | **Dynamics 365 (SaaS)** |
| Open Data | 237 | 638 | 11 | 2 | **flagship (erm2-nwe9: 1.26M views)** |
| Core-data machine-readable | partial | partial | strong | none | **strongest** |
| Transactional API | none | none | none | none | **retired (Open311 lapsed)** |

## Modernization implications

1. **The data is the most open in the city; the service is the least owned.** 311 request *data* is a flagship open dataset, but the request *service* is a Microsoft CRM with no public API.
2. **Revive the open standard.** Unlike other domains, NYC311 doesn't need a bespoke API invented — **Open311 GeoReport v2 already defines it**, and NYC already ran it. The verb is **Standardize**: re-adopt the open contract for the flagship civic service.
3. **A real gateway exists** (`api.nyc.gov`) — extend it beyond GeoClient to host the Open311 surface, rather than standing up something new.
