## https://youtu.be/dmgeY79DvV8
## https://github.com/WhiteRedTHT/Karalamalarim/blob/master/D%C3%B6viz%20Hesaplama/Doviz_cevirme.py
import json
import requests

print("-"*30)
print("Döviz Dönüştürücü API'sine Hoş Geldiniz!")
print("-"*30)

print("-"*30)
print("Programdan çıkmak için ilk iki sorunun birisinde 'q' yazmanız yeterlidir.")
print("-"*30)

print("-"*30)
print("Para Birimleri: CAD, HKD, ISK, PHP, DKK, HUF, CZK, GBP, RON, SEK, IDR"
      "INR, BRL, RUB, HRK, JPY, THB, CHF, EUR, MYR, BGN, TRY,"
      "CNY, NOK, NZD, ZAR, USD, MXN, SGD, AUD, ILS, KRW, PLN")

while True:
    api_url = "https://api.exchangeratesapi.io/latest?base="
    doviz_boz = input("Bozmak istediğiniz döviz türü: \n")
    doviz_alinan = input("Almak istediğiniz döviz türü: \n")
    miktar = int(input("Ne kadar {} bozdurmak istiyorsunuz: \n".format(doviz_boz)))

    if doviz_boz == "q" or doviz_alinan == "q":
        print("Programdan çıkılıyor...")
        input()
        break
    else:
        sonuc = requests.get(api_url+doviz_boz) # api_url'nin sonunda = işareti var buraya doviz_boz değerini yazarak ona göre işlem yapmamızı sağlar.
        sonuc = json.loads(sonuc.text) # Siteye gidrek json verilerini text verisine döndürür.
        print("1 {} = {} {}\n".format(doviz_boz, sonuc["rates"][doviz_alinan], doviz_alinan)) # 1 olarak burada 1 Bozdurmak istediğiniz döviz türü almak istediğiniz dövüz türüne eşit anlamında yazamaktadır.
        print("{} {} = {} {}\n".format(miktar, doviz_boz, miktar * sonuc["rates"][doviz_alinan], doviz_alinan)) #Genel hesaplama yaparak bizlere dövizin dönüşmüş halini yazar.