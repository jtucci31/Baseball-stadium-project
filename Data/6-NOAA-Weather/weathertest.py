
import json
import csv


infile = open('weather-precip-2017.json', 'r', encoding = 'utf-8')
data = json.load(infile)
infile.close()

print(type(data))


# print(type(data))
# print(len(data))
#
# full_data = data['data']
#
# for record in full_data:
#     print(record.keys())

