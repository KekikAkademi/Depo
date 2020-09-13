from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel

from bs4 import BeautifulSoup
import requests

import sys
#####################################
class Pencere(QWidget):             # Penceremizi Oluşturduk
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        baslik = QLabel("")
        logo = QLabel()
        self.veriGirisi = QLineEdit()
        gonderButonu = QPushButton()
        self.alinanEntryler = QTextEdit()

        # Başlık
        baslik.setText('<h1><font color="green">Ekşi Sözlük Entry Alıcı</font></h1>')
        baslik.setFont(QFont("Helvatica",15,QFont.Bold))
        baslik.setAlignment(Qt.AlignCenter)

        # Logo
        logo.setPixmap(QPixmap(r"eksiLogo.png").scaled(100,100))
        logo.setAlignment(Qt.AlignCenter)

        # Buton
        gonderButonu.setIcon(QIcon(r"git.png"))
        gonderButonu.setText("işini Yap!")

        # Horizontal Box
        h_box = QHBoxLayout()
        h_box.addWidget(self.veriGirisi)
        h_box.addWidget(gonderButonu)

        # Vertical Box
        v_box = QVBoxLayout()
        v_box.addWidget(baslik)
        v_box.addWidget(logo)
        v_box.addWidget(self.alinanEntryler)
        v_box.addLayout(h_box)

        gonderButonu.clicked.connect(self.Uygulama)

        self.setLayout(v_box)
#########################################################
        self.show()                                     # Pencereyi göster
        self.setWindowTitle("Pencere Başlığı!")         # Pencere Başlığımızı Belirledik
        self.setWindowIcon(QIcon("eksiLogo.png"))       # Pencere İkonumuzu Belirledik
        self.setMinimumSize(QSize(750, 500))            # Pencere Min. Ebat Tanımladık
        self.setMaximumSize(QSize(750, 750))            # Pencere Max. Ebat Tanımladık
        #pencere.setGeometry(700,300,500,500)            # 700x300 kordinatında başlayarak / 500x500 ebatında aç

    def Uygulama(self):
        url = str(self.veriGirisi.text())
        kimlik = {'User-Agent': '@KekikAkademi'}  # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
        html = requests.get(url, headers=kimlik)  # link'in içerisindeki bütün html dosyasını indiriyoruz.
        kaynak = BeautifulSoup(html.content,"html5lib")  # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık

        liste = []
        for i in kaynak.find_all("div", attrs={"class": "content"}):
            liste.append(i.text)

        toplamYazi = ""
        for i in liste:
            toplamYazi = toplamYazi + i + "\n"

        self.alinanEntryler.setText(toplamYazi)


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)           # Uygulamamızı Oluşturduk
    pencere = Pencere()                         # Pencereyi göster
    sys.exit(uygulama.exec())                   # çıkış yapıldığı zaman, uygulamayı kapat