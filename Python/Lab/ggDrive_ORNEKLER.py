# https://stackoverflow.com/questions/57582032/how-do-i-upload-to-a-shared-drive-in-python-with-google-drive-api-v3

# credentials/scope koduyla ilgili arka plana ihtiyacınız olması durumunda,
#   https://developers.google.com/drive/api/v3/quickstart/python
# Şuradan kod yüklemenin temeli:
#   https://developers.google.com/drive/api/v3/manage-uploads

import pickle, sys, math, json
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from mimetypes import guess_type
from tabulate import tabulate

bilgiler = json.load(open("bilgiler.json"))

# Bu kapsamları değiştiriyorsanız, 'token.pickle' dosyasını silin.
SCOPES = [
	'https://www.googleapis.com/auth/drive',
	'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.appdata',
    'https://www.googleapis.com/auth/drive.metadata'
]

credentials_json = 'credentials.json'

if not os.path.exists(credentials_json):
    print('''\tcredentials.json Bulunamadı..
Lütfen https://developers.google.com/drive/api/v3/quickstart/python adresinden;
    Api Etkinleştirmesini yapıp json dosyasını dizine ekleyiniz...''')
    sys.exit()

credentials_pickle = 'token.pickle'

def driveYetkilendirme():
    referans = None
    # OAuth token / kullanıcı yetkilendirmesi alın.
    if os.path.exists(credentials_pickle):
        with open(credentials_pickle, 'rb') as token:
            referans = pickle.load(token)
    # Kullanılabilir (geçerli) kimlik bilgisi yoksa, kullanıcının oturum açmasına izin verin.
    if not referans or not referans.valid:
        if referans and referans.expired and referans.refresh_token:
            referans.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_json, SCOPES)
            referans = flow.run_local_server(port=0)
        # Bir sonraki çalıştırma için kimlik bilgilerini kaydedin
        with open(credentials_pickle, 'wb') as token:
            pickle.dump(referans, token)
    # Google Drive API hizmetini döndür
    return build('drive', 'v3', credentials=referans, cache_discovery=False)

def byteOku(byte, etken=1024, son_ek="B"):
    """
    Baytları uygun bayt biçimine ölçekleyin
     Örneğin:
         1253656 => '1,20 MB'
         1253656678 => '1,17 GB'
    """
    for birim in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if byte < etken:
            return f"{byte:.2f}{birim}{son_ek}"
        byte /= etken
    return f"{byte:.2f}Y{son_ek}"

def gDriveDosyaYukle(yerel_dosya_adi):
    drive_service = driveYetkilendirme()
    ortak_drivelar = drive_service.drives().list(pageSize=10).execute()

    # import json
    # print(json.dumps(ortak_drivelar, indent=2, sort_keys=False, ensure_ascii=False))
    # return

    nerdeyiz = None
    for say in range(len(ortak_drivelar['drives'])):
        if ortak_drivelar['drives'][say]['name'] == '@KekikAkademi':       # Ortak Drive ADI
            ortak_drive_id = ortak_drivelar['drives'][say]['id']
            nerdeyiz = ortak_drivelar['drives'][say]['name']

    mime_turu = guess_type(yerel_dosya_adi)[0]
    mime_turu = mime_turu if mime_turu else "text/plain"

    govde = {
        "name": yerel_dosya_adi,
        "description": "Python ile Yüklenmiştir..",
        "mimeType": mime_turu,
        "parents": [ortak_drive_id]
    }
    
    dosya_govde = MediaFileUpload(yerel_dosya_adi, mimetype=mime_turu, chunksize=50*1024*1024, resumable=True)
    yuklenen_dosya = drive_service.files().create(body=govde, media_body=dosya_govde, supportsAllDrives=True)
    dosya_bilgi = yuklenen_dosya.execute()

    yanit = None
    gorunen_mesaj = ""
    while yanit == None:
        durum, yanit = yuklenen_dosya.next_chunk()
        if durum:
            print(dosya_bilgi.get('name'))
            print("Yüklenen %d%%." % int(durum.progress() * 100))
            print('-'*100)

            yuzde = int(durum.progress() * 100)
            progress_str = "**[{0}{1}]**\n**Süreç** : __%__`{2}`\n".format(
                "".join(["●" for i in range(math.floor(yuzde / 5))]),
                "".join(["○" for i in range(20 - math.floor(yuzde / 5))]),
                round(yuzde, 2),
            )
            
            gecerli_mesaj = f"**Arşive yüklüyorum kanka..**\n**Dosya Adı**: `{yerel_dosya_adi}`\n{progress_str}"
            
            if gorunen_mesaj != gecerli_mesaj:
                try:
                    print(gecerli_mesaj)
                    gorunen_mesaj = gecerli_mesaj
                except:
                    pass
    
    return f"\nŞu Konuma: `{nerdeyiz}` >> `{ortak_drive_id}`\n\n\tDosya Yüklendi: `{yanit.get('name')}` >> `{yanit.get('id')}`"

# print(gDriveDosyaYukle('VNC-Viewer-6.20.113-Linux-x64'))

def gDriveDizinListele():
    """
    Drive v3 API'nin temel kullanımını gösterir.
     Kullanıcının erişebildiği ilk 5 dosyanın adlarını ve kimliklerini yazdırır.
    """

    drive_service = driveYetkilendirme()
    # Drive v3 API'sini çağırın

    sonuclar = drive_service.files().list(
        pageSize=5, fields="nextPageToken, files(id, name, mimeType, size, parents, modifiedTime)").execute()
    # Sonuçları Al

    liste = sonuclar.get('files', [])
    # 20 dosyanın ve klasörün tümünü listele

    if not liste:
        # Boş Sürücü
        print('Dosya Bulunamadı..')
    else:
        satirlar = []
        for eleman in liste:
            # Dosya ID'sini al
            id = eleman["id"]
            # Dosya Adını al
            ad = eleman["name"]
            try:
                # Üst Dizin ID'si
                ust_dizin = eleman["parents"]
            except:
                # Üst Dizin Yoksa
                ust_dizin = "N/A"
            try:
                # Boyutu Güzel bir şekilde al (KB, MB, vs.)
                boyut = byteOku(int(eleman["size"]))
            except:
                # Dosya değil, dizin ise
                boyut = "N/A"
            # Google Drive dosya türünü alın
            mime_turu = eleman["mimeType"]
            # son değiştirilme tarihini al
            degistirilme_zamani = eleman["modifiedTime"]
            # Her şeyi listeye ekle
            satirlar.append((id, ad, ust_dizin, boyut, mime_turu, degistirilme_zamani))
        print("Dosyalar:")
        # insan tarafından okunabilir bir tabloya dönüştür
        tablo = tabulate(satirlar, headers=["ID", "Ad", "Üst Dizin", "Boyut", "Türü", "Değiştirilme Zamanı"])
        # tabloyu yazdır
        print(tablo)

# gDriveDizinListele()

def gDriveDosyaAra():
    """ disk içerisinde arama yapmanıza olanak tanır """
    drive_service = driveYetkilendirme()

    sonuclar = []
    sayfa_token = None
    while True:
        drive_yaniti = drive_service.files().list(
            q=f"mimeType='text/plain'",
            spaces="drive",
            fields="nextPageToken, files(id, name, mimeType)",
            pageToken=sayfa_token).execute()
        # filtrelenmiş dosyaları yineleyin
        for dosya in drive_yaniti.get("files", []):
            sonuclar.append((dosya["id"], dosya["name"], dosya["mimeType"]))
        sayfa_token = drive_yaniti.get('nextPageToken', None)
        if not sayfa_token:
            # daha fazla dosya yoksa
            break
    # insan tarafından okunabilir bir tabloya dönüştür
    tablo = tabulate(sonuclar, headers=["ID", "Ad", "Türü"])
    print(tablo)

# gDriveDosyaAra()

#--------------------------------------------------------------------------------------------------#

# from google_api_v3_helper import *
# fileId = '0ADYmVLSet22XUk9PVA' #id of the file you wish to get the folder tree for.
# tree = get_google_files_in_folder(driveYetkilendirme(), fileId)
# print(tree)

#--------------------------------------------------------------------------------------------------#
