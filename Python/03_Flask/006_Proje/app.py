from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veritabani.db'
db = SQLAlchemy(app)

class Yap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    baslik = db.Column(db.String(80))
    icekil = db.Column(db.Text)
    tamam = db.Column(db.Boolean)

@app.route('/')
def anaSayfa():
    yapilacaklar = Yap.query.all()
    return render_template('anaSayfa.html', liste=yapilacaklar)

@app.route('/ekle', methods = ['POST'])
def ekle():
    baslik = request.form.get('baslik')
    icerik = request.form.get('icerik')
    
    yeniBisi = Yap(baslik = baslik, icekil = icerik, tamam = False)
    db.session.add(yeniBisi)
    db.session.commit()
    
    return redirect(url_for('anaSayfa'))

@app.route('/tamamla/<int:id>', methods = ['GET'])
def tamamla(id):
    sor = Yap.query.filter_by(id=id).first()
    
    if sor.tamam == False:
        sor.tamam = True
    else:
        sor.tamam = False
    
    db.session.commit()
    
    return redirect(url_for('anaSayfa'))

@app.route('/sil/<int:id>', methods = ['GET'])
def sil(id):
    bakalim = Yap.query.filter_by(id=id).first()
    db.session.delete(bakalim)
    db.session.commit()

    return redirect(url_for('anaSayfa'))

@app.route('/detay/<int:id>', methods = ['GET'])
def detay(id):
    detayVer = Yap.query.filter_by(id=id).first()


    return render_template('detay.html', yap=detayVer)

if __name__ == "__main__":
    app.run(debug = True)