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


class ClientTableTransformer(AbstractTableTransformer):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        self.clientsIdCounter = 0
        self.allClients = []

        # helpers
        self._date_format = self.settings["date_format"]
        self._date_format_out = self.settings["date_format_out"]


    def __get_ageGroup(self, birthDate):
        date = datetime.strptime(birthDate, self._date_format)
        age = relativedelta(datetime.now(), date).years

        age_group = "Unknown"
        if age <= 25:
            age_group = "15-25"
        elif age <= 35:
            age_group = "26-35"
        elif age <= 45:
            age_group = "36-45"
        elif age <= 55:
            age_group = "46-55"
        elif age <= 65:
            age_group = "56-65"
        elif age <= 75:
            age_group = "66-75"
        elif age <= 85:
            age_group = "76-85"
        elif age >= 86:
            age_group = "86-95"

        return age_group


    def __get_gender(self, gender):
        return gender


    def __get_married(self, married):
        status = "Unknown"

        if married == "married":
            status = "true"
        elif married == "single":
            status = "false"

        return status


    def __get_children(self, children):
        return children


    def __asserts(self, data):
        pass


    def __check_for_repeaters(self, data):
        for i in self.allClients:
            if data["AGE_GROUP"] == i["AGE_GROUP"] and data["GENDER"] == i["GENDER"] and data["MARRIED"] == i["MARRIED"] and data["CHILDREN"] == i["CHILDREN"]:
                data = i
                break
        else:
            data["CLIENTID"] = self.clientsIdCounter
            self.allClients.append(data)
            self.clientsIdCounter += 1
        return data


    def transform(self, src_data):
        # to collection
        data = {
            "CLIENTID": None,
            "AGE_GROUP": self.__get_ageGroup(src_data["client_birthDate"]),
            "GENDER": self.__get_gender(src_data["client_gender"]),
            "MARRIED": self.__get_married(src_data["client_married"]),
            "CHILDREN": self.__get_children(src_data["client_children"])
        }

        self.__asserts(data)
        data = self.__check_for_repeaters(data)
        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["CLIENTID"],
            data["AGE_GROUP"],
            data["GENDER"],
            data["MARRIED"],
            data["CHILDREN"]
        ])


    def table_write_all(self):
        for item in self.allClients:
            self.table_write(item)
