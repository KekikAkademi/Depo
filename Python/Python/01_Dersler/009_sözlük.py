hayvanlar = {
             "memeli" : "yunus",
             "sürüngen" : "kertenkele",
             "kuş" : "serçe",
             }

print(hayvanlar)
print(len(hayvanlar))

print(hayvanlar["kuş"])

hayvanlar["memeli"] = "kaplan"              # memeli'de değişiklik yapar
print(hayvanlar)

hayvanlar["balık"] = "sazan"                # dictionary e  ekleme
print(hayvanlar)

del(hayvanlar["sürüngen"])                  # silme fonksiyonu
print(hayvanlar)