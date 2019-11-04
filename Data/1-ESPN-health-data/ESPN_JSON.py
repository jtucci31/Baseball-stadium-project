
import json
import csv
import pathlib


# infile = open('stadiums_espn.json', 'r', encoding = 'utf-8')
# data = json.loads(infile)
# infile.close()


data = json.loads(pathlib.Path('stadiums_espn.json').read_text())


print(type(data))

for record in data:
    print(record)


# print(len(data['items']))
#
# print(data['items'])

names = [d['name'] for d in data['items']]
city = [d['city']for d in data['items']]
state = [d['state_abbrev'] for d in data['items']]
violations = [d['inspections'] for d in data['items']]
violations_specific = [d['inspections'] for d in data['items']]
sports = [d['sports'] for d in data['items']]
critical_score = [d['critical'] for d in data['items']]
teams = [d['teams'] for d in data['items']]

print(teams)


for record in data['items']:
    if 'MLB' in record['sports']:
        print(record['name'] + "/", record['city'], record['inspections'])



