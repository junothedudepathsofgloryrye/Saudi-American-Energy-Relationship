import os, math, requests, pandas as pd, numpy as np, matplotlib.pyplot as plt, matplotlib.ticker as ticker
os.makedirs("Charts", exist_ok=True); os.makedirs("Data-Spreadsheets", exist_ok=True)
EIA_KEY = os.getenv("EIA_API_KEY", "rDdMKGPLzfChtQJWJJn9m7cfkqzKwRGk8NwwtN7M")
INFRA_NODES = {"Abqaiq": (25.9267, 49.6808), "Ras Tanura": (26.6439, 50.1592), "Yanbu": (23.9889, 38.2214), "East-West Pipeline": (24.7500, 44.5000), "Shaybah": (22.5167, 53.9500)}
def cite(fig, t): fig.text(0.01, 0.012, t, ha="left", va="bottom", fontsize=8, color="#444444", style="italic")
def hav(lat1, lon1, lat2, lon2):
    r = 6371.0; p1, p2 = math.radians(lat1), math.radians(lat2); dp = math.radians(lat2-lat1); dl = math.radians(lon2-lon1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*r*math.atan2(math.sqrt(a), math.sqrt(1-a))
arms = pd.DataFrame([{"Supplier":"United States","Share":77.0},{"Supplier":"France","Share":6.4},{"Supplier":"Spain","Share":4.9},{"Supplier":"China & Other","Share":11.7}])
arms.to_csv("Data-Spreadsheets/SIPRI-Saudi-Arms-Imports-Share-2021-2025.csv", index=False)
fig, ax = plt.subplots(figsize=(10.5,5.5))
bars = ax.barh(arms["Supplier"][::-1], arms["Share"][::-1], color=["#ed7d31","#5b9bd5","#2e75b6","#1f4e78"], height=0.55)
for b in bars: w=b.get_width(); ax.text(w+1.2, b.get_y()+b.get_height()/2, f"{w:.1f}%", va="center", fontsize=10, fontweight="bold")
ax.set_xlim(0,92); ax.set_title("Saudi Arabian Major Arms Imports Share by Supplier (2021-2025)", fontsize=11.5, fontweight="bold"); ax.set_xlabel("Share (%)"); ax.grid(axis="x", ls="--", alpha=0.4)
cite(fig, "Source: SIPRI, Trends in International Arms Transfers 2025 (March 2026).")
plt.tight_layout(rect=[0,0.04,1,1]); plt.savefig("Charts/5-SIPRI-Saudi-Arms-Dependency.png", dpi=300); plt.close(); print("Saved Chart 5")
r3 = requests.get("https://api.eia.gov/v2/petroleum/pri/spt/data/", params={"api_key":EIA_KEY,"frequency":"monthly","data[0]":"value","facets[series][]":"RBRTE","start":"2019-01","end":"2026-12","length":5000}, timeout=60).json().get("response",{}).get("data",[])
if r3:
    d3 = pd.DataFrame(r3); d3["Brent"] = pd.to_numeric(d3["value"], errors="coerce"); o3 = d3[["period","Brent"]].dropna().sort_values("period")
    o3.to_csv("Data-Spreadsheets/Brent-Crude-Monthly-Spot-Prices-2019-2026.csv", index=False)
    fig, ax = plt.subplots(figsize=(12.5,5.8)); ax.plot(o3["period"], o3["Brent"], lw=2.3, color="#1f4e78"); ax.set_xticks(o3["period"][::6]); ax.tick_params(axis="x", rotation=45)
    ax.set_title("Brent Crude Monthly Spot Price (2019-2026)", fontsize=12, fontweight="bold"); ax.set_ylabel("USD per Barrel ($/bbl)"); ax.grid(axis="y", ls="--", alpha=0.4)
    cite(fig, "Source: U.S. EIA Open Data API v2 (petroleum/pri/spt, Series RBRTE), 2019-2026.")
    plt.tight_layout(rect=[0,0.04,1,1]); plt.savefig("Charts/3-Brent-Crude-Price-Shocks.png", dpi=300); plt.close(); print("Saved Chart 3")
r1 = requests.get("https://api.eia.gov/v2/petroleum/move/impcus/data/", params={"api_key":EIA_KEY,"frequency":"annual","data[0]":"value","facets[product][]":"EPC0","facets[process][]":"IM0","facets[duoarea][]":["NUS-NSA","NUS-NCA"],"start":"1990","end":"2026","length":5000}, timeout=60).json().get("response",{}).get("data",[])
if r1:
    d1 = pd.DataFrame(r1); d1["Year"] = d1["period"].astype(int); d1["val"] = pd.to_numeric(d1["value"], errors="coerce").fillna(0)
    d1["Partner"] = d1["duoarea"].map({"NUS-NSA":"Saudi Arabia","NUS-NCA":"Canada"})
    piv = d1.pivot_table(index="Year", columns="Partner", values="val", aggfunc="mean", fill_value=0)
    piv.to_csv("Data-Spreadsheets/US-Crude-Imports-Saudi-vs-Canada-1990-2026.csv")
    fig, ax = plt.subplots(figsize=(12,5.8))
    if "Saudi Arabia" in piv.columns: ax.plot(piv.index, piv["Saudi Arabia"], marker="o", lw=2.5, color="#b22222", label="Saudi Arabia")
    if "Canada" in piv.columns: ax.plot(piv.index, piv["Canada"], marker="s", lw=2.5, color="#1f4e78", label="Canada")
    ax.axvline(2001, color="#555555", ls="--"); ax.set_title("U.S. Crude Oil Imports: Canada vs. Saudi Arabia (1990-2026)", fontsize=12, fontweight="bold")
    ax.set_ylabel(str(d1["units"].iloc[0])); ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}")); ax.legend(); ax.grid(axis="y", ls="--", alpha=0.4)
    cite(fig, "Source: U.S. EIA Open Data API v2 (petroleum/move/impcus, EPC0, IM0, NUS-NSA & NUS-NCA), 1990-2026.")
    plt.tight_layout(rect=[0,0.04,1,1]); plt.savefig("Charts/1-US-Crude-Imports-Saudi-vs-Canada.png", dpi=300); plt.close(); print("Saved Chart 1")
r2 = requests.get("https://api.eia.gov/v2/petroleum/sum/snd/data/", params={"api_key":EIA_KEY,"frequency":"annual","data[0]":"value","facets[product][]":"EPC0","start":"1990","end":"2026","length":5000}, timeout=60).json().get("response",{}).get("data",[])
if r2:
    d2 = pd.DataFrame(r2); d2["Year"] = d2["period"].astype(int); d2["val"] = pd.to_numeric(d2["value"], errors="coerce").fillna(0)
    o2 = d2.groupby("Year", as_index=False)["val"].mean().sort_values("Year"); o2.to_csv("Data-Spreadsheets/US-Total-Crude-Balance-1990-2026.csv", index=False)
    fig, ax = plt.subplots(figsize=(12,5.8)); ax.plot(o2["Year"], o2["val"], marker="o", lw=2.4, color="#1f4e78")
    ax.set_title("U.S. Crude Oil Supply / Balance Series (1990-2026)", fontsize=12, fontweight="bold")
    ax.set_ylabel(str(d2["units"].iloc[0])); ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}")); ax.grid(axis="y", ls="--", alpha=0.4)
    cite(fig, "Source: U.S. EIA Open Data API v2 (petroleum/sum/snd, EPC0), 1990-2026.")
    plt.tight_layout(rect=[0,0.04,1,1]); plt.savefig("Charts/2-US-Crude-Net-Exporter-Shift.png", dpi=300); plt.close(); print("Saved Chart 2")
gdelt_csv = "Data-Spreadsheets/Live-GDELT-Saudi-Oil-Infra-Proximity.csv"
q = "(Abqaiq OR Ras Tanura OR Yanbu OR Shaybah OR Aramco OR pipeline) (attack OR strike OR drone OR missile OR security)"
df_g = pd.DataFrame()
try:
    rg = requests.get("https://api.gdeltproject.org/api/v2/geo/geo", params={"query": q, "format": "geojson", "timespan": "3m"}, timeout=60)
    feats = rg.json().get("features", []) if rg.status_code == 200 else []
    rows = []
    for f in feats:
        coords = f.get("geometry", {}).get("coordinates", [])
        if len(coords) >= 2:
            lon, lat = float(coords[0]), float(coords[1])
            props = f.get("properties", {})
            dists = {k: hav(lat, lon, la, lo) for k, (la, lo) in INFRA_NODES.items()}
            nearest = min(dists, key=dists.get)
            rows.append({"name": props.get("name", ""), "lat": lat, "lon": lon, "nearest_node": nearest, "dist_km": round(dists[nearest], 2), "within_5km": dists[nearest] <= 5.0})
    if rows:
        df_g = pd.DataFrame(rows)
        df_g.to_csv(gdelt_csv, index=False)
    elif os.path.exists(gdelt_csv):
        df_g = pd.read_csv(gdelt_csv)
except Exception as e:
    if os.path.exists(gdelt_csv): df_g = pd.read_csv(gdelt_csv)
    print("GDELT note:", e)
if not df_g.empty:
    by_node = df_g.groupby(["nearest_node", "within_5km"]).size().unstack(fill_value=0)
    for c in [True, False]:
        if c not in by_node.columns: by_node[c] = 0
    by_node = by_node[[True, False]]; by_node.columns = ["Within 5 km", "Beyond 5 km"]
    fig, ax = plt.subplots(figsize=(11, 5.5))
    by_node.plot(kind="bar", stacked=True, ax=ax, color=["#b22222", "#1f4e78"], width=0.55)
    ax.set_title("Live GDELT Geolocated Reporting Near Saudi Oil Nodes (Last 3 Months)", fontsize=11.5, fontweight="bold")
    ax.set_ylabel("Geolocated Reports"); ax.tick_params(axis="x", rotation=20); ax.grid(axis="y", ls="--", alpha=0.4)
    cite(fig, "Source: GDELT 2.0 GEO API (live query), Haversine Distance to Saudi Oil Infrastructure Nodes.")
    plt.tight_layout(rect=[0, 0.04, 1, 1]); plt.savefig("Charts/4-Saudi-Export-Corridor-Capacity-and-Flows.png", dpi=300); plt.close(); print("Saved Chart 4")
print("CHARTS PRESENT:", sorted(os.listdir("Charts")))

import subprocess; subprocess.run(["python3", "-u", "scripts/build_synthesis.py"], check=False)

import re
rm = open("README.md", encoding="utf-8").read().replace(" -> ", " → ")
idx = re.sub(r"<details[^>]*>|</details>|<summary>.*?</summary>", "", rm, flags=re.DOTALL)
idx = re.sub(r"!\[([^\]]*)\]\((Charts/[^)\s]+)\)", r"<img src=\"{{ '/\2' | relative_url }}\" alt=\"\1\" style=\"max-width:100%; height:auto; display:block; margin:14px 0;\">", idx)
open("index.md", "w", encoding="utf-8").write(re.sub(r"\n{3,}", "\n\n", idx).strip() + "\n")

live_map_html = """\n### Live AIS Tanker Tracking: Strait of Hormuz & Persian Gulf Export Corridor\n\n<iframe name="vesselfinder" id="vesselfinder" width="100%" height="500" frameborder="0" src="https://www.vesselfinder.com/aismap?zoom=7&lat=26.35&lon=55.80&width=100%25&height=500&names=false&mmsi=0&imo=0&track=false&fleet=&fleet_name=&fleet_timespan=1440&fleet_hide_old_positions=false&clicktoact=false&store_pos=true&ra=false">Browser does not support embedded objects.<br/>Visit directly <a href="https://www.vesselfinder.com" target="_blank">www.vesselfinder.com</a></iframe>\n"""
with open("index.md", "r", encoding="utf-8") as f:
    cur_idx = f.read()
if "vesselfinder.com/aismap" not in cur_idx:
    with open("index.md", "w", encoding="utf-8") as f:
        f.write(cur_idx.strip() + "\n" + live_map_html)

subprocess.run(["python3", "-u", "scripts/build_live_saudi_panel.py"], check=False)
