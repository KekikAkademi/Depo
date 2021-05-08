# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, json
from bs4 import BeautifulSoup
from tabulate import tabulate

kullanim = {
    'kullanim' : [
        'coinMarket("json_veri")',
        'coinMarket("json", "Bitcoin")',
        'coinMarket("json_gorsel")',
        'coinMarket("gorsel_veri")',
        'coinMarket("basliklar")'
    ]
}

def coinMarket(cikti='gorsel_veri', baslik=None):
    """
    CoinMarketCap Verileri

        Kullanım;

                coinMarket("json_veri")
                coinmarket("json", "Bitcoin")
                coinMarket("json_gorsel")
                coinMarket("gorsel_veri")
                coinMarket("basliklar")
    """

    url = f"https://coinmarketcap.com/tr/"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    istek = requests.get(url, headers=kimlik)
    # print(istek)
    # print(istek.headers)

    corba = BeautifulSoup(istek.content, "lxml")

    # veriler = corba.select('div.cmc-table__table-wrapper-outer > div > table')[2]
    # print(veriler.prettify())
    # print(veriler.get_text(separator="\n\n"))

    tablo = corba.findAll('table')[2]
    # print(tablo)
    # print(tablo.get_text(separator="\n"))

    ayristir = tablo.get_text(separator="\n").split('\n')

    stabil = 0
    say = 8

    liste = []
    for _ in range(len(ayristir)):
        try:
            liste.append({
                ayristir[stabil] : ayristir[say],
                ayristir[stabil+1] : ayristir[say+1],
                ayristir[stabil+2] : ayristir[say+2],
                ayristir[stabil+3] : ayristir[say+3],
                ayristir[stabil+4] : ayristir[say+4],
                ayristir[stabil+5] : ayristir[say+5],
                ayristir[stabil+6] : ayristir[say+6],
            })
            say += 7
            stabil = 0
        except:
            pass

    basliklar = [anahtar for anahtar in liste[0].keys()]

    if cikti == 'json_veri':
        return liste
    
    elif cikti == 'json_gorsel':
        return json.dumps(liste, indent=2, sort_keys=False, ensure_ascii=False)
    
    elif cikti == 'json' and baslik != None:
        for bul in range(len(liste)):
            if liste[bul]['Ad'] == baslik:
                return liste[bul]
    
    elif cikti == 'basliklar':
        return basliklar
    
    elif cikti == 'gorsel_veri':
        return tabulate(liste, headers='keys', tablefmt='psql')
    
    else:
        return kullanim

# print(coinMarket("json_veri"))

# print(coinMarket("json", "Bitcoin"))

# print(coinMarket("json_gorsel"))

# print(coinMarket("gorsel_veri"))

# print(coinMarket("basliklar"))

# print(coinMarket("alakasız bişi"))