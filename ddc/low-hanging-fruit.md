# Low-Hanging Fruit Index — DDC

**Agency:** New York City Department of Design and Construction (DDC)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/ddc` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace + Akamai mPulse + AWS ALB) and read the "Work With DDC" procurement page, which names the citywide systems DDC solicits through (**PASSPort**/MOCS, **City Record**, **Checkbook NYC**, **DDC Anywhere**). Verified the NYC Open Data agency label `Department of Design and Construction (DDC)` via the Socrata Discovery API and pulled all **4** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-ddc.md](opendata-ddc.md).

## Headline findings

1. **DDC is a vendor-facing, business-to-government agency.** The City's primary capital construction project manager (550+ active projects, $34B+ portfolio) that builds *for other agencies*. There is **no citizen and no citizen transaction** anywhere in the domain.
2. **DDC exposes no API of its own.** Its only machine-readable data is **4 NYC Open Data datasets** — three of them frozen `(Historical)` snapshots of active projects, plus a 4-column directory of awarded contracts.
3. **The transactions are outsourced.** Solicitations and vendor prequalification run in **PASSPort** (managed by MOCS), notices go to the **City Record**, and contract records live on **Checkbook NYC** (Comptroller). The one DDC-owned vendor portal (**DDC Anywhere**) has no API.
4. **Even the portfolio isn't fully DDC-published.** The richer live capital data (Capital Commitment Plan / Capital Project Detail Data) is published under **OMB/Comptroller** labels, not DDC.

> **Reframe (sixth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* fragmented APIs; NYCHA = *unlock* a locked service layer; DFTA = *connect* via a phone line; **DDC = surface.** Here DDC owns almost none of its surface — its data is thin and historical and its transactions run on citywide systems it doesn't control — so the work is to *surface* the live capital portfolio as an owned API and front the citywide vendor flow (prequalification) with an agent-native contract.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Active Capital Projects | `CapitalProject` | SODA (snapshots) | 🟡 Active Projects (`3ss8-m844`) + two `(Historical)` |
| 2 | Awarded Construction Contracts | `AwardedContract` | SODA + Checkbook | ✅ Directory (`j7gw-gcxi`, 4c) |
| 3 | Vendors / Firms | `Vendor` | PASSPort (MOCS) | 🟡 derived from `j7gw-gcxi` |
| 4 | DDC Divisions | `Division` | — | 🟡 derived from `Division` column |
| 5 | Open Solicitations | `Solicitation` | PASSPort / City Record | ❌ gap (no DDC API) |
| 6 | City Record notification signup | `VendorPrequalification` | City Record | ❌ gap (citywide) |
| 7 | **Submit vendor prequalification** | `VendorPrequalification` | PASSPort (MOCS) | ❌ **net-new (B2G)** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 4 DDC datasets (the one real, open data surface; thin and mostly historical).
- **PASSPort (MOCS)** — the citywide solicitation + vendor prequalification system; login-walled, no API; **not DDC-owned**.
- **City Record / Checkbook NYC** — citywide notices and contract transparency; Checkbook's API belongs to the Comptroller.
- **DDC Anywhere** — the one DDC-owned vendor portal; no API observed.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace + mPulse RUM, AWS ALB) — the same chassis as Parks/DOE/NYCHA/DFTA peers.

## Reverse-engineered entities

`CapitalProject` · `AwardedContract` · `Vendor` (firm/consultant; derived) · `Division` (derived) · `Solicitation` (citywide, no DDC twin) · `VendorPrequalification` (net-new B2G write; also stands in for the City Record notification opt-in) — join keys: **Project ID**, **PIN**, and **SELECTED FIRM**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Project ID, PIN, Division, Client Agency, Dollar Amount, $Value) and the citywide vendor concepts — done ([schemas/](schemas/)).
2. **OpenAPI** surfacing the capital portfolio + contracts + vendors as clean resources + the net-new `POST /prequalifications` (submit a vendor prequalification) — done ([openapi/ddc.yaml](openapi/ddc.yaml)).
3. **MCP** artifact: `find_projects`, `get_project`, `get_project_contracts`, `find_contracts`, `get_contract`, `find_vendors`, `list_divisions`, `find_solicitations`, `list_my_prequalifications`, `submit_prequalification` — done ([mcp/ddc-mcp.json](mcp/ddc-mcp.json)).
