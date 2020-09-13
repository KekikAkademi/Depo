import requests
from bs4 import BeautifulSoup

link = f"https://www.eczaneler.gen.tr/nobetci-canakkale-merkez"
kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
istek = requests.get(link, kimlik)
soup = BeautifulSoup(istek.text, "html5lib")

sozluk = {"nobetciEczaneler": []}

def veriKAZI():
    for table in soup.findAll("table", {"class": "table table-striped mt-2"}):
        #print(table)
        #print(table.tr.text)
        eczane_adi = table.findAll("td", {"style": "width:20%"})
        eczane_adresi = table.findAll("td", {"style": "width:50%"})
        eczane_telefon = table.findAll("td", {"style": "width:30%"})

        for adet in range(len(eczane_adi)):
            sozluk["nobetciEczaneler"].append({"eczane_adi": eczane_adi[adet].text})
            sozluk["nobetciEczaneler"][adet]["eczane_adresi"] = eczane_adresi[adet].text
            sozluk["nobetciEczaneler"][adet]["eczane_telefon"] = eczane_telefon[adet].text

    print(sozluk)
    return sozluk

def jSonVer():
    import json

    cikti = json.dumps(sozluk, indent=2, sort_keys=True, ensure_ascii=False)

    json_yaz = open(f"{soup.title.text.replace(' | Eczaneler.gen.tr','')}.json", "w+", encoding='utf8')
    json_yaz.write(cikti)
    json_yaz.close()

    print("\n\t\tjSon Oluşturuldu\n")

    yazilan_veri = json.loads(cikti)

    for bilgi in yazilan_veri['nobetciEczaneler']:
        print(f"""
    # : {bilgi['eczane_adi']}
    # : {bilgi['eczane_adresi']}
    # : {bilgi['eczane_telefon']}
    """)

if __name__ == '__main__':
    veriKAZI()
    jSonVer()