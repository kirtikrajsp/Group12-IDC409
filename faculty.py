import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import re
import numpy as np
import tabulate
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
print("Fetching main faculty page...")
data = requests.get('https://www.iiserkol.ac.in/web/en/people/faculty/dbs/')
soup = BeautifulSoup(data.content, "html.parser")

# Collecting faculty profile URLs
urls = [link['href'] for link in soup.find_all('a')]
urls = [url for url in urls if '/web/en/people/faculty/dbs/' in url]
link = 'https://www.iiserkol.ac.in'
faculty_websites = list(set([link + url for url in urls]))
print(f"Found {len(faculty_websites)} faculty profile URLs.")