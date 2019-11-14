import csv

stadium_stats = open("stadium_statistics.CSV", "rt")

current_stadiums = open('Voice-of-Fan-report-2017-averages.csv', 'rt')

#
# def clean_stadiums(record):
#     if stadium_list in record:
#         result = record
#         return result


# Grabs list of current MLB stadiums for 2017 list
stadium_list = []
reader_1 = csv.DictReader(current_stadiums)
for rows in reader_1:
    current_stadium_name = rows['Stadium']
    stadium_list.append(current_stadium_name)

print(type(stadium_list))


reader_2 = csv.DictReader(stadium_stats)
for row in reader_2:
    stadium_name_2 = row['Stadium']
    if stadium_name_2 in stadium_list:
        team_name = row['Team']
        print(team_name)

#
# all_scores = []
# reader_2 = csv.DictReader(stadium_stats)
# for row in reader_2:
#     stadium_name = row['Stadium']
#     print(clean_stadiums(stadium_name))

