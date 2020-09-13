import sys
from PyQt5 import QtWidgets

class Window2(QtWidgets.QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2. Penceren Hayırlı Olsun")
        self.yazi1 = QtWidgets.QLabel("")
        self.yazi2 = QtWidgets.QLabel("")
        self.buton = QtWidgets.QPushButton("Tıkla Bakalım")


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi1)
        v_box.addWidget(self.buton)
        
        wid = QtWidgets.QWidget(self)  ## QMainWindow'a layout set edebilmek
        wid.setLayout(v_box)  ## icin QWidget olusturmak gerekiyormus
        self.setCentralWidget(wid)  ## https://stackoverflow.com/a/37306238


        self.buton.clicked.connect(self.click1)

        self.top = 100
        self.left = 100
        self.width = 250
        self.height = 250
        self.setGeometry(self.top,self.left, self.width,self.height)


    def click1(self):
        self.yazi1.setText("Yüksel")

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.yazi = QtWidgets.QLabel("")
        self.buton1 = QtWidgets.QPushButton("Tıkladım.")
        self.checkbox = QtWidgets.QCheckBox("Lütfen İşaretleyiniz.")
        self.buton2 = QtWidgets.QPushButton("Sayfa 2")

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        #v_box.addWidget(self.yazi)


        v_box.addWidget(self.checkbox)
        v_box.addStretch()
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.buton1)
        v_box.addWidget(self.buton2)

        self.setLayout(v_box)
        self.setWindowTitle("@ykslkrkci")
        self.setGeometry(100,100,200,200)
        self.setMaximumSize(250,250)
        self.setMinimumSize(200,200)

        self.buton1.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi))
        self.buton2.clicked.connect(self.window2)
        self.show()
    def click(self,checkbox, yazi):
        if checkbox:
            yazi.setText("Ne Güzel Tıkladın Öyle :))")
        else:
            yazi.setText("İşaretlemeyi Unuttun :(")

    def window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

#pencere.setWindowTitle("Deneme")

sys.exit(app.exec_())