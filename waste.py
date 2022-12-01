import csv
import random as rd
import decimal

# opening the CSV file
with open('foodCsv.csv', mode ='r')as file:
# reading the CSV file
    csvFile = csv.reader(file)

# displaying the contents of the CSV file
    for lines in csvFile:
        value=lines[1]
        amount=lines[2]
        if(int(value)>=250 and int(value)<=270):
            temp_waste = float(decimal.Decimal(rd.randrange(10,30))/10)
        else:
            temp_waste = float(decimal.Decimal(rd.randrange(30,40))/10)
        print(temp_waste)