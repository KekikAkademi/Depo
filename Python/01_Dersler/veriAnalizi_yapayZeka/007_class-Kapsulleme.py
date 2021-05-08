class Araba():
    def __init__(self, marka, model, renk):
        self.marka = marka
        self.model = model
        self.renk = renk


ilkAraba = Araba("Opel", "Korsa", "Kırmızı")

print(ilkAraba)
print(f"{ilkAraba.marka} | {ilkAraba.model} | {ilkAraba.renk}")



"Özel Verilere Erişim Engelleme"

class Vatandas():
    def __init__(self):
        self.ad = "Mehmet"
        self.soyAd = "Can"
        self.__vatandaslikNo = "1111111111"         # Kapsülleme

    def verTC(self):
        return self.__vatandaslikNo

    def olusturTC(self, yeniTC):
        self.__vatandaslikNo = yeniTC

ilkVatandas = Vatandas()

print(ilkVatandas)
print(f"{ilkVatandas.ad} | {ilkVatandas.soyAd} | {ilkVatandas.verTC()}")

ilkVatandas.olusturTC("5555555555555")
print(f"Yeni Kimlik Numarası {ilkVatandas.verTC()}")