istenen  = int(input("Sayı gir lütfen "))

def faktoriyelHesapla():
    if istenen < 0:
        print("Negatif Sayıların Faktöryeli Olmaz!")
    elif istenen == 0:
        print("Hesaplandı : 1")
    else:
        faktoriyel = 1

        for i in range(1, istenen+1):
            faktoriyel *= i

        return faktoriyel


verilecek = faktoriyelHesapla()
if verilecek:
    print(f"Hesaplandı : {verilecek}")