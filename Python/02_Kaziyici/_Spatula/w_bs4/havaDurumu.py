# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

kullanim =  {
    'kullanim' : [
        'hava_Durum("Çanakkale", "Merkez", "json_veri")',
        'hava_Durum("Çanakkale", "Merkez", "json_gorsel")',
        'hava_Durum("Çanakkale", "Merkez", "gorsel_veri")',
        'hava_Durum("Çanakkale", "Merkez", "basliklar")'
    ]
}

def hava_Durum(il=None, ilce=None, cikti='gorsel_veri'):
    """
    eczaneler.gen.tr Nöbetçi Eczane Verileri

        Kullanım;

                hava_Durum("Çanakkale", "Merkez", "json_veri")
                hava_Durum("Çanakkale", "Merkez", "json_gorsel")
                hava_Durum("Çanakkale", "Merkez", "gorsel_veri")
                hava_Durum("Çanakkale", "Merkez", "basliklar")
    """

    url = f"https://www.google.com/search?&q={il}+{ilce}+hava+durumu" + "&lr=lang_tr&hl=tr"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, "lxml")

    gun_durum = corba.findAll('div', class_='BNeawe')
    gun, durum = gun_durum[3].text.strip().split('\n')
    derece = corba.find('div', class_='BNeawe').text

    liste = []
    sozluk = {
        'sehir'     : il.capitalize() + ' ' + ilce.capitalize(),
        'gun'       : gun,
        'derece'    : f'{durum} {derece}',
    }

    liste.append(sozluk)

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

# print(hava_Durum("Çanakkale", "Merkez", "json_veri"))

# print(hava_Durum("Çanakkale", "Merkez", "json_gorsel"))

# print(hava_Durum("Çanakkale", "Merkez", "gorsel_veri"))

# print(hava_Durum("Çanakkale", "Merkez", "basliklar"))

# print(hava_Durum("alakasız bişi"))