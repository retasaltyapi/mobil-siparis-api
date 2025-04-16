from flask import Flask
import os  # os modülünü eklemeyi unutmayın

app = Flask(__name__)

@app.route('/')
def home():
    return "API Çalışıyor!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render için port ayarı
    app.run(host='0.0.0.0', port=port)