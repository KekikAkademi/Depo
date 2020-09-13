kokular = ["defne", "yasemin", "kekik"]

for esans in kokular:
    print(esans)

for esans in kokular:
    print(f"{esans} kısaltması = {esans[0:3]}")

for esans in kokular:
    if esans != "kekik":
        print(f"{esans} kısaltması = {esans[0:3]}")
    #print("***********************")

print()
print()

tr_harfler = "şçöğüİı"

for harf in tr_harfler:
    print(harf)