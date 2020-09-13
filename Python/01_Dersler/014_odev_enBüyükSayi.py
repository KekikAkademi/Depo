sayi1 = int(input("1. sayıyı giriniz "))
sayi2 = int(input("2. sayıyı giriniz "))
sayi3 = int(input("3. sayıyı giriniz "))


if (sayi1 >= sayi2) and (sayi1 >= sayi3):
    enBuyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3
print(f"En büyük girdi : {enBuyuk}")

# --
sayilar = [sayi1, sayi2, sayi3]
sayilar.sort()
sayilar.reverse()

print(f"Girmiş Olduğunuz En yüksek rakam {sayilar[0]}")
#print("Girmiş Olduğunuz En yüksek rakam " + sayilar[0])