import quandl
# sys.path hack, avoid in prod, build proper py package!!
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from utils import fetch_with_cache

# quandl.ApiConfig.api_key = "XXXXXXXXXXXXXXXXX"
quandl.ApiConfig.api_key = "PFgrzKFe_dX2aLk9PJuY"

def fetch_data(quandl_id):
    return quandl.get(quandl_id, returns="pandas")

def fetch_data_with_cache(quandl_id):
    cache_path = '{}.pkl'.format(quandl_id).replace('/', '-')
    def fetch_method():
        return fetch_data(quandl_id)
    return fetch_with_cache(cache_path, fetch_method)

def fetch_data_from_exchanges(exchanges, from_sym='BCHARTS', to_sym='USD', with_cache=True):
    exchanges_data = {}
    for e in exchanges:
        quandl_id = '{}/{}{}'.format(from_sym, e, to_sym)
        if with_cache:
            df = fetch_data_with_cache(quandl_id)
        else:
            df = fetch_data(quandl_id)
        exchanges_data[e] = df
    return exchanges_data
