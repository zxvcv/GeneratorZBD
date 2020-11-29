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


    def __get_uuid(self):
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


    def __get_e_mail(self, name, surname):
        return "{}.{}@gmail.com".format(name, surname)


    def __get_civil_status(self):
        return "married" if random.randrange(2) == 0 else "single"


    def __get_kids_number(self):
        return random.randrange(5)


    def __get_gender(self):
        return "MAN" if random.randrange(2) == 0 else "WOMAN"


    def __get_birthDate(self):
        return str_time_prop(self._birth_first_date, datetime.now() - relativedelta(years=20), 
            random.random())


    def __get_phone_number(self):
        number = ""
        for i in range(9):
            number += str(random.randrange(10))
        return number


    def __get_accound_date_create(self, customerbirthDate):
        return str_time_prop(customerbirthDate, datetime.now(), random.random())


    def __get_last_login(self, accoundDateCreate):
        return str_time_prop(accoundDateCreate, datetime.now(), random.random())


    def __asserts(self, data):
        pass


    def generate(self):
        gender = self.__get_gender()
        name = self.__get_name(gender)
        surname = self.__get_surname()
        birthDate = self.__get_birthDate()
        accound_date_create = self.__get_accound_date_create(birthDate)

        # to collection
        data = {
            "uuid": self.__get_uuid(),
            "name": name,
            "second_name": self.__get_second_name(gender),
            "surname": surname,
            "e_mail": self.__get_e_mail(name, surname),
            "civil_status": self.__get_civil_status(),
            "kids_number": self.__get_kids_number(),
            "gender": "NOT_SELECTED" if random.randrange(100) > 95 else gender,
            "birthDate": birthDate, #when writing will be changed to age
            "phone_number": self.__get_phone_number(),
            "accound_date_create": accound_date_create,
            "last_login": self.__get_last_login(accound_date_create),
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        age = relativedelta(datetime.now(), data["birthDate"])

        self._writer.writerow([
            data["uuid"],
            data["name"],
            data["second_name"],
            data["surname"],
            data["e_mail"],
            data["civil_status"],
            data["kids_number"],
            data["gender"],
            age.years,
            data["phone_number"],
            data["accound_date_create"].strftime(self._date_format),
            data["last_login"].strftime(self._date_format)
        ])

