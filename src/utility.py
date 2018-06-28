import matplotlib.pyplot as plt
import mpl_finance as mpf
import pandas as pd


from .importer import Importer


class Utility:
    def __init__(self):
        importer = Importer()
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

    @staticmethod
    def show_graph(ohlc):
        ax = plt.subplot()
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        mpf.candlestick2_ohlc(
            ax,
            ohlc.open.values,
            ohlc.high.values,
            ohlc.low.values,
            ohlc.close.values,
            0.5, 'r', 'b'
        )

        plt.show()
