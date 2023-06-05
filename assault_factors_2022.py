import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px


# What factors resulted in the greatest amount of assault offenses in
# Seattle in 2022?
def plot_assault_factors_2022(data: pd.DataFrame) -> None:
    data = data[['Offense Start DateTime',
                 'Offense Parent Group']].dropna()
    data['Offense Start DateTime'] = \
        pd.to_datetime(data['Offense Start DateTime'])
    data['Hour'] = data['Offense Start DateTime'].dt.hour
    data = data[data['Offense Parent Group'] == "ASSAULT OFFENSES"]
    data = (
        data.groupby('Hour')['Hour'].count()
        .reset_index(name="Count")
    )
    fig = px.bar(data, x='Hour', y='Count',
                 title='Number of Assault Offenses Per Hour',
                 labels={
                    'Hour': 'Time',
                 })
    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(25)),
            ticktext=[f'{12 if i == 0 else i}am'
                      if i < 12
                      else f'{12 if i == 12 else i % 12}pm' for i in range(25)]
        )
    )

    fig.write_image('./results/assault_factors_2022.jpg')


def merge_data(shp_file: str, csv_file: str) -> gpd.GeoDataFrame:
    geospatial_data = gpd.read_file(shp_file)
    spd_data = pd.read_csv(csv_file)

    # if doesnt work try how=inner or on
    merged_gdf = geospatial_data.merge(spd_data, left_on='sector',
                                       right_on='Sector', how='outer')
    return merged_gdf


def plot_geo_data(data: gpd.GeoDataFrame) -> None:
    data.plot()
    fig, ax = plt.subplots(1)
    # data = data[['sector', 'geometry', 'Offense Parent Group']]
    # data = data[data['Offense Parent Group'] == "ASSAULT OFFENSES"]
    # data = data.dissolve(by='sector', aggfunc='count')
    # print(data.head(10))
    # data.plot(ax=ax, column='Count', legend=True)
    # plt.title("Assault Offenses by Sector")
    plt.savefig('./results/assault_offense_map.png')
