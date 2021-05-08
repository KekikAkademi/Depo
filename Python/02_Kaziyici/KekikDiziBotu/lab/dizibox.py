#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş

"""
Biz robot,bot,örümcek tasarlamaya çalışıyoruz,
bunun için websitesini index'den taramaya başlamak yerine sitemap'den taramaya başlamalıyız
çünkü orası robotlar için oluşturulan bir yer :)
"""

link = "https://www.dizibox.pw/sitemap-tax-diziler.xml"
# Gerçek Bir Tarayıcı Olmamız Lazım!
kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)'}
istek = requests.get(link, headers=kimlik)          # Link'e kimlik bilgimizle istek gönderiyor ve gelen veriyi tutuyoruz
soup = BeautifulSoup(istek.text, "html5lib")        # Gelen veriyi html5lib ile ayrıştırmaya başlıyoruz

#-----------------------#
# Bakalım Neyimiz Var?
"""
print(soup)
"""
# Güzel
#-----------------------#

#----------------------------#
# Deneme 1
"""
print(soup.findAll('loc'))
"""
# Harika
#----------------------------#

#--------------------------------------------------------------------------------------#
# findAll > for döngüsü kullanarak yineleyebileceğiniz bir ResultSet nesnesi döndürür.
"""
for gelenlink in soup.findAll('loc'):
    print(gelenlink.text)
"""
# Bakın Ayıkladık :)
#--------------------------------------------------------------------------------------#

"""
https://www.dizibox.pw/freud-1-sezon-1-bolum-izle/5/ > içerisinde

https://odnoklassniki.ru/videoembed/1795922332305 > linki var


aldığın kaynaktan | <a olanları ve href="../odnoklassniki.ru/videoembed/" olan linkleri tut;

.findAll('a', attrs={'href': re.compile("^https://odnoklassniki.ru/videoembed/")})
"""

#--------------------------------------------------------------------------------------#
# Hadi Yardıralım

from tqdm import tqdm

for dizi_adresleri in tqdm(soup.findAll('loc')):                                              # Örümceğimizi Başlattık!
    # demin aldığımız linklerin içine giricez;
    dizi_istek = requests.get(dizi_adresleri.text, headers=kimlik)                      # sitemap'den aldığımız her linke ayrı istek atıyoruz
    dizi_icerik = BeautifulSoup(dizi_istek.text, "html5lib")                            # html5lib ile parse ediyoruz

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