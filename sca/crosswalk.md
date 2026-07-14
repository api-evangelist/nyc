# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (SCA)

Maps the low-hanging fruit on **nycsca.org** and the **bidset SharePoint portal** to (a) the **existing APIs** (Socrata SODA; the bidset portal) and (b) the **43 SCA datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-sca.json](opendata-sca.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** the reference data is open, but every resident transaction is locked in an Oracle Siebel CRM → *unlock the service layer.*
- **SCA:** the whole capital plan and procurement pipeline is **already wide open** (43 Socrata datasets), but every **vendor transaction is locked inside a SharePoint portal** and PDF forms → **onboard vendors via API.**

SCA is a vendor-facing variation on NYCHA's inversion. The projects, budgets, upcoming contracts, RFP notices, approved-vendor roster, capacity, and inspections are all machine-readable on Open Data. What a *vendor* does — get prequalified, obtain bid sets, bid — lives only behind the login-walled bidset SharePoint portal. A firm or agent asking "how do I get prequalified for this trade?" has no API to call, even though the *result* (the Prequalified Firms roster) is open.

Coverage: ✅ strong open twin · 🟡 partial (notice open, docs walled) · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `CapitalProject` | `/Community/Capital-Plan-Reports-Data` | SODA | Active Projects (`8586-3zfm`, 29c); Schedules & Budgets (`2xh6-psuq`); Capacity by School (`a94k-kjys`) | ✅ |
| `UpcomingContract` | Business Opportunities | SODA | Upcoming CIP (`tsak-vtv3`); CAP (`6m3u-8rbh`); Change Orders (`gzvm-na49`) | ✅ |
| `Solicitation` (RFP) | Business Opportunities + bidset | SODA (notice) / **SharePoint (docs)** | Current RFP (`bzjf-rmtp`); Anticipated RFP (`p8e4-uwuv`) | 🟡 notice open, docs walled |
| `PrequalifiedFirm` | `/Vendor/Vendor-List` | SODA | Prequalified Firms (`szkz-syh6`, 15c); Disqualified Firms (`krwf-eng6`) | ✅ |
| `EnrollmentCapacity` | Capital plan reports | SODA | Enrollment Capacity & Utilization (`gkd7-3vk7`); historical (`q9xk-w9iv`, `hq56-zhrp`); projections (`e649-r223`) | ✅ |
| `Inspection` | — | SODA | Inspections Requested (`n4tc-j6kh`); Observations (`6246-94tp`) | ✅ |
| Obtain bid documents | bidset portal | **SharePoint UI only** | — | ❌ gap |
| **`VendorPrequalification`** (apply/renew/add trade) | `/Vendor/Prequalification` + bidset | **PDF forms / SharePoint only** | — (roster only) | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (43 datasets)** | Open, machine-readable; strong on the capital plan, procurement pipeline, vendor roster, capacity, and inspections | Reference/asset data only; static snapshots; nothing about live vendor transactions |
| **Bidset SharePoint portal** | The real vendor transaction system — bid documents and submissions | Login-walled SharePoint; no API, no OpenAPI, no JSON; not agent-accessible; prequalification is PDF forms |

## Implications for the API-first + MCP proposal

1. **Publish the open reference data as one clean resource model.** Capital projects, upcoming contracts, solicitations, vendors, capacity, and inspections behind one owned SCA contract ([OpenAPI](openapi/sca.yaml)) — so consumers learn one model, not 43 Socrata IDs.
2. **Onboard the vendor.** Front the bidset portal and prequalification forms with an API so the core vendor transaction — **applying to become a prequalified firm** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `apply_for_prequalification` (submit/renew/add-trade), with document attachments and a status lifecycle, so the *act* of applying is finally as open as the *roster* of who got in.
4. **Keep the read/write model coherent.** The approved roster stays the read view (`PrequalifiedFirm`); the application is the write view (`VendorPrequalification`).
5. **MCP server** so an agent can answer "which upcoming CAP contracts add seats in District 24?", "which prequalified electricians are M/WBE-certified?", and — the point — "apply to prequalify my firm for this trade and tell me the status."
