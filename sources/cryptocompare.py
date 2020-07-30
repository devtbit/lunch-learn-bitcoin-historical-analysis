import pandas as pd
import requests

base_url = 'https://min-api.cryptocompare.com/data/histo'
supported_intervals = {'minute', 'hour', 'day'}
default_limit = 2000

def fetch_data(from_sym, to_sym, exchange, datetime_interval, limit=default_limit):
    assert datetime_interval in supported_intervals, \
        '[!] datetime_interval should be one of %s' % supported_intervals
    url = '%s%s' % (base_url, datetime_interval)
    params = {
            'fsym': from_sym,
            'tsym': to_sym,
            'limit': limit,
            'aggregate': 1,
            'e': exchange
    }
    req = requests.get(url, params=params)
    data = req.json()
    return pd.json_normalize(data, ['Data'])
