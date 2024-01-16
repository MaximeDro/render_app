from dash import Dash, html, dcc

app = Dash(__name__)
server = app.server

# Layout de base
app.layout = html.Div([
############## Titres et textes :
    html.H1("Titre Principal updated"),
    html.P("Ceci est un paragraphe décrivant le contenu de la page."),
    html.A("Lien vers la Wild Code School", href="https://www.wildcodeschool.com/"),
############## Listes et images :
    html.Ul([
        html.Li("Premier élément"),
        html.Li("Deuxième élément"),
        html.Li("Troisième élément")
    ]),
    html.Img(src="https://www.wildcodeschool.com/hs-fs/hubfs/booster-carriere.png?width=575&height=620&name=booster-carriere.png"),
############# Graphique interactif avec liste de choix :
    dcc.Dropdown(
        id='dropdown-exemple',
        options=[{'label': i, 'value': i} for i in ['Option 1', 'Option 2']],
        value='Option 1'
    ),
    dcc.Graph(id='graph-exemple'),
############# Contrôles d'entrée, slider et choix :
    dcc.Input(id='input-exemple', type='text', value='Texte initial'),
    dcc.Slider(min=0, max=10, step=0.5, value=5),
    dcc.RadioItems(options=[{'label': i, 'value': i} for i in ['Option A', 'Option B']], value='Option A'),
############# Lier un Fichier CSS à Dash
    html.H1("Titre avec Style", className='header-title'),
    dcc.Graph(id='graph1', className='graph-style'),
############# intégration de CSS directement dans le code python
    html.H1(
        "Titre Principal",
        style={'textAlign': 'center', 'color': 'blue'}
    ),
    html.Div(
        "Ce texte est dans un Div.",
        style={'border': '2px solid black', 'padding': '10px'}
    ),
    html.Button(
        "Cliquez-moi",
        style={'backgroundColor': 'green', 'color': 'white', 'fontSize': 20}
    )

    
])

if __name__ == '__main__':
    app.run_server(debug=True) # , port = 8071 # pour ne pas être sur dashtools gui si déjà executé