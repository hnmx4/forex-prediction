from invoke import task
from src.utility import Utility
from src.importer import Importer
from src.forecaster import Forecaster


@task
def show(ctx):
    utility = Utility()

    importer = Importer()
    hd = importer.historical_data
    ohlc_15min = utility.resample_ohlc(hd, '15Min')

    utility.show_graph(ohlc_15min)

@task
def forecast(ctx):
    utility = Utility()
    importer = Importer()
    ohlc_15min = utility.resample_ohlc(importer.historical_data, '15Min')

    forecaster = Forecaster(ohlc_15min)
    forecaster.forecast()
