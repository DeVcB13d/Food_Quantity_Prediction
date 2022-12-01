import csv
import random as rd

# opening the CSV file
with open('foodCsv.csv', mode ='r')as file:
# reading the CSV file
    csvFile = csv.reader(file)

# displaying the contents of the CSV file
    for lines in csvFile:
        value=lines[1]
        amount=lines[2]
        print(value)
        if(value>=250 and value<270):
            temp=rd.randrange((amount/10),(amount/5))
