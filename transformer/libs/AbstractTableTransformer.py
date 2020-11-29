import os
import csv
import json
from .abstract import abstract


class AbstractTableTransformer:
    def __init__(self, settings, tableName):
        self.settings = settings
        self.tableName = tableName

        self._counterID = -1

        file_out_name = self.settings["out_tables"][self.tableName]["data_file"]

        dir_name = file_out_name.split("/")[0]
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        self.writeFile = open(file_out_name, "w+", newline='')
        self._writer = csv.writer(self.writeFile, delimiter=';')

        keys = self.settings["out_tables"][self.tableName]["keys"]
        self._writer.writerow(keys)


    def __del__(self):
        self.writeFile.close()


    def table_write(self): abstract()

    def generate(self): abstract()

