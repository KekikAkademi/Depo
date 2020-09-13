# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qdarkgraystyle
import qdarkstyle
import sys, platform

def WindowsTerminaliGizle():
    if platform.system() == "Windows":
        import win32console, win32gui
        terminal = win32console.GetConsoleWindow()
        win32gui.ShowWindow(terminal, 0)
    else:
        pass
#WindowsTerminaliGizle()
# -- pyinstaller -i img/trendyol.ico --onefile --noconsole gui.py --

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        # Toplanma Alanı
        groupBox = QGroupBox("Trendyol Ürün Linki Veriniz")

        # vBox -- Dikey Yerleşim (Vertical Layout)
        vBox=QVBoxLayout()

        # hBox -- Yatay Yerleşim (Horizontal Layout)
        hBox = QHBoxLayout()
        #hBox.setGeometry(QRect(0, 0, 500, 150)) # x, y eksen | genişlik, yükseklik

        # json Ver Buton
        btnJSON=QPushButton("json Ver")
        btnJSON.setToolTip("<h5>Bas Bana!</h5>")
        btnJSON.clicked.connect(self.JsonClick)

        # input
        self.inputOlustur = QLineEdit()
        self.inputOlustur.setPlaceholderText("Lütfen 'ÜRÜN' Linki Giriniz..")
        self.inputOlustur.setToolTip("https://www.trendyol.com/kiwi/kj-1903-kati-meyve-sikacagi-p-33262682")

        # Output
        self.outputOlustur = QTextEdit()
        self.outputOlustur.setFont(QFont("Courier", 9))

        # Yatay Düzen'e(hBox'a) Yerleştir
        hBox.addWidget(self.inputOlustur)
        #hBox.addStretch()         # Dikey dinamik uzaklığı koru
        hBox.addWidget(btnJSON)

        # hBox'ı groupBox(Toplanma Alanı) içine Yerleştir
        groupBox.setLayout(hBox)

        # grupgroupBox'ı(Toplanma Alanını) Dikey Düzene(vBox'a) Ekle
        vBox.addWidget(groupBox)                                # groupBox'ı Layout olarak set edemeyeceğimiz için vBox içine attık
        vBox.addWidget(self.outputOlustur)                      # Dikey Düzene outputOlustur Ekle

        # Dikey Düzeni(vBox'ı) Çağır
        self.setLayout(vBox)                                    # vBox'ımızı Ana Yerleşim olarak belirle
        
        #-----------------------------------------------#
        self.show()                                     # Pencereyi göster
        self.setWindowTitle(f"Trendyol | Yorum")
        self.setWindowIcon(QIcon("img/trendyol.png"))
        self.setMinimumSize(QSize(600, 400))
        #self.setMaximumSize(QSize(600, 400))
        #self.setStyleSheet(qdarkgraystyle.load_stylesheet())
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        #pencere.setGeometry(700,300,500,500)           # 700x300 kordinatında başlayarak / 500x500 ebatında aç
        									            # "x" x "y" (ekseninde) / genişlik x yükseklik ile

    def JsonClick(self):
        import requests
        from bs4 import BeautifulSoup
        import json

        gelen = self.inputOlustur.text()
        self.inputOlustur.clear()

        try:
            urun, butik = gelen.split("?")
        except ValueError:
            urun = gelen

        link = urun + "/yorumlar"
        kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        istek = requests.get(link, headers=kimlik)
        soup = BeautifulSoup(istek.text, "html5lib")

        urun_ismi = soup.find('span', attrs={'class': 'product-name'})

        yorum_sahibi = []
        yildiz_sayisi = []
        kullanici_yorumu = []

        for yorum in soup.findAll('div', attrs={'class': 'pr-rnr-com'}):
            for i_yorum in yorum.findAll('p', attrs={'class': 'rnr-com-tx'}):
                kullanici_yorumu.append(i_yorum.text)
            for i_kullanici in yorum.findAll("span", attrs={'class': 'rnr-com-usr'}):
                yorum_sahibi.append(i_kullanici.text)
            for i_yildiz in yorum.findAll("div", attrs={'class': 'ratings readonly'}):
                yildiz = []
                for tek_yildiz in i_yildiz.findAll("div", attrs={'style': 'width:100%;max-width:100%'}):
                    yildiz.append(tek_yildiz)
                yildiz_sayisi.append(len(yildiz))

        liste = []
        for adet in range(0, len(yorum_sahibi)):
            sozluk = {}
            sozluk['yildiz'] = yildiz_sayisi[adet]
            sozluk['kullanici'] = yorum_sahibi[adet]
            sozluk['yorum'] = kullanici_yorumu[adet]
            liste.append(sozluk)

        sonuc = {"ad": urun_ismi.text, "link": urun, "yorumlar": liste}

        sonuc_json = json.dumps(sonuc, indent=2, sort_keys=True, ensure_ascii=False)

        json_yaz = open(f"{urun_ismi.text}.json", "w+", encoding='utf8')
        json_yaz.write(sonuc_json)
        json_yaz.close()

        self.outputOlustur.setText(f"\n\t\tjSon Oluşturuldu\n")

        yazilan_veri = json.loads(sonuc_json)

        self.outputOlustur.append(f"""{yazilan_veri['ad']}
Yorum Sayısı : {len(yorum_sahibi)}""")

        for bilgi in yazilan_veri['yorumlar']:
            self.outputOlustur.append(f"""
{bilgi['kullanici']} | {bilgi['yildiz']} Yıldız!
---------------------------------------------
{bilgi['yorum']}""")

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)           # Uygulamamızı Oluşturduk
    pencere = Pencere()                         # Pencereyi çağır
    sys.exit(uygulama.exec())                   # çıkış yapıldığı zaman, uygulamayı kapat