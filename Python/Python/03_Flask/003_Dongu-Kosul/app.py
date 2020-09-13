from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def anaSayfa():
    sayilar = [2, 4, 6, 8]
    
    return render_template('anaSayfa.html', a=5, b=10, tabloSayi=sayilar)


if __name__ == '__main__':
    app.run(debug = True)