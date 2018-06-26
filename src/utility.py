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

    @staticmethod
    def convert_minutes(minutes, hdata):
        ret = pd.DataFrame()
        for i in range(0, len(hdata), minutes):
            part = hdata[i:i + minutes]
            df = pd.DataFrame(columns=[
                'opening', 'closing', 'low', 'high', 'volume', 'date-time'
            ], data=[[
                part.loc[i, 'opening'],
                part.loc[i + len(part) - 1, 'closing'],
                min(part.low.values),
                max(part.high.values),
                np.sum(part.volume.values),
                part.loc[i, 'date-time']
            ]])
            ret = ret.append(df)
        return ret

    def show_graph(self):
        hdata_15 = self.convert_minutes(15, self.historical_data)

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
