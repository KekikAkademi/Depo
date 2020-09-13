#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
#-------- @raifpy       > Ömer Rai'ye Sonsuz Teşekkürler..
#-------- @ykslkrkci    > Yüksel Kürekçi'ye Sonsuz Teşekkürler..

#################################
from PyQt5.QtCore import *      #
from PyQt5.QtGui import *       #
from PyQt5.QtWidgets import *   #
import sys                      #
#####################################
import qdarkstyle                   # Stil Sağlayan Arkadaş (https://github.com/ColinDuquesnoy/QDarkStyleSheet)
import qdarkgraystyle               # Stil Sağlayan Arkadaş (https://github.com/mstuttgart/qdarkgraystyle)
#################################################################################
from bs4 import BeautifulSoup       # HTML veya XML dosyalarını okuyan arkadaş  #
import html5lib                     # HTML dosyalarını işleyen arkadaş          #
import re                           # Ayrıştırıcı Arkadaş                       #
#########################################################################################################
import os                           # Dizinler ve dosyalarla çalışmak için                              #
import platform                     # Çalışılan makine bilgisi sağlayacak arkadaş                       #
import time, datetime, pytz         # Zaman/Tarih Bilgisi sağlayacak arkadaşlar                         #
import requests                     # Websitelerine istek atmamızı sağlayacak arkadaş                   #
#-------------------------------------------------------------------------------------------------------#
try:                                                                                                    #
    kullanici_adi = os.getlogin()                               # Kullanıcı Adı                         #
except:                                                                                                 #
    import pwd                                                                                          #
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]               # Kullanıcı Adı                         #
                                                                                                        #
bilgisayar_adi = platform.node()                                # Bilgisayar Adı                        #
oturum = kullanici_adi + "@" + bilgisayar_adi                   # Örn.: "kekik@Administrator"           #
                                                                                                        #
isletim_sistemi = platform.system()                     # İşletim Sistemi                               #
bellenim_surumu = platform.release()                    # Sistem Bellenim Sürümü                        #
cihaz = isletim_sistemi + " | " + bellenim_surumu       # Örn.: "Windows | 10"                          #
                                                                                                        #
tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")     # Bugünün Tarihi        #
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")         # Bugünün Saati         #
zaman = tarih + " | " + saat                                                    # 18-03-2020 | 02:30    #
                                                                                                        #
ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz    #
ip = ip_req.text                                # ip Adresi                                             #
                                                                                                        #
ust_bilgi = f"{kullanici_adi} | {cihaz} | {ip} \n\t{zaman}"     # Üst Bilgimiz                          #
pencere_basligi = "KekikUdemy Kupon Botu GUI | @KekikAkademi"   # Pencere Başlığımız                    #
#-------------------------------------------------------------------------------------------------------#####
def WindowsTerminaliGizle():                        # WindowsTerminaliGizle adında bir fonksiyon oluşturduk #
    if isletim_sistemi == "Windows":                # Eğer İşletim Sistemi "Windows" ise                    #
        import win32console, win32gui               # Gerekli Modüller                                      #
        terminal = win32console.GetConsoleWindow()  # Terminal adlı değişken                                #
        win32gui.ShowWindow(terminal, 0)            # Görünmez yap                                          #
    else:                                           # Eğer İşletim Sistemi "Windows" değilse                #
        pass                                        # Boşver :)                                             #
WindowsTerminaliGizle()     # Eğer Windows'da Terminalin gizlenmesini istiyosanız aktifleştirin             #
                            # -- pyinstaller -i udemy.ico --onefile --noconsole KekikUdemyGUI.py --         #
#############################################################################################################
#-----------------------------------------------------------------------------------------------------------#
class AnaSayfa(QMainWindow):
    def __init__(self):             #
        super().__init__()
        #--------------------------------------------------------------------------------------------------------------#
        self.show()                                                     # Pencereyi göster
        self.setWindowTitle(f"{pencere_basligi}")                       # Pencere Başlığımızı Belirledik
        self.setWindowIcon(QIcon("img/udemy.png"))                      # Pencere İkonumuzu Belirledik
        self.setMinimumSize(QSize(750, 500))                            # Pencere Min. Ebat Tanımladık
        self.setMaximumSize(QSize(750, 750))                            # Pencere Max. Ebat Tanımladık
        # pencere.setGeometry(700,300,500,500)                  # 700x300 kordinatında başlayarak / 500x500 ebatında aç
        self.setStyleSheet(open("style/style.qss", "r").read())         # Stil Dosyamızı Çağırdık
        #self.setStyleSheet(qdarkgraystyle.load_stylesheet())            # Stil Kütüphanemizi Çağırdık
        #self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))  # Stil Kütüphanemizi Çağırdık
        #--------------------------------------------------------------------------------------------------------------#
        self.TumEkran()             # TumEkran'ı Çağırdık
        self.Malzeme()              # Malzeme'yi Çağırdık

    def TumEkran(self):             # TumEkran Adında Bir Fonksiyon Oluşturduk
        menuBar = self.menuBar()                        # menuBar değişkenine menuBar() tanımladık
        #-------------------------------------------------------------------------------------------------------#
        ### Dosya İşlemleri
        dosya = menuBar.addMenu("Dosya")                # "menuBar" değişkenimize "Dosya" Adında menü oluşturduk

        dosya_ac = QAction("Dosya Aç", self)            # Self Yazmazsam Ana Pencerede Görünmez
        dosya_ac.setShortcut("Ctrl+O")                  # Kısa Yol Tuşu

        dosya_kaydet = QAction("Dosya Kaydet", self)    # Self Yazmazsam Ana Pencerede Görünmez
        dosya_kaydet.setShortcut("Ctrl+S")              # Kısa Yol Tuşu

        temizle = QAction("Temizle", self)              # Aksiyon Belirledik
        temizle.setShortcut("Ctrl+D")                   # Kısa Yol Tuşu

        cikis = QAction("Çıkış", self)                  # Aksiyon Belirledik
        cikis.setShortcut("Ctrl+Q")                     # Kısa Yol Tuşu

        dosya.addAction(dosya_ac)                       # "Dosya" isimli menümüze aksiyonu yönlendirdik
        dosya.addAction(dosya_kaydet)                   # "Dosya" isimli menümüze aksiyonu yönlendirdik
        dosya.addAction(temizle)                        # "Dosya" isimli menümüze aksiyonu yönlendirdik
        dosya.addAction(cikis)                          # "Dosya" isimli menümüze aksiyonu yönlendirdik

        dosya.triggered.connect(self.BarTepki)          # "Dosya"'daki aksiyonlarımızı BarTepki'ye yönlendirdik
        #-------------------------------------------------------------------------------------------------------#

        #---------------------------------------------------------------------------------------------#
        ### Temalar
        tema = menuBar.addMenu("Tema Değiştir")         # "menuBar" değişkenimizde menü oluşturduk

        mavimsi_tema = QAction("Mavimsi Tema", self)    # Aksiyon Belirledik
        mavimsi_tema.setShortcut("ALT+1")               # Kısa Yol Tuşu

        kara_tema = QAction("Kara Tema", self)          # Aksiyon Belirledik
        kara_tema.setShortcut("ALT+2")                  # Kısa Yol Tuşu

        tema.addAction(mavimsi_tema)                    # Menümüze aksiyonu yönlendirdik
        tema.addAction(kara_tema)                       # Menümüze aksiyonu yönlendirdik

        tema.triggered.connect(self.BarTepki)           # Aksiyonlarımızı BarTepki'ye yönlendirdik
        #-----------------------------------------------------------------------------------------#
        ### Hakkında
        hakkinda = menuBar.addMenu("Hakkında")          # "menuBar" değişkenimizde menü oluşturduk
        hakkinda.addAction("Hakkında")                  # Aksiyon Belirledik
        hakkinda.triggered.connect(self.BarTepki)       # Aksiyonu BarTepki'ye yönlendirdik
        # -----------------------------------------------------------------------------------------#

    def Malzeme(self):              # Malzeme Adında Bir Fonksiyon Oluşturduk
        #---------------------------------------------------------------------#
        malzeme = QWidget(self)     # "malzeme" değişkenine Pencere Tanımladık
        #---------------------------------------------------------------------#

        # vBox -- Dikey Yerleşim (Vertical Layout)
        malzeme.vBox = QVBoxLayout()

        # hBox -- Yatay Yerleşim (Horizontal Layout)
        malzeme.hBox = QHBoxLayout()

        # Başlık
        baslik = QLabel()
        baslik.setText(f'<h1><font color="green">{pencere_basligi}</font></h1>')
        baslik.setFont(QFont("Helvatica", 15, QFont.Bold))
        baslik.setAlignment(Qt.AlignCenter)

        # Sistem
        sistem = QLabel()
        sistem.setText(ust_bilgi)
        sistem.setFont(QFont("Courier", 12, QFont.Bold))
        sistem.setAlignment(Qt.AlignCenter)

        # Alınan Kurslar
        self.alinanKurslar = QTextEdit()

        # Çekilecek Sayfa
        self.cekilecekSayfa = QLineEdit()
        self.cekilecekSayfa.setPlaceholderText("Kaç Sayfa Çekilsin?")

        # discUdemy
        discUdemy = QPushButton()
        discUdemy.setIcon(QIcon(r"img/discUdemy.png"))
        discUdemy.setText("discUdemy")
        discUdemy.clicked.connect(self.DiscUdemy)

        # 2.Sekme İçin
        sekme2 = QPushButton("Sekme 2")
        #sekme2.clicked.connect(self.mouseDoubleClickEvent())

        # realDiscount
        realDiscount = QPushButton()
        realDiscount.setIcon(QIcon(r"img/realDiscount.png"))
        realDiscount.setText("realDiscount")
        realDiscount.clicked.connect(self.RealDiscount)

        # Yatay Düzen'e(hBox'a) Yerleştir
        malzeme.hBox.addWidget(self.cekilecekSayfa)
        #hBox.addStretch()                              # Dikey dinamik uzaklığı koru
        malzeme.hBox.addWidget(discUdemy)
        #hBox.addStretch()                              # Dikey dinamik uzaklığı koru
        malzeme.hBox.addWidget(realDiscount)
        #hBox.addWidget(sekme2)                          # Yan Sekme için butonu

        # Dikey Düzen'e(vBox'a) Yerleştir
        malzeme.vBox.addWidget(baslik)
        malzeme.vBox.addWidget(sistem)
        malzeme.vBox.addWidget(self.alinanKurslar)
        malzeme.vBox.addLayout(malzeme.hBox)
        #------------------------------------------------------------------------#
        malzeme.setLayout(malzeme.vBox)
        self.setCentralWidget(malzeme)  ## https://stackoverflow.com/a/37306238
        #------------------------------------------------------------------------#

    def BarTepki(self,action):      # BarTepki Adında Bir Fonksiyon Oluşturduk
        #---------------------------------------------------------------------------------------------------------#
        ### Dosya İşlemleri
        if action.text() == "Dosya Aç":
            dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç", filter="Tüm Dosyalar (*);;Python (*.py)")
            with open(dosya_ismi[0], "r", encoding='utf-8-sig') as gelen_dosya:
                self.alinanKurslar.setText(gelen_dosya.read())

        if action.text() == "Dosya Kaydet":
            dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet", filter="Çıkışlar TxT (*.txt)")
            with open(dosya_ismi[0], "w", encoding='utf-8-sig') as gelen_dosya:
                gelen_dosya.write(self.alinanKurslar.toPlainText())

        if action.text() == "Temizle":
            self.alinanKurslar.clear()

        if action.text() == "Çıkış":
            qApp.quit()
        #---------------------------------------------------------------------------------------------------------#
        
        #--------------------------------------#
        ### Temalar
        if action.text() == "Mavimsi Tema":
            self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        if action.text() == "Kara Tema":
            self.setStyleSheet(qdarkgraystyle.load_stylesheet())
        #--------------------------------------#
        
        #----------------------------------------------------------------------------------------------------------------#
        ### Hakkında
        if action.text() == "Hakkında":
            self.hakkinda_pencere = QWidget()                                           # Penceremizi Oluşturduk
            self.hakkinda_pencere.show()                                                # Penceremizi Açtık
            self.hakkinda_pencere.setWindowTitle(f"{action.text()} / {pencere_basligi}")# Pencere Başlığımızı Belirledik
            self.hakkinda_pencere.setWindowIcon(QIcon("img/udemy.png"))                 # Pencere İkonumuzu Belirledik
            self.hakkinda_pencere.setStyleSheet(open("style/style.qss", "r").read())    # Stil Dosyamızı Çağırdık

            self.vBox = QVBoxLayout()

            # Logo
            self.logo = QLabel()
            self.logo.setPixmap(QPixmap(r"img/KekikAkademiQt5Logo.png"))
            self.logo.setAlignment(Qt.AlignCenter)

            # Açıklama
            self.aciklama = QLabel()
            self.aciklama.setText("""@keyiflerolsun tarafından Eğitim Amaçlı Yazılmıştır.
            Telegram Kanalımıza Bekleriz: @KekikAkademi""")
            self.aciklama.setFont(QFont("Courier", 16, QFont.Bold))
            self.aciklama.setAlignment(Qt.AlignTop | Qt.AlignCenter)

            self.vBox.addWidget(self.aciklama)
            self.vBox.addWidget(self.logo)

            self.hakkinda_pencere.setLayout(self.vBox)
        #----------------------------------------------------------------------------------------------------------------#

    def DiscUdemy(self):            # DiscUdemy Adında Bir Fonksiyon Oluşturduk
        def Deneysel():
            self.disc_pencere = QDialog()                                           # Penceremizi Oluşturduk
            self.disc_pencere.show()                                                # Penceremizi Açtık
            self.disc_pencere.setWindowTitle(f"DiscUdemy / {pencere_basligi}")      # Pencere Başlığımızı Belirledik
            self.disc_pencere.setWindowIcon(QIcon("img/udemy.png"))                 # Pencere İkonumuzu Belirledik
            self.disc_pencere.setStyleSheet(open("style/style.qss", "r").read())    # Stil Dosyamızı Çağırdık
            self.disc_pencere.setMaximumSize(QSize(750, 250))                       # Pencere Max. Ebat Tanımladık

            self.vBox = QVBoxLayout()

            # Veri
            self.veri = QLabel()
            self.veri.setText("Burada Loading Ekranı Olacak")
            self.veri.setAlignment(Qt.AlignCenter)

            self.vBox.addWidget(self.veri)

            self.disc_pencere.setLayout(self.vBox)
        #Deneysel()
        #-------------------------------------------------------------------------------------------#
        udemy_baslik = []                                                   # Boş Tablo Oluşturduk  #
        udemy_link = []                                                     # Boş Tablo Oluşturduk  #
        #-------------------------------------------------------------------------------------------#
        gelen_rakam = int(self.cekilecekSayfa.text()) + 1                   # gelen veriyi rakama çevir 1 ekle

        self.alinanKurslar.append(f"{gelen_rakam - 1} Sayfa Çekilecek \n\n\t Program Çalışırken Tıklama Yapmayın!\n")  # TextEdit'e ekle
        self.alinanKurslar.repaint()                                        # TextEdit'i güncelle

        for sayfa in range(1, gelen_rakam):                            # Sayfa Sayısı | örn:(1, 3) {2 Sayfa Tarar [1-2]}
            #----------------------------------------------------------------------------------------------------------------------------------#
            sayfa = str(sayfa)                                              # int olan değerimizi str yapıyoruz
            link = 'https://www.discudemy.com/language/Turkish/' + sayfa    # sayfalar arasında gezinmek için
            kimlik = {'User-Agent': '@KekikAkademi'}                        # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
            istek = requests.get(link)                                      # link'e istek göderiyoruz ve gelen veriyi kaydediyoruz
            kaynak = BeautifulSoup(istek.text, 'html5lib')                  # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık

            self.alinanKurslar.append(f"\t[*] {link} | Burdayım !\n")       # TextEdit'e ekle
            self.alinanKurslar.repaint()                                    # TextEdit'i güncelle
            #sleep(1)                                                        # Bekleme Ver
            #----------------------------------------------------------------------------------------------------------------------------------#

            #---------------------------------------------------------------------------------------------------------------------#
            for heading in kaynak.findAll('a', {'class': 'card-header'}):   # kaynak'tan | <a class'ı = card-header olanları tut
                heading = heading.text                                      # Yazı Formatına Çevir
                udemy_baslik.append(heading)                                # Tablomuza Yerleştir
            #sleep(1)                                                        # Bekleme Ver
            #---------------------------------------------------------------------------------------------------------------------#

            #-----------------------------------------------------------------------------------------------------------------------#
            for discudemy_linkler in kaynak.findAll('a', attrs={                        # kaynak'tan | <a olanları _ ve
                'href': re.compile("^https://www.discudemy.com/Turkish/")}):            # href="../Turkish/' olan linkleri tut
                gelen_discudemy = discudemy_linkler['href']                             # dönen verideki linkleri tut
                discudemy_go_html = requests.get(gelen_discudemy)                       # onlara istek gönder
                discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'html5lib') # kaynağını al
                self.alinanKurslar.append(f"[/] {gelen_discudemy} | Burdayım !\n")      # TextEdit'e ekle
                self.alinanKurslar.repaint()                                            # TextEdit'i güncelle
                #sleep(1)                                                                # Bekleme Ver

                #-------------------------------------------------------------------------------------------------------------------#
                for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={    # aldığın kaynaktan | <a olanları _ ve
                    'href': re.compile("^https://www.discudemy.com/go/")}):             # href="../go/kurs-adi" olan linkleri tut
                    gelen_discudemy_go = discudemy_go_linkler['href']                   # dönen verideki linkleri tut
                    udemy_html = requests.get(gelen_discudemy_go)                       # onlara istek gönder
                    udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')           # kaynağını al
                    self.alinanKurslar.append(f"[/] {gelen_discudemy_go} | Burdayım !\n")# TextEdit'e ekle
                    self.alinanKurslar.repaint()                                        # TextEdit'i güncelle
                    #sleep(1)                                                            # Bekleme Ver

                    #---------------------------------------------------------------------------------------------------------------#
                    for udemy_linkler in udemy_kaynak.findAll('a', attrs={              # aldığın kaynaktan | <a olanları _ ve
                        'href': re.compile("^https://www.udemy.com/")}):                # href="../www.udemy.com/" olan linkleri tut
                        gelen_udemy = udemy_linkler['href']                             # dönen verideki linkleri tut
                        udemy_link.append(gelen_udemy)                                  # Tablomuza Yerleştir
                        self.alinanKurslar.append(f"[+] {gelen_udemy} | BULDUM !\n\n")  # TextEdit'e ekle
                        self.alinanKurslar.repaint()                                    # TextEdit'i güncelle
                        #sleep(1)                                                        # Bekleme Ver
            #-----------------------------------------------------------------------------------------------------------------------#

        #-------------------------------------------------------------------------------------------------------------------------#
        for adet in range(0, len(udemy_baslik)):                    # 0'dan Başlayarak, Dönen "başlık" sayısı kadar "adet" oluştur
            gelen_udemy_kaydet = open("DiscUdemy.txt", "a+")        # .txt oluştur
            gelen_udemy_kaydet.write(f"{udemy_baslik[adet]}\n")     # Başlık[adet] yaz satır atla
            gelen_udemy_kaydet.write(f"{udemy_link[adet]}\n\n")     # Link[adet] Yaz satır atla, satır atla
            gelen_udemy_kaydet.close()                              # dosyayı kapat
        #-------------------------------------------------------------------------------------------------------------------------#

        #---------------------------------------------------------------------------#
        icerik = open("DiscUdemy.txt", "r+").read()                 # Dosyayı oku   #
        self.alinanKurslar.setText(icerik)                          # Ekrana Yaz    #
        #---------------------------------------------------------------------------#

    def RealDiscount(self):         # RealDiscount Adında Bir Fonksiyon Oluşturduk
        #-------------------------------------------------------------------------------------------------------#
        gelen_rakam = int(self.cekilecekSayfa.text()) + 1                   # gelen veriyi rakama çevir 1 ekle

        self.alinanKurslar.append(f"{gelen_rakam - 1} Sayfa Çekilecek \n\n\t Program Çalışırken Tıklama Yapmayın!\n")  # TextEdit'e ekle
        self.alinanKurslar.repaint()                                        # TextEdit'i güncelle
        # -------------------------------------------------------------------------------------------------------#
        for sayfa in range(1, gelen_rakam):  # Sayfa Sayısı | örn:(1, 3) {2 Sayfa Tarar [1-2]}
            #------------------------------------------------------------------------------------------------------------------------#
            sayfa = str(sayfa)                                  # int olan değerimizi str yapıyoruz
            link = 'https://www.real.discount/new/' + sayfa     # sayfalar arasında gezinmek için
            kimlik = {'User-Agent': '@KekikAkademi'}            # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
            html = requests.get(link, headers=kimlik)           # link'in içerisindeki bütün html dosyasını indiriyoruz.
            kaynak = BeautifulSoup(html.text, "html5lib")       # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık
            #------------------------------------------------------------------------------------------------------------------------#

            self.alinanKurslar.append(f"\t[*] {link} | Burdayım !\n")       # TextEdit'e ekle
            self.alinanKurslar.repaint()                                    # TextEdit'i güncelle
            
            #------------------------------------------------------------------------------------------------------------------------#
            for discount_linkler in kaynak.findAll('a', attrs={'href': re.compile("^https://www.real.discount/offer/")}):
                gelen_discount = discount_linkler['href']

                self.alinanKurslar.append(f"[/] {gelen_discount} | Burdayım !\n")   # TextEdit'e ekle
                self.alinanKurslar.repaint()                                        # TextEdit'i güncelle
                #------------------------------------------------------------------------------------------------------------------------#
                udemy_html = requests.get(gelen_discount, headers=kimlik)
                udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')
                for udemy_linkler in udemy_kaynak.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/")}): # o sayfanın içindeki udemy linki
                    gelen_udemy = udemy_linkler['href']

                    self.alinanKurslar.append(f"[+] {gelen_udemy} | BULDUM !\n\n")  # TextEdit'e ekle
                    self.alinanKurslar.repaint()                                    # TextEdit'i güncelle
                    #----------------------------------------------------#
                    gelen_udemy_kaydet = open("UdemyeGiderken.txt", "a")
                    gelen_udemy_kaydet.write(gelen_udemy + "\n")
                    gelen_udemy_kaydet.close()
                    #----------------------------------------------------#
        
        #---------------------------------------------------------#
        lines_seen = set()              # holds lines already seen
        outfile = open("RealDiscount.txt", "a")
        for line in open("UdemyeGiderken.txt", "r"):
            if line not in lines_seen:  # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()
        os.remove("UdemyeGiderken.txt")
        #---------------------------------------------------------#
        #---------------------------------------------------------------------------#
        icerik = open("RealDiscount.txt", "r+").read()              # Dosyayı oku   #
        self.alinanKurslar.setText(icerik)                          # Ekrana Yaz    #
        #---------------------------------------------------------------------------#
            
if __name__ == "__main__":
    uygulama = QApplication(sys.argv)           # Uygulamamızı Oluşturduk
    pencere = AnaSayfa()                        # Penceremizi Oluşturkuk
    sys.exit(uygulama.exec())                   # Çıkış yapıldığı zaman, uygulamayı kapat