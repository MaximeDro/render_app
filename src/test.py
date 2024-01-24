# import dash
# from dash import html, dash_table
# import dash_bootstrap_components as dbc
# import pandas as pd


# dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR, dbc_css])

# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

# table = html.Div(
#     dash_table.DataTable(
#         columns=[{"name": i, "id": i} for i in df.columns],
#         data=df.to_dict("records"),
#         # row_selectable="single",
#         # row_deletable=True,
#         # editable=True,
#         # filter_action="native",
#         # sort_action="native",
#         # style_table={"overflowX": "auto"},
#     ),
# )
# ############### FONCTION QUI GENERE UN TABLEAU A MOI !!!
# def generate_table(dataframe, max_rows=10):
#     return html.Div([
#             html.H5("DataTable with Bootstrap theme"),
#             html.Div(
#                 dash_table.DataTable(
#                     columns=[{"name": i, "id": i} for i in df.columns],
#                     data=df.iloc[:max_rows,:].to_dict("records"),
#                     # row_selectable="single",
#                     # row_deletable=True,
#                     # editable=True,
#                     # filter_action="native",
#                     sort_action="native",
#                     # style_table={"overflowX": "auto"},
#                 ),
#             ),
#         ],
#         className="dbc dbc-row-selectable",
#     )


# with_theme = html.Div([
#         html.H5("DataTable with Bootstrap theme"),
#         table,
#     ],
#     className="dbc dbc-row-selectable",
# )


# without_theme = html.Div([
#         html.H5("No theme", className="mt-4"), 
#         table
#     ],
# )

# app.layout = html.Div([dbc.Container([with_theme, without_theme]),
#     generate_table(df)])


# if __name__ == "__main__":
#     app.run_server(debug=True)


import module_compl 

print(module_compl.test_funct('salut'))
