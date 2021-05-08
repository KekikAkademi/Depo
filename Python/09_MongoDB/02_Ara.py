import pymongo

my_client = pymongo.MongoClient("mongodb+srv://keyif:SIFRE@cluster0.k8zos.mongodb.net/")

my_db = my_client['denemedb']

#### Collection'a Bağlan;
my_collection = my_db['kisiler']

def db_ara(sorgu:dict):
    say = my_collection.count_documents(sorgu)
    if say == 1:
        ara = my_collection.find_one(sorgu, {'_id': 0})
        print(f"{say} Adet Kaydın İlki;\n{ara}")
    elif say > 1:
        ara = my_collection.find(sorgu, {'_id': 0})
        print(f"{say} Adet Kaydın İlki;\n{ara[0]}")

    return ara

### https://docs.mongodb.com/manual/reference/operator/query/

# bak = db_ara({'ad': {'$regex': '[A-Z]'}})
bak = db_ara({'dogum': {'$gt': 1900}})

for i in bak:
    print(i)