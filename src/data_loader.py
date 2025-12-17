import pandas as pd

def load_expenses(file_path):
    return pd.read_csv(file_path, parse_dates=["date"])
