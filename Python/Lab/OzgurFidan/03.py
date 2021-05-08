"""
- Kullanıcıdan tamsayı değeri alan ve döndüren bir Python işlevi yazın.
- Kullanıcı bir tamsayı girmezse,
    - kullanıcı geçerli bir değer girene kadar işlemi uyarır ve tekrarlar.
"""

def gelenSayi():
    while True:
        try: veri = int(input("Lütfen TamSayı Giriniz : "))
        except: continue

        print(veri)
        break

gelenSayi()