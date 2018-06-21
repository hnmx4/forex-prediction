import csv
import os


class CsvImporter:
    def __init__(self):
        historical_data_filename = os.path.join(
            os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
            "data",
            "USDJPY_2015_all.csv"
        )
        with open(historical_data_filename, newline='') as f:
            self.historical_data = list(csv.reader(f))

    def show_graph(self):
        print(self.historical_data)
