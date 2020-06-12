import datetime
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

app = Dash(__name__)
app.layout = html.Div(children=[
    html.Div(id="output"),
    dcc.Interval(id="interval", interval=1000),
])


@app.callback(Output("output", "children"), [Input("interval", "n_intervals")])
def interval(n_interval):
    time = datetime.datetime.now()
    return time.strftime("%d-%m-%Y %H:%M:%S")


app.run_server(port=5000)