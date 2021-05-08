# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app, log_ver
from flask import render_template, request

@app.route('/')
def ana_sayfa():
    log_ver(request)

    return render_template(
        'ana_sayfa.html',
        baslik = "Merhaba Flask!",
        icerik = "Ben Python Dosyasından Değişken Olarak Geldim.."
    )