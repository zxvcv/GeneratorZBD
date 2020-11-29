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


class CustomerTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        # helpers
        self._date_format = self.settings["date_format"]
        self._files_examples_num = self.settings["files_examples_num"]
        self._birth_first_date = datetime.strptime(self.settings["birth_first_date"], self._date_format)


    def __get_customerid(self):
        self._counterID += 1
        return self._counterID


    def __get_name(self, gender):
        name = ""
        if gender == "MAN":
            name = get_file_lines(self.settings["male_names_file"], 
                [random.randrange(self._files_examples_num)])[0]
        else:
            name = get_file_lines(self.settings["female_names_file"], 
                [random.randrange(self._files_examples_num)])[0]
        return name


    def __get_second_name(self, gender):
        name = ""
        if gender == "MAN":
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


    def __get_email(self, name, surname):
        return "{}.{}@gmail.com".format(name, surname)


    def __get_married(self):
        return random.randrange(2)


    def __get_children(self):
        return random.randrange(5)


    def __get_gender(self):
        return "man" if random.randrange(2) == 0 else "woman"


    def __get_birthDate(self):
        return str_time_prop(self._birth_first_date, datetime.now() - relativedelta(years=20), 
            random.random())


    def __get_phonenumber(self):
        number = ""
        for i in range(9):
            number += str(random.randrange(10))
        return number


    def __asserts(self, data):
        pass


    def generate(self):
        gender = self.__get_gender()
        name = self.__get_name(gender)
        surname = self.__get_surname()
        birthDate = self.__get_birthDate()

        # to collection
        data = {
            "customerid": self.__get_customerid(),
            "name": name,
            "surname": surname,
            "email": self.__get_email(name, surname),
            "married": self.__get_married(),
            "children": self.__get_children(),
            "gender": "not_selected" if random.randrange(100) > 95 else gender,
            "birthDate": birthDate, #when writing will be changed to age
            "phonenumber": self.__get_phonenumber()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        age = relativedelta(datetime.now(), data["birthDate"])

        self._writer.writerow([
            data["customerid"],
            data["name"],
            data["surname"],
            data["email"],
            data["married"],
            data["children"],
            data["gender"],
            age.years,
            data["phonenumber"]
        ])

