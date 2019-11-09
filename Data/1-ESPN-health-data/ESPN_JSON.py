
import json
import csv
import pathlib


# infile = open('stadiums_espn.json', 'r', encoding = 'utf-8')
# data = json.loads(infile)
# infile.close()


data = json.loads(pathlib.Path('stadiums_espn.json').read_text())


# print(type(data))
#
# for record in data:
#     print(record)


# print(len(data['items']))
#
# print(data['items'])
#
# name = [d['name'] for d in data['items']]
# city = [d['city']for d in data['items']]
# state = [d['state_abbrev'] for d in data['items']]
# violations = [d['inspections'] for d in data['items']]
# violations_specific = [d['inspections'] for d in data['items']]
# sports = [d['sports'] for d in data['items']]
# critical_score = [d['critical'] for d in data['items']]
# teams = [d['teams'] for d in data['items']]


# for record in data['items']:
#     if 'MLB' in record['sports']:
#         print(record['name'] + " /", record['city'], record['inspections'], record['teams'])

def clean_team(record):
    if len(record) > 1:
        result = record[1]
    else:
        result = record[0]
    return result

# for record in data['items']:
#     mlb_teams = clean_team(record['teams'])
#     print(mlb_teams)

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
        violations = record['violations']

        row = []
        row.append(mlb_teams)
        row.append(stadium_name)
        row.append(capacity)
        row.append(city)
        row.append(state_abbrev)
        row.append(state)
        row.append(venue_score)
        row.append(area_score)
        row.append(total_inspections)
        row.append(critical_inspections)
        row.append(critical_score)
        row.append(violations)
        all_stadiums.append(row)


csv_file = open('ESPN_stadium_violations.csv', 'w', newline = '')
csvout = csv.writer(csv_file)
csvout.writerow(['MLB Team', 'Stadium Name', 'Seating Capacity', 'City', 'State Abbreviation',
                 'State', 'Venue Score', 'Area Score', 'Total Inspections',
                 'Critical Inspections Found', 'Critical Score in percentage', 'Violations'])

csvout.writerows(all_stadiums)
csv_file.close()





