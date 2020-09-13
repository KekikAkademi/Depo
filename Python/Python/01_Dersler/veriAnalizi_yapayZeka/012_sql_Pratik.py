import sqlite3

# veritabanı Oluştur
con = sqlite3.connect("okul.db")

# veritabanına imleç ekle
imlec = con.cursor()

# tablo oluştur
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenci (ad TEXT, soyAd TEXT, sinif INT)")

# tabloya eleman ekle
imlec.execute("INSERT INTO ogrenci VALUES('Adil', 'Kiraz', 5)")

# eklenilen değeri işle
con.commit()

# tabloya eleman ekle
imlec.execute("INSERT INTO ogrenci VALUES('Furkan', 'Kızıl', 6)")

# eklenilen değeri işle
con.commit()




# tablodan verileri okumak
imlec.execute("SELECT * FROM ogrenci")
con.commit()

# liste halinde verileri okumak
imlec.execute("SELECT * FROM ogrenci")
veri = imlec.fetchall()
print(veri)
print()s