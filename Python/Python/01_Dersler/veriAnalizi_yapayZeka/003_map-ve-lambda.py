"""
map > tuple, dict, list gibi array(dizi)'lerde işlem yaparız.

map(fonksiyon, iterasyon)
"""
liste = [4,3,2]
def carp(sayi):
    return sayi*2

print(f'Fonksiyona argüman olarak listeyi veriyorum > {carp(liste)}')

map1 = map(carp,liste)
print(f'map1 > {map1} | Veri Tipi {type(map1)}')
print(f'map1 i listeye çevirelim > {list(map1)} | Veri Tipi {type(list(map1))}')


def topla(sayi):
    return sayi+5
tekSatir = list(map(topla, [5, 10, 15, 20]))
print(f"Tek Satır Kod : {tekSatir}")

# Lambda Fonksiyonu ile de map kullanabiliriz !
acaba = list(map(lambda sayi1, sayi2 : sayi1*sayi2, [3, 5, 7], [2, 5, 9]))
print(f"Acaba > {acaba}")