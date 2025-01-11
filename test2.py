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

os.system('cls')
list_location = ['10 dy','17 shhrywr','abkhwh','azdshhr','ayt llh khmnhy','ayt llh `bdy,bwdhr','bwTlb','Hmdabd','rshd','rwnd','qbl','lhyh','mm khmyny','mm rD,myrabd','myryh','nSr','nqlb','ythr','ythrgrn','ymn','ywn','bG mlkhabd','bhnr','bll','blwr tws','blwr sjd','bhrn','bhrstn','bhshty','bhmn','prdys','prwyn `tSmy','pnj tn al `b','tlgrd','thmn','jnbz','jnt','chhrbG','chhnw','Hjt','Hrm mThr','Hsynabd','khwjh rby`','dnsh','dnshjw','dnshgh frdwsy mshhd','drwy','dhnwy','rh ahn','rhnmyy','rbT Trq','rslt','rDshhr','rDyyh','spd','stry','sjdyh','s`dy','slm','smrqnd','snbd','syd rDy','sydy','sysabd','shf','shhrar','shhrkh bwdhr','shhrkh shhyd rjyy','shhrkh shyryn','shhrkh Tlqny','shhyd awyny','shhyd qrbny','shhyd mThry shmly','shhyd m`qwl','shhyd hnrwr','shyrwdy','Sdf','Syd shyrzy','Tbrsy','Tbrsy shmly','Trq','`ml','`bsabd','`bdlmTlb','`sgryh','`nSry','`ydgh','frG ltHSyln','fTmyh','fdkh','frmrz `bsy','frwdgh','frhng','flkhh brq (mydn bsyj)','flkhh Dd (15 khrdd)','qsmabd (shhrkh Grb)','khrgrn','khrmndn wl','khrmndn dwm','khshmr','pwrsyn','khshwrz','khlhdwz','flsTyn','khwshsh','khwh sngy','khwy myrlmwmnyn','khwy plys','khwy mhdy','gz','glshwr','gwhrshd','mjd','mHlh myrlmwmnyn','mHlh bl khybn','mHlh pyyn khybn','mHlh pnj tn','mHlh jhdshhr','mHlh chhrchshmh','mHlh rdh','mHlh srfrzn','mHlh Tlb','mHlh khwthr','mHlh nn rDwy','mHlh nyrw hwyy','mHlh wHyd','mHlh hnrstn','mHmdabd','mSTfy khmyny','mSly','mThry jnwby','mqdm','mwswy qwchny','mw`wd','mhdy abd','mhrabd','mydn `dl khmyny','nmyshgh byn lmlly mshhd','nwGn','nwfl lwshtw','nyzh','wkhylabd','wly`Sr','hshmynjd','hshmyh','hft tyr','','','','']
print(len(list_location))
loc_file = open('loc_link.txt',mode='r+',encoding='utf-8')
loc_eq = open('loc_eq.txt',mode='r+',encoding='utf-8')

loc_file_read = loc_file.readlines()
name = ''
index = 0

simple = ['https://divar.ir/s/mashhad/buy-apartment/10-day','https://divar.ir/s/mashhad/buy-apartment/17-shahrivar']
locations_dict = dict()

counter = 0
for i in loc_file_read:
    for j in range(len(i)-1,0,-1):
        if i[j] == '/':
            index = j
            break
    for k in range(j+1,len(i)):
        name+=i[k]
    locations_dict[list_location[counter]]=[name]
    # print(locations_dict)
    counter+=1
    name = ''
        
print(locations_dict)

loc_eq.write(str(locations_dict))



