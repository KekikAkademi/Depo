# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

class NobetciEczane(object):
    """
    NobetciEczane : eczaneler.gen.tr adresinden nöbetçi eczane verilerini hazır formatlarda elinize verir.

    Öz Nitelikler
    -------------
        il (str): Nöbetçi Eczane Bilgisi istenilen il
        ilce (str): Nöbetçi Eczane Bilgisi istenilen ilçe

    Methodlar
    ----------
        .veri()         -> list:
            json verisi döndürür.

        .gorsel()       -> str:
            oluşan json verisini insanın okuyabileceği formatta döndürür.

        .tablo()        -> str:
            tabulate verisi döndürür.

        .anahtarlar()   -> list:
            kullanılan anahtar listesini döndürür.
    """
    def __init__(self, il:str, ilce:str):
        super().__init__()

        il      = il.replace('İ', "i").lower()
        ilce    = ilce.lower()

        tr2eng  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
        il      = il.translate(tr2eng)
        ilce    = ilce.translate(tr2eng)

        kaynak  = "eczaneler.gen.tr" 
        url     = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
        kimlik  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        istek   = requests.get(url, headers=kimlik)

        corba = BeautifulSoup(istek.content, "lxml")
        bugun = corba.find('div', id='nav-bugun')

        json = {"kaynak": kaynak, 'veri' : []}
        try:
            for bak in bugun.findAll('tr')[1:]:
                ad    = bak.find('span', class_='isim').text
                mah   = None if bak.find('div', class_='my-2') == None else bak.find('div', class_='my-2').text
                adres = bak.find('span', class_='text-capitalize').text
                tarif = None if bak.find('span', class_='text-secondary font-italic') == None else bak.find('span', class_='text-secondary font-italic').text
                telf  = bak.find('div', class_='col-lg-3 py-lg-2').text

                json['veri'].append({
                    'ad'        : ad,
                    'mahalle'   : mah,
                    'adres'     : adres,
                    'tarif'     : tarif,
                    'telefon'   : telf
                })
        except AttributeError:
            pass

        self.json  = json if json['veri'] != [] else None

    def veri(self):
        "json verisi döndürür."
        return self.json or None

    def gorsel(self):
        "oluşan json verisini insanın okuyabileceği formatta döndürür."
        return json.dumps(self.json, indent=2, sort_keys=False, ensure_ascii=False) if self.json else None

    def tablo(self):
        "tabulate verisi döndürür."
        return tabulate(self.json['veri'], headers='keys', tablefmt='psql') if self.json else None

    def anahtarlar(self):
        "kullanılan anahtar listesini döndürür."
        return [anahtar for anahtar in self.json['veri'][0].keys()] if self.json else None

#bakalim = NobetciEczane("İstanbul", "Beylikdüzü")

#print(bakalim.json)
#print(bakalim.veri())
#print(bakalim.gorsel())
#print(bakalim.tablo())
#print(bakalim.anahtarlar())

#----------------------------------------------------------------------------------------------------#

# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

kullanim =  {
    'kullanim' : [
        'nobetciEczane("canakkale", "merkez", "json_veri")',
        'nobetciEczane("canakkale", "merkez", "json_gorsel")',
        'nobetciEczane("canakkale", "merkez", "gorsel_veri")',
        'nobetciEczane("canakkale", "merkez", "basliklar")'
    ]
}

def nobetciEczane(il=None, ilce=None, cikti='gorsel_veri'):
    """
    eczaneler.gen.tr Nöbetçi Eczane Verileri

        Kullanım;

                nobetciEczane("canakkale", "merkez", "json_veri")
                nobetciEczane("canakkale", "merkez", "json_gorsel")
                nobetciEczane("canakkale", "merkez", "gorsel_veri")
                nobetciEczane("canakkale", "merkez", "basliklar")
    """

    il = il.lower()
    try:
        ilce = ilce.lower()
    except AttributeError:
        return kullanim

    tr2eng = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
    il = il.translate(tr2eng)
    ilce = ilce.translate(tr2eng)

    url = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    istek = requests.get(url, headers=kimlik)
    # print(istek)
    # print(istek.headers)
    
    corba = BeautifulSoup(istek.content, "lxml")
    
    eczane_adi = []
    eczane_adresi = []
    eczane_telefonu = []

    for tablo in corba.find('table', class_='table table-striped mt-2'):
        for ad in tablo.findAll('span', class_='isim'):
            eczane_adi.append(ad.text)

        for adres in tablo.findAll('span', class_='text-capitalize'):
            eczane_adresi.append(adres.text)

        for telefon in tablo.findAll('div', class_='col-lg-3 py-lg-2'):
            eczane_telefonu.append(telefon.text)
        
    liste = []
    for adet in range(0, len(eczane_adi)):
        sozluk = {}
        sozluk['eczane_adi'] = eczane_adi[adet]
        sozluk['eczane_adresi'] = eczane_adresi[adet]
        sozluk['eczane_telefonu'] = eczane_telefonu[adet]
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

# print(nobetciEczane("canakkale", "merkez", "json_veri"))

# print(nobetciEczane("canakkale", "merkez", "json_gorsel"))

# print(nobetciEczane("canakkale", "merkez", "gorsel_veri"))

# print(nobetciEczane("canakkale", "merkez", "basliklar"))

# print(nobetciEczane("alakasız bişi"))
