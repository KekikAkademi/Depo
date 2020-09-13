import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

istek = requests.get("https://www.worldometers.info/coronavirus/")
corba = BeautifulSoup(istek.content, 'lxml')
tablo = corba.find_all('table')[0]

dataFrame = pd.read_html(str(tablo))
print( tabulate(dataFrame[0], headers='keys', tablefmt='psql') )

#---------------------------------------------------------------------------------------#

from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')

# get html using selenium webdriver, supports javascript
tarayici = webdriver.PhantomJS("/home/keyiflerolsun/phantomjs/bin/phantomjs")
tarayici.get( "https://azure.microsoft.com/tr-tr/pricing/details/storage/blobs/" )
kaynakKodu = tarayici.page_source

# parse
corba = BeautifulSoup(kaynakKodu,'lxml')

tablo = corba.find_all('table')[0]
dataFrame = pd.read_html(str(tablo))
print( tabulate(dataFrame[0], headers='keys', tablefmt='pretty') )