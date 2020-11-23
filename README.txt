to change number of generated items:
 -go to .\libs\generators\<generatorType>\settings.json
 -"iterations" filed determines number of customers to generate (~rents = 5*iterations)
 -"cars_num" filed determines number of cars to generate

to change date formating:
 -go to .\libs\generators\<generatorType>\settings.json
 -"birth_first_date" is string passed to datetime.strptime method (https://docs.python.org/3/library/datetime.html)

DO NOT change fields:
 -"tables"
 -"female_names_file"
 -"male_names_file"
 -"surnames_file"
 -"files_examples_num"
 -"cars_file"
 -"cars_examples_num"

ALL GENERATED FILES WILL BE PLACED INTO: .\<generatorType>_generated\

TO GENERATE ALL FILES TYPE: "python generate.py" IN CMD