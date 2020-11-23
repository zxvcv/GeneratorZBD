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


class ClientTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        # helpers
        self._date_format = self.settings["date_format"]
        self._files_examples_num = self.settings["files_examples_num"]
        self._birth_first_date = datetime.strptime(self.settings["birth_first_date"], self._date_format)


    def __get_id(self):
        self._counterID += 1
        return self._counterID


    def __get_name(self, gender):
        name = ""
        if gender == "male":
            name = get_file_lines(self.settings["male_names_file"], 
                [random.randrange(self._files_examples_num)])[0]
        else:
            name = get_file_lines(self.settings["female_names_file"], 
                [random.randrange(self._files_examples_num)])[0]
        return name


    def __get_surname(self):
        surname = get_file_lines(self.settings["surnames_file"], 
            [random.randrange(self._files_examples_num)])[0]
        return surname.capitalize()


    def __get_birthDate(self):
        return str_time_prop(self._birth_first_date, datetime.now() - relativedelta(years=20), 
            random.random())


    def __get_gender(self):
        return "male" if random.randrange(2) == 0 else "female"


    def __get_maritialStatus(self):
        return "married" if random.randrange(2) == 0 else "single"


    def __get_numberOfChildrens(self):
        return random.randrange(5)


    def __get_priceFactor(self):
        return float(random.randrange(50, 150)) / 100


    def __asserts(self, data):
        assert (data["name"] != ""), "Clients' name is empty"
        assert (data["surname"] != ""), "Clients' surname is empty"
        assert (data["birthDate"] > self._birth_first_date), "Client is too old"
        assert (data["birthDate"] < datetime.now() - relativedelta(years=20)), "Client is too young"
        assert (data["priceFactor"] < 1.51), "clients' price factor is bigger than 1,51"
        assert (data["priceFactor"] > 0.49), "clients' price factor is lower than 0,49"


    def generate(self):
        gender = self.__get_gender()

        # to collection
        data = {
            "id": self.__get_id(),
            "name": self.__get_name(gender),
            "surname": self.__get_surname(),
            "birthDate": self.__get_birthDate(),
            "gender": gender,
            "maritialStatus": self.__get_maritialStatus(),
            "numberOfChildrens": self.__get_numberOfChildrens(),
            "priceFactor": self.__get_priceFactor()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["name"],
            data["surname"],
            data["birthDate"].strftime(self._date_format),
            data["gender"],
            data["maritialStatus"],
            data["numberOfChildrens"],
            data["priceFactor"]
        ])

