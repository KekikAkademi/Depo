class Birey:
    def __init__(self, ad, soyAd, yas):
        self.ad = ad
        self.soyAd = soyAd
        self.yas = yas

class Personel(Birey):
    def __init__(self, ad, soyAd, yas, maas=None):
        super().__init__(ad, soyAd, yas)
        self.maas = maas

class Musteri(Birey):
    def __init__(self, ad, soyAd, yas, krediKart):
        super().__init__(ad, soyAd, yas)
        self.krediKart = krediKart


ali = Personel("Ali", "Çakıcı", 50, 1500)

print(f"{ali.ad} {ali.soyAd} | {ali.yas} >> {ali.maas}")