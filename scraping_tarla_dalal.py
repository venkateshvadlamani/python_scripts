"""Scraping the Tarla Dalal website


"""
from requests_html import HTMLSession
import csv, pprint

# Access the csv file and create a header row
csv_file = csv.writer(
    open(
        '/Volumes/vv-external-1/Django/python_scripts/data/tarla-dalal.csv',
        'w'))



url = 'https://www.tarladalal.com/'

session = HTMLSession()
response = session.get(url)
csv_file.writerow(response.html.absolute_links)
for link in response.html.absolute_links:
    pprint(type(link))
    pprint('%%%%')