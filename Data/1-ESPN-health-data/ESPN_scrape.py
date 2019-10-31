import requests

# Grabs the URL that links to other games I'll be grabbing links to
url = 'http://www.espn.com/espn/feature/story/_/id/25316231/health-inspection-reports-find-critical-violations-nfl-nhl-nba-mlb-stadiums-2018-espn-lines#!'
result = requests.get(url)


if result.status_code is 200:
    print("All good")
else: print("Uh oh")
# Saves the URL html code into a file locally, so that I'm not hitting the website every time
outfile = open('ESPN.html', 'w', encoding='utf-8')

print(result.text, file = outfile)


