import pandas as pd
import chardet
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def detect_encoding(file_path):
    """
    Detects the encoding of a file.
    
    Args:
        file_path (str): The path to the file.
    
    Returns:
        str: The detected encoding.
    """
    raw_data = open(file_path, 'rb').read()
    result = chardet.detect(raw_data)
    return result['encoding']


def read_tsv(file_path, encoding):
    """
    Reads a TSV file into a pandas dataframe with the specified encoding.
    
    Args:
        file_path (str): The path to the TSV file.
        encoding (str): The encoding of the file.
    
    Returns:
        pd.DataFrame: The dataframe containing the data from the TSV file.
    """
    return pd.read_csv(file_path, sep='\t', encoding=encoding)


def make_bar_plot(df, x, y, title):
    """
    Generates a bar plot from a groupby object.
    
    Args:
        df (pd.DataFrame): The dataframe containing the data.
        x (str): The column name to use as the x-axis.
        y (str): The column name to use as the y-axis.
        title (str): The title of the plot.
    
    Returns:
        go.Bar: The bar plot object.
    """
    return go.Bar(x=df[x], y=df[y], name=title)


# Detect the file encoding
file_path = 'export.tsv'
encoding = detect_encoding(file_path)

# Read the TSV file into a pandas dataframe with the detected encoding
df = read_tsv(file_path, encoding)

# Create the groupby objects
sales_country = df.groupby('Country of Sale')['Quantity'].sum().sort_values(ascending=False).reset_index()
earnings_country = df.groupby('Country of Sale')['Earnings (USD)'].sum().sort_values(ascending=False).reset_index()
sales_artist_title = df.groupby(['Artist', 'Title'])['Quantity'].sum().sort_values(ascending=False).reset_index()
sales_store = df.groupby('Store')['Quantity'].sum().sort_values(ascending=False).reset_index()
earnings_title = df.groupby('Title')['Earnings (USD)'].sum().sort_values(ascending=False).reset_index()

# Create the subplots
fig = make_subplots(rows=3, cols=2, subplot_titles=('Sales by Country', 'Earnings by Country',
                                                     'Sales by Artist and Title', 'Sales by Store',
                                                     'Earnings by Title'))

# Add the plots
fig.add_trace(make_bar_plot(sales_country, 'Country of Sale', 'Quantity', 'Sales by Country'), row=1, col=1)
fig.add_trace(make_bar_plot(earnings_country, 'Country of Sale', 'Earnings (USD)', 'Earnings by Country'), row=1, col=2)
fig.add_trace(make_bar_plot(sales_artist_title, 'Artist', 'Quantity', 'Sales by Artist and Title'), row=2, col=1)
fig.add_trace(make_bar_plot(sales_store, 'Store', 'Quantity', 'Sales by Store'), row=2, col=2)
fig.add_trace(make_bar_plot(earnings_title, 'Title', 'Earnings (USD)', 'Earnings by Title'), row=3, col=1)

# Update layout
fig.update_layout(height=1200, width=1200, title_text="Sales Data Analysis", showlegend=False)
fig.show()
