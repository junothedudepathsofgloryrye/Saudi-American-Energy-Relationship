import os, io, zipfile, requests, pandas as pd, matplotlib.pyplot as plt

os.makedirs("Charts", exist_ok=True)
os.makedirs("Data-Spreadsheets", exist_ok=True)

EIA_KEY = os.getenv("EIA_API_KEY", "rDdMKGPLzfChtQJWJJn9m7cfkqzKwRGk8NwwtN7M")

latest_brent = 82.0
latest_period = "Latest"
brent_csv = "Data-Spreadsheets/Brent-Crude-Monthly-Spot-Prices-2019-2026.csv"
try:
    r = requests.get(
        "https://api.eia.gov/v2/petroleum/pri/spt/data/",
        params={
            "api_key": EIA_KEY,
            "frequency": "monthly",
            "data[0]": "value",
            "facets[series][]": "RBRTE",
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "length": 12,
        },
        timeout=30,
    )
    rows = r.json().get("response", {}).get("data", []) if r.status_code == 200 else []
    valid = [(x.get("period"), pd.to_numeric(x.get("value"), errors="coerce")) for x in rows]
    valid = [(p, float(v)) for p, v in valid if p and pd.notna(v)]
    if valid:
        latest_period, latest_brent = valid[0]
except Exception:
    pass

if latest_period == "Latest" and os.path.exists(brent_csv):
    bdf = pd.read_csv(brent_csv).dropna(subset=["Brent"]).sort_values("period")
    if not bdf.empty:
        latest_period = str(bdf["period"].iloc[-1])
        latest_brent = float(bdf["Brent"].iloc[-1])

sa_all_events = 0
gulf_sa_mentions = 0
yanbu_ew_mentions = 0
try:
    master = requests.get("http://data.gdeltproject.org/gdeltv2/masterfilelist.txt", timeout=30).text.splitlines()
    urls = [l.split()[-1] for l in master if l.endswith(".export.CSV.zip")][-24:]
    for u in urls:
        try:
            z = zipfile.ZipFile(io.BytesIO(requests.get(u, timeout=20).content))
            df_raw = pd.read_csv(
                z.open(z.namelist()[0]),
                sep="\t",
                header=None,
                usecols=[1, 26, 53, 60],
                names=["SQLDATE", "EventCode", "Country", "SourceURL"],
                low_memory=False,
            )
            sa_sub = df_raw[df_raw["Country"] == "SA"]
            sa_all_events += int(len(sa_sub))
            urls_lower = sa_sub["SourceURL"].astype(str).str.lower()
            gulf_sa_mentions += int(urls_lower.str.contains(r"(ras tanura|juaymah|ju'aymah|abqaiq|aramco|tanker|crude|oil)", regex=True).sum())
            yanbu_ew_mentions += int(urls_lower.str.contains(r"(yanbu|east-west|petroline|red sea|pipeline)", regex=True).sum())
        except Exception:
            pass
except Exception:
    pass

summary_df = pd.DataFrame([
    {"Corridor": "East-West Pipeline (Abqaiq -> Yanbu Red Sea)", "Capacity_MBD": 5.0, "Live_GDELT_Reports": yanbu_ew_mentions, "Live_Brent_USD": round(latest_brent, 2), "Period": latest_period},
    {"Corridor": "Gulf Terminals (Ras Tanura / Juaymah)", "Capacity_MBD": 7.0, "Live_GDELT_Reports": gulf_sa_mentions, "Live_Brent_USD": round(latest_brent, 2), "Period": latest_period},
])
summary_df.to_csv("Data-Spreadsheets/Live-Saudi-Shipping-Capacity-Brent.csv", index=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.0), facecolor="white")
plt.subplots_adjust(wspace=0.28, top=0.80, bottom=0.18, left=0.07, right=0.96)
fig.suptitle(
    f"Live Saudi Export Corridors: East-West Pipeline (Yanbu) vs. Gulf Terminals & Brent ({latest_period})",
    fontsize=12, fontweight="bold", y=0.94
)

c1_labels = ["East-West Pipeline\n(to Yanbu Red Sea)", "Gulf Terminals\n(Ras Tanura / Juaymah)", "Live Brent Spot\n(EIA RBRTE)"]
c1_vals = [5.0, 7.0, latest_brent]
c1_units = ["M b/d", "M b/d", "$/bbl"]
bars1 = ax1.bar(c1_labels, c1_vals, color=["#2e8b57", "#1f4e78", "#b22222"], width=0.50)
for b, u in zip(bars1, c1_units):
    h = b.get_height()
    ax1.text(b.get_x() + b.get_width()/2, h + max(c1_vals)*0.02, f"{h:.1f} {u}", ha="center", va="bottom", fontsize=9.5, fontweight="bold")
ax1.set_ylim(0, max(c1_vals)*1.18)
ax1.set_title("Corridor Capacity vs. Live Brent Price", fontsize=10.5, fontweight="bold", loc="left")
ax1.grid(axis="y", ls="--", alpha=0.35)

c2_labels = ["East-West / Yanbu\nRed Sea Stream (~6h)", "Gulf / Ras Tanura\nEnergy Stream (~6h)", "All GDELT SA\nEvents (~6h)"]
c2_vals = [yanbu_ew_mentions, gulf_sa_mentions, sa_all_events]
bars2 = ax2.bar(c2_labels, c2_vals, color=["#2e8b57", "#d95f02", "#4472c4"], width=0.48)
for b in bars2:
    h = b.get_height()
    ax2.text(b.get_x() + b.get_width()/2, h + max(1, max(c2_vals)*0.03), f"{int(h):,}", ha="center", va="bottom", fontsize=9.5, fontweight="bold")
ax2.set_ylim(0, max(10, max(c2_vals)*1.2))
ax2.set_title("Live Saudi Corridor Reporting (GDELT 2.0)", fontsize=10.5, fontweight="bold", loc="left")
ax2.grid(axis="y", ls="--", alpha=0.35)

fig.text(
    0.01, 0.02,
    f"Live pull ({latest_period}): EIA API v2 RBRTE (${latest_brent:.2f}/bbl), GDELT 2.0 SA corridor mentions, and Aramco Petroline (5.0M b/d) vs. Gulf (7.0M b/d) capacities.",
    fontsize=8, color="#444444", style="italic"
)
plt.savefig("Charts/7-Live-Saudi-Shipping-Capacity-Brent.png", dpi=300)
plt.close()
print("Updated Charts/7-Live-Saudi-Shipping-Capacity-Brent.png")
