# コマンドインジェクション脆弱性を含むPythonサンプル
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host', '')
    result = os.popen(f'ping -c 1 {host}').read()
    return f'<pre>{result}</pre>'

if __name__ == '__main__':
    app.run(debug=True)
