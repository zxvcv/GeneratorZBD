import csv
import json
import time
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta



class GeneratorCSV:
    def __init__(self, settingsFile):
        self.csvfile = open("data.csv", "w")
        self.writer = csv.writer(self.csvfile, delimiter=';')
        
        self.settings = []
        with open(settingsFile, "r") as f:
            self.settings = json.loads(f.read())


    def __del__(self):
        self.csvfile.close()


    def __str_time_prop(self, start, end, format, prop):
        """
            Get a time at a proportion of a range of two formatted times.

            start and end should be strings specifying times formated in the
            given format (strftime-style), giving an interval [start, end].
            prop specifies how a proportion of the interval to be taken after
            start.  The returned time will be in the specified format.
        """
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))

        ptime = stime + prop * (etime - stime)

        return time.strftime(format, time.localtime(ptime))


    def __get_file_lines(self, file_name, lines_to_read):
        found_lines = []
        with open(file_name, "r") as file:
            for position, line in enumerate(file):
                if position in lines_to_read:
                    found_lines.append(line)
        return found_lines


    def __hire_generate(self):
        # helpers
        max_hires_for_client = self.settings["max_hires_for_client"]
        max_hire_length_months = self.settings["max_hire_length_months"]
        start_hire_minus_delta_days = self.settings["start_hire_minus_delta_days"]
        date_format = self.settings["date_format"]
        datetime_helper1 = datetime.strptime(client["birthDate"], date_format)

        #generation
        client = self.__client_generate()
        for i in range(random.randrange(1, max_hires_for_client + 1)):
            hireStartTime = self.__str_time_prop(datetime_helper1 + timedelta(years=18)



            hireStartTime = self.__str_time_prop(self.settings["birth_first_date"],
                date_helper.strftime(date_format), date_format, random.random())
            hireEndTime
            carId
            clientId
            clientSatisfaction
            roadLength
            repairsCost
        #datetime.now() + timedelta(days=1)

        self.__str_time_prop("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", '%m/%d/%Y %I:%M %p', random.random())
        self.writer.writerow(['Spam'] * 5 + ['Baked Beans'])
        self.writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


    def __client_generate(self):
        # helpers
        date_format = self.settings["date_format"]
        files_examples = self.settings["files_examples"]
        date_helper = datetime.now() - timedelta(years=18)

        # data generation
        birthDate = self.__str_time_prop(self.settings["birth_first_date"],
                date_helper.strftime(date_format), date_format, random.random())
        gender = "male" if random.randrange(2) == 0 else "female"
        surname = self.__get_file_lines(self.settings["surnames_file"], random.randrange(files_examples))
        name = ""
        if gender == "male":
            name = self.__get_file_lines(self.settings["male_names_file"], random.randrange(files_examples))
        else:
            name = self.__get_file_lines(self.settings["female_names_file"], random.randrange(files_examples))
        maritialStatus = "married" if random.randrange(2) == 0 else "single"
        numberOfChildrens = random.randrange(5)
        priceFactor = float(random.randrange(50, 150)) / 100

        # to collection
        data = {
            "name": name,
            "surname": surname,
            "birthDate": birthDate,
            "gender": gender,
            "maritialStatus": maritialStatus,
            "numberOfChildrens": numberOfChildrens,
            "priceFactor": priceFactor
        }
        return data


    def __part2(self):
        normalVar = pd.DataFrame(np.random.normal(0,10,70))
        normalVar.columns = ['value']
        normalVar.head()
        print(normalVar.shape)
        print(normalVar)


    def generate(self):
        #self.__hire_generate()
        self.__part2()
