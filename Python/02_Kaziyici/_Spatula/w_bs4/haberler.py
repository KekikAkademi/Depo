# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

kullanim =  {
    'kullanim' : [
        'sonDakika("json_veri")',
        'sonDakika("json_gorsel")',
        'sonDakika("gorsel_veri")',
        'sonDakika("basliklar")'
    ]
}

def sonDakika(cikti='gorsel_veri'):
    """
    ntv.com.tr Son Dakika Verileri

        Kullanım;

                sonDakika("json_veri")
                sonDakika("json_gorsel")
                sonDakika("gorsel_veri")
                sonDakika("basliklar")
    """
    
    url = "https://www.ntv.com.tr/son-dakika"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, headers=kimlik)
    corba = BeautifulSoup(istek.text, "lxml")

    liste = []

    for table in corba.findAll("ul", class_="gallery-page-video-list-items"):
        # print(table)
        # print(table.tr.text)
        haberManset = table.findAll("div", class_="card card--md")

        for adet in range(len(haberManset)):
            liste.append({
                "Haber" : haberManset[adet].p.text.replace('SON DAKİKA HABERİ:','').replace(' | Son depremler','').replace('SON DAKİKA: ', '').strip(),
                "Link" : "https://www.ntv.com.tr" + haberManset[adet].a['href']
            })

    basliklar = [anahtar for anahtar in liste[0].keys()]

    if cikti == 'json_veri':
        return liste
    
    elif cikti == 'json_gorsel':
        return json.dumps(liste, indent=2, sort_keys=False, ensure_ascii=False)
    
    elif cikti == 'gorsel_veri':
        return tabulate(liste, headers='keys', tablefmt='psql')
    
    elif cikti == 'basliklar':
        return basliklar
    
    else:
        return kullanim

# print(sonDakika("json_veri"))

# print(sonDakika("json_gorsel"))

# print(sonDakika("gorsel_veri"))

# print(sonDakika("basliklar"))

# print(sonDakika("alakasız bişi"))