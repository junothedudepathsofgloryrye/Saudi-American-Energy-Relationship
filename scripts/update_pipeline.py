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
ev_path = "Data-Spreadsheets/ACLED-Saudi-Kinetic-Events-2019-2026.csv"
if os.path.exists(ev_path):
    ev = pd.read_csv(ev_path)
    if not ev.empty:
        ev["lat"] = pd.to_numeric(ev["latitude"], errors="coerce"); ev["lon"] = pd.to_numeric(ev["longitude"], errors="coerce")
        ev["Year"] = pd.to_datetime(ev["event_date"]).dt.year
        ev["Min_Dist_km"] = ev.apply(lambda r: np.nan if (pd.isna(r["lat"]) or pd.isna(r["lon"])) else min(hav(r["lat"],r["lon"],la,lo) for la,lo in INFRA_NODES.values()), axis=1)
        ev["Within_5km"] = ev["Min_Dist_km"] <= 5.0
        yc = ev.groupby(["Year","Within_5km"]).size().unstack(fill_value=0)
        for c in [False,True]:
            if c not in yc.columns: yc[c] = 0
        yc = yc[[True,False]]; yc.columns = ["Within 5 km of Oil Infrastructure","Other Events in KSA"]
        fig, ax = plt.subplots(figsize=(11.5,5.8)); yc.plot(kind="bar", stacked=True, ax=ax, color=["#b22222","#1f4e78"], width=0.6)
        ax.set_title("Kinetic Events in Saudi Arabia by Proximity to Oil Infrastructure (2019-2026)", fontsize=11.5, fontweight="bold")
        ax.set_ylabel("Events"); ax.tick_params(axis="x", rotation=0); ax.grid(axis="y", ls="--", alpha=0.4)
        cite(fig, "Source: ACLED Dataset (Saudi Arabia), Haversine Distance to Saudi Oil Nodes, 2019-2026.")
        plt.tight_layout(rect=[0,0.04,1,1]); plt.savefig("Charts/4-ACLED-Saudi-Oil-Infrastructure-Proximity.png", dpi=300); plt.close(); print("Saved Chart 4")
print("CHARTS PRESENT:", os.listdir("Charts"))
