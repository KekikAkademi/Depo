from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

uygulama = QApplication(sys.argv)               # Uygulamamızı Oluşturduk
pencere = QWidget()                             # Penceremizi Oluşturduk
pencere.setWindowTitle("Pencere Başlığı!")      # Pencere Başlığımızı Belirledik
pencere.setGeometry(250,250,400,400)            # 250x250 kordinatında başlayarak / 400x400 ebatında aç
izgara = QGridLayout()                          # Izgaramızı Oluşturduk

b1 = izgara.addWidget(QPushButton("Tıklama Alanı 1"),1,1)    # Buton 1'i 1. Satır 1. Sütunda Oluştur
b2 = izgara.addWidget(QPushButton("Tıklama Alanı 2"),1,2)    # Buton 2'yi 1. Satır 2. Sütunda Oluştur
b3 = izgara.addWidget(QPushButton("Tıklama Alanı 3"),2,1)    # Buton 3'ü 2. Satır 1. Sütunda Oluştur
b4 = izgara.addWidget(QPushButton("Tıklama Alanı 4"),2,2)    # Buton 4'ü 2. Satır 2. Sütunda Oluştur
b5 = izgara.addWidget(QPushButton("Tıklama Alanı 5"),3,1)    # Buton 5'i 3. Satır 1. Sütunda Oluştur
b6 = izgara.addWidget(QPushButton("Tıklama Alanı 6"),3,2)    # Buton 6'yı 3. Satır 2. Sütunda Oluştur

"""
for satir in range(3):          # veya 1,4
    for sutun in range(2):      # veya 1,3
        #for buton in range(6):
            #izgara.addWidget(QPushButton(f"Tıklama Alanı {buton}"),satir,sutun)
        for yazi in range(6):
            izgara.addWidget(QLabel(f"Satır:{satir} / Sütun:{sutun}"),satir,sutun)
"""

pencere.setLayout(izgara)                       # Izgarayı pencereye ekle

pencere.show()                                  # Pencereyi göster
sys.exit(uygulama.exec())                       # çıkış yapıldığı zaman, uygulamayı kapat