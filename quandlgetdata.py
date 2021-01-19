# import needed libraries
import quandl
import numpy as ny
import pandas as pd
import requests
import re
import csv
from numpy import loadtxt
from bs4 import BeautifulSoup
from pandas_datareader import data

# add quandl API key for unrestricted
quandl.ApiConfig.api_key = 'shAvzzwDvkzzDq93Kzyy'
QUANDL_API_KEY= 'shAvzzwDvkzzDq93Kzyy'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

#data = quandl.get('WIKI/AAPL')
#cleartickers = ['XJPX/13760','XOP','IBM']
tickers = loadtxt("tickerlist.csv", dtype=str, comments="#", delimiter=",", unpack=False)

for stock in tickers:
    print(stock)
    data = quandl.get_table('WIKI/PRICES', ticker=stock, 
                        qopts = { 'columns': ['ticker', 'date', 'open', 'close'] }, 
                        date = { 'gte': '2018-01-01', 'lte': '2018-04-16' }, 
                        paginate=True)
    csvfilename = stock + '.csv'
    data.to_csv(csvfilename)
    data.head()


#Extrace holdings from etf into file
ETFtickers = loadtxt("etflist.csv", dtype=str, comments="#", delimiter=",", unpack=False)

#keys = ["XLU","XLRE"] #list of tickers whose financial data needs to be extracted
#financial_dir = {}


#keys = ['XLU', 'XLRE']
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
}

def main(url):
    with requests.Session() as req:
        req.headers.update(headers)
        for key in ETFtickers:
            r = req.get(url.format(key))
            print(f"Extracting: {r.url}")
            goal = re.findall(r'etf\\\/(.*?)\\', r.text)
            print(goal)
           # filename=r.text+'.csv'
           # r.to_csv(filename)

main("https://www.zacks.com/funds/etf/{}/holding")