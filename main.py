import pandas as pd

from correct_data import correct_data
from transform_data import transform_data
from structurize_data import structurize_data
from enrich_data import enrich_data

import re

if __name__ == '__main__':
    df = pd.read_csv('./data/915_corrupted_incidents.csv')
    pd.set_option("display.expand_frame_repr", False)

    # Установить отображение максимального количества строк и столбцов
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)

    # print(df)

    transform_data(df)
    structurize_data(df)
    correct_data(df)

    print(df['description'].head(50))