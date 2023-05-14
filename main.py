import pandas as pd
import chardet
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Detect the file encoding
rawdata = open('export.tsv', 'rb').read()
result = chardet.detect(rawdata)
encoding = result['encoding']

# Read the tsv file into a pandas dataframe with the detected encoding
df = pd.read_csv('export.tsv', sep='\t', encoding=encoding)

# Define a function to generate a bar plot from a groupby object
def make_plot(df, x, y, title):
    return go.Bar(x=df[x], y=df[y], name=title)

# Create the groupby objects
sales_country = df.groupby('Country of Sale')['Quantity'].sum().sort_values(ascending=False).reset_index()
earnings_country = df.groupby('Country of Sale')['Earnings (USD)'].sum().sort_values(ascending=False).reset_index()
sales_artist_title = df.groupby(['Artist', 'Title'])['Quantity'].sum().sort_values(ascending=False).reset_index()
sales_store = df.groupby('Store')['Quantity'].sum().sort_values(ascending=False).reset_index()
earnings_title = df.groupby('Title')['Earnings (USD)'].sum().sort_values(ascending=False).reset_index()

# Create the subplots
fig = make_subplots(rows=3, cols=2, subplot_titles=('Sales by Country', 'Earnings by Country', 'Sales by Artist and Title', 'Sales by Store', 'Earnings by Title'))

# Add the plots
fig.add_trace(make_plot(sales_country, 'Country of Sale', 'Quantity', 'Sales by Country'), row=1, col=1)
fig.add_trace(make_plot(earnings_country, 'Country of Sale', 'Earnings (USD)', 'Earnings by Country'), row=1, col=2)
fig.add_trace(make_plot(sales_artist_title, 'Artist', 'Quantity', 'Sales by Artist and Title'), row=2, col=1)
fig.add_trace(make_plot(sales_store, 'Store', 'Quantity', 'Sales by Store'), row=2, col=2)
fig.add_trace(make_plot(earnings_title, 'Title', 'Earnings (USD)', 'Earnings by Title'), row=3, col=1)

# Update layout
fig.update_layout(height=1200, width=1200, title_text="Sales Data Analysis", showlegend=False)
fig.show()
