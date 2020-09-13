from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def anaSayfa():
    return render_template('anaSayfa.html', sayiTest=10, yaziTest='Mahmut')

if __name__ == '__main__':
    app.run(debug = True)