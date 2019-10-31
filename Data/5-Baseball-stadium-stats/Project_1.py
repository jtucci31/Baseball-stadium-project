import requests

# Grabs the URL that links to other games I'll be grabbing links to
url = 'http://www.andrewclem.com/Baseball/Stadium_statistics.html'
result = requests.get(url)

# Saves the URL html code into a file locally, so that I'm not hitting the website every time
outfile = open('stadium_statistics.xml', 'w', encoding='utf-8')

print(result.text, file = outfile)
