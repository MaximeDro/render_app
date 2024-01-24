import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H1('This is our Archive page'),
    html.Div('This is our Archive page content.'),
    html.H1("Bonjour je m'appelle Dalida "),
    html.Br(),
    html.H1('Dalida SH'),
])