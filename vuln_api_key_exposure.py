# APIキーの露出脆弱性サンプル
from flask import Flask

app = Flask(__name__)

API_KEY = 'sk_test_51H8QwLw9EXAMPLESECRETKEY1234567890'

@app.route('/')
def index():
    return f"API Key: {API_KEY}"

if __name__ == '__main__':
    app.run(debug=True)
