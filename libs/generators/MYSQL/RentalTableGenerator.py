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


    def __get_uuid(self):
        self._counterID += 1
        return self._counterID


    def __get_total_time(self, fromDate, toDate):
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


    def __get_road_total_limit_length(self, dailyLimit, daysRent):
        return dailyLimit * (daysRent + 10)


    def __get_road_daily_limit_length(self):
        return random.randrange(50, 100)


    def __get_total_road_length(self, total_limit):
        return random.randrange(0, total_limit)


    def __get_satisfaction_rating(self):
        return random.randrange(0, 11)


    def __asserts(self, data):
        pass


    def generate(self, inputs):
        from_date = self.__get_from_date(inputs["customerBirthDate"])
        to_date = self.__get_to_date(from_date)
        total_time = self.__get_total_time(from_date, to_date)
        daily_limit = self.__get_road_daily_limit_length()
        total_limit = self.__get_road_total_limit_length(daily_limit, total_time)

        # to collection
        data = {
            "uuid": self.__get_uuid(),
            "total_time": total_time,
            "from_date": from_date,
            "to_date": to_date,
            "road_total_limit_length": total_limit,
            "road_daily_limit_length": daily_limit,
            "total_road_length": self.__get_total_road_length(total_limit),
            "satisfaction_rating": self.__get_satisfaction_rating()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["uuid"],
            data["total_time"],
            data["from_date"].strftime(self._date_format),
            data["to_date"].strftime(self._date_format),
            data["road_total_limit_length"],
            data["road_daily_limit_length"],
            data["total_road_length"],
            data["satisfaction_rating"]
        ])
