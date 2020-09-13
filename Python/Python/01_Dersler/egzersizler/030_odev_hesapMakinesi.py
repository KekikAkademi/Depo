print("""Hesap Makinemize Hoşgeldiniz

Toplamak    için    > 1 <   e    Basınız
Çıkarmak    için    > 2 <   ye   Basınız
Çarpmak     için    > 3 <   e    Basınız
Bölmek      için    > 4 <   e    Basınız  """)

secenek = input("\n\n\tLütfen Seçim Yapınız ")

sayi1 = int(input("Sayı Giriniz "))
sayi2 = int(input("Sayı Giriniz "))

if secenek == "1":
    print(f"    İşleminizin sonucu  {sayi1+sayi2}")
elif secenek == "2":
    print(f"    İşleminizin sonucu  {sayi1 - sayi2}")

elif secenek == "3":
    print(f"    İşleminizin sonucu  {sayi1*sayi2}")

elif secenek == "4":
    print(f"    İşleminizin sonucu  {sayi1/sayi2}")
else:
    print("işlem yap piç")



