# https://www.linode.com/docs/applications/big-data/how-to-scrape-a-website-with-beautiful-soup/

from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib3
import xlsxwriter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://elpaso.craigslist.org/search/mcy?sort=date'
toplam_eklenen = 0

def corbaYap(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data,'lxml')

def ana(url):
    global toplam_eklenen
    db = TinyDB("db.json")

    while url:
        print ("Web Sayfası: ", url)
        corba           = corbaSureci(url, db)
        sonraki_link    = corba.find("link", rel="next")

        url = False
        if (sonraki_link):
            url = sonraki_link['href']

    print ("Eklendi ",toplam_eklenen)

    exelYap(db)

def corbaSureci(url, db):
    global toplam_eklenen

    corba       = corbaYap(url)
    sonuclar    = corba.find_all("li", class_="result-row")
    print(sonuclar)

    for sonuc in sonuclar:
        try:
            kayit = {
                'pid': sonuc['data-pid'],
                'webpage': sonuc.a['href'],
                'createdt': datetime.datetime.now().isoformat()
            }

            Sonuc = Query()
            ara = db.search(Sonuc.pid == kayit["pid"])

            if not ara:
                toplam_eklenen += 1
                print ("Ekleniyor ... ", toplam_eklenen)
                db.insert(kayit)

        except (AttributeError, KeyError):
            pass

    return corba

def exelYap(db):
    Basliklar = ["Pid", "Webpage", "Created Date"]
    satir = 0

    calisma_kitabi = xlsxwriter.Workbook('motorcycle.xlsx')
    calisma_alani = calisma_kitabi.add_worksheet()

    calisma_alani.set_column(0,0, 15) # pid
    calisma_alani.set_column(1,1, 10)  # webpage
    calisma_alani.set_column(2,2, 30)  # created date

    for sutun, baslik in enumerate(Basliklar):
        calisma_alani.write(satir, sutun, baslik)

    for urun in db.all():
        satir += 1
        calisma_alani.write(satir, 0, urun['pid'] )
        calisma_alani.write_url(satir, 1, urun['webpage'], string='Web Sayfası')
        calisma_alani.write(satir, 2, urun['createdt'] )

    calisma_kitabi.close()

if __name__ == '__main__':
    ana(url)