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


class RentalTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        # helpers
        self._date_format = self.settings["date_format"]
        self._start_hire_minus_delta_days = self.settings["start_hire_minus_delta_days"]
        self._min_hire_time_hours = self.settings["min_hire_time_hours"]
        self._max_hire_length_months = self.settings["max_hire_length_months"]


    def __get_rentalid(self):
        self._counterID += 1
        return self._counterID


    def __get_totaltime(self, fromDate, toDate):
        delta = relativedelta(toDate, fromDate)
        return delta.days


    def __get_from_date(self, clientBirthDate):
        hireStartTime = str_time_prop(clientBirthDate + relativedelta(years=18), 
            datetime.now() - timedelta(days=self._start_hire_minus_delta_days), random.random())
        return hireStartTime


    def __get_to_date(self, hireStartTime):
        helper = str_time_prop(hireStartTime + relativedelta(hours=self._min_hire_time_hours), 
            hireStartTime + relativedelta(months=self._max_hire_length_months), random.random())
        hireEndTime = datetime.now() if helper > datetime.now() else  helper
        return hireEndTime


    def __get_satisfactionrating(self):
        return random.randrange(0, 11)


    def __asserts(self, data):
        pass


    def generate(self, inputs):
        from_date = self.__get_from_date(inputs["customerBirthDate"])
        to_date = self.__get_to_date(from_date)
        totaltime = self.__get_totaltime(from_date, to_date)

        # to collection
        data = {
            "rentalid": self.__get_rentalid(),
            "totaltime": totaltime,
            "from_date": from_date,
            "to_date": to_date,
            "satisfactionrating": self.__get_satisfactionrating()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        period = relativedelta(data["to_date"], data["from_date"])

        self._writer.writerow([
            data["rentalid"],
            data["totaltime"],
            period.days,
            data["satisfactionrating"]
        ])
