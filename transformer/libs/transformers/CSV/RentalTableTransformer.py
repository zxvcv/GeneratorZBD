import csv
import time
import random
import string
import numpy as np
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from ...helpers import get_file_lines, str_time_prop
from ...AbstractTableTransformer import AbstractTableTransformer


class RentalTableTransformer(AbstractTableTransformer):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        # helpers
        self._date_format = self.settings["date_format"]
        self._date_format_out = self.settings["date_format_out"]


    def __get_clientID(self, clientID):
        return clientID


    def __get_carID(self, carID):
        return carID


    def __get_rentalTime(self, hireStartTime, hireEndTime):
        hireStartTime = datetime.strptime(hireStartTime, self._date_format)
        hireEndTime = datetime.strptime(hireEndTime, self._date_format)
        rentalTime = relativedelta(hireEndTime, hireStartTime).days
        return rentalTime


    def __get_totalPrice(self, repairsCost, totalIncome):
        totalPrice = float(totalIncome) - int(repairsCost)
        return "{:.2f}".format(totalPrice)


    def __get_avgSatisfaction(self, clientSatisfaction):
        return clientSatisfaction


    def __get_dailyIncome(self, totalIncome, rentalTime):
        if rentalTime == 0:
            rentalTime = 1
        dailyIncome = float(totalIncome) / int(rentalTime)
        return "{:.2f}".format(dailyIncome)


    def __get_repairsCost(self, repairsCost):
        return int(repairsCost)


    def __get_totalIncome(self, rentalTime, carDailyHireCost, clientPriceFactor):
        totalIncome = int(rentalTime) * int(carDailyHireCost) * float(clientPriceFactor)
        return "{:.2f}".format(totalIncome)


    def __get_fromTime(self, hireEndTime):
        hireEndTime = datetime.strptime(hireEndTime, self._date_format)
        return hireEndTime.strftime(self._date_format_out)


    def __asserts(self, data):
        pass


    def transform(self, src_data):
        rentalTime = self.__get_rentalTime(src_data["hireStartTime"], src_data["hireEndTime"])
        repairsCost = self.__get_repairsCost(src_data["repairsCost"])
        totalIncome = self.__get_totalIncome(rentalTime, src_data["carDailyHireCost"],
            src_data["clientPriceFactor"])
        
        # to collection
        data = {
            "CLIENTID": self.__get_clientID(src_data["clientID"]),
            "CARID": self.__get_carID(src_data["carID"]),
            "RENTAL_TIME": rentalTime,
            "TOTAL_PRICE": self.__get_totalPrice(repairsCost, totalIncome),
            "AVG_SATISFACTION": self.__get_avgSatisfaction(src_data["clientStaisfaction"]),
            "DAILY_INCOME": self.__get_dailyIncome(totalIncome, rentalTime),
            "REPAIRS_COST": repairsCost,
            "TOTAL_INCOME": totalIncome,
            "FROM_TIME": self.__get_fromTime(src_data["hireEndTime"])
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["CLIENTID"],
            data["CARID"],
            data["RENTAL_TIME"],
            data["TOTAL_PRICE"],
            data["AVG_SATISFACTION"],
            data["DAILY_INCOME"],
            data["REPAIRS_COST"],
            data["TOTAL_INCOME"],
            data["FROM_TIME"]
        ])
