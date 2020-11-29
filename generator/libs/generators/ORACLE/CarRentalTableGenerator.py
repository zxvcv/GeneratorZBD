import csv
import time
import random
import string
import numpy as np
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from ...helpers import get_file_lines, str_time_prop
from ...AbstractTableGenerator import AbstractTableGenerator


class CarRentalTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)


    def __get_carid(self, carId):
        return carId


    def __get_carRental(self):
        return random.randrange(20, 100)


    def __get_rentalid(self, rentalId):
        return rentalId


    def __asserts(self, data):
        pass


    def generate(self, inputs):
        # to collection
        data = {
            "carid": self.__get_carid(inputs["carid"]),
            "carrental": self.__get_carRental(),
            "rentalid": self.__get_rentalid(inputs["rentalid"])
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["carid"],
            data["carrental"],
            data["rentalid"]
        ])

