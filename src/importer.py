import os
import pandas as pd


class Importer:
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

        source = pd.DataFrame()
        for filename in filenames:
            with open(filename, newline='') as f:
                df = pd.read_csv(filename, header=None, names=[
                    'date', 'time', 'open', 'close', 'low', 'high', 'volume'])
                source = source.append(df)

        source['date-time'] = source['date'].str.cat(source['time'], sep='-')
        source.drop(['date', 'time'], axis=1, inplace=True)
        source['date-time'] = source['date-time'].map(lambda x: pd.to_datetime(x))
        source = source.set_index('date-time')
        source = source.ix[:, ['open', 'high', 'low', 'close', 'volume']]
        self.historical_data = source
