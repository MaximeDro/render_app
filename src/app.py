import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.DARKLY] #voir avec le themes pour le cadrage des colonnesCERULEAN
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets) 
server = app.server
# app = Dash(__name__, use_pages=True)

app.layout = dbc.Container([
    dbc.Row([
        html.H1('Tableau de bord interactif',style={'textAlign': 'center'}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
    ]),
    dbc.Row([
        dbc.Col([
            html.H2('Menu',style={}),   
            html.Div([
            html.Div(
                dcc.Link(f"{page['name']}", href=page["relative_path"])
            ) for page in dash.page_registry.values()
        ]),
        ], width = 1 ),  
        dbc.Col([
            dash.page_container
        ], width=10),
    ])
], fluid=True)
if __name__ == '__main__':
    app.run(debug=True)






    