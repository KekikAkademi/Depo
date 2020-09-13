# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup
import json

gelen = input("Lütfen 'ÜRÜN' Linki Giriniz.. : ")

try:
    urun, butik = gelen.split("?")
except ValueError:
    urun = gelen

link = urun + "/yorumlar"
kimlik = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
istek = requests.get(link, headers=kimlik)
soup = BeautifulSoup(istek.text, "html5lib")

urun_ismi = soup.find('span', attrs={'class' : 'product-name'})

yorum_sahibi = []
yildiz_sayisi =[]
kullanici_yorumu = []

for yorum in soup.findAll('div', attrs={'class':'pr-rnr-com'}):
    for i_yorum in yorum.findAll('p', attrs={'class':'rnr-com-tx'}):
        kullanici_yorumu.append(i_yorum.text)
    for i_kullanici in yorum.findAll("span", attrs={'class': 'rnr-com-usr'}):
        yorum_sahibi.append(i_kullanici.text)
    for i_yildiz in yorum.findAll("div", attrs={'class':'ratings readonly'}):
        yildiz = []
        for tek_yildiz in i_yildiz.findAll("div", attrs={'style':'width:100%;max-width:100%'}):
            yildiz.append(tek_yildiz)
        yildiz_sayisi.append(len(yildiz))

liste = []
for adet in range(0, len(yorum_sahibi)):
    sozluk = {}
    sozluk['yildiz'] = yildiz_sayisi[adet]
    sozluk['kullanici'] = yorum_sahibi[adet]
    sozluk['yorum'] = kullanici_yorumu[adet]
    liste.append(sozluk)

sonuc = {"ad": urun_ismi.text, "link" : urun,"yorumlar":liste}

sonuc_json = json.dumps(sonuc, indent=2, sort_keys=True, ensure_ascii=False)

json_yaz = open(f"{urun_ismi.text}.json", "w+", encoding='utf8')
json_yaz.write(sonuc_json)
json_yaz.close()

print("\n\t\tjSon Oluşturuldu\n")

yazilan_veri = json.loads(sonuc_json)

print(f"""Ürün Adı     : {yazilan_veri['ad']}
Ürün Link    : {yazilan_veri['link']}
Yorum Sayısı : {len(yorum_sahibi)}""")

for bilgi in yazilan_veri['yorumlar']:
    print(f"""
{bilgi['kullanici']} | {bilgi['yildiz']} Yıldız!
---------------------------------------------
{bilgi['yorum']}""")