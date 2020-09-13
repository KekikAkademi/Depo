# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#-------------------------------#
import os,sys                   # Dizinler ve dosyalarla çalışmak için
import platform                 # Çalışılan makine bilgisi sağlayacak arkadaş
import time, datetime, pytz     # Zaman/Tarih Bilgisi sağlayacak arkadaşları
import requests                 # ip bilgisi almak için websitesine istek atıcak
import ctypes                   # C dili veri tipleri kullanmamızı sağlayacak arkadaş (.DLL / .SO)
import colorama                 # Ortalığın renklenmesini sağlayacak arkadaşı
#-------------------------------#
from colorama import Fore       # Boyamayı kolaylaştıran arkadaş (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
colorama.init(autoreset=True)   # Renklerin ilgili satırdan başka satıra devam etmemesi için
#-------------------------------#
import json                     #
from threading import Thread    #
import subprocess               #
#-------------------------------#

## GenelDegiskenler
pencere_basligi = "Nöbetçi Eczaneler"                               # Pencere Başlığımız
logo = '''
#              _          _       _   _____                         _           
#             | |        | |     (_) |  ___|                       | |          
#  _ __   ___ | |__   ___| |_ ___ _  | |__  ___ ______ _ _ __   ___| | ___ _ __ 
# | '_ \ / _ \| '_ \ / _ \ __/ __| | |  __|/ __|_  / _` | '_ \ / _ \ |/ _ \ '__|
# | | | | (_) | |_) |  __/ || (__| | | |__| (__ / / (_| | | | |  __/ |  __/ |   
# |_| |_|\___/|_.__/ \___|\__\___|_| \____/\___/___\__,_|_| |_|\___|_|\___|_|   
'''                                                                   # Logomuz
        # logo = http://patorjk.com/software/taag/#p=display&f=Doom&t=nobetci%20Eczaneler
#------------------------------------------------------------------------------------------------------------#
try: kullanici_adi = os.getlogin()                                              # Kullanıcı Adı
except: import pwd; kullanici_adi = pwd.getpwuid(os.geteuid())[0]               # Kullanıcı Adı
bilgisayar_adi = platform.node()                                                # Bilgisayar Adı
oturum = kullanici_adi + "@" + bilgisayar_adi                                   # Örn.: "kekik@Administrator"

isletim_sistemi = platform.system()                                             # İşletim Sistemi
bellenim_surumu = platform.release()                                            # Sistem Bellenim Sürümü
cihaz = isletim_sistemi + " | " + bellenim_surumu                               # Örn.: "Windows | 10"

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")     # Bugünün Tarihi
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")         # Bugünün Saati
zaman = tarih + " | " + saat

ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz
ip = ip_req.text                                # ip Adresi

ust_bilgi = f"""
    {Fore.LIGHTBLACK_EX}{kullanici_adi} | {cihaz} | {Fore.LIGHTGREEN_EX}{ip} 
          {Fore.YELLOW}{zaman}
    """                                                                         # Üst Bilgimiz
#------------------------------------------------------------------------------------------------------------#
def Temizle():
    if isletim_sistemi == "Windows": os.system("cls")
    else: os.system("clear")
Temizle()

def WindowsTerminaliGizle():
    if isletim_sistemi == "Windows":
        import win32console, win32gui
        terminal = win32console.GetConsoleWindow()
        win32gui.ShowWindow(terminal, 0)
    else:pass
#WindowsTerminaliGizle() # Eğer Windows'da Terminalin gizlenmesini istiyosanız aktifleştirin
                         # -- pyinstaller -i udemy.ico --onefile --noconsole KekikUdemyGUI.py --

def PencereBasligi():
    if isletim_sistemi == "Windows": ctypes.windll.kernel32.SetConsoleTitleW(f"{pencere_basligi}")
    elif isletim_sistemi == "Android": os.system("clear")
    elif isletim_sistemi == "Linux": os.system(f'echo "\033]0;{pencere_basligi}\007"')
    else: os.system(f'title {pencere_basligi}')
PencereBasligi()

def WindowsBildirimi():
    if isletim_sistemi == "Windows" and bellenim_surumu >= "10":
        from win10toast import ToastNotifier
        bildirim = ToastNotifier()
        bildirim.show_toast(f"{pencere_basligi}", "Telegram : @KekikAkademi", icon_path=None, duration=10, threaded=True)
    else:pass
WindowsBildirimi()
#------------------------------------------------------------------------------------------------------------------------#

def AcilisSayfasi():
    Temizle()
    print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
    print(ust_bilgi)                # Üst Bilgimizi yazdırdık
    print(f"""
    {Fore.GREEN}[{Fore.YELLOW} 1 {Fore.GREEN}] {Fore.CYAN}Crawl'dan Çek
    {Fore.GREEN}[{Fore.YELLOW} 2 {Fore.GREEN}] {Fore.CYAN}APi'den Çek
    """) # Seçeneklerimizi ayarladık

    konum = os.getcwd()
    if isletim_sistemi == "Windows": konum = konum.split("\\")
    elif isletim_sistemi == "Linux": konum = konum.split("/")
    else: konum = "/"

    secenek = str(input(
        f"{Fore.RED}{oturum}:{Fore.LIGHTBLUE_EX}~/../{konum[-2] + '/' + konum[-1]} >> {Fore.GREEN}")
        ) # Kullanıcı için input oluşturduk

    #-------------------------------------------------------------#
    if secenek == '1' or secenek == '01':
        from crawl.for_crawl import ECZANE

        il = str(input(f"\n\t{Fore.YELLOW}Lütfen İl Giriniz >> {Fore.GREEN}"))
        ilce = str(input(f"\n\t{Fore.YELLOW}Lütfen İlçe Giriniz >> {Fore.GREEN}"))

        if not il or not ilce: print("Lütfen il ve ilçe Giriniz"); time.sleep(1.5); AcilisSayfasi()

        data = ECZANE(il,ilce)

        jtopy = json.dumps(data)
        veri = json.loads(jtopy)

        for bilgi in veri['nobetciEczaneler']:
            print(f"""
        # : {bilgi['eczane_adi']}
        # : {bilgi['eczane_adresi']}
        # : {bilgi['eczane_telefonu']}
            """)

    #-------------------------------------------------------------#
    elif secenek == '2' or secenek == '02':
        il = str(input(f"\n\t{Fore.YELLOW}Lütfen İl Giriniz >> {Fore.GREEN}"))
        ilce = str(input(f"\n\t{Fore.YELLOW}Lütfen İlçe Giriniz >> {Fore.GREEN}"))

        try:
            #response = requests.get(f'http://127.0.0.1:5000/nobetciEczane/{il}/{ilce}')
            response = requests.get(f'http://127.0.0.1:5000/nobetciEczane?il={il}&ilce={ilce}')
        except: print("\n\tApi Başlatılmamış\n\n\t\tApi'yi Başlatın!"); time.sleep(3); AcilisSayfasi()

        data = response.text

        if not il or not ilce: print("Lütfen il ve ilçe Giriniz"); time.sleep(1.5); AcilisSayfasi()

        veri = json.loads(data)     # (data, encoding='utf-8')

        print(f"\n\tSunucu Zamanı : {veri['istek_zamanı']}")

        for bilgi in veri['nobetciEczaneler']:
            print(f"""
        # : {bilgi['eczane_adi']}
        # : {bilgi['eczane_adresi']}
        # : {bilgi['eczane_telefonu']}
                                    """)

    else:pass;Temizle();AcilisSayfasi()
#------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------#
if __name__ == '__main__':                  #
    Thread(target=AcilisSayfasi).start()    #

    # Burda sorun var!
    #subprocess.call('start /wait python api.py', shell=True)
#-------------------------------------------#