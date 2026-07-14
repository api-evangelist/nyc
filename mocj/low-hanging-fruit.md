# Low-Hanging Fruit Index — MOCJ

**Agency:** NYC Mayor's Office of Criminal Justice (MOCJ)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Found the thin informational stub at `nyc.gov/site/criminaljustice` (Akamai + nginx + NYC.gov "Livesite" + Dynatrace/mPulse; most subpages 404) and the real office site at `criminaljustice.cityofnewyork.us`, fingerprinted as **WordPress on WP Engine behind Cloudflare** (`x-powered-by: WP Engine`; Kadence/ACF/Contact Form 7/The Events Calendar/Yoast/Site Kit). Enumerated the site's custom post types via its **accidental `wp/v2` REST API**. Verified the NYC Open Data agency label `Mayor's Office of Criminal Justice (MOCJ)` via the Socrata Discovery API — exactly **1** dataset.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-mocj.md](opendata-mocj.md).

## Headline findings

1. **MOCJ is a split domain.** A near-empty stub on the shared NYC.gov chassis, and the real office site on **WordPress / WP Engine / Cloudflare** (`criminaljustice.cityofnewyork.us`) — a fifth distinct platform after Parks, DOE, Council, and NYCHA.
2. **It owns almost no data.** NYC Open Data carries exactly **one** MOCJ dataset — Supervised Release Dockets (`atne-2dki`, 6 columns, last updated 2023, ~1,074 views).
3. **The jail numbers aren't MOCJ's.** Its System Data page publishes PDF *explainers* (jail-population increase, re-arrest rates) and links OUT to DOC, NYPD (CompStat), NYS DCJS, and the Board of Correction for the underlying figures. MOCJ convenes and analyzes; it does not own the metrics.
4. **Its only real API is accidental.** The default WordPress `wp/v2` REST API exposes programs (26), solicitations (25), notices (26), reports (26), data reports (109), briefs (54), and data stories (6) as JSON — undocumented, unintended, not a product. Contact Form 7 is the only write path.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **MOCJ = route.** Here the office owns little — the work is least about liberating datasets and most about giving a **coordination office** an owned contract: promoting its accidental WordPress API to an intentional one, citing the metrics it only links to, and giving its core function — routing a person or case to a program — a machine-readable, agent-native surface.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | MOCJ Programs | `Program` | WordPress (accidental `wp/v2`) | ❌ none (JSON via WP REST) |
| 2 | Supervised Release Dockets | `SupervisedReleaseDocket` | SODA | ✅ `atne-2dki` (6c, stale 2023) |
| 3 | Jail population & system indicators | `JailPopulationMetric` | PDF explainers + external links | 🟡 aggregate, owned by DOC/NYPD/DCJS/BOC |
| 4 | Publications, reports & briefs | `DataReport` | WordPress (accidental `wp/v2`) | ❌ none (JSON via WP REST) |
| 5 | Procurement — solicitations & notices | `Solicitation` | WordPress (accidental `wp/v2`) | ❌ none (JSON via WP REST) |
| 6 | Vendor enrollment / contact | `ProgramReferral` | Contact Form 7 web form | ❌ gap (form-to-email) |
| 7 | **Refer to a program** | `ProgramReferral` | offline / web form | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **WordPress `wp/v2` REST API** — the one real, machine-readable surface; accidental and undocumented.
- **Contact Form 7 REST** — the only write path (generic form-to-email).
- **Socrata SODA** — one MOCJ dataset (Supervised Release Dockets).
- **External dashboards** — DOC / NYPD / DCJS / BOC, linked but not owned.
- Platform: **WordPress on WP Engine behind Cloudflare** (Kadence/ACF/Contact Form 7) — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite+Siebel.

## Reverse-engineered entities

`Program` · `SupervisedReleaseDocket` (the one dataset) · `JailPopulationMetric` (aggregate; owned by other agencies) · `DataReport` (reports/briefs/data reports/stories) · `Solicitation` (procurement) · `ProgramReferral` (net-new write; also stands in for the vendor-enrollment / contact web forms) — organizing vocabularies: **Sequential Intercept Model (0-5)** and **Programs by Issue**.

## Next

1. **JSON Schema** per entity, reconciling the WordPress content model, the one Open Data dataset, and MOCJ's Sequential Intercept framework — done ([schemas/](schemas/)).
2. **OpenAPI** promoting the accidental WordPress API to an intentional resource model + the net-new `POST /program-referrals` — done ([openapi/mocj.yaml](openapi/mocj.yaml)).
3. **MCP** artifact: `find_programs`, `get_program`, `find_supervised_release_dockets`, `find_jail_population_metrics`, `find_data_reports`, `find_solicitations`, `get_solicitation`, `refer_to_program`, `get_referral` — done ([mcp/mocj-mcp.json](mcp/mocj-mcp.json)).
