import yfinance as yf
import numpy as np

def get_data():
    """
    Downloads historical stock data for a given ticker symbol over a 10-year period with daily intervals.

    Returns:
        pandas.DataFrame: A DataFrame containing the historical stock data if successful.
        None: If an error occurs or no data is found.

    Raises:
        ValueError: If no data is found for the given ticker symbol.
    """
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