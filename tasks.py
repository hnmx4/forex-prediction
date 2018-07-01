from invoke import task
from src.utility import Utility
from src.importer import Importer
from src.predictor import Predictor


@task
def show(ctx):
    utility = Utility()

    importer = Importer()
    hd = importer.historical_data
    ohlc_15min = utility.resample_ohlc(hd, '15Min')

    utility.show_graph(ohlc_15min)

@task
def preditc(ctx):
    utility = Utility()
    importer = Importer()
    ohlc_15min = utility.resample_ohlc(importer.historical_data, '15Min')

    predictor = Predictor(ohlc_15min)
    predictor.predict_ar2()
