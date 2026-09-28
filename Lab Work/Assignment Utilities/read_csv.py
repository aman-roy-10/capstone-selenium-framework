import csv

with open("testdata.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)