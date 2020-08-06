import sqlite3

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

import utils.App

"""
render_template: templateフォルダ内のhtmlファイルを返す
"""

# グローバルにこのファイル名を設定
app = Flask(__name__, static_folder='graph')


@app.route('/', methods=['GET', 'POST'])
def get_ticker():
    if request.method == 'GET':
        return render_template('hello.html')
    else:
        # サーバーからの入力を受けるとき
        print(str(request.values))
        # return str(request.values['ticker_symbol'])
        ticker_symbol = str(request.values['ticker_symbol'])
        trading = utils.App.Prediction(ticker_symbol)
        trading.prediction()

        template_data = {
            'title': ticker_symbol,
            'filename': 'graph.jpeg'
        }
        return render_template('graph.html', **template_data)


def main():
    app.run(debug=True)
    # trading = App.Prediction('MSFT')
    # trading.prediction()

if __name__ == '__main__':
    main()


"""
def get_db():
    # グローバルなデータベース
    db = getattr(g,'_database', None)
    # データベースがないなら作る
    if db is None:
        db = g._database = sqlite3.connect('test_sqlite.db')
    return db


# アプリケーションが閉じるときに実行するプロパティ
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'database', None)
    # データベースが動いている場合クローズする
    if db is not None:
        db.close()


@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.excute(
        'CREATE TABLE IF NOT EXISTS persons('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )

    name = request.values.get('name', name)
    if request.method == 'GET':
        curs.excute('SELECT * FROM persons WHERE name = ')
        
        
@app.route('/')
def hello_world():
    return 'TOP Page'


@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world2(username=None):
    # return 'Hello World! {}'.format(username)
    return render_template('hello.html', username=username)


@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    return str(request.values['username'])


def main():
    # app.debug = True
    # app.run()
    # まとめて書ける
    app.run(debug=True)

    # app.run(host='127.0.0.1', port=5000)

"""
if __name__ == '__main__':
    main()