"""



"""

import requests
from bs4 import BeautifulSoup

istek = requests.get("https://www.nefisyemektarifleri.com/bugun-ne-pisirsem/")
soup = BeautifulSoup(istek.content, "html5lib")

yemekler = soup.find_all("div", attrs={"class": "post-title-author"})

adListe = []
yazarListe = []

for yemek in yemekler:
    print(yemek)
    break






def dosyaKaydet():
    open("aaaaaaa.txt", "w+").close()

    for adet in range(len(adListe)):
        with open("aaaaaaa.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"{adListe[adet]}\n\t{yazarListe[adet]}\n\n")

#dosyaKaydet()