from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

uygulama = QApplication(sys.argv)               # Uygulamamızı Oluşturduk
pencere = QWidget()                             # Penceremizi Oluşturduk
pencere.setWindowTitle("Pencere Başlığı!")      # Pencere Başlığımızı Belirledik
pencere.setGeometry(250,250,400,400)            # 250x250 kordinatında başlayarak / 400x400 ebatında aç

yazi = QLabel(pencere)                          # Pencere İçinde Yazı Oluştur
yazi.setText("Arayüzde bulunan bir yazı.")      # Yazıyı Yaz
yazi.move(125,200)                              # Pencere içinde 125x200 olan alana

pencere.show()                                  # Pencereyi göster
sys.exit(uygulama.exec())                       # çıkış yapıldığı zaman, uygulamayı kapat