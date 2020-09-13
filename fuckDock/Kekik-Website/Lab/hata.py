from Lab import app
from flask import make_response, jsonify, send_from_directory
import os


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), filename='img/favicon.ico', mimetype='image/x-icon')

@app.errorhandler(404)
def dortYuzDort(error):
    return make_response(jsonify(KolektifAPI='Sayfa Bulunamadı'), 404)

@app.errorhandler(500)
def besYuz(error):
    return make_response(jsonify(KolektifAPI='Düzgün Argüman Verilmedi'), 500)