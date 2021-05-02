import requests
from bs4 import BeautifulSoup
import csv
import time
import re

from piratebay_web_scraping import *

def piratbay_search_page_data(search_term):
    
    URL = 'https://officialpiratebay.com/search.php?q=' + search_term + '&cat=0'
    print('URL = ', URL)
    page_scrape(URL = URL)

def main():
    search_term = 'daredevil'
    piratbay_search_page_data(search_term)

if __name__ == "__main__":
    main()