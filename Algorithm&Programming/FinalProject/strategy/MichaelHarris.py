'''
 # @ Author: Lucas Iglesia
 # @ Create Time: 2024-12-12 11:16:55
 # @ Modified by: Lucas Iglesia
 # @ Modified time: 2024-12-12 11:17:49
 # @ Description: Michael Harris strategy
 '''

from backtesting import Strategy
from data import data

class MichaelHarris(Strategy):
    trade_size = 0.1
    stoploss = 0.07
    takeprofit = 0.04

    def init(self):
        """
        Initializes the strategy by setting up the initial signal values and generating signals for the data.

        This method overrides the parent class's init method. It initializes the 'Signal' column in the data
        to 0 and then applies the generate_signal method to each row of the data to populate the 'Signal' column.
        Finally, it sets the signal attribute to the 'Signal' column of the data.
        """
        super().init()
        data['Signal'] = 0
        data['Signal'] = data.apply(lambda x: self.generate_signal(x.name, data), axis=1)
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
            self.buy(size=self.trade_size, tp=tp, sl=sl)

    def generate_signal(self, candle, data):
        """
        Generates a trading signal based on the given candle and historical data.

        Args:
        candle (pandas.Timestamp): The timestamp of the current candle.
        data (pandas.DataFrame): Historical market data containing 'High', 'Low', and 'Close' prices.

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
