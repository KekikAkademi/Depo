for _ in range(1, 10):                              # while = 'iken
    print("bilgisayar yine çıldırdı!")

print()
print()
b = 1

while b == 1:
    sayi = int(float(input("sayı giriniz (99)> ")))     # input direkt integer'a çevrildiğinde ondalık sayıda hata veriyor

    if sayi == 99:
        b = 0
        print("Çıkış yaptım keke")
    elif sayi > 0:
        print("sayı pozitiftir")
    elif sayi == 0:
        print("sayı nötr")
    elif sayi < 0:
        print("sayı negatiftir")
    else:
        print("fuck off")