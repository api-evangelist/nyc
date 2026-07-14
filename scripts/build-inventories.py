#!/usr/bin/env python3
"""Build master cross-domain inventories from the repo artifacts:
  data/entities.json   + ENTITIES.md    — every object schema (entity) across all domains
  data/technology.json + TECHNOLOGY.md  — every platform / vendor / API / standard in use
Run from repo root: python3 scripts/build-inventories.py"""
import json, glob, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

manifest = json.load(open("data/manifest.json"))
DOMAINS = manifest["domains"]
short = {d["id"]: d["short"] for d in DOMAINS}
verb = {d["id"]: d.get("verb", "") for d in DOMAINS}
platform = {d["id"]: (json.load(open(f'{d["id"]}/fruit.json')).get("meta", {}) or {}).get("platform", "") for d in DOMAINS}

# ---------------- ENTITIES ----------------
by_entity = collections.defaultdict(list)   # title -> [domain ids]
by_domain_ent = {}
for d in DOMAINS:
    did = d["id"]
    titles = []
    for sp in sorted(glob.glob(f"{did}/schemas/*.json")):
        if os.path.basename(sp) == "_common.json":
            continue
        try:
            t = json.load(open(sp)).get("title")
        except Exception:
            t = None
        if t:
            titles.append(t)
            by_entity[t].append(did)
    by_domain_ent[did] = sorted(titles, key=str.lower)

# Alphabetical by entity name (case-insensitive).
ent_rows = sorted(([e, doms] for e, doms in by_entity.items()),
                  key=lambda x: x[0].lower())
entities_json = {
    "generated_from": "schemas/*.json titles across all domains",
    "total_entities": sum(len(v) for v in by_domain_ent.values()),
    "distinct_entities": len(by_entity),
    "byEntity": [{"entity": e, "count": len(doms),
                  "domains": [{"id": x, "short": short[x]} for x in doms]} for e, doms in ent_rows],
    "byDomain": [{"id": d["id"], "short": d["short"], "verb": d.get("verb", ""),
                  "entities": by_domain_ent[d["id"]]} for d in DOMAINS],
}
json.dump(entities_json, open("data/entities.json", "w"), indent=1)

L = ["# Master Entity List\n",
     f"Every object modeled across the **{len(DOMAINS)} assessed domains** — {entities_json['total_entities']} object schemas, **{entities_json['distinct_entities']} distinct entity names**. Generated from each domain's `schemas/*.json` titles. Interactive: [entities.html](https://nyc.apievangelist.com/entities.html).\n",
     "## Recurring entities (shared across domains)\n",
     "Entities modeled in 2+ domains — the natural candidates for shared, citywide schemas.\n",
     "| Entity | # domains | Domains |", "|---|---|---|"]
for e, doms in ent_rows:
    if len(doms) >= 2:
        L.append(f"| `{e}` | {len(doms)} | {', '.join(short[x] for x in doms)} |")
L.append("\n## All entities by domain\n")
for d in DOMAINS:
    ents = by_domain_ent[d["id"]]
    L.append(f"- **{d['short']}** (`{d['id']}`) — {', '.join('`'+e+'`' for e in ents)}")
open("ENTITIES.md", "w").write("\n".join(L) + "\n")

# ---------------- TECHNOLOGY ----------------
# canonical tech -> (category, [alias regexes])
TECH = {
 # Platforms / frameworks
 "WordPress": ("Platform / CMS", [r"wordpress", r"wp[- ]engine", r"wp/v2", r"wp-json"]),
 "Drupal": ("Platform / CMS", [r"drupal"]),
 "Progress Sitefinity": ("Platform / CMS", [r"sitefinity"]),
 "Smarty (PHP)": ("Platform / CMS", [r"smarty"]),
 "Microsoft Dynamics 365": ("Platform / CMS", [r"dynamics ?365", r"power apps portal"]),
 "Oracle WebCenter Sites": ("Platform / CMS", [r"webcenter"]),
 "DotNetNuke (DNN)": ("Platform / CMS", [r"dotnetnuke", r"\bdnn\b"]),
 "Adobe Experience Manager": ("Platform / CMS", [r"\baem\b", r"adobe experience manager"]),
 "Weebly": ("Platform / CMS", [r"weebly"]),
 "Revize": ("Platform / CMS", [r"revize"]),
 "NYC.gov Livesite": ("Platform / CMS", [r"livesite"]),
 "ASP.NET / IIS": ("Framework / runtime", [r"asp\.net", r"\biis\b", r"\.aspx"]),
 "Java / Tomcat / WebLogic": ("Framework / runtime", [r"tomcat", r"weblogic", r"\bjsf\b", r"\bjsp\b", r"apache struts", r"struts"]),
 "Spring": ("Framework / runtime", [r"spring"]),
 "Next.js": ("Framework / runtime", [r"next\.js", r"_next"]),
 "React": ("Framework / runtime", [r"\breact\b"]),
 "Angular": ("Framework / runtime", [r"angular"]),
 "nginx": ("Framework / runtime", [r"nginx"]),
 "Apache": ("Framework / runtime", [r"\bapache\b"]),
 # Hosting / CDN / edge
 "Akamai": ("Hosting / CDN / edge", [r"akamai", r"mpulse"]),
 "Cloudflare": ("Hosting / CDN / edge", [r"cloudflare"]),
 "AWS CloudFront": ("Hosting / CDN / edge", [r"cloudfront"]),
 "AWS (ALB/S3/EC2)": ("Hosting / CDN / edge", [r"\balb\b", r"\bs3\b", r"\bec2\b", r"aws "]),
 "Microsoft Azure": ("Hosting / CDN / edge", [r"\bazure\b", r"app service", r"azure ad b2c", r"azure blob"]),
 "WP Engine": ("Hosting / CDN / edge", [r"wp ?engine"]),
 "Pantheon": ("Hosting / CDN / edge", [r"pantheon"]),
 "Netlify": ("Hosting / CDN / edge", [r"netlify"]),
 "Vercel": ("Hosting / CDN / edge", [r"vercel"]),
 "Kinsta": ("Hosting / CDN / edge", [r"kinsta"]),
 "SiteGround": ("Hosting / CDN / edge", [r"siteground"]),
 "Fastly": ("Hosting / CDN / edge", [r"fastly"]),
 "Imperva": ("Hosting / CDN / edge", [r"imperva"]),
 "Varnish": ("Hosting / CDN / edge", [r"varnish"]),
 "Oracle Cloud": ("Hosting / CDN / edge", [r"oracle cloud"]),
 # Vendor SaaS / applications
 "Accela": ("Vendor SaaS / app", [r"accela"]),
 "Salesforce": ("Vendor SaaS / app", [r"salesforce", r"experience cloud", r"portico"]),
 "Oracle Siebel": ("Vendor SaaS / app", [r"siebel"]),
 "Unqork": ("Vendor SaaS / app", [r"unqork"]),
 "Kaseware": ("Vendor SaaS / app", [r"kaseware"]),
 "Epic / MyChart": ("Vendor SaaS / app", [r"\bepic\b", r"mychart"]),
 "PeopleSoft (CUNYfirst)": ("Vendor SaaS / app", [r"peoplesoft", r"cunyfirst"]),
 "Legistar (Granicus)": ("Vendor SaaS / app", [r"legistar", r"granicus"]),
 "Checkbook NYC": ("Vendor SaaS / app", [r"checkbook"]),
 "Everbridge": ("Vendor SaaS / app", [r"everbridge"]),
 "Combined Arms": ("Vendor SaaS / app", [r"combined arms"]),
 "HawkSearch": ("Vendor SaaS / app", [r"hawksearch"]),
 "Viebit": ("Vendor SaaS / app", [r"viebit"]),
 "StreamText": ("Vendor SaaS / app", [r"streamtext"]),
 "BiblioCommons": ("Vendor SaaS / app", [r"bibliocommons"]),
 "Communico": ("Vendor SaaS / app", [r"communico"]),
 "OverDrive / hoopla": ("Vendor SaaS / app", [r"overdrive", r"hoopla", r"axis 360"]),
 "Preservica": ("Vendor SaaS / app", [r"preservica"]),
 "LUNA Imaging": ("Vendor SaaS / app", [r"luna"]),
 "Microsoft SharePoint": ("Vendor SaaS / app", [r"sharepoint"]),
 "Microsoft Power BI": ("Vendor SaaS / app", [r"power ?bi"]),
 "Shopify": ("Vendor SaaS / app", [r"shopify"]),
 "Constant Contact": ("Vendor SaaS / app", [r"constant contact"]),
 "WSO2 API Gateway": ("Vendor SaaS / app", [r"wso2"]),
 "Divi / GeneratePress / Themeco": ("Vendor SaaS / app", [r"\bdivi\b", r"generatepress", r"themeco", r"beaver builder"]),
 # Maps / geo
 "Esri ArcGIS": ("Maps / geospatial", [r"arcgis", r"\besri\b"]),
 "CARTO": ("Maps / geospatial", [r"carto"]),
 "Mapbox": ("Maps / geospatial", [r"mapbox"]),
 "Google Maps": ("Maps / geospatial", [r"google maps"]),
 "NYC GeoClient / GeoSearch": ("Maps / geospatial", [r"geoclient", r"geosearch", r"geosupport"]),
 # Media / assets
 "Cloudinary": ("Media / assets", [r"cloudinary"]),
 "Azure Blob Storage": ("Media / assets", [r"blob"]),
 # Analytics / monitoring
 "Google Tag Manager": ("Analytics / monitoring", [r"tag ?manager", r"gtag", r"googletagmanager"]),
 "Google Analytics": ("Analytics / monitoring", [r"google.analytics", r"\bga4\b"]),
 "Dynatrace": ("Analytics / monitoring", [r"dynatrace"]),
 "New Relic": ("Analytics / monitoring", [r"new ?relic"]),
 "Siteimprove": ("Analytics / monitoring", [r"siteimprove"]),
 "Matomo": ("Analytics / monitoring", [r"matomo"]),
 "Loggly": ("Analytics / monitoring", [r"loggly"]),
 "Meta / Facebook Pixel": ("Analytics / monitoring", [r"facebook", r"meta pixel"]),
 "Wordfence": ("Analytics / monitoring", [r"wordfence"]),
 # APIs / standards / data
 "Socrata / Tyler (SODA)": ("API / standard / data", [r"socrata", r"\bsoda\b", r"tyler"]),
 "WordPress REST API": ("API / standard / data", [r"wp/v2", r"wordpress rest", r"wp-json"]),
 "Drupal JSON:API": ("API / standard / data", [r"json:api", r"jsonapi"]),
 "FHIR / SMART on FHIR": ("API / standard / data", [r"\bfhir\b", r"smart on fhir"]),
 "Open311 (GeoReport v2)": ("API / standard / data", [r"open311", r"georeport"]),
 "api.nyc.gov (Azure APIM)": ("API / standard / data", [r"api\.nyc\.gov", r"api management", r"\bapim\b"]),
 "Google Translate": ("API / standard / data", [r"google translate"]),
 "Contact Form 7": ("API / standard / data", [r"contact form 7", r"\bcf7\b"]),
}

# Licensing: canonical tech -> (license, open-source alternative).
#   "open source" — the tool itself is OSS / an open standard; no alternative needed.
#   "commercial"  — proprietary; `alt` names a credible open-source replacement.
#   "hybrid"      — open-core / dual-licensed / open-standard-with-commercial-host;
#                   `alt` names the path to a fully open-source deployment.
# Alternatives are real, maintained OSS projects a NYC agency could actually adopt.
LIC = {
 # Platform / CMS
 "WordPress": ("open source", ""),
 "Drupal": ("open source", ""),
 "Progress Sitefinity": ("commercial", "Drupal or WordPress — OSS CMSs with strong government deployments (e.g. the govCMS Drupal distribution)"),
 "Smarty (PHP)": ("open source", ""),
 "Microsoft Dynamics 365": ("commercial", "Odoo or ERPNext (OSS CRM/ERP) for constituent & case management; Drupal for the public portal"),
 "Oracle WebCenter Sites": ("commercial", "Drupal or WordPress"),
 "DotNetNuke (DNN)": ("hybrid", "DNN Platform is open-source (MIT); replace the commercial Evoq tier with WordPress or Drupal"),
 "Adobe Experience Manager": ("commercial", "Drupal or WordPress"),
 "Weebly": ("commercial", "WordPress, Ghost, or Grav (flat-file OSS CMS)"),
 "Revize": ("commercial", "Drupal (govCMS distribution) or WordPress"),
 "NYC.gov Livesite": ("commercial", "Drupal (govCMS) or WordPress as the shared publishing platform"),
 # Framework / runtime
 "ASP.NET / IIS": ("hybrid", "ASP.NET Core (cross-platform, MIT) on Linux/nginx, or Node.js / Django — drops the Windows Server + IIS licensing"),
 "Java / Tomcat / WebLogic": ("hybrid", "Apache Tomcat or WildFly (OSS app servers) in place of Oracle WebLogic"),
 "Spring": ("open source", ""),
 "Next.js": ("open source", ""),
 "React": ("open source", ""),
 "Angular": ("open source", ""),
 "nginx": ("open source", ""),
 "Apache": ("open source", ""),
 # Hosting / CDN / edge
 "Akamai": ("commercial", "Apache Traffic Server (the OSS CDN used at scale) or self-managed nginx + Varnish edge cache"),
 "Cloudflare": ("commercial", "nginx + Varnish + Let's Encrypt for cache/TLS; ModSecurity + OWASP CRS for WAF"),
 "AWS CloudFront": ("commercial", "Apache Traffic Server or nginx caching in front of the origin"),
 "AWS (ALB/S3/EC2)": ("commercial", "Kubernetes / OpenStack on Linux; MinIO (S3-compatible OSS object store); HAProxy for load balancing"),
 "Microsoft Azure": ("commercial", "Kubernetes / OpenStack; MinIO for blob storage"),
 "WP Engine": ("commercial", "Self-hosted WordPress on nginx/Apache (DDEV/Lando for local dev)"),
 "Pantheon": ("commercial", "Self-hosted Drupal/WordPress with DDEV or Lando"),
 "Netlify": ("commercial", "Static hosting on nginx; Coolify or CapRover (OSS PaaS) for CI/deploy"),
 "Vercel": ("commercial", "Self-hosted Next.js on Node + nginx; Coolify (OSS PaaS)"),
 "Kinsta": ("commercial", "Self-hosted WordPress on nginx"),
 "SiteGround": ("commercial", "Self-hosted LEMP/LAMP stack"),
 "Fastly": ("commercial", "Varnish Cache (OSS) — Fastly is built on it — self-managed"),
 "Imperva": ("commercial", "ModSecurity + OWASP Core Rule Set (OSS WAF)"),
 "Varnish": ("open source", ""),
 "Oracle Cloud": ("commercial", "Kubernetes / OpenStack on Linux"),
 # Vendor SaaS / app
 "Accela": ("commercial", "Form.io + Camunda (OSS forms + BPM/workflow) as a build-your-own permitting/licensing stack"),
 "Salesforce": ("commercial", "SuiteCRM, EspoCRM, or Odoo (OSS CRM)"),
 "Oracle Siebel": ("commercial", "SuiteCRM or Odoo (OSS CRM)"),
 "Unqork": ("commercial", "Budibase, Appsmith, or ToolJet (OSS low-code app builders)"),
 "Kaseware": ("commercial", "Appsmith/Budibase over PostgreSQL for case management (no turnkey OSS equivalent)"),
 "Epic / MyChart": ("commercial", "OpenMRS or OpenEMR (OSS EHR); Bahmni for the patient-facing layer"),
 "PeopleSoft (CUNYfirst)": ("commercial", "Odoo or ERPNext (OSS ERP)"),
 "Legistar (Granicus)": ("commercial", "No turnkey OSS legislative suite; Councilmatic (OSS) can re-expose the record openly over an OSS database"),
 "Checkbook NYC": ("open source", ""),
 "Everbridge": ("commercial", "Novu (OSS notification infrastructure) wired to IPAWS/Twilio for multichannel alerts"),
 "Combined Arms": ("commercial", "An OpenReferral/HSDS directory (OSS) for the human-services referral graph"),
 "HawkSearch": ("commercial", "OpenSearch, Meilisearch, or Typesense (OSS search)"),
 "Viebit": ("commercial", "PeerTube or Owncast (OSS video streaming)"),
 "StreamText": ("commercial", "Self-hosted Whisper (OSS speech-to-text) for live/near-live captioning"),
 "BiblioCommons": ("commercial", "VuFind or Blacklight (OSS library discovery layers)"),
 "Communico": ("commercial", "Koha (OSS ILS) plus a custom events layer"),
 "OverDrive / hoopla": ("commercial", "The Palace Project / Library Simplified (OSS e-content platform, DPLA)"),
 "Preservica": ("commercial", "Archivematica + AtoM (OSS digital preservation + description)"),
 "LUNA Imaging": ("commercial", "Omeka S + IIIF viewers (Mirador / OpenSeadragon, OSS image collections)"),
 "Microsoft SharePoint": ("commercial", "Nextcloud (OSS document collaboration / intranet)"),
 "Microsoft Power BI": ("commercial", "Apache Superset, Metabase, or Grafana (OSS BI / dashboards)"),
 "Shopify": ("commercial", "Medusa, Saleor, or WooCommerce (OSS commerce)"),
 "Constant Contact": ("commercial", "Listmonk or Mautic (OSS email / newsletter)"),
 "WSO2 API Gateway": ("open source", ""),
 "Divi / GeneratePress / Themeco": ("commercial", "WordPress core block themes / full-site editing (GPL, no premium-builder lock-in)"),
 # Maps / geospatial
 "Esri ArcGIS": ("commercial", "QGIS + GeoServer/MapServer + PostGIS + Leaflet/MapLibre (OSS geospatial stack)"),
 "CARTO": ("commercial", "PostGIS + MapLibre/Leaflet; kepler.gl for exploration"),
 "Mapbox": ("commercial", "MapLibre GL (OSS fork of Mapbox GL) on OpenStreetMap tiles"),
 "Google Maps": ("commercial", "Leaflet or MapLibre + OpenStreetMap + Nominatim/Pelias geocoding"),
 "NYC GeoClient / GeoSearch": ("open source", ""),
 # Media / assets
 "Cloudinary": ("commercial", "imgproxy or Thumbor (OSS image transform/CDN) + MinIO/S3 storage"),
 "Azure Blob Storage": ("commercial", "MinIO (S3-compatible OSS object storage)"),
 # Analytics / monitoring
 "Google Tag Manager": ("commercial", "Matomo Tag Manager (OSS)"),
 "Google Analytics": ("commercial", "Matomo, Plausible, or Umami (OSS, privacy-friendly analytics)"),
 "Dynatrace": ("commercial", "OpenTelemetry + Prometheus + Grafana; SigNoz (OSS APM)"),
 "New Relic": ("commercial", "SigNoz, or OpenTelemetry + Grafana (Loki/Tempo/Prometheus)"),
 "Siteimprove": ("commercial", "axe-core, Pa11y, and Lighthouse CI (OSS accessibility / QA testing)"),
 "Matomo": ("open source", ""),
 "Loggly": ("commercial", "Grafana Loki or OpenSearch + Fluent Bit (OSS log aggregation)"),
 "Meta / Facebook Pixel": ("commercial", "Drop third-party tracking; first-party Matomo/Plausible if measurement is needed"),
 "Wordfence": ("hybrid", "Free tier suffices; the premium tier maps to ModSecurity + OWASP CRS (OSS WAF)"),
 # API / standard / data
 "Socrata / Tyler (SODA)": ("commercial", "CKAN (OSS open-data portal) — the standard open-source alternative to Socrata"),
 "WordPress REST API": ("open source", ""),
 "Drupal JSON:API": ("open source", ""),
 "FHIR / SMART on FHIR": ("open source", ""),
 "Open311 (GeoReport v2)": ("open source", ""),
 "api.nyc.gov (Azure APIM)": ("commercial", "Kong, Tyk, Apache APISIX, or Gravitee (OSS API gateways)"),
 "Google Translate": ("commercial", "LibreTranslate (OSS, self-hosted machine translation)"),
 "Contact Form 7": ("open source", ""),
}
# every detected tech must be licensed
assert set(TECH) == set(LIC), f"license map mismatch: {set(TECH) ^ set(LIC)}"

def blob(did):
    # Only the structured, domain-specific fields — NOT tech-stack.md prose, which
    # often name-drops the exemplar/other agencies for comparison (false positives).
    parts = [platform.get(did, "")]
    try:
        fr = json.load(open(f"{did}/fruit.json"))
        for a in fr.get("apis_observed", []):
            parts += [str(a.get("endpoint","")), str(a.get("type","")), str(a.get("owner","")), str(a.get("note",""))]
        parts.append((fr.get("meta", {}) or {}).get("tagline", ""))
        parts.append((fr.get("meta", {}) or {}).get("headline", ""))
    except Exception:
        pass
    return " \n ".join(parts).lower()

by_tech = collections.defaultdict(list)
by_domain_tech = {}
for d in DOMAINS:
    did = d["id"]; b = blob(did); found = []
    for tech, (cat, aliases) in TECH.items():
        if any(re.search(a, b) for a in aliases):
            by_tech[tech].append(did); found.append(tech)
    by_domain_tech[did] = sorted(found)

cats = collections.OrderedDict()
for tech, (cat, _) in TECH.items():
    cats.setdefault(cat, [])
    if tech in by_tech:
        cats[cat].append(tech)

detected = [t for t in by_tech]
lic_summary = collections.Counter(LIC[t][0] for t in detected)
# commercial/hybrid techs (in use) that have an OSS alternative, ranked by reach
alt_rows = sorted(
    [{"tech": t, "category": TECH[t][0], "license": LIC[t][0], "alternative": LIC[t][1],
      "count": len(by_tech[t]), "domains": [{"id": x, "short": short[x]} for x in by_tech[t]]}
     for t in detected if LIC[t][0] in ("commercial", "hybrid") and LIC[t][1]],
    key=lambda r: (-r["count"], r["tech"].lower()))

tech_json = {
    "generated_from": "meta.platform + apis_observed + tech-stack.md across all domains (keyword match)",
    "distinct_technologies": len(detected),
    "license_summary": {
        "commercial": lic_summary.get("commercial", 0),
        "open source": lic_summary.get("open source", 0),
        "hybrid": lic_summary.get("hybrid", 0),
        "with_oss_alternative": len(alt_rows),
    },
    "categories": [{"name": c, "techs": [
        {"tech": t, "category": c, "count": len(by_tech[t]),
         "license": LIC[t][0], "alternative": LIC[t][1],
         "domains": [{"id": x, "short": short[x]} for x in by_tech[t]]}
        for t in sorted(cats[c], key=str.lower)]} for c in cats if cats[c]],
    "alternatives": alt_rows,
    "byDomain": [{"id": d["id"], "short": d["short"], "platform": platform.get(d["id"], ""),
                  "techs": [{"tech": t, "license": LIC[t][0]} for t in by_domain_tech[d["id"]]]} for d in DOMAINS],
}
json.dump(tech_json, open("data/technology.json", "w"), indent=1)

ls = tech_json["license_summary"]
LICLABEL = {"open source": "🟢 open source", "hybrid": "🟡 hybrid", "commercial": "🔴 commercial"}
T = ["# Master Technology List\n",
     f"Every platform, framework, hosting/CDN, vendor SaaS, and API/standard detected across the **{len(DOMAINS)} assessed domains**, from each domain's platform fingerprint, observed APIs, and tech-stack inventory. **{tech_json['distinct_technologies']} distinct technologies.** Keyword-matched, so read as a strong signal, not a certified BOM. Interactive: [technology.html](https://nyc.apievangelist.com/technology.html).\n",
     f"Each technology is tagged **🟢 open source**, **🟡 hybrid** (open-core / dual-licensed / open standard with a commercial host), or **🔴 commercial** — {ls['open source']} open source, {ls['hybrid']} hybrid, {ls['commercial']} commercial. For every commercial or hybrid tool there's a credible **open-source alternative** a NYC agency could actually adopt.\n",
     "## Commercial & hybrid → open-source alternatives\n",
     f"The **{ls['with_oss_alternative']}** proprietary/open-core technologies in use, each with a recommended open-source replacement, ranked by how many domains run it.\n",
     "| Technology | License | # domains | Open-source alternative |",
     "|---|---|---|---|"]
for r in tech_json["alternatives"]:
    T.append(f"| **{r['tech']}** | {LICLABEL[r['license']]} | {r['count']} | {r['alternative']} |")
T.append("")
for c in tech_json["categories"]:
    T.append(f"## {c['name']}\n")
    T.append("| Technology | License | # domains | Open-source alternative | Domains |")
    T.append("|---|---|---|---|---|")
    for t in c["techs"]:
        T.append(f"| **{t['tech']}** | {LICLABEL[t['license']]} | {t['count']} | {t['alternative'] or '—'} | {', '.join(x['short'] for x in t['domains'])} |")
    T.append("")
open("TECHNOLOGY.md", "w").write("\n".join(T) + "\n")

print(f"entities: {entities_json['distinct_entities']} distinct ({entities_json['total_entities']} total)")
print(f"technology: {tech_json['distinct_technologies']} distinct across {len(tech_json['categories'])} categories")
print(f"licensing: {ls['open source']} open source · {ls['hybrid']} hybrid · {ls['commercial']} commercial · {ls['with_oss_alternative']} with OSS alternative")
print("top recurring entities:", [(e, len(d)) for e, d in ent_rows[:8]])
print("top technologies:", sorted(((t, len(v)) for t, v in by_tech.items()), key=lambda x: -x[1])[:10])
