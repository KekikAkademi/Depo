# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#-------------------------------#
import requests                 #
from bs4 import BeautifulSoup   #
#-------------------------------#

def ECZANE(il,ilce):
    link = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(link, headers=kimlik)
    soup = BeautifulSoup(istek.text, "html5lib")

    #------------------------------------------------------#
    #print(istek)              # <Response [200]>
    #print(soup)               # Kaynak Kodlar
    #print(soup.title.text)    # Kaynak Kodu Sayfa Başlığı
    #------------------------------------------------------#

    eczane_adi = []
    eczane_adresi = []
    eczane_telefonu = []

    for table in soup.findAll("table", attrs={"class": "table table-striped mt-2"}):
        for ad in table.findAll("td", attrs={"style": "width:20%"}):
            eczane_adi.append(ad.text)
        for adres in table.findAll("td", attrs={"style": "width:50%"}):
            eczane_adresi.append(adres.text)
        for telefon in table.findAll("td", attrs={"style": "width:30%"}):
            eczane_telefonu.append(telefon.text)

    liste = []
    for adet in range(0, len(eczane_adi)):
        sozluk = {}
        sozluk['eczane_adi'] = eczane_adi[adet]
        sozluk['eczane_adresi'] = eczane_adresi[adet]
        sozluk['eczane_telefonu'] = eczane_telefonu[adet]
        liste.append(sozluk)

    #print(liste)
    return liste

#ECZANE("canakkale","merkez")