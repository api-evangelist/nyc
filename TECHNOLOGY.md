# Master Technology List

Every platform, framework, hosting/CDN, vendor SaaS, and API/standard detected across the **67 assessed domains**, from each domain's platform fingerprint, observed APIs, and tech-stack inventory. **78 distinct technologies.** Keyword-matched, so read as a strong signal, not a certified BOM. Interactive: [technology.html](https://nyc.apievangelist.com/technology.html).

Each technology is tagged **🟢 open source**, **🟡 hybrid** (open-core / dual-licensed / open standard with a commercial host), or **🔴 commercial** — 17 open source, 4 hybrid, 57 commercial. For every commercial or hybrid tool there's a credible **open-source alternative** a NYC agency could actually adopt.

## Commercial & hybrid → open-source alternatives

The **61** proprietary/open-core technologies in use, each with a recommended open-source replacement, ranked by how many domains run it.

| Technology | License | # domains | Open-source alternative |
|---|---|---|---|
| **Socrata / Tyler (SODA)** | 🔴 commercial | 66 | CKAN (OSS open-data portal) — the standard open-source alternative to Socrata |
| **Dynatrace** | 🔴 commercial | 41 | OpenTelemetry + Prometheus + Grafana; SigNoz (OSS APM) |
| **Akamai** | 🔴 commercial | 39 | Apache Traffic Server (the OSS CDN used at scale) or self-managed nginx + Varnish edge cache |
| **NYC.gov Livesite** | 🔴 commercial | 36 | Drupal (govCMS) or WordPress as the shared publishing platform |
| **AWS (ALB/S3/EC2)** | 🔴 commercial | 13 | Kubernetes / OpenStack on Linux; MinIO (S3-compatible OSS object store); HAProxy for load balancing |
| **ASP.NET / IIS** | 🟡 hybrid | 12 | ASP.NET Core (cross-platform, MIT) on Linux/nginx, or Node.js / Django — drops the Windows Server + IIS licensing |
| **Cloudflare** | 🔴 commercial | 12 | nginx + Varnish + Let's Encrypt for cache/TLS; ModSecurity + OWASP CRS for WAF |
| **Microsoft Azure** | 🔴 commercial | 10 | Kubernetes / OpenStack; MinIO for blob storage |
| **Esri ArcGIS** | 🔴 commercial | 6 | QGIS + GeoServer/MapServer + PostGIS + Leaflet/MapLibre (OSS geospatial stack) |
| **Divi / GeneratePress / Themeco** | 🔴 commercial | 5 | WordPress core block themes / full-site editing (GPL, no premium-builder lock-in) |
| **WP Engine** | 🔴 commercial | 5 | Self-hosted WordPress on nginx/Apache (DDEV/Lando for local dev) |
| **api.nyc.gov (Azure APIM)** | 🔴 commercial | 4 | Kong, Tyk, Apache APISIX, or Gravitee (OSS API gateways) |
| **AWS CloudFront** | 🔴 commercial | 4 | Apache Traffic Server or nginx caching in front of the origin |
| **Google Maps** | 🔴 commercial | 4 | Leaflet or MapLibre + OpenStreetMap + Nominatim/Pelias geocoding |
| **Java / Tomcat / WebLogic** | 🟡 hybrid | 4 | Apache Tomcat or WildFly (OSS app servers) in place of Oracle WebLogic |
| **Salesforce** | 🔴 commercial | 4 | SuiteCRM, EspoCRM, or Odoo (OSS CRM) |
| **Wordfence** | 🟡 hybrid | 4 | Free tier suffices; the premium tier maps to ModSecurity + OWASP CRS (OSS WAF) |
| **Google Analytics** | 🔴 commercial | 3 | Matomo, Plausible, or Umami (OSS, privacy-friendly analytics) |
| **Accela** | 🔴 commercial | 2 | Form.io + Camunda (OSS forms + BPM/workflow) as a build-your-own permitting/licensing stack |
| **Azure Blob Storage** | 🔴 commercial | 2 | MinIO (S3-compatible OSS object storage) |
| **BiblioCommons** | 🔴 commercial | 2 | VuFind or Blacklight (OSS library discovery layers) |
| **CARTO** | 🔴 commercial | 2 | PostGIS + MapLibre/Leaflet; kepler.gl for exploration |
| **Constant Contact** | 🔴 commercial | 2 | Listmonk or Mautic (OSS email / newsletter) |
| **Google Tag Manager** | 🔴 commercial | 2 | Matomo Tag Manager (OSS) |
| **HawkSearch** | 🔴 commercial | 2 | OpenSearch, Meilisearch, or Typesense (OSS search) |
| **Legistar (Granicus)** | 🔴 commercial | 2 | No turnkey OSS legislative suite; Councilmatic (OSS) can re-expose the record openly over an OSS database |
| **PeopleSoft (CUNYfirst)** | 🔴 commercial | 2 | Odoo or ERPNext (OSS ERP) |
| **Adobe Experience Manager** | 🔴 commercial | 1 | Drupal or WordPress |
| **Cloudinary** | 🔴 commercial | 1 | imgproxy or Thumbor (OSS image transform/CDN) + MinIO/S3 storage |
| **Combined Arms** | 🔴 commercial | 1 | An OpenReferral/HSDS directory (OSS) for the human-services referral graph |
| **Communico** | 🔴 commercial | 1 | Koha (OSS ILS) plus a custom events layer |
| **DotNetNuke (DNN)** | 🟡 hybrid | 1 | DNN Platform is open-source (MIT); replace the commercial Evoq tier with WordPress or Drupal |
| **Epic / MyChart** | 🔴 commercial | 1 | OpenMRS or OpenEMR (OSS EHR); Bahmni for the patient-facing layer |
| **Everbridge** | 🔴 commercial | 1 | Novu (OSS notification infrastructure) wired to IPAWS/Twilio for multichannel alerts |
| **Google Translate** | 🔴 commercial | 1 | LibreTranslate (OSS, self-hosted machine translation) |
| **Imperva** | 🔴 commercial | 1 | ModSecurity + OWASP Core Rule Set (OSS WAF) |
| **Kaseware** | 🔴 commercial | 1 | Appsmith/Budibase over PostgreSQL for case management (no turnkey OSS equivalent) |
| **Kinsta** | 🔴 commercial | 1 | Self-hosted WordPress on nginx |
| **Loggly** | 🔴 commercial | 1 | Grafana Loki or OpenSearch + Fluent Bit (OSS log aggregation) |
| **LUNA Imaging** | 🔴 commercial | 1 | Omeka S + IIIF viewers (Mirador / OpenSeadragon, OSS image collections) |
| **Mapbox** | 🔴 commercial | 1 | MapLibre GL (OSS fork of Mapbox GL) on OpenStreetMap tiles |
| **Microsoft Dynamics 365** | 🔴 commercial | 1 | Odoo or ERPNext (OSS CRM/ERP) for constituent & case management; Drupal for the public portal |
| **Microsoft Power BI** | 🔴 commercial | 1 | Apache Superset, Metabase, or Grafana (OSS BI / dashboards) |
| **Microsoft SharePoint** | 🔴 commercial | 1 | Nextcloud (OSS document collaboration / intranet) |
| **Netlify** | 🔴 commercial | 1 | Static hosting on nginx; Coolify or CapRover (OSS PaaS) for CI/deploy |
| **New Relic** | 🔴 commercial | 1 | SigNoz, or OpenTelemetry + Grafana (Loki/Tempo/Prometheus) |
| **Oracle Cloud** | 🔴 commercial | 1 | Kubernetes / OpenStack on Linux |
| **Oracle Siebel** | 🔴 commercial | 1 | SuiteCRM or Odoo (OSS CRM) |
| **Oracle WebCenter Sites** | 🔴 commercial | 1 | Drupal or WordPress |
| **OverDrive / hoopla** | 🔴 commercial | 1 | The Palace Project / Library Simplified (OSS e-content platform, DPLA) |
| **Pantheon** | 🔴 commercial | 1 | Self-hosted Drupal/WordPress with DDEV or Lando |
| **Preservica** | 🔴 commercial | 1 | Archivematica + AtoM (OSS digital preservation + description) |
| **Progress Sitefinity** | 🔴 commercial | 1 | Drupal or WordPress — OSS CMSs with strong government deployments (e.g. the govCMS Drupal distribution) |
| **Revize** | 🔴 commercial | 1 | Drupal (govCMS distribution) or WordPress |
| **Shopify** | 🔴 commercial | 1 | Medusa, Saleor, or WooCommerce (OSS commerce) |
| **SiteGround** | 🔴 commercial | 1 | Self-hosted LEMP/LAMP stack |
| **StreamText** | 🔴 commercial | 1 | Self-hosted Whisper (OSS speech-to-text) for live/near-live captioning |
| **Unqork** | 🔴 commercial | 1 | Budibase, Appsmith, or ToolJet (OSS low-code app builders) |
| **Vercel** | 🔴 commercial | 1 | Self-hosted Next.js on Node + nginx; Coolify (OSS PaaS) |
| **Viebit** | 🔴 commercial | 1 | PeerTube or Owncast (OSS video streaming) |
| **Weebly** | 🔴 commercial | 1 | WordPress, Ghost, or Grav (flat-file OSS CMS) |

## Platform / CMS

| Technology | License | # domains | Open-source alternative | Domains |
|---|---|---|---|---|
| **Adobe Experience Manager** | 🔴 commercial | 1 | Drupal or WordPress | NYC Small Business Services (SBS) |
| **DotNetNuke (DNN)** | 🟡 hybrid | 1 | DNN Platform is open-source (MIT); replace the commercial Evoq tier with WordPress or Drupal | NYC School Construction Authority (SCA) |
| **Drupal** | 🟢 open source | 6 | — | NYC Board of Elections, NYC Transportation (DOT), NYC Comptroller, Brooklyn Public Library (BPL), NYC Economic Development (EDC), Queens Public Library (QPL) |
| **Microsoft Dynamics 365** | 🔴 commercial | 1 | Odoo or ERPNext (OSS CRM/ERP) for constituent & case management; Drupal for the public portal | NYC311 |
| **NYC.gov Livesite** | 🔴 commercial | 36 | Drupal (govCMS) or WordPress as the shared publishing platform | NYC Taxi & Limousine (TLC), NYC Housing Authority (NYCHA), NYC Children's Services (ACS), NYC Business Integrity Commission (BIC), Bronx Borough President, Bronx District Attorney, NYC Standards & Appeals (BSA), NYC Human Rights (CCHR), NYC Civilian Complaint Review (CCRB), NYC Conflicts of Interest Board (COIB), NYC Citywide Admin Services (DCAS), NYC Cultural Affairs (DCLA), NYC Consumer & Worker Protection (DCWP), NYC Design & Construction (DDC), NYC Environmental Protection (DEP), NYC Aging (DFTA), NYC Homeless Services (DHS), NYC Correction (DOC), NYC Finance (DOF), NYC Investigation (DOI), NYC Records (DORIS), NYC Veterans' Services (DVS), NYC Youth & Community Dev (DYCD), NYC Fire (FDNY), NYC Social Services (HRA), NYC Law Department, NYC Landmarks (LPC), NYC Criminal Justice (MOCJ), NYC Media & Entertainment (MOME), NYC Emergency Management (NYCEM), NYC Admin Trials & Hearings (OATH), NYC Medical Examiner (OCME), NYC Technology & Innovation (OTI), NYC Public Advocate, NYC Small Business Services (SBS), NYC Tax Commission |
| **Oracle WebCenter Sites** | 🔴 commercial | 1 | Drupal or WordPress | NYPD |
| **Progress Sitefinity** | 🔴 commercial | 1 | Drupal or WordPress — OSS CMSs with strong government deployments (e.g. the govCMS Drupal distribution) | NYC Public Schools (DOE) |
| **Revize** | 🔴 commercial | 1 | Drupal (govCMS distribution) or WordPress | Bronx Borough President |
| **Weebly** | 🔴 commercial | 1 | WordPress, Ghost, or Grav (flat-file OSS CMS) | Staten Island Borough President |
| **WordPress** | 🟢 open source | 12 | — | NYC Council, NYC Comptroller, Brooklyn Borough President, Brooklyn District Attorney, City University of New York (CUNY), NYC Social Services (HRA), Manhattan Borough President, Manhattan District Attorney, NYC Criminal Justice (MOCJ), Queens Borough President, Queens District Attorney, Staten Island District Attorney |

## Framework / runtime

| Technology | License | # domains | Open-source alternative | Domains |
|---|---|---|---|---|
| **Angular** | 🟢 open source | 5 | — | NYC Health (DOHMH), NYPD, NYC Campaign Finance Board (CFB), NYC City Clerk, NYC Youth & Community Dev (DYCD) |
| **Apache** | 🟢 open source | 4 | — | NYC Buildings (DOB), Brooklyn District Attorney, NYC Correction (DOC), NYC Admin Trials & Hearings (OATH) |
| **ASP.NET / IIS** | 🟡 hybrid | 12 | ASP.NET Core (cross-platform, MIT) on Linux/nginx, or Node.js / Django — drops the Windows Server + IIS licensing | NYC Housing (HPD), NYC Health (DOHMH), NYC Sanitation (DSNY), NYC Campaign Finance Board (CFB), NYC Citywide Admin Services (DCAS), NYC Environmental Protection (DEP), NYC Finance (DOF), NYC Youth & Community Dev (DYCD), NYC Fire (FDNY), NYC Health + Hospitals, NYC Media & Entertainment (MOME), NYC School Construction Authority (SCA) |
| **Java / Tomcat / WebLogic** | 🟡 hybrid | 4 | Apache Tomcat or WildFly (OSS app servers) in place of Oracle WebLogic | NYC Buildings (DOB), Bronx Borough President, NYC Correction (DOC), NYC Admin Trials & Hearings (OATH) |
| **Next.js** | 🟢 open source | 4 | — | NYC Parks & Recreation, Brooklyn Borough President, NYC Veterans' Services (DVS), NYC Public Advocate |
| **nginx** | 🟢 open source | 38 | — | NYC Buildings (DOB), NYC Housing Authority (NYCHA), NYC Children's Services (ACS), NYC Business Integrity Commission (BIC), NYC Standards & Appeals (BSA), NYC Human Rights (CCHR), NYC Civilian Complaint Review (CCRB), NYC City Clerk, NYC Conflicts of Interest Board (COIB), City University of New York (CUNY), NYC Citywide Admin Services (DCAS), NYC Cultural Affairs (DCLA), NYC Consumer & Worker Protection (DCWP), NYC Design & Construction (DDC), NYC Environmental Protection (DEP), NYC Aging (DFTA), NYC Homeless Services (DHS), NYC Correction (DOC), NYC Finance (DOF), NYC Investigation (DOI), NYC Records (DORIS), NYC Veterans' Services (DVS), NYC Youth & Community Dev (DYCD), NYC Fire (FDNY), NYC Social Services (HRA), NYC Independent Budget Office (IBO), NYC Law Department, NYC Landmarks (LPC), NYC Criminal Justice (MOCJ), NYC Media & Entertainment (MOME), NYC Emergency Management (NYCEM), New York Public Library (NYPL), NYC Admin Trials & Hearings (OATH), NYC Medical Examiner (OCME), NYC Technology & Innovation (OTI), NYC Public Advocate, NYC Small Business Services (SBS), NYC Tax Commission |
| **React** | 🟢 open source | 3 | — | NYC Sanitation (DSNY), NYC Social Services (HRA), New York Public Library (NYPL) |
| **Spring** | 🟢 open source | 3 | — | NYC Consumer & Worker Protection (DCWP), Queens Public Library (QPL), NYC Small Business Services (SBS) |

## Hosting / CDN / edge

| Technology | License | # domains | Open-source alternative | Domains |
|---|---|---|---|---|
| **Akamai** | 🔴 commercial | 39 | Apache Traffic Server (the OSS CDN used at scale) or self-managed nginx + Varnish edge cache | NYC Buildings (DOB), NYC Transportation (DOT), NYC Sanitation (DSNY), NYPD, NYC Housing Authority (NYCHA), NYC Children's Services (ACS), NYC Business Integrity Commission (BIC), Bronx District Attorney, NYC Standards & Appeals (BSA), NYC Human Rights (CCHR), NYC Civilian Complaint Review (CCRB), NYC City Clerk, NYC Conflicts of Interest Board (COIB), NYC Citywide Admin Services (DCAS), NYC Cultural Affairs (DCLA), NYC Consumer & Worker Protection (DCWP), NYC Design & Construction (DDC), NYC Environmental Protection (DEP), NYC Aging (DFTA), NYC Homeless Services (DHS), NYC Correction (DOC), NYC Finance (DOF), NYC Investigation (DOI), NYC Records (DORIS), NYC Veterans' Services (DVS), NYC Youth & Community Dev (DYCD), NYC Fire (FDNY), NYC Social Services (HRA), NYC Independent Budget Office (IBO), NYC Law Department, NYC Landmarks (LPC), NYC Criminal Justice (MOCJ), NYC Media & Entertainment (MOME), NYC Emergency Management (NYCEM), NYC Admin Trials & Hearings (OATH), NYC Medical Examiner (OCME), NYC Technology & Innovation (OTI), NYC Small Business Services (SBS), NYC Tax Commission |
| **AWS (ALB/S3/EC2)** | 🔴 commercial | 13 | Kubernetes / OpenStack on Linux; MinIO (S3-compatible OSS object store); HAProxy for load balancing | NYC Taxi & Limousine (TLC), Bronx District Attorney, NYC Standards & Appeals (BSA), NYC Human Rights (CCHR), NYC Civilian Complaint Review (CCRB), NYC City Clerk, NYC Design & Construction (DDC), NYC Youth & Community Dev (DYCD), NYC Landmarks (LPC), New York Public Library (NYPL), NYC Medical Examiner (OCME), NYC School Construction Authority (SCA), NYC Tax Commission |
| **AWS CloudFront** | 🔴 commercial | 4 | Apache Traffic Server or nginx caching in front of the origin | NYC Parks & Recreation, NYC Taxi & Limousine (TLC), NYC Veterans' Services (DVS), NYC Economic Development (EDC) |
| **Cloudflare** | 🔴 commercial | 12 | nginx + Varnish + Let's Encrypt for cache/TLS; ModSecurity + OWASP CRS for WAF | Brooklyn Public Library (BPL), Brooklyn Borough President, NYC Citywide Admin Services (DCAS), NYC Investigation (DOI), NYC Economic Development (EDC), NYC Fire (FDNY), NYC Social Services (HRA), Manhattan Borough President, NYC Criminal Justice (MOCJ), Queens Borough President, Queens District Attorney, Staten Island Borough President |
| **Imperva** | 🔴 commercial | 1 | ModSecurity + OWASP Core Rule Set (OSS WAF) | New York Public Library (NYPL) |
| **Kinsta** | 🔴 commercial | 1 | Self-hosted WordPress on nginx | Queens District Attorney |
| **Microsoft Azure** | 🔴 commercial | 10 | Kubernetes / OpenStack; MinIO for blob storage | NYC Public Schools (DOE), NYC311, NYPD, NYC City Planning (DCP), NYC Campaign Finance Board (CFB), NYC Citywide Admin Services (DCAS), NYC Environmental Protection (DEP), NYC Fire (FDNY), NYC Technology & Innovation (OTI), NYC School Construction Authority (SCA) |
| **Netlify** | 🔴 commercial | 1 | Static hosting on nginx; Coolify or CapRover (OSS PaaS) for CI/deploy | NYC City Planning (DCP) |
| **Oracle Cloud** | 🔴 commercial | 1 | Kubernetes / OpenStack on Linux | Bronx Borough President |
| **Pantheon** | 🔴 commercial | 1 | Self-hosted Drupal/WordPress with DDEV or Lando | NYC Transportation (DOT) |
| **SiteGround** | 🔴 commercial | 1 | Self-hosted LEMP/LAMP stack | Staten Island District Attorney |
| **Vercel** | 🔴 commercial | 1 | Self-hosted Next.js on Node + nginx; Coolify (OSS PaaS) | NYC Public Advocate |
| **WP Engine** | 🔴 commercial | 5 | Self-hosted WordPress on nginx/Apache (DDEV/Lando for local dev) | Brooklyn Borough President, NYC Social Services (HRA), Manhattan Borough President, NYC Criminal Justice (MOCJ), Queens Borough President |

## Vendor SaaS / app

| Technology | License | # domains | Open-source alternative | Domains |
|---|---|---|---|---|
| **Accela** | 🔴 commercial | 2 | Form.io + Camunda (OSS forms + BPM/workflow) as a build-your-own permitting/licensing stack | NYC Health (DOHMH), NYC Fire (FDNY) |
| **BiblioCommons** | 🔴 commercial | 2 | VuFind or Blacklight (OSS library discovery layers) | Brooklyn Public Library (BPL), Queens Public Library (QPL) |
| **Checkbook NYC** | 🟢 open source | 2 | — | NYC Comptroller, NYC Design & Construction (DDC) |
| **Combined Arms** | 🔴 commercial | 1 | An OpenReferral/HSDS directory (OSS) for the human-services referral graph | NYC Veterans' Services (DVS) |
| **Communico** | 🔴 commercial | 1 | Koha (OSS ILS) plus a custom events layer | Queens Public Library (QPL) |
| **Constant Contact** | 🔴 commercial | 2 | Listmonk or Mautic (OSS email / newsletter) | Bronx Borough President, Staten Island Borough President |
| **Divi / GeneratePress / Themeco** | 🔴 commercial | 5 | WordPress core block themes / full-site editing (GPL, no premium-builder lock-in) | Brooklyn District Attorney, Manhattan Borough President, Queens Borough President, Queens District Attorney, Staten Island District Attorney |
| **Epic / MyChart** | 🔴 commercial | 1 | OpenMRS or OpenEMR (OSS EHR); Bahmni for the patient-facing layer | NYC Health + Hospitals |
| **Everbridge** | 🔴 commercial | 1 | Novu (OSS notification infrastructure) wired to IPAWS/Twilio for multichannel alerts | NYC Emergency Management (NYCEM) |
| **HawkSearch** | 🔴 commercial | 2 | OpenSearch, Meilisearch, or Typesense (OSS search) | NYC Parks & Recreation, NYC Public Schools (DOE) |
| **Kaseware** | 🔴 commercial | 1 | Appsmith/Budibase over PostgreSQL for case management (no turnkey OSS equivalent) | NYC Investigation (DOI) |
| **Legistar (Granicus)** | 🔴 commercial | 2 | No turnkey OSS legislative suite; Councilmatic (OSS) can re-expose the record openly over an OSS database | NYC Council, NYC Public Advocate |
| **LUNA Imaging** | 🔴 commercial | 1 | Omeka S + IIIF viewers (Mirador / OpenSeadragon, OSS image collections) | NYC Records (DORIS) |
| **Microsoft Power BI** | 🔴 commercial | 1 | Apache Superset, Metabase, or Grafana (OSS BI / dashboards) | Bronx District Attorney |
| **Microsoft SharePoint** | 🔴 commercial | 1 | Nextcloud (OSS document collaboration / intranet) | NYC School Construction Authority (SCA) |
| **Oracle Siebel** | 🔴 commercial | 1 | SuiteCRM or Odoo (OSS CRM) | NYC Housing Authority (NYCHA) |
| **OverDrive / hoopla** | 🔴 commercial | 1 | The Palace Project / Library Simplified (OSS e-content platform, DPLA) | Queens Public Library (QPL) |
| **PeopleSoft (CUNYfirst)** | 🔴 commercial | 2 | Odoo or ERPNext (OSS ERP) | City University of New York (CUNY), NYC Citywide Admin Services (DCAS) |
| **Preservica** | 🔴 commercial | 1 | Archivematica + AtoM (OSS digital preservation + description) | NYC Records (DORIS) |
| **Salesforce** | 🔴 commercial | 4 | SuiteCRM, EspoCRM, or Odoo (OSS CRM) | NYC Health (DOHMH), NYC Business Integrity Commission (BIC), NYC Cultural Affairs (DCLA), NYC Landmarks (LPC) |
| **Shopify** | 🔴 commercial | 1 | Medusa, Saleor, or WooCommerce (OSS commerce) | NYC Citywide Admin Services (DCAS) |
| **StreamText** | 🔴 commercial | 1 | Self-hosted Whisper (OSS speech-to-text) for live/near-live captioning | NYC Council |
| **Unqork** | 🔴 commercial | 1 | Budibase, Appsmith, or ToolJet (OSS low-code app builders) | NYC City Clerk |
| **Viebit** | 🔴 commercial | 1 | PeerTube or Owncast (OSS video streaming) | NYC Council |
| **WSO2 API Gateway** | 🟢 open source | 1 | — | NYC Housing (HPD) |

## Maps / geospatial

| Technology | License | # domains | Open-source alternative | Domains |
|---|---|---|---|---|
| **CARTO** | 🔴 commercial | 2 | PostGIS + MapLibre/Leaflet; kepler.gl for exploration | NYC Council, NYC City Planning (DCP) |
| **Esri ArcGIS** | 🔴 commercial | 6 | QGIS + GeoServer/MapServer + PostGIS + Leaflet/MapLibre (OSS geospatial stack) | NYC Public Schools (DOE), NYC Housing (HPD), NYC Health (DOHMH), NYC Sanitation (DSNY), NYC Independent Budget Office (IBO), NYC Landmarks (LPC) |
| **Google Maps** | 🔴 commercial | 4 | Leaflet or MapLibre + OpenStreetMap + Nominatim/Pelias geocoding | NYC Children's Services (ACS), NYC Conflicts of Interest Board (COIB), NYC Cultural Affairs (DCLA), NYC Youth & Community Dev (DYCD) |
| **Mapbox** | 🔴 commercial | 1 | MapLibre GL (OSS fork of Mapbox GL) on OpenStreetMap tiles | NYC City Planning (DCP) |
| **NYC GeoClient / GeoSearch** | 🟢 open source | 4 | — | NYC311, NYC Housing (HPD), NYC City Planning (DCP), NYC Technology & Innovation (OTI) |

## Media / assets

| Technology | License | # domains | Open-source alternative | Domains |
|---|---|---|---|---|
| **Azure Blob Storage** | 🔴 commercial | 2 | MinIO (S3-compatible OSS object storage) | NYC Public Schools (DOE), NYC School Construction Authority (SCA) |
| **Cloudinary** | 🔴 commercial | 1 | imgproxy or Thumbor (OSS image transform/CDN) + MinIO/S3 storage | NYC Parks & Recreation |

## Analytics / monitoring

| Technology | License | # domains | Open-source alternative | Domains |
|---|---|---|---|---|
| **Dynatrace** | 🔴 commercial | 41 | OpenTelemetry + Prometheus + Grafana; SigNoz (OSS APM) | NYC Buildings (DOB), NYC Transportation (DOT), NYC Health (DOHMH), NYC Sanitation (DSNY), NYPD, NYC Taxi & Limousine (TLC), NYC Housing Authority (NYCHA), NYC Children's Services (ACS), NYC Business Integrity Commission (BIC), Bronx District Attorney, NYC Standards & Appeals (BSA), NYC Human Rights (CCHR), NYC Civilian Complaint Review (CCRB), NYC City Clerk, NYC Conflicts of Interest Board (COIB), NYC Citywide Admin Services (DCAS), NYC Cultural Affairs (DCLA), NYC Consumer & Worker Protection (DCWP), NYC Design & Construction (DDC), NYC Environmental Protection (DEP), NYC Aging (DFTA), NYC Homeless Services (DHS), NYC Correction (DOC), NYC Finance (DOF), NYC Investigation (DOI), NYC Records (DORIS), NYC Veterans' Services (DVS), NYC Youth & Community Dev (DYCD), NYC Fire (FDNY), NYC Social Services (HRA), NYC Independent Budget Office (IBO), NYC Law Department, NYC Landmarks (LPC), NYC Criminal Justice (MOCJ), NYC Media & Entertainment (MOME), NYC Emergency Management (NYCEM), NYC Admin Trials & Hearings (OATH), NYC Medical Examiner (OCME), NYC Technology & Innovation (OTI), NYC Small Business Services (SBS), NYC Tax Commission |
| **Google Analytics** | 🔴 commercial | 3 | Matomo, Plausible, or Umami (OSS, privacy-friendly analytics) | NYC Housing (HPD), Bronx Borough President, Bronx District Attorney |
| **Google Tag Manager** | 🔴 commercial | 2 | Matomo Tag Manager (OSS) | NYC Housing (HPD), Bronx Borough President |
| **Loggly** | 🔴 commercial | 1 | Grafana Loki or OpenSearch + Fluent Bit (OSS log aggregation) | NYC Parks & Recreation |
| **Matomo** | 🟢 open source | 1 | — | Queens District Attorney |
| **New Relic** | 🔴 commercial | 1 | SigNoz, or OpenTelemetry + Grafana (Loki/Tempo/Prometheus) | NYC Comptroller |
| **Wordfence** | 🟡 hybrid | 4 | Free tier suffices; the premium tier maps to ModSecurity + OWASP CRS (OSS WAF) | Brooklyn Borough President, Brooklyn District Attorney, Manhattan District Attorney, Queens Borough President |

## API / standard / data

| Technology | License | # domains | Open-source alternative | Domains |
|---|---|---|---|---|
| **api.nyc.gov (Azure APIM)** | 🔴 commercial | 4 | Kong, Tyk, Apache APISIX, or Gravitee (OSS API gateways) | NYC311, NYC Housing (HPD), NYC City Planning (DCP), NYC Technology & Innovation (OTI) |
| **Contact Form 7** | 🟢 open source | 3 | — | Manhattan District Attorney, NYC Criminal Justice (MOCJ), Staten Island District Attorney |
| **Drupal JSON:API** | 🟢 open source | 3 | — | NYC Board of Elections, NYC Transportation (DOT), Brooklyn Public Library (BPL) |
| **FHIR / SMART on FHIR** | 🟢 open source | 1 | — | NYC Health + Hospitals |
| **Google Translate** | 🔴 commercial | 1 | LibreTranslate (OSS, self-hosted machine translation) | NYC Sanitation (DSNY) |
| **Open311 (GeoReport v2)** | 🟢 open source | 1 | — | NYC311 |
| **Socrata / Tyler (SODA)** | 🔴 commercial | 66 | CKAN (OSS open-data portal) — the standard open-source alternative to Socrata | NYC Parks & Recreation, NYC Public Schools (DOE), NYC Council, NYC Board of Elections, NYC311, NYC Buildings (DOB), NYC Housing (HPD), NYC Transportation (DOT), NYC Health (DOHMH), NYC Sanitation (DSNY), NYPD, NYC Taxi & Limousine (TLC), NYC City Planning (DCP), NYC Comptroller, NYC Housing Authority (NYCHA), NYC Children's Services (ACS), NYC Business Integrity Commission (BIC), Brooklyn Public Library (BPL), Bronx Borough President, Bronx District Attorney, Brooklyn Borough President, Brooklyn District Attorney, NYC Standards & Appeals (BSA), NYC Human Rights (CCHR), NYC Civilian Complaint Review (CCRB), NYC Campaign Finance Board (CFB), NYC City Clerk, NYC Conflicts of Interest Board (COIB), City University of New York (CUNY), NYC Citywide Admin Services (DCAS), NYC Cultural Affairs (DCLA), NYC Consumer & Worker Protection (DCWP), NYC Design & Construction (DDC), NYC Environmental Protection (DEP), NYC Aging (DFTA), NYC Homeless Services (DHS), NYC Correction (DOC), NYC Finance (DOF), NYC Investigation (DOI), NYC Records (DORIS), NYC Veterans' Services (DVS), NYC Youth & Community Dev (DYCD), NYC Economic Development (EDC), NYC Fire (FDNY), NYC Health + Hospitals, NYC Social Services (HRA), NYC Independent Budget Office (IBO), NYC Law Department, NYC Landmarks (LPC), Manhattan Borough President, NYC Criminal Justice (MOCJ), NYC Media & Entertainment (MOME), NYC Emergency Management (NYCEM), New York Public Library (NYPL), NYC Admin Trials & Hearings (OATH), NYC Medical Examiner (OCME), NYC Technology & Innovation (OTI), NYC Public Advocate, Queens Borough President, Queens District Attorney, Queens Public Library (QPL), NYC Small Business Services (SBS), NYC School Construction Authority (SCA), Staten Island Borough President, Staten Island District Attorney, NYC Tax Commission |
| **WordPress REST API** | 🟢 open source | 11 | — | NYC Council, NYC Comptroller, Brooklyn Borough President, Brooklyn District Attorney, City University of New York (CUNY), Manhattan Borough President, Manhattan District Attorney, NYC Criminal Justice (MOCJ), Queens Borough President, Queens District Attorney, Staten Island District Attorney |

