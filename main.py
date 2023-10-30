import pandas as pd

from correct_data import correct_data
from transform_data import transform_data
from structurize_data import structurize_data
from enrich_data import enrich_data


df = pd.read_csv('./data/915_corrupted_incidents.csv')
pd.set_option("display.expand_frame_repr", False)

correct_data(df)
transform_data(df)
structurize_data(df)
enrich_data(df)

print(df)
