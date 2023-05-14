# Distrokid Export Visualizer

This project performs an analysis of "sales" data stored in a TSV(csv) file. It generates interactive visualizations using Python, pandas, chardet, and Plotly.

## Prerequisites

### Script
Before running the script, you need to have the following installed:

1. Python 3.6 or above
2. pandas
3. chardet
4. plotly

You can install the Python libraries using pip: `pip install -r requirements.txt`

## Running the Script

The script is contained in a file called `main.py`. You can run it from the command line like so:



The script reads a file named `export.tsv` from the same directory. The TSV file is expected to contain sales data with the following columns:

1. Country of Sale
2. Quantity
3. Earnings (USD)
4. Artist
5. Title
6. Store

## Results

The script will display interactive plots in a web-based environment, showing:

1. Sales by Country of Sale
2. Earnings by Country of Sale
3. Sales by Artist and Title
4. Sales by Store
5. Earnings by Title

Each plot is contained within a panel. You can click on the bars in each plot to isolate them, and hover over the bars to see the exact values.

