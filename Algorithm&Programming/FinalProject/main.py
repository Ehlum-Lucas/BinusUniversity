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
        self.root = root
        self.root.title("Range Selector")
        self.root.geometry("600x600")

        # Initialize entries storage
        self.entries = []

        # Setup UI components
        self.setup_ui()

    def setup_ui(self):
        # Create a label
        label = ctk.CTkLabel(self.root, text="Select a strategy to backtest", font=("Arial", 20, "bold"))
        label.pack(pady=10)

        # Dropdown menu for options
        strategies = ["Moving Average Crossover", "Relative Strength Index", "Michael Harris"]
        self.strategy_menu = ctk.CTkOptionMenu(self.root, values=strategies, command=self.update_inputs)
        self.strategy_menu.pack(pady=10)

        label = ctk.CTkLabel(self.root, text="Select a stock to trade", font=("Arial", 20, "bold"))
        label.pack(pady=10)

        tickers = ['Apple', 'S&P 500', 'EUR / USD']
        self.tickers_menu = ctk.CTkOptionMenu(self.root, values=tickers)
        self.tickers_menu.pack(pady=10)

        # Frame for range inputs
        self.entry_frame = ctk.CTkFrame(self.root)
        self.entry_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Initialize default range inputs
        self.create_checkboxes("Moving Average Crossover")

        # Submit button
        submit_button = ctk.CTkButton(self.root, text="Submit", command=self.submit_action)
        submit_button.pack(pady=10)

        # Label to display results
        self.result_label = ctk.CTkLabel(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def update_inputs(self, _):
        selected_option = self.strategy_menu.get()

        # Clear existing range inputs
        for widget in self.entry_frame.winfo_children():
            widget.destroy()

        # Dynamically create range inputs based on the selected option
        if selected_option == "Moving Average Crossover":
            self.create_checkboxes("Moving Average Crossover")
        elif selected_option == "Relative Strength Index":
            self.create_checkboxes("Relative Strength Index")
        elif selected_option == "Michael Harris":
            self.create_checkboxes("Michael Harris")

    def create_checkboxes(self, strategy_name):
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
    if row['Signal'] == 1:
            return row['Low'] - 1e-4
    elif row['Signal'] == -1:
        return row['High'] + 1e-4
    else:
        return np.nan

def add_points(data):
    data['Points'] = data.apply(lambda row: points(row), axis=1)

def moving_average_crossover(data, short_window, long_window):
    data['SMA_short'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['SMA_long'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    data['Signal'] = 0
    data.loc[data["SMA_short"] > data["SMA_long"], "Signal"] = 1
    data.loc[data["SMA_short"] <= data["SMA_long"], "Signal"] = -1
    add_points(data)
    return data

def relative_strength_index(data, fast_ma, slow_ma, rsi_period, buy_threshold, sell_threshold):
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
    data['Signal'] = 0
    data['Signal'] = data.apply(lambda x: generate_signal(x.name, data), axis=1)
    add_points(data)
    return data

def plot_candles(data):
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