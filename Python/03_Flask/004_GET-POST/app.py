from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def anaSayfa():
    return render_template('anaSayfa.html')

@app.route('/toplam', methods = ['GET', 'POST'])
def toplam():
    if request.method == 'POST':
        sayi1 = int(request.form.get('sayi1'))
        sayi2 = int(request.form.get('sayi2'))
        return render_template('sayilar.html', toplam = sayi1 + sayi2)
    else:
        return render_template('sayilar.html')


if __name__ == "__main__":
    app.run(debug = True)