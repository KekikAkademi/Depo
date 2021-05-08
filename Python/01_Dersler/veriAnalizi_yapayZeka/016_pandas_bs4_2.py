import pandas as pd
from bs4 import BeautifulSoup
import requests

istek = requests.get('https://gcoins.net/en/catalog/view/104977')
corba = BeautifulSoup(istek.content, "lxml")
tablo = corba.find('table', class_='subs noBorders evenRows')
tabloSatir = tablo.find_all('tr')

sonuc = []
for tr in tabloSatir:
    td = tr.find_all('td')
    satir = [tr.text.strip() for tr in td if tr.text.strip()]
    if satir: sonuc.append(satir)


dataFrame = pd.DataFrame(sonuc, columns=["Sene", "Basılan Para", "Kalite", "Paranın Değeri"])
print(dataFrame)

from tabulate import tabulate
print( tabulate(dataFrame, headers='keys', tablefmt='psql') )