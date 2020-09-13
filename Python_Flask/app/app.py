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
    # データベースに接続する
    conn = sqlite3.connect('Python_Flask/models/sales.db')
    c = conn.cursor()
    if request.method == 'POST':
        
        # 画面をCSVを取り込んだ初期状態に戻す
        if 'input' in request.form:
             # テーブルの作成
            c.execute('''DROP TABLE IF EXISTS sales''')
            c.execute('''CREATE TABLE sales(name text, cost real, price real)''')
            # CSVをpandasで取得する
            df = pd.read_csv('Python_Flask/app/static/csv/sales_sample.csv')
            # INSERT文作成と実行
            for i in range(len(df.index)):
                c.execute("INSERT INTO sales VALUES ('{name}', '{cost}', '{price}')" .format(
                    name=df.iloc[i, 0], cost=df.iloc[i, 1], price=df.iloc[i, 2]))
            # 登録した結果を保存（コミット）する
            conn.commit()
            
        
        # リストをCSVに出力する
        elif 'output' in request.form:
            df = pd.read_sql_query(sql=u"SELECT * FROM sales", con=conn)
            df.to_csv('Python_Flask/app/static/csv/sales_sample.csv', index=False)    
            
        # 画面から入力した値を登録する
        elif 'register' in request.form:
            try:
                # 全ての項目に入力がなかった場合、例外発生させる
                if request.form['name'] == '' or request.form['cost'] == '' or request.form['price'] == '': 
                    raise ValueError("全ての項目に入力してください。")
                # 入力した値を登録する
                c.execute("INSERT INTO sales VALUES ('{name}', '{cost}', '{price}')" .format(
                name=request.form['name'], cost=request.form['cost'], price=request.form['price']))
                # 結果を保存（コミット）する
                conn.commit()
                
            except ValueError as e:
                df = pd.read_sql_query(sql=u"SELECT * FROM sales", con=conn)
                conn.close()
                table = list_results(df)
                return render_template('index.html', error_message=e, table=table)
                
                   
        # 画面から入力した値を更新する
        elif 'update' in request.form:
            try:
                # 全ての項目に入力がなかった場合、例外発生させる
                if request.form['name'] == '' or request.form['cost'] == '' or request.form['price'] == '': 
                    raise ValueError("全ての項目に入力してください。")
                # 入力した値を削除する
                c.execute("UPDATE sales SET cost = '{cost}',price = '{price}' where name = '{name}'" .format(
                        name=request.form['name'], cost=request.form['cost'], price=request.form['price']))
                # 結果を保存（コミット）する
                conn.commit()
                
            except ValueError as e:
                df = pd.read_sql_query(sql=u"SELECT * FROM sales", con=conn)
                conn.close()
                table = list_results(df)
                return render_template('index.html', error_message=e, table=table)
                
                
        # 画面から入力した値を削除する
        elif 'delete' in request.form:
            try:
                # 削除する商品名に入力がなかった場合、例外発生させる
                if request.form['name'] == '': 
                    raise ValueError("削除する商品名を入力してください。")
                # 入力した値を削除する
                c.execute("DELETE FROM sales WHERE name = '{name}'" .format(name=request.form['name']))
                # 結果を保存（コミット）する
                conn.commit()
                
            except ValueError as e:
                df = pd.read_sql_query(sql=u"SELECT * FROM sales", con=conn)
                conn.close()
                table = list_results(df)
                return render_template('index.html', error_message=e, table=table)

    elif request.method == 'GET':
        print(request.method)
        
    df = pd.read_sql_query(sql=u"SELECT * FROM sales", con=conn)
    # データベースへのアクセスが終わったらcloseする
    conn.close()
    table = list_results(df)
    return render_template('index.html', table=table)


def list_results(df):        
    items = []
    for i in range(len(df.index)):
        items.append(Item(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2]))
    return ItemTable(items)

    
    




