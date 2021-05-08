"""
-Tebrikler !! Döngü içerisinde ekrana yazdırdığın veriyi dosyaya yazdırmayı başardın(ama append ile:(  )
-Yeni görevin ; Döngü ile kazınılan veriyi döngü dışında tut(kaydet) ve
-Write argümanı ile tek seferde yaz ( append ile değil :))   )
"""
import requests
from bs4 import BeautifulSoup

istek = requests.get("https://www.nefisyemektarifleri.com/bugun-ne-pisirsem/")
soup = BeautifulSoup(istek.content, "html5lib")

yemekler = soup.find_all("div", attrs={"class": "post-title-author"})

adListe = []
yazarListe = []

for yemek in yemekler:
    yemekAdi = yemek.h5.text
    yazarAdi = yemek.span.text

    adListe.append(yemekAdi)
    yazarListe.append(yazarAdi)

print(adListe)
print(yazarListe)

open("tarifler2.txt", "w+").close()

for adet in range(len(adListe)):
    dosya = open("tarifler2.txt", "a", encoding="utf-8")

    dosya.write(f"""Yemeğimizin Adı : {adListe[adet]}
        Tarifimizin Yazarı : {yazarListe[adet]} 
    """)

    dosya.close()