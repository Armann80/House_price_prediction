from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
from unidecode import unidecode


loc = open('Q.txt',mode='r+',encoding='utf-8')
loc1 = open('location.txt',mode='r+',encoding='utf-8')

def get_data_page(str_text,mode=1):
    url = str_text
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    type(soup)
    Data_fpage = 'h1',{'class':'DUwDvf fontHeadlineLarge'} #link
    
    links = soup.findAll(Data_fpage)
    
    to_str = str(links)

    cleared_text = BeautifulSoup(to_str,'html.parser').get_text() 

    return links,cleared_text 

r,r1 = get_data_page('https://www.google.com/maps/place/%D8%A7%D8%B3%D8%AA%D8%A7%D9%86+%D8%AE%D8%B1%D8%A7%D8%B3%D8%A7%D9%86+%D8%B1%D8%B6%D9%88%DB%8C%D8%8C+%D9%85%D8%B4%D9%87%D8%AF%D8%8C+%D9%85%DB%8C%D8%AF%D8%A7%D9%86+%D8%AF%D9%87+%D8%AF%DB%8C%D8%8C+%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%E2%80%AD/@36.2839269,59.6061482,15z/data=!4m5!3m4!1s0x3f6c913b17c2cf09:0xa6795223cc507c22!8m2!3d36.2839272!4d59.5974149')

a = loc.readlines()

for item in range(len(a)):
    Encoded = unidecode(a[item])
    loc1.write(Encoded)
    # loc1.write('\n')



