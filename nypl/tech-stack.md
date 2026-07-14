# Technology & Vendor Inventory — NYPL

What the New York Public Library's public surfaces are built on and which third parties they depend on — fingerprinted from response headers, API payloads, and the github.com/NYPL open-source org during the crawl (2026-07-13). NYPL is an **independent nonprofit**, not a city agency, and it shows: rather than sitting on the shared NYC.gov chassis, NYPL runs and **open-sources its own stack**, including real public APIs.

## The surfaces

| Surface | URL | What it does |
|---|---|---|
| Patron site + Research Catalog | `www.nypl.org` | Discovery, accounts, holds, events, library-card application |
| **Digital Collections API** | **`api.repo.nypl.org/api/v2`** | Token-authenticated public API over digitized items (search, MODS, captures, rights, collections) |
| **Locations API** | **`refinery.nypl.org/api/nypl/locations/v1.0`** | Open, hypermedia API over branches, hours, amenities, events, exhibitions, alerts |
| Research Catalog API | `discovery-api` (github.com/NYPL) | Open-source bibliographic search over the Sierra ILS |

## Fingerprint

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Patron-site edge | **Imperva Incapsula** | `x-iinfo`, `incap_ses_*` and `_Incapsula_Resource` in `www.nypl.org` responses; headers are edge-obscured |
| Digital Collections API | **Ruby on Rails + Phusion Passenger + nginx** | `x-powered-by: Phusion Passenger 6.1.6`, `server: nginx/1.24.0 (Ubuntu) + Phusion Passenger`, `x-runtime`, `_api_service_session` cookie on `api.repo.nypl.org` |
| Digital Collections API auth | **Token / OAuth (HTTP Basic gate)** | `GET /api/v2/items/search` → `401 HTTP Basic: Access denied.` without a registered token |
| Locations API | **PHP + Slim framework** | error payload namespaces `NYPL\Refinery\Server`, `slim/slim/Slim/Handlers`; `server: nginx/1.28.0` on `refinery.nypl.org` |
| Research Catalog | **Node on AWS (ALB) + Sierra ILS** | `AWSALB`/`AWSALBCORS` cookies; `github.com/NYPL/discovery-api`, `ruby-sierra-api-client` |
| Monitoring | **New Relic** | `NREUM` / `gov-bam.nr-data.net` beacon on `api.repo.nypl.org` |
| Design system | **NYPL Design System** (React, accessibility-first) | `github.com/NYPL/nypl-design-system` (80 stars) |
| Ontology / data models | **nypl-core** | `github.com/NYPL/nypl-core` |
| ILS (system of record) | **Sierra** (Innovative / III) | `ruby-sierra-api-client`, `sierra-shadow-dataset`, `sierraUpdatePollerV2` |
| Patron / holds services | **NYPL microservices** | `on-site-hold-request-service`, `nypl-hold-request-consumer`, `patron-eligibility-service`, `dgx-patron-creator-service`, `barcode-service` |

## What this means

- **NYPL owns its stack.** Nearly everything is on github.com/NYPL — the Digital Collections API, the Research Catalog `discovery-api`, a web-based ebook reader, the `nypl-core` ontology, and an accessibility-first React design system. Vendor dependence is limited to infrastructure (AWS, Incapsula, New Relic) and the Sierra ILS.
- **The APIs already exist and are mature.** The Digital Collections API is token-authenticated Rails; the Locations API is open hypermedia PHP/Slim. These are not screen-scrape targets — they are documented, versioned APIs.
- **The transaction system is real but internal.** Placing a hold is backed by `on-site-hold-request-service`, `patron-eligibility-service`, and the Sierra client — production services — but exposed only through the patron's authenticated account UI, not a clean public API.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data open, service layer locked in a vendor CRM → *unlock*.
- **BIC** = open registry, transactions behind a Salesforce portal → *transact*.
- **NYPL** = a nonprofit that **already built and open-sourced good public APIs** → **lead** — be the model, unify the three APIs, and close the one write gap (holds).

## Modernization implications

1. **The gap is unification and one write, not liberation.** Three good APIs with three different auth models, hosts, and shapes make a consumer learn each separately. One owned contract ([OpenAPI](openapi/nypl.yaml)) presents digital items, collections, branches, events, and catalog under a single resource model.
2. **Expose the hold as a clean, documented, agent-native API.** The internal hold/eligibility/Sierra services already exist; publishing `POST /holds` turns the everyday transaction into something an agent can call.
3. **Hold NYPL up as the model.** For a project cataloging how much city data is trapped, NYPL is the proof that a public-serving institution can own its APIs and open-source its stack — the exemplar other domains should be measured against.
