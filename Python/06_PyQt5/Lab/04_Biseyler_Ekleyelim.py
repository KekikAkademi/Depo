#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#################################
from PyQt5.QtCore import *      #
from PyQt5.QtGui import *       #
from PyQt5.QtWidgets import *   #
import sys                      #
#################################
#####################################
class Pencere(QWidget):             # Penceremizi Oluşturduk
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        # Toplanma Alanı
        groupBox = QGroupBox("Favori Spor Seçiminiz nedir ?")

        # vBox -- Dikey Yerleşim (Vertical Layout)
        vBox=QVBoxLayout()                                      # Dikey Yerleşim Planı

        # hBox -- Yatay Yerleşim (Horizontal Layout)
        hBox = QHBoxLayout()
        hBox.setGeometry(QRect(0, 0, 500, 150))                 # x, y eksen | genişlik, yükseklik

        # Futbol Buton
        btnFutbol=QPushButton("Futbol")                         # Buton Başlığı
        btnFutbol.setIcon(QIcon("img/futbol.png"))              # ikon yolu
        btnFutbol.setIconSize(QSize(15,15))                     # genişlik, yükseklik
        btnFutbol.setToolTip("<h5>Futbol Butonu</h5>")          # PyQt5 içinde HTML etiket çalıştırabiliriz
        btnFutbol.setGeometry(QRect(20,40,150,150))             # x, y eksen | genişlik, yükseklik
        btnFutbol.clicked.connect(self.FutbolTiklanirsa)        # Tıklandığı zaman

        # Basketbol Buton
        btnBasketbol=QPushButton("Basketbol")                   # Buton Başlığı
        btnBasketbol.setIcon(QIcon("img/basketbol.png"))        # ikon yolu
        btnBasketbol.setIconSize(QSize(15,15))                  # genişlik, yükseklik
        btnBasketbol.setToolTip("<h5>Basketbol Butonu</h5>")    # PyQt5 içinde HTML etiket çalıştırabiliriz
        btnBasketbol.setGeometry(QRect(20,40,150,150))          # x, y eksen | genişlik, yükseklik
        btnBasketbol.clicked.connect(self.BasketbolTiklanirsa)  # Tıklandığı zaman

        # Golf Buton
        btnGolf=QPushButton("Golf")                             # Buton Başlığı
        btnGolf.setIcon(QIcon("img/golf.png"))                  # ikon yolu
        btnGolf.setIconSize(QSize(15,15))                       # genişlik, yükseklik
        btnGolf.setToolTip("<h5>Golf Butonu</h5>")              # PyQt5 içinde HTML etiket çalıştırabiliriz
        btnGolf.setGeometry(QRect(20,40,150,150))               # x, y eksen | genişlik, yükseklik
        btnGolf.clicked.connect(self.GolfTiklanirsa)            # Tıklandığı zaman

        # input / Output
        self.inputOlustur = QLineEdit()                                     # input satırı ekle
        self.inputOlustur.setPlaceholderText("Hey Merhaba!")                # input için ipucu ekle
        self.inputOlustur.setToolTip("Üzerinde Bekleyince Çıkan Yazı")      # input için aksiyon ekle
        self.outputOlustur = QTextEdit()                                    # output için paragraf ekle

        # Yatay Düzen'e(hBox'a) Yerleştir
        hBox.addWidget(self.inputOlustur)                       # Yatay Düzene inputOlustur Ekle
        hBox.addWidget(btnFutbol)                               # Yatay Düzene btnFutbol Ekle
        hBox.addWidget(btnBasketbol)                            # Yatay Düzene btnBasketbol Ekle
        hBox.addWidget(btnGolf)                                 # Yatay Düzene btnGolf Ekle

        # Yeni bi değişkende grup'Landır
        groupBox.setLayout(hBox)                                # Hbox'ı groupBox(Toplanma Alanı) içine attık .

        # grupgroupBox'ı(Toplanma Alanını) Dikey Düzene(vBox'a) Ekle
        vBox.addWidget(groupBox)                                # groupBox'ı Layout olarak set edemeyeceğimiz için vBox içine attık
        vBox.addWidget(self.outputOlustur)                      # Dikey Düzene outputOlustur Ekle

        # Dikey Düzeni(vBox'ı) Çağır
        self.setLayout(vBox)                                    # vBox'ımızı Ana Yerleşim olarak belirle
        
#########################################################
        self.show()                                     # Pencereyi göster
        self.setWindowTitle(f"Pencere Başlığı")         # Pencere Başlığımızı Belirledik
        self.setWindowIcon(QIcon("img/kekik.png"))      # Pencere İkonumuzu Belirledik
        #self.setMinimumSize(QSize(750, 500))            # Pencere Min. Ebat Tanımladık
        self.setMaximumSize(QSize(750, 750))            # Pencere Max. Ebat Tanımladık
        #pencere.setGeometry(700,300,500,500)           # 700x300 kordinatında başlayarak / 500x500 ebatında aç
        									            # "x" x "y" (ekseninde) / genişlik x yükseklik ile
    def FutbolTiklanirsa(self):
        print("Futbola Tıkladılar Amca!")
        gelen = self.inputOlustur.text()
        self.outputOlustur.setText(f"Futbola'a Bunu Yazdın : {gelen}")

    def BasketbolTiklanirsa(self):
        print("Basketbola Tıkladılar Amca!")
        gelen = self.inputOlustur.text()
        self.outputOlustur.setText(f"Basketbol'a Bunu Yazdın : {gelen}")

    def GolfTiklanirsa(self):
        print("Golfe Tıkladılar Amca!")
        gelen = self.inputOlustur.text()
        self.outputOlustur.setText(f"Golf'e Bunu Yazdın : {gelen}")

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)           # Uygulamamızı Oluşturduk
    pencere = Pencere()                         # Pencereyi çağır
    sys.exit(uygulama.exec())                   # çıkış yapıldığı zaman, uygulamayı kapat