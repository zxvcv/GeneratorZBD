import csv
import json
from abstract import abstract


class AbstractTableGenerator:
    def __init__(self, settings, tableName):
        self.settings = settings
        self.tableName = tableName

        self.counterID = -1

        file_name = self.settings["tables"][self.tableName]["data_file"]
        self.writeFile = open(file_name, "w", newline='')
        self.writer = csv.writer(self.writeFile, delimiter=';')

        keys = self.settings["tables"][self.tableName]["keys"]
        self.writer.writerow(keys)


    def __del__(self):
        self.writeFile.close()


    def table_write(self): abstract()

    def generate(self): abstract()

