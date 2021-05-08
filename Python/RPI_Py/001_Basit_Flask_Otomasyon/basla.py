# Python ve Flask ile Raspberry Pi 3 GPIO Pinlerinin Durum ve Kontrolleri

import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_kirmizi = 13
led_sari    = 19
led_yesil   = 26

kirmizi_durum   = 0
sari_durum      = 0
yesil_durum     = 0

GPIO.setup(led_kirmizi, GPIO.OUT)
GPIO.setup(led_sari,    GPIO.OUT)
GPIO.setup(led_yesil,   GPIO.OUT)

GPIO.output(led_kirmizi, GPIO.LOW)
GPIO.output(led_sari,    GPIO.LOW)
GPIO.output(led_yesil,   GPIO.LOW)

@app.route('/')
def index():
    kirmizi_durum = GPIO.input(led_kirmizi)
    sari_durum    = GPIO.input(led_sari)
    yesil_durum   = GPIO.input(led_yesil)

    veri_sablonu = {
        'led_kirmizi' : kirmizi_durum,
        'led_sari'    : sari_durum,
        'led_yesil'   : yesil_durum
    }

    return render_template('index.html', **veri_sablonu)

@app.route('/<parca>/<olay>')
def yap(parca, olay):
    if parca == "led_yesil":
        islem = led_yesil
    elif parca == "led_kirmizi":
        islem = led_kirmizi
    elif parca == "led_sari":
        islem = led_sari

    if olay == "on":
        GPIO.output(islem, GPIO.HIGH)
    if olay == "off":
        GPIO.output(islem, GPIO.LOW)

    kirmizi_durum = GPIO.input(led_kirmizi)
    sari_durum    = GPIO.input(led_sari)
    yesil_durum   = GPIO.input(led_yesil)

    veri_sablonu = {
        'led_kirmizi' : kirmizi_durum,
        'led_sari'    : sari_durum,
        'led_yesil'   : yesil_durum
    }

    return render_template('index.html', **veri_sablonu )

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)