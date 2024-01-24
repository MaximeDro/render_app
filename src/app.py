import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

# app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages',style = 'center'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)