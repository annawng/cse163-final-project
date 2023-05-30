import pandas as pd
# import other classes here

DATASET = './data/SPD_Crime_Data__2008-Present.csv'


def main():
    data = pd.read_csv(DATASET)
    print(data.head(10))


if __name__ == '__main__':
    main()
