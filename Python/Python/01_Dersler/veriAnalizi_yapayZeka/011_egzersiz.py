class Personel():
    def __init__(self, ad, soyAd, ucret):
        self.ad = ad
        self.soyAd = soyAd
        self.ucret = ucret

    def gorevi(self):
        print(f"{self.ad} {self.soyAd} | {self.ucret}TL")

class Muhendis(Personel):
    def __init__(self, ad, soyAd, ucret, pozisyon):
        super().__init__(ad, soyAd, ucret)
        self.pozisyon = pozisyon

    def gorevi(self):
        super().gorevi()
        print("Yazılım Geliştiriyorum.")

class Muhasebeci(Personel):
    def __init__(self, ad, soyAd, ucret, tecrube):
        super().__init__(ad, soyAd, ucret)
        self.tecrube = tecrube

    def gorevi(self):
        super().gorevi()
        print("Şirket Hesaplarını Yönetiyorum.")








muh = Muhendis("Musa", "Çevik", 4500, "Uzman")
muh.gorevi()
print(muh.pozisyon)

print()

muha = Muhasebeci("Haydar", "Baş", 3000, "15 Yıllık Tecrübe")
muha.gorevi()
print(muha.tecrube)