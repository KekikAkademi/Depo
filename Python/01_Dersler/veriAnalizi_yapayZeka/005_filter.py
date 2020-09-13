"fonksiyon içerisindeki True değerleri döndür"

filterTest = filter(lambda sayi: sayi%2 == 0, [1,2,3,4,5,6,7,8,9])
print(filterTest) # <filter object at 0x0103E4D8> >>>> Ram'deki yeri
print(list(filterTest))


filterTest2 = filter(lambda sayi: sayi%2 == 0, range(50))
print(list(filterTest2))





def asalSayi(sayi):
    sayac = 2
    if sayi == 2 : return True
    elif sayi < 2 : return False
    else:
        while(sayac < sayi):
            if sayi%sayac == 0 : return False
            sayac += 1
            return True

print(asalSayi(5))
print(asalSayi(6))

asalFilter = filter(asalSayi, range(50))
print(list(asalFilter))