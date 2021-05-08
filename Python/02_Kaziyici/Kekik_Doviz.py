#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import time,datetime,pytz,os,platform        # OturumBilgisi sağlayacak arkadaşlar
import requests                              # İstek gönderici arkadaşımız
from bs4 import BeautifulSoup                # Ayrıştırıcı arkadaşımız
import ctypes                                # CMD ekran başlığı oluşturabilmek için
import colorama                              # Ortalığın renklenmesi için
from colorama import Fore                    # Ortalığın renklenmesi için
colorama.init(autoreset=True)                # Renklerin satırdan başka devam etmemesi için

##########################################################################################################################################
# Önce çalışma alanımızı oluşturuyoruz
Sistem = platform.system() # Betiğin çalıştığı işletim sistemini öğreniyoruz

def Temizle(): # Temizle adında bir metod oluşturduk
    if Sistem == "Windows": # Eğer Sistem Windows ise
        os.system("cls") # Sisteme "cls" komutu gönder
    else: # Sistem Windows değil ise
        os.system("clear") # Sisteme "clear" komutu gönder
Temizle() # Temizle metodumuzu çağırdık

SistemKullaniciAdi = os.getlogin() # Sistem Kullanıcı Adı
Tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y") # Bugünün Tarihini Alıyoruz
Saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M") # Bugünün Saatini Alıyoruz

def KonsolBasligi(): # KonsolBasligi adında bir metod oluşturduk
    if Sistem == "Windows": # Eğer Sistem Windows ise
        ctypes.windll.kernel32.SetConsoleTitleW("@KekikAkademi Canlı Döviz Kuru Takip Betiği | {} {} | {}".format(SistemKullaniciAdi, Sistem, Saat)) # Pencere başlığı oluştur
KonsolBasligi()

def OturumBilgisi(): # OturumBilgisi adında bir metod oluşturduk
    print("\n\t" + Fore.YELLOW + SistemKullaniciAdi  + Fore.GREEN + "\tMerhaba!\t\n\n" + Fore.CYAN + Tarih + Fore.MAGENTA +"\t|\t" + Fore.RED + Saat + "\n") # Anlık oturum ve tarh bilgisini ekranımıza yazıyoruz.
OturumBilgisi() # OturumBilgisi metodumuzu çağırdık

def WindowsBildirimi(): # WindowsBildirimi adında bir metod oluşturduk
    if Sistem == "Windows":
        from win10toast import ToastNotifier         # Windows'a bildirim göndermek için
        Bildirim = ToastNotifier()
        Bildirim.show_toast("Güncellendi!", "Veriler Güncel", icon_path=None, duration=3, threaded=True)
##########################################################################################################################################

# Hadi Yapalım Şu İşi
def Doviz(): # Doviz adında bir metod oluşturduk
    WindowsBildirimi() # OturumBilgisi metodumuzu çağırdık <<<< Başka projede bunu istediğiniz yerde çağırabilirsiniz..
    # Tanımlamalarımızı Yapalım
    URL = "https://www.doviz.com/"
    Kimlik = {'User-Agent': '@KekikAkademi'} # Websitesine istek yollarken kimlik bilgimizi sunuyoruz

    # WebSitesinin Cevabına bakalım (ilk kontrol)
    #Cevap = requests.get(URL, headers=Kimlik)
    #print(Cevap)

    # Sorun yoksa devam edelim
    Kaynak = requests.get(URL, headers=Kimlik).text # Url'nin içerisindeki bütün html dosyasını indiriyoruz.
    SayfaOku = BeautifulSoup(Kaynak , "html.parser")
    #print(SayfaOku) # bakalım bize gelen veri görüntülenen ile aynı mı?(ikinci kontrol)

    # Siteye girdik. Ne Alıcaz Burdan?
    isim = [] # içerisine veri ekleyeceğimiz boş tablo
    rakam = [] # içerisine veri ekleyeceğimiz boş tablo
    oran = [] # içerisine veri ekleyeceğimiz boş tablo

    # Hadi Kazıyalım!
    for AyristirilanAlan in SayfaOku.findAll('div', attrs={'class':'market-data'}):
        #print(AyristirilanAlan) # ilk ayrıştırmamızı yaptık
        #print(AyristirilanAlan.text) # Bir de kodlardan arındırıp bakalım

        # Parçalamaya devam edelim
        for birinci in AyristirilanAlan.findAll('span', attrs={'class':'name'}):
            #print(birinci) # Bakalım ne geldi
            gelenisim = birinci.text # kodlarından ayıralım
            #print(isim) # kontrol edelim, olmuşsa devam
            isim.append(gelenisim) # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            #Tablo kontrolünü "print(isim)" döngünün dışında yapmayı unutma !

        # şimdi de rakamları çekelim
        for ikinci in AyristirilanAlan.findAll('span', attrs={'class':'value'}):
            #print(ikinci) # Bakalım ne geldi
            gelenrakam = ikinci.text # kodlarından ayıralım
            #print(gelenrakam) # kontrol edelim, olmuşsa devam
            rakam.append(gelenrakam) # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            ## Tablo kontrolünü "print(rakam)" döngünün dışında yapmayı unutma !

        # oranları da çekersek tamamdır
        for ucuncu in AyristirilanAlan.findAll('div', attrs={'class':'change'}):
            #print(ucuncu) # Bakalım ne geldi
            gelenoran = ucuncu.text # kodlarından ayıralım
            #print(gelenoran) # kontrol edelim, boşluklarımız var. boşlukları yok etmeliyiz..
            gelenoran = gelenoran.replace("\n", "") # boşlukları kaldır
            #print(gelenoran) # hala değil
            gelenoran = gelenoran.replace(" ", "") # boşlıkları kaldır :)
            #print(gelenoran) # tamamdır :)
            oran.append(gelenoran) # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            ## Tablo kontrolünü "print(oran)" döngünün dışında yapmayı unutma !

    # Tablolarımızı kontrol edelim
    #print(isim)
    #print(rakam)
    #print(oran)
    # haaarika
    
    for i in range(0,len(isim)): # döngüyü isim tablosunun elemanı kadar sürdür
        print(Fore.MAGENTA + "*"*30 + "\n" + Fore.GREEN + "{} ".format(isim[i]) + Fore.RED + ">>" + Fore.YELLOW + " {} ".format(rakam[i]) + Fore.RED + ">>" + Fore.CYAN + " {}".format(oran[i]) + "\n" + Fore.MAGENTA + "*"*30)

    print("\n\t" + Fore.YELLOW + "Teşekkürler doviz.com")
    
    time.sleep(10) # DDoS gibi olmaması için 10 saniye aralık la yap bu işi
    Temizle() # Temizle metodumuzu çağırdık
    OturumBilgisi() # OturumBilgisi metodumuzu çağırdık

# Betiği sonsuz döngüye alıyoruz
while True:
    Doviz() # Doviz metodumuzu çağırdık