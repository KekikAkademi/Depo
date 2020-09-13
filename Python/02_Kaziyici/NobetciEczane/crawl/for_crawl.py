# Bu araç Yunus Emre Karabulut tarafından | @KekikAkademi için yazılmıştır.

#-------------------------------#
from bs4 import BeautifulSoup   #
from requests import get        #
#-------------------------------#

def ECZANE(il, ilce):
    if not il or not ilce: return print("Yanlış Kullanım")

    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    soup = BeautifulSoup(get(f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}", headers=kimlik).text, "html5lib").find_all("table", {"class": "table table-striped mt-2"})

    sozluk = {"nobetciEczaneler": []}

    for result in soup:
        for ad in result.find_all("td", {"style": "width:20%"}):
            sozluk["nobetciEczaneler"].append({"eczane_adi": ad.text})

        n = 0
        for adres in result.find_all("td", {"style": "width:50%"}):
            sozluk["nobetciEczaneler"][n]["eczane_adresi"] = adres.text
            n += 1

        n = 0
        for telefon in result.find_all("td", {"style": "width:30%"}):
            sozluk["nobetciEczaneler"][n]["eczane_telefonu"] = telefon.text
            n += 1

    return sozluk

#print(ECZANE("istanbul","beylikduzu"))