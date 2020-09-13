class Birey:
    def __init__(self, ad, soyAd, yas):
        self.ad = ad
        self.soyAd = soyAd
        self.yas = yas

class Personel(Birey):
    def __init__(self, maas=""):
        self.maas = maas

class Musteri(Birey):
    def __init__(self, krediKart):
        self.krediKart = krediKart


#ali = Birey("Ali", "Savaş", 50)
ali = Personel()
ali.ad = "Ali"
ali.soyAd = "Çakıcı"
ali.yas = "58"
ali.maas = "1300"

print(f"{ali.ad} {ali.soyAd} | {ali.yas} >> {ali.maas}")
