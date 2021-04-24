#This will not run on online IDE
import requests
from bs4 import BeautifulSoup
import csv
import time

def upload_status(URL = "https://officialpiratebay.com/search.php?q=user:sotnikam"):
    
    r = requests.get(URL)
  
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

    download_list_new = []

    download_list = []
    print(soup.prettify())

    for row in soup.findAll('span',attrs = {'class':['list-item item-name item-title']}):

        title = {}
        title['title'] = row.get_text()
        download_list.append(title)

        
    print(download_list)

    filename = 'sotnikam_page_info.csv'
    print(download_list)
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['title'])
        w.writeheader()
        for quote in download_list:
            w.writerow(quote)


upload_status()

