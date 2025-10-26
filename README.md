# Group12-IDC409
Group 12 - Web Scraping 2
(MS22254 & MS22217)

Web scraping 2  is a data analysis project that collects, stores and processes information about faculty members from the Department of Biological Sciences (DBS), IISER Kolkata.
It automatically extracts key academic details such as their Designation, PhD background, Research interests, Awards,Years of experience, and then stores the data in a SQLite3 database and generates graphs for analysis.

Here’s what the script does step-by-step:

	1.	Scrapes the main IISER Kolkata DBS faculty webpage to get all individual faculty profile links.

	2.	Visits each profile and extracts relevant data such as: Name, Designations (current and past), Academic background (PhD institution, year, etc.), Research interests, Awards and honors

	3.	Stores the collected data into a local SQLite3 database for easy retrieval and further analysis.

	4.	Loads the data into a Pandas DataFrame and performs classification:
	a.	Automatically identifies whether the faculty’s PhD was done in India or Abroad.
	b.	Calculates years of experience since PhD.
	c.	Categorizes designations as Assistant / Associate / Professor.

	5.	Performs data analysis and visualization using Matplotlib:
	a.	Pie charts comparing Indian vs. Abroad PhD counts, Faculty designation distribution, and Indian vs. Abroad PhD comparison by designation (Professor, Associate, Assistant)
	b.	Bar charts showing average awards and experience by designation, Comparison of awards by PhD location.