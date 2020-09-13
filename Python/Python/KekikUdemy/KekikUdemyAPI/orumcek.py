#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#-----------------------------------------------------------------------------------#
import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş   #
from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş          #
import html5lib                 # HTML dosyalarını işleyen arkadaş                  #
import re                       # Ayrıştırıcı Arkadaş                               #
#-----------------------------------------------------------------------------------#

def TR(hangi_sayfa):
    #-------------------------------------------------------------------------------------------#
    udemy_baslik = []                                                   # Boş liste Oluşturduk  #
    udemy_link = []                                                     # Boş liste Oluşturduk  #
    #-------------------------------------------------------------------------------------------#

    #----------------------------------------------------------------------------------------------------------------------------------#
    sayfa = str(hangi_sayfa)                                        # int olan değerimizi str yapıyoruz
    link = 'https://www.discudemy.com/language/Turkish/' + sayfa    # sayfalar arasında gezinmek için
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)'}                        # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
    istek = requests.get(link)                                      # link'e istek göderiyoruz ve gelen veriyi kaydediyoruz
    kaynak = BeautifulSoup(istek.text, 'html5lib')                  # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık
    #----------------------------------------------------------------------------------------------------------------------------------#

    #---------------------------------------------------------------------------------------------------------------------#
    for baslik in kaynak.findAll('a',{'class': 'card-header'}):     # kaynak'tan | <a class'ı = card-header olanları tut
        baslik = baslik.text                                        # Yazı Formatına Çevir

        udemy_baslik.append(baslik)                                 # listeye Yerleştir
    #---------------------------------------------------------------------------------------------------------------------#

    #-----------------------------------------------------------------------------------------------------------------------#
    for discudemy_linkler in kaynak.findAll('a', attrs={                            # kaynak'tan | <a olanları _ ve
        'href': re.compile("^https://www.discudemy.com/Turkish/")}):                # href="../Turkish/' olan linkleri tut
        gelen_discudemy = discudemy_linkler['href']                                 # dönen verideki linkleri tut
        discudemy_go_html = requests.get(gelen_discudemy)                           # onlara istek gönder
        discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'html5lib')     # kaynağını al
        #-------------------------------------------------------------------------------------------------------------------#
        for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={        # aldığın kaynaktan | <a olanları _ ve
            'href': re.compile("^https://www.discudemy.com/go/")}):                 # href="../go/kurs-adi" olan linkleri tut
            gelen_discudemy_go = discudemy_go_linkler['href']                       # dönen verideki linkleri tut
            udemy_html = requests.get(gelen_discudemy_go)                           # onlara istek gönder
            udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')               # kaynağını al
            #---------------------------------------------------------------------------------------------------------------#
            for udemy_linkler in udemy_kaynak.findAll('a', attrs={                  # aldığın kaynaktan | <a olanları _ ve
                'href': re.compile("^https://www.udemy.com/")}):                    # href="../www.udemy.com/" olan linkleri tut
                gelen_udemy = udemy_linkler['href']                                 # dönen verideki linkleri tut

                udemy_link.append(gelen_udemy)                                      # listeye Yerleştir
        #-----------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------#
    liste = []                                      # liste oluştur
    for adet in range(0, len(udemy_baslik)):        # 0'dan Başlayarak, Dönen "başlık" sayısı kadar "adet" oluştur
        sozluk = {}                                 # sözlük oluştur
        sozluk['kurs_adi'] = udemy_baslik[adet]     # kurs adını sözlüğe ekle
        sozluk['kurs_linki'] = udemy_link[adet]     # kurs linkini sözlüğe ekle
        liste.append(sozluk)                        # sözlüğü listeye ekle
    return liste                                    # Listeyi Döndür

def EN(hangi_sayfa):
    #-------------------------------------------------------------------------------------------#
    udemy_baslik = []                                                   # Boş liste Oluşturduk  #
    udemy_link = []                                                     # Boş liste Oluşturduk  #
    #-------------------------------------------------------------------------------------------#

    #----------------------------------------------------------------------------------------------------------------------------------#
    sayfa = str(hangi_sayfa)                                        # int olan değerimizi str yapıyoruz
    link = 'https://www.discudemy.com/language/English/' + sayfa    # sayfalar arasında gezinmek için
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)'}                        # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
    istek = requests.get(link)                                      # link'e istek göderiyoruz ve gelen veriyi kaydediyoruz
    kaynak = BeautifulSoup(istek.text, 'html5lib')                  # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık
    #----------------------------------------------------------------------------------------------------------------------------------#

    #---------------------------------------------------------------------------------------------------------------------#
    for baslik in kaynak.findAll('a',{'class': 'card-header'}):     # kaynak'tan | <a class'ı = card-header olanları tut
        baslik = baslik.text                                        # Yazı Formatına Çevir

        udemy_baslik.append(baslik)                                 # listeye Yerleştir
    #---------------------------------------------------------------------------------------------------------------------#

    #-----------------------------------------------------------------------------------------------------------------------#
    for discudemy_linkler in kaynak.findAll('a', attrs={                            # kaynak'tan | <a olanları _ ve
        'href': re.compile("^https://www.discudemy.com/English/")}):                # href="../English/' olan linkleri tut
        gelen_discudemy = discudemy_linkler['href']                                 # dönen verideki linkleri tut
        discudemy_go_html = requests.get(gelen_discudemy)                           # onlara istek gönder
        discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'html5lib')     # kaynağını al
        #-------------------------------------------------------------------------------------------------------------------#
        for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={        # aldığın kaynaktan | <a olanları _ ve
            'href': re.compile("^https://www.discudemy.com/go/")}):                 # href="../go/kurs-adi" olan linkleri tut
            gelen_discudemy_go = discudemy_go_linkler['href']                       # dönen verideki linkleri tut
            udemy_html = requests.get(gelen_discudemy_go)                           # onlara istek gönder
            udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')               # kaynağını al
            #---------------------------------------------------------------------------------------------------------------#
            for udemy_linkler in udemy_kaynak.findAll('a', attrs={                  # aldığın kaynaktan | <a olanları _ ve
                'href': re.compile("^https://www.udemy.com/")}):                    # href="../www.udemy.com/" olan linkleri tut
                gelen_udemy = udemy_linkler['href']                                 # dönen verideki linkleri tut

                udemy_link.append(gelen_udemy)                                      # listeye Yerleştir
        #-----------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------#
    liste = []                                      # liste oluştur
    for adet in range(0, len(udemy_baslik)):        # 0'dan Başlayarak, Dönen "başlık" sayısı kadar "adet" oluştur
        sozluk = {}                                 # sözlük oluştur
        sozluk['kurs_adi'] = udemy_baslik[adet]     # kurs adını sözlüğe ekle
        sozluk['kurs_linki'] = udemy_link[adet]     # kurs linkini sözlüğe ekle
        liste.append(sozluk)                        # sözlüğü listeye ekle
    return liste                                    # Listeyi Döndür