import pymongo

my_client = pymongo.MongoClient("mongodb+srv://keyif:SIFRE@cluster0.k8zos.mongodb.net/")

my_db = my_client['denemedb']

print(my_db.list_collection_names())


#### Collection'a Bağlan;
my_collection = my_db['kisiler']

# kisi = {
#     "ad"    : "Ahmet",
#     "soyad" : "Demir",
#     "dogum" : 1880
# }

#### Veri Gir;
# sonuc = my_collection.insert_one(kisi)
# print(sonuc.inserted_id)

kisi_listesi = [
    {"ad" : "Hüseyin", "soyad": "Kirazlı", "dogum" : 1920},
    {"ad" : "Ali", "soyad": "Bekir", "dogum" : 1620},
    {"ad" : "Deli", "soyad": "Dumrul", "dogum" : 2007},
    {"ad" : "Hasan", "soyad": "Hüseyin", "dogum" : 1452}
]

sonuc = my_collection.insert_many(kisi_listesi)

#### Verileri Gir;
print(sonuc.inserted_ids)