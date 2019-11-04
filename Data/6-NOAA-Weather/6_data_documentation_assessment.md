# 6. NOAA-Weather


### Data Cleaning Assessment
As of right now I will actually be working with two separate CSV files from this source. Both are along the same lines of listing major cities within the US and their weather or precipitation data. The cleaning process for each file will primarily consist of consolidating the data down to the 30 cities where the baseball stadiums are located. As of right now, both CSV's contain 219 rows. 

1. Gather a list of the 30 cities that I need from another data source. 
2. Write this list into a separate .txt file to be used within the main CSV files.
3. Get row data from the 30 cities.
4. Edit the column headers to indicate temperature in degrees Fahrenheit and precipitation in inches.

This may take between 6-7 hours. There is a lot of data to gather, and I still may need to get even more specific with areas within a certain region for weather data. Creating two new CSV's from the previous files will require I get through that data.


### Authorship, Attribution, Provenance
This data was compiled at the request of NOAA Headquarters. I don't think individual authorship exists for these data sets.


### Semantic Contents
The weather temperature file contains average temperature and its comparison to 1981-2010 averages from May through October 2017 for all major US cities.

The weather precipitation file contains average precipitation and its comparison to 1981-2010 averages from May through October 2017 for all major US cities.

This data is broad and contains averages on a 6 month scale, so it will help when I look at the average attendance per game, since I don't have specific data that is tied to a specific month or date.

The CSV files were downloaded in October 2019. I selected my time frame (6 months) and date range (from May to October) in the year 2017 before downloading the files directly from the NOAA website.


### Collection Process
The only information about the collection process can be found [here]('https://www.ncdc.noaa.gov/cag/city/background'). 


### Data Structure
Both of these files are in CSV format and each file contains 219 rows of data. There are no missing values in either of these datasets The temperature CSV file columns start on line 4 and include:

* Location ID - This is an alpha-numeric code given to each city, and I will not be using this.
* Location - The city and state for each row of data in this dataset. 
* Value - The average temperature within the 6 month span of time. Expressed as an integer in degrees Fahrenheit.
* 1981-2010 Mean - The average temperature in that area over the 30 year span between those years.
* Anomaly - Compares the value with the 30 year mean to give a difference integer.


The weather CSV file columns start on line 4 and include:

* Location ID - This is an alpha-numeric code given to each city, and I will not be using this.
* Location - The city and state for each row of data in this dataset.
* Value - The average precipitation within the 6 month span of time. Expressed as an integer in inches.
* 1981-2010 Mean - The average precipitation in that area over the 30 year span between those years.
* Anomaly - Compares the value with the 30 year mean to give a difference integer.
