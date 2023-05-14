# Distrokid Export Visualizer

This repository contains a Python script for visualizing music distribution data exported from Distrokid. The script performs an in-depth analysis of the data and presents the results through interactive visualizations. The sales data is expected to be stored in a tab-separated values (TSV) file.

The Python script uses the pandas library to manipulate and analyze the data, chardet to correctly interpret the text encoding of the input file, and Plotly to create dynamic, interactive visualizations.

## Features

The script generates a series of bar plots, each of which provides insights into different aspects of the sales data:

1. Sales by Country of Sale: This plot displays the total quantity of sales for each country.
2. Earnings by Country of Sale: This plot shows the total earnings for each country in USD.
3. Sales by Artist and Title: This plot presents the total quantity of sales for each combination of artist and title.
4. Sales by Store: This plot illustrates the total quantity of sales for each store.
5. Earnings by Title: This plot reveals the total earnings for each title in USD.

Each plot is contained within a panel, and the panels are arranged in a grid for easy comparison. You can click on the bars within each plot to isolate them, and hover over the bars to see the exact values.

## Getting Your Export File from Distrokid

To generate the `export.tsv` file:

1. If you are not a Distrokid user, please join using this [referral link](https://distrokid.com/vip/seven/2858436) to upload unlimited songs per month to several streaming services.
2. Visit [Distrokid Bank Details](https://distrokid.com/bank/details/).
3. Filter data if required by Artist or Time.
4. Click the Export button.
5. Rename your exported file to `export.tsv`.

## Installation

Before running the script, you need to have Python 3.6 or above installed on your machine. You also need the pandas, chardet, and plotly libraries, which can be installed via pip:


## Usage

The script is contained in a file called `sales_analysis.py`. To run it, navigate to the directory containing the script and the `export.tsv` file, and type the following into your command line:

`python sales_analysis.py`

The script will read the `export.tsv` file, perform the analysis, and display the interactive plots in a new browser window.

## Support

For questions or personal support, please send an email to [dev@trapify.de](mailto:dev@trapify.de).

## Contributing

We welcome contributions to this project. Please feel free to submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License. Please see the LICENSE file for more details.

