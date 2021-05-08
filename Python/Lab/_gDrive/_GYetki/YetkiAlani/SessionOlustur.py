# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pydrive.auth import GoogleAuth
import json, os, sys

AYARLAR          = "ayar.env"
credentials_json = 'client_secrets.json'

if (not os.path.exists(credentials_json)) and (not os.path.exists(AYARLAR)):
    print(f'''\n\t{credentials_json} Bulunamadı..


Lütfen https://developers.google.com/drive/api/v3/quickstart/python adresinden;

    Api Etkinleştirmesini yapıp json dosyasını (https://console.developers.google.com/apis/credentials)


        '{credentials_json}' olarak dizine ekleyiniz ya da elle giriniz..\n''')

    if input('OAuth 2.0 İstemci Kimliğinin ID ve SECRET Biliyor Musun? (e/H) : ').lower() not in ['e', 'y']:
        print("\n\n\tDizine istediğim gibi indir, sonra tekrar başlat..")
        sys.exit()
    else:
        ID     = input('\n\nID   : ')
        SECRET = input('SECRET : ')
        with open(AYARLAR, "w+") as ayar:
            ayar.write(f"CLIENT_ID = \"{ID}\"\nCLIENT_SECRET = \"{SECRET}\"")
        print(f"\n\n\n\t[+] {AYARLAR} Oluşturuldu..\n\n")

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

    with open(AYARLAR, "w+") as ayar:
        ayar.write(f"CLIENT_ID = \"{bilgiler['client_id']}\"\nCLIENT_SECRET = \"{bilgiler['client_secret']}\"")

    os.remove(credentials_json)
    os.remove(G_DRIVE_TOKEN_DOSYASI)

    return f"[+] {AYARLAR} Oluşturuldu.."