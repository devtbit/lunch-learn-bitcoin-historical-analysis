import pandas as pd
import pickle

def to_datetime(df, timecol='datetime', set_index=True, datetimecol='Datetime', to_unit=None, dateformat=None):
    df[datetimecol] = pd.to_datetime(df[timecol], unit=to_unit, format=dateformat)
    if set_index:
        df = df.set_index(datetimecol)
    return df

def map_ohlc(trades, timesep='30S', sample='price'):
    trades = to_datetime(trades)
    return trades.resample(timesep).agg({sample:'ohlc'})

def drop_empty_datapoints(df, axis=1, debug=False):
    indices = df[df.sum(axis=axis) == 0].index
    if debug:
        print('[+] Filtering %d empty datapoints' % indices.shape[0])
    return df.drop(indices)

def read_csv_dataset(filename, to_datetime=True):
    df = pd.read_csv(filename)
    if to_datetime: df = to_datetime(df)
    return df.sort_index();

def merge_dfs_column(dfs_dict, col):
    series = {}
    dfs = list(dfs_dict.values())
    labels = list(dfs_dict.keys())
    for i in range(len(dfs)):
        series[labels[i]] = dfs[i][col]
    return pd.DataFrame(series)

def fetch_with_cache(cache_path, fetch_method=None, json_url=None, csv=False, to_datetime=True):
    try:
        f = open(cache_path, 'rb')
        df = pickle.load(f)
    except (OSError, IOError) as e:
        if fetch_method and not json_url:
            df = fetch_method()
        elif json_url:
            df = pd.read_json(json_url)
        df.to_pickle(cache_path)
    return df
