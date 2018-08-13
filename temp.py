# Access the csv file and create a header row
csv_file = csv.writer(
    open(
        '/Volumes/vv-external-1/Django/python_scripts/data/z-artist-names.csv',
        'w'))
csv_file.writerow(['Name', 'Link'])


# Retrieve related pages
# on this site there are 4 pages listing pages with the letter Z
pages = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(
        i) + '.htm'
    pages.append(url)

for item in pages:

    # Collect first page of artists list
    page = requests.get(item, headers=HEADER)
    # print(page.content)

    # Create BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    # Remove superflous data
    # Inspect the DOM. SUerflous data is in table name AlphaNav. Decompose them
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    # Pull all text from the BodyText div
    artist_list = soup.find(class_='BodyText')

    # Pull text items from all instances of the <a> tag within the BodyText tag into a list
    artist_name_list_items = artist_list.find_all('a')

    # Iterate over all the artist names and put them in a list
    for artist_name in artist_name_list_items:
        # prettified list of artist names
        # print(artist_name.prettify())

        # Pull contents from the tag
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        # print (names)
        # print (links)

        # output to the csv file
        csv_file.writerow([names, links])
