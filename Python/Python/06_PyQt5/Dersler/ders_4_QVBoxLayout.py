from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def Buton1():                                   # Buton1 Fonksiyonumuz
    print("Buton 1'e Tıkladın..")               # Ekrana Yaz

def Buton2():                                   # Buton2 Fonksiyonumuz
    print("Buton 2'ye Tıkladın..")              # Ekrana Yaz

def Buton3():                                   # Buton3 Fonksiyonumuz
    print("Buton 3'e Tıkladın..")               # Ekrana Yaz

def Buton4():                                   # Buton4 Fonksiyonumuz
    print("Buton 4'e Tıkladın..")               # Ekrana Yaz

uygulama = QApplication(sys.argv)               # Uygulamamızı Oluşturduk
pencere = QDialog()                             # Penceremizi Oluşturduk
pencere.setWindowTitle("Pencere Başlığı!")      # Pencere Başlığımızı Belirledik
pencere.setGeometry(250,250,400,400)            # 250x250 kordinatında başlayarak / 400x400 ebatında aç

b1 = QPushButton("Tıklama Alanı 1")             # Buton 1 Oluştur
b1.clicked.connect(Buton1)                      # Tıklandığı zaman Buton1 Fonksiyonunu Çalıştır

b2 = QPushButton("Tıklama Alanı 2")             # Buton 2 Oluştur
b2.clicked.connect(Buton2)                      # Tıklandığı zaman Buton1 Fonksiyonunu Çalıştır

b3 = QPushButton("Tıklama Alanı 3")             # Buton 3 Oluştur
b3.clicked.connect(Buton3)                      # Tıklandığı zaman Buton1 Fonksiyonunu Çalıştır

b4 = QPushButton("Tıklama Alanı 4")             # Buton 4 Oluştur
b4.clicked.connect(Buton4)                      # Tıklandığı zaman Buton1 Fonksiyonunu Çalıştır

yatay = QVBoxLayout()                           # VerticalBox
dikey = QHBoxLayout()                           # HorizontalBox

yatay.addWidget(b1)                             # Yatay ölçekte dinamik yerleştir
yatay.addStretch()                              # Yatay dinamik uzaklığı koru
yatay.addWidget(b2)                             # Yatay ölçekte dinamik yerleştir

dikey.addWidget(b3)                             # Dikey ölçekte dinamik yerleştir
dikey.addStretch()                              # Yinamik dinamik uzaklığı koru
dikey.addWidget(b4)                             # Dikey ölçekte dinamik yerleştir

yatay.addLayout(dikey)                          # dikey olanı yatay olanın içine koy
pencere.setLayout(yatay)                        # yatay olanı pencereye ekle

pencere.show()                                  # Pencereyi göster
sys.exit(uygulama.exec())                       # çıkış yapıldığı zaman, uygulamayı kapat