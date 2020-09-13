# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from kaziyici.scrape_korona import sozluk
import json

cikti = json.dumps(sozluk, indent=2, sort_keys=True, ensure_ascii=False)

print(cikti + "\n\n")

yazilan_veri = json.loads(cikti)

for bilgi in yazilan_veri['koronaVerileri']:
    print(f"""Dünya Geneli;
Vaka Sayısı     : {bilgi['vakaSayisi']['dunyaGeneli']}
Ölü Sayısı      : {bilgi['oluSayisi']['dunyaGeneli']}
İyileşen Sayısı : {bilgi['iyilesmeSayisi']['dunyaGeneli']}

Türkiye;
Vaka Sayısı     : {bilgi['vakaSayisi']['TR']}
Ölü Sayısı      : {bilgi['oluSayisi']['TR']}
İyileşen Sayısı : {bilgi['iyilesmeSayisi']['TR']}
""")