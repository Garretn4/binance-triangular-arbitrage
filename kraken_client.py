import requests

KRAKEN_API_URL = "https://api.kraken.com/0/public"

def get_product_price(pair):
    # Convert Coinbase-style pairs like BTC-USD to Kraken's format: XBTUSD
    kraken_pair = pair.replace("-", "").replace("BTC", "XBT").upper()

    try:
        response = requests.get(f"{KRAKEN_API_URL}/Ticker?pair={kraken_pair}")
        data = response.json()

        if "error" in data and data["error"]:
            raise Exception(data["error"])

        result = list(data["result"].values())[0]
        ask = float(result["a"][0])
        bid = float(result["b"][0])
        return ask, bid
    except Exception as e:
        print(f"Error fetching {pair} from Kraken: {e}")
        return None, None
