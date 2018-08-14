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

# Access the csv file and create a header row
csv_file = csv.writer(
    open(
        '/Volumes/vv-external-1/Django/python_scripts/data/z-artist-names.csv',
        'w'))
csv_file.writerow(['Name', 'Link'])


for c in ascii_uppercase:
    for i in range(1, 100):

        url = 'https://web.archive.org/web/20120928064648/http://www.nga.gov/collection/an' + c \
            + str(i) + '.htm'
        # print(url)

        page = requests.get(url, headers=HEADER)
        # print(page.status_code)

        if page.status_code == 200:
            soup = BeautifulSoup(page.text, 'html.parser')

            # Remove superflous data
            # Inspect the DOM. SUerflous data is in table name AlphaNav. Decompose them
            last_links = soup.find(class_='AlphaNav')
            last_links.decompose()

            page_list = soup.find(class_='BodyText')
            # print(page_list)

            artist_name_list = page_list.find_all('a')

            try: 
                for artist_name in artist_name_list:   
                    print(artist_name)   
                    name = artist_name.contents[0]
                    link = 'https://web.archive.org' + artist_name.get('href')
                    # output to the csv file
                    csv_file.writerow([name, link])
            except IndexError:
                name = 'null'
                link = 'null'
            continue
        else:
            break
csv_file.close()