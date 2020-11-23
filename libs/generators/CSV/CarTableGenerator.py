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
        self._cars_examples_num = self.settings["cars_examples_num"]


    def __get_id(self):
        self._counterID += 1
        return self._counterID


    def __get_model(self, car_name):
        return car_name.split(" ")[1]


    def __get_brand(self, car_name):
        return car_name.split(" ")[0]


    def __get_bodyType(self):
        cars_body_types = self.settings["cars_body_types"]
        return cars_body_types[random.randrange(0, len(cars_body_types))]


    def __get_color(self):
        cars_colors = self.settings["cars_colors"]
        return cars_colors[random.randrange(0, len(cars_colors))]


    def __get_fuelId(self):
        fuel_types = self.settings["fuel_types"]
        return fuel_types[random.randrange(0, len(fuel_types))]["id"]


    def __get_maxSpeed(self):
        return random.randrange(140, 300, 10)


    def __get_rentalPrice(self):
        return random.randrange(700, 3000)


    def __get_theftProbability(self):
        return float(random.randrange(50)) / 1000


    def __get_insuranceCost(self):
        return random.randrange(600, 2000)


    def __get_otherCosts(self):
        return random.randrange(500, 5000)


    def __get_dailyHireCost(self):
        return random.randrange(100, 1000)


    def __asserts(self, data):
        assert (data["id"] >= 0), "Cars' id can't be negative"


    def generate(self):
        car_num = random.randrange(0, self._cars_examples_num)
        car_name = get_file_lines(self.settings["cars_file"], [car_num])[0]

        # to collection
        data = {
            "id": self.__get_id(),
            "model": self.__get_model(car_name),
            "brand": self.__get_brand(car_name),
            "bodyType": self.__get_bodyType(),
            "color": self.__get_color(),
            "fuelId": self.__get_fuelId(),
            "maxSpeed": self.__get_maxSpeed(),
            "rentalPrice": self.__get_rentalPrice(),
            "theftProbability": self.__get_theftProbability(),
            "insuranceCost": self.__get_insuranceCost(),
            "otherCosts": self.__get_otherCosts(),
            "dailyHireCost": self.__get_dailyHireCost()
        }

        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["id"],
            data["model"],
            data["brand"],
            data["bodyType"],
            data["color"],
            data["fuelId"],
            data["maxSpeed"],
            data["rentalPrice"],
            data["theftProbability"],
            data["insuranceCost"],
            data["otherCosts"],
            data["dailyHireCost"]
        ])

