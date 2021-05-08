dosya = open("anasinin_nikahi.txt", "w", encoding="utf-8")
yazi = "fuuuuk"
dosya.write(f"Yazı {yazi}")
dosya.close()

#------------------------------------------#

esya = ["yatak", "masa", "dolap"]

metin = open("nesne.txt","w",encoding="utf-8")

for i in esya:
    metin.write(f"{i}\n")

metin.close()

#------------------------------------------#

with open("nesne.txt") as karpuzus:
    a = karpuzus.read()

print(a)