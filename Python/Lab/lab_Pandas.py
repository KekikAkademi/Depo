import pandas as pd

veri = {
  'isim': ['Ahmet', 'Melike', 'Hasan', 'Ayfer', 'Şahin', 'Hüseyin', 'Fatma'],
  'sehir': ['Sivas', 'Samsun', 'Hatay', 'Burdur','Urfa', 'Mardin', 'Düzce'],
  'yas': [41, 28, 33, 34, 38, 31, 37]
}

satirEtiketleri = [1, 2, 3, 4, 5, 6, 7]

df = pd.DataFrame(data=veri, index=satirEtiketleri)
print(df)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"head(2)\n\n{df.head(2)}")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"tail(2)\n\n{df.tail(2)}")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
sehirler = df['sehir']
print(f"sehirler\n\n{sehirler}")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"df.sehir\n\n{df.sehir}")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"sehirler[5]\n\n{sehirler[5]}")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"loc[5]\n\n{df.loc[5]}")