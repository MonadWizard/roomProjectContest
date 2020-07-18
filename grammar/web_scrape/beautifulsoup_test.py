import requests
from bs4 import BeautifulSoup

# Collect and parse first page
page = requests.get('https://www.google.com/search?q=president+of+bangladesh')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='_XWk')

# Pull text from all instances of <a> tag within BodyText div
# artist_name_list_items = artist_name_list.find_all('_uX kno-fb-ctx')
artist_name_list_items = artist_name_list.find_all('a')


for artist_name in artist_name_list_items:
    print(artist_name.prettify())
# print(artist_name_list)


