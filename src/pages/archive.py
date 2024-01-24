import dash
from dash import html
# WEBSCRAPPING MODULE
from bs4 import BeautifulSoup
import requests
import pandas as pd
import module_compl as mc



dash.register_page(__name__)

# df = mc.df_meteo

layout = html.Div([
    html.H1('Here is meteo prevision'),
    mc.generate_table(df = mc.df_meteo, max_rows= 20),
    html.Div('This is our Archive page content.'),
    html.H1("Bonjour je m'appelle Dalida "),
    html.Br(),
    html.H1('Dalida SH'),
])

