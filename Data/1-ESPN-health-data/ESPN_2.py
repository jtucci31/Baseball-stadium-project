
import re
from lxml import html
import csv
import json

# Calls on the html file locally
infile = open('ESPN.html', 'rb')
site = infile.read()
infile.close()

tree = html.fromstring(site)

stadiums = tree.xpath('//div[@class="espn-template"]/text()')

print((stadiums))


#################################################

# This is the main node for each stadium in the list that I'll loop through
# stadium_row = tree.xpath('div[@class="espn-template"]')



# This loop grabs elements and accumulates them into rows first and then all rows together with .append
# all_stadiums = []
# for stadium in stadium_row:
#     row = []
#     stadium_name = (stadium.xpath('/div[2]/text()'))
#     print(stadium_name)



