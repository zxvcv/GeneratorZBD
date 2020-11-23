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

from ...AbstractGenerator import AbstractGenerator
from .HireTableGenerator import HireTableGenerator
from .ClientTableGenerator import ClientTableGenerator
from .CarTableGenerator import CarTableGenerator
from .FuelTableGenerator import FuelTableGenerator


class GeneratorCSV(AbstractGenerator):
    def __init__(self, settingsFile):
        super().__init__(settingsFile)

        self.clientGenerator = ClientTableGenerator(self.settings, "client")
        self.hireGenerator = HireTableGenerator(self.settings, "hires")
        self.carGenerator = CarTableGenerator(self.settings, "cars")
        self.fuelGenerator = FuelTableGenerator(self.settings, "fuels")

        # helpers
        self._max_hires_for_client = self.settings["max_hires_for_client"]
        self._cars_num = self.settings["cars_num"]
        self._iterations = self.settings["iterations"]


    def generate(self):
        print("Fuel generating...")
        fuel = self.fuelGenerator.generate()
        self.fuelGenerator.table_write(fuel)

        print("Cars & Clients generating...")
        for i in tqdm(range(self._cars_num)):
            car = self.carGenerator.generate()
            self.carGenerator.table_write(car)

        print("Hires & Clients generating...")
        for i in tqdm(range(self._iterations)):
            client = self.clientGenerator.generate()

            hires_for_client = random.randrange(1, self._max_hires_for_client + 1)
            for nHire in range(hires_for_client):
                inputsHire = {
                    "clientBirthDate": client["birthDate"],
                    "clientID": client["id"],
                    "carID": random.randrange(self._cars_num)
                }
                hire = self.hireGenerator.generate(inputsHire)
                self.hireGenerator.table_write(hire)
            
            self.clientGenerator.table_write(client)
