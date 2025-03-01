import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date='2015-01-01', end_date='2025-01-31'):
    stock = yf.download(ticker, start=start_date, end=end_date)
    stock.reset_index(inplace=True)
    return stock

def save_data(df, filename):
    df.to_csv(filename, index=False)
