import yfinance as yf
import pandas as pd

# Define tickers (NVIDIA, AMD, Intel, S&P 500)
tickers = ["NVDA", "AMD", "INTC", "^GSPC"]

# Download 10 years of historical stock data
data = yf.download(tickers, start="2015-01-01", end="2025-01-01")["Adj Close"]


# Save to CSV for later analysis
data.to_csv("stock_data.csv")
print("✅ Stock data saved to stock_data.csv")

pandas
numpy
matplotlib
seaborn
yfinance
scipy
