from dash import Dash, html, dcc, callback, Output, Input, ctx
import plotly.express as px
import pandas as pd
import requests

from opentelemetry import trace

tracer = trace.get_tracer('dash')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
@tracer.start_as_current_span("update-graph.callback")
def update_graph(value):
    with tracer.start_as_current_span("update-graph") as span: 
        span.set_attribute("dash.context", ctx.triggered_id or "none")   
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        response.raise_for_status()
        dff = df[df.country==value]
        return px.line(dff, x='year', y='pop')



