'https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-datase'

import pandas as pd

pandaVeri = pd.read_csv("novel-corona-virus-2019-dataset/covid_19_data.csv").rename(columns={
    "ObservationDate": "Gözlem Tarihi",
    "Province/State": "İl / Eyalet",
    "Country/Region": "Ülke / Bölge",
    "Last Update": "Son Güncelleme",
    "Confirmed": "Vaka",
    "Deaths": "Ölü",
    "Recovered": "Taburcu"
    })

print(pandaVeri)                # DataSetin Tamamı
print(pandaVeri.shape)          # Satır ve Sütun Bilgisi
print(pandaVeri.columns)        # Sütun Değerleri
print(pandaVeri.dtypes)         # Sütunların Veri Türleri
print(pandaVeri.head())         # İlk 5 Satır
print(pandaVeri.tail())         # Son 5 Satır
print(pandaVeri.info())         # Genel Bilgi
print(pandaVeri.isnull().sum()) # Eksik Bilgilerin(null) Toplamı
print(pandaVeri.describe())     # Sütun İstatistikleri
print(pandaVeri["Ülke / Bölge"].describe())       # Spesifik Sütun İstatistiği
print(pandaVeri["İl / Eyalet"].describe())
print("\n\n")
print(pandaVeri.describe(include=["O"]))        # Sayısal Olmayan Sütun Analizleri
print("\n\n")
print(pandaVeri["Ülke / Bölge"].value_counts())   # Boş Değere Sahip olmayan kaç veri var
print("\n\n")
print(pandaVeri[pandaVeri['Ülke / Bölge'] == 'Turkey']) # Şartı Sağlayan Değeri Almak
print("\n\n")
print("\n\n")
print(pandaVeri[pandaVeri['Ülke / Bölge'] == 'Turkey'].describe())

from os import system
system('clear')

print(pandaVeri[["Ülke / Bölge", "Vaka", "Ölü", "Taburcu"]])    # İstediğimiz Kolonları Almak
print(pandaVeri.loc[1])                                             # 1. Satırı Al
print(pandaVeri.loc[1:5])                                           # ilk 5 Satırı Al
print("\n\n")
print(pandaVeri.loc[27:30, ["Ülke / Bölge", "Vaka", "Ölü", "Taburcu"]])
print(pandaVeri.iloc[5])
print("\n\n\n")
print(pandaVeri[pandaVeri['Ölü']>50])    # 50 Den fazla ölü olduğu Durumlar

system('clear')

print(pandaVeri[["Ülke / Bölge", "Vaka", "Ölü", "Taburcu"]].sort_values(by="Ölü", ascending=False).head(20))    # En yüksek ölüm azalan sıralama
pandaVeri.drop(26127, inplace=True)                                 # Satır Sil
print(pandaVeri.sort_values(by="Ölü", ascending=False).head(20))    # En yüksek ölüm azalan sıralama
pandaVeri = pandaVeri.drop("SNo", axis=1)                           # Sütun Sil
pandaVeri = pandaVeri.drop(columns="Son Güncelleme")                # Sütun Sil
print(pandaVeri.sort_values(by="Ölü", ascending=False).head(20))    # En yüksek ölüm azalan sıralama
print("\n\n\n")
print(pandaVeri.groupby("Ülke / Bölge")["Ölü"].mean().head(20))     # Ortalama Ölüm Oranları
print(pandaVeri.groupby("Ülke / Bölge")["Ölü"].max().head(20))      # En Yüksek Ölüm Oranları
print("\n\n\n")
print(pandaVeri.groupby(["Ülke / Bölge", "İl / Eyalet"])["Ölü"].max().head(10))      # En Yüksek Ölüm Oranları
print("\n\n\n")
print(pandaVeri.groupby(["İl / Eyalet", "Ülke / Bölge"])["Ölü"].max().head(10))      # En Yüksek Ölüm Oranları

system('clear')

'''
drpona > None | olan satır ve sütünları siler (1 none varsa bütün satırı siler)
'''

print(pandaVeri.isnull().sum())     # İl / Eyalet      13649

pandaVeri['İl / Eyalet'].fillna(method="ffill", inplace=True)   # ffill > none değerden önceki değer boş satıra yazılır

print(pandaVeri.isnull().sum())