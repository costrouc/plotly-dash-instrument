from dash import Dash, html, dcc, callback, Output, Input, ctx
import plotly.express as px
import pandas as pd
import requests

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

RequestsInstrumentor().instrument()


RESOURCE = Resource.create({SERVICE_NAME: "dash-otlp"})
trace_provider = TracerProvider(resource=RESOURCE)
trace.set_tracer_provider(trace_provider)

# environment variable configuration
# https://opentelemetry-python.readthedocs.io/en/latest/exporter/otlp/otlp.html
span_processor = BatchSpanProcessor(OTLPSpanExporter())
trace_provider.add_span_processor(span_processor)


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



