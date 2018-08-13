"""Scraping web pages with Beautiful Soup and Python

Required libraries - requests  bs4  csv pprint
Objective - Scrape the National Gallery of Art - 
    https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm
"""
import requests, csv
from bs4 import BeautifulSoup
from pprint import pprint
from string import ascii_uppercase

HEADER = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

for c in ascii_uppercase:
    for i in range(1, 50):

        url = 'https://web.archive.org/web/20120928064648/http://www.nga.gov/collection/an' + c \
            + str(i) + '.htm'
        print(url)

        page = requests.get(url, headers=HEADER)
        print(page.status_code)

        if page.status_code == 200:
            soup = BeautifulSoup(page.text, 'html.parser')

            page_list = soup.find(class_='BodyText')
            # print(page_list)

            alphabet_list = page_list.find_all('a')
            print(alphabet_list)
        