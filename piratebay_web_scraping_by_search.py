import requests
from bs4 import BeautifulSoup
import csv
import time
import re

from piratebay_web_scraping import upload_status

def piratbay_search_page_data(search_term):
    search_term = 'daredevil'
    URL = 'https://officialpiratebay.com/search.php?q=' + search_term + '&cat=0'
    print('URL = ', URL)
    upload_status(URL = URL)

def main():
    search_term = 'daredevil'
    piratbay_search_page_data(search_term)

if __name__ == "__main__":
    main()