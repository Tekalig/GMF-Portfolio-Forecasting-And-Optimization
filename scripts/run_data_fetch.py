from src.data_fetch import fetch_stock_data, save_data

assets = {'TSLA': 'data/tsla.csv', 'BND': 'data/bnd.csv', 'SPY': 'data/spy.csv'}

for ticker, filepath in assets.items():
    df = fetch_stock_data(ticker)
    save_data(df, filepath)
