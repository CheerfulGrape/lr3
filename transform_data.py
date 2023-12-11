import pandas as pd
from pandas import DataFrame


def transform_data(df: DataFrame):
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    # print(df)
