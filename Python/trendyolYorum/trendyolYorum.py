# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup

gelen = input("Lütfen 'ÜRÜN' Linki Giriniz.. : ")

try:
    urun, butik = gelen.split("?")
except ValueError:
    urun = gelen

link    = urun + "/yorumlar"
kimlik  = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
yanit   = requests.get(link, headers=kimlik)
corba   = BeautifulSoup(yanit.text, "html5lib")

urun_ismi = corba.find('span', class_='product-name').text
yorumlar  = corba.find('div', class_='pr-rnr-com')

yorum_sahibi     = [yorum_sahibi.text.split(' | ')[0] for yorum_sahibi in yorumlar.findAll('span', class_='rnr-com-usr')]
kullanici_yorumu = [yorum_.text for yorum_ in yorumlar.findAll('div', class_='rnr-com-tx')]

yildiz_sayisi    = []
for i_yildiz in yorumlar.findAll("div", attrs={'class':'ratings readonly'}):
    yildiz = list(
        i_yildiz.findAll(
            "div",
            attrs={'class': 'full', 'style': 'width:100%;max-width:100%'},
        )
    )

    yildiz_sayisi.append(len(yildiz))

liste = [
    {
        'kullanici' : yorum_sahibi[adet],
        'yildiz'    : yildiz_sayisi[adet],
        'yorum'     : kullanici_yorumu[adet]
    }
    for adet in range(len(yorum_sahibi))
]

sonuc = {"urun_adi": urun_ismi, "urun_linki" : urun, "urun_yorumlari":liste}

sonuc_json = json.dumps(sonuc, indent=2, sort_keys=True, ensure_ascii=False)

with open(f"{urun_ismi}.json", "w+", encoding='utf8') as json_yaz:
    json_yaz.write(sonuc_json)
print("\n\t\tjSon Oluşturuldu\n")

yazilan_veri = json.loads(sonuc_json)

print(f"""Ürün Adı     : {yazilan_veri['urun_adi']}
Ürün Link    : {yazilan_veri['urun_linki']}
Yorum Sayısı : {len(yorum_sahibi)}""")

for bilgi in yazilan_veri['urun_yorumlari']:
    print(f"""
{bilgi['kullanici']} | {bilgi['yildiz']} Yıldız!
---------------------------------------------
{bilgi['yorum']}""")
