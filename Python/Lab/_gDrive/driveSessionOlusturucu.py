from pydrive.auth import GoogleAuth
import json, os, sys

credentials_json    = 'client_secrets.json'

if not os.path.exists(credentials_json):
    print(f'''\n\t{credentials_json} Bulunamadı..
Lütfen https://developers.google.com/drive/api/v3/quickstart/python adresinden;
    Api Etkinleştirmesini yapıp json dosyasını '{credentials_json}' olarak dizine ekleyiniz...\n''')
    sys.exit()

G_DRIVE_TOKEN_DOSYASI = "drive_erisim.json"

def erisim_ver():
    gauth = GoogleAuth()

    if not os.path.exists(G_DRIVE_TOKEN_DOSYASI):
        with open(G_DRIVE_TOKEN_DOSYASI, 'w+') as dosya:
            dosya.write('')

    gauth.LoadCredentialsFile(G_DRIVE_TOKEN_DOSYASI)    # Kayıtlı istemci kimlik bilgilerini yüklemeyi dene

    if gauth.credentials is None:                       # Orada değillerse kimlik doğrulaması yap
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:                    # Süresi dolmuşsa yenile
        gauth.Refresh()
    else:                                               # Kaydedilen kimlik bilgilerini başlat
        gauth.Authorize()

    gauth.SaveCredentialsFile(G_DRIVE_TOKEN_DOSYASI)    # Geçerli kimlik bilgilerini bir dosyaya kaydet

    bilgiler = json.load(open(G_DRIVE_TOKEN_DOSYASI, 'r+'))

    print(f"""
    CLIENT_ID       : {bilgiler['client_id']}
    CLIENT_SECRET   : {bilgiler['client_secret']}
    """)

if __name__ == '__main__':
    erisim_ver()