'''
 # @ Author: Lucas Iglesia
 # @ Create Time: 2024-11-19 11:32:01
 # @ Modified by: Lucas Iglesia
 # @ Modified time: 2024-11-19 11:32:03
 # @ Description: main file
 '''

from backtesting import Backtest
from strategy.MovingAverageCrossover import MovingAverageCrossover
from strategy.RelativeStrengthIndex import RelativeStrengthIndex
from strategy.MichaelHarris import MichaelHarris
from data import data

# ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'] period
# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo] interval

def main():
    if data is None:
        return
    backtest = Backtest(data, RelativeStrengthIndex, cash=10000, margin=1/5, commission=0.0002)
    stats, heatmap = backtest.optimize( stoploss=[i/100 for i in range(1, 8)],
                                        takeprofit=[i/100 for i in range(1, 8)],
                                        maximize='Return [%]', max_tries=3000,
                                        random_state=0,
                                        return_heatmap=True)
    print(stats)

if __name__ == "__main__":
    main()
