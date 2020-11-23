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


    def __get_uuid(self):
        self._counterID += 1
        return self._counterID


    def __get_cost_type(self):
        cost_types = self.settings["cost_types"]
        return cost_types[random.randrange(0, len(cost_types))]


    def __get_amount(self):
        return random.randrange(50, 100)


    def __get_description(self):
        return "description description description"



    def __asserts(self, data):
        pass


    def generate(self):
        # to collection
        data = {
            "uuid": self.__get_uuid(),
            "cost_type": self.__get_cost_type(),
            "amount": self.__get_amount(),
            "description": self.__get_description()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["uuid"],
            data["cost_type"],
            data["amount"],
            data["description"]
        ])

