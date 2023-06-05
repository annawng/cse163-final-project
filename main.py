import pandas as pd

from assault_offenses_over_time import plot_assault_offenses_over_time
from assault_factors_2022 import plot_assault_factors_2022
from assault_factors_2022 import merge_data
from assault_factors_2022 import plot_geo_data


DATASET = './data/SPD_Crime_Data__2008-Present.csv'
GEO_DATASET = './data/Seattle_Police_Beats_2018-Present.shp'


def main():
    # data = pd.read_csv(DATASET)
    # plot_assault_offenses_over_time(data)
    # plot_assault_factors_2022(data)
    geodata = merge_data(GEO_DATASET, DATASET)
    plot_geo_data(geodata)


if __name__ == '__main__':
    main()
