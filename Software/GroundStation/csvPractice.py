import csv

#Data has all the data in a 2d array
with open('database.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
