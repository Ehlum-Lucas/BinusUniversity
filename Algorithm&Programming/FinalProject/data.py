import yfinance as yf
import numpy as np

def get_data():
    try:
        data = yf.download(ticker, period='10y', interval='1d', progress=True)
        if data.empty:
            raise ValueError("No data found")
    except Exception as e:
        print(f"Error: {e}")
        return None
    return data

global data
global ticker
ticker = "^GSPC"
data = get_data()