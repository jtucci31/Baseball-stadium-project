import json
import csv

# cities from ESPN data
cities_infile = open('6-ESPN_stadium_violations.csv', 'rt')
# precipitation from NOAA data
weather_infile = open('weather-precip-2017.csv', 'rt')

# Writes in stadium cities
cities = []

# Reads in the ESPN CSV data to gather a list of cities
reader_1 = csv.DictReader(cities_infile)
for rows in reader_1:
    stadium_cities = rows['Location']

    cities.append(stadium_cities)


precip_list = []

# Reads in the precipitation data
reader_2 = csv.DictReader(weather_infile)

for row in reader_2:
    stadium_weather = row['Location']

    # Checks for cities where a baseball stadium is based on the previous variable from the ESPN CSV list of cities
    if stadium_weather in cities:

        # Grabs data from the precipitation CSV
        total_precip = row['Value']
        decades_average = row['1981-2010 Mean']
        anomaly = row['Anomaly (1981-2010 base period)']

        full_row = []

        # Appends the appropriate precipitation data from the baseball cities
        full_row.append(stadium_weather)
        full_row.append(total_precip)
        full_row.append(decades_average)
        full_row.append(anomaly)

        precip_list.append(full_row)

# Writes the appended precipitation data to a CSV
csv_file = open('stadium_precip_list.csv', 'w', newline = '')
csvout = csv.writer(csv_file)
csvout.writerow(['Location', 'Total Precipitation May-Oct 2017', '1981-2010 Average', 'Anomaly'])

csvout.writerows(precip_list)
csv_file.close()
