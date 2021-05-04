import requests
from bs4 import BeautifulSoup
import time
import re
from tqdm import tqdm
import datetime


def hash_finder(link):

    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html5lib")
    file_hash = soup.findAll(id="ih")
    file_hash = file_hash[0].get_text()
    # time.sleep(5)
    return file_hash


def page_scraper(URL="https://officialpiratebay.com/search.php?q=user:sotnikam"):

    r = requests.get(URL)

    soup = BeautifulSoup(
        r.content, "html5lib"
    )  # If this line causes an error, run 'pip install html5lib' or install html5lib
    title_list = []
    date_list = []
    size_list = []
    link_list = []
    hash_list = []
    category_list = []
    count = 0

    for title in soup.findAll(
        "span", attrs={"class": ["list-item item-name item-title"]}
    ):

        title = title.get_text()
        title_list.append(title)

    for date in soup.findAll("span", attrs={"class": ["list-item item-uploaded"]}):

        date = date.get_text()
        date_list.append(date)

    for size in soup.findAll("span", attrs={"class": ["list-item item-size"]}):

        size = size.get_text()
        size_list.append(size)

    pbar = tqdm(total=100)

    for link in soup.findAll(href=re.compile("description")):

        link = link.get("href")
        link = "https://officialpiratebay.com" + str(link)
        link_list.append(link)
        file_hash = hash_finder(link)
        hash_list.append(file_hash)
        count = count + 1
        #print("No. of HASH found. " + str(count))
        pbar.update(100/len(title_list))
    pbar.close()
        

    for category in soup.findAll("span", attrs={"class": ["list-item item-type"]}):

        category = category.get_text()
        category_list.append(category)

    return (title_list, date_list, size_list, link_list, hash_list, category_list)


def file_output(URL, filename):

    count = 0
    (
        title_list,
        date_list,
        size_list,
        link_list,
        hash_list,
        category_list,
    ) = page_scraper(URL)
    filename = filename + ".md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("**Category**"+"|"+"**Title**" + "|" + "**Date**" + "|" + "**Size**|" + "**Link**|" + "**Hash**")
        f.write("\n")
        f.write(":-----:|:-----:|:-----:|:-----:|:-----:|:-----:")
        for i in range(len(title_list)):
            f.write(
                category_list[i]
                + "|"
                + title_list[i]
                + "|"
                + date_list[i]
                + "|"
                + size_list[i]
                + "|"
                + "[Link]("+link_list[i]+")"
                + "|"
                + hash_list[i]
            )
            count += 1

    print("\nTotal " + str(count) + " HASH found. File in " + filename + "\n")


def page_scraper_user(user_name):

    prefix = "https://officialpiratebay.com/search.php?q=user:"
    URL = prefix + user_name
    file_output(URL, user_name)


def page_scraper_search(search_term):

    prefix = "https://officialpiratebay.com/search.php?q="
    suffix = "&cat=0"
    URL = prefix + search_term + suffix
    file_output(URL, search_term)


def page_scraper_recent_100():

    URL = "https://officialpiratebay.com/search.php?q=top100:recent"
    file_output(URL, "top100recent")

def page_scraper_url(URL):

    URL = URL
    filename = 'url'
    file_output(URL, filename)


def main():

    #page_scraper_user("MrStark")
    #page_scraper_search("")
    #page_scraper_recent_100()
    page_scraper_url('https://officialpiratebay.com/search.php?q=top100:599')


if __name__ == "__main__":
    main()
