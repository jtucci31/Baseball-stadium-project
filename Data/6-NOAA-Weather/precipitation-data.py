
import json
import csv

# cities
cities_infile = open('6-ESPN_stadium_violations.csv', 'rt')
# weather
weather_infile = open('weather-precip-2017.csv', 'rt')

# Writes in stadium cities
cities = []
teams = []

reader_1 = csv.DictReader(cities_infile)
for rows in reader_1:
    stadium_cities = rows['City, State']
    team_name = rows['MLB Team']
    stadium_name = rows['Stadium Name']

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





csv_file = open('stadium_precip_list.csv', 'w', newline = '')
csvout = csv.writer(csv_file)
csvout.writerow(['Stadiums', 'Location', 'Total Precipitation 2017', '1981-2010 Average', 'Anomaly'])

csvout.writerows(precip_list)
csv_file.close()
