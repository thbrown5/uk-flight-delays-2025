# UK airport delays by month

## Question

Which months have the highest share of delayed flights at UK airports.

## Data

- Source: UK Civil Aviation Authority, airport punctuality statistics
- Period: January 2025 to December 2025
- Size: [number of rows] rows, [number of columns] columns
- Link: https://www.caa.co.uk/data-and-analysis/uk-aviation-market/flight-punctuality/uk-flight-punctuality-statistics/2025/

## What I did

1. Loaded the CSV files with pandas and combined them into one table.
2. Cleaned the data: removed [number] duplicate rows, dropped [number] rows with missing delay values, and converted the date column to a proper date type.
3. Defined "delayed" as a flight more than 15 minutes late.
4. Grouped the data by month and by airport size, and calculated the share of delayed flights in each group.
5. Plotted the results as a bar chart.

## Findings

- The highest share of delays was in July at 37.2%. The lowest was in March at 16.2%.
- [One thing that surprised you, with a number.]

![Delay share by month](charts/delay_by_month.png)

## Limitations

- The data shows when delays happened, not why. I did not have weather or air traffic data.
- [Any data you excluded, and how that could change the result.]
- This covers one year, so I can't say whether the pattern repeats.

## How to run it

1. Install the libraries: `pip install pandas matplotlib seaborn jupyter`
2. Download the data from the link above into the `data/` folder.
3. Open `analysis.ipynb` and choose Run All.

## Next steps

- Add [weather data] and test whether it explains the winter peak.
- Compare [two airlines] directly.

## Tools

Python, pandas, matplotlib, seaborn, Jupyter
