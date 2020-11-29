import csv
import time
import random
import string
import numpy as np
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from ...helpers import get_file_lines, str_time_prop
from ...AbstractTableTransformer import AbstractTableTransformer


class CarTableTransformer(AbstractTableTransformer):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        self.carsIdCounter = 0
        self.allCars = []

        # helpers
        self._date_format = self.settings["date_format"]


    def __get_carBrand(self, brand):
        return brand


    def __get_carModel(self, model):
        return model


    def __asserts(self, data):
        pass


    def __check_for_repeaters(self, data):
        for i in self.allCars:
            if data["BRAND"] == i["BRAND"] and data["MODELL"] == i["MODELL"]:
                data = i
                break
        else:
            data["CARID"] = self.carsIdCounter
            self.allCars.append(data)
            self.carsIdCounter += 1
        return data


    def transform(self, src_data):
        # to collection
        data = {
            "CARID": None,
            "BRAND": self.__get_carBrand(src_data["carBrand"]),
            "MODELL": self.__get_carModel(src_data["carModel"])
        }

        self.__asserts(data)
        data = self.__check_for_repeaters(data)
        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["CARID"],
            data["BRAND"],
            data["MODELL"]
        ])


    def table_write_all(self):
        for item in self.allCars:
            self.table_write(item)
