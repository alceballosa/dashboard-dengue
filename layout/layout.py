from dash import dcc
from dash import html

from .sidebar.view import sidebar

content = html.Div(id="page-content")
layout = html.Div([dcc.Location(id="url"), sidebar, content])
