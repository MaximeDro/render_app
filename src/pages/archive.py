import dash
from dash import html
# WEBSCRAPPING MODULE
from bs4 import BeautifulSoup
import requests
import pandas as pd
import module_compl as mc

# print(module_compl.test_funct('salut'))

dash.register_page(__name__)

############################## A METTRE DANS LE MODULE 

############### FONCTION QUI GENERE UN TABLEAU
def generate_table(dataframe, max_rows=20):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

layout = html.Div([
    html.H1('Here is meteo prevision'),
    generate_table(mc.df_meteo),
    html.Div('This is our Archive page content.'),
    html.H1("Bonjour je m'appelle Dalida "),
    html.Br(),
    html.H1('Dalida SH'),
])

