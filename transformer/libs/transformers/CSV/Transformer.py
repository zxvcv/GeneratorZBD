import csv
import sys
import json
import time
import random
import string
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from ...AbstractTransformer import AbstractTransformer

from .RentalTableTransformer import RentalTableTransformer as RentalTransformer
from .ClientTableTransformer import ClientTableTransformer as ClientTransformer
from .CarTableTransformer import CarTableTransformer as CarTransformer
from .CarDetailsTableTransformer import CarDetailsTableTransformer as CarDetailsTransformer


class Transformer(AbstractTransformer):
    def __init__(self, settingsFile):
        super().__init__(settingsFile)

        absFilePath = self.settings["absolute_src_tables_path"]

        # for rentals
        filePath = absFilePath + self.settings["src_tables"]["hires"]["data_file"]
        self.rentalFileSrc = open(filePath, "r", newline='')

        # for clients
        filePath = absFilePath + self.settings["src_tables"]["client"]["data_file"]
        self.clientFileSrc = open(filePath, "r", newline='')

        # for cars
        filePath = absFilePath + self.settings["src_tables"]["cars"]["data_file"]
        self.carFileSrc = open(filePath, "r", newline='')

        filePath = absFilePath + self.settings["src_tables"]["fuels"]["data_file"]
        self.fuelsFileSrc = open(filePath, "r", newline='')

        # Transformers objects
        self.rentalTransformer = RentalTransformer(self.settings, "rental_facts")
        self.clientTransformer = ClientTransformer(self.settings, "client_dimension")
        self.carTransformer = CarTransformer(self.settings, "car_dimension")
        self.carDetailsTransformer = CarDetailsTransformer(self.settings, "car_details")

        # helpers


    def __del__(self):
        self.clientFileSrc.close()

    def transform(self):
        clients = self.clientFileSrc.readlines()[1:]
        cars = self.carFileSrc.readlines()[1:]
        fuels = self.fuelsFileSrc.readlines()[1:]

        # for every rent
        for rent in self.clientFileSrc:
            spltRent = rent.split(';')

            clientID = spltRent[3] #clientId
            carID = spltRent[2] #carId

            client = clients[clientID].split(';')
            car = cars[carID].split(';')

            # clients
            clientData = {
                "client_birthDate": client[3], #birthDate
                "client_gender": client[4], #gender
                "client_married": client[5], #maritialStatus
                "client_children": client[6], #numberOfChildrens
            }
            transformedClient = self.clientTransformer.transform(clientData)

            # cars
            carData = {
                "carBrand": car[2], #brand
                "carModel": car[1], #model
            }
            transformedCar = self.carTransformer.transform(carData)

            # car details
            carDetailsData = {
                "carId": transformedCar["CARID"],
                "carBodyType": car[3], #bodyType
                "carColor": car[4], #color
                "carFuelType": fuels[car[5]].split(';')[1], #fuelName
                "carMaxSpeed": car[6], #maxSpeed
                "carRentalprice": car[7], #rentalPrice
                "carInsuranceCost": car[9], #insuranceCost
                "carOthercosts": car[10], #otherCosts
            }
            transformedCarDetails = self.carDetailsTransformer.transform(carDetailsData)

            # hires
            dataHire = {
                "clientID": transformedClient["CLIENTID"],
                "carID": transformedCar["CARID"],
                "hireStartTime": spltRent[0], #hireStartTime
                "hireEndTime": spltRent[1], #hireEndTime
                "staisfaction": spltRent[4], #clientSatisfaction
                "repairsCost": spltRent[6], #repairsCost
                "carDailyHireCost": car[11], #dailyHireCost
                "clientPriceFactor": client[7], #priceFactor
            }
            transformedHire = self.hireTransformer.transform(dataHire)
            self.hireTransformer.table_write(transformedHire)
        
        self.carDetailsTransformer.table_write_all()
        self.carTransformer.table_write_all()
        self.clientTransformer.table_write_all()
