import requests
from bs4 import BeautifulSoup
import csv
import time
import re

import piratebay_web_scraping

search_term = 'supergirl'

URL = 'https://officialpiratebay.com/search.php?q=' + search_term + '&cat=0'
print('URL = ', URL)

piratebay_web_scraping.upload_status(URL = URL)