# 3. Baseball-reference-team-data


### Data Cleaning Assessment
This file is currently in a CSV file format with seven columns. My initial process of gathering this data and downloading it from Baseball-reference.com inherently had me curating the pieces of data that I was looking for. The website let me do an initial search for attendance data, and that gave me too many data points within the larger set that I did not want. The site interface allowed me to choose what I did and did not want.

Small and minor hand edits were made to the file to describe abbreviations like BPF and PPF. The only thing that will require some cleaning or editing will be adding in either the full team name or the stadium attached to the team, because right now the team name is just listed as their three character abbreviation. When I want to mash datasets together, that will make identifying data easier. 

### Authorship, Attribution, Provenance
This source was gathered from data listed on the Baseball-reference.com website. There is no listed author because this entire site acts as an aggregate collector of baseball data and statistics. Data developers listed on the website include Jay Hutchinson, Jaclyn Mahoney, Sean Forman, and Mike Lynch. 

### Semantic Contents
This CSV is a list of team statistics from the 2017 season that lists their attendance, seating capactiy, and things like payroll and average playtime. 

The main things that will be used from this dataset are attendance numbers and seating capacity for each stadium. Other data points like average game time, payroll, and batter/pitcher park factor may or may not be used in the final assessment.

I curated the data and downloaded the CSV in early September 2019. 

### Collection Process
From their website they state, "Much of the play-by-play, game results, and transaction information both shown and used to create certain data sets was obtained free of charge from and is copyrighted by [RetroSheet.](https://www.retrosheet.org/)"

The website allows for user curation on the column level, so I was able to pick and choose the pieces of data that I wanted. Then once I got all the data, the website allows you to download a CSV. This CSV is then not formatted correctly into proper rows and columns, so I needed to use the data formatting tool within Excel to get it formatted correctly. 

### Data Structure
This CSV file has 30 total rows (technically 32 with the top row being the identifiers). It was taken directly from Baseball-reference.com and organized alphabetically according to each team's shorthand abbreviation. Each column contains the following:

* Team name
* Attendance - This is a total sum number based on 81 home games from each team. This number will be used against a seating capacity number for each stadium from other sources to find the expected attendance vs total attendance found. 
* Attendance per game - This is an average attendance number per game. The total attendance number above is divided by 81. This stat comes from the website.
* BPF (Batting Park Factor) - The neutral number is 100, where numbers greater than 100 means the park favors batters and less than 100 favors pitchers. 
* PPF (Pitching Park Factor) - The neutral number is 100, where numbers greater than 100 means the park favors batters and less than 100 favors pitchers.
* Estimated Payroll - This is a lump sum total in American dollars of the players' salaries.
* Time - This is the average playtime of a game for each home game.

This dataset has no missing values, and largely contains integers based on sums and division. It also contains dollar values in a sum value and a time average in hours:minutes format. 