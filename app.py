# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/compiled_daily_sales_data.csv')

fig = px.line(df, x="date", y="sales", title="Daily Sales Data from Jan 2018 to present")

app.layout = html.Div(children=[
    dcc.Graph(
        id='pink-sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)