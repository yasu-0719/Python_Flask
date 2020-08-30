#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request
from flask_table import Table, Col
import sqlite3
import pandas as pd

#Flaskオブジェクトの生成
app = Flask(__name__)

class Item(object):
    def __init__(self, name, cost, price):
        self.name = name
        self.cost = cost
        self.price = price

class ItemTable(Table):
    name = Col('商品名')
    cost = Col('原価')
    price = Col('売価')


@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Submit') == 'Submit':
            
            # CSVをpandasで取得する
            df = pd.read_csv('Python_Flask/app/static/csv/sales_sample.csv')

            # データベースに接続する
            conn = sqlite3.connect('Python_Flask/models/sales.db')
            c = conn.cursor()

            # テーブルの作成
            c.execute('''DROP TABLE IF EXISTS sales''')
            c.execute('''CREATE TABLE sales(name text, cost real, sales real)''')

            # INSERT文作成と実行
            for i in range(len(df.index)):
                c.execute("INSERT INTO sales VALUES ('{name}', '{cost}', '{price}')" .format(
                    name=df.iloc[i, 0], cost=df.iloc[i, 1], price=df.iloc[i, 2]))

            # 挿入した結果を保存（コミット）する
            conn.commit()

            # データベースへのアクセスが終わったらcloseする
            conn.close()

        else:
            return render_template("index.html")
    name = request.args.get("うどん")
    # データベースに接続する
    conn = sqlite3.connect('sales.db')

    df = pd.read_sql_query(sql=u"SELECT * FROM sales", con=conn)

    items = []
    for i in range(len(df.index)):
        items.append(Item(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2]))

    # データベースへのアクセスが終わったらcloseする
    conn.close()

    table = ItemTable(items)

    # or {{ table }} in jinja
    print(table.__html__())
    return render_template('index.html', title='商品一覧', table=table)
    # return render_template("index.html", title="うどん", name=name)
    




