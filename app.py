# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)

colors = {
    'background': '#111111',
    'line': '#FF1493'
}

df = pd.read_csv('data/compiled_daily_sales_data.csv')

fig = px.line(df, x="date", y="sales", title="Daily Sales Data of Pink Morsel from Jan 2018 to present")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Data', style={
        'flex': '0 1 100%',
    }),

    html.Div(children=[
        html.Div(children=[
            html.Div(children='Select a Region:'),
            dcc.RadioItems(['all', *df['region'].unique()], 'all', id='region-input', inline=True),
        ], style={
            'border': '1px solid',
            'padding': '16px',
            'width': 'max-content',
        })
    ], style={
        'flex': '0 1 100%',
    }),
    
    html.Div(children= [
        dcc.Graph(
            id='pink-sales-graph',
            figure=fig
        ),
    ], style={
        'flex': '0 1 100%',
    })

], style={
    'margin': '16px',
    'display': 'flex',
    'flexWrap': 'wrap',
})

@app.callback(
    Output('pink-sales-graph', component_property='figure'),
    Input('region-input', component_property='value')
)
def update_figure(region_value):
    if region_value == 'all':
        fig = px.line(df, x="date", y="sales", title="Daily Sales Data of Pink Morsel from Jan 2018 to present")
    else:
        dff = df[df.region == region_value]
        fig = px.line(dff, x="date", y="sales", title=f"Daily Sales Data of Pink Morsel from Jan 2018 to present ({region_value})")
    
    fig.update_traces(line_color=colors['line'])

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)