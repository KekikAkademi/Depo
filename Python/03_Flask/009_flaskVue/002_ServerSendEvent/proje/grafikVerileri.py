from proje import app
from flask import Response
import os, json
from time import sleep
from datetime import datetime

@app.route('/grafikVerileri')
def grafikVerileri():
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