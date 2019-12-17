
import json
import csv
import pathlib

# Imports the JSON file
data = json.loads(pathlib.Path('stadiums_espn.json').read_text())

# Function for the one stadium that has both a baseball and football team
def clean_team(record):
    if len(record) > 1:
        result = record[1]
    else:
        result = record[0]
    return result

# Finds the necessary data from each JSON entry and writes it to a defined variable
all_stadiums = []
for record in data['items']:
    if 'MLB' in record['sports']:
        stadium_name = record['name']
        mlb_teams = clean_team(record['teams'])
        city = record['city']
        state_abbrev = record['state_abbrev']
        state = record['state']
        capacity = record['capacity']
        venue_score = record['venue']
        area_score = record['area']
        total_inspections = record['inspections']['total']
        critical_inspections = record['inspections']['critical']
        critical_score = record['critical']


        # Accumulates all of the variables so that it can write a CSV file
        row = []
        row.append(mlb_teams)
        row.append(stadium_name)
        row.append(capacity)
        row.append(city + ", " + state)
        row.append(state_abbrev)
        row.append(venue_score)
        row.append(area_score)
        row.append(total_inspections)
        row.append(critical_inspections)
        row.append(critical_score)
        all_stadiums.append(row)

# Writes the accumulated new variables from rows into a CSV
csv_file = open('ESPN_stadium_violations.csv', 'w', newline = '')
csvout = csv.writer(csv_file)
csvout.writerow(['Team', 'Stadium', 'Seating Capacity', 'Location', 'State Abbreviation',
                 'Venue Score', 'Area Score', 'Total Inspections',
                 'Critical Inspections Found', 'Critical Score in percentage'])

csvout.writerows(all_stadiums)
csv_file.close()
