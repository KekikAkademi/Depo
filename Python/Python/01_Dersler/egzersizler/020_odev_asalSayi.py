"""

Listedeki elemanların çift olup olmadığını söyle

"""

sayiListesi = [12, 11, 9, 17]

for i in sayiListesi:
    if i % 2 == 0:
        print(f"{i} çift sayıdır")
    else:
        print(f"{i} tek sayıdır")