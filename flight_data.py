import pandas as pd, glob
import os
import matplotlib.pyplot as plt

files = sorted(glob.glob("data/*.csv"))
df = pd.concat((pd.read_csv(f, encoding="utf-8-sig") for f in files), ignore_index=True)
df = df[df["number_flights_matched"] > 0]

late_cols = [c for c in df.columns if "minutes_late" in c and "0_to_15" not in c]
df["delayed_flights"] = df[late_cols].sum(axis=1) / 100 * df["number_flights_matched"]

monthly = df.groupby("reporting_period")[["delayed_flights", "number_flights_matched"]].sum()
monthly["delayed_share"] = monthly["delayed_flights"] / monthly["number_flights_matched"]
print(monthly)

os.makedirs("charts", exist_ok=True)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(months, monthly["delayed_share"] * 100)
ax.set_title("Share of UK flights more than 15 minutes late, 2025")
ax.set_xlabel("Month")
ax.set_ylabel("Delayed flights (%)")
plt.tight_layout()
plt.savefig("charts/delay_by_month.png", dpi=150)
plt.show()