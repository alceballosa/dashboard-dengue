import dash_bootstrap_components as dbc
from dash import html

# from utils.constants import home_page_location, gdp_page_location, iris_page_location


# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(
            [
                html.Img(
                    src=("./assets/img/onehealth.png"),
                    alt="One Health logo",
                    style={
                        "width": 100,
                        "height": "auto",
                        "margin-left": "auto",
                        "margin-right": "auto",
                    },
                ),
                html.H2("Dengue en ciudades colombianas"),
            ],
            className="text-center",
        ),
        html.Br(),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "borderColor": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "borderColor": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "Una herramienta para visualizar los resultados del estudio retrospectivo de la relación entre el Dengue y el clima en ciudades colombianas.",
                    className="lead",
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Inicio", href="/", active="exact"),
                    # dbc.NavLink("Home", href=home_page_location, active="exact"),
                    # dbc.NavLink("GDP", href=gdp_page_location, active="exact"),
                    # dbc.NavLink("Iris", href=iris_page_location, active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)
