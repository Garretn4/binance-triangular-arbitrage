# binance-triangular-arbitrage
# Binance Triangular Arbitrage Bot

A Python-based bot that scans for and optionally executes profitable triangular arbitrage opportunities on Binance. Built for learning, testing, and scaling into real-world usage with safe rollout stages.

---

## 🚀 Features

- Detects real-time triangular arbitrage loops (e.g., USDT → BTC → ETH → USDT)
- Configurable profit thresholds and fees
- Logging system for monitoring trades
- Works via Binance API (API key required)
- Built for gradual scaling — from simulation to live trading

---

## 📦 Project Structure

binance-triangular-arbitrage-bot/
├── main.py # Entry point to run the bot
├── triangle_finder.py # Detects arbitrage paths
├── trade_executor.py # Executes trades (optional)
├── config.py # Settings and constants
├── binance_client.py # Binance API logic
├── utils.py # Logging helpers, fee calculators
├── logs/
│ └── trades.log # Logged results
├── .env # Your API keys (not tracked by Git)
├── .env.example # Template for environment config
├── .gitignore # Files/folders ignored by Git
└── README.md # This file

---

## 🧪 Staged Development Plan

### ✅ Stage 1: Simulation Mode (No Real Trading)
- [x] Use **test API keys** or limit permissions to read-only
- [x] Simulate triangle detection logic
- [x] Log profitable paths to console and `logs/trades.log`
- [ ] Confirm real spreads vs fees before trading

### ✅ Stage 2: Dry-Run Execution Mode
- [ ] Connect live Binance account (no funds or trading permission yet)
- [ ] Log intended trade execution paths without placing orders
- [ ] Validate trade sequence & balance requirements

### ⚠️ Stage 3: Real Trading Mode (Live Funds)
- [ ] Add trade execution via `trade_executor.py`
- [ ] Start with **low trade amounts** (e.g., $10)
- [ ] Monitor logs and exchange for actual fills and slippage
- [ ] Auto-adjust thresholds for spread vs. fee profit

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
