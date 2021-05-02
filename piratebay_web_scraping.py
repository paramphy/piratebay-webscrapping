import requests
from bs4 import BeautifulSoup
import csv
import time
import re

def hash_finder(link):
    
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html5lib')
    file_hash = soup.findAll(id = "ih")
    file_hash = file_hash[0].get_text()
    #time.sleep(5)
    return(file_hash)


def page_scraper(URL = "https://officialpiratebay.com/search.php?q=user:sotnikam"):
    
    r = requests.get(URL)
  
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    title_list = []
    date_list = []
    size_list = []
    link_list = []
    hash_list = []
    category_list = []
    count = 0

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
        file_hash = hash_finder(link)
        hash_list.append(file_hash)
        count = count + 1
        print('No. of HASH found. ' + str(count))

    for category in soup.findAll('span',attrs = {'class':['list-item item-type']}):

        category = category.get_text()
        category_list.append(category)

    return(title_list, date_list, size_list, link_list, hash_list, category_list)

def file_output(URL,filename):

    count = 0
    title_list, date_list, size_list, link_list, hash_list, category_list = page_scraper(URL)        
    filename = filename + '.txt'
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Title" + "\t" + "Date" + "\t" + "Size\t" + "Link\t" + "Hash\n" ) 
        for i in range(len(title_list)):
            f.write(category_list[i] + '\t' + title_list[i] + '\t' + date_list[i] + '\t' + size_list[i] + '\t' + link_list[i] + '\t' + hash_list[i])
            f.write('\n')
            count+=1
    
    print('Total ' + str(count) + " HASH found. File in " + filename)

def page_scraper_user(user_name):
    
    prefix = 'https://officialpiratebay.com/search.php?q=user:'
    URL = prefix + user_name
    file_output(URL, user_name)

def page_scraper_search(search_term):

    prefix = 'https://officialpiratebay.com/search.php?q='  
    suffix = '&cat=0'
    URL = prefix + search_term + suffix
    file_output(URL, search_term)


def page_scraper_recent_100():

    URL = 'https://officialpiratebay.com/search.php?q=top100:recent'
    file_output(URL, 'top100recent')


def main():
     
    page_scraper_user('jajaja')
    page_scraper_search('DC')
    page_scraper_recent_100()



if __name__ == "__main__":
    main()


