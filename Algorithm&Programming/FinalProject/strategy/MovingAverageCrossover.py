'''
 # @ Author: Lucas Iglesia
 # @ Create Time: 2024-11-19 11:18:01
 # @ Modified by: Lucas Iglesia
 # @ Modified time: 2024-11-19 11:18:03
 # @ Description: MovingAverageCrossover class strategy
 '''

from backtesting import Strategy
from data import data

class MovingAverageCrossover(Strategy):
    mysize = 0.1
    stoploss = 0.07
    takeprofit = 0.04
    short_window = 20
    long_window = 50

    def init(self) -> None:
        """
        Initializes the Moving Average Crossover strategy by calculating the short-term
        and long-term simple moving averages (SMA) for the given data. It then generates
        trading signals based on the crossover of these SMAs.
        """
        super().init()
        data['SMA_short'] = data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        data['SMA_long'] = data['Close'].rolling(window=self.long_window, min_periods=1).mean()
        data['Signal'] = 0
        data.loc[data["SMA_short"] > data["SMA_long"], "Signal"] = 1
        data.loc[data["SMA_short"] <= data["SMA_long"], "Signal"] = -1
        self.signal = self.I(lambda: data.Signal)

    def next(self):
        """
        Executes the next step in the trading strategy.

        This method is called to perform the next action in the trading strategy.
        It calculates the stop loss (sl) and take profit (tp) levels based on the
        current closing price and predefined stop loss and take profit percentages.
        If the signal is 1, it executes a buy order with the specified trade size,
        take profit, and stop loss levels.
        """
        super().next()
        current_close = self.data.Close[-1]
        sl = current_close - self.stoploss * current_close
        tp = current_close + self.takeprofit * current_close
        if self.signal == 1:
            self.buy(size=self.mysize, tp=tp, sl=sl)
