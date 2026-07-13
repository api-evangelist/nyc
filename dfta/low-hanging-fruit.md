# Low-Hanging Fruit Index — NYC Aging (DFTA)

**Agency:** NYC Department for the Aging (DFTA / "NYC Aging")
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/dfta` (Akamai + nginx + NYC.gov "Livesite" platform v22 + Dynatrace) and the resident-facing **Aging Connect** intake at `nyc.gov/site/dfta/services/find-help.page` (information-and-referral contact center, **212-AGING-NYC / 212-244-6469** — phone/web, no API). Verified the NYC Open Data agency label `Department for the Aging (NYC Aging)` via the Socrata Discovery API and pulled all **11** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dfta.md](opendata-dfta.md).

## Headline findings

1. **DFTA is a connective, network-funding agency.** It rarely delivers services itself — it funds ~1,000 community providers and routes older adults to them. Its data is therefore a directory of providers, sites, senior-center operations, activities, and contract service units.
2. **The provider/program reference data is well open.** **11 NYC Open Data datasets** cover all contracted providers (38 columns), publicly open sites, older adult center (senior center) Local Law 140 operations, activities, budgeted/reported service units, expenditures, and aggregate participation.
3. **But the service layer is a phone call.** Connecting an older adult to case management, home-delivered meals, benefits, caregiver support, elder-abuse help, or center enrollment happens only through **Aging Connect** by phone/walk-in, 311, or a web form. None has a machine-readable contract.
4. **Clients stay private by design.** Participation is published only in aggregate (unduplicated clients); no individual older adult record is ever exposed.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **DFTA = connect the older adult to services.** Here the provider data is already open — and there is no vendor system to unlock, only a phone-based referral process. The work is to give the **intake/referral layer** (above all, making a service referral) an owned, agent-native API instead of a contact-center phone queue.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Contracted Service Providers | `ServiceProvider` | SODA + finder | ✅ All Contracted Providers (`cqc8-am9x`, 38c) |
| 2 | Older Adult Centers (senior centers) | `OlderAdultCenter` | SODA | ✅ Senior Center LL140 (`ygfr-ij6t`, 49c) |
| 3 | Older Adult Center Activities | `ProgramActivity` | SODA | ✅ OAC Activities (`fzy4-e84j`, 26c) |
| 4 | Contract Service Units & Budgets | `ServiceUnit` | SODA (×4) | ✅ Reported Service Units (`exaw-9qnu`) + budget/expenditures |
| 5 | Program Participation | `Participation` | SODA | 🟡 Number of Participants (`2td3-mfek`) — aggregate only |
| 6 | Apply for home-delivered meals | `ServiceReferral` | Aging Connect | ❌ gap (no API) |
| 7 | Request case management | `ServiceReferral` | Aging Connect | ❌ gap (no API) |
| 8 | Report suspected elder abuse | `ServiceReferral` | Aging Connect / APS | ❌ gap (no API) |
| 9 | Find help / get connected | `ServiceReferral` | Aging Connect (212-AGING-NYC) | ❌ gap (no API) |
| 10 | **Make a service referral** | `ServiceReferral` | Aging Connect + 311 | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 11 DFTA datasets (the one real, open API; provider/program data only).
- **Aging Connect** — the information-and-referral contact center; phone/walk-in, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as NYCHA, but with **no separate vendor application** behind the transactions (DFTA's service layer is a phone line, not a Siebel CRM).

## Reverse-engineered entities

`ServiceProvider` · `OlderAdultCenter` (senior center) · `ProgramActivity` · `ServiceUnit` (budgeted/reported) · `Participation` (aggregate; never individual client) · `ServiceReferral` (net-new write; also stands in for the Aging-Connect-locked meals / case-management / elder-abuse referrals) — join key: **DFTA ID**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (DFTA ID, ProviderType, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open provider network as clean resources + the net-new `POST /referrals` (make a service referral) — done ([openapi/dfta.yaml](openapi/dfta.yaml)).
3. **MCP** artifact: `find_providers`, `get_provider`, `find_older_adult_centers`, `find_activities`, `find_service_units`, `find_participation`, `list_my_referrals`, `make_referral` — done ([mcp/dfta-mcp.json](mcp/dfta-mcp.json)).
