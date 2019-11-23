
import json
import csv

# cities from ESPN data
cities_infile = open('6-ESPN_stadium_violations.csv', 'rt')
# temperature from NOAA data
weather_infile = open('weather-temp-2017.csv', 'rt')

# Writes in stadium cities
cities = []
teams = [] # This does not work yet

reader_1 = csv.DictReader(cities_infile)
for rows in reader_1:
    stadium_cities = rows['Location']
    team_name = rows['Team']
    stadium_name = rows['Stadium']

    teams.append(team_name)
    cities.append(stadium_cities)

# all_teams = ('\n'.join(teams))


precip_list = []

reader_2 = csv.DictReader(weather_infile)

for row in reader_2:

    stadium_weather = row['Location']
    if stadium_weather in cities:
        # print(type(stadium_weather))
        # location = row['Location']

        total_precip = row['Value']
        decades_average = row['1981-2010 Mean']
        anomaly = row['Anomaly (1981-2010 base period)']

        full_row = []
        # full_row.append(all_teams)
        # full_row.append(stadiums)

        full_row.append(stadium_weather)
        full_row.append(total_precip)
        full_row.append(decades_average)
        full_row.append(anomaly)

        precip_list.append(full_row)


csv_file = open('stadium_temp_list.csv', 'w', newline = '')
csvout = csv.writer(csv_file)
csvout.writerow(['Location', 'Average Temperature May-Oct 2017', '1981-2010 Average', 'Anomaly'])

csvout.writerows(precip_list)
csv_file.close()
