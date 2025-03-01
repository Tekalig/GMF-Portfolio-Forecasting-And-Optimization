import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_prices(df, title):
    plt.figure(figsize=(10,5))
    plt.plot(df['Close'], label='Close Price')
    plt.title(title)
    plt.legend()
    plt.show()

def calculate_returns(df):
    df['Daily Return'] = df['Close'].pct_change()
    return df
