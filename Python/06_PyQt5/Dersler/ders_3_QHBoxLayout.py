from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def Buton1():                                   # Buton1 Fonksiyonumuz
    print("Buton 1'e Tıkladın..")               # Ekrana Yaz

def Buton2():                                   # Buton2 Fonksiyonumuz
    print("Buton 2'ye Tıkladın..")              # Ekrana Yaz

uygulama = QApplication(sys.argv)               # Uygulamamızı Oluşturduk
pencere = QDialog()                             # Penceremizi Oluşturduk
pencere.setWindowTitle("Pencere Başlığı!")      # Pencere Başlığımızı Belirledik
pencere.setGeometry(250,250,400,400)            # 250x250 kordinatında başlayarak / 400x400 ebatında aç
dikey = QHBoxLayout()                           # Dikey ölçekte dinamik yerleştir

buton_1 = QPushButton(pencere)                  # Pencere İçinde Buton Oluştur
buton_1.setText("Tıklama Alanı 1")              # Buton Yazısı Tanımladık
dikey.addWidget(buton_1)                        # Buton 1'i Dikey Ölçekte dinamik Yerleştir
buton_1.clicked.connect(Buton1)                 # Tıklandığı zaman Buton1 Fonksiyonunu Çalıştır

buton_2 = QPushButton(pencere)                  # Pencere İçinde Buton Oluştur
buton_2.setText("Tıklama Alanı 2")              # Buton Yazısı Tanımladık
dikey.addWidget(buton_2)                        # Buton 2'yi Dikey Ölçekte dinamik Yerleştir
buton_2.clicked.connect(Buton2)                 # Tıklandığı zaman Buton2 Fonksiyonunu Çalıştır

pencere.setLayout(dikey)                        # Pencereyi Dikey Ölçekte dinamik Çalıştır
pencere.show()                                  # Pencereyi göster
sys.exit(uygulama.exec())                       # çıkış yapıldığı zaman, uygulamayı kapat