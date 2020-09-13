#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş
from tqdm import tqdm           # ProgressBar oluşturan arkadaşımız

link = "https://www.dizibox.pw/sitemap-tax-diziler.xml"
kimlik = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)'}
istek = requests.get(link, headers=kimlik)
soup = BeautifulSoup(istek.text, "html5lib")

for dizi_adresleri in tqdm(soup.findAll('loc')):
    dizi_istek = requests.get(dizi_adresleri.text, headers=kimlik)
    dizi_icerik = BeautifulSoup(dizi_istek.text, "html5lib")

    diziLink = dizi_adresleri.text
    diziAdi = dizi_icerik.title.text.replace(" izle | DiziBOX","")
    diziAciklama = dizi_icerik.find("div", attrs={'class': 'tv-story'}).find("p").text
    diziBilgi = dizi_icerik.find("div", attrs={"class" : "terms text-muted-dark text-overflow"})
    diziUlke = diziBilgi.find("a", attrs={"rel": "tag"}).text
    diziTuru = diziBilgi.text.replace("\xa0","").split("|")[2]
    
    print(f'\n{diziAdi}\n\t\t\t{diziUlke} | {diziTuru}\n\t{diziAciklama}\n{diziLink}\n\n')