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

    for row in soup.findAll('span',attrs = {'class':'list-item item-name item-title'}):

        quote = {}
        quote['title'] = row.string
        download_list.append(quote)

    if not (download_list_new==download_list):
        print("New content has been uploaded \n")

    download_list_new = download_list

    filename = 'sotnikam_page_info.csv'
    print(download_list)
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['title','date'])
        w.writeheader()
        for quote in download_list:
            w.writerow(quote)


while True:
    upload_status()
    time.sleep(60*60)

