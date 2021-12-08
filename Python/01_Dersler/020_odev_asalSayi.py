while True:                                 # Sınırsız Döngü içerisinde programımızı çalıştırıyoruz
    sayi = input("sayı giriniz ")           # Kullanıcı'dan değişkene değer atamasını sağlıyoruz

    if sayi == "q":                         # eğer atadığı veri "q" ise
        print("Hoçça Galın Ben gittim")     # uyarı ver
        break                               # sınırsız döngüyü kır / programı kapat
    else:                                   # eğer atadığı veri "q" değil ise
        try:                                # dene
            sayi = int(sayi)                # değeri integer(tamsayı)'a çevirmeyi
        except:                             # eğer tamsayıya çeviremiyosan
            print("Ne diyon kardeş tekrar dene")
            continue                        # döngüyü bir tur atla

    asalMi = all(sayi % i != 0 for i in range(2, sayi))
    if asalMi:                              # eğer global değişken (True ise)
        print("Asal")
    else:
        print("Asal Değildir")