import os, json

def dict2json(sozluk:dict, dosya_adi:str):
    liste = []
    if not os.path.isfile(dosya_adi):
        liste.append(sozluk)

        with open(dosya_adi, mode='w') as f:
            f.write(json.dumps(liste, indent=2, ensure_ascii=False, sort_keys=False))
    else:
        with open(dosya_adi) as gelen_json:
            gelen_veri = json.load(gelen_json)

        gelen_veri.append(sozluk)

        with open(dosya_adi, mode='w') as f:
            f.write(json.dumps(gelen_veri, indent=2, ensure_ascii=False, sort_keys=False))

for _ in range(50):
    dict2json(
        {
            "Merhaba" : "Dunya",
            "Selam"   : "Json"
        },
        dosya_adi='kurek.json')
