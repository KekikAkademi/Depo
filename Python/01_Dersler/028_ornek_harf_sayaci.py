class HarfSayacı:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuü'
        self.sayaç = 0

    def kelime_sor(self):
        return input('Bir kelime girin: ')

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç += 1
        return self.sayaç

    def ekrana_bas(self):
        sesli_harf_sayısı = self.artır()
        print(f"{self.kelime} kelimesinde {sesli_harf_sayısı} sesli harf var.")

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()


sayaç = HarfSayacı()
sayaç.çalıştır()

##

sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

for harf in kelime:
    if harf in sesli_harfler:
        sayaç += 1

print(f'{kelime} kelimesinde {sayaç} sesli harf var.')