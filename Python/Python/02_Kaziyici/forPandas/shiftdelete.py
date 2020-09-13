from os import system
system('clear')

import requests
from bs4 import BeautifulSoup

link = "https://shiftdelete.net/haberler"
istek = requests.get(link)
corba = BeautifulSoup(istek.content, 'lxml')


def tekSayfa():
    baslik = [i.text for i in corba.find_all('em', class_='p-name')]
    tarih = [i.text for i in corba.findAll('i', class_='dt-published')]
    print(f"{len(baslik)}\n{len(tarih)}\n\n")
    print(f"{baslik}\n{tarih}\n\n")

    import pandas as pd

    veri = pd.DataFrame({
        'baslik' : baslik,
        'tarih' : tarih
    })

    print(veri)
    return veri


def cokSayfa():
    link = "https://shiftdelete.net/haberler"
    istek = requests.get(link)
    corba = BeautifulSoup(istek.content, 'lxml')
    
    
    baslik = []
    tarih = []


    sayfalar = [i.text for i in corba.find_all('a') if 'haberler/page' in str(i)]
    # print(sayfalar) # >> ['2', '3', '2054', 'Sonraki sayfa »']
    sonSayfa = sayfalar[-2]


    from time import sleep

    for bakalim in range(1,int(sonSayfa)+1):
        link = "https://shiftdelete.net/haberler/page/" + str(bakalim)
        istek = requests.get(link)
        corba = BeautifulSoup(istek.content, 'lxml')

        baslik.append([i.text for i in corba.find_all('em', class_='p-name')])
        tarih.append([i.text for i in corba.findAll('i', class_='dt-published')])
        print(bakalim)
        sleep(1)
        
        if bakalim == 5: break
    system('clear')

    print(f"{len(baslik)}\n{len(tarih)}\n\n")
    print(f"{baslik}\n{tarih}\n\n")

    baslikFlat = [y for x in baslik for y in x]
    tarihFlat = [y for x in tarih for y in x]

    print(f"\tFlat\n{baslikFlat}\n{tarihFlat}\n\n")
    print(f"{len(baslikFlat)}\n{len(tarihFlat)}\n\n")

    import pandas as pd

    veri = pd.DataFrame({
        'baslik' : baslikFlat,
        'tarih' : tarihFlat
    })

    print(veri)
    return veri


veri = cokSayfa()

from tabulate import tabulate
gorselVeri = tabulate(veri, headers='keys', tablefmt='psql')
print(gorselVeri)
# with open("gorselVeri.txt", "w+") as dosya: dosya.write(gorselVeri)

import json
jsonVeri = json.loads(veri.to_json(orient='records'))
#print(jsonVeri)

jsonCikti = json.dumps(jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
print(jsonCikti)
# with open("jsonVeri.json", "w+") as dosya: dosya.write(jsonCikti)