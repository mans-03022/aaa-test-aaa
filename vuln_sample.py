# サンプル: SQLインジェクション脆弱性を含むPythonコード
import sqlite3
from flask import Flask, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # 脆弱なSQLクエリ（SQLインジェクションの危険あり）
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    if result:
        return 'Login successful!'
    else:
        return 'Login failed!'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
