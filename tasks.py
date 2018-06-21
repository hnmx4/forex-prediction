from invoke import task
from src import csv_importer

@task
def show(ctx):
    importer = csv_importer.CsvImporter()
    importer.show_graph()
