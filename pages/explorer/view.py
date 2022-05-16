import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
from app import app
from dash import dcc
from dash import html
from dash.dependencies import Input
from dash.dependencies import Output

from . import data

params = {
    "x_space_between_nodes": 200,
    "y_space_between_nodes": 20,
    "x_first_node": 50,
    "current_top_node_word": 0,
    "current_top_node_attention": 0,
    "y_first_node": 9,
    "max_nodes_to_visualize": 9,
    "current_sample": 0,
    "n_weights_ff": 128,
    "y_first_node_ff": 5,
    "x_space_between_nodes_ff": 10,
    "y_space_between_nodes_ff": 9,
}


dfs = data.get_city_dfs()

figures_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="figure_dengue", figure=data.get_fig_dengue(dfs)),
                    width=6,
                ),
                dbc.Col(
                    dcc.Graph(id="figure_temp", figure=data.get_fig_temp(dfs)), width=6
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="figure_hum", figure=data.get_fig_humidity(dfs)),
                    width=6,
                ),
                dbc.Col(
                    dcc.Graph(id="figure_prec", figure=data.get_fig_precipitation(dfs)),
                    width=6,
                ),
            ]
        ),
    ]
)


text_description = html.P(
    """
    A continuación dispone de varias secciones en las que puede visualizar las series
    de tiempo de Dengue y datos climáticos de cada variable de interés.

    Puede visualizar una única serie de tiempo haciendo doble clic sobre la leyenda a
    la derecha de cada visualización. También puede hacer zoom seleccionando un área
    de interés en la gráfica, o pasar el ratón por encima de cualquiera de las líneas
    para obtener los valores específicos que estas codifican.
    """
)


layout = html.Div(
    [
        dcc.Store(id="explorer-view-store", data=params),
        html.H1("Visualización de series de tiempo"),
        text_description,
        figures_layout,
    ]
)
