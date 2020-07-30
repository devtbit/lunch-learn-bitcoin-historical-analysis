import ccxt
import pandas as pd

def fetch_trades(exchange, market='BTC/USD'):
    if not exchange.markets:
        exchange.load_markets()
    if market not in exchange.markets.keys():
        print('Error: market not found')
        return None
    trades = exchange.fetch_trades(market)
    return pd.DataFrame(trades)

def fetch_trades_from(exchange_name, market='BTC/USD'):
    try:
        exchange = getattr(ccxt, exchange_name)()
        _ = getattr(exchange, 'fetch_trades')
    except:
        print('Error: exchange not supported')
        return None
    trades = fetch_trades(exchange, market=market)
    return trades

