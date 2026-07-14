import json, glob, os, urllib.request, ssl, concurrent.futures as cf
SCRATCH = "/private/tmp/claude-501/-Users-kinlane-GitHub/f37428a9-6b61-4b1a-a6af-cf8142a0f513/scratchpad"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE

# merge all result files
data = {}
for f in sorted(glob.glob(f"{SCRATCH}/excel-results*.json")):
    for dom, items in json.load(open(f)).items():
        data.setdefault(dom, [])
        seen = {i["url"] for i in data[dom]}
        for it in items:
            if it["url"] not in seen:
                data[dom].append(it); seen.add(it["url"])

def check(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                ct = (r.headers.get("Content-Type") or "").lower()
                ok = r.status < 400 and ("html" not in ct)
                return ok, r.status, ct[:40]
        except Exception as e:
            if method == "GET":
                return False, "ERR", str(e)[:40]
    return False, "ERR", ""

# verify all urls in parallel
allurls = [(d, it) for d, items in data.items() for it in items]
results = {}
with cf.ThreadPoolExecutor(max_workers=12) as ex:
    futs = {ex.submit(check, it["url"]): (d, it["url"]) for d, it in allurls}
    for fu in cf.as_completed(futs):
        d, u = futs[fu]; results[u] = fu.result()

added_total = dropped = 0
summary = []
for dom, items in data.items():
    fp = f"{dom}/fruit.json"
    if not os.path.exists(fp):
        summary.append((dom, "NO fruit.json", 0)); continue
    j = json.load(open(fp))
    key = "fruit" if "fruit" in j else "items"
    arr = j.get(key, [])
    existing = {i.get("url") for i in arr}
    add = 0
    for it in items:
        ok, st, ct = results.get(it["url"], (False, "?", ""))
        if not ok:
            dropped += 1; continue
        if it["url"] in existing:
            continue
        arr.append(it); existing.add(it["url"]); add += 1
    if add:
        j[key] = arr
        json.dump(j, open(fp, "w"), indent=1)
    added_total += add
    summary.append((dom, f"+{add}", len(items)))

print(f"TOTAL added: {added_total} | dropped (failed verify): {dropped}")
for dom, a, n in sorted(summary, key=lambda x: x[0]):
    print(f"  {dom:22} {a:5} (of {n} returned)")
