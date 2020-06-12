from dash import Dash
import dash_html_components as html


app = Dash(__name__)
app.layout = html.Div(
    "Hello World"
)


app.run_server(port=5000)
