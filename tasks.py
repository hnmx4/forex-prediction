from invoke import task
from src.utility import Utility
from src.importer import Importer
from src.predictor import Predictor


def gen_ohlc_15min():
    utility = Utility()
    importer = Importer()

    return utility.resample_ohlc(importer.historical_data, '15Min')

@task
def show(ctx):
    utility = Utility()
    utility.show_graph(gen_ohlc_15min())

@task
def preditc(ctx):
    predictor = Predictor(gen_ohlc_15min())
    predictor.predict_ar2()

@task
def kmeans(ctx):
    predictor = Predictor(gen_ohlc_15min())
    predictor.kmeans()
