# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests, xmltodict
from tinydb import TinyDB
from progress.bar import Bar

RSS_FEED_URL = "https://www.ntv.com.tr/son-dakika.rss"

def haberAl(db_yolu):
    print("NTV'den Haberler Alınıyor..")

    rss_icerik      = requests.get(RSS_FEED_URL).content
    rss_ayristir    = xmltodict.parse(rss_icerik)

    ## fetiş
    # import json
    # with open('ntv.json','w', encoding='utf-8') as dosya: 
    #     json.dump(rss_ayristir, dosya, indent=2, sort_keys=False, ensure_ascii=False)
    # return
    ## fetiş

    veriler = rss_ayristir['feed']['entry']

    print(f'\n\tRSS beslemesinde {len(veriler)} öğe bulundu.')

    bar = Bar('\t\tÖğeler Depolanıyor..', max=len(veriler))
    db = TinyDB(db_yolu)
    for item in veriler:
        db.insert(item)
        bar.next()
    bar.finish()
            
    print(f'\nDB\'de {len(veriler)} öğe depolandı.')

def haberGetir(db_yolu):
    return TinyDB(db_yolu).all()

if __name__=='__main__':
    import datetime, pytz
    tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y") # Bugünün Tarihi
    saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H-%M")     # Bugünün Saati
    zaman = tarih + '_' + saat

    haberAl(db_yolu=f"ntv_{zaman}.json")