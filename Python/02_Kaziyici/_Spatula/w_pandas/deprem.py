# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

kullanim =  {
    'kullanim' : [
        'depremVerileri("json_veri")',
        'depremVerileri("json_gorsel")',
        'depremVerileri("gorsel_veri")',
        'depremVerileri("basliklar")'
    ]
}

def depremVerileri(cikti='gorsel_veri'):
    """
    afet.gen.tr Son Depremler Verisi

        Kullanım;

                depremVerileri("json_veri")
                depremVerileri("json_gorsel")
                depremVerileri("gorsel_veri")
                depremVerileri("basliklar")
    """
    
    url = "http://www.afet.gen.tr/son-depremler.php"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    istek = requests.get(url, headers=kimlik)
    corba = BeautifulSoup(istek.content, 'lxml')
    tablo = corba.find('table', width="100%")

    pandaVeri = pd.read_html(str(tablo))[0].rename(
        columns={
            0   : 'Tarih',
            1   : 'Saat',
            2   : 'Enlem(N)',
            3   : 'Boylam(E)',
            4   : 'Derinlik(km)',
            5   : 'MD',
            6   : 'ML',
            7   : 'MS',
            8   : 'Yer'
        }
    ).drop([0], axis=0).reset_index(drop = True)

    jsonVeri = json.loads(pandaVeri.to_json(orient='records'))
    # print(jsonVeri)

    if cikti == 'json_veri':
        return json.loads(pandaVeri.to_json(orient='records'))
    
    elif cikti == 'json_gorsel':
        return json.dumps(jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
    
    elif cikti == 'basliklar':
        return [anahtar for anahtar in jsonVeri[0].keys()]
    
    elif cikti == 'gorsel_veri':
        return tabulate(pandaVeri, headers='keys', tablefmt='psql')
    
    else:
        return kullanim

# print(depremVerileri("json_veri"))

# print(depremVerileri("json_gorsel"))

# print(depremVerileri("gorsel_veri"))

# print(depremVerileri("basliklar"))

# print(depremVerileri("alakasız bişi"))