from flask import Flask

app = Flask(__name__)

@app.route('/')
def anaSayfa():
    return "Ana Sayfa"

@app.route('/ara')
def aramaSayfasi():
    return "Arama Sayfası"

@app.route('/sil/bisey')
def silBisey():
    return "Sil Bişey"

@app.route('/sil/<int:id>')
def silID(id):
    return f"Bunu Mu Sileceksin Delikanlı? {id}"

if __name__ == '__main__':
    app.run(debug = True)