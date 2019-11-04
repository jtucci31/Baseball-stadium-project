# 4. Voice-of-Fan-Report-2017


### Data Cleaning Assessment
This file is currently in a CSV format. The cleaning will involve transforming a lot of the numbers within this dataset and writing a new CSV that makes a little bit more sense of the raw data. I will mainly want to take an average of the four main factors (facility, family, fan experience, food and drink) so that the new overall score will generate an average score for each stadium, rather than the current overall score which is just all four factors added together. This number will make more sense logistically because the overall score does not make sense compared to the other scores which are in a range from -1 to +1.

This will take me between 2-3 hours. I will need to run the current CSV through Python code and extract the values for each row. Then those values and that data will need to run through an equation that will calculate the average score per stadium, and then that new piece of data will need to be written back into the dataset to create an all new dataset. 

One row will actually need to be removed entirely, and that can be done by hand. The Atlanta Braves opened a new stadium and began playing at SunTrust Park in 2017, abandoning Turner Field and playing their last season there in 2016. Yet, this dataset still includes Turner Field in a 2017 review, because they wanted to compare both stadiums to see how the new stadium compared. The Turner Field entry will be removed by hand before transforming this data.

### Authorship, Attribution, Provenance
I'm still unable to find a true author for this source. Still in the process of looking for that. 

### Semantic Contents
This file contains data collected from baseball stadium reviews and compiled that data into a score for four categories: food and drink, fan experience, family experience, and facilities.

I will be looking at this entire dataset, and the other subsequent pieces of data I created with this set of data to compare to different aspects of baseball stadiums like attendance, team success, and weather to see any correlation. 

I obtained this data in early September 2019. The data was already organized into a chart from the webpage, so I just copied the entire dataset as it was and pasted it into Excel because I knew it would retain its look. Within Excel, I had to do some basic data formatting for it to convert properly, then I saved it as a CSV. 

### Collection Process
This data used reviewtrackers.com to get access to thousands of reviews from websites like Google, Facebook, Yelp, etc. The authors used a natural language understanding algorithm to properly analyze over 130,000 reviews of stadiums based on certain keywords and phrases such as hot dogs, seats, family, etc. These keywords were then grouped into the four main categories that the data is set to. This data was then given a sentiment score which ranges on a scale from -1 to + 1. 

Little effort was done on my part to gather this data for my own use. As I stated previously, I was able to simply copy and paste this data into an Excel file since it was already well organized on the webpage. 

### Data Structure
This CSV file is structured according to each stadium, much like my previous datasets have been. There are 31 total entries and rows of data with 1 row above for the identifiers, totalling 32 rows. The columns are as follows: 

* Stadium Name
* Facility - This score is based on keywords like parking, neighborhood, transit, bathrooms, accessibility, and customer service found in reviews. This score is in a range of -1 being the worst and +1 being the best.
* Family - This score is based on keywords like cost, giveaways, security, activity areas, free activities, and lower prices found in reviews. This score is in a range of -1 being the worst and +1 being the best.
* Fan Experience - This score is based on keywords like seats, scoreboard, sightlines, atmosphere, crowd, history, and ambiance found in reviews. This score is in a range of -1 being the worst and +1 being the best.
* Food and Drink - This score is based on keywords like hot dog, beer, and any other kind of food and drink offered at stadiums found in reviews. This score is in a range of -1 being the worst and +1 being the best.
* Overall - This is the sum of the previous four categories added together. Because 1 is the best score and -1 is the worst score, that means that the overall score is in a range from -4 to +4. This specific data point is one I aim to change and have make more sense within the context of the previous four categories by taking the average instead. 

This data has no missing values within any row. This data is largely integers in a range, which make them all long numbers. The overall score, as mentioned previously, is all four categories added together to create a new general score for each stadium. 