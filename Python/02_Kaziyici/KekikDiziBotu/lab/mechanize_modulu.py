#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import mechanize
from bs4 import BeautifulSoup

link = "https://www.dizibox.pw/sitemap-tax-diziler.xml"

tarayici = mechanize.Browser()                              # Tarayıcı Tanımlıyoruz
# Kimlik Bilgimizi Tanımlıyoruz
tarayici.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)')]
tarayici.set_handle_robots(False)                           # Robots.txt Engeline Takılma!
tarayici.open(link)                                         # Link'i Tarayıcıda Aç

response = tarayici.response()
pars = response.read()
#print(pars)                            # b'<?xml version="1.0"
soup = BeautifulSoup(pars, "html5lib")

"""for linkler in soup.find_all('loc'):
    print(linkler.text)"""
#----------------------------------------------------------------------------------------------------------------------#
from tqdm import tqdm

for dizi_adresleri in tqdm(soup.findAll('loc')):                                              # Örümceğimizi Başlattık!
    # demin aldığımız linklerin içine giricez;
    dizi = mechanize.Browser()  # Tarayıcı Tanımlıyoruz
    # Kimlik Bilgimizi Tanımlıyoruz
    dizi.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)')]
    dizi.set_handle_robots(False)  # Robots.txt Engeline Takılma!
    dizi.open(dizi_adresleri.text)  # Link'i Tarayıcıda Aç

    site_yaniti = dizi.response()
    yanit = site_yaniti.read()
    dizi_icerik = BeautifulSoup(yanit, "html5lib")

    diziLink = dizi_adresleri.text                                                      # sitemap'i crawl ettik
    diziAdi = dizi_icerik.title.text.replace(" izle | DiziBOX","")                      # sayfa başlığını scrape ettik

    diziAciklama = dizi_icerik.find("div", attrs={'class': 'tv-story'}).find("p").text  # tam olarak dediğimiz şu;
                                                                                        # "dizi_icerik'ten gelen html içerisindeki
                                                                                        # <div class='tv-story'> içerisindeki
                                                                                        # <p> öğesinin yazısını al" dedik

    diziBilgi = dizi_icerik.find("div", attrs={"class" : "terms text-muted-dark text-overflow"})
    diziUlke = diziBilgi.find("a", attrs={"rel": "tag"}).text
    diziTuru = diziBilgi.text.replace("\xa0","").split("|")[2]

    #-------------------------------#
    # Her yeni Şeyi Deneme Alanımız
    #print(diziTuru)
    #-------------------------------#

    # Ana Çıktı Alanımız
    def Veri():
        print(f'\n{diziAdi}\n\t\t\t{diziUlke} | {diziTuru}\n\t{diziAciklama}\n{diziLink}\n\n')

    Veri()