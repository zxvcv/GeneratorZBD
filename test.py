#from libs.GeneratorCSV import GeneratorCSV
from datetime import datetime
from datetime import timedelta
import random
from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    #generatorCSV = GeneratorCSV()
    
    #generatorCSV.generate()
    datetime_helper1 = datetime.strptime("1/1/2008 1:30 PM", "%m/%d/%Y %I:%M %p")
    datetime_helper1 = datetime_helper1 + relativedelta(years=18)
    print(datetime_helper1.strftime("%m/%d/%Y %I:%M %p"))
    #POPRAWIC TO W KODZIE!!!! (zamienic dodawanie czasu na relativetime)

    print("Done")
