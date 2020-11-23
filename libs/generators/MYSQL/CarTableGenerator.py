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


class CarTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        # helpers
        self._date_format = self.settings["date_format"]
        self._cars_examples_num = self.settings["cars_examples_num"]
        self._birth_first_date = datetime.strptime(self.settings["birth_first_date"], self._date_format)


    def __get_uuid(self):
        self._counterID += 1
        return self._counterID


    def __get_brand(self, car_name):
        return car_name.split(" ")[0]


    def __get_model(self, car_name):
        return car_name.split(" ")[1]


    def __get_buying_data(self):
        return str_time_prop(self._birth_first_date, self._birth_first_date + relativedelta(years=19),
            random.random())


    def __get_last_check_date(self, buyingData):
        return str_time_prop(buyingData, datetime.now(), random.random())


    def __get_last_repair_date(self, buyingData):
        return str_time_prop(buyingData, datetime.now(), random.random())


    def __get_body_type(self):
        cars_body_types = self.settings["cars_body_types"]
        return cars_body_types[random.randrange(0, len(cars_body_types))]


    def __get_color(self):
        cars_colors = self.settings["cars_colors"]
        return cars_colors[random.randrange(0, len(cars_colors))]


    def __get_fuel_type(self):
        fuel_types = self.settings["fuel_types"]
        return fuel_types[random.randrange(0, len(fuel_types))]


    def __get_maxSpeed(self):
        return random.randrange(140, 300, 10)


    def __get_acceleration(self):
        return float(random.randrange(15, 300)) / 10



    def __asserts(self, data):
        pass


    def generate(self):
        car_num = random.randrange(0, self._cars_examples_num)
        car_name = get_file_lines(self.settings["cars_file"], [car_num])[0]
        buying_data = self.__get_buying_data()

        # to collection
        data = {
            "uuid": self.__get_uuid(),
            "brand": self.__get_brand(car_name),
            "model": self.__get_model(car_name),
            "buying_data": buying_data,
            "last_check_date": self.__get_last_check_date(buying_data),
            "last_repair_date": self.__get_last_repair_date(buying_data),
            "body_type": self.__get_body_type(),
            "color": self.__get_color(),
            "fuel_type": self.__get_fuel_type(),
            "max_speed": self.__get_maxSpeed(),
            "acceleration": self.__get_acceleration()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["uuid"],
            data["brand"],
            data["model"],
            data["buying_data"].strftime(self._date_format),
            data["last_check_date"].strftime(self._date_format),
            data["last_repair_date"].strftime(self._date_format),
            data["body_type"],
            data["color"],
            data["fuel_type"],
            data["max_speed"],
            data["acceleration"]
        ])

