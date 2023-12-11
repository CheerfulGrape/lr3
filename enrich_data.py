import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import requests
from pandas import DataFrame


def enrich_data(df: DataFrame):
    def categorize_ip(ip):
        octets = ip.split('.')
        last_octet = int(octets[-1])
        if 10 <= last_octet < 100:
            return 'User'
        if 100 <= last_octet < 220:
            return 'Service'
        if 220 <= last_octet:
            return 'System'

    df['IP'] = df['IP'].apply(categorize_ip)


