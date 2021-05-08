#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from base64 import b64encode, b64decode

def sifrele(metin):
    return b64encode(metin.encode())

def coz(metin):
    return b64decode(metin).decode()

print(sifrele("Merhaba Dünya.."))
print()
print(coz(b'TWVyaGFiYSBEw7xueWEuLg=='))
print()

####
komut = '''
for i in range(10):
    print("Ebesinin Amı!")
'''

sifrelenmis_komut = sifrele(komut)
print(sifrelenmis_komut)
# b'CmZvciBpIGluIHJhbmdlKDEwKToKICAgIHByaW50KCdFYmVzaW5pbiBBbcSxIScpCg=='

eval(compile(coz(b'CmZvciBpIGluIHJhbmdlKDEwKToKICAgIHByaW50KCdFYmVzaW5pbiBBbcSxIScpCg=='), '<string>', 'exec'))