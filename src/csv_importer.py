import csv
import os
import matplotlib.pyplot as plt
import mpl_finance as mpf


class CsvImporter:
    def __init__(self):
        data_dir = os.path.join(
            os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
            "data")

        files = []
        for _, _, f in os.walk(data_dir):
            files = f

        filenames = list(map(
            lambda x: os.path.join(data_dir, x),
            list(filter(lambda x: x.find(".csv") > 0, files))))

        self.historical_data = []
        for filename in filenames:
            with open(filename, newline='') as f:
                # historical data format:
                # [date, time, opening, closing, low, high, volume]
                self.historical_data.extend(list(csv.reader(f)))

    def gen_prices(self, t):
        price_type = {
            'opening': 2,
            'closing': 3,
            'low': 4,
            'high': 5
        }

        return list(map(lambda x: x[price_type[t]], self.historical_data))

    def show_graph(self):
        ax = plt.subplot()
        mpf.candlestick2_ohlc(
            ax,
            self.gen_prices('opening'),
            self.gen_prices('high'),
            self.gen_prices('low'),
            self.gen_prices('closing')
        )
        plt.show()
