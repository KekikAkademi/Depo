# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

kullanim =  {
    'kullanim' : [
        'aktuelBim("json_veri")',
        'aktuelBim("json_gorsel")',
        'aktuelBim("gorsel_veri")',
        'aktuelBim("basliklar")'
    ]
}

def aktuelBim(cikti='gorsel_veri'):
    """
    BİM Aktüel Verileri

        Kullanım;

                aktuelBim("json_veri")
                aktuelBim("json_gorsel")
                aktuelBim("gorsel_veri")
                aktuelBim("basliklar")
    """
    
    url = f"https://www.bim.com.tr/default.aspx"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, headers=kimlik, allow_redirects=True)
    corba = BeautifulSoup(istek.text, "lxml")

    sozluk = {}

    tarih = corba.find('a', class_='active subButton').text.strip()
    urun_alani = corba.find('div', class_='productArea')

    urun_rerero = []
    for urun in urun_alani.findAll('div', class_='inner'):
        host = 'https://www.bim.com.tr'
        try:
            urun_basligi = urun.find('h2', class_='title').text.strip()
            urun_linki = host + urun.a['href']
            urun_gorseli = host + urun.img['src'].replace(' ', '%20')
            urun_fiyati = urun.find('a', class_='gButton triangle').text.strip()

            urun_rerero.append({
                "urun_baslik": urun_basligi,
                "urun_link" : urun_linki,
                "urun_gorsel" : urun_gorseli,
                "urun_fiyat" : urun_fiyati
            })
        except:
            pass
    

    sozluk.update({
        'tarih' : tarih
    })
    sozluk.update({
        'urunler' : urun_rerero
    })

    basliklar = [anahtar for anahtar in sozluk['urunler'][0].keys()]

    if cikti == 'json_veri':
        return sozluk
    
    elif cikti == 'json_gorsel':
        return json.dumps(sozluk, indent=2, sort_keys=False, ensure_ascii=False)
    
    elif cikti == 'gorsel_veri':
        return tabulate(sozluk['urunler'], headers='keys', tablefmt='psql')
    
    elif cikti == 'basliklar':
        return basliklar
    
    else:
        return kullanim

# print(aktuelBim("json_veri"))

# print(aktuelBim("json_gorsel"))

# print(aktuelBim("gorsel_veri"))

# print(aktuelBim("basliklar"))

# print(aktuelBim("alakasız bişi"))