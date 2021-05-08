from flask import Flask, jsonify, render_template, request
from textblob import TextBlob
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/yorum_ekle', methods=["POST"])
def yorum_ekle():
    # İstek verilerini ayıklayın
    request_data = request.get_json()
    id = request_data.get('id', '')
    kAdi = request_data.get('kAdi', '')
    yorum = request_data.get('yorum', '')
    
    # Bir yorumun duygusunu alın
    text = TextBlob(yorum)
    sentiment =  text.polarity
    
    comment_data = {
        "id": id,
        "kAdi": kAdi,
        "yorum": yorum,
        "sentiment": sentiment,
    }
    
    print(comment_data)
    return jsonify(comment_data)

# run Flask app
if __name__ == "__main__":
    app.run()