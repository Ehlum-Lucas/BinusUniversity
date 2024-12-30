import numpy as np
import customtkinter as ctk
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from backtesting import Backtest
from strategy.MovingAverageCrossover import MovingAverageCrossover
from strategy.RelativeStrengthIndex import RelativeStrengthIndex
from strategy.MichaelHarris import MichaelHarris
from data import data, ticker, get_data

class App:
    def __init__(self, root):
        """
        Initializes the main application window.

        Args:
            root (Tk): The root window of the Tkinter application.
        """
        self.root = root
        self.root.title("Range Selector")
        self.root.geometry("600x600")

        self.entries = []

        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface for the application.

        This method creates and arranges various UI elements including labels, dropdown menus, frames, and buttons.
        It initializes the default range inputs and sets up the command for the submit button.

        UI Elements:
        - Label: "Select a strategy to backtest"
        - Dropdown menu for strategy options: ["Moving Average Crossover", "Relative Strength Index", "Michael Harris"]
        - Label: "Select a stock to trade"
        - Dropdown menu for stock options: ['Apple', 'S&P 500', 'EUR / USD']
        - Frame for range inputs
        - Submit button
        - Label to display results

        Commands:
        - `self.update_inputs`: Updates the input fields based on the selected strategy.
        - `self.submit_action`: Handles the action when the submit button is pressed.
        """
        label = ctk.CTkLabel(self.root, text="Select a strategy to backtest", font=("Arial", 20, "bold"))
        label.pack(pady=10)

        strategies = ["Moving Average Crossover", "Relative Strength Index", "Michael Harris"]
        self.strategy_menu = ctk.CTkOptionMenu(self.root, values=strategies, command=self.update_inputs)
        self.strategy_menu.pack(pady=10)

        label = ctk.CTkLabel(self.root, text="Select a stock to trade", font=("Arial", 20, "bold"))
        label.pack(pady=10)

        tickers = ['Apple', 'S&P 500', 'EUR / USD']
        self.tickers_menu = ctk.CTkOptionMenu(self.root, values=tickers)
        self.tickers_menu.pack(pady=10)

        self.entry_frame = ctk.CTkFrame(self.root)
        self.entry_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.create_checkboxes("Moving Average Crossover")

        submit_button = ctk.CTkButton(self.root, text="Submit", command=self.submit_action)
        submit_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def update_inputs(self, _):
        """
        Updates the checkboxes dynamically based on the selected strategy option from the strategy menu.

        This method clears any existing checkboxes in the entry frame and creates new checkboxes
        corresponding to the selected strategy option. The available strategy options are:
        - "Moving Average Crossover"
        - "Relative Strength Index"
        - "Michael Harris"

        Args:
            _: Placeholder for an event parameter (typically used in callback functions).
        """
        selected_option = self.strategy_menu.get()

        for widget in self.entry_frame.winfo_children():
            widget.destroy()

        if selected_option == "Moving Average Crossover":
            self.create_checkboxes("Moving Average Crossover")
        elif selected_option == "Relative Strength Index":
            self.create_checkboxes("Relative Strength Index")
        elif selected_option == "Michael Harris":
            self.create_checkboxes("Michael Harris")

    def create_checkboxes(self, strategy_name):
        """
        Creates checkboxes for the given trading strategy parameters.

        This method initializes a dictionary of options with BooleanVar values
        for 'stoploss' and 'takeprofit'. Depending on the strategy_name provided,
        additional options are added to the dictionary.

        The method also creates and packs a label and checkboxes for each option
        in the options dictionary into the entry_frame.

        Args:
            strategy_name (str): The name of the trading strategy for which
                                 checkboxes are to be created.
        """
        self.options = {
            'stoploss': ctk.BooleanVar(),
            'takeprofit': ctk.BooleanVar()
        }

        if strategy_name == 'Moving Average Crossover':
            self.options['short_window'] = ctk.BooleanVar()
            self.options['long_window'] = ctk.BooleanVar()
        elif strategy_name == 'Relative Strength Index':
            self.options['fast_ma'] = ctk.BooleanVar()
            self.options['slow_ma'] = ctk.BooleanVar()
            self.options['buy_threshold'] = ctk.BooleanVar()
            self.options['sell_threshold'] = ctk.BooleanVar()
            self.options['rsi_period'] = ctk.BooleanVar()

        self.label = ctk.CTkLabel(self.entry_frame, text="Select the parameters to train (the more you add the longer the training is):", font=("Arial", 14, 'bold'))
        self.label.pack(pady=10)

        for option, var in self.options.items():
            checkbox = ctk.CTkCheckBox(self.entry_frame, text=option, variable=var)
            checkbox.pack(anchor="w", padx=20, pady=5)

    def submit_action(self):
        """
        Handles the submission action for the trading strategy optimization.

        This function retrieves user-selected parameters, strategy, and ticker symbol,
        fetches the relevant data, and performs backtesting and optimization on the selected
        strategy using the specified parameters. It then prints the optimized parameters and
        calls the appropriate function to execute the strategy.
        """
        parameters = {
            'stoploss': [i/100 for i in range(1, 8)],
            'takeprofit': [i/100 for i in range(1, 8)],
            'short_window': range(10, 30, 5),
            'long_window': range(30, 60, 5),
            'fast_ma': range(10, 30, 5),
            'slow_ma': range(30, 60, 5),
            'rsi_period': range(10, 30, 5),
            'buy_threshold': range(20, 40, 5),
            'sell_threshold': range(60, 80, 5)
        }
        strategy = {
            'Moving Average Crossover': MovingAverageCrossover,
            'Relative Strength Index': RelativeStrengthIndex,
            'Michael Harris': MichaelHarris
        }
        tickers = {
            'Apple': 'AAPL',
            'S&P 500': '^GSPC',
            'EUR / USD': 'EURUSD=X'
        }
        selected_parameters = {}
        selected_strategy = self.strategy_menu.get()
        selected_ticker = self.tickers_menu.get()
        for option, var in self.options.items():
            if var.get():
                selected_parameters[option] = parameters[option]

        ticker = tickers[selected_ticker]
        data = get_data()
        if data.empty:
            exit(0)
        backtest = Backtest(data, strategy[selected_strategy], cash=10000, margin=1/5, commission=0.0002)
        stats = backtest.optimize(**selected_parameters, maximize='Return [%]', max_tries=3000, random_state=0)
        print(stats)
        strat = stats._strategy
        if selected_strategy == 'Moving Average Crossover':
            print(f"Optimized Parameters: Short Window: {strat.short_window}, Long Window: {strat.long_window}, Stoploss: {strat.stoploss}, Takeprofit: {strat.takeprofit}")
            moving_average_crossover(data, strat.short_window, strat.long_window)
        elif selected_strategy == 'Relative Strength Index':
            print(f"Optimized Parameters: Fast MA: {strat.fast_ma}, Slow MA: {strat.slow_ma}, RSI Period: {strat.rsi_period}, Buy Threshold: {strat.buy_threshold}, Sell Threshold: {strat.sell_threshold}")
            relative_strength_index(data, strat.fast_ma, strat.slow_ma, strat.rsi_period, strat.buy_threshold, strat.sell_threshold)
        elif selected_strategy == 'Michael Harris':
            print(f"Optimized Parameters: Stoploss: {strat.stoploss}, Takeprofit: {strat.takeprofit}")
            michael_harris(data)
        plot_candles(data)

def points(row):
    """
    Calculate points based on the 'Signal' value in the given row.

    Args:
    row (pd.Series): A pandas Series object containing at least the columns 'Signal', 'Low', and 'High'.

    Returns:
    float:
        - If 'Signal' is 1, returns 'Low' minus 0.0001.
        - If 'Signal' is -1, returns 'High' plus 0.0001.
        - Otherwise, returns NaN.
    """
    if row['Signal'] == 1:
            return row['Low'] - 1e-4
    elif row['Signal'] == -1:
        return row['High'] + 1e-4
    else:
        return np.nan

def add_points(data):
    """
    Adds a 'Points' column to the given DataFrame by applying the points function to each row.

    Args:
    data (pandas.DataFrame): The input DataFrame to which the 'Points' column will be added.
    """
    data['Points'] = data.apply(lambda row: points(row), axis=1)

def moving_average_crossover(data, short_window, long_window):
    """
    Calculate the moving average crossover signals for a given dataset.

    This function computes the short-term and long-term simple moving averages (SMA) 
    for the 'Close' prices in the dataset and generates buy/sell signals based on 
    the crossover of these moving averages.

    Args:
    data (pandas.DataFrame): The input data containing at least a 'Close' column with price data.
    short_window (int): The window size for the short-term moving average.
    long_window (int): The window size for the long-term moving average.

    Returns:
    pandas.DataFrame: The processed data with generated signals and added points.
    """
    data['SMA_short'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['SMA_long'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    data['Signal'] = 0
    data.loc[data["SMA_short"] > data["SMA_long"], "Signal"] = 1
    data.loc[data["SMA_short"] <= data["SMA_long"], "Signal"] = -1
    add_points(data)
    return data

def relative_strength_index(data, fast_ma, slow_ma, rsi_period, buy_threshold, sell_threshold):
    """
    Calculate the Relative Strength Index (RSI) for a given dataset and generate buy/sell signals.

    Args:
    data (pd.DataFrame): DataFrame containing the stock price data with a 'Close' column.
    fast_ma (int): Not used in the current implementation.
    slow_ma (int): Not used in the current implementation.
    rsi_period (int): The period over which to calculate the RSI.
    buy_threshold (float): The RSI value above which a buy signal is generated.
    sell_threshold (float): The RSI value below which a sell signal is generated.

    Returns:
    pd.DataFrame: The input DataFrame with additional columns for RSI and trading signals.
    """
    data['delta'] = data['Close'].diff()
    data['gain'] = np.where(data['delta'] > 0, data['delta'], 0)
    data['loss'] = np.where(data['delta'] < 0, -data['delta'], 0)
    avg_gain = data['gain'].rolling(window=rsi_period).mean()
    avg_loss = data['loss'].rolling(window=rsi_period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    data['Signal'] = 0
    data.loc[(data['RSI'] > buy_threshold) & (data['RSI'].shift(1) <= buy_threshold), 'Signal'] = 1
    data.loc[(data['RSI'] < sell_threshold) & (data['RSI'].shift(1) >= sell_threshold), 'Signal'] = -1
    add_points(data)
    return data

def generate_signal(candle, data):
    """
    Generates a trading signal based on the given candle and historical data.

    Parameters:
    candle (datetime): The specific candle (timestamp) for which to generate the signal.
    data (pandas.DataFrame): The historical data containing 'High', 'Low', and 'Close' prices.

    Returns:
    int: Returns 1 if the conditions for the trading signal are met, otherwise returns 0.
    """
    pos = data.index.get_loc(candle)

    if data['High'].iloc[pos] > data['Close'].iloc[pos] and \
        data['Close'].iloc[pos] > data['High'].iloc[pos-2] and \
        data['High'].iloc[pos-2] > data['High'].iloc[pos-1] and \
        data['High'].iloc[pos-1] > data['Low'].iloc[pos] and \
        data['Low'].iloc[pos] > data['Low'].iloc[pos-2] and \
        data['Low'].iloc[pos-2] > data['Low'].iloc[pos-1]:
        return 1
    return 0

def michael_harris(data):
    """
    Processes the given data by generating signals and adding points.

    This function performs the following steps:
    1. Initializes a 'Signal' column in the data with a default value of 0.
    2. Applies the `generate_signal` function to each row of the data to generate signals.
    3. Calls the `add_points` function to add points to the data based on the generated signals.

    Args:
        data (pandas.DataFrame): The input data to be processed.

    Returns:
        pandas.DataFrame: The processed data with generated signals and added points.
    """
    data['Signal'] = 0
    data['Signal'] = data.apply(lambda x: generate_signal(x.name, data), axis=1)
    add_points(data)
    return data

def plot_candles(data):
    """
    Plots a candlestick chart with entry points using Plotly.

    Parameters:
    data (pandas.DataFrame): A DataFrame containing the following columns:
        - 'Open': Opening prices
        - 'High': Highest prices
        - 'Low': Lowest prices
        - 'Close': Closing prices
        - 'Points': Entry points to be marked on the chart

    The DataFrame index should be the dates corresponding to the prices.
    """
    plot = make_subplots(rows=1, cols=1)
    plot.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Candlestick'), row=1, col=1)
    plot.add_trace(go.Scatter(x=data.index, y=data['Points'], mode="markers",
                             marker=dict(size=10, color="MediumPurple", symbol='circle'),
                             name="Entry Points"),
                             row=1, col=1)

    plot.update_layout(
        title_text="Candlestick Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white'),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        showlegend=True,
        legend=dict(
            x=0.01,
            y=0.99,
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color="white"
            ),
            bgcolor="black",
            bordercolor="gray",
            borderwidth=2
        )
    )
    plot.show()

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = App(root)
    root.mainloop()