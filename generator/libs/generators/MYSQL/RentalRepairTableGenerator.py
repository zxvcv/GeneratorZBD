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


class RentalRepairTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)


    def __get_rental_uuid(self, rentalUiid):
        return rentalUiid


    def __get_repair_uuid(self, repairUiid):
        return repairUiid


    def __asserts(self, data):
        pass


    def generate(self, inputs):
        # to collection
        data = {
            "rental_uuid": self.__get_rental_uuid(inputs["rental_uuid"]),
            "repair_uuid": self.__get_repair_uuid(inputs["repair_uuid"])
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["rental_uuid"],
            data["repair_uuid"]
        ])

