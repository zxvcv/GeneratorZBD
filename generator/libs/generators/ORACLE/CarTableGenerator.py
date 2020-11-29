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


    def __get_carid(self):
        self._counterID += 1
        return self._counterID


    def __get_brand(self, car_name):
        return car_name.split(" ")[0]


    def __get_model(self, car_name):
        return car_name.split(" ")[1]


    def __get_bodytype(self):
        cars_body_types = self.settings["cars_body_types"]
        return cars_body_types[random.randrange(0, len(cars_body_types))]


    def __get_color(self):
        cars_colors = self.settings["cars_colors"]
        return cars_colors[random.randrange(0, len(cars_colors))]


    def __get_fueltype(self):
        fuel_types = self.settings["fuel_types"]
        return fuel_types[random.randrange(0, len(fuel_types))]


    def __get_maxspeed(self):
        return random.randrange(140, 300, 10)


    def __get_acceleration(self):
        return float(random.randrange(15, 300)) / 10



    def __asserts(self, data):
        pass


    def generate(self):
        car_num = random.randrange(0, self._cars_examples_num)
        car_name = get_file_lines(self.settings["cars_file"], [car_num])[0]

        # to collection
        data = {
            "carid": self.__get_carid(),
            "brand": self.__get_brand(car_name),
            "model": self.__get_model(car_name),
            "bodytype": self.__get_bodytype(),
            "color": self.__get_color(),
            "fueltype": self.__get_fueltype(),
            "maxspeed": self.__get_maxspeed(),
            "acceleration": self.__get_acceleration()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["carid"],
            data["brand"],
            data["model"],
            data["bodytype"],
            data["color"],
            data["fueltype"],
            data["maxspeed"],
            data["acceleration"]
        ])

