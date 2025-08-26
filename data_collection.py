import yfinance as yf
import pandas as pd

# Define tickers (NVIDIA, AMD, Intel, S&P 500)
tickers = ["NVDA", "AMD", "INTC", "^GSPC"]

# Download 10 years of historical stock data
data = yf.download(tickers, start="2015-01-01", end="2025-01-01")["Adj Close"]

print("📥 Downloading stock data...")
data = yf.download(tickers, start="2015-01-01", end="2025-01-01")["Adj Close"]

# Save to CSV
data.to_csv("stock_data.csv")
print("✅ Data saved to stock_data.csv")
