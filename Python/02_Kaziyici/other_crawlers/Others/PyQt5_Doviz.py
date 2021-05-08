#Buradaki kod çalışıyor fakat verileri siteden tek sefer çekebiliyor...
#start() fonksiyonunu Thread ile arkaplanda 5 saniye aralıkla çalıştırabilirsiniz.
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import time

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 147)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.alis_dolar = QtWidgets.QLabel(dialog)
        self.alis_dolar.setGeometry(QtCore.QRect(120, 32, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alis_dolar.setFont(font)
        self.alis_dolar.setObjectName("alis_dolar")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 79, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.satis_dolar = QtWidgets.QLabel(dialog)
        self.satis_dolar.setGeometry(QtCore.QRect(120, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.satis_dolar.setFont(font)
        self.satis_dolar.setObjectName("satis_dolar")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dolar"))
        self.label.setText(_translate("dialog", "Dolar Alış :"))
        self.alis_dolar.setText(_translate("dialog", "None"))
        self.label_3.setText(_translate("dialog", "Dolar Satış :"))
        self.satis_dolar.setText(_translate("dialog", "None"))

        self.start()
    
    def start(self):
        url = "https://canlidolar.com"
        r = requests.get(url)
        soup = BeautifulSoup(r.content,"lxml")
        self.dolar_alis = soup.find("span",{"id":"USDTRY_buy"}).text 
        self.dolar_satis = soup.find("span",{"id":"USDTRY_sell"}).text
        self.alis_dolar.setText(str(self.dolar_alis))
        self.satis_dolar.setText(str(self.dolar_satis))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())