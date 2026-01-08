import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import folium
    import marimo as mo
    import pandas as pd
    import geopandas as gpd

    from shapely import wkb
    from shapely.geometry import Point

    return Point, folium, gpd, mo, pd, wkb