# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError
from oauth2client.file import Storage
from googleapiclient.discovery import build
import httplib2, os, sys
from YetkiAlani.SessionOlustur import AYARLAR, erisim_ver
from dotenv import load_dotenv

load_dotenv(AYARLAR)

# Bu kapsamları değiştiriyorsanız, yeniden yetkilendirme almalısınız..
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.appdata',
    'https://www.googleapis.com/auth/drive.metadata'
]

# Bu Kısım driveSessionOlusturucu.py'dan temin edilir..
CLIENT_ID               = os.environ.get("CLIENT_ID", None)
CLIENT_SECRET           = os.environ.get("CLIENT_SECRET", None)

# evrensel dosya adı tanımı
G_DRIVE_TOKEN_DOSYASI   = "drive_erisim.json"

def kod_al():
    if os.path.exists(G_DRIVE_TOKEN_DOSYASI):
        return ('Drive Yetkilendirmesi yapılmış..')

    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, SCOPES, redirect_uri="urn:ietf:wg:oauth:2.0:oob")
    yetkilendirme_linki = flow.step1_get_authorize_url()

    return (f'Lütfen bağlantıya gidip yetkilendirme aşamalarını tamamlayın, ardından kodu giriniz..\n\nGoogle OAuth 2.0 \n\t{yetkilendirme_linki}')

def token_olustur(token:str): # fiziksel olarak dosya bağımlılığı yoktur ve drive_erisim.json oluşturur
    try:
        flow             = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, SCOPES, redirect_uri="urn:ietf:wg:oauth:2.0:oob")
        yetki_kodu       = token.strip()
        kimlik_bilgileri = flow.step2_exchange(yetki_kodu)
        dosya            = Storage(G_DRIVE_TOKEN_DOSYASI)
        dosya.put(kimlik_bilgileri)
        return "[+] Drive Yetkilendirme Başarılı!"
    except FlowExchangeError:
        return "[!] Vermiş olduğun kod geçersiz.."
    except Exception as hata:
        return f"[!] {type(hata).__name__} ~ {hata}"

def g_yetki():
    if not os.path.exists(AYARLAR):
        print(erisim_ver())
        sys.exit()

    if not os.path.exists(G_DRIVE_TOKEN_DOSYASI):
        print("\t[!] Önce Yetkilendirme Yapmalısınız...\n\n")
        print(kod_al())
        print(token_olustur(input('\n\nLütfen Kodu Giriniz.. : ')))

    # Kişisel bilgilei alır
    kimlik_bilgileri = Storage(G_DRIVE_TOKEN_DOSYASI).get()
    # httplib2.Http objesi oluşturur ve kişisel bilgilerinizle yetkilendirir.
    http = httplib2.Http()
    kimlik_bilgileri.refresh(http)
    referans = kimlik_bilgileri.authorize(http)
    return build("drive", "v3", http=referans, cache_discovery=False)