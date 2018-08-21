"""Scraping wikipedia to play 7-degrees of seperation.

Required libraries - requests, csv, bs4
"""
import requests, csv
from bs4 import BeautifulSoup

HEADER = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
