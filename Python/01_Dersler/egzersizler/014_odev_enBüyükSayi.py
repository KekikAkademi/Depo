"""

kullanıcıdan 3 farklı sayı al ve bu sayılardan en büyüğünü söyle

"""
while True:
    sayi1 = int(input("Sayı giriniz "))
    sayi2 = int(input("Sayı giriniz "))
    sayi3 = int(input("Sayı giriniz "))

    if sayi1 > sayi2 and sayi1 > sayi3:
        print(f"\t{sayi1} En büyük sayıdır")
    elif sayi2 > sayi1 and sayi2 > sayi3:
        print(f"\t{sayi2} En büyük sayıdır")
    else:
        print(f"\t{sayi3} En büyük sayıdır")