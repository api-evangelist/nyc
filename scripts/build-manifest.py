#!/usr/bin/env python3
"""Regenerate data/manifest.json from the repo's domain artifacts.
Run from repo root: python3 scripts/build-manifest.py
Add a new domain by (1) creating its <domain>/ folder with the standard
artifacts and (2) adding an entry to META + ORDER below."""
import json, glob, os, re, sys
try:
    import yaml
except ImportError:
    print("pyyaml required (pip install pyyaml)"); sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

META = {
 "nycgovparks.org": {"verb":"Replatform","platform":"Smarty 2.6.2 / jQuery (legacy PHP)","short":"NYC Parks & Recreation","netnew":"PermitApplication","accent":"#3098d8",
   "tagline":"Data-rich but rendered as HTML; a legacy delivery layer with one modern island (the Next.js Tree Map). Modernize by replatforming behind a resource API."},
 "schools.nyc.gov": {"verb":"Reclaim","platform":"Progress Sitefinity (.NET)","short":"NYC Public Schools (DOE)","netnew":"EnrollmentApplication","accent":"#e0803a",
   "tagline":"638 Open Data assets, yet search is rented to a vendor (HawkSearch) and the backend is hidden behind an internal API. Modernize by reclaiming those capabilities."},
 "council.nyc.gov": {"verb":"Consolidate & Own","platform":"WordPress / WP Engine","short":"NYC Council","netnew":"TestimonyRegistration","accent":"#7a5cc0",
   "tagline":"The most API-covered domain — three APIs (Legistar, WordPress REST, Open Data), none owned or unified. Modernize by consolidating them behind one owned contract."},
 "vote.nyc": {"verb":"Digitize","platform":"Drupal 9","short":"NYC Board of Elections","netnew":"BallotRequest","accent":"#c0504d",
   "tagline":"The least-modernized: no site API, only 2 Open Data assets; results and candidates are PDFs. Modernize by digitizing the data that does not yet exist."},
 "nyc311": {"verb":"Standardize","platform":"Microsoft Dynamics 365","short":"NYC311","netnew":"ServiceRequest (Open311)","accent":"#1f9e8f",
   "tagline":"The flagship 311 dataset is the most-used in the city, but the interactive Open311 standard NYC once ran is retired and the service is a vendor CRM. Modernize by reviving the open standard."},
 "dob": {"verb":"Transact","platform":"aNNN-*.nyc.gov legacy app layer (BIS/DOB NOW, Java/Tomcat) behind Akamai","short":"NYC Buildings (DOB)","netnew":"PermitApplication","accent":"#b07d3a",
   "tagline":"A mature transactional core (BIS Web, DOB NOW) with no public API — only a nightly one-way Open Data batch dump. The app layer IS the legacy surface. Modernize by fronting it with one owned live API + a permit-filing write."},
 "hpd": {"verb":"Expose","platform":"Angular SPA over a private owned REST API (WSO2 gateway) + NYC GeoSearch","short":"NYC Housing (HPD)","netnew":"HousingLotteryApplication","accent":"#3f8f6a",
   "tagline":"HPD already runs a modern, owned, versioned REST API — kept private behind one Angular app while the public surface is 47 flattened snapshots and a closed lottery. Modernize by exposing what exists."},
 "dot": {"verb":"Unify","platform":"Legacy .shtml on nyc.gov + Drupal (nycstreetdesign.info); Socrata data","short":"NYC Transportation (DOT)","netnew":"StreetWorkPermit","accent":"#c99a1f",
   "tagline":"More open data than any NYC domain (267 assets) but as scattered flat snapshots + map-only visualizations keyed to a street SegmentID never exposed as a queryable network API."},
 "dohmh": {"verb":"Transact","platform":"NYC.gov CMS over Accela COTS + ASP.NET apps on a816-*.nyc.gov","short":"NYC Health (DOHMH)","netnew":"VitalRecordRequest","accent":"#c85a86",
   "tagline":"The most-liberated data in the city (81 datasets incl. restaurant inspections), yet transactions — ordering a birth/death certificate — are locked in siloed legacy apps with no API."},
 "dsny": {"verb":"Expose","platform":"Oracle WebCenter Sites + React forms over ASP.NET backends","short":"NYC Sanitation (DSNY)","netnew":"BulkPickupRequest","accent":"#5f9e42",
   "tagline":"DSNY already runs first-party lookup and pickup-scheduling APIs — undocumented backends behind React forms, waiting to be surfaced as one owned, agent-native contract."},
 "nypd": {"verb":"Expose","platform":"Oracle WebCenter Sites + Angular SPAs on an undocumented Azure Gov backend","short":"NYPD","netnew":"PoliceReportRequest","accent":"#2f5fb0",
   "tagline":"The most data-rich domain, yet its record ships as flattened Open Data snapshots and its live surfaces are trapped in Angular apps on an undocumented backend."},
 "tlc": {"verb":"Operationalize","platform":"NYC.gov CMS; Socrata + a CloudFront/S3 parquet trip-record host","short":"NYC Taxi & Limousine (TLC)","netnew":"LicenseApplication","accent":"#d99a2a",
   "tagline":"A world-famous open-data producer whose data ships as monthly parquet dumps and flat snapshots, never a queryable, transactional API."},
 "dcp": {"verb":"Anchor","platform":"nyc.gov + Netlify Planning Labs apps (ZoLa) on CARTO/Mapbox; open-source geocoder; GeoClient on Azure APIM","short":"NYC City Planning (DCP)","netnew":"— reference agency (owned /geocode)","accent":"#6f8aad",
   "tagline":"The source of the city's shared geography — BBL, community districts, NTAs, census tracts, council/election boundaries — so it should be the explicit, owned base every other domain's schemas reference."},
 "comptroller.nyc.gov": {"verb":"Consolidate & Own","platform":"WordPress (Comptroller) + Drupal (Checkbook NYC), both behind Imperva","short":"NYC Comptroller","netnew":"ClaimFiling","accent":"#2fa08f",
   "tagline":"Already runs a real public API (Checkbook NYC, XML) + 15 Open Data assets + an eClaim form, but nothing is a unified, JSON-first, agent-native contract."},
 "nycha": {"verb":"Unlock","platform":"NYC.gov Livesite + Oracle Siebel CRM Self-Service portal","short":"NYC Housing Authority (NYCHA)","netnew":"WorkOrder","accent":"#8a5fb0",
   "tagline":"Reference data is wide open on Open Data, but every resident transaction is locked inside a vendor Siebel CRM with no API."},
}
ORDER = ["nycgovparks.org","schools.nyc.gov","council.nyc.gov","vote.nyc","nyc311",
         "dob","hpd","dot","dohmh","dsny","nypd","tlc","dcp","comptroller.nyc.gov","nycha"]

def load(p): return json.load(open(p))

# Auto-discover every domain folder (any dir with a fruit.json). Keep ORDER first
# (the curated 15), then append newly-added domains alphabetically. New domains
# self-describe via a "meta" block in their fruit.json (written by the assessment).
_discovered = sorted(os.path.dirname(f) for f in glob.glob("*/fruit.json"))
DOMAINS = list(ORDER) + [d for d in _discovered if d not in ORDER]

domains=[]
for d in DOMAINS:
    if not os.path.isdir(d) or not os.path.exists(f"{d}/fruit.json"): continue
    fruit=load(f"{d}/fruit.json")
    od_files=glob.glob(f"{d}/opendata-*.json")
    od=load(od_files[0]) if od_files else []
    schemas=[]
    for sp in sorted(glob.glob(f"{d}/schemas/*.json")):
        base=os.path.basename(sp); sd=load(sp)
        schemas.append({"file":f"schemas/{base}","title":sd.get("title",base),
                        "shared":base=="_common.json","desc":(sd.get("description","")[:140])})
    oa_ops=[]; oa_file=None
    for op in glob.glob(f"{d}/openapi/*.yaml"):
        oa_file=f"openapi/{os.path.basename(op)}"; doc=yaml.safe_load(open(op))
        for path,methods in doc.get("paths",{}).items():
            for mth,spec in methods.items():
                if isinstance(spec,dict) and "operationId" in spec:
                    oa_ops.append({"method":mth.upper(),"path":path,"op":spec["operationId"],
                                   "summary":spec.get("summary",""),"tags":spec.get("tags",[]),
                                   "write":mth.lower() in ("post","put","patch","delete")})
    mcp_tools=[]; mcp_file=None
    for mp in glob.glob(f"{d}/mcp/*mcp*.json"):
        mcp_file=f"mcp/{os.path.basename(mp)}"; md=load(mp)
        for t in md.get("tools",[]):
            mcp_tools.append({"name":t["name"],"title":t.get("title",t["name"]),
                              "desc":t.get("description","")[:160],
                              "write":not t.get("annotations",{}).get("readOnlyHint",True)})
    docs=[os.path.basename(f) for f in sorted(glob.glob(f"{d}/*.md")) if os.path.basename(f)!="README.md"]
    ents=[]
    for it in fruit.get("fruit",[]):
        e=it.get("entity")
        if e and e not in ents: ents.append(e)
    m=META.get(d) or fruit.get("meta",{})  # curated 15, else self-described in fruit.json
    domains.append({"id":d,"agency":fruit.get("agency",d),"short":m.get("short",d),
        "verb":m.get("verb",""),"platform":m.get("platform",""),"tagline":m.get("tagline",""),
        "accent":m.get("accent","#3098d8"),"netnew":m.get("netnew",""),
        "findings":fruit.get("headline_findings",[]),"apis_observed":fruit.get("apis_observed",[]),
        "counts":{"fruit":len(fruit.get("fruit",[])),"opendata":len(od),
                  "schemas":len([s for s in schemas if not s.get("shared")]),
                  "openapiOps":len(oa_ops),"mcpTools":len(mcp_tools),"entities":len(ents)},
        "entities":ents,
        "files":{"fruit":f"{d}/fruit.json","opendata":(od_files[0] if od_files else None),
                 "docs":docs,"openapi":oa_file,"mcp":mcp_file},
        "schemas":schemas,"openapiOps":oa_ops,"mcpTools":mcp_tools})

inv=open("domains.md").read()
inv_count=len(set(re.findall(r'\b[a-z0-9][a-z0-9.-]+\.(?:gov|nyc|us|org|com|info|edu|net)\b', inv)) - {"apievangelist.com","github.com"})

manifest={
 "project":{"title":"NYC — Digital Modernization","site":"nyc.apievangelist.com",
   "repo":"https://github.com/api-evangelist/nyc",
   "tagline":"Mapping the digital surface of New York City government and turning it into an API-first, copilot, and agent-native layer — assessing the gap that lives across existing city government domains, and the current open data efforts within the public commons."},
 "thesis":{"heading":"Not another data-liberation project",
   "body":"From 2010–2018 the open-data movement (Socrata, Obama-era directives, NYC's Open Data law) pushed cities to publish data. It only partially worked: data got published but stayed disconnected from the front door, read-only, unproductized, and not agent-ready. This project is step two — unify what exists behind resource-oriented APIs, complete the missing write workflows, and expose it all through MCP so agents are first-class consumers. Make the city programmable."},
 "method":[
   {"n":1,"t":"Low-hanging-fruit assessment","d":"Outside-in crawl; index every table, form, and data file as name · type · URL · entity."},
   {"n":2,"t":"Technology & vendor inventory","d":"Fingerprint the CMS, hosting, CDN, analytics, and any outsourced capabilities."},
   {"n":3,"t":"APIs-observed inventory","d":"Document every backend/service API the site calls while crawling."},
   {"n":4,"t":"Open Data crosswalk","d":"Match each resource to existing data.cityofnewyork.us datasets; separate gaps from disconnects."},
   {"n":5,"t":"JSON Schema per object","d":"One canonical schema file per entity, reconciling website columns with Open Data schemas."},
   {"n":6,"t":"OpenAPI","d":"A resource-oriented contract that $refs each object schema; reads over unified data, writes for missing workflows."},
   {"n":7,"t":"MCP","d":"Expose the same resources as agent tools (design artifact, not a deployment)."}],
 "inventory":{"count":inv_count,"doc":"domains.md",
   "note":"Distinct registrable domains/subdomains catalogued; the true surface is larger (~100 agencies mostly under nyc.gov/site/* paths, plus hundreds of aNNN-*.nyc.gov app hosts)."},
 "domains":domains,
}
json.dump(manifest, open("data/manifest.json","w"), indent=1)
print("wrote data/manifest.json —", len(domains), "domains, inventory", inv_count)
for d in domains: print(" ", d["id"], d["counts"])
