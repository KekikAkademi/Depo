# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

import requests, json
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

kullanim =  {
    'kullanim' : [
        'dovizVerileri("json_veri")',
        'dovizVerileri("json", "USD")',
        'dovizVerileri("json_gorsel")',
        'dovizVerileri("gorsel_veri")',
        'dovizVerileri("basliklar")'
    ]
}

def dovizVerileri(cikti='gorsel_veri', birim=None):
    """
    altinkaynak.com Döviz Verileri

        Kullanım;

                dovizVerileri("json_veri")
                dovizVerileri("json", "USD")
                dovizVerileri("json_gorsel")
                dovizVerileri("gorsel_veri")
                dovizVerileri("basliklar")
    """
    
    url = "http://www.altinkaynak.com/Doviz/Kur/Guncel"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    istek = requests.get(url, headers=kimlik)
    corba = BeautifulSoup(istek.content, 'lxml')
    tablo = corba.find('table', class_='table')

    pandaVeri = pd.read_html(str(tablo))[0].rename(
        columns={
            'Unnamed: 0'    : 'Birim',
            'Unnamed: 1'    : 'sil',
            'Unnamed: 5'    : 'sil',
            '₺ ₺'           : 'sil',
        }
    ).drop(columns = 'sil').dropna().reset_index(drop = True)

    for say in range(len(pandaVeri['Birim'])):
        pandaVeri['Birim'][say] = pandaVeri['Birim'][say][-3:]

    # print(pandaVeri)

    jsonVeri = json.loads(pandaVeri.to_json(orient='records'))
    # print(jsonVeri)

    if cikti == 'json_veri':
        return json.loads(pandaVeri.to_json(orient='records'))
    
    elif cikti == 'json_gorsel':
        return json.dumps(jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
    
    elif cikti == 'json' and birim != None:
        birim = birim.upper()

        for bul in range(len(jsonVeri)):
            if jsonVeri[bul]['Birim'] == birim:
                return jsonVeri[bul]
    
    elif cikti == 'basliklar':
        return [anahtar for anahtar in jsonVeri[0].keys()]
    
    elif cikti == 'gorsel_veri':
        return tabulate(pandaVeri, headers='keys', tablefmt='psql')
    
    else:
        return kullanim

# print(dovizVerileri("json_veri"))

# print(dovizVerileri("json", "USD"))

# print(dovizVerileri("json_gorsel"))

# print(dovizVerileri("gorsel_veri"))

# print(dovizVerileri("basliklar"))

# print(dovizVerileri("alakasız bişi"))