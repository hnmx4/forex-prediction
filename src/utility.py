import matplotlib.pyplot as plt
import mpl_finance as mpf
import pandas as pd


from .csv_importer import CsvImporter


class Utility:
    def __init__(self):
        importer = CsvImporter()
        self.historical_data = importer.historical_data

    @staticmethod
    def format_ohlc(df):
        ohlc = df.ohlc()
        ret = {
            'open': ohlc['open']['open'].values,
            'high': ohlc['high']['high'].values,
            'low': ohlc['low']['low'].values,
            'close': ohlc['close']['close'].values
        }
        return pd.DataFrame(data=ret, columns=['open', 'high', 'low', 'close'], index=ohlc.index).dropna()

    def show_graph(self):
        hdata_15 = self.format_ohlc(self.historical_data.resample(rule='15Min'))
        print(hdata_15.head())

        ax = plt.subplot()
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        mpf.candlestick2_ohlc(
            ax,
            hdata_15.open.values,
            hdata_15.high.values,
            hdata_15.low.values,
            hdata_15.close.values,
            0.5, 'r', 'b'
        )

        plt.show()
