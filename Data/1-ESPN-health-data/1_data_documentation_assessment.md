# 1. ESPN-health-data


### Data Cleaning Assessment
This file is in a JSON format because it was taken from the HTML code of the actual ESPN website. The biggest part of the cleaning process requires it to be converted to a CSV format. Before that, I will need to gather the JSON entries that are only baseball stadiums, because this file has every major sport stadium in the United States listed. 

1. Hand code to gather only the MLB stadiums from the JSON file. There is a key entitled "sports" that I can use to filter out only the "MLB" records.
2. Write these MLB stadiums to a CSV with the keys from the JSON file as the columns.
3. I will also only take out the data I need from the JSON and write it to the CSV. That data will be taken from the following keys in the JSON file: id, name, city, state_abbrev, state, critical, capactiy, opened, venue, area, inspections, and teams. 

This should take me between 3-4 hours to go through the JSON file and make sure my coding grabs every MLB stadium and data from each stadium that I need, interpret and grab the violations in a meaningful way, and then write it to a CSV from the .py file.


### Authorship, Attribution, Provenance
Research was done by Sandra Fish, and comparison data was done by Hazel Analytics. The article was then written by Paula Lavigne and Sandra Fish and published on ESPN.com on December 13, 2018. Simon Baumgart, a producer at ESPN, also contributed to the report.



### Semantic Contents
This file contains health code violation data for MLB stadiums from the 2017 season. It was compiled by ESPN and gives a raw number of violations per stadium in the given year. 

I will be looking at the violations, venue, critical, and area columns to gauge a score of some kind for each stadiums health code violations and general food safety rating. I will compare the total inspections and number of critical violations found at each stadium to get a percentage of failure rate.

The HTML page was web scraped sometime in September 2019 by Joe Tucci. The JSON data was taken directly out of the HTML file, copied into a separate file, and cleaned with the help of Elizabeth Wickes on October 20, 2019.


### Collection Process
ESPN "reviewed and collected more than 16,000 food-safety inspection reports from health departments that monitor the 111 professional football, baseball, basketball and hockey facilities across North America." This is taken from the detailed report where I got my data from [here](http://www.espn.com/espn/feature/story/_/id/25316231/health-inspection-reports-find-critical-violations-nfl-nhl-nba-mlb-stadiums-2018-espn-lines#!). They also "calculated the average number of high-level violations per inspection at each venue, and compared that to the average for restaurants and other foot outlets in the surrounding area, for the 82 venues for which [they] had community data provided by Hazel Analytics.

I gathered the data from the report by first web scraping using Python's requests module. From there I was able to use requests.get to get the HTML contents from the web page, and then from there on I accessed everything from my HTML file I saved locally. To extract the data from the JSON file I used the json, csv, and pathlib modules within PyCharm.

### Data Structure
This data is currently stored as a JSON file, but for the remainder of the data structure description I will refer to it in the future CSV format. This CSV file will have a total of 30 rows because there are 30 total baseball stadiums in the MLB. Each row will contain the following columns (in order from left to right):

* Stadium Name
* Team Name
* City and State - The location of the stadium within the United States (only one stadium is in Toronto, Canada and will be listed under Toronto, Ontario.)
* Critical - This percentage is the average number of violations found at each location visited within the stadium.
* Venue - This is the number of high-level violations per inspection.
* Area - This is the number of high-level violations per inspection in the area/city of the stadium.
* Inspections - This gives both the total number of inspections done and critical violations found.

There should be no missing values since every stadium had violations and a critical score associated with their average number of violations aggregate average. This data will include categorical data like locations, cities, and team names, and also include integers and percentages in numbers.
