# APIs Observed While Crawling — NYC Department of Buildings (DOB)

Backend/service APIs the DOB web presence calls or exposes, surfaced during the crawl (2026-07-13). DOB is the project's clearest example that **the real system is not the website — it is the `aNNN-*.nyc.gov` application layer** — and that layer offers **no public API**. The only machine-readable DOB surface is a nightly Open Data batch dump. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`data.cityofnewyork.us`** (SODA) | Open Data API | NYC / Socrata (Tyler) | **Yes — read-only** | **44 DOB datasets.** A **nightly batch extract** of BIS/DOB NOW — every dataset carries a `DOBRunDate` column. The only machine-readable DOB surface; lossy and up to a day stale. |
| **`a810-dobnow.nyc.gov`** | Filing/permitting web app | NYC DOB (DOB NOW) | **Browser-only — Akamai-gated** | The modern transactional system (jobs, permits, C of O, safety). **403 "Access Denied"** to non-browser clients. No API. |
| **`a810-bisweb.nyc.gov`** | Legacy record web app | NYC DOB (BIS) | **Browser-only — Akamai-gated** | Legacy Building Information System. Akamai bot-manager challenge; browser-only. No API. |
| **`a810-efiling.nyc.gov`** | eFiling web app | NYC DOB | Browser-only | **Apache Tomcat/9.0.117** (Java). DOB eFiling. No API. |
| `www.nyc.gov/site/buildings` | Content CMS | NYC (citywide NYC.gov) | Yes (HTML) | Brochureware behind nginx + Akamai (Dynatrace/mPulse RUM). Links out to the app layer; holds no records. |
| `translate.google.com` | Translation widget API | Google | Vendor | Google Website Translator on the CMS. |
| `a856-cityrecord.nyc.gov`, `a858-nycnotify.nyc.gov` | Adjacent aNNN apps | NYC | Browser | City Record Online + notifications — same numbered-legacy-app pattern, referenced from DOB pages. |

## Takeaways

- **The API problem here is absence at the transactional core.** DOB has a mature application layer (BIS, DOB NOW, eFiling) but **not one public API** over it.
- **The only "API" is a nightly one-way dump.** NYC Open Data exposes the records, but as a stale batch extract (`DOBRunDate`), disconnected from the live systems and read-only.
- **The write side is entirely closed.** Filing a permit application, paying fees, or checking real-time status can only be done in-browser through DOB NOW.
- **This is why the modernization verb is *Transact*.** The [OpenAPI](openapi/dob.yaml) + [MCP artifact](mcp/dob-mcp.json) here propose one owned contract that fronts the app layer for reads **and** adds the net-new [`PermitApplication`](schemas/permit-application.json) write workflow.
