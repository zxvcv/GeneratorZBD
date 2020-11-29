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


class FuelTableGenerator(AbstractTableGenerator):
    def __init__(self, settings, tableName):
        super().__init__(settings, tableName)


    def generate(self):
        fuel_types = self.settings["fuel_types"]
        
        # to collection
        data = []
        for i in fuel_types:
            data.append(i.values())
        return data


    def table_write(self, data):
        self._writer.writerows(data)

