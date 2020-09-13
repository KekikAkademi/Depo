#!flask/bin/python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------------------------------#
from flask import Flask                 #
from flask import jsonify,make_response #
from orumcek import TR, EN              #
from time import strftime               #
#---------------------------------------#

#-----------------------#
app = Flask(__name__)   #
#-----------------------#

# https://stackabuse.com/deploying-a-flask-application-to-heroku/

@app.route('/TR/', methods=['GET'])
def Turkce_1():
    return jsonify(Kurslar=TR(1), Zaman=strftime('%d/%m %H:%M:%S'))

@app.route('/TR/<int:hangi_sayfa>', methods=['GET'])
def Turkce_Hangi(hangi_sayfa):
    return jsonify(Kurslar=TR(hangi_sayfa), Zaman=strftime('%d/%m %H:%M:%S'))

@app.route('/EN/', methods=['GET'])
def Eng_1():
    return jsonify(Kurslar=EN(1), Zaman=strftime('%d/%m %H:%M:%S'))

@app.route('/EN/<int:hangi_sayfa>', methods=['GET'])
def Eng_Hangi(hangi_sayfa):
    return jsonify(Kurslar=EN(hangi_sayfa), Zaman=strftime('%d/%m %H:%M:%S'))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'HTTP 404 Error': 'Aradığınız içerik mevcut değil. Lütfen isteğinizi kontrol edin.'}), 404)

#---------------------------------------------------#
if __name__ == '__main__':                          #
    app.config['JSON_AS_ASCII'] = False             #
    app.run(debug=True, host='0.0.0.0', port=5000)  #
#---------------------------------------------------#