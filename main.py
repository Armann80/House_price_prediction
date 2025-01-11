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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import mean_squared_error
from sklearn import datasets
import csv
import tkinter as tk


def Model():
    os.system('cls')
    Dataset_file = open('Dataset.csv',mode='r+',encoding='utf-8')
    ordinal_encoder = OrdinalEncoder()


    Data = pd.read_csv('Dataset.csv')
    Data.drop(labels='Total Price',axis=1,inplace=True)


    house_loc = Data[['Location']]
    house_loc_enc = ordinal_encoder.fit_transform(house_loc)


    # Data['Garage'] = Data['Garage'].astype(int)
    # Data['WareHouse'] = Data['WareHouse'].astype(int)
    # Data['Elevator'] = Data['Elevator'].astype(int)


    Data['Garage'].replace([True,False],[1,0],inplace=True)
    Data['WareHouse'].replace([True,False],[1,0],inplace=True)
    Data['Elevator'].replace([True,False],[1,0],inplace=True)


    # print(corr_mat['PPA'].sort_values(ascending=False))


    Data['Location'] = house_loc_enc
    Data.drop('Floor',axis=1,inplace=True)
    # Data['Floor'] = Data['Floor'].map(lambda x: x.lstrip('+-').rstrip('aAbBcCdefghijklomnpqrstuvwxyz'))
    Data = Data.dropna()
    x = Data.drop('PPA',axis=1)
    y = Data.PPA


    print(x)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,shuffle=True)



    lr = LinearRegression()
    lr.fit(x_train,y_train)

    my_simple = np.array([150,1397,3,4,1,1,1])
    my_simple2 = np.array([[150],[1397],[3],[4],[1],[1],[1]])
    my_simple3 = np.array([[150,1397,3,4,1,1,1]])
    my_simple = my_simple.reshape(1,-1)
    # my_simple2 = my_simple.reshape(-1,1)
    # my_simple3 = my_simple.reshape(-1,1)

    print(my_simple)
    lr_p = lr.predict(my_simple)
    # lr_sc = lr.score(x_test,y_test)
    # mse = mean_squared_error (y_test,y_pred=lr_p)
    print(lr_p)

    # plt.scatter(x_train,y_train)
    # print(mse)
    # print(Data)



Model()
# boston = datasets.load_boston()
# boston_pd = pd.DataFrame(data=boston)
# x = boston_pd.data
# y = boston_pd.target


# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,shuffle=True)
# reg = LinearRegression()
# reg.fit(x_train,y_train)

# y_predicit = reg.predict(x_test)

# sc = reg.score(x_test,y_predicit)

# print(sc)



# att = ['Area','Year','Room','PPA','Floor','Garage','WareHouse','Elevator']

# print(x)

