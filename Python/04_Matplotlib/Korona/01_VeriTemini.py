import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import json

istek = requests.get("https://www.worldometers.info/coronavirus/")
corba = BeautifulSoup(istek.content, 'lxml')
tablo = corba.find('table', id='main_table_countries_today')

pandaVeri = pd.read_html(str(tablo))[0].rename(
    columns={
        'Country,Other'     : 'Ülkeler',
        'TotalCases'        : 'Toplam Vaka',
        'NewCases'          : 'Yeni Vaka',
        'TotalDeaths'       : 'Toplam Ölüm',
        'NewDeaths'         : 'Yeni Ölüm',
        'TotalRecovered'    : 'Toplam Taburcu',
        'ActiveCases'       : 'Aktif Vaka',
        'Serious,Critical'  : 'Kritik Vaka',
        'Tot Cases/1M pop'  : 'Vaka/Nüfus Oranı',
        'Deaths/1M pop'     : 'Ölüm/Nüfus Oranı',
        'TotalTests'        : 'Toplam Test',
        'Tests/ 1M pop'     : 'Test/Nüfus Oranı'
    }
)

jsonVeri = json.loads(pandaVeri.to_json(orient='records'))
#print(jsonVeri)

jsonCikti = json.dumps(jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
#print(jsonCikti)

gorselVeri = tabulate(pandaVeri, headers='keys', tablefmt='github')
print(gorselVeri)
with open("GorselVeri.md", "w+") as dosya : dosya.write(gorselVeri)

anahtarlar = [anahtar for anahtar in jsonVeri[0].keys()]
#print(anahtarlar)