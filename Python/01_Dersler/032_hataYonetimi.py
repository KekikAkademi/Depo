import sys

liste = [5, "karpuzus", 24, 0, "ömer favuk"]

for eleman in liste:
    try:
        print(f"Sayımız : {eleman}")
        sonuc = 1 / eleman
        print(f"\tSonuç : {sonuc}\n")
    except Exception as hataAdi:
        print(f"\t\tHata Türü : {sys.exc_info()[0]}")
        print(f"\t\tHata Adı : {hataAdi}\n")