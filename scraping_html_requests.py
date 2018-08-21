from requests_html import HTMLSession
import csv, pprint
from string import ascii_uppercase

# Access the csv file and create a header row
csv_file = csv.writer(
    open(
        '/Volumes/vv-external-1/Django/python_scripts/data/a-z-artist-names.csv',
        'w'))
csv_file.writerow(['Name', 'Link'])

session = HTMLSession()

for c in ascii_uppercase:
    for i in range(1, 100):

        url = 'https://web.archive.org/web/20120928064648/http://www.nga.gov/collection/an' + c \
            + str(i) + '.htm'

        r = session.get(url)

        artist_list = r.html.find('table', first=True)
        
        pprint.pprint(artist_list.find('a'))
