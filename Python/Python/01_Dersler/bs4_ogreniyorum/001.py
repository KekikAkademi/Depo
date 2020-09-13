"""  
- web sitesine bağlan 
- kaynak kodunu al
- bs modulüne aktar
- bs modulü ile html kodlarını parçala

"""
import requests
from bs4 import BeautifulSoup

istek = requests.get("https://www.nefisyemektarifleri.com/bugun-ne-pisirsem/")          # response [200]
soup = BeautifulSoup(istek.content, "html5lib")                                         # kaynak kodu(soup),html5lib ile ayrıştırdık

yemekler = soup.find_all("div", attrs={"class": "post-title-author"})                   # çorbayı cımbızla
                                                                                    # findAll fonksiyonu Liste Çevirir
                                                                                    # find fonksiyonu Obje Çevirir

for yemek in yemekler:          # yemekler listesini for ile işliyoruz (yemek için)
    #print(yemek.text)           #text fonksiyonu yazıyı kaynak kodundan ayrıştırır
    #print(yemek)
    #break

    yemekAdi = yemek.h5.text
    #yazarAdi = yemek.find("span", attrs={"class": "post_author_link"}).text
    yazarAdi = yemek.span.text


    print(f"""Yemeğimizin Adı : {yemekAdi}
    Tarifimizin Yazarı : {yazarAdi} 
""")