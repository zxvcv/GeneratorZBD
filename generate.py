import time
import json
import random
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from libs.generators.CSV.Generator import Generator as GeneratorCSV
from libs.generators.MYSQL.Generator import Generator as GeneratorMYSQL
from libs.generators.ORACLE.Generator import Generator as GeneratorORACLE


if __name__ == "__main__":
    print("##################### CSV generation #####################")
    generatorCSV = GeneratorCSV("libs/generators/CSV/settings.json")
    generatorCSV.generate()
    print("Done")

    print("##################### MYSQL generation ###################")
    generatorMYSQL = GeneratorMYSQL("libs/generators/MYSQL/settings.json")
    generatorMYSQL.generate()
    print("Done")

    print("##################### ORACLE generation ##################")
    generatorORACLE = GeneratorORACLE("libs/generators/ORACLE/settings.json")
    generatorORACLE.generate()
    print("Done")
