#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
# @raifpy > Ömer Rai'ye Sonsuz Teşekkürler..

#-------------------------------#
import os                       # Dizinler ve dosyalarla çalışmak için
import platform                 # Çalışılan makine bilgisi sağlayacak arkadaş
import time,datetime,pytz       # Zaman/Tarih Bilgisi sağlayacak arkadaşlar
import ctypes                   # C dili veri tipleri kullanmamızı sağlayacak arkadaş (.DLL / .SO)
import colorama                 # Ortalığın renklenmesini sağlayacak arkadaş
from colorama import Fore       # Boyamayı kolaylaştıran arkadaş (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
colorama.init(autoreset=True)   # Renklerin ilgili satırdan başka satıra devam etmemesi için
import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş
import html5lib                 # HTML dosyalarını işleyen arkadaş
import re                       # Ayrıştırıcı Arkadaş
from time import sleep          # sleep() için
#-------------------------------#

#---------------------------------------------------------------#
## GenelDegiskenler
pencere_basligi = "@KekikAkademi UDEMY Kupon Çekme Aracı"       # Pencere Başlığımız
logo = '''
   _    _      _     _ _        _     _     _                   
  | |  / )    | |   (_) |      | |   | |   | |                  
  | | / / ____| |  _ _| |  _   | |   | | _ | | ____ ____  _   _ 
  | |< < / _  ) | / ) | | / )  | |   | |/ || |/ _  )    \| | | |
  | | \ ( (/ /| |< (| | |< (   | |___| ( (_| ( (/ /| | | | |_| |
  |_|  \_)____)_| \_)_|_| \_)   \______|\____|\____)_|_|_|\__  |
                                                         (____/   
'''                                                             # Logomuz
        # logo = http://patorjk.com/software/taag/#p=display&f=Doom&t=kopya%20Kagidi
#---------------------------------------------------------------#
try:
    kullanici_adi = os.getlogin()                                     # Kullanıcı Adı
except:
    import pwd
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]                     # Kullanıcı Adı
bilgisayar_adi = platform.node()                                      # Bilgisayar Adı
oturum = kullanici_adi + "@" + bilgisayar_adi                         # Örn.: "kekik@Administrator"

isletim_sistemi = platform.system()                                        # İşletim Sistemi
bellenim_surumu = platform.release()                                       # Sistem Bellenim Sürümü
cihaz = isletim_sistemi + " | " + bellenim_surumu                          # Örn.: "Windows | 10"

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y") # Bugünün Tarihi
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")     # Bugünün Saati
zaman = tarih + " | " + saat

ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz
ip = ip_req.text                                # ip Adresi

ust_bilgi = f"""
    {Fore.LIGHTBLACK_EX}{kullanici_adi} | {cihaz} | {Fore.LIGHTGREEN_EX}{ip} 
          {Fore.YELLOW}{zaman}
    """                                         # Üst Bilgimiz
#-----------------------------------------------#

#---------------------------------------#
def Temizle():                          # Temizle adında bir fonksiyon oluşturduk
    if isletim_sistemi == "Windows":    # Eğer İşletim Sistemi "Windows" ise
        os.system("cls")                # Sisteme "cls" komutu gönder
    else:                               # Sistem Windows değil ise
        os.system("clear")              # Sisteme "clear" komutu gönder
Temizle()                               # Temizle fonksiyonumuzu çağırdık
#---------------------------------------#

#---------------------------------------------------------------------------#
def PencereBasligi():                                                       # PencereBasligi fonksiyonu
    if isletim_sistemi == "Windows":                                        # Eğer İşletim Sistemi "Windows" ise
        ctypes.windll.kernel32.SetConsoleTitleW(f"{pencere_basligi}")       # Konsol Başlığını ayarla
    elif isletim_sistemi == "Android":                                      # Eğer İşletim Sistemi "Android" ise
        os.system("clear")                                                  # Sisteme "clear" komutu gönder
    elif isletim_sistemi == "Linux":                                        # Eğer İşletim Sistemi "Linux" ise
        os.system(f'echo "\033]0;{pencere_basligi}\007"')                   # Başlık Ayarla
    else:                                                                   # Hiçbiri değil ise
        os.system(f'title {pencere_basligi}')                               # Başlık Ayarla
PencereBasligi()                                                            # PencereBasligi çağır
#---------------------------------------------------------------------------#

#----------------------------------------------------#
def WindowsBildirimi():                              # WindowsBildirimi adında bir metod oluşturduk
    if isletim_sistemi == "Windows" and bellenim_surumu >= "10":    # Windows ve 10'a büyük eşitse
        from win10toast import ToastNotifier         # Windows'a bildirim göndermek için
        bildirim = ToastNotifier()
        bildirim.show_toast(f"{pencere_basligi}", "Başlıyoruz :)", icon_path=None, duration=10, threaded=True)
    else:
        pass
WindowsBildirimi()
#----------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------------#
def DiscUdemy():
    #-------------------------------------------------------------------------------------------#
    udemy_baslik = []                                                   # Boş Tablo Oluşturduk  #
    udemy_link = []                                                     # Boş Tablo Oluşturduk  #
    #-------------------------------------------------------------------------------------------#

    for sayfa in range(1, 3):                                           # Sayfa Sayısı | örn:(1, 3) {2 Sayfa Tarar [1-2]}
        #----------------------------------------------------------------------------------------------------------------------------------#
        sayfa = str(sayfa)                                              # int olan değerimizi str yapıyoruz
        link = 'https://www.discudemy.com/language/Turkish/' + sayfa    # sayfalar arasında gezinmek için
        kimlik = {'User-Agent': '@KekikAkademi'}                        # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
        istek = requests.get(link)                                      # link'e istek göderiyoruz ve gelen veriyi kaydediyoruz
        kaynak = BeautifulSoup(istek.text, 'html5lib')                  # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık
        print(f"\t{Fore.RED}[*] {link} {Fore.CYAN}| {Fore.RED}Burdayım !")# Bulunduğun Link'i Terminale Yazdır
        print("\t\t Değişken : // link\n")                              # ilgili Değişkeni Terminale Yazdır
        #sleep(1)                                                        # Bekleme Ver
        #----------------------------------------------------------------------------------------------------------------------------------#

        #---------------------------------------------------------------------------------------------------------------------#
        for heading in kaynak.findAll('a', {'class': 'card-header'}):   # kaynak'tan | <a class'ı = card-header olanları tut
            heading = heading.text                                      # Yazı Formatına Çevir
            udemy_baslik.append(heading)                                # Tablomuza Yerleştir
        print(f"\tBaşlık Yakaladım : {Fore.LIGHTBLACK_EX}{udemy_baslik}")
        print("\t\t Değişken : // udemy_baslik\n")                      # ilgili Değişkeni Terminale Yazdır
        #sleep(1)                                                        # Bekleme Ver
        #---------------------------------------------------------------------------------------------------------------------#

        #-----------------------------------------------------------------------------------------------------------------------#
        for discudemy_linkler in kaynak.findAll('a', attrs={                        # kaynak'tan | <a olanları _ ve
            'href': re.compile("^https://www.discudemy.com/Turkish/")}):            # href="../Turkish/' olan linkleri tut
            gelen_discudemy = discudemy_linkler['href']                             # dönen verideki linkleri tut
            discudemy_go_html = requests.get(gelen_discudemy)                       # onlara istek gönder
            discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'html5lib') # kaynağını al
            print(f"{Fore.LIGHTBLACK_EX}[/] {gelen_discudemy} {Fore.CYAN}| {Fore.LIGHTBLACK_EX}Burdayım !")
            print(f"\t {Fore.LIGHTBLUE_EX}Değişken : // gelen_discudemy\n")          # ilgili Değişkeni Terminale Yazdır
            #sleep(1)                                                                # Bekleme Ver

            #-------------------------------------------------------------------------------------------------------------------#
            for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={    # aldığın kaynaktan | <a olanları _ ve
                'href': re.compile("^https://www.discudemy.com/go/")}):             # href="../go/kurs-adi" olan linkleri tut
                gelen_discudemy_go = discudemy_go_linkler['href']                   # dönen verideki linkleri tut
                udemy_html = requests.get(gelen_discudemy_go)                       # onlara istek gönder
                udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')           # kaynağını al
                print(f"{Fore.LIGHTBLACK_EX}[/] {gelen_discudemy_go} {Fore.CYAN}| {Fore.LIGHTBLACK_EX}Burdayım !")
                print(f"\t {Fore.LIGHTBLUE_EX}Değişken : // gelen_discudemy_go\n")   # ilgili Değişkeni Terminale Yazdır
                #sleep(1)                                                            # Bekleme Ver

                #---------------------------------------------------------------------------------------------------------------#
                for udemy_linkler in udemy_kaynak.findAll('a', attrs={              # aldığın kaynaktan | <a olanları _ ve
                    'href': re.compile("^https://www.udemy.com/")}):                # href="../www.udemy.com/" olan linkleri tut
                    gelen_udemy = udemy_linkler['href']                             # dönen verideki linkleri tut
                    udemy_link.append(gelen_udemy)                                  # Tablomuza Yerleştir
                    print(f"{Fore.GREEN}[+] {Fore.YELLOW}{gelen_udemy} {Fore.CYAN}| {Fore.GREEN}Buldum !")
                    print(f"\t {Fore.LIGHTBLUE_EX}Değişken : // gelen_udemy\n")      # ilgili Değişkeni Terminale Yazdır
                    #sleep(1)                                                        # Bekleme Ver
        #-----------------------------------------------------------------------------------------------------------------------#

    #-------------------------------------------#
    print("\n\n\n\tSiliyorum...")               # Sildiğini Bildir
    sleep(2)                                    # 2sn Bekle
    os.system("cls")                            # Terminal'i Temizle
    print("\n\n\n\tKursları Listeliyorum...")   # Listelediğini Bildir
    sleep(2)                                    # 2sn Bekle
    os.system("cls")                            # Terminal'i Temizle
    #-------------------------------------------#

    #-------------------------------------------------------------------------------------------------------------------------#
    for adet in range(0, len(udemy_baslik)):                    # 0'dan Başlayarak, Dönen "başlık" sayısı kadar "adet" oluştur
        gelen_udemy_kaydet = open("DiscUdemy.txt", "a+")        # .txt oluştur
        gelen_udemy_kaydet.write(f"{Fore.RED}{udemy_baslik[adet]}\n")     # Başlık[adet] yaz satır atla
        gelen_udemy_kaydet.write(f"{Fore.CYAN}{udemy_link[adet]}\n\n")     # Link[adet] Yaz satır atla, satır atla
        gelen_udemy_kaydet.close()                              # dosyayı kapat
    #-------------------------------------------------------------------------------------------------------------------------#

    #---------------------------------------------------------------------------#
    icerik = open("DiscUdemy.txt", "r+").read()                 # Dosyayı oku   #
    print(icerik)                                               # Ekrana Yaz    #
    #---------------------------------------------------------------------------#

    #---------------------------------------------------------------------------------------------#
    satir_say = open("DiscUdemy.txt")
    satir = 0
    for line in satir_say:
        satir = satir+1
    print(f"\n\t{Fore.YELLOW} Bulunup, Yazılan Link Sayısı{Fore.YELLOW} >> {Fore.RED}" + f"{int(satir/3)}")
    satir_say.close()
    os.remove("DiscUdemy.txt")                                  # Dosyayı Sil  /Fore.İle Yazıldı 
    #---------------------------------------------------------------------------------------------#

def RealDiscount():
    for sayfa in range(1, 2):                               # Sayfa Sayısı | örn:(1, 3) {2 Sayfa Tarar [1-2]}
        #------------------------------------------------------------------------------------------------------------------------#
        sayfa = str(sayfa)                                  # int olan değerimizi str yapıyoruz
        link = 'https://www.real.discount/new/' + sayfa     # sayfalar arasında gezinmek için
        kimlik = {'User-Agent': '@KekikAkademi'}            # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
        html = requests.get(link, headers=kimlik)           # link'in içerisindeki bütün html dosyasını indiriyoruz.
        kaynak = BeautifulSoup(html.text, "html5lib")       # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık
        print(f"\t{Fore.RED}[*] {link} {Fore.CYAN}| {Fore.RED}Burdayım !")
        #------------------------------------------------------------------------------------------------------------------------#

        #------------------------------------------------------------------------------------------------------------------------#
        for discount_linkler in kaynak.findAll('a', attrs={'href': re.compile("^https://www.real.discount/offer/")}):
            gelen_discount = discount_linkler['href']
            print(f"{Fore.LIGHTBLACK_EX}[/] {gelen_discount} {Fore.CYAN}| {Fore.LIGHTBLACK_EX}Burdayım !")

            #------------------------------------------------------------------------------------------------------------------------#
            udemy_html = requests.get(gelen_discount, headers=kimlik)
            udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')
            for udemy_linkler in udemy_kaynak.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/")}): # o sayfanın içindeki udemy linki
                gelen_udemy = udemy_linkler['href']
                print(f"{Fore.GREEN}[+] {Fore.YELLOW}{gelen_udemy} {Fore.CYAN}| {Fore.GREEN}Buldum !\n") # gelen_udemy değerimizi (linkimizi) yazdık

                #----------------------------------------------------#
                gelen_udemy_kaydet = open("UdemyeGiderken.txt", "a")
                gelen_udemy_kaydet.write(gelen_udemy + "\n")
                gelen_udemy_kaydet.close()
                #----------------------------------------------------#

    #---------------------------------------------------------------------------------------------#
    satir_say = open("UdemyeGiderken.txt")
    satir = 0
    for line in satir_say:
        satir = satir+1
    print(f"\n\t{Fore.GREEN} Bulunup, Yazılan Link Sayısı{Fore.YELLOW} >> {Fore.RED}{satir}")
    satir_say.close()
    #---------------------------------------------------------------------------------------------#

def CiftLinkSil():
    #---------------------------------------------------------#
    lines_seen = set()              # holds lines already seen
    outfile = open("RealDiscount.txt", "a")
    for line in open("UdemyeGiderken.txt", "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.remove("UdemyeGiderken.txt")
    print("\n\t\t" + Fore.YELLOW + "Çift Linkler Bulunup Silindi ve RealDiscount.txt Kaydedildi!!!" + Fore.WHITE + "\n")
    #---------------------------------------------------------#

    #---------------------------------------------------------#
    satir_say = open("RealDiscount.txt")
    satir = 0
    for line in satir_say:
        satir = satir+1
    print(f"\n\t{Fore.GREEN} Kalan Link Sayısı{Fore.YELLOW} >> {Fore.RED}{satir}")
    satir_say.close()
    #---------------------------------------------------------#

#-----------------------------------#
def AcilisSayfasi():
    print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
    print(ust_bilgi)                # Üst Bilgimizi yazdırdık
    print(f"""
    {Fore.GREEN}[{Fore.YELLOW} 1 {Fore.GREEN}] {Fore.CYAN}Discudemy TR Linkleri (3 Sayfa Tarar)
    {Fore.GREEN}[{Fore.YELLOW} 2 {Fore.GREEN}] {Fore.CYAN}RealDiscount Linkleri (2 Sayfa Tarar)
    """) # Seçeneklerimizi ayarladık

    konum = os.getcwd()
    if isletim_sistemi == "Windows":
        konum = konum.split("\\")
    elif isletim_sistemi == "Linux":
        konum = konum.split("/")
    else:
        konum = "/"
    secenek = str(input(f"{Fore.RED}{oturum}:{Fore.LIGHTBLUE_EX}~/../{konum[-2] + '/' + konum[-1]} >> {Fore.GREEN}")) # Kullanıcı için input oluşturduk
    #-----------------------#
    if secenek == '1':      # Eğer 1 i seçerse
        Temizle()           # Temizle fonksiyonunu çalıştır
        print(Fore.LIGHTBLUE_EX + logo)
        print(ust_bilgi)    # Üst Bilgi fonksiyonunu çalıştır
        DiscUdemy()         # DiscUdemy fonksiyonunu çalıştır
    #-----------------------#
    elif secenek == '2':    # Eğer 2 yi seçerse
        Temizle()           # Temizle fonksiyonunu çalıştır
        print(Fore.LIGHTBLUE_EX + logo)
        print(ust_bilgi)    # Üst Bilgi fonksiyonunu çalıştır
        RealDiscount()      # RealDiscount fonksiyonunu çalıştır
        CiftLinkSil()
    #-----------------------#
    else:                   # Eğer harici bişey seçerse
        pass                # Aldırış etme (çökme)
        Temizle()           # Temizle fonksiyonunu çalıştır
        AcilisSayfasi()     # AcilisSayfasi fonksiyonunu çalıştır

AcilisSayfasi()