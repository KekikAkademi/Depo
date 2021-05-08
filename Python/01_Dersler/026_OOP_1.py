class Matematik:
    def topla(self, sayi1, sayi2):
        return sayi1 + sayi2

    def cikar(self, sayi1, sayi2):
        return sayi1 - sayi2

    def carp(self, sayi1, sayi2):
        return sayi1 * sayi2

    def bol(self, sayi1, sayi2):
        return sayi1 / sayi2

islem = Matematik()

print(islem.topla(5,2))
print(islem.cikar(5,2))
print(islem.carp(5,2))
print(islem.bol(5,2))