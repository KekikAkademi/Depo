def alanHesap(a,b):
    return a*b/2

alanHesap(5,7)          # değeri döndürdü fakat bu dönen değeri biz kullanmadık

print(alanHesap(5,7))   # dönen değeri ekrana yazdırdık


##

def merhabaReturn():
    isim = input("Adın Ne Emmoğlu? ")
    print(f" Adın {isim} imiş. Güzel isim.")
    return isim

print(f"Hoş geldin {merhabaReturn()}")