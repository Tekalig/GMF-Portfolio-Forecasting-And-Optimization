import pandas as pd

def load_data(filename):
    return pd.read_csv(filename, parse_dates=['Date'])

def preprocess_data(df):
    df.dropna(inplace=True)
    df.set_index('Date', inplace=True)
    return df

def save_preprocessed_data(df, filename):
    df.to_csv(filename)
