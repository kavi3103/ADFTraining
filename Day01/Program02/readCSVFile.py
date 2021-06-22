'''
  2.	Program to read a CSV (CSV with n number of columns) and store it in DICT of list.
'''

import csv

#inialise empty dictonary to store csv file rows
dict = dict()
count = 0

#opens csv file Iris.csv in read mode
try:
    with open("Iris.csv","r") as file:
        reader = csv.reader(file)  #reads csv file rows
        for row in reader:
            dict[count] = row  #store rows in dictonary
            count += 1

    print(dict)
except (FileNotFoundError, IOError):
    print("Wrong file or file path")
