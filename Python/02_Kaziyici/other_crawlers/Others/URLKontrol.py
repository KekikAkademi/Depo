import requests

"""
print('[ UYARI ]Lütfen Bir WorldList Dosyası Yazınız Örnek : worldlist.txt')
filename = input('[Dosya Seç] Dosyanın İsmi : ')
"""

siteler = ['https://www.google.com','https://www.google.com/admin','https://www.google.com/ornek-admin']

for x in siteler:
    r = requests.get(x)
    if r.status_code == 200: #200 döndürüyorsa böyle bir url var demektir.
        print('Url Bulundu : {}'.format(x))
    elif r.status_code == 404: #404 döndürüyorsa böyle bir url yok demektir.
        print('Url Hatalı')