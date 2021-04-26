#This will not run on online IDE
import requests
from bs4 import BeautifulSoup
import csv
import time
import re

def upload_status(URL = "https://officialpiratebay.com/search.php?q=user:sotnikam"):
    
    r = requests.get(URL)
  
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

    title_list = []
    date_list = []
    size_list = []
    link_list = []
    hash_list = []
    count = 0
    #print(soup.prettify())

    for title in soup.findAll('span',attrs = {'class':['list-item item-name item-title']}):

        title = title.get_text()
        title_list.append(title)

    for date in soup.findAll('span',attrs = {'class':[ 'list-item item-uploaded']}):

        date = date.get_text()
        date_list.append(date)

    for size in soup.findAll('span',attrs = {'class':['list-item item-size']}):

        size = size.get_text()
        size_list.append(size)

    for link in soup.findAll(href=re.compile("description")):
        
        
        link = link.get('href')
        link = "https://officialpiratebay.com" + str(link)
        link_list.append(link)

        r = requests.get(link)
  
        soup = BeautifulSoup(r.content, 'html5lib')

        file_hash = soup.findAll(id = "ih")
    
        file_hash = file_hash[0].get_text()

        hash_list.append(file_hash)

        count = count + 1
        print(str(count) + ' no. of HASH found.')
        
    filename = URL.strip('https://officialpiratebay.com/search.php?q=user: ')
    filename = filename + '.txt'
    with open(filename, "a") as f:
        f.write("Title" + "\t" + "Date" + "\t" + "Size\t" + "Link\t" + "Hash\n" ) 
        for i in range(len(title_list)):
            f.write(title_list[i] + '\t' + date_list[i] + '\t' + size_list[i] + '\t' + link_list[i] + '\t' + hash_list[i])
            f.write('\n')
    
    print('Total ' + str(count) + " HASH found. File in " + filename)


upload_status()
upload_status(URL = 'https://officialpiratebay.com/search.php?q=user:TvTeam')


