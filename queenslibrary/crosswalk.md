# Crosswalk — Website/Vendor Fruit ↔ APIs ↔ NYC Open Data (Queens Public Library)

Maps the low-hanging fruit on **queenslibrary.org** and its **vendor platforms** to (a) the **existing APIs** (Socrata SODA; the BiblioCommons / Communico / OverDrive vendor APIs) and (b) the **one** QPL dataset on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-queenslibrary.json](opendata-queenslibrary.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** the reference data is open, but every resident transaction is locked inside a vendor CRM → *unlock.*
- **Queens Public Library:** an **independent nonprofit** whose **every patron surface is a different vendor SaaS silo** — catalog (BiblioCommons), events (Communico), digital (OverDrive/Axis 360/hoopla), help (Springshare) — with only the **branch directory** open, and the site itself WAF-locked → **federate.**

QPL is the first *non-agency* domain. Because it is a nonprofit, not a mayoral agency, it publishes almost nothing to NYC Open Data — a single branch dataset. But it is far from data-poor: its catalog, events, and digital titles are all machine-readable *inside vendor systems*. The problem is that a patron, developer, or agent has **no single owned QPL contract** — to search everything, to place a hold, or to get a card — and the transactions they care about (holds, cards) are trapped behind a BiblioCommons login.

Coverage: ✅ strong open twin · 🟡 vendor API only (not owned/open) · ❌ gap (no API / login-walled).

## Entity crosswalk

| Entity | Website / Vendor | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Branch` | `/about-us/locations` + catalog selector | SODA | Queens Library Branches (`kh3d-xhq7`, 21c) | ✅ |
| `CatalogItem` | BiblioCommons catalog | BiblioCommons partner API / RSS (vendor) | — | 🟡 vendor |
| `Event` | `/calendar` (Communico) | Communico API (vendor) | — | 🟡 vendor |
| `DigitalCollection` | OverDrive/Libby, Axis 360, hoopla | OverDrive/Axis 360/hoopla APIs (vendor, siloed) | — | 🟡 vendor |
| `LibraryCard` | login-walled application | **BiblioCommons UI only** | — | ❌ gap |
| My account (holds/checkouts/fines) | BiblioCommons account | **BiblioCommons UI only** | — | ❌ gap |
| **`BookHold`** (place a hold) | BiblioCommons account | **BiblioCommons UI only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (1 dataset)** | Open, machine-readable branch directory with full NYC geography spine | Branches only; nothing about catalog, events, digital, or patron transactions |
| **Vendor APIs (BiblioCommons / Communico / OverDrive / Axis 360 / hoopla / Springshare)** | The real systems — rich catalog, events, and digital data | Five separate models, logins, and APIs; none owned by QPL; holds and cards behind login; no unified contract |
| **Drupal site (F5 BIG-IP)** | Public content, hours, help | WAF rejects browser-UA crawls; no content API |

## Implications for the API-first + MCP proposal

1. **Publish the open branch data as one clean resource.** `Branch` behind an owned QPL contract ([OpenAPI](openapi/queenslibrary.yaml)) — the one thing already open, modeled cleanly.
2. **Federate the vendor silos.** Present `CatalogItem` (BiblioCommons), `Event` (Communico), and `DigitalCollection` (OverDrive/Axis 360/hoopla) through one owned QPL API, so consumers learn one model instead of five vendor APIs.
3. **Unlock the patron transactions.** Add the net-new write workflows: `place_hold` (`POST /holds` — the primary net-new **BookHold** surface) and `apply_for_library_card` (`POST /library-cards`), replacing login-walled BiblioCommons screens.
4. **Keep patrons private.** Account data (holds, checkouts, fines) stays authenticated and per-patron; nothing individual is published.
5. **MCP server** so an agent can answer "which Queens branch near me is open now?", "does QPL have this title as an eBook?", "what kids' programs are at Flushing this week?", and — the point — "place a hold on this book for pickup at Jamaica and tell me my place in line."
6. **The bigger prize: a shared NYC library API.** Queens, Brooklyn, and NYPL are three separate systems; one federated contract across all three would be the real modernization.
