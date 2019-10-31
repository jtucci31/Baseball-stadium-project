
import json
import csv

infile = open('weather-precip-2017.json', 'r', encoding = 'utf-8')
data = json.load(infile)
infile.close()



for record in data:
    cities = ('location', record)
    average_precip = ('value', record)
    print(cities)
