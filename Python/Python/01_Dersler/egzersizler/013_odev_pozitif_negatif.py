"""

Kullanıcıdan Sayı Girmesini İste ve Pozitif mi Yoksa Negatif Mi olduğunu Söyle

"""
while True:
    sayi = int(input("Sayı Giriniz "))

    if sayi > 0:
        print("Sayı Pozitif")
    elif sayi == 0:
        print("Sayı nört")
    else:
        print("Sayı Negatif")