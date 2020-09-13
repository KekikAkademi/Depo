## https://youtu.be/00bc9BdUPSw
import requests
from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top"
r = requests.get(imdburl)
soup = BeautifulSoup(r.content,"html.parser")
gelen_veri = soup.find_all("table",{"class":"chart full-width"})

filmtablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
filmtablosu = filmtablosu.find_all("tr")

for film in filmtablosu:
    filmbasliklari = film.find_all("td",{"class":"titleColumn"})
    filmismi = filmbasliklari[0].text
    filmismi = filmismi.replace("\n","")
    
    print(filmismi)
    print("*"*100)