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



class GeneratorCSV:
    def __init__(self, settingsFile):
        self.settings = []
        with open(settingsFile, "r") as f:
            self.settings = json.loads(f.read())

        self.csvClientFile = open(self.settings["client_data_file"], "w", newline='')
        self.clientWriter = csv.writer(self.csvClientFile, delimiter=';')

        self.csvHireFile = open(self.settings["hire_data_file"], "w", newline='')
        self.hireWriter = csv.writer(self.csvHireFile, delimiter=";")

        self.carID = 0
        self.clientID = 0

        self.clientKeys = ["name","surname","birthDate","gender","maritialStatus",
            "numberOfChildrens","priceFactor"]
        self.clientWriter.writerow(self.clientKeys)

        self.hireKeys = ["hireStartTime","hireEndTime","carId","clientId","clientSatisfaction",
            "roadLength","repairsCost"]
        self.hireWriter.writerow(self.hireKeys)


    def __del__(self):
        self.csvClientFile.close()
        self.csvHireFile.close()


    def __str_time_prop(self, start, end, prop):
        """
            Get a time at a proportion of a range of two formatted times.

            start and end should be strings specifying times formated in the
            given format (strftime-style), giving an interval [start, end].
            prop specifies how a proportion of the interval to be taken after
            start.  The returned time will be in the specified format.
        """
        delta = end - start
        ptime = start + timedelta(seconds=prop * delta.total_seconds())

        return ptime


    def __get_file_lines(self, file_name, lines_to_read):
        found_lines = []
        with open(file_name, "r") as file:
            for position, line in enumerate(file):
                if position in lines_to_read:
                    found_lines.append(line.replace("\"", "").rstrip("\n"))
        return found_lines


    def __hire_generate(self):
        # helpers
        _max_hires_for_client = self.settings["max_hires_for_client"]
        _max_hire_length_months = self.settings["max_hire_length_months"]
        _start_hire_minus_delta_days = self.settings["start_hire_minus_delta_days"]
        _min_hire_time_hours = self.settings["min_hire_time_hours"]
        _date_format = self.settings["date_format"]

        # other items generation
        client = self.__client_generate()

        #car = self.__car_get() #TODO: poyslec nad generacja auta tak zeby to mialo sens

        #generation
        client = self.__client_generate()
        for i in range(random.randrange(1, _max_hires_for_client + 1)):
            hireStartTime = self.__str_time_prop(client["birthDate"] + relativedelta(years=18), 
                datetime.now() - timedelta(days=_start_hire_minus_delta_days), random.random())
            __helper = self.__str_time_prop(hireStartTime + relativedelta(hours=_min_hire_time_hours), 
                hireStartTime + relativedelta(months=_max_hire_length_months), random.random())
            hireEndTime = datetime.now() if __helper > datetime.now() else  __helper
            carId = 0#car["id"]
            clientId = client["id"]
            clientSatisfaction = random.randrange(0, 11)
            __helper3 = hireEndTime - hireStartTime
            roadLength = __helper3.days * float(random.randrange(0, 1000)) / 10
            __helper2 = 1 if random.randrange(0, 100) == 0 else 0
            repairsCost = __helper2 * random.randrange(0, 200) * 100
            
            

            # to collection
            data = {
                "hireStartTime": hireStartTime,
                "hireEndTime": hireEndTime,
                "carId": 0,#carID,
                "clientId": clientId,
                "clientSatisfaction": clientSatisfaction,
                "roadLength": roadLength,
                "repairsCost": repairsCost
            }

            # asserts
            assert (data["hireStartTime"] >= datetime.strptime(self.settings["birth_first_date"], _date_format)),"Hire Start Time is too small"
            assert (data["hireStartTime"] <= datetime.now() - relativedelta(days=_start_hire_minus_delta_days)), "Hire Start Time is too big"
            assert (data["hireEndTime"] >= datetime.strptime(self.settings["birth_first_date"], _date_format)), "Hire End Time is too small"
            assert (data["hireEndTime"] <= datetime.now()), "Hire End Time is too big"
            assert (data["carId"] >= 0), "CarID cant be negative"
            assert (data["clientId"] >= 0), "ClientID cant be negative"
            assert (data["clientSatisfaction"] >= 0), "Clients' satisfaction cant be negative"
            assert (data["clientSatisfaction"] <= 10), "Clients' satisfaction cant be bigger than 10"
            assert (data["roadLength"] >= 0), "road cant be negative"
            assert (data["repairsCost"] >= 0), "repairs cost cant be negative"
            assert (data["repairsCost"] <= 20000), "repairs cost cant be greater than 20000"

            # writing hire
            self.hireWriter.writerow([
                data["hireStartTime"].strftime(_date_format),
                data["hireEndTime"].strftime(_date_format),
                data["carId"],
                data["clientId"],
                data["clientSatisfaction"],
                data["roadLength"],
                data["repairsCost"]
            ])

        # writing client
        self.clientWriter.writerow([
            client["name"],
            client["surname"],
            client["birthDate"].strftime(_date_format),
            client["gender"],
            client["maritialStatus"],
            client["numberOfChildrens"],
            client["priceFactor"]
        ])


    def __client_generate(self):
        # helpers
        date_format = self.settings["date_format"]
        birth_first_date = datetime.strptime(self.settings["birth_first_date"], date_format)
        files_examples_num = self.settings["files_examples_num"]

        # data generation
        birthDate = self.__str_time_prop(birth_first_date, datetime.now() - relativedelta(years=20),
            random.random())
        gender = "male" if random.randrange(2) == 0 else "female"
        surname = self.__get_file_lines(self.settings["surnames_file"], [random.randrange(files_examples_num)])[0]
        name = ""
        if gender == "male":
            name = self.__get_file_lines(self.settings["male_names_file"], [random.randrange(files_examples_num)])[0]
        else:
            name = self.__get_file_lines(self.settings["female_names_file"], [random.randrange(files_examples_num)])[0]
        maritialStatus = "married" if random.randrange(2) == 0 else "single"
        numberOfChildrens = random.randrange(5)
        priceFactor = float(random.randrange(50, 150)) / 100

        # to collection
        data = {
            "id": self.clientID,
            "name": name,
            "surname": surname.capitalize(),
            "birthDate": birthDate,
            "gender": gender,
            "maritialStatus": maritialStatus,
            "numberOfChildrens": numberOfChildrens,
            "priceFactor": priceFactor
        }

        self.clientID += 1

        # asserts
        assert (data["name"] != ""), "Clients' name is empty"
        assert (data["surname"] != ""), "Clients' surname is empty"
        assert (data["birthDate"] > birth_first_date), "Client is too old"
        assert (data["birthDate"] < datetime.now() - relativedelta(years=20)), "Client is too young"
        assert (data["priceFactor"] < 1.51), "clients' price factor is bigger than 1,51"
        assert (data["priceFactor"] > 0.49), "clients' price factor is lower than 0,49"

        return data


    def generate(self):
        for i in tqdm(range(self.settings["clients_number"])):
            self.__hire_generate()
