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