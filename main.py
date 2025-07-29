import os
from dotenv import load_dotenv
from binance.client import Client
from triangle_finder import find_triangles


load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")
BASE_CURRENCY = os.getenv("BASE_CURRENCY", "USDT")
MIN_PROFIT_PERCENT = float(os.getenv("MIN_PROFIT_PERCENT", 0.3))

client = Client(API_KEY, SECRET_KEY)

def get_symbols():
    info = client.get_exchange_info()
    symbols = [s["symbol"] for s in info["symbols"] if s["status"] == "TRADING"]
    return symbols

def find_triangles(symbols):
    # Placeholder triangle simulation
    print("Scanning for triangle opportunities...")
    print(f"Simulated Triangle: {BASE_CURRENCY} → BTC → ETH → {BASE_CURRENCY}")
    print(f"Estimated profit: {MIN_PROFIT_PERCENT + 0.1}%\n")

if __name__ == "__main__":
    symbols = get_symbols()
    find_triangles(symbols)
