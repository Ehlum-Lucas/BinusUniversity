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
        super().init()
        data['Signal'] = 0
        data['Signal'] = data.apply(lambda x: self.generate_signal(x.name, data), axis=1)
        self.signal = self.I(lambda: data.Signal)

    def next(self):
        super().next()
        current_close = self.data.Close[-1]
        sl = current_close - self.stoploss * current_close
        tp = current_close + self.takeprofit * current_close
        if self.signal == 1:
            self.buy(size=self.trade_size, tp=tp, sl=sl)

    def generate_signal(self, candle, data):
        pos = data.index.get_loc(candle)

        if data['High'].iloc[pos] > data['Close'].iloc[pos] and \
            data['Close'].iloc[pos] > data['High'].iloc[pos-2] and \
            data['High'].iloc[pos-2] > data['High'].iloc[pos-1] and \
            data['High'].iloc[pos-1] > data['Low'].iloc[pos] and \
            data['Low'].iloc[pos] > data['Low'].iloc[pos-2] and \
            data['Low'].iloc[pos-2] > data['Low'].iloc[pos-1]:
            return 1
        return 0
