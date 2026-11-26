import csv
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime

os.makedirs("Data-Spreadsheets", exist_ok=True)
OUT_CSV = "Data-Spreadsheets/Recent-Saudi-Maritime-Pipeline-Incidents.csv"

existing_rows = []
if os.path.exists(OUT_CSV):
    with open(OUT_CSV, encoding="utf-8") as f:
        existing_rows = list(csv.DictReader(f))

query = '("Ras Tanura" OR "East-West pipeline" OR "Petroline" OR "Yanbu" OR "Jazan port" OR "Hormuz") (attack OR strike OR drone OR missile OR fire OR intercepted OR mine)'
params = urllib.parse.urlencode({
    "query": query,
    "mode": "ArtList",
    "maxrecords": "15",
    "format": "json",
    "sort": "DateDesc",
})
url = f"https://api.gdeltproject.org/api/v2/doc/doc?{params}"

live_rows = []
seen_titles = set()
try:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    for art in data.get("articles", []):
        title = (art.get("title") or "").strip()
        src_url = (art.get("url") or "").strip()
        seen_date = (art.get("seendate") or "")[:8]
        if not title or not src_url or title.lower() in seen_titles:
            continue
        seen_titles.add(title.lower())
        low = title.lower()
        if "pipeline" in low or "petroline" in low or "pumping station" in low:
            cat = "PIPELINE"
            node = "East-West Pipeline (Petroline)"
        elif "tanker" in low or "vessel" in low or "hormuz" in low or "mine" in low:
            cat = "TANKER"
            node = "Strait of Hormuz / Red Sea"
        else:
            cat = "PORT"
            node = "Ras Tanura" if "ras tanura" in low else ("Jazan Port" if "jazan" in low else ("Yanbu Terminal" if "yanbu" in low else "Saudi Export Terminal"))
        dt_fmt = f"{seen_date[:4]}-{seen_date[4:6]}-{seen_date[6:8]}" if len(seen_date) == 8 else datetime.utcnow().strftime("%Y-%m-%d")
        live_rows.append({
            "Date": dt_fmt,
            "Category": cat,
            "Node": node,
            "Summary": title[:165],
            "Market_Impact": f"Live GDELT ({art.get('domain', 'wire')})",
            "Source_URL": src_url,
        })
        if len(live_rows) >= 4:
            break
except Exception as exc:
    print(f"GDELT DOC fetch fallback: {exc}")

merged = []
seen_urls = set()
for row in live_rows + existing_rows:
    u = row.get("Source_URL", "")
    if u and u in seen_urls:
        continue
    seen_urls.add(u)
    merged.append(row)
    if len(merged) == 4:
        break

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Date", "Category", "Node", "Summary", "Market_Impact", "Source_URL"])
    writer.writeheader()
    writer.writerows(merged)

print(f"Wrote {len(merged)} rows to {OUT_CSV}")
