kuslar = ["martı", "kırlangıç", "leylek", "serçe", "güvercin", "leylek"]
print(kuslar)

print("Şunu Sildim > " + kuslar[4].upper())
kuslar.remove("güvercin")                           # sil
print(kuslar)

kuslar.append("karga")                              # sonuna ekle
print("Şunu Ekledim > " + kuslar[5].upper())
print(kuslar)

#kuslar.clear()                                      # listeyi temizler
#print(kuslar)                                       # []

print(kuslar.count("leylek"))                        # kaç tane var
print("Leylek Sayısı > " + str(kuslar.count("leylek")))

print(kuslar.index("serçe"))                        # kaçıncı index
print("Serçe İndex'i > " + str(kuslar.index("serçe")))

kuslar.pop(3)                                       # 3. index'i sil
print(kuslar)

kuslar.insert(1, "ağaçkakan")                       # 1. index' e ekle
print(kuslar)

kuslar.reverse()                                    # listeyi ters çevirir
print(kuslar)

print("KOPYALAMA ÖĞRENİYORUM")
ters_kuslar = kuslar.copy()                         # listeyi kopyalar
kuslar.reverse()
print(kuslar)
print(ters_kuslar)

print("BÜTÜN KUŞLAR")
kuslar.extend(ters_kuslar)                          # liste içine liste elemanlarını ekleme
print(kuslar)
print(ters_kuslar)

kuslar.sort()                                       # a-z / 0-9 sıralı hale çevir
print(kuslar)

