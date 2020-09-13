apartman = "               Cafer Salman | papatya | sümbül            ".strip()     # baş ve sondaki boşlukları aldırma

print(apartman.upper())                             # bütün harfleri büyüt

print(apartman.lower())                             # bütün harfleri küçült

print(apartman.replace("a","f"))                    # a'ları f' ile değiştir

print(apartman.replace("a", "f", 2))                # ilk 2 a'yı f' ile değiştri

print(len(apartman))                                # uzunluk
print(apartman.split())                             # listeye çevir
print(len(apartman.split()))                        # liste uzunluğu

a = apartman.replace(" ","")                        # "boşluk" ları "hiçbişey" e çevir
b = a.split("|")                                    # | (pipe) işareti ile ayrıştırarak listeye çevir

print("apartman adı : " + b[1])                     # b'nin birinci elemanı