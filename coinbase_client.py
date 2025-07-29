import requests

API_URL = "https://api.exchange.coinbase.com"

def get_product_price(pair):
    try:
        response = requests.get(f"{API_URL}/products/{pair}/ticker", timeout=2)
        if response.status_code != 200:
            return None, None
        data = response.json()
        if "ask" not in data or "bid" not in data:
            return None, None
        ask = float(data["ask"])
        bid = float(data["bid"])
        return ask, bid
    except Exception as e:
        print(f"⚠️ Coinbase error for {pair}: {e}")
        return None, None
