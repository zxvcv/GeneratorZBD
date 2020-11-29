from dateutil.relativedelta import relativedelta
from libs.transformers.CSV.Transformer import Transformer as TransformerCSV
#from libs.generators.MYSQL.Generator import Generator as GeneratorMYSQL
#from libs.generators.ORACLE.Generator import Generator as GeneratorORACLE


if __name__ == "__main__":
    print("##################### CSV generation #####################")
    transformerCSV = TransformerCSV("libs/transformers/CSV/settings.json")
    transformerCSV.transform()
    print("Done")

    #print("##################### MYSQL generation ###################")
    #generatorMYSQL = GeneratorMYSQL("libs/generators/MYSQL/settings.json")
    #generatorMYSQL.generate()
    #print("Done")

    #print("##################### ORACLE generation ##################")
    #generatorORACLE = GeneratorORACLE("libs/generators/ORACLE/settings.json")
    #generatorORACLE.generate()
    #print("Done")
