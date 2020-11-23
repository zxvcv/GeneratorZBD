import csv
import time
import random
import string
import numpy as np
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from ...helpers import get_file_lines, str_time_prop
from AbstractTableGenerator import AbstractTableGenerator


class HireTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super.__init__(settings, tableName)

        # helpers
        self._date_format = self.settings["date_format"]
        self._start_hire_minus_delta_days = self.settings["start_hire_minus_delta_days"]
        self._min_hire_time_hours = self.settings["min_hire_time_hours"]
        self._max_hire_length_months = self.settings["max_hire_length_months"]


    def __get_id(self):
        self.counterID += 1
        return self.counterID


    def __get_hireStartTime(self, clientBirthDate):
        hireStartTime = str_time_prop(clientBirthDate + relativedelta(years=18), 
            datetime.now() - timedelta(days=self._start_hire_minus_delta_days), random.random())
        return hireStartTime


    def __get_hireEndTime(self, hireStartTime):
        helper = self.__str_time_prop(hireStartTime + relativedelta(hours=self._min_hire_time_hours), 
            hireStartTime + relativedelta(months=self._max_hire_length_months), random.random())
        hireEndTime = datetime.now() if helper > datetime.now() else  helper
        return hireEndTime


    def __get_carID(self, carID):
        return carID


    def __get_clientID(self, clientID):
        return clientID


    def __get_clientSatisfaction(self):
        return random.randrange(0, 11)


    def __get_roadLength(self, hireEndTime, hireStartTime):
        helper = hireEndTime - hireStartTime
        roadLength = helper.days * float(random.randrange(0, 1000)) / 10
        return roadLength


    def __get_repairsCost(self):
        helper = 1 if random.randrange(0, 100) == 0 else 0
        repairsCost = helper * random.randrange(0, 200) * 100
        return repairsCost


    def __asserts(self, data):
        assert (data["hireStartTime"] >= datetime.strptime(self.settings["birth_first_date"],
            self._date_format)),"Hire Start Time is too small"
        assert (data["hireStartTime"] <= datetime.now() - 
            relativedelta(days=self._start_hire_minus_delta_days)), "Hire Start Time is too big"
        assert (data["hireEndTime"] >= datetime.strptime(self.settings["birth_first_date"],
            self._date_format)), "Hire End Time is too small"
        assert (data["hireEndTime"] <= datetime.now()), "Hire End Time is too big"
        assert (data["carId"] >= 0), "CarID cant be negative"
        assert (data["clientId"] >= 0), "ClientID cant be negative"
        assert (data["clientSatisfaction"] >= 0), "Clients' satisfaction cant be negative"
        assert (data["clientSatisfaction"] <= 10), "Clients' satisfaction cant be bigger than 10"
        assert (data["roadLength"] >= 0), "road cant be negative"
        assert (data["repairsCost"] >= 0), "repairs cost cant be negative"
        assert (data["repairsCost"] <= 20000), "repairs cost cant be greater than 20000"


    def generate(self, inputs):
        hireStartTime = self.__get_hireStartTime(inputs["clientBirthDate"])
        hireEndTime = self.__get_hireEndTime(hireStartTime)

        # to collection
        data = {
            "hireStartTime": hireStartTime,
            "hireEndTime": hireEndTime,
            "carId": self.__get_carID(inputs["carID"]),
            "clientId": self.__get_clientID(inputs["clientID"]),
            "clientSatisfaction": self.__get_clientSatisfaction(),
            "roadLength": self.__get_roadLength(hireEndTime, hireStartTime),
            "repairsCost": self.__get_repairsCost()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self.hireWriter.writerow([
            data["hireStartTime"].strftime(self._date_format),
            data["hireEndTime"].strftime(self._date_format),
            data["carId"],
            data["clientId"],
            data["clientSatisfaction"],
            data["roadLength"],
            data["repairsCost"]
        ])
