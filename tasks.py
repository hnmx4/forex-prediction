from invoke import task
from src.utility import Utility
from src.importer import Importer


@task
def show(ctx):
    utility = Utility()

    importer = Importer()
    hd = importer.historical_data
    ohlc_15min = utility.format_ohlc(hd.resample(rule='15Min'))

    utility.show_graph(ohlc_15min)
