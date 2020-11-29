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


class CostTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)


    def __get_costid(self):
        self._counterID += 1
        return self._counterID


    def __get_costtype(self):
        cost_types = self.settings["cost_types"]
        return cost_types[random.randrange(0, len(cost_types))]


    def __get_amount(self):
        return random.randrange(50, 100)


    def __get_reason(self):
        return "reason reason"


    def __asserts(self, data):
        pass


    def generate(self):
        # to collection
        data = {
            "costid": self.__get_costid(),
            "costtype": self.__get_costtype(),
            "amount": self.__get_amount(),
            "reason": self.__get_reason()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["costid"],
            data["costtype"],
            data["amount"],
            data["reason"]
        ])

