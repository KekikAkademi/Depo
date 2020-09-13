"""
- İki parametre alan bir Python işlevi yazın.
- Eğer iki parametre de tamsayı ise;
    - işlev bu iki tamsayının toplamını döndürür.
- Bunlardan yalnızca biri tamsayı ise;
    - işlev bu tamsayıyı döndürür.
- hiçbiri tamsayı değilse;
    - işlev dize olarak "Error" değerini döndürür.
"""

def toplama(sayi1, sayi2):
    try:
        if type(sayi1) or type(sayi2) != int:
            try: print(int(sayi1))
            except: print(int(sayi2))

        else: print(sayi1 + sayi2)

    except Exception as hata: print(f"Hata! : {hata}")



toplama(1, 5)
toplama(15, "a")
toplama("a", 27)
toplama("aaaa", "bbb")