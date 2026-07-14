# QA / Verification

Automated re-verification of the falsifiable claims across all **67 domains** — is the site live, do the crosswalked Open Data assets actually exist, are the observed-API endpoints reachable. Interactive: [qa.html](https://nyc.apievangelist.com/qa.html).

**Confidence:** 66 high · 0 medium · 1 low. **Sites:** 63 ok · 3 gated (live but bot/auth-walled) · 1 unreachable.

## Flagged for review

| Domain | Confidence | Issue |
|--|--|--|
| NYC Public Advocate | low | primary site unreachable (0) — https://www.pubadvocate.nyc.gov/ |

## Deep-verified sample (manual)

The boldest qualitative claims, re-probed against live sources:

| Domain | Claim | Verdict | Evidence |
|--|--|--|--|
| H+H | live Epic FHIR R4 endpoint | **CONFIRMED** | epicproxypda.nychhc.org FHIR R4 /metadata → 200 (CapabilityStatement). |
| OTI | 221 Open Data assets (platform operator) | **CONFIRMED** | Socrata agency facet 'Office of Technology and Innovation (OTI)' → resultSetSize 221, exact. |
| DOB | transactional core in the aNNN app layer (BIS/DOB NOW) | **CONFIRMED** | a810-bisweb.nyc.gov → 200; a810-dobnow.nyc.gov → 403 (bot-gated, live). |
| NYPL | three real public APIs | **PARTLY CONFIRMED** | Locations API → 200; Digital Collections API → 401 (exists, token-gated); the Research Catalog discovery endpoint did not resolve at the guessed URL (2 of 3 verified live). |
| Public Advocate | self-hosted site degraded / down | **CONFIRMED (defect)** | pubadvocate.nyc.gov and advocate.nyc.gov both unreachable (000) — the office's primary web presence is down. |
