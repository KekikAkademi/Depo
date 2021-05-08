# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

kullanim =  {
    'kullanim' : [
        'akaryakitFiyat("json_veri")',
        'akaryakitFiyat("json_gorsel")',
        'akaryakitFiyat("gorsel_veri")',
        'akaryakitFiyat("basliklar")'
    ]
}

def akaryakitFiyat(cikti='gorsel_veri'):
    """
    finans.haberler.com Akaryakıt Verileri

        Kullanım;

                akaryakitFiyat("json_veri")
                akaryakitFiyat("json_gorsel")
                akaryakitFiyat("gorsel_veri")
                akaryakitFiyat("basliklar")
    """
    
    url = f"https://finans.haberler.com/akaryakit/"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, headers=kimlik)
    corba = BeautifulSoup(istek.text, "lxml")

    # son_guncellenme = corba.select('body > div > div.hbMain.stickyNo > div:nth-child(3) > div > div.col696 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')[0].text
    
    cerceve = corba.find('div', class_='hbTableContent piyasa')

    tur = cerceve.findAll('td', {'width' : '50%'})
    fiyat = cerceve.findAll('td', {'width' : '16%'})

    liste = []
    
    for adet in range(len(tur)):
        liste.append(
            {
            "turu" : tur[adet].text.replace(' TL', ' -- ₺'),
            "fiyati" : fiyat[adet].text.replace('TL', '₺')
            }
        )

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

# print(akaryakitFiyat("json_veri"))

# print(akaryakitFiyat("json_gorsel"))

# print(akaryakitFiyat("gorsel_veri"))

# print(akaryakitFiyat("basliklar"))

# print(akaryakitFiyat("alakasız bişi"))