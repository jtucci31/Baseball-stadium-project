# 5. Baseball-stadium-stats


### Data Cleaning Assessment
This file is a CSV that was taken from HTML code that was web scraped. The cleaning process will involve getting the data out of brackets and quotations and making it look better. On top of that, there are over 70 entries, because the list compiled every baseball stadium (or at least a large number of them) throughout history. So, I have a lot of unnecessary rows and data that I will need to remove. 

1. Gather a list of the current 30 MLB stadiums into a separate CSV or .txt file from a previous source.
2. Use source from step 1 to cross reference and grab only the stadiums from said list. This will allow me to delete the other stadiums. 
3. With 30 current MLB stadiums, clean data across the five columns. Making sure there are no missing values anywhere.
4. Since some stadiums have the same names (old Yankee Stadium and new Yankee Stadium), I will need to hand edit the dataset to remove the incorrect stadium that I need.
5. Some stadiums have changed names since this list was updated, which may make things a little difficult. Hand edits will be made where necessary to compensate for stadium name changes like U.S. Cellular Field, now called Guaranteed Rate Field, for example.

This should take me between 5-6 hours given how much data is in the original set, and how I will need to go to another dataset to gather and create a new, small set, so that I can get the data I need from this dataset. 

### Authorship, Attribution, Provenance
This data comes from andrewclem.com whose author, according to their Terms of Service page, is Andrew G. Clem. The Stadium Statistics page that I used was last updated on August 17, 2018 that's listed on the top of the webpage. The Terms of Service state that the user may use the content of the website so long as there is respect given to the intellectual property rights of the author. 

### Semantic Contents
This file contains data about every baseball stadium including its name, seating capacity, and dimensions of fair and foul territory.

I will mainly be looking at the seating capacity within this file, and potentially the list of stadiums if I can get it to come out well. The fair and foul territory were taken as an option for my final dataset to include, in that source #4 of mine (voice-of-fan-report-2017) has a category that looked at facilities, which considered sightlines and seating. Fair and foul territory within stadiums could have some correlation to this category.

The HTML page was web scraped sometime in September 2019 and written to a CSV file.


### Collection Process
Not much is known about the collection process since the website seems to be largely run by one person. I will need to find more about this later.

I was able to use Python's requests module to scrape the contents of the web page and save the HTML contents locally. Since the data was neatly written into table format within the HTML code, I was able to use a tree structure using the lxml html module to then simply grab the data points I wanted. I appended all of those rows of data and then wrote it into a CSV. 

### Data Structure
The data is currently structured into 73 rows in a CSV file that I web scraped. This data was written into a CSV file, so every data entry is currently in quotations and brackets. Each column is as follows:

* Stadium Name - This will include stadiums from the past and present. 
* Team Name 
* Seating Capacity - The number of total seats in a stadium. This will be used with the baseball-reference data as I described there.
* Fair Territory - The number given in each row is according to 1,000 sq ft.
* Foul Territory - The number given in each row is according to 1,000 sq ft.

The missing values can be attributed to old stadiums not having the data at all, or in the case of stadium names missing, it could be a formatting issue. This will require either another web scrape effort or simple hand edits to the CSV. It will be determined on whether or not there are missing values once I weed out the stadiums I do not need.