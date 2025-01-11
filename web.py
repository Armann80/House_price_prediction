from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from unidecode import unidecode
import collections


T_file = open('T.txt',mode='r+',encoding = 'utf-8')

os.system('cls')

# driver = webdriver.Firefox()
print('Program Ran!')

driver = webdriver.Chrome()
url = 'https://divar.ir/s/mashhad/buy-apartment/abkuh'

driver.get(url)



SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    html = urlopen(url)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(html,'html.parser')
type(soup)

links = soup.findAll()

my_links = []

for link in soup.find_all('a'):
   my_links.append(link.get('href'))
   T_file.write(link.get('href'))


w = ([item for item, count in collections.Counter(my_links).items() if count > 1])
print(len(w))

