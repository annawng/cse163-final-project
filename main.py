import pandas as pd

from assault_offenses_over_time import plot_assault_offenses_over_time
# from assault_factors_2022 import plot_assault_factors_2022

DATASET = './data/SPD_Crime_Data__2008-Present.csv'


def main():
    data = pd.read_csv(DATASET)
    plot_assault_offenses_over_time(data)


if __name__ == '__main__':
    main()
