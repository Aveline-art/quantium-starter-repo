# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)



'''
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
    '''