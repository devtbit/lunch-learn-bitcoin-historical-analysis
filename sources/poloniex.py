import pandas as pd
import requests
# sys.path hack, avoid in prod, build proper py package!!
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from utils import fetch_with_cache

base_url = 'https://poloniex.com/public'

def fetch_data(currency_pair, start, end, period, command='returnChartData', with_cache=True):
    url = '{}?command={}&currencyPair={}&start={}&end={}&period={}'.format(base_url, command, currency_pair, start, end, period)
    if with_cache:
        df = fetch_with_cache(currency_pair, json_url=url)
    else:
        df = fetch_method()
    return df
