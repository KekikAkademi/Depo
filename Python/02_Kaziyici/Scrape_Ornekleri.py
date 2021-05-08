#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu kopya kağıdı @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

def Bs4_Req():
    import requests
    from bs4 import BeautifulSoup

    link = "https://www.icisleri.gov.tr/65-yas-ve-ustu-ile-kronik-rahatsizligi-olanlara-sokaga-cikma-yasagi-ek-genelgesi"
    kimlik = {'User-Agent' : '@KekikAkademi'}       # Kimlik Bilgimizi Tanımlıyoruz
    istek = requests.get(link, headers=kimlik)      # Link'e kimlik bilgimizle istek gönderiyor ve gelen veriyi tutuyoruz
    soup = BeautifulSoup(istek.text, "html5lib")    # Gelen veriyi html5lib ile ayrıştırmaya başlıyoruz

    print(soup.title.text)

    tr2eng = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
    print(f"{soup.title.text.translate(tr2eng)}.pdf")
#Bs4_Req()
#----------------------------------------------------------------------------------------------------------------------#
def HTTPx():
    import httpx

    link = "https://www.icisleri.gov.tr/65-yas-ve-ustu-ile-kronik-rahatsizligi-olanlara-sokaga-cikma-yasagi-ek-genelgesi"
    kimlik = {'User-Agent' : '@KekikAkademi'}   # Kimlik Bilgimizi Tanımlıyoruz
    istek = httpx.get(link, headers=kimlik)     # Link'e kimlik bilgimizle istek gönderiyor ve gelen veriyi tutuyoruz

    print(istek.text)
#HTTPx()
#----------------------------------------------------------------------------------------------------------------------#
def Mechanize():
    import mechanize

    link = "https://www.icisleri.gov.tr/65-yas-ve-ustu-ile-kronik-rahatsizligi-olanlara-sokaga-cikma-yasagi-ek-genelgesi"
    tarayici = mechanize.Browser()                          # Tarayıcı Tanımlıyoruz
    tarayici.addheaders = [('User-agent', '@KekikAkademi')] # Kimlik Bilgimizi Tanımlıyoruz
    tarayici.set_handle_robots(False)                       # Robots.txt Engeline Takılma!
    tarayici.open(link)                                     # Link'i Tarayıcıda Aç

    for sayfa_linkleri in tarayici.links():
        gelen = f"[*] Başlık: {sayfa_linkleri.text} -- Bağlantı: {sayfa_linkleri.url}"
        print(gelen)
        
        #dosya = open("dosya.txt", "a+")
        #dosya.write(f"{gelen}\n")
        #dosya.close()

    tarayici.close()
#Mechanize()
#----------------------------------------------------------------------------------------------------------------------#
def MechanicalSoup_re():
    import re
    import mechanicalsoup

    # Google Tarama Örneği
    link = "https://www.google.com/"
    tarayici = mechanicalsoup.StatefulBrowser(              # Tarayıcı Tanımlıyoruz
        soup_config={'features': 'html5lib'},               # html5lib ile ayrıştır
        raise_on_404=True,                                  # ?
        user_agent='@KekikAkademi : t.me/KekikAkademi',     # Kimlik Bilgimizi Tanımlıyoruz
    )
    tarayici.open(link)

    # Form'u Dolduralım
    tarayici.select_form('form[action="/search"]')
    #degisken = input("Aranacak Kelimeyi Girin : ")
    tarayici["q"] = "@KekikAkademi"
    
    
    # Not: "btnK" adlı içerik gerçek insanlar için
    # "btnG" ise botlar için
    tarayici.submit_selected(btnName="btnG")

    # Link'leri Göster
    for link in tarayici.links():
        hedef = link.attrs['href']
        
        
        # Alakasız Bağlantıları Çıkartıp Gerçek Bağlantıya Ulaşalım
        # Tıklama Takibi
        if (hedef.startswith('/url?') and not
        hedef.startswith("/url?q=http://webcache.googleusercontent.com")):
            hedef = re.sub(r"^/url\?q=([^&]*)&.*", r"\1", hedef)
            print(hedef)

    tarayici.close()
#MechanicalSoup_re()
#----------------------------------------------------------------------------------------------------------------------#
def Lassie():
    import lassie

    k = lassie.fetch("https://www.sitebuilderreport.com/stock-up",all_images=True,handle_file_content=True)

    print(k)
#Lassie()
#----------------------------------------------------------------------------------------------------------------------#