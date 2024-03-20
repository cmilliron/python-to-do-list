#Working with csv

import csv

with open('weather.csv', "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(f"The temperature in {row[0]} is {row[1]}")