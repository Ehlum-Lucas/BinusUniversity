'''
 # @ Author: Lucas Iglesia
 # @ Create Time: 2024-11-20 08:47:17
 # @ Modified by: Lucas Iglesia
 # @ Modified time: 2024-11-20 08:48:59
 # @ Description: RelativeStrengthIndex class strategy
 '''

from backtesting import Strategy
from data import data

class RelativeStrengthIndex(Strategy):
    mysize = 0.1
    stoploss = 0.07
    takeprofit = 0.04
    fast_ma = 20
    slow_ma = 50
    buy_threshold = 30
    sell_threshold = 70
    rsi_period = 14

    def init(self) -> None:
        super().init()
        data['Signal'] = 0
        data['fast_ma'] = data['Close'].rolling(window=self.fast_ma, min_periods=1).mean()
        data['slow_ma'] = data['Close'].rolling(window=self.slow_ma, min_periods=1).mean()
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=self.rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.rsi_period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        data.loc[(data['fast_ma'] > data['slow_ma']) & (rsi < self.buy_threshold), 'Signal'] = 1
        data.loc[(data['fast_ma'] < data['slow_ma']) & (rsi > self.sell_threshold), 'Signal'] = -1
        self.signal = self.I(lambda: data.Signal)

    def next(self):
        super().next()
        current_close = self.data.Close[-1]
        sl = current_close - self.stoploss * current_close
        tp = current_close + self.takeprofit * current_close
        if self.signal == 1:
            self.buy(size=self.mysize, tp=tp, sl=sl)