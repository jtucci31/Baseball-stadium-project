import csv

infile = open("Voice_of_Fan_Report_2017.CSV", "rt")

# Reads in the CSV and calculates the average scores instead of the sum
all_scores = []
reader = csv.DictReader(infile)
for row in reader:
    stadium_name = row['Stadium']
    facility_score = float(row['Facility'])
    family_score = float(row['Family'])
    fan_score = float(row['Fan Experience'])
    food_score = float(row['Food and Drink'])
    average_score = ((facility_score + family_score + fan_score + food_score) / 4)

    # Writes new rows with new average score
    row = []
    row.append(stadium_name)
    row.append(facility_score)
    row.append(family_score)
    row.append(fan_score)
    row.append(food_score)
    row.append(average_score)
    all_scores.append(row)


# Creates new CSV with the new average score
csv_file = open('Voice-of-Fan-Report-2017-averages.csv', 'w', newline = '')
csvout = csv.writer(csv_file)
csvout.writerow(['Stadium', 'Facility', 'Family', 'Fan Experience', 'Food and Drink', 'Average Score'])

csvout.writerows(all_scores)
csv_file.close()



