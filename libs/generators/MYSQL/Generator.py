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
from .RentalTableGenerator import RentalTableGenerator
from .CustomerTableGenerator import CustomerTableGenerator
from .CustomerRentalTableGenerator import CustomerRentalTableGenerator
from .CarTableGenerator import CarTableGenerator
from .CarRentalTableGenerator import CarRentalTableGenerator
from .CostTableGenerator import CostTableGenerator
from .CarCostTableGenerator import CarCostTableGenerator


class Generator(AbstractGenerator):
    def __init__(self, settingsFile):
        super().__init__(settingsFile)

        self.customerGenerator = CustomerTableGenerator(self.settings, "customer")
        self.rentalGenerator = RentalTableGenerator(self.settings, "rental")
        self.customerRentalGenerator = CustomerRentalTableGenerator(self.settings, "customer_rental")
        self.carGenerator = CarTableGenerator(self.settings, "cars")
        self.carRentalGenerator = CarRentalTableGenerator(self.settings, "car_rental")
        self.costGenerator = CostTableGenerator(self.settings, "costs")
        self.carCostGenerator = CarCostTableGenerator(self.settings, "car_cost")

        # helpers
        self._max_rentals_for_customer = self.settings["max_rentals_for_customer"]
        self._cars_num = self.settings["cars_num"]
        self._iterations = self.settings["iterations"]


    def generate(self):
        print("Rentals & Customers generating...")
        for i in tqdm(range(self._iterations)):
            customer = self.customerGenerator.generate()

            rentals_for_client = random.randrange(1, self._max_rentals_for_customer + 1)
            for nRental in range(rentals_for_client):
                inputsRental = {
                    "customerBirthDate": customer["birthDate"]
                }
                rental = self.rentalGenerator.generate(inputsRental)
                self.rentalGenerator.table_write(rental)

                inputsCustomerRental = {
                    "customer_uuid": customer["uuid"],
                    "rental_uuid": rental["uuid"],
                }
                customerrental = self.customerRentalGenerator.generate(inputsCustomerRental)
                self.customerRentalGenerator.table_write(customerrental)

                inputsCarRental = {
                    "car_uuid": random.randrange(self._cars_num),
                    "rental_uuid": rental["uuid"],
                }
                carrental = self.carRentalGenerator.generate(inputsCarRental)
                self.carRentalGenerator.table_write(carrental)
            
            self.customerGenerator.table_write(customer)
        
        print("Cars & Costs generating...")
        for i in tqdm(range(self._cars_num)):
            car = self.carGenerator.generate()
            self.carGenerator.table_write(car)

            cost = self.costGenerator.generate()
            self.costGenerator.table_write(cost)

            inputsCarCost= {
                "car_uuid": car["uuid"],
                "cost_uuid": cost["uuid"],
            }
            carcost = self.carCostGenerator.generate(inputsCarCost)
            self.carCostGenerator.table_write(carcost)
