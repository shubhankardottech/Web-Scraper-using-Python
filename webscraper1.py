# import the libraries
import requests
from bs4 import BeautifulSoup

# specify the url of the webpage you want to scrape
url = 'https://www.shubhankar.tech'
# send an HTTP request to the webpage
response = requests.get(url)

# parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# find specific elements on the webpage using tags, classes, and/or ids
data = soup.find_all('p')

# print the scraped data
for d in data:
    print(d.text)