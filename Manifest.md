# Manifest


## .idea
This folder is for the GitHub Desktop app.

## ipynb_checkpoints
This folder contains my Jupyter Notebook and a draft of it, but I typically access it from my Data folder.

## Class Documentation
This folder contains Word documents from throughout the semester like the Final Project Proposal, Dataset Inventory and Reviews, Final Dataset Design Plan, etc. Some of these documents may not reflect my final project because of the ways my project has changed throughout the semester.


## Data
Contains six total folders, four of which are my intermediate datasets labeled with a number. There numbers are out of order because I eliminated some datasets throughout the semester. Anything in a bullet point is considered a folder below.

* **.idea** <br />
This folder is for the GitHub Desktop app.

* **ipynb_checkpoints** <br />
This folder contains my Jupyter Notebook and a draft of it, but I typically access it from my Data folder.

* **1-ESPN-health-data** <br />
This folder contains the ESPN health code violation dataset. There are two .py files, one for the web scraping and another one for extracting the code from the scraped data. The data was web scraped into the .HTML file, then copied and reworked into a separate JSON file. There is a readme file with notes from throughout the semester, and the final CSV of data that made up this intermediate dataset.
	* **originaldataDONOTEDIT** <br />
	Original dataset undedited in JSON form.</p>

* **3-baseball-reference-team-data** <br />
Contains the baseball statistics gathered and download from Baseball-reference.com. Two CSVs make up this intermediate dataset, along with a readme file of notes and data documentation.
	* **originaldataDONOTEDIT** <br />
	Original datasets unedited in CSV form.</p>


* **4-voice-of-fan-report-2017** <br />
This folder contains review score data on baseball stadiums. The data originally comes as a CSV, which was copied from the webpage. The .py file then calculates a new average score within this dataset. Contains the final intermediate dataset file as a CSV.
	* **originaldataDONOTEDIT** <br />
	Original dataset unedited in CSV form.</p>


* **6-NOAA-weather** <br />
Contains the two original downloaded CSV files for both temperature and precipitation data. Then uses two separate .py files for each to extract the necessary data and write it into two new CSV files. </p>
Note: 6-ESPN-stadium-violations is a copy of the intermediate dataset from 1-ESPN-stadium-violations. I renamed it to have the number 6 to match this current intermediate dataset. It provides a list of cities that correspond to the stadium so that those cities can be matched with city temperature and precipitation data. 

	* **Missing City Data** <br />
	Contains eight total CSV files. Two files correspond to cities that had missing data for both temperature and precipitation. These were all found from the same NOAA source by looking at the county level instead of just the city. Hand-calculated averages are contained within each CSV in this folder as well. The results were then added to the original CSV datasets.
	

	* **originaldataDONOTEDIT** <br />
	Original datasets unedited in CSV form.</p>


**Final Single Dataset** <br />
Filename: baseball-stadium-data-dataset.CSV

**Jupyter Notebook** <br />
Tucci-notebook.ipynb


