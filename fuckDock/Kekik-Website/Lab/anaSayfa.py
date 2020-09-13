from Lab import app
from flask import render_template

bakalim = "Flask Uygulamasını Docker ile Ayağa Kaldırma denemesi :)"

@app.route('/')
def anaSayfa():
    return render_template('index.html',
        baslik = "Merhaba Docker!",
        girdi = bakalim
    )