class Anne():
    def annesi(self):
        print("Annesine Benzedi")

class Baba():
    def babasi(self):
        print("Babasına Benzedi")

class Cocuk(Anne, Baba):
    pass


Cocuk().babasi()

Cocuk().annesi()