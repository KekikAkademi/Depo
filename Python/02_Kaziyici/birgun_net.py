# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests import get
from xmltodict import parse
from tinydb import TinyDB
from progress.bar import Bar

from xlsxwriter import Workbook

db = TinyDB('birgun_net.json')

rss_icerik      = get('https://www.birgun.net/xml/rss.xml').content
rss_ayristir    = parse(rss_icerik)
veriler         = rss_ayristir['rss']['channel']['item']

print(f'RSS beslemesinde {len(veriler)} öğe bulundu.\n')

bar = Bar('\tÖğeler Depolanıyor..', max=len(veriler))

# al_bu_da = {'haber' : []}                 # pandas için
for haber in veriler:
    haber = {
        'tarih'     : haber['pubDate'],
        'kategori'  : haber['category'],
        'link'      : haber['link'],
        'baslik'    : haber['title'],
        'aciklama'  : haber['description']
    }

    db.insert(haber)
    # al_bu_da['haber'].append(haber)       # pandas için
    bar.next()

bar.finish()

###########################################################################################

# Yeni bir Excel dosyası oluşturun ve bir çalışma sayfası ekleyin.
with Workbook('birgun_net.xlsx') as workbook:

    # Çalışma sayfası ekle
    worksheet = workbook.add_worksheet()

    # Başlıkları yaz
    basliklar = ['Tarih', 'Kategori', 'Link', 'Başlık', 'Açıklama']
    for sutun, baslik in enumerate(basliklar):
        worksheet.write(0, sutun, baslik, workbook.add_format({'align': 'center', 'bold': True}))

    # Sütun genişliğini ve biçimini ayarla
    italik  = workbook.add_format({'italic': True})
    kalin   = workbook.add_format({'bold': True})
    carpan  = 4.01767778224

    worksheet.set_column(0,0, 7.54*carpan,  kalin)  # Tarih
    worksheet.set_column(1,1, 3.49*carpan,  italik) # Kategori
    worksheet.set_column(2,2, 2.86*carpan,  italik) # Link
    worksheet.set_column(3,3, 23.72*carpan, italik) # Başlık
    worksheet.set_column(4,4, 51.89*carpan, italik) # Açıklama

    # Liste verilerini yaz
    satir = 0
    for urun in db.all():
        satir += 1
        worksheet.write(satir, 0, urun['tarih'] )
        worksheet.write(satir, 1, urun['kategori'])
        worksheet.write_url(satir, 2, urun['link'], string='Web Sayfası')
        worksheet.write(satir, 3, urun['baslik'])
        worksheet.write(satir, 4, urun['aciklama'])

###########################################################################################
###########################################################################################

# Basliklar = ["Tarih", "Kategori", "Link", "Başlık", "Açıklama"]
# satir = 0

# calisma_kitabi = Workbook('birgun_net.xlsx')
# calisma_alani = calisma_kitabi.add_worksheet()

# calisma_alani.set_column(0,0, 25)   # Tarih
# calisma_alani.set_column(1,1, 20)   # Kategori
# calisma_alani.set_column(2,2, 35)   # Link
# calisma_alani.set_column(3,3, 50)   # Başlık
# calisma_alani.set_column(4,5, 90)   # Açıklama

# for sutun, baslik in enumerate(Basliklar):
#     calisma_alani.write(satir, sutun, baslik)

# for urun in db.all():
#     satir += 1
#     calisma_alani.write(satir, 0, urun['tarih'] )
#     calisma_alani.write(satir, 1, urun['kategori'])
#     calisma_alani.write_url(satir, 2, urun['link'], string='Web Sayfası')
#     calisma_alani.write(satir, 3, urun['baslik'])
#     calisma_alani.write(satir, 4, urun['aciklama'])

# calisma_kitabi.close()

###########################################################################################
###########################################################################################

# import pandas as pd

# df = pd.DataFrame(al_bu_da['haber'])
# # df.to_excel(r'demo.xlsx', index = False, header=True)

# # Motor olarak XlsxWriter kullanarak bir Pandas Excel yazıcısı oluşturun.
# writer = pd.ExcelWriter("pandas_column_formats.xlsx", engine='xlsxwriter')

# # Veri çerçevesini bir XlsxWriter Excel nesnesine dönüştürün.
# df.to_excel(writer, sheet_name='Sheet1')

# # XlsxWriter çalışma kitabını ve çalışma sayfası nesnelerini alın.
# workbook  = writer.book
# worksheet = writer.sheets['Sheet1']

# # Bazı hücre formatları ekleyin.
# format1 = workbook.add_format({'align': 'center', 'bold': True})
# format2 = workbook.add_format({'align': 'left', 'italic': True})

# # Sütun genişliğini ve biçimini ayarlayın.
# carpan = 4.01767778224
# worksheet.set_column('B:B', 7.54*carpan, format1)
# worksheet.set_column('C:C', 3.49*carpan, format2)
# worksheet.set_column('E:E', 23.72*carpan, format2)
# worksheet.set_column('F:F', 51.89*carpan, format2)

# # Pandas Excel yazıcısını kapatın ve Excel dosyasının çıktısını alın.
# writer.save()

###########################################################################################

print(f'\nDB\'de {len(veriler)} öğe depolandı.')