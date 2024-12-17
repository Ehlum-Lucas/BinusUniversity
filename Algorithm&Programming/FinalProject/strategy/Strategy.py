'''
 # @ Author: Lucas Iglesia
 # @ Create Time: 2024-11-19 11:03:47
 # @ Modified by: Lucas Iglesia
 # @ Modified time: 2024-11-19 11:03:49
 # @ Description: Strategy class
 '''

import pandas as pd

class Strategy:
    def __init__(self, name: str) -> None:
        self.name = name

    def generate_signals(self, data: pd.DataFrame):
        """
        Abstract method to generate signals.
        :param data: A pandas DataFrame containing market data.
        """
        raise NotImplementedError("Subclasses should implement generate_signals() method.")
