from libs.GeneratorCSV import GeneratorCSV
from datetime import datetime
from datetime import timedelta
import random
import time
from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    generatorCSV = GeneratorCSV("settings.json")
    generatorCSV.generate()
    
    #for i in range(50):
    #    print(float(random.randrange(50, 150)) / 100)

    print("Done")
