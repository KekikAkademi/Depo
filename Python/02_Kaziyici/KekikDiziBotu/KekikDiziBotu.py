#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------------------------------------------------------------------------#
import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş
#---------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#
link = "https://www.dizibox.pw/sitemap-tax-diziler.xml"
# Gerçek Bir Tarayıcı Olmamız Lazım!
kimlik = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
istek = requests.get(link, headers=kimlik)          # link'e kimlik bilgimizle istek gönderiyoruz
soup = BeautifulSoup(istek.text, "html5lib")        # Gelen veriyi html5lib ile ayrıştırmaya başlıyoruz
#----------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------#
#print(istek)                    # <Response [200]>
#print(soup)                     # Kaynak Kodlar
#print(soup.find('loc'))         # Kaynak Kodundaki <loc>
#print(soup.findAll('loc'))      # Kaynak Kodundaki <loc>'lar
#-------------------------------------------------------------#

for dizi_adresleri in soup.findAll('loc'):                              # Örümceğimizi Başlattık!
    diziLink = dizi_adresleri.text                                      # Crawl ettiğimiz linkler = Dizi Linkleri
                                                                        # Bu linklerin içine girelim
    dizi_istek = requests.get(dizi_adresleri.text, headers=kimlik)      # Her gelen link'e istek atıyorz
    dizi_icerik = BeautifulSoup(dizi_istek.text, "html5lib")            # html5lib ile parse ediyoruz

    diziAdi = dizi_icerik.title.text.replace(" izle | DiziBOX","")      # Bulunduğumuz Sayfa Başlığı
    diziAciklama = dizi_icerik.find("div", attrs={'class': 'tv-story'}).find("p").text  # tam olarak dediğimiz şu;
                                                                                        # "dizi_icerik" ile gelen html içerisindeki
                                                                                        # <div class='tv-story'> içerisindeki
                                                                                        # <p> öğesinin yazısını al"

    diziBilgi = dizi_icerik.find("div", attrs={"class" : "terms text-muted-dark text-overflow"})
    diziUlke = diziBilgi.find("a", attrs={"rel": "tag"}).text
    diziTuru = diziBilgi.text.replace("\xa0","").split("|")[2]

    #-------------------------------#
    # Her yeni Şeyi Deneme Alanımız
    #print(diziUlke)
    #-------------------------------#

    print(f'\n{diziAdi}\n\t\t\t{diziUlke} | {diziTuru}\n\t{diziAciklama}\n{diziLink}\n\n')

    #break                                                               # Döngüyü Kır > Linklerin Hepsini Tarama!


def DiziUlkesiFantezi():
    diziBilgi = []
    for diziData in dizi_icerik.findAll("a", attrs={"rel": "tag"}):
        diziBilgi.append(diziData.text)
    a = ''.join(map(str, diziBilgi[1]))[0]
    if a != '2':
        diziUlkesi = ', '.join(map(str, diziBilgi[:2]))
        print(diziUlkesi)
    elif a == '1':
        diziUlkesi = ', '.join(map(str, diziBilgi[:1]))
        print(diziUlkesi)
    else:
        diziUlkesi = ', '.join(map(str, diziBilgi[:1]))
        print(diziUlkesi)