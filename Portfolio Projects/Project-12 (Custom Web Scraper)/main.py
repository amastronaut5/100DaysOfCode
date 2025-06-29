#CUSTOM WEB SCRAPER
from bs4 import BeautifulSoup
import pandas as pd
import requests


URL= 'https://apod.nasa.gov/apod/archivepixFull.html'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('b').text.strip()

