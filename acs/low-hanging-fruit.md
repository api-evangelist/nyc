# Low-Hanging Fruit Index — ACS

**Agency:** NYC Administration for Children's Services (ACS)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/acs` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace + embedded Google Maps JS) and traced its public actions to their real homes: **reporting child abuse** links out to the **NY State OCFS Statewide Central Register** (`ocfs.ny.gov`, 1-800-342-3720), and **service/provider complaints** to **NYC 311** (`portal.311.nyc.gov`). Verified the NYC Open Data agency label `Administration for Children's Services (ACS)` via the Socrata Discovery API and pulled all **21** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-acs.md](opendata-acs.md).

## Headline findings

1. **ACS is a confidentiality-bound agency.** Abuse/neglect investigations, foster care, and juvenile detention are confidential by statute; they are published **only in aggregate** — and never as individual cases.
2. **Its Open Data is thin and mostly files.** Of **21** ACS assets, **16 are `file` attachments** (uploaded Excel/PDF reports you cannot query) and only **5 are tabular**. Just **one** is address-level and machine-readable: the **ACS Community Partners** provider directory (`9hyh-zkx9`, 39 columns).
3. **Its public actions are delegated.** ACS owns neither intake it fronts: **report child abuse → NY State Central Register**; **complain about a child care provider → NYC 311**. There is no ACS-owned API.
4. **Case data is never public, correctly.** No individual investigation, foster child, or youth is exposed — the modernization job must preserve that.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* fragmented APIs; NYCHA = *unlock* a service layer locked in a CRM; **ACS = insource what ACS can own.** Here there is no hidden backend to unlock — the data is confidential or dumped as files, and the two public actions are handed to the State and to 311. The work is to publish ACS's one real dataset and its aggregate reports as clean resources, and to *insource* an owned, agent-native provider-complaint intake — while routing suspected abuse to 1-800-342-3720 and never touching case data.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | ACS Community Partners (provider directory) | `Provider` | SODA + map | ✅ Community Partners (`9hyh-zkx9`, 39c) |
| 2 | Child Welfare Indicators | `ChildWelfareIndicator` | SODA (mostly files) | 🟡 Indicators (`3m2q-9maw`), Flash (`2ubh-v9er`), Demographics (`uhvm-6sct`, 13c) |
| 3 | Preventive Services | `PreventionService` | SODA (files) | 🟡 Children Served (`ding-39n6`), New Cases (`a2ju-qb9a`) |
| 4 | Foster Care statistics | `FosterCareStatistics` | SODA (files) | 🟡 24-hr Care (`hfa5-7rzg`), Psych Meds (`qw7r-btyb`, 15c) |
| 5 | Youth & Family Justice statistics | `JuvenileJusticeStatistics` | SODA (files) | 🟡 Detention Admissions (`2hrw-qfsu`, 4c), Preplacement (`iwat-y983`, 9c) |
| 6 | Report child abuse/neglect | — (delegated) | NY State Central Register | ❌ gap (State hotline; by design) |
| 7 | **Complain about a child care provider** | `ChildCareComplaint` | NYC 311 | ❌ **net-new** |
| 8 | Individual case / child record | — | Internal ACS (CCWIS) | ❌ never public (correct) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 21 ACS assets, but only 5 tabular and 1 address-level (the one useful open API).
- **NY State OCFS Statewide Central Register / CONNECTIONS** — where abuse reports actually go; phone-based, no API, deliberately human-mediated.
- **NYC 311** (`portal.311.nyc.gov`) — the citywide intake ACS delegates provider complaints to; ACS owns no equivalent.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM, Google Maps JS) — the same chassis as NYCHA, with no ACS-specific application.

## Reverse-engineered entities

`Provider` (Community Partner; the one machine-readable object) · `ChildWelfareIndicator` · `PreventionService` · `FosterCareStatistics` · `JuvenileJusticeStatistics` (all aggregate-only; never an individual case) · `ChildCareComplaint` (net-new write; the provider concern ACS delegates to 311) — shared spines: **NYC geography** (BBL/BIN, council district, community board, NTA) and **reporting period** (year / period / frequency).

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (the 39-column Community Partners directory; the aggregate report fields; the period + geography spines) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the provider directory + aggregate reports as clean resources + the net-new `POST /child-care-complaints` (report a provider concern) — done ([openapi/acs.yaml](openapi/acs.yaml)).
3. **MCP** artifact: `find_providers`, `get_provider`, `find_child_welfare_indicators`, `find_prevention_services`, `find_foster_care_statistics`, `find_juvenile_justice_statistics`, `list_my_complaints`, `get_complaint`, `report_child_care_concern` — done ([mcp/acs-mcp.json](mcp/acs-mcp.json)).
