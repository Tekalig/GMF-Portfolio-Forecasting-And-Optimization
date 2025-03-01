from src.exploratory_analysis import plot_stock_prices, calculate_returns
from src.data_preprocessing import load_data

assets = ['data/preprocessed_tsla.csv', 'data/preprocessed_bnd.csv', 'data/preprocessed_spy.csv']

dataframes = {asset: load_data(asset) for asset in assets}

for asset, df in dataframes.items():
    plot_stock_prices(df, f'Stock Prices for {asset}')
    df = calculate_returns(df)
