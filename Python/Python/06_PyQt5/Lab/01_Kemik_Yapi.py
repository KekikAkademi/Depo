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
        print("Kemik")

#########################################################
        self.show()                                     # Pencereyi göster
        self.setWindowTitle(f"Pencere Başlığı")         # Pencere Başlığımızı Belirledik
        self.setWindowIcon(QIcon("img/kekik.png"))      # Pencere İkonumuzu Belirledik
        self.setMinimumSize(QSize(750, 500))            # Pencere Min. Ebat Tanımladık
        self.setMaximumSize(QSize(750, 750))            # Pencere Max. Ebat Tanımladık
        #pencere.setGeometry(700,300,500,500)            # 700x300 kordinatında başlayarak / 500x500 ebatında aç

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)           # Uygulamamızı Oluşturduk
    pencere = Pencere()                         # Pencereyi göster
    sys.exit(uygulama.exec())                   # çıkış yapıldığı zaman, uygulamayı kapat