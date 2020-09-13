sayi = int(float(input("sayı giriniz > ")))     # input direkt integer'a çevrildiğinde ondalık sayıda hata veriyor

if sayi > 0:
    print("sayı pozitiftir")
elif sayi == 0:
    print("sayı nötr")
elif sayi < 0:
    print("sayı negatiftir")
else:
    print("fuck off")