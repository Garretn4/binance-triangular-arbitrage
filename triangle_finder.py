from binance.client import Client
from collections import defaultdict

def build_market_map(symbols):
    """Builds a mapping of base and quote pairs."""
    market_map = defaultdict(list)
    for s in symbols:
        base = s['baseAsset']
        quote = s['quoteAsset']
        market_map[base].append(quote)
    return market_map

def find_triangles(symbols, base_currency='USDT'):
    """Returns a list of triangular arbitrage paths starting and ending with base_currency."""
    market_map = build_market_map(symbols)
    triangles = []

    for base1 in market_map[base_currency]:
        if base1 not in market_map:
            continue
        for base2 in market_map[base1]:
            if base2 == base_currency:
                continue
            if base_currency in market_map[base2]:
                triangle = [base_currency, base1, base2, base_currency]
                triangles.append(triangle)

    return triangles
