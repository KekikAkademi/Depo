# hesap makinesi projesi
# class -> init -> method/attribute -> funct vs method

class HesapMakinesi(object):            # Class Oluşturduk
    "hesap makinesi"

    # init methodu
    def __init__(self, a, b):           # Class'ımızın Ana Yapısı Tanımladık (initializer/başlatıcı Method)
        "değerleri başlat"
        # attribute (özellik)
        self.deger1 = a
        self.deger2 = b
    
    def toplama(self):                  # Method Oluşturduk
        "toplama a + b = sonuç -> sonuç döndür"
        return self.deger1 + self.deger2
         
    def carpma(self):                   # Method Oluşturduk
        "çarpma a * b = sonuç -> sonuç döndür"
        return self.deger1 * self.deger2
    
    def bolme(self):                    # Method Oluşturduk
        "bölme a / b = sonuç -> sonuç döndür"
        return self.deger1 / self.deger2
#-----------------------------------------------------------------
print("Seçim | toplama(1), carpma(2), div(3)")      # Bilgilendirme Yazısı
secim = input("Lüfen Seçim Yapın! 1 - 2 - 3 : ")    # Seçim Alanı

deger_1 = int(input("ilk değer : "))                # Seçim Alanı
deger_2 = int(input("ikinci değer : "))             # Seçim Alanı

sonuc = HesapMakinesi(deger_1,deger_2)              # Sonuç Alanı

if secim == "1":                                    # Eğer Seçim 1 ise
    toplama_result = sonuc.toplama()                # Değerleri Topla
    print(f"Toplam : {toplama_result}")             # Ekrana Yaz
elif secim == "2":                                  # Eğer Seçim 2 ise
    carpma_result = sonuc.carpma()                  # Değerleri Çarp
    print(f"Çarpım : {carpma_result}")              # Ekrana Yaz
elif secim == "3":                                  # Eğer Seçim 2 ise
    bolme_result = sonuc.bolme()                    # Değerleri Böl
    print(f"Bölüm : {bolme_result}")                # Ekrana Yaz
else:                                               # Eğer Seçim hiçbiri değil ise
    print("Hata! Lütfen Doğru Seçim Yapın..")       # Hata Mesajı ver