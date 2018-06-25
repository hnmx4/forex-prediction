from invoke import task
from src.utility import Utility

@task
def show(ctx):
    utility = Utility()
    utility.show_graph()
