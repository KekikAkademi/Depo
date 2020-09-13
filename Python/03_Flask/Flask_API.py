#!flask/bin/python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
    # Kaynak : https://www.buraksenyurt.com/post/python-ile-rest-tabanli-servis-gelistirmek

from flask import Flask, jsonify, make_response, send_from_directory, request 

app = Flask(__name__)

kullanicilar = [
    {'id': 1000,'kullanici_adi': 'keyiflerolsun','mahalle': 'KekikAkademi','rutbe': 'root'},
    {'id': 1001,'kullanici_adi': 'raifpy','mahalle': 'KekikSiber','rutbe': 'python'},
    {'id': 1002,'kullanici_adi': 'ykslkrkci','mahalle': 'KekikSiber','rutbe': 'hain'},
    {'id': 1003,'kullanici_adi': 'Kullanici_bot','mahalle': 'KekikSiber','rutbe': 'BOT'},
]

@app.route('/kekik/api/kullanicilar', methods=['GET'])
def get():
    return jsonify({'Kullanıcılar': kullanicilar})

@app.route('/kekik/api/kullanicilar', methods=['POST'])
def post():
    yeniKullanici = {
        'id': kullanicilar[-1]['id'] + 1,
        'kullanici_adi': request.json['kullanici_adi'],
        'mahalle': request.json['mahalle'],
        'rutbe': request.json['rutbe'],
    }
    kullanicilar.append(yeniKullanici)
    return jsonify({'kullanici': yeniKullanici}), 201

@app.route('/kekik/api/kullanicilar/<int:kullanici_id>', methods=['GET'])
def get_kullanici(kullanici_id):
    kullanici = [kullanici for kullanici in kullanicilar if kullanici['id'] == kullanici_id]
    if len(kullanici) == 0:
        return jsonify({'Kullanıcı': 'Bulunamadı'}), 404
    return jsonify({'Kullanıcı': kullanici})

@app.route('/kekik/api/kullanicilar/<int:kullanici_id>', methods=['DELETE'])
def delete_kullanici(kullanici_id):
    kullanici = [kullanici for kullanici in kullanicilar if kullanici['id'] == kullanici_id]
    if len(kullanici) == 0:
        return jsonify({'Kullanıcı': 'Bulunamadı'}), 404
    kullanicilar.remove(kullanici[0])
    return jsonify({'Kullanıcı Silindi': kullanici})

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(directory=app.root_path, filename='favicon.ico', mimetype='image/x-icon')

@app.errorhandler(404)
def dortYuzDort(error):
    return make_response(
        jsonify({'HTTP 404 Error': 'Aradığınız içerik mevcut değil. Lütfen isteğinizi kontrol edin.'}), 404
    )

@app.errorhandler(500)
def besYuz(error):
    return make_response(
        jsonify({'HTTP 500 Error': 'Bağlantı Hatası!'}), 500
    )

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, host='0.0.0.0', port=5000)