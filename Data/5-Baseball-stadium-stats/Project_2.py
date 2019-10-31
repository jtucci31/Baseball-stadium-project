
from lxml import html
import csv

# Calls on the html file locally
infile = open('stadium_statistics.html', 'rb')
site = infile.read()
infile.close()

tree = html.fromstring(site)

# This is the main node for each stadium in the list that I'll loop through
stadium_row = tree.xpath('//tr')

# This loop grabs elements and accumulates them into rows first and then all rows together with .append
all_stadiums = []
for stadium in stadium_row[3:-3]:
    row = []
    stadium_name = (stadium.xpath('td[1]/a/text()'))
    team = (stadium.xpath('td[2]/text()'))
    capacity = (stadium.xpath('td[4]/text()'))
    fair = (stadium.xpath('td[10]/text()'))
    foul = (stadium.xpath('td[11]/text()'))
    row.append(stadium_name)
    row.append(team)
    row.append(capacity)
    row.append(fair)
    row.append(foul)
    all_stadiums.append(row)

print(all_stadiums)

csv_file = open('stadium_statistics.csv', 'w', newline = '')
csvout = csv.writer(csv_file)
csvout.writerow(['Stadium', 'Team','Seating Capacity', 'Fair Territory (1,000 sq. ft.)', 'Foul Territory (1,000 sq. ft.)'])


csvout.writerows(all_stadiums)
csv_file.close()
