"""
Joey Kang, Eric Kim, and Anna Wang
CSE 163
Analyzes and plots Seattle Police Department crime data to determine how the
incidence of assault offenses across Seattle has changed over time from 2008 to
2022. We decided to filter down to these years because the datasheet says that
the data is from 2008 to present, but the data from 2023 is incomplete because
it is the current year.
"""
import pandas as pd
import plotly.express as px


def plot_assault_offenses_over_time(data: pd.DataFrame) -> None:
    """
    Creates a line chart of the assault offenses committed over time from 2008
    to 2022, using `data`, the SPD crime dataset.
    """
    data = data[['Offense Start DateTime', 'Offense Parent Group']].dropna()
    data['Offense Start DateTime'] = pd.to_datetime(
        data['Offense Start DateTime'])
    data['Year'] = data['Offense Start DateTime'].dt.year.astype(int)
    data = data[(data['Year'] >= 2008) & (data['Year'] <= 2022)]
    data = (
        data.groupby('Year')['Offense Parent Group'].count()
        .reset_index(name="Count")
    )
    fig = px.line(data, x='Year', y='Count',
                  title='Assault Offenses in Seattle Over Time (2008-2022)')
    fig.write_image('./results/assault_offenses_over_time.jpg')
