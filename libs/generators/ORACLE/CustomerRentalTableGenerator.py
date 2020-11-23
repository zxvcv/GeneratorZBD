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


class CustomerRentalTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)


    def __get_customerid(self, customerId):
        return customerId


    def __get_rentalid(self, rentalId):
        return rentalId


    def __asserts(self, data):
        pass


    def generate(self, inputs):
        # to collection
        data = {
            "customerid": self.__get_customerid(inputs["customerid"]),
            "rentalid": self.__get_rentalid(inputs["rentalid"])
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["customerid"],
            data["rentalid"]
        ])

