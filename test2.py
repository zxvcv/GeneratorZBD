from libs.GeneratorCSV import GeneratorCSV
from datetime import datetime
from datetime import timedelta
import random
import time
import json
from dateutil.relativedelta import relativedelta

from lib.generators.CSV.ClientTableGenerator import ClientTableGenerator

if __name__ == "__main__":
    settings = []
    with open("settings.json", "r") as f:
        settings = json.loads(f.read())

    generatorCSV = ClientTableGenerator(settings, "client")
    
    
    #for i in range(50):
    #    print(float(random.randrange(50, 150)) / 100)

    print("Done")
