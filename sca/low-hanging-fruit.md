# Low-Hanging Fruit Index — SCA

**Agency:** NYC School Construction Authority (SCA)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nycsca.org/robots.txt` disallows DNN system paths like `/admin/`, `/DesktopModules/`, `/Portals/`, not content). Fingerprinted `www.nycsca.org` as a **DotNetNuke (DNN) ASP.NET CMS** (the "obvio" skin — `.ASPXANONYMOUS`/`dnn_IsMobile`/`__RequestVerificationToken` cookies, `__VIEWSTATE`, `DNNGoContentBuilder` markup) behind an **AWS load balancer** (`AWSALB` cookies) with document content in **Azure Blob Storage** (`dnnhh5cc1.blob.core.windows.net`). Identified the vendor **bidset** portal (`bidset.nycsca.org`) as a login-walled **SharePoint** app (`_layouts/OnlineBidsetsLogin/CustomLogin.aspx`), and confirmed the `/WS/Reports/` path returns DNN HTML, not JSON. Verified the NYC Open Data agency label `School Construction Authority (SCA)` via the Socrata Discovery API and pulled all **43** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-sca.md](opendata-sca.md).

## Headline findings

1. **SCA is a vendor-facing agency on a fifth distinct platform.** A DotNetNuke ASP.NET CMS behind AWS, content in Azure Blob, plus a **SharePoint bid-document portal** (`bidset.nycsca.org`) with **no API**.
2. **The reference data is unusually open and procurement-rich.** **43 NYC Open Data datasets** cover the capital plan (active projects, schedules and budgets, capacity by school), the forward pipeline (upcoming CIP/CAP contracts, current/anticipated RFPs, change orders), the approved-vendor roster (prequalified and disqualified firms), enrollment/capacity demand, demographic projections, and inspections.
3. **But the vendor transaction layer is locked.** Obtaining bid documents and — upstream — applying to become a **prequalified vendor** live only behind the bidset SharePoint login and PDF forms. None has a machine-readable contract.
4. **SCA publishes the result, not the act.** The Prequalified Firms roster (`szkz-syh6`) is open, but the act of *applying* is not — a clean read/write mismatch.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a CRM; **SCA = onboard the vendor.** Here the whole capital pipeline is already open — the work is least about liberating datasets and most about giving the **vendor transaction layer** (above all, getting prequalified) an owned, agent-native API instead of a SharePoint login.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Active Projects Under Construction | `CapitalProject` | SODA + map | ✅ Active Projects (`8586-3zfm`, 29c) |
| 2 | Capital Project Schedules & Budgets | `CapitalProject` | SODA | ✅ Schedules & Budgets (`2xh6-psuq`, 14c) |
| 3 | Upcoming Contracts (CIP / CAP) | `UpcomingContract` | SODA | ✅ CIP (`tsak-vtv3`) + CAP (`6m3u-8rbh`) + change orders |
| 4 | RFP Solicitations (Current & Anticipated) | `Solicitation` | SODA (notice) + bidset (docs) | 🟡 Current/Anticipated RFP (`bzjf-rmtp`, `p8e4-uwuv`) — docs walled |
| 5 | Prequalified & Disqualified Firms | `PrequalifiedFirm` | SODA | ✅ Prequalified (`szkz-syh6`) + Disqualified (`krwf-eng6`) |
| 6 | Enrollment, Capacity & Utilization | `EnrollmentCapacity` | SODA | ✅ Enrollment Capacity & Utilization (`gkd7-3vk7`) + projections |
| 7 | Construction Inspections | `Inspection` | SODA | ✅ Inspections Requested (`n4tc-j6kh`) + Observations (`6246-94tp`) |
| 8 | Obtain bid documents (bidset) | `VendorPrequalification` | SharePoint portal | ❌ gap (no API) |
| 9 | **Apply to become a prequalified vendor** | `VendorPrequalification` | PDF forms + bidset | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 43 SCA datasets (the one real, open API; reference data only).
- **Microsoft SharePoint** — the bidset vendor portal; login-walled, no API.
- Platform: informational/vendor site on **DotNetNuke (DNN) ASP.NET** (obvio skin) behind an **AWS ALB**, documents in **Azure Blob Storage** — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Siebel.

## Reverse-engineered entities

`CapitalProject` · `UpcomingContract` · `Solicitation` · `PrequalifiedFirm` · `EnrollmentCapacity` · `Inspection` · `VendorPrequalification` (net-new write; also stands in for the SharePoint-locked bid-document transaction) — join keys: **Building ID / BIN**, **DSF Number**, **Geographic (school) District**, **Master Trade Code**, **BBL**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Building ID, DSF Number, Geographic District, Master Trade Code, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference data as clean resources + the net-new `POST /prequalifications` (apply to prequalify) — done ([openapi/sca.yaml](openapi/sca.yaml)).
3. **MCP** artifact: `find_capital_projects`, `get_capital_project`, `find_upcoming_contracts`, `find_solicitations`, `find_vendors`, `find_enrollment_capacity`, `find_inspections`, `list_my_prequalifications`, `apply_for_prequalification` — done ([mcp/sca-mcp.json](mcp/sca-mcp.json)).
