import csv
import os


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

        hdata = []
        for filename in filenames:
            with open(filename, newline='') as f:
                # historical data format:
                # [date, time, opening, closing, low, high, volume]
                hdata.extend(list(csv.reader(f)))
        for row in hdata:
            for i in range(2, 7):
                row[i] = float(row[i])
        self.historical_data = hdata
