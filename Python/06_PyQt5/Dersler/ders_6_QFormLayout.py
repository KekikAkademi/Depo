from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

uygulama = QApplication(sys.argv)               # Uygulamamızı Oluşturduk
pencere = QWidget()                             # Penceremizi Oluşturduk
pencere.setWindowTitle("Pencere Başlığı!")      # Pencere Başlığımızı Belirledik
#################################################
""""
form = QFormLayout()                            # Form Oluşturduk
form.addRow(QLabel("Adınız :"),QLineEdit())     # Form'a / Label ve LineEdit ekledik

cinsiyet = QLabel("Cinsiyet :")                 # Cinsiyet isimli bir Label oluşturduk
erkek = QRadioButton("Erkek")
kadin = QRadioButton("Kadın")

cinsiyet_secim = QHBoxLayout()
cinsiyet_secim.addWidget(erkek)
cinsiyet_secim.addStretch()
cinsiyet_secim.addWidget(kadin)

form.addRow(cinsiyet,cinsiyet_secim)

form.addRow(QPushButton("Gönder"))

pencere.setLayout(form)
"""

form = QFormLayout()

form.addRow(QLabel("Kulalnıcı Adı :"),QLineEdit())
sifre = QLineEdit()
sifre.setEchoMode(QLineEdit.Password)
form.addRow(QLabel("Şifre :"),sifre)
form.addRow(QLabel("Adres :"),QTextEdit())

cinsiyet_secim = QHBoxLayout()
erkek = QRadioButton("Erkek")
kadin = QRadioButton("Kadın")
cinsiyet_secim.addWidget(erkek)
#cinsiyet_secim.addStretch()
cinsiyet_secim.addWidget(kadin)

form.addRow(QLabel("Cinsiyet :"),cinsiyet_secim)

buton_secim = QHBoxLayout()
gonder = QPushButton("Gönder")
iptal = QPushButton("İptal")
buton_secim.addWidget(gonder)
#buton_secim.addStretch()
buton_secim.addWidget(iptal)

form.addRow(buton_secim)

pencere.setLayout(form)
#################################################
pencere.show()                                  # Pencereyi göster
sys.exit(uygulama.exec())                       # çıkış yapıldığı zaman, uygulamayı kapat