from coinbase_client import get_product_price as coinbase_price
from kraken_client import get_product_price as kraken_price

symbols = ["BTC-USD", "ETH-USD", "SOL-USD"]

print("🔁 Checking inter-exchange prices...\n")

for symbol in symbols:
    cb_ask, cb_bid = coinbase_price(symbol)
    kr_ask, kr_bid = kraken_price(symbol)

    if None in [cb_ask, cb_bid, kr_ask, kr_bid]:
        print(f"⚠️ Skipping {symbol} due to missing data.\n")
        continue

    print(f"🪙 {symbol}")
    print(f"  Coinbase Ask: {cb_ask:.2f} | Bid: {cb_bid:.2f}")
    print(f"  Kraken Ask:   {kr_ask:.2f} | Bid: {kr_bid:.2f}")

    if cb_bid > kr_ask:
        profit = cb_bid - kr_ask
        print(f"  ✅ Arbitrage: Buy on Kraken, sell on Coinbase → Profit: ${profit:.2f}\n")
    elif kr_bid > cb_ask:
        profit = kr_bid - cb_ask
        print(f"  ✅ Arbitrage: Buy on Coinbase, sell on Kraken → Profit: ${profit:.2f}\n")
    else:
        print("  ❌ No arbitrage opportunity.\n")
