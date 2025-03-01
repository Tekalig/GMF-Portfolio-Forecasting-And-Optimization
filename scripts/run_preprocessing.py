from src.data_preprocessing import load_data, preprocess_data, save_preprocessed_data

assets = {'TSLA': 'data/tsla.csv', 'BND': 'data/bnd.csv', 'SPY': 'data/spy.csv'}

for ticker, filepath in assets.items():
    df = load_data(filepath)
    df = preprocess_data(df)
    save_preprocessed_data(df, f'data/preprocessed_{ticker.lower()}.csv')
