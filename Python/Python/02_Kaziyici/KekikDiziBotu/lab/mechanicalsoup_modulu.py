#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import mechanicalsoup

link = "https://www.dizibox.pw/sitemap-tax-diziler.xml"

tarayici = mechanicalsoup.StatefulBrowser(      # Tarayıcı Tanımlıyoruz
    soup_config={'features': 'html5lib'},       # html5lib ile ayrıştır
    raise_on_404=True,                          # ?
    # Kimlik Bilgimizi Tanımlıyoruz
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)',
)
tarayici.open(link)

nerdeyim = tarayici.get_url()
#print(nerdeyim)             # https://www.dizibox.pw/sitemap-tax-diziler.xml
sayfa = tarayici.get(link)
#print(sayfa)                # <Response [200]>
icerik = sayfa.content
#print(icerik)               # b'<?xml version="1.0"
kodlar = icerik.decode()
#print(kodlar)               # kodlar geldi :)


#for linkler in kodlar.find('loc'):
#    print(linkler)