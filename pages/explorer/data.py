from pathlib import Path

# import matplotlib.cm as cm
# import matplotlib.colors as mcolors
import pandas as pd
import plotly.express as px

city_codes_to_names = {
    54001: "Cúcuta",
    91001: "Leticia",
    76001: "Cali",
    5001: "Medellín",
}


def get_city_dfs():
    path_dfs = Path("./data/").glob("*.csv")
    dfs = []
    for path_df in path_dfs:
        df = pd.read_csv(path_df)
        city = df["COD_MUNICIPIO"][0]
        df["NOMBRE_MUNICIPIO"] = city_codes_to_names[city]
        dfs.append(df)
    dfs = pd.concat(dfs, axis=0)
    return dfs


def get_fig_dengue(dfs):
    fig = px.line(
        dfs,
        x="FECHA",
        y="DENGUE",
        color="NOMBRE_MUNICIPIO",
        labels={
            "FECHA": "Fecha",
            "DENGUE": "Casos de Dengue",
            "NOMBRE_MUNICIPIO": "Municipio",
        },
    )
    fig.update_layout(
        font_family="Lato",
        title={
            "text": "Casos de Dengue semanales por municipio",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
    )
    return fig


def get_fig_temp(dfs):
    fig = px.line(
        dfs,
        x="FECHA",
        y="TEMPERATURE_MEAN",
        color="NOMBRE_MUNICIPIO",
        labels={
            "FECHA": "Fecha",
            "TEMPERATURE_MEAN": "Temp. media (°C)",
            "NOMBRE_MUNICIPIO": "Municipio",
        },
    )
    fig.update_layout(
        font_family="Lato",
        title={
            "text": "Temperatura media semanal por municipio",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
    )
    return fig


def get_fig_humidity(dfs):
    fig = px.line(
        dfs,
        x="FECHA",
        y="REL_HUMIDITY_MEAN",
        color="NOMBRE_MUNICIPIO",
        labels={
            "FECHA": "Fecha",
            "REL_HUMIDITY_MEAN": "Humedad relativa media (%)",
            "NOMBRE_MUNICIPIO": "Municipio",
        },
    )
    fig.update_layout(
        font_family="Lato",
        title={
            "text": "Humedad relativa media semanal por municipio",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
    )
    return fig


def get_fig_precipitation(dfs):
    fig = px.line(
        dfs,
        x="FECHA",
        y="PRECIPITATION",
        color="NOMBRE_MUNICIPIO",
        labels={
            "FECHA": "Fecha",
            "PRECIPITATION": "Precipitación (mm)",
            "NOMBRE_MUNICIPIO": "Municipio",
        },
    )
    fig.update_layout(
        font_family="Lato",
        title={
            "text": "Precipitación acumulada semanal por municipio",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
    )
    return fig
