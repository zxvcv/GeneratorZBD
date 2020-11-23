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


class Generator(AbstractGenerator):
    def __init__(self, settingsFile):
        super().__init__(settingsFile)

        self.customerGenerator = CustomerTableGenerator(self.settings, "customer")
        self.rentalGenerator = RentalTableGenerator(self.settings, "rental")

        # helpers
        self._max_rentals_for_customer = self.settings["max_rentals_for_customer"]
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
            
            self.customerGenerator.table_write(customer)
