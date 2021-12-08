with open("anasinin_nikahi.txt", "w", encoding="utf-8") as dosya:
    yazi = "fuuuuk"
    dosya.write(f"Yazı {yazi}")
#------------------------------------------#

esya = ["yatak", "masa", "dolap"]

with open("nesne.txt","w",encoding="utf-8") as metin:
    for i in esya:
        metin.write(f"{i}\n")

#------------------------------------------#

with open("nesne.txt") as karpuzus:
    a = karpuzus.read()

print(a)