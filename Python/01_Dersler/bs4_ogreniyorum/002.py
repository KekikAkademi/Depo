"""
- İlgili linkten istediğin veriyi kazımayı başardın  Tebrikleer. Bu yaptığın kazıma işleminin adı scraping
- Yeni görevin ; bu veriyi txt dosyasına yaz
"""
import requests
from bs4 import BeautifulSoup

istek = requests.get("https://www.nefisyemektarifleri.com/bugun-ne-pisirsem/")
soup = BeautifulSoup(istek.content, "html5lib")

yemekler = soup.find_all("div", attrs={"class": "post-title-author"})

for yemek in yemekler:
    yemekAdi = yemek.h5.text
    yazarAdi = yemek.span.text

    dosya = open("tarifler.txt", "a", encoding="utf-8")          # dosyayı append ile açtık çünkü döngü içerisinde ,"w" ile değil :)
    dosya.write(f"""Yemeğimizin Adı : {yemekAdi}
    Tarifimizin Yazarı : {yazarAdi} 
""")
    dosya.close()

    print(f"""Yemeğimizin Adı : {yemekAdi}
    Tarifimizin Yazarı : {yazarAdi} 
""")