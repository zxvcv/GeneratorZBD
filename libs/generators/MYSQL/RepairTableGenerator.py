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


class RepairTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        # helpers
        self._date_format = self.settings["date_format"]
        self._birth_first_date = datetime.strptime(self.settings["birth_first_date"], self._date_format)


    def __get_uuid(self):
        self._counterID += 1
        return self._counterID


    def __get_by_who(self):
        by_who = self.settings["by_who"]
        return by_who[random.randrange(0, len(by_who))]


    def __get_coast(self):
        return float(random.randrange(0, 10000)) / 100


    def __get_repair_date(self):
        return str_time_prop(self._birth_first_date - relativedelta(years=22), datetime.now(), 
            random.random())


    def __get_description(self):
        return "description description description"



    def __asserts(self, data):
        pass


    def generate(self):
        # to collection
        data = {
            "uuid": self.__get_uuid(),
            "by_who": self.__get_by_who(),
            "coast": self.__get_coast(),
            "repair_date": self.__get_repair_date(),
            "description": self.__get_description(),
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["uuid"],
            data["by_who"],
            data["coast"],
            data["repair_date"].strftime(self._date_format),
            data["description"]
        ])

