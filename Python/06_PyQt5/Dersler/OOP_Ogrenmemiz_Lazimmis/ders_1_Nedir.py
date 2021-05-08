# integer = 10
# string = "kekik" "akademi"

#%% Nasıl Değişken Tanımlarız?
integerDegisken = 33
stringDegisken = "KekikAkademi"

#%% Class Ne İşimize Yarar?
grupAdi = "KekikAkademi"
uyeSayisi = 33
yoneticiAdi = "keyiflerolsun"

class Telegram(object):
    # attribute(ozellik) = grupAdi, uyeSayisi, yoneticiAdi
    # behavior(davranis) = notlar, kurallar 
    pass

grup1 = Telegram()

# %% attribute
class Futbolcu:
    klup = "Barcelona"
    yas = 30

f1 = Futbolcu()

print(f1)
print(f1.yas)
print(f1.klup)

f1.klup = "Real Madrid"
print(f1.klup)

# %% methods
class Kare(object):                     # "Kare" _Class_'ını Oluşturduk
    kenar = 5   # metre
    alan = 0    # varsayılan değer
    def alanHesap(self):                # "alanHesap" _metod_unun içinde "self" kullanarak "Kare" _obje_sini kullandık
        self.alan = self.kenar * self.kenar # 5*5
        print("Alan: ", self.alan)

k1 = Kare()
print(k1)
print(k1.kenar)
k1.kenar = 7
k1.alanHesap()

# %% methods vs functions
class Isci(object):                     # Class / Obje
    yas = 25
    maas = 1000
    def yasMaasOrani(self):             # Metod
        print(f"Method : {self.yas / self.maas}")
isci1 = Isci()
isci1.yasMaasOrani()

#------------------------------------------------------
def yassMaasOrani(yas, maas):           # Fonksiyon
    print(f"Fonksiyon : {yas / maas}")
yassMaasOrani(25,1000)


def yassMaasOrani(a, b):           # a = yas, b = maas
    hesap = a / b
    #print(f"Fonksiyon input : {a / b}")
    return hesap                    # Elde Edilen Sonucu Fonksiyon Dışına Çıkart

yas = 25
maas = 1000

sonuc1 = yassMaasOrani(yas, maas)
sonuc2 = yassMaasOrani(yas, 2500)
sonuc3 = yassMaasOrani(18, 1300)

print(f"Sonuc : {sonuc1 + sonuc2 + sonuc3}")

# %% initializer or constructor (başlatıcı veya kurucu)
class Hayvan(object):       # Class Oluşturduk
    tur = "Köpek"           # Tür Belirledik
    yas = 2                 # Yas Belirledik
    def yasVer(self):       # Method Yazdık
        return self.yas     # Hayvanın Yaşını Döndür

hayvan_1 = Hayvan()                         # Hayvan oluştur
hayvan_1_yas = hayvan_1.yasVer()            # Yaşını çağır
print(f"Hayvan Yaşı : {hayvan_1_yas}")      # Ekrana Yazdır

#-----------------------------------------------------------

class Hayvan(object):                   # Class Oluşturduk
    def __init__(self, tur, yas):       # Class'ımızın Ana Yapısı
        self.tur = tur                  # Dışarıdan gelen "Tür"ü içerdeki Tür'e Eşitledik
        self.yas = yas                  # Dışarıdan gelen "Yaş"ı içerdeki Yaş'a Eşitledik
    def turVer(self):                   # Method Yazdık
        return self.tur                 # Hayvanın Yaşını Döndür
    def yasVer(self):                   # Method Yazdık
        return self.yas                 # Hayvanın Yaşını Döndür

a1 = Hayvan("Köpek", 2)                                     # Hayvan oluştur
print(f"{a1.tur} Hayvanı - {a1.yas} Yaşında")               # $
print(f"{a1.turVer()} Hayvanı - {a1.yasVer()} Yaşında")     # $


