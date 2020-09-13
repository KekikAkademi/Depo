from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def KekikAkademi():
    uygulama = QApplication(sys.argv)               # Uygulamamızı Oluşturduk
    pencere = QDialog()                             # Penceremizi Oluşturduk
    pencere.setWindowTitle("Pencere Başlığı!")      # Pencere Başlığımızı Belirledik
    pencere.setGeometry(250,250,400,400)            # 250x250 kordinatında başlayarak / 400x400 ebatında aç

    yazi = QLabel(pencere)                          # Pencere İçinde Yazı Oluştur
    yazi.setText("Arayüzde bulunan bir yazı.")      # Yazıyı Yaz
    yazi.move(125,200)                              # Pencere içinde 125x200 olan alana

    buton_1 = QPushButton(pencere)                  # Pencere İçinde Buton Oluştur
    buton_1.setText("Tıklama Alanı 1")              # Buton Yazısı Tanımladık
    buton_1.move(150,100)                           # Pencere içinde 150x100 olan alana yerleş
    buton_1.clicked.connect(Buton1)                 # Tıklandığı zaman Buton1 Fonksiyonunu Çalıştır

    buton_2 = QPushButton(pencere)                  # Pencere İçinde Buton Oluştur
    buton_2.setText("Tıklama Alanı 2")              # Buton Yazısı Tanımladık
    buton_2.move(150,150)                           # Pencere içinde 150x150 olan alana yerleş
    buton_2.clicked.connect(Buton2)                 # Tıklandığı zaman Buton2 Fonksiyonunu Çalıştır

    pencere.show()                                  # Pencereyi göster
    sys.exit(uygulama.exec())                       # çıkış yapıldığı zaman, uygulamayı kapat

def Buton1():                                       # Buton1 Fonksiyonumuz
    print("Buton 1'e Tıkladın..")                   # Ekrana Yaz

def Buton2():                                       # Buton2 Fonksiyonumuz
    print("Buton 2'ye Tıkladın..")                  # Ekrana Yaz

if __name__ == "__main__":                          # Sonsuz Döngüye Al
    KekikAkademi()                                  # KekikAkademi Fonksiyonunu