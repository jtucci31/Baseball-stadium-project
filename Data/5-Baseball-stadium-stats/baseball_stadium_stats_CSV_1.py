import csv

stadium_stats = open("stadium_statistics.CSV", "rt")

current_stadiums = open('Voice-of-Fan-report-2017-averages.csv', 'rt')


def clean_stadiums(record):
    if current_stadium_name in record:
        result = record
        return result


# Grabs list of current MLB stadiums for 2017 list
reader_1 = csv.DictReader(current_stadiums)
for row in reader_1:
    current_stadium_name = row['Stadium']
    stadium_row = []
    stadium_row = stadium_row + current_stadium_name
    print(stadium_row)





    # reader_2 = csv.DictReader(stadium_stats)
    # for row in reader_2:
    #     stadium_name = row['Stadium']
    #     print(clean_stadiums(stadium_name))

#
# all_scores = []
# reader_2 = csv.DictReader(stadium_stats)
# for row in reader_2:
#     stadium_name = row['Stadium']
#     print(clean_stadiums(stadium_name))

