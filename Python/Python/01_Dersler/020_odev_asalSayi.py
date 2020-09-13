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

    asalMi = True                           # Global değişken oluşturduk

    for i in range(2, sayi):                # 2 ile gelen sayı arasında döngü oluştur
        if (sayi % i) == 0:                 # eğer gelen sayı döngü sayısına bölümünden kalan 0 ise
            asalMi = False                  # global değişkeni False yap
            break                           # ve bu döngüyü kır, diğer sayıları bölüp kalanını kontrol etme

    if asalMi:                              # eğer global değişken (True ise)
        print("Asal")
    elif asalMi == False:                   # True değil de False ise
        print("Asal Değildir")
    else:                                   # Her ikisi de değil ise
        print("yooğğaaamınaa")