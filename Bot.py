from base64 import encode
from gettext import find
from operator import mod
from bs4 import BeautifulSoup
from urllib.request import urlopen
from unidecode import unidecode
import os
import urllib.parse
from unidecode import unidecode
import time
import csv
import pandas as pd
import requests
import ast
import json
os.system('cls')



Data = open('Data.txt',mode='r+',encoding = 'utf-8')
Data_r = Data.readlines()

T_file = open('T.txt',mode='r+',encoding = 'utf-8')
T_read = T_file.readlines()
Dataset_file = open('Dataset.csv',mode='w')
list_file = open('list_file.txt',mode='r+',encoding = 'utf-8')
host = open('host.txt',mode='r+',encoding = 'utf-8')
list_Encoded = open('list_Encoded.txt',mode='r+',encoding = 'utf-8')
loc = open('location.txt',mode='r+',encoding = 'utf-8')
loc_link = open('loc_link.txt',mode='r+',encoding = 'utf-8')
host_list = host.readlines()
file_list = list_file.readlines()
Encoded_list = list_Encoded.readlines()
loc_list = loc.readlines()
loc_links = loc_link.readlines()


list_location = ['10 dy','17 shhrywr','abkhwh','azdshhr','ayt llh khmnhy','ayt llh `bdy,bwdhr','bwTlb','Hmdabd','rshd','rwnd','qbl','lhyh','mm khmyny','mm rD,myrabd','myryh','nSr','nqlb','ythr','ythrgrn','ymn','ywn','bG mlkhabd','bhnr','bll','blwr tws','blwr sjd','bhrn','bhrstn','bhshty','bhmn','prdys','prwyn `tSmy','pnj tn al `b','tlgrd','thmn','jnbz','jnt','chhrbG','chhnw','Hjt','Hrm mThr','Hsynabd','khwjh rby`','dnsh','dnshjw','dnshgh frdwsy mshhd','drwy','dhnwy','rh ahn','rhnmyy','rbT Trq','rslt','rDshhr','rDyyh','spd','stry','sjdyh','s`dy','slm','smrqnd','snbd','syd rDy','sydy','sysabd','shf','shhrar','shhrkh bwdhr','shhrkh shhyd rjyy','shhrkh shyryn','shhrkh Tlqny','shhyd awyny','shhyd qrbny','shhyd mThry shmly','shhyd m`qwl','shhyd hnrwr','shyrwdy','Sdf','Syd shyrzy','Tbrsy','Tbrsy shmly','Trq','`ml','`bsabd','`bdlmTlb','`sgryh','`nSry','`ydgh','frG ltHSyln','fTmyh','fdkh','frmrz `bsy','frwdgh','frhng','flkhh brq (mydn bsyj)','flkhh Dd (15 khrdd)','qsmabd (shhrkh Grb)','khrgrn','khrmndn wl','khrmndn dwm','khshmr','pwrsyn','khshwrz','khlhdwz','flsTyn','khwshsh','khwh sngy','khwy myrlmwmnyn','khwy plys','khwy mhdy','gz','glshwr','gwhrshd','mjd','mHlh myrlmwmnyn','mHlh bl khybn','mHlh pyyn khybn','mHlh pnj tn','mHlh jhdshhr','mHlh chhrchshmh','mHlh rdh','mHlh srfrzn','mHlh Tlb','mHlh khwthr','mHlh nn rDwy','mHlh nyrw hwyy','mHlh wHyd','mHlh hnrstn','mHmdabd','mSTfy khmyny','mSly','mThry jnwby','mqdm','mwswy qwchny','mw`wd','mhdy abd','mhrabd','mydn `dl khmyny','nmyshgh byn lmlly mshhd','nwGn','nwfl lwshtw','nyzh','wkhylabd','wly`Sr','hshmynjd','hshmyh','hft tyr']

def Encode_url(list_url,mode='save', obj = ''):
    if mode == 'save':
        Enc_list = []
        for item in list_url:
            Encoded = urllib.parse.quote(item)
            Encoded = Encoded.replace('%0A','')
            list_Encoded.write('https://divar.ir')
            list_Encoded.write(Encoded)
            list_Encoded.write('\n')
    elif mode == 'online':
        Encoded = urllib.parse.quote(obj)
        Encoded = Encoded.replace('%0A','')
        return 'https://divar.ir' +  Encoded        
def find_link(text): # Finding all Special Links from the page
    page_url = ''
    item = 0
    for item in range(len(text)+1):
        if (len(text)-10) > item:
            if text[item] == 'h' and text[item+1] == 'r' and text[item+2] == 'e' and text[item+3] == 'f' and text[item+7] == 'v':
                counter = 6
                while text[item+counter] != '"' and text[item+counter+1] != '>':
                    page_url+=text[item+counter]
                    counter+=1
                

                # return page_url
                list_file.write(page_url)
                list_file.write('\n')
                page_url = ''

def Extract_links():
    for item in range(len(T_read)):
            if T_read[item][1] == 'v' :
                list_file.write(T_read[item])


def get_data_page(str_text):
    url = str_text
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    Data_Spage = 'p',{'class':'kt-unexpandable-row__value'} #price-price per area-floor -> ppf
    Data_r_a_a = 'span',{'class':'kt-group-row-item__value'} #age - area - rooms -> raa
    Data_loc = 'div',{'class':'kt-page-title__subtitle kt-page-title__subtitle--responsive-sized'} #location
    Data_wge = 'span',{'class':'kt-group-row-item__value kt-body kt-body--stable'} #wge -> warehouse - garage - elevator
    
    
    raa_links = soup.findAll(Data_r_a_a)
    ppf_links = soup.findAll(Data_Spage)
    location_links = soup.findAll(Data_loc)
    wge_links = soup.findAll(Data_wge)


    raa_cleared_text = BeautifulSoup(str(raa_links),'html.parser').get_text()
    ppf_cleared_text = BeautifulSoup(str(ppf_links),'html.parser').get_text() 
    location_cleared_text = BeautifulSoup(str(location_links),'html.parser').get_text() 
    wge_cleared_text = BeautifulSoup(str(wge_links),'html.parser').get_text() 


    return raa_links,raa_cleared_text,ppf_links,ppf_cleared_text,location_links,location_cleared_text,wge_links,wge_cleared_text

   

    list_file.close()
    host.close()
    list_Encoded.close()

def extract_data(text,mode): #This is for Extracing Data from Each Page
    if mode == 'ppf':
        Encoded_text = unidecode(text)
        house_info = []
        temp = ''
        counter = 0
        
        item = 0
        def clean_comma(text):
            new_text = ''
            for i in text:
                if i != ',':
                    new_text+=i
            return new_text     
    
        cleaned_text = clean_comma(text=Encoded_text)
        for item in range(len(cleaned_text)):
            loop_counter = 0
            Latin_NO = ['0','1','2','3','4','5','6','7','8','9']
            if cleaned_text[item] in Latin_NO and cleaned_text[item-1] not in Latin_NO:
                searcher = item
                while cleaned_text[searcher] in ['0','1','2','3','4','5','6','7','8','9']:
                    temp+=cleaned_text[searcher]
                    searcher+=1
                    loop_counter+=1
                house_info.append(temp)
                if len(house_info) >= 2:
                    if 'hmkhf' in cleaned_text:
                        house_info.append('0')
                if len(house_info) >= 3:
                    break
                temp = ''
        return house_info
    elif mode == 'raa':
        temp = ''
        Encoded_text = unidecode(text)
        words = ['mtrj','skht','tq']
        RAA_info = []
        for item in words:
            if item in Encoded_text:
                index = Encoded_text.find(item)
                counter = index + len(item) + 2
                while Encoded_text[counter] != ',':
                    temp+=Encoded_text[counter]
                    counter+=1
                RAA_info.append(temp)
                temp = ''
        return RAA_info
                
    elif mode == 'wge':
        Enc_T = unidecode(text)
        Have_Garage = True
        Have_warehouse = True
        Have_Elevator = True
        if 'prkhyng ndrd' in Enc_T:
            Have_Garage = False
        if 'asnswr ndrd' in Enc_T:
            Have_Elevator = False
        if 'nbry ndrd' in Enc_T:
            Have_warehouse = False
        
        return Have_Garage,Have_warehouse,Have_Elevator
       
def find_loc(text):
    Encoded = unidecode(text)
    index = Encoded.find('|')
    location = ''
    comma_index = 0
    for item in range(index,0,-1):
        if Encoded[item] == ',':
            comma_index = item
            break
    for i in range(comma_index+2,index):
        location+=Encoded[i]
    return location



def get_links(file_name):
    for i in loc_links:
        url = i
        html = urlopen(url)
        soup = BeautifulSoup(html,'html.parser')
        type(soup)
        Data_fpage = 'div',{'class':'post-card-item-_-af972 kt-col-6-_-bee95 kt-col-xxl-4-_-e9d46'} #link
        links = soup.findAll(Data_fpage)
        # for j in soup.find_all('a'):
            # file_name.write(j.get('href'))
        find_link(links)

            
def Clear_files():
    list_file.truncate(0)
    # host.truncate(0)
    list_Encoded.truncate(0)
   
def write_to_file():
    Dataset_list = []
    Total_Dataset = []
    start = time.time()
    for i in range(559,len(Encoded_list)):
        # time.sleep(1)
        print(f'Step {i}th')
        # res = Encode_url(list_url=file_list,mode='online',obj=file_list[i])
        # if str(requests.get(res)) == '<Response [200]>':
        try:
            raa_L,raa_clt,ppf_L,ppf_clt,location_L,location_clt,wge_L,wge_clt = get_data_page(str_text=Encoded_list[i])

            raa = extract_data(text=raa_clt,mode='raa')
            ppf = extract_data(text=ppf_clt,mode='ppf')
            location = find_loc(text=location_clt)
            wge = extract_data(text=wge_clt,mode='wge')
            print(f'Raa = {raa}, ppf = {ppf}, location = {location},wge = {wge}')
            Dataset_list.append(raa[0])
            Dataset_list.append(raa[1])
            Dataset_list.append(raa[2]) 
            Dataset_list.append(ppf[0])
            Dataset_list.append(ppf[1])
            Dataset_list.append(ppf[2])
            Dataset_list.append(location)
            wge = list(wge)
            Dataset_list.append(wge[0])
            Dataset_list.append(wge[1])
            Dataset_list.append(wge[2])
            # Data.write(str(Dataset_list))
            # Data.write('\n')
            T_file.write(str(Dataset_list))
            T_file.write('\n')
            # Total_Dataset.append(Dataset_list)
            Dataset_list = []
        except:
            pass
   
def check_url_response():
    for i in range(len(Encoded_list)):
        print(requests.get(Encoded_list[i]))

def sync_data():
    get_links(file_name=list_file)


# main



try:
    temp_list = []
    for i in Data_r:
        i = i.strip()
        i = ast.literal_eval(i)
        temp_list.append(i)
    
    print(len(temp_list))
    y_label = ['Area','Year','Room','Total Price','PPA','Floor','Location','Garage','WareHouse','Elevator']
    write_csv = csv.writer(Dataset_file)
    write_csv.writerow(y_label)
    write_csv.writerows(temp_list)
    # print(len(Data_r))
    # a = Data_r[3]
    # a_b = a.strip()    
    # print(a_b)
    # a_b = ast.literal_eval(a_b)
    # print('okay')
    # temp_list.append(a_b)
    # print(temp_list)
    # print(a)
except ConnectionError:
    print('no connection found')













Dataset_file.close()
list_file.close()
host.close()
list_Encoded.close()
loc.close()
loc_link.close()

