# Technology & Vendor Inventory — Queens Public Library (QPL)

What Queens Public Library's public surfaces are built on and which third parties they depend on — fingerprinted from response headers, host probes, and URL schemes during the crawl (2026-07-13). QPL is an **independent nonprofit**, and its distinguishing trait is that it is **composed almost entirely of packaged SaaS vendors**: a Drupal site out front, and the catalog, events, digital lending, and help all rented from different companies — none federated under an owned QPL API.

## The front doors

| Surface | URL | Vendor | What it does |
|---|---|---|---|
| Informational site | `www.queenslibrary.org/` | **Drupal** (behind **F5 BIG-IP**) | About, locations, hours, help, calendar embed — content only |
| **Catalog** | **`queenslibrary.bibliocommons.com`** | **BiblioCommons** | Search the collection; the patron account, **holds**, checkouts, and **card** |
| **Events** | **`queens.libnet.info`** / `connect.queenslibrary.org` | **Communico** | Programs calendar; registration |
| **Digital lending** | `queenslibrary.overdrive.com` (+ Axis 360, hoopla) | **OverDrive/Libby**, Axis 360, hoopla | eBooks, eAudiobooks, eMagazines, streaming |
| Help / FAQ / chat | `qpl.libanswers.com` | **Springshare** (LibAnswers) | Knowledge base + chat |

## Informational site (queenslibrary.org)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CMS platform | **Drupal** (inferred) | `taxonomy/term/<id>` URL scheme; `/core/` and `/help/...` node paths |
| WAF / edge | **F5 BIG-IP ASM** | `Set-Cookie: TS<hex>` on the homepage; content paths return an F5 `<title>Request Rejected</title>` "support ID" interstitial |
| Security headers | `X-Frame-Options: SAMEORIGIN`, `X-XSS-Protection`, `X-Content-Type-Options: nosniff` | response headers |

The WAF is notable: a **polite, browser-UA crawl of content pages is actively rejected**. The site both lacks a public API and resists machine access — the opposite of the "data-as-HTML" pattern seen in earlier domains.

## The vendor platforms — the important part

QPL's actual services are **not** on queenslibrary.org. Each is a separate packaged product on its own host:

| Vendor | Host | Product | Evidence | Owns |
|---|---|---|---|---|
| **BiblioCommons** | `queenslibrary.bibliocommons.com` | Catalog / discovery + patron account | `x-version: nerf15 9.35.0`; `/v2/search` route; `select_library` redirect | Catalog, **holds**, checkouts, **card** |
| **Communico** | `queens.libnet.info`, `connect.queenslibrary.org` | Events / programs | `Server: Communico` | Events, registration, room booking |
| **OverDrive / Libby** | `queenslibrary.overdrive.com` | Digital lending | 200 OK OverDrive catalog | eBooks / eAudio / eMagazines |
| **Axis 360**, **hoopla** | (vendor hosts) | Digital lending | QPL help pages / OverDrive listings | Additional digital silos |
| **Springshare** | `qpl.libanswers.com` | LibAnswers / LibGuides | `x-backend-server: libanswers-us-7.springyaws.com` | Help / FAQ / chat |

Each vendor exposes **its own** API, RSS, or widgets. But there is **no owned QPL API, no owned OpenAPI, no unified JSON** across them. A patron's card works at BiblioCommons and (via the same barcode) at OverDrive — but a developer or agent has no single QPL contract to call.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = data open, service layer locked in a vendor CRM → *unlock*.
- **QPL** = an independent nonprofit whose **every patron surface is a different vendor SaaS silo**, only the branch directory is open, and the site itself is WAF-locked → **federate.**

## Modernization implications

1. **The problem is fragmentation, not a hidden backend.** QPL's catalog, events, and digital titles are all machine-readable *somewhere* — just in five different vendor systems with five different models, logins, and APIs.
2. **Federate the silos behind one owned API.** A QPL API ([OpenAPI](openapi/queenslibrary.yaml)) should present branches (open data), catalog (BiblioCommons), events (Communico), and digital collections (OverDrive/Axis 360/hoopla) as one coherent resource model — and expose the patron write workflows (**placing a hold**, applying for a **card**) that today live only behind a BiblioCommons login.
3. **Depending on a stack of vendors with no owned surface is a governance and continuity risk.** An agent-native contract in front of it ([MCP artifact](mcp/queenslibrary-mcp.json)) is the low-hanging fruit — and, because Queens, Brooklyn, and NYPL are three separate systems, a *shared* NYC library API is the larger opportunity.
