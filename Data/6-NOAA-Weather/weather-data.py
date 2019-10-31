
import requests

# Grabs the URL that links to other games I'll be grabbing links to
url = 'https://www.ncdc.noaa.gov/cag/city/mapping/132-tavg.xml'
result = requests.get(url)

# Saves the URL html code into a file locally, so that I'm not hitting the website every time
outfile = open('weather-temp-2017.xml', 'w', encoding='utf-8')

print(result.text, file = outfile)
