import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from datetime import datetime

# Load the CSV file and ensure the 'date' column is in datetime format
def load_data():
    df = pd.read_csv('formatted_sales_data.csv')  # Replace with your actual file path
    df['date'] = pd.to_datetime(df['date'])  # Convert 'date' column to datetime
    return df

# Initialize the Dash app
app = Dash(__name__)
df = load_data()

# App layout
app.layout = html.Div([
    html.H1("Sales Data Dashboard"),
    dcc.Dropdown(
        id='region-filter',
        options=[{'label': region, 'value': region} for region in df['region'].unique()],
        value=df['region'].unique()[0],
        clearable=False
    ),
    dcc.Graph(id='line-chart')
])

# Callback to update the chart
@app.callback(
    Output('line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_charts(selected_region):
    filtered_df = df[df['region'] == selected_region]

    # Use datetime object for the specific date
    specific_date = datetime(2021, 1, 15)

    # Create the line chart
    line_fig = px.line(filtered_df, x='date', y='sales', title=f"Sales in {selected_region}")

    # Add a vertical line for the specific date
    line_fig.add_vline(
        x=specific_date,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top left"
    )

    return line_fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
