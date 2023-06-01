import pandas as pd
import geopandas as gpd
# import numpy as np
import plotly.express as px


# What factors resulted in the greatest amount of assault offenses in Seattle in 2022?
# Time -> Pie Chart, MCPP -> Bar Chart, Sector -> GeoPandas
def plot_assault_factors_2022(data: pd.DataFrame) -> None:
    # Filter data by time of offense, only assault cases, and MCPP (area)
    data = data[['Offense Start DateTime', 'Offense Parent Group','MCPP']].dropna()
    data['Offense Start DateTime'] = pd.to_datetime(data['Offense Start DateTime'])
    # df['date_col'].dt.strftime('%H:%M') another possible way to filter time
    data['Time'] = data['Offense Start DateTime'].dt.time.astype(int)
    # data = data.groupby['Offense Parent Group']('MCPP')
    time_data = data.groupby['Time']('Hour').count()
    fig = px.pie(time_data, values='time_count', names='Hour', title='Number of Crimes for each Hour')
    fig.show()


def merge_data(shp_file: str, csv_file: str) -> gpd.DataFrame:
    geospatial_data = gpd.read_file(shp_file)
    spd_data = pd.read_csv(csv_file)

    # figure out how to merge
    merged_gdf = geospatial_data.merge(spd_data, left_on='sector', right_on='sector', how='left')

    return merged_gdf


def plot_geo_data(sector_data: gpd.DataFrame) -> None:
    fig, ax = plt.subplots(1)
    sector_filter =

