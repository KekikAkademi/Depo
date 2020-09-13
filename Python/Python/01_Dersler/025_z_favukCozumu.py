m1 = {"x" : [1, 3, 5], "y" : [2, 4, 6]}
m2 = {"x" : [2, 2, 2], "y" : [3, 3, 3]}

sonuc = {"x" : [], "y" : []}

for i in range(len(m1["x"])):
    a = m1["x"][i] + m2["x"][i]
    b = m1["y"][i] + m2["y"][i]

    sonuc["x"].append(a)
    sonuc["y"].append(b)

print(sonuc)