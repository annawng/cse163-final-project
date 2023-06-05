"""
Joey Kang, Eric Kim, and Anna Wang
CSE 163
Analyzes and plots Seattle Police Department crime data to determine what
factors resulted in the greatest number of assault offenses in Seattle in 2022.
"""
import pandas as pd
import plotly.express as px


def plot_assaults_by_time_2022(data: pd.DataFrame) -> None:
    """
    Creates a bar chart of the assault offenses committed during each hour
    during the day in 2022, using `data`, the SPD crime dataset.
    """
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

    fig.write_image('./results/assaults_by_time_2022.jpg')


def plot_assaults_by_location_2022(data: pd.DataFrame) -> None:
    """
    Creates a bar chart of the assault offenses committed in each MCPP in 2022,
    using `data`, the SPD crime dataset. MCPP stands for Micro-Community
    Policing Plans and essentially refers to neighborhoods in Seattle.
    """
    data = data[['Offense Parent Group', 'MCPP']].dropna()
    data = data[data['Offense Parent Group'] == "ASSAULT OFFENSES"]
    data = (
        data.groupby('MCPP')['MCPP'].count()
        .reset_index(name="Count")
    )
    data = data.sort_values('Count', ascending=False)
    fig = px.bar(data, x='MCPP', y='Count',
                 title='Number of Assault Offenses Per MCPP')
    fig.write_image('./results/assaults_by_location_2022.jpg')
