import glob
import os

import matplotlib.pyplot as plt
import pandas as pd

# load all 12 monthly files into one table
files = sorted(glob.glob("data/*.csv"))
flights = pd.concat(
    (pd.read_csv(f, encoding="utf-8-sig") for f in files),
    ignore_index=True,
)

# routes with no flights that month add nothing
flights = flights[flights["number_flights_matched"] > 0]

# the delay columns are percentages of all scheduled flights on a route,
# so turn them back into counts before adding anything up
flights["total_flights"] = (
    flights["number_flights_matched"]
    + flights["actual_flights_unmatched"]
    + flights["number_flights_cancelled"]
)

# delayed = more than 15 minutes late (every late band except 0 to 15)
late_cols = [
    c for c in flights.columns
    if "minutes_late" in c and "0_to_15" not in c
]
flights["delayed_flights"] = (
    flights[late_cols].sum(axis=1) / 100 * flights["total_flights"]
)

# monthly totals and delay share
monthly = flights.groupby("reporting_period")[
    ["delayed_flights", "number_flights_matched"]
].sum()
monthly["delayed_share"] = (
    monthly["delayed_flights"] / monthly["number_flights_matched"]
)

print(monthly.round(4))

# quick check on how many flights were unmatched or cancelled
print(flights[[
    "number_flights_matched",
    "actual_flights_unmatched",
    "number_flights_cancelled",
]].sum())

# bar chart
os.makedirs("charts", exist_ok=True)
labels = pd.to_datetime(monthly.index.astype(str), format="%Y%m").strftime("%b")

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(labels, monthly["delayed_share"] * 100)
ax.set_title("Share of UK flights more than 15 minutes late, 2025")
ax.set_xlabel("Month")
ax.set_ylabel("Delayed flights (%)")
plt.tight_layout()
plt.savefig("charts/delay_by_month.png", dpi=150)
plt.show()