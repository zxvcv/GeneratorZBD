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


    def __get_customer_uuid(self, customerUiid):
        return customerUiid


    def __get_rental_uuid(self, rentalUiid):
        return rentalUiid


    def __asserts(self, data):
        pass


    def generate(self, inputs):
        # to collection
        data = {
            "customer_uuid": self.__get_customer_uuid(inputs["customer_uuid"]),
            "rental_uuid": self.__get_rental_uuid(inputs["rental_uuid"])
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["customer_uuid"],
            data["rental_uuid"]
        ])

