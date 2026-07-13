# Technology & Vendor Inventory — vote.nyc

What the NYC Board of Elections (BOENY) website runs on — fingerprinted from response headers and page markup during the crawl (2026-07-13). BOE is the **fourth distinct platform** in this project and by far the least-modernized.

## Platform & hosting

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS | **Drupal 9** | `x-generator: Drupal 9`; `/sites/default/files/...` asset paths |
| CDN / edge | **Cloudflare** | `server: cloudflare` |
| Cache | **Varnish** | `via: varnish`, `x-cache: HIT` |
| Monitoring | **New Relic** | `js-agent.newrelic.com` |
| Analytics | **Google Tag Manager** | script ref |
| Fonts | Google Fonts | link ref |

## Separate systems (not on vote.nyc)

| System | Domain | Role |
|---|---|---|
| **Election Night Results (ENR)** | **`enr.boenyc.gov`** (+ `/rcv/` for ranked-choice) | The results viewer — a **separate legacy app** on the old `boenyc.gov` domain. Not integrated with vote.nyc; no documented data API. |
| **Ballot request / tracking** | **`requestballot.vote.nyc`** (+ `/tracking`) | Absentee / mail-ballot request and tracking — the one transactional workflow. |

## The defining characteristic: PDFs

Unlike the other three domains, vote.nyc's core content is distributed as **PDFs on the Drupal file system** (`/sites/default/files/pdf/...`):

- **Election results** — one PDF per contest (a "Recap" and an "EDLevel" file per race), foldered by election date.
- **Candidate lists, contest lists, petition filing calendars, random-draw ballot positions** — all PDF "important notices."

There is **no machine-readable feed** for any of this on the site.

## Contrast with the first three domains

| | Parks | DOE | Council | **BOE / vote.nyc** |
|---|---|---|---|---|
| Platform | Smarty/PHP | Sitefinity/.NET | WordPress | **Drupal 9** |
| Site API | none | hidden `/CustomApi` | open WP REST | **none (JSON:API off)** |
| Open Data | 237 assets | 638 assets | 11 assets | **2 assets (poll sites only)** |
| Core data format | HTML tables | JS + Excel | Legistar + OD | **PDFs + legacy viewer** |

## Modernization implications

1. **This is the original low-hanging-fruit case, essentially untouched.** The open-data era barely reached BOE — poll sites are the only machine-readable data; results, candidates, and contests are PDFs.
2. **Results need to be digitized before they can be productized.** The precondition here isn't unifying APIs (Council) or reclaiming a vendor (DOE) — it's **creating machine-readable election data at all** (parse the ENR system / result PDFs into a `ElectionResult` resource).
3. **Two disconnected apps** (ENR results, requestballot) should be first-class resources in one BOE API, not siloed systems.
4. **Highest civic stakes, lowest modernization** — the inverse of what election infrastructure should be.
