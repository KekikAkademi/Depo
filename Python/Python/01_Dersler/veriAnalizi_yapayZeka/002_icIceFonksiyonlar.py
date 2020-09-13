def gunadin(isim):
    return isim

print(f'Günaydın : {gunadin("Ahmet")}')


def sabah(isim):
    def aksam(isim):
        return 'İyi Akşamlar ' + isim
    return 'Günaydınlar ' + aksam(isim)

print(f'Günaydın : {sabah("Ahmet")}')

def dükkan(kira):
    def daire(kira):
        print("dükkan kirası:",kira)
    print("ev kirası:",kira)
    daire(1500)
dükkan(2900)