import pandas as pd
import plotly.express as px


# How has the incidence of assault offenses across Seattle changed over time
# from 2008 to present?
def plot_assault_offenses_over_time(data: pd.DataFrame) -> None:
    data = data[['Offense Start DateTime', 'Offense Parent Group']].dropna()
    data['Offense Start DateTime'] = pd.to_datetime(
        data['Offense Start DateTime'])
    data['Year'] = data['Offense Start DateTime'].dt.year.astype(int)
    data = (
        data.groupby('Year')['Offense Parent Group'].count()
        .reset_index(name="Count")
    )
    fig = px.line(data, x='Year', y='Count',
                  title='Assault Offenses in Seattle Over Time')
    fig.write_image('./results/assault_offenses_over_time.jpg')
