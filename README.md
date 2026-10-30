# MC - SDIR | Streamlit Data App

## Purpose
An interactive Streamlit dashboard for exploring Biscayne Bay water-quality data.

## Dataset
`data/biscayneBay_waterquality.csv`: water-quality and survey measurements (temperature, salinity, pH, depth, and more).

## How to Run
```bash
pip install -r requirements.txt
streamlit run webapp.py
```

## How to Use
1. Pick a measurement from the dropdown.
2. View the Plotly line chart of that measurement over time.
3. Review the descriptive statistics and raw data below the chart.

## Features
- Dropdown to select a numeric parameter
- Plotly line chart with title, axis labels, and legend
- Descriptive statistics and raw data table
- Overview, Data Display, and Insights sections

## AGILE Process
- Planned a minimal app: one dataset, one widget, one chart
- Built in small iterations, starting with the data and chart
- Tested each change by running the app and cycling through the dropdown options
- Refined the layout and labels based on feedback
