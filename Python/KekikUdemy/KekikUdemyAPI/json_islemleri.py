#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
#--------------------------------------------------------------------------------------#
# [J]ava
# [S]cript
# [O]bject
# [N]otation
# JavaScript Objesi Gösterimi; Küçük ve hafif bir veri biçimidir.
    # XML'den Daha hızlı, tarayıcılar tarafından daha hızlı ayrıştırılır.
    # JSON, sunucu ile istemci arasında veri transferi için ideal bir formattır.
        # Eğer veri transferi yapılacak yer bir tarayıcı değilse bile endişelenmeyin;
        # Çünkü neredeyse bütün sistemler JSON ile çalışabilir/ayrıştırabilir.
# JSON söz dizimi Python Dict.(Kütüphane) yapısı ile fazlaca benzerlik gösterir.
    # JSON ;
        # Keys: Strings, Numbers, Booleans, Lists, null, JSON Objects
#--------------------------------------------------------------------------------------#
def JsonAl():
    import http.client

    conn = http.client.HTTPConnection("127.0.0.1:5000") # HTTP veya HTTPS
    conn.request("GET", "/")

    res = conn.getresponse()
    data = res.read()
    #print(data.decode("utf-8"))

    json_yaz = open("Kekik.json", "w+")
    json_yaz.write(data.decode("utf-8"))
    json_yaz.close()

def JsonOku():
    import json

    veri = json.load(open("Kekik.json", "r+"))

    #veri = json.loads(data.decode('utf-8'), encoding='utf-8')

    print(veri['Zaman'])
    
    for bilgi in veri['Kurslar']:
        print(f"""
    Kurs Adı   : {bilgi['kurs_adi']}
    Kurs Linki : {bilgi['kurs_linki']}
                                """)

#JsonAl()
#JsonOku()