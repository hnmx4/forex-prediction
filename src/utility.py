import matplotlib.pyplot as plt
import mpl_finance as mpf
import pandas as pd
import numpy as np

from .csv_importer import CsvImporter


class Utility:
    def __init__(self):
        importer = CsvImporter()
        self.historical_data = importer.historical_data

    @staticmethod
    def gen_prices(t, hdata):
        price_type = {
            'opening': 2,
            'closing': 3,
            'low': 4,
            'high': 5,
            'volume': 6
        }

        return list(map(lambda x: x[price_type[t]], hdata))

    def show_graph(self):
        print(self.historical_data.head())
        hdata_15 = self.historical_data.resample(rule='15M').ohlc()  # not working
        print(hdata_15.head())

        ax = plt.subplot()
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        mpf.candlestick2_ohlc(
            ax,
            hdata_15.opening.values,
            hdata_15.high.values,
            hdata_15.low.values,
            hdata_15.closing.values,
            0.5, 'r', 'b'
        )

        plt.show()
