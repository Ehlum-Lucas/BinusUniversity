'''
 # @ Author: Lucas Iglesia
 # @ Create Time: 2024-11-19 11:21:20
 # @ Modified by: Lucas Iglesia
 # @ Modified time: 2024-11-19 11:21:23
 # @ Description: Backtester class
 '''

import pandas as pd
import matplotlib.pyplot as plt
from strategy.Strategy import Strategy
class Backtester:
    def __init__(self, data: pd.DataFrame, strategy: Strategy, initial_capital: int = 10000) -> None:
        self.data = data
        self.strategy = strategy
        self.initial_capital = initial_capital

    def run_backtest(self):
        """
        Apply the strategy to the data and calculate the cumulative returns.
        """
        self.data = self.strategy.generate_signals(self.data)
        self.data['Returns'] = self.data['Close'].pct_change()
        self.data['Strategy_returns'] = self.data['Returns'] * self.data['Signal'].shift(1)
        self.cumulative_returns = (1 + self.data['Strategy_returns']).cumprod()
        self.final_balance = self.initial_capital * self.cumulative_returns.iloc[-1]
        print(self.data.tail(5))
        print(f"Initial Capital: {self.initial_capital}")
        print(f"Final Balance: {self.final_balance}")
        print(f'Performance: {round((self.final_balance - self.initial_capital) / self.initial_capital * 100, 2)}%')
        return self.cumulative_returns

    def plot_results(self):
        """
        Plot the cumulative returns.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.cumulative_returns, label="Strategy Cumulative Returns")
        plt.plot((1 + self.data["Returns"]).cumprod(), label="Market Cumulative Returns")
        plt.legend()
        plt.title(f"Backtest Results for {self.strategy.name}")
        plt.show()

        # plt.figure(figsize=(12, 6))
        # plt.plot(self.data['Close'], label='Close Price', alpha=0.7)
        # plt.plot(self.data['fast_ma'], label=f'{self.strategy.fast_ma}-day MA', linestyle='--')
        # plt.plot(self.data['slow_ma'], label=f'{self.strategy.slow_ma}-day MA', linestyle='--')
        # plt.scatter(self.data.index, self.data['Signal'] == 1, label='Buy Signal', marker='^', color='green', alpha=1)
        # plt.scatter(self.data.index, self.data['Signal'] == -1, label='Sell Signal', marker='v', color='red', alpha=1)
        # plt.legend(loc='upper left')
        # plt.title(f'Backtest Results for {self.strategy.name}')
        # plt.show()