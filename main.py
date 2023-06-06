"""
Joey Kang, Eric Kim, and Anna Wang
CSE 163
Analyzes and plots Seattle Police Department crime data to reveal insights
about assault offenses in the Seattle area. The dataset covers crimes from
2008 to present and contains columns for various information relating to the
crimes including the date and time of the offense, type of offense, and where
it was committed (precinct, sector, beat, MCPP/neighborhood, address,
longitude, and latitude).
"""
import pandas as pd

from assault_offenses_over_time import plot_assault_offenses_over_time
from assault_factors_2022 import plot_assaults_by_time_2022
from assault_factors_2022 import plot_assaults_by_location_2022
from predicting_offenses import predict_offense_type
from predicting_offenses import test_filtering


DATASET = './data/SPD_Crime_Data__2008-Present.csv'
TESTDATA = './data/SPD_Test_Data.csv'


def main():
    data = pd.read_csv(DATASET)
    plot_assault_offenses_over_time(data, 'assault_offenses_over_time.jpg')
    plot_assaults_by_time_2022(data, 'assaults_by_time_2022.jpg')
    plot_assaults_by_location_2022(data, 'assaults_by_location_2022.jpg')
    predict_offense_type(data)

    test_data = pd.read_csv(TESTDATA)
    plot_assault_offenses_over_time(test_data,
                                    'test_assault_offenses_over_time.jpg')
    plot_assaults_by_time_2022(test_data, 'test_assaults_by_time_2022.jpg')
    plot_assaults_by_location_2022(test_data,
                                   'test_assaults_by_location_2022.jpg')
    test_filtering(test_data)


if __name__ == '__main__':
    main()
