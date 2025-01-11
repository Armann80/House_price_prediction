from base64 import encode
from gettext import find
from operator import mod
from bs4 import BeautifulSoup
from urllib.request import urlopen
from unidecode import unidecode
import os
import urllib.parse
from unidecode import unidecode
t_file = open('T.txt',mode='r+',encoding = 'utf-8')
host = open('host.txt',mode='r+',encoding = 'utf-8')


os.system('cls')

url = 'https://divar.ir/s/mashhad/buy-apartment/abkuh'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
type(soup)
Data_fpage = 'div',{'class':'post-card-item-_-af972 kt-col-6-_-bee95 kt-col-xxl-4-_-e9d46'} #link
num = 10304
New_Data_mode = 'div',{'class':'browse-post-list-_-f3858','style':'padding-top: 7176px; padding-bottom: 2208px;'}
Data_Spage = 'p',{'class':'kt-unexpandable-row__value'} #price-price per area-floor
Data_r_a_a = 'span',{'class':'kt-group-row-item__value'} #age - area - rooms
Data_loc = 'div',{'class':'kt-page-title__subtitle kt-page-title__subtitle--responsive-sized'}
    

links = soup.findAll(Data_fpage)
to_str = str(links)
cleared_text = BeautifulSoup(to_str,'html.parser').get_text() 

# host.write(str(links))

for i in soup.findAll('a'):
    print(i.get('href'))

      

 