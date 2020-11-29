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


class CarDetailsTableTransformer(AbstractTableTransformer):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)

        self.carDetailsIdCounter = 0
        self.allCarDetails = []

        # helpers
        self._date_format = self.settings["date_format"]


    def __get_carID(self, carId):
        return carId


    def __get_carBodyType(self, carBodyType):
        return carBodyType.lower()


    def __get_carColor(self, carColor):
        return carColor.lower()


    def __get_carFuelType(self, carFuelType):
        return carFuelType.lower()


    def __get_carMaxSpeed(self, carMaxSpeed):
        carMaxSpeed = int(carMaxSpeed)
        maxSpeedGroup = "Unknown"

        if carMaxSpeed < 195:
            maxSpeedGroup = "140-190"
        elif carMaxSpeed < 255:
            maxSpeedGroup = "200-250"
        elif carMaxSpeed > 255:
            maxSpeedGroup = "260-310"

        return maxSpeedGroup


    def __get_carRentalPrice(self, carRentalprice):
        carRentalprice = int(carRentalprice) / 10 #inna waluta
        rentalPriceGroup = "Unknown"

        if carRentalprice <= 20:
            rentalPriceGroup = "0-20"
        elif carRentalprice <= 40:
            rentalPriceGroup = "21-40"
        elif carRentalprice <= 60:
            rentalPriceGroup = "41-60"
        elif carRentalprice <= 80:
            rentalPriceGroup = "61-80"
        elif carRentalprice > 80:
            rentalPriceGroup = "81-100"

        return rentalPriceGroup


    def __get_carMaintenanceCost(self, insuranceCost, otherCosts):
        maintenanceCost = int(insuranceCost) + int(otherCosts)
        maintenanceCostGroup = "Unknown"

        if maintenanceCost <= 2000:
            maintenanceCostGroup = "0-2000"
        elif maintenanceCost <= 4000:
            maintenanceCostGroup = "2001-4000"
        elif maintenanceCost <= 6000:
            maintenanceCostGroup = "4001-6000"
        elif maintenanceCost <= 8000:
            maintenanceCostGroup = "6001-8000"
        elif maintenanceCost > 8000:
            maintenanceCostGroup = "8001-10000"

        return maintenanceCostGroup


    def __asserts(self, data):
        pass


    def __check_for_repeaters(self, data):
        for i in self.allCarDetails:
            if data["CARID"] == i["CARID"] and data["BODYTYPE"] == i["BODYTYPE"] and \
               data["COLOR"] == i["COLOR"] and data["FUEL_TYPE"] == i["FUEL_TYPE"] and \
               data["MAX_SPEED"] == i["MAX_SPEED"] and data["RENTAL_PRICE"] == i["RENTAL_PRICE"] and \
               data["MAINTENANCE_COST"] == i["MAINTENANCE_COST"]:
                data = i
                break
        else:
            data["CARTYPEID"] = self.carDetailsIdCounter
            self.allCarDetails.append(data)
            self.carDetailsIdCounter += 1
        return data


    def transform(self, src_data):
        # to collection
        data = {
            "CARTYPEID": None,
            "CARID": self.__get_carID(src_data["carId"]),
            "BODYTYPE": self.__get_carBodyType(src_data["carBodyType"]),
            "COLOR": self.__get_carColor(src_data["carColor"]),
            "FUEL_TYPE": self.__get_carFuelType(src_data["carFuelType"]),
            "MAX_SPEED": self.__get_carMaxSpeed(src_data["carMaxSpeed"]),
            "RENTAL_PRICE": self.__get_carRentalPrice(src_data["carRentalprice"]),
            "MAINTENANCE_COST": self.__get_carMaintenanceCost(src_data["carInsuranceCost"],
                src_data["carOtherCosts"])
        }

        self.__asserts(data)
        data = self.__check_for_repeaters(data)
        self.__asserts(data)

        return data


    def table_write(self, data):
        self._writer.writerow([
            data["CARTYPEID"],
            data["CARID"],
            data["BODYTYPE"],
            data["COLOR"],
            data["FUEL_TYPE"],
            data["MAX_SPEED"],
            data["RENTAL_PRICE"],
            data["MAINTENANCE_COST"]
        ])


    def table_write_all(self):
        for item in self.allCarDetails:
            self.table_write(item)
