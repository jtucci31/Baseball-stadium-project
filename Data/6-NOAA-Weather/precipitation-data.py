
import json
import csv

# cities
cities_infile = open('6-ESPN_stadium_violations.csv', 'rt')

# weather
weather_infile = open('weather-precip-2017.csv', 'rt')

# Writes in stadium cities
cities = []
reader_1 = csv.DictReader(cities_infile)
for rows in reader_1:
    stadium_cities = rows['City, State']
    cities.append(stadium_cities)

print(type(cities))

# Runs stadium cities through the CSV to find only the rows needed
reader_2 = csv.DictReader(weather_infile)
for row in reader_2:
    # print(row['Location'])
    stadium_weather = row['Location']
    if stadium_weather in cities:
        print(stadium_weather)
        # total_precip = row['Value']
        # print(total_precip)
