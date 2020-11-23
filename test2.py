import time
import json
import random
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from libs.generators.CSV.GeneratorCSV import GeneratorCSV


if __name__ == "__main__":
    generatorCSV = GeneratorCSV("libs/generators/CSV/settings.json")
    
    generatorCSV.generate()

    print("Done")
