# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle, os, sys

# Bu kapsamları değiştiriyorsanız, 'token.pickle' dosyasını silin.
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.appdata',
    'https://www.googleapis.com/auth/drive.metadata'
]

credentials_json    = 'credentials.json'
credentials_pickle  = 'token.pickle'

def drive_yetkilendirme(): # fiziksel olarak credentials.json bağımlılığı vardır ve token.pickle oluşturur
    if not os.path.exists(credentials_json):
        print(f'''\n\t{credentials_json} Bulunamadı..
    Lütfen https://developers.google.com/drive/api/v3/quickstart/python adresinden;
        Api Etkinleştirmesini yapıp json dosyasını '{credentials_json}' olarak dizine ekleyiniz...\n''')
        sys.exit()

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
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_json, SCOPES)
            referans = flow.run_local_server(port=0)
        # Bir sonraki çalıştırma için kimlik bilgilerini kaydedin
        with open(credentials_pickle, 'wb') as token:
            pickle.dump(referans, token)
    # Google Drive API hizmetini döndür
    return build('drive', 'v3', credentials=referans, cache_discovery=False)

###

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from googleapiclient.discovery import build
import httplib2
from dotenv import load_dotenv

load_dotenv("ayar.env")

# Bu Kısım driveSessionOlusturucu.py'dan temin edilir..
CLIENT_ID               = os.environ.get("CLIENT_ID", None)
CLIENT_SECRET           = os.environ.get("CLIENT_SECRET", None)
# evrensel dosya adı tanımı
G_DRIVE_TOKEN_DOSYASI   = "drive_erisim.json"

def token_yarat():
    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, SCOPES, redirect_uri="urn:ietf:wg:oauth:2.0:oob")
    yetkilendirme_linki = flow.step1_get_authorize_url()

    print(yetkilendirme_linki)
    yetkilendirme_kodu = input("\n\n\tLütfen yukarıdaki Linke Gidin\nYetkilendirmeyi tamamlayıp kodu buraya giriniz : ")

    yetki_kodu = yetkilendirme_kodu.strip()
    kimlik_bilgileri = flow.step2_exchange(yetki_kodu)
    dosya = Storage(G_DRIVE_TOKEN_DOSYASI)
    dosya.put(kimlik_bilgileri)
    return dosya

def yetkilendir(): # fiziksel olarak dosya bağımlılığı yoktur ve drive_erisim.json oluşturur
    if not os.path.exists(G_DRIVE_TOKEN_DOSYASI):
        print('''\ndrive_erisim.json Bulunamadı..
Lütfen yetkilendirmenizi tamamlayınız..\n''')
        token_yarat()

    # Kişisel bilgilei alır
    kimlik_bilgileri = Storage(G_DRIVE_TOKEN_DOSYASI).get()
    # httplib2.Http objesi oluşturur ve kişisel bilgilerinizle yetkilendirir.
    http = httplib2.Http()
    kimlik_bilgileri.refresh(http)
    referans = kimlik_bilgileri.authorize(http)
    return build("drive", "v3", http=referans, cache_discovery=False)

yetkilendir()