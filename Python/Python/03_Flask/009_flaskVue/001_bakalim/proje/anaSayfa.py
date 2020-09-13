from proje import app
from flask import render_template

@app.route('/')
def anaSayfa():
    return render_template('vueTest.html', baslik="İşte Bunu Seviyorum")