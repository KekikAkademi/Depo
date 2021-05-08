class Matematik:
    def __init__(self, sayi1, sayi2):
        print("init Çalışıyoo")
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def topla(self):
        return self.sayi1 + self.sayi2

    def cikar(self):
        return self.sayi1 - self.sayi2

    def carp(self):
        return self.sayi1 * self.sayi2

    def bol(self):
        return self.sayi1 / self.sayi2

islem = Matematik(5,2)

print(islem.topla())
print(islem.cikar())
print(islem.carp())
print(islem.bol())