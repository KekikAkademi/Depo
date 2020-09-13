# https://ron.sh/creating-real-time-charts-with-flask/

from flask import Flask, Response, render_template, send_from_directory
from flask_sitemap import Sitemap
import os, json
from time import sleep
from datetime import datetime

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
ext = Sitemap(app=app)

@app.route('/')
def anaSayfa():
    return render_template('index.html', baslik="İşte Bunu Seviyorum")

@app.route('/grafik-verileri')
def grafik_verileri():
    def veriUretim():
        while True:
            toplam, kullanilan, bosta = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

            json_data = json.dumps(
                {
                    'Zaman': datetime.now().strftime('%H:%M:%S'),
                    'toplam': toplam,
                    'kullanilan': kullanilan,
                    'bosta': bosta
                },
                sort_keys=False, ensure_ascii=False)
            
            yield f"data: {json_data}\n\n"
            sleep(1)

    return Response(veriUretim(), mimetype='text/event-stream')

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), filename='img/favicon.ico', mimetype='image/x-icon')

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_AS_ASCII'] = False
    app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
    app.run(debug = True, threaded=True, host = '0.0.0.0', port = port)
    #from waitress import serve
    #serve(app, host = "0.0.0.0", port = port)
