# Group12-IDC409
Group 12 - Web Scraping 2
(MS22254 & MS22217)

Web scraping 2  is a data analysis project that collects, stores and processes information about faculty members from the Department of Biological Sciences (DBS), IISER Kolkata.
It automatically extracts key academic details such as their Designation, PhD background, Research interests, Awards,Years of experience, and then stores the data in a SQLite3 database and generates graphs for analysis.

What does the code do?

	1.	Scrapes the main IISER Kolkata DBS faculty webpage to get all individual faculty profile links.

	2.	Visits each profile and extracts relevant data such as: Name, Designations (current and past), Academic background (PhD institution, year, etc.), Research interests, Awards and honors.

	3.	Calculates years of experience since PhD.

	4.	Stores the collected data into a local SQLite3 database for easy retrieval and further analysis.

	5.	Loads the data into a Pandas DataFrame and performs classification:
	a.	Classifies based on whether the faculty’s PhD was done in India or Abroad.
	b.	Categorizes designations as Assistant / Associate / Professor.

	6.	Performs data analysis and visualization using Matplotlib:
	a.	Pie charts comparing Indian vs. Abroad PhD counts, Faculty designation distribution, and Indian vs. Abroad PhD comparison by designation (Professor, Associate, Assistant)
	b.	Bar charts showing average awards and experience by designation, Comparison of awards by PhD location. 
	c. Scatter plot 


Tools used:

	•	Requests → To fetch website data
	•	BeautifulSoup (bs4) → For HTML parsing and web scraping
	•	SQLite3 → For storing scraped data in a local database
	•	Pandas → For data manipulation and analysis
	•	Matplotlib → For plotting and visualization
	•	NumPy → For numerical operations
	•	Regular Expressions (re) → For cleaning and extracting text



Now lets look at the code by analysing each section:


Section 1: Importing Required Libraries

All Python libraries needed for this project are imported at the start.
	•	requests is used to fetch web pages from IISER Kolkata.
	•	BeautifulSoup from bs4 parses the HTML content of these pages.
	•	pandas and numpy handle data organization, cleaning, and analysis.
	•	sqlite3 is used to create and manage a database for storing the scraped data.
	•	re helps extract patterns such as PhD years.
	•	matplotlib.pyplot is used for plotting graphs.
	•	seaborn is used for swarm plots.
	•	scipy.optimize is used for curve fitting in scatter plots.
	•	tabulate and IPython.display help display tables neatly.



Section 2: Fetching Faculty Profile URLs

The main faculty page of IISER Kolkata’s Department of Biological Sciences is fetched using requests.get().
	•	HTML content is parsed with BeautifulSoup.
	•	All <a> links are collected, then filtered to retain only those belonging to faculty profiles.
	•	Duplicate links are removed with set().
	•	At the end of this step, we have 27 unique faculty profile URLs.



Section 3: Scraping Faculty Details and Creating the Profile Dictionary

Each faculty profile page is visited individually using requests.
	•	BeautifulSoup parses each page to extract required information.
	•	A dictionary called profile_data is created for each faculty member.

The dictionary contains:
	•	Name
	•	Positions (all positions held)
	•	Designation (current position)
	•	Academic Background
	•	PhD (Location)
	•	PhD Year (of completion)
	•	Years of Experience (calculated from 2025 minus PhD year)
	•	Research Interests
	•	Awards and Honors
	•	Number of Awards
All valid dictionaries are appended to all_data, forming a complete collection of faculty profiles.
Pages that do not load or have missing information are skipped.



Section 4: Storing Data into SQLite3 Database

The scraped data is stored in SQLite3.
	•	A new database faculty_data.db is created, with a table Faculty matching the profile dictionary keys.
	•	Any existing table is dropped to avoid duplication.
	•	Each profile is inserted with SQL commands in a Python loop.
	•	conn.commit() saves all changes.



Section 5: Data Loaded into Pandas and Classified



