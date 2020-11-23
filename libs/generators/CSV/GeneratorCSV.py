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


class GeneratorCSV(AbstractGenerator):
    def __init__(self, settingsFile):
        super().__init__(settingsFile)

        self.clientGenerator = ClientTableGenerator(self.settings, "client")
        self.hireGenerator = HireTableGenerator(self.settings, "hires")

        # helpers
        self._max_hires_for_client = self.settings["max_hires_for_client"]


    def generate(self):
        for i in tqdm(range(self.settings["iterations"])):
            client = self.clientGenerator.generate()

            hires_for_client = random.randrange(1, self._max_hires_for_client + 1)
            for nHire in range(hires_for_client):
                inputsHire = {
                    "clientBirthDate": client["birthDate"],
                    "clientID": client["id"],
                    "carID": 0
                }
                hire = self.hireGenerator.generate(inputsHire)
                self.hireGenerator.table_write(hire)
            
            self.clientGenerator.table_write(client)
