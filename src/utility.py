import matplotlib.pyplot as plt
import mpl_finance as mpf

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

    def convert_minutes(self, minutes, hdata):
        ret = []
        for i in range(0, len(hdata), minutes):
            part = hdata[i:i + minutes]
            ret.append([
                part[0][0],  # data
                part[0][1],  # time
                part[0][2],  # opening
                part[-1][3],  # closing
                min(self.gen_prices("low", part)),  # low
                max(self.gen_prices("high", part)),  # high
                sum(self.gen_prices("volume", part))  # volume
            ])

        return ret

    def show_graph(self):
        hdata_15 = self.convert_minutes(15, self.historical_data)

        ax = plt.subplot()
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        mpf.candlestick2_ohlc(
            ax,
            self.gen_prices('opening', hdata_15),
            self.gen_prices('high', hdata_15),
            self.gen_prices('low', hdata_15),
            self.gen_prices('closing', hdata_15),
            0.5, 'r', 'b'
        )

        plt.show()
