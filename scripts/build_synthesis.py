import os, pandas as pd, numpy as np, matplotlib.pyplot as plt, matplotlib.ticker as ticker

os.makedirs("Charts", exist_ok=True)
os.makedirs("Data-Spreadsheets", exist_ok=True)

# 1. Load existing pipeline CSVs
imp = pd.read_csv("Data-Spreadsheets/US-Crude-Imports-Saudi-vs-Canada-1990-2026.csv")
bal = pd.read_csv("Data-Spreadsheets/US-Total-Crude-Balance-1990-2026.csv")
brent = pd.read_csv("Data-Spreadsheets/Brent-Crude-Monthly-Spot-Prices-2019-2026.csv")
arms = pd.read_csv("Data-Spreadsheets/SIPRI-Saudi-Arms-Imports-Share-2021-2025.csv")

gdelt_path = "Data-Spreadsheets/Live-GDELT-Saudi-Oil-Infra-Proximity.csv"
gdelt = pd.read_csv(gdelt_path) if os.path.exists(gdelt_path) else pd.DataFrame()

# 2. Harmonize on annual index (1990-2026)
years = pd.DataFrame({"Year": range(1990, 2027)})
master = years.merge(imp, on="Year", how="left")
bal_col = [c for c in bal.columns if c != "Year"][0]
master = master.merge(bal.rename(columns={bal_col: "US_Crude_Balance"}), on="Year", how="left")

brent["Year"] = brent["period"].astype(str).str[:4].astype(int)
brent_yr = brent.groupby("Year", as_index=False)["Brent"].mean().rename(columns={"Brent": "Brent_Annual_Avg_USD"})
master = master.merge(brent_yr, on="Year", how="left")

if "Saudi Arabia" in master.columns and "Canada" in master.columns:
    master["Saudi_to_Canada_Import_Ratio"] = (master["Saudi Arabia"] / master["Canada"].replace(0, np.nan)).round(3)

master["US_Arms_Share_Pct_2021_2025"] = float(arms.loc[arms["Supplier"] == "United States", "Share"].iloc[0])
master["Live_GDELT_SA_Events"] = int(len(gdelt))
master["Live_GDELT_Within_5km_Nodes"] = int(gdelt["within_5km"].sum()) if (not gdelt.empty and "within_5km" in gdelt.columns) else 0

master.to_csv("Data-Spreadsheets/Master-US-Saudi-Security-Matrix.csv", index=False)
print("Saved Data-Spreadsheets/Master-US-Saudi-Security-Matrix.csv")

# 3. Render 4-Panel Executive Synthesis Figure
fig = plt.figure(figsize=(15, 9.5), facecolor="white")
gs = fig.add_gridspec(2, 2, hspace=0.34, wspace=0.22, top=0.87, bottom=0.08, left=0.07, right=0.96)

fig.suptitle(
    "U.S.-Saudi Energy Security Synthesis: Physical Decoupling vs. Price Risk & Asymmetric Arms Dependency",
    fontsize=13.5, fontweight="bold", y=0.95
)
fig.text(
    0.5, 0.912,
    "Integrating EIA Crude Flows (1990-2026), Brent Price Shocks (2019-2026), Live GDELT Infrastructure Proximity & SIPRI Arms Transfers (2021-2025)",
    ha="center", fontsize=9.5, color="#444444"
)

# Panel A: Crude Import Displacement
ax1 = fig.add_subplot(gs[0, 0])
if "Canada" in master.columns:
    ax1.plot(master["Year"], master["Canada"], color="#1f4e78", lw=2.3, marker="s", markersize=3.5, label="Canada")
if "Saudi Arabia" in master.columns:
    ax1.plot(master["Year"], master["Saudi Arabia"], color="#b22222", lw=2.3, marker="o", markersize=3.5, label="Saudi Arabia")
ax1.axvline(2001, color="#555555", ls="--", lw=1.1)
ax1.text(2001.5, ax1.get_ylim()[1]*0.86, "2001 Crossover", fontsize=8, color="#333333", fontweight="bold")
ax1.set_title("A. Physical Decoupling: U.S. Crude Imports (1990-2026)", fontsize=10.5, fontweight="bold", loc="left")
ax1.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
ax1.grid(axis="y", ls="--", alpha=0.35)
ax1.legend(frameon=True, fontsize=8.5)

# Panel B: U.S. Supply / Net-Exporter Shift
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(master["Year"], master["US_Crude_Balance"], color="#2e75b6", lw=2.4, marker="o", markersize=3.5)
ax2.axvline(2019, color="#b22222", ls="--", lw=1.1)
ax2.text(2019.4, master["US_Crude_Balance"].dropna().max()*0.92, "2019 Net-Exporter Shift", fontsize=8, color="#b22222", fontweight="bold")
ax2.set_title("B. Domestic Insulation: U.S. Crude Balance Trajectory (1990-2026)", fontsize=10.5, fontweight="bold", loc="left")
ax2.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
ax2.grid(axis="y", ls="--", alpha=0.35)

# Panel C: Brent Price Shocks & Live GDELT Infrastructure Proximity
ax3 = fig.add_subplot(gs[1, 0])
b_sub = master.dropna(subset=["Brent_Annual_Avg_USD"])
ax3.bar(b_sub["Year"].astype(str), b_sub["Brent_Annual_Avg_USD"], color="#4472c4", alpha=0.85, width=0.55, label="Brent Annual Avg ($/bbl)")
ax3.set_title("C. Global Price Exposure & Live Saudi Infra Alerts (2019-2026)", fontsize=10.5, fontweight="bold", loc="left")
ax3.set_ylabel("Brent Spot ($/bbl)", fontsize=9)
ax3.grid(axis="y", ls="--", alpha=0.35)
tot_ev = int(len(gdelt))
near_ev = int(gdelt["within_5km"].sum()) if (not gdelt.empty and "within_5km" in gdelt.columns) else 0
ax3.text(
    0.03, 0.88,
    f"Live GDELT SA Stream: {tot_ev} events ({near_ev} <= 5 km of oil nodes)",
    transform=ax3.transAxes, fontsize=8.5, fontweight="bold", color="#7f0000",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff2f2", edgecolor="#b22222", lw=0.9)
)

# Panel D: Asymmetric Security Bargain (SIPRI Arms Share)
ax4 = fig.add_subplot(gs[1, 1])
arms_s = arms.iloc[::-1]
colors = ["#d9d9d9", "#8faadc", "#4472c4", "#b22222"]
bars = ax4.barh(arms_s["Supplier"], arms_s["Share"], color=colors[:len(arms_s)], height=0.52)
for b in bars:
    w = b.get_width()
    ax4.text(w + 1.5, b.get_y() + b.get_height()/2, f"{w:.1f}%", va="center", fontsize=9, fontweight="bold")
ax4.set_xlim(0, 95)
ax4.set_title("D. Asymmetric Bargain: Saudi Major Arms Imports (2021-2025)", fontsize=10.5, fontweight="bold", loc="left")
ax4.set_xlabel("Share of Saudi Arms Imports (%)", fontsize=9)
ax4.grid(axis="x", ls="--", alpha=0.35)

fig.text(
    0.01, 0.015,
    "Sources: U.S. EIA Open Data API v2 (impcus, sum/snd, pri/spt RBRTE); GDELT 2.0 Master Event Stream (SA); SIPRI Arms Transfers (2021-2025).",
    fontsize=8, color="#444444", style="italic"
)

plt.savefig("Charts/0-US-Saudi-Energy-Security-Synthesis.png", dpi=300)
plt.close()
print("Saved Charts/0-US-Saudi-Energy-Security-Synthesis.png")
