# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
from bs4 import BeautifulSoup

link = f"https://www.worldometers.info/coronavirus/"
kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
istek = requests.get(link, kimlik)
soup = BeautifulSoup(istek.text, "html5lib")

sozluk = {"koronaVerileri": []}

dunya = soup.select("#maincounter-wrap > div")
dunyaVaka = dunya[0].text.strip()
dunyaOlu = dunya[1].text.strip()
dunyaKurtulan = dunya[2].text.strip()

turkiye = soup.select("#main_table_countries_today > tbody:nth-child(2) > tr:nth-child(16)")
turkiye = turkiye[0].text.split()
trVaka = turkiye[1]
trOlu = turkiye[3]
trKurtulan = turkiye[5]

sozluk["koronaVerileri"].append({
    "vakaSayisi": {"TR": trVaka, "dunyaGeneli": dunyaVaka},
    "oluSayisi": {"TR": trOlu, "dunyaGeneli": dunyaOlu},
    "iyilesmeSayisi": {"TR": trKurtulan, "dunyaGeneli": dunyaKurtulan}
})

print(sozluk)



import json

cikti = json.dumps(sozluk, indent=2, sort_keys=True, ensure_ascii=False)

print(cikti + "\n\n")

yazilan_veri = json.loads(cikti)

for bilgi in yazilan_veri['koronaVerileri']:
    print(f"""Dünya Geneli;
Vaka Sayısı     : {bilgi['vakaSayisi']['dunyaGeneli']}
Ölü Sayısı      : {bilgi['oluSayisi']['dunyaGeneli']}
İyileşen Sayısı : {bilgi['iyilesmeSayisi']['dunyaGeneli']}
Türkiye;
Vaka Sayısı     : {bilgi['vakaSayisi']['TR']}
Ölü Sayısı      : {bilgi['oluSayisi']['TR']}
İyileşen Sayısı : {bilgi['iyilesmeSayisi']['TR']}
""")