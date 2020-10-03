#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request, session
from flask_table import Table, Col
import sqlite3
import pandas as pd
import sys
import re
import os
import hashlib

#Flaskオブジェクトの生成
app = Flask(__name__)

app.secret_key = "aaa"

class Sales(object):
    def __init__(self, name, date, price):
        self.name = name
        self.date = date
        self.price = price

class SalesTable(Table):
    name = Col('商品名')
    date = Col('購入日')
    price = Col('金額')
    
class Users(object):
    def __init__(self, user_name, user_id, password):
        self.user_name = user_name
        self.user_id = user_id
        self.password = password

class UsersTable(Table):
    user_name = Col('ユーザー名')
    user_id = Col('ユーザーID')
    

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    return render_template('login.html')
    

# ログイン処理
@app.route("/login", methods=['GET', 'POST', 'PUT', 'DELETE'])
def login():
    # データベースに接続する
    conn = sqlite3.connect('Python_Flask/models/sales.db')
    c = conn.cursor()
    # パスワードをチェックして、買い物一覧画面に遷移する
    try:
        df = pd.read_sql_query(sql=u"SELECT password FROM users WHERE user_id ='{user_id}'" .format(
        user_id=request.form['user_id']), con=conn)
        if len(df) == 0:
            raise ValueError("存在しないログインIDです。")
        elif hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest() != df.iloc[0, 0]:
            raise ValueError("パスワードが間違っています。")
        # セッションにログインIDを保持する
        session["login_user"] = request.form['user_id']
        df = pd.read_sql_query(sql=u"SELECT * FROM sales WHERE user_id = '{user_id}'" .format(
                                                user_id=str(session["login_user"])), con=conn)
        conn.close()
        table = shopping_list(df)
        return render_template('shopping_list.html', login_user=session["login_user"], table=table)
    except ValueError as e:
        conn.close()
        return render_template('login.html', message=e)
        
        
# ユーザー登録処理
@app.route("/user_register", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_register():
    # データベースに接続する
    conn = sqlite3.connect('Python_Flask/models/sales.db')
    c = conn.cursor()
    try:
        # 全ての項目に入力がなかった場合、例外発生させる
        if request.form['user_name'] == '' or request.form['user_id'] == '' or request.form['password'] == '': 
            raise ValueError("全ての項目に入力してください。")
        # ユーザーIDとパスワードに使用可能文字が入力されているかチェック
        elif not is_allowed_chars(request.form['user_id']) or not is_allowed_chars(request.form['password']): 
            raise ValueError("ユーザーIDとパスワードは半角英数字を入力してください")    
        # ユーザーIDとパスワードに必要文字数が入力されているかチェック
        elif len(str(request.form['user_id'])) < 8 or len(str(request.form['password'])) < 8: 
            raise ValueError("ユーザーIDとパスワードは半角英数字8文字以上で入力してください。")
        # ユーザーIDとパスワードに半角数字が含まれているかチェック
        elif not _has_digit(str(request.form['user_id'])) or not _has_digit(str(request.form['password'])): 
            raise ValueError("ユーザーIDとパスワードは半角数字を入れてください。")
        # ユーザーIDとパスワードに半角英字が含まれているかチェック
        elif not _has_lower_letter(str(request.form['user_id'])) or not _has_lower_letter(str(request.form['password'])): 
            raise ValueError("ユーザーIDとパスワードは半角英字を入れてください。")
        # パスワードのハッシュ化
        hashed_pw = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
        # 入力した値を登録する
        c.execute("INSERT INTO users VALUES ('{user_name}', '{user_id}', '{password}')" .format(
                        user_name=request.form['user_name'], user_id=request.form['user_id'], password=hashed_pw))
        if not os.path.isdir('Python_Flask/app/static/csv/' + request.form['user_id']):
            # ユーザーごとのCSVフォルダを作成する
            os.mkdir('Python_Flask/app/static/csv/' + request.form['user_id'])
        # 登録した結果を保存（コミット）する
        conn.commit()
        conn.close()
        return render_template('login.html', message=str(request.form['user_name']) + "さんのユーザー登録が完了しました。")
    except ValueError as e:
        conn.close()
        return render_template('users_registration.html', message=e)
                
                
# ログアウトまたはユーザー解除処理
@app.route("/logout", methods=['GET', 'POST', 'PUT', 'DELETE'])
def logout():
    if 'logout' in request.form:
        # セッション値を削除してログイン画面に遷移する
        # セッションIDの削除
        session.pop('user_id', None)
        return render_template('login.html', message="ログアウトしました。")
    if 'cancel_user_registration' in request.form:
        logout_user = str(session["login_user"])
        # データベースに接続する
        conn = sqlite3.connect('Python_Flask/models/sales.db')
        c = conn.cursor()
         # 入力した値で更新する
        c.execute("DELETE FROM users WHERE user_id = '{user_id}'" .format(user_id=logout_user))
        # 結果を保存（コミット）する
        conn.commit()
        conn.close()
        # セッションIDの削除
        session.pop('user_id', None)
        return render_template('login.html', message="ID：" + logout_user + "さんの登録を解除しました。")
                

# CSV関連の処理           
@app.route("/csv", methods=['GET', 'POST', 'PUT', 'DELETE'])
def csv():
    # データベースに接続する
    conn = sqlite3.connect('Python_Flask/models/sales.db')
    c = conn.cursor()
    if request.method == 'POST':
         # CSVを取り込んだ結果を画面表示する
        if 'input' in request.form:
            c.execute("DELETE FROM sales WHERE user_id = '{user_id}'" .format(user_id=str(session["login_user"])))
            # CSVをpandasで取得する
            df = pd.read_csv('Python_Flask/app/static/csv/' + str(session["login_user"]) + '/' + str(session["login_user"]) + '.csv')
            # INSERT文作成と実行
            for i in range(len(df.index)):
                c.execute("INSERT INTO sales VALUES ('{user_id}', '{name}', '{date}', '{price}')" .format(
                            user_id=str(session["login_user"]), name=df.iloc[i, 0], date=df.iloc[i, 1], price=df.iloc[i, 2]))
            # 登録した結果を保存（コミット）する
            conn.commit()
            e = 'CSVの取り込みが完了しました。'
        # リストをCSVに出力する
        elif 'output' in request.form:
            df = pd.read_sql_query(sql=u"SELECT name, date, price FROM sales WHERE user_id = '{user_id}'" .format(
                                                user_id=str(session["login_user"])), con=conn)
            df.to_csv('Python_Flask/app/static/csv/' + str(session["login_user"]) + '/' + str(session["login_user"]) + '.csv', index=False)
            e = 'CSVの保存が完了しました。'
    df = pd.read_sql_query(sql=u"SELECT * FROM sales WHERE user_id = '{user_id}'" .format(
                                                user_id=str(session["login_user"])), con=conn)
    conn.close()
    table = shopping_list(df)
    return render_template('shopping_list.html', login_user=session["login_user"], message=e, table=table)
  
            
# データの登録、更新、削除           
@app.route("/register_shopping_list", methods=['GET', 'POST', 'PUT', 'DELETE'])
def register_shopping_list():
    # データベースに接続する
    conn = sqlite3.connect('Python_Flask/models/sales.db')
    c = conn.cursor()
    if request.method == 'POST':
        # 画面から入力した値を登録する
        if 'register' in request.form:
            try:
                # 全ての項目に入力がなかった場合、例外発生させる
                if request.form['name'] == '' or request.form['date'] == '' or request.form['price'] == '': 
                    raise ValueError("全ての項目に入力してください。")
                # 入力した値を登録する
                c.execute("INSERT INTO sales VALUES ('{user_id}', '{name}', '{date}', '{price}')" .format(
                user_id=str(session["login_user"]), name=request.form['name'], date=request.form['date'], price=request.form['price']))
                # 結果を保存（コミット）する
                conn.commit()
                e = '商品名：「' + request.form['name'] + '」の登録が完了しました。'
            except ValueError as e:
                df = pd.read_sql_query(sql=u"SELECT * FROM sales WHERE user_id = '{user_id}'" .format(
                                                user_id=str(session["login_user"])), con=conn)
                conn.close()
                table = shopping_list(df)
                return render_template('shopping_list.html', login_user=session["login_user"], message=e, table=table)
        # 画面から入力した値を更新する
        elif 'update' in request.form:
            try:
                # 全ての項目に入力がなかった場合、例外発生させる
                if request.form['name'] == '' or request.form['date'] == '' or request.form['price'] == '': 
                    raise ValueError("全ての項目に入力してください。")
                # 入力した値で更新する
                c.execute("UPDATE sales SET price = '{price}' WHERE user_id = '{user_id}' AND name = '{name}' AND date = '{date}'" .format(
                user_id=str(session["login_user"]), name=request.form['name'], date=request.form['date'], price=request.form['price']))
                # 結果を保存（コミット）する
                conn.commit()
                e = '商品名：「' + request.form['name'] + '」の更新が完了しました。'
            except ValueError as e:
                df = pd.read_sql_query(sql=u"SELECT * FROM sales WHERE user_id = '{user_id}'" .format(
                                                user_id=str(session["login_user"])), con=conn)
                conn.close()
                table = shopping_list(df)
                return render_template('shopping_list.html', login_user=session["login_user"], message=e, table=table)
        # 画面から入力した値を削除する
        elif 'delete' in request.form:
            try:
                # 削除する商品名と購入日に入力がなかった場合、例外発生させる
                if request.form['name'] == '' or request.form['date'] == '': 
                    raise ValueError("削除する商品名と購入日を入力してください。")
                # 入力した値を削除する
                c.execute("DELETE FROM sales WHERE user_id = '{user_id}' AND name = '{name}' AND date = '{date}'" .format(
                            user_id=str(session["login_user"]), name=request.form['name'], date=request.form['date']))
                # 結果を保存（コミット）する
                conn.commit()
                e = '商品名:「' + request.form['name'] + '」の削除が完了しました。'
            except ValueError as e:
                df = pd.read_sql_query(sql=u"SELECT * FROM sales WHERE user_id = '{user_id}'" .format(
                                                user_id=str(session["login_user"])), con=conn)
                conn.close()
                table = shopping_list(df)
                return render_template('shopping_list.html', login_user=session["login_user"], message=e, table=table)
    df = pd.read_sql_query(sql=u"SELECT * FROM sales WHERE user_id = '{user_id}'" .format(
                                                user_id=str(session["login_user"])), con=conn)
    conn.close()
    table = shopping_list(df)
    return render_template('shopping_list.html', login_user=session["login_user"], message=e, table=table)
            
   
# 画面遷移処理           
@app.route("/transit", methods=['GET', 'POST', 'PUT', 'DELETE'])
def transit():
    if 'login' in request.form:
        # ログイン画面に遷移する
        return render_template('login.html')      
    elif 'users_register' in request.form:
        # ユーザー登録画面に遷移する
        return render_template('users_registration.html')      
    elif 'users_list' in request.form:
        # データベースに接続する
        conn = sqlite3.connect('Python_Flask/models/sales.db')
        df = pd.read_sql_query(sql=u"SELECT * FROM users", con=conn)
        conn.close()
        table = users_list(df)
        # ユーザ一覧画面に遷移する
        return render_template('users_list.html', login_user=session["login_user"], table=table)
    elif 'shopping_list' in request.form:
        # データベースに接続する
        conn = sqlite3.connect('Python_Flask/models/sales.db')
        df = pd.read_sql_query(sql=u"SELECT * FROM sales WHERE user_id = '{user_id}'" .format(
                                                user_id=str(session["login_user"])), con=conn)
        conn.close()
        table = shopping_list(df)
        # 買い物一覧画面に遷移する
        return render_template('shopping_list.html', login_user=session["login_user"], table=table)


def shopping_list(df):        
    items = []
    for i in range(len(df.index)):
        items.append(Sales(df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3]))
    return SalesTable(items)
    
    
def users_list(df):        
    items = []
    for i in range(len(df.index)):
        items.append(Users(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2]))
    return UsersTable(items)
    
    
def is_allowed_chars(password):
    # 全ての文字が「 （スペース）」〜「~」までの範囲内かをチェック
    m = re.search(r'^[\x20-\x7E]+$', password)
    return True if m else False
    
    
def _has_digit(password):
    # 半角数字が含まれるかをチェック
    m = re.search(r'[0-9]', password)
    return True if m else False


def _has_lower_letter(password):
    # 半角英字が含まれるかをチェック
    m = re.search(r'[a-z|A-Z]', password)
    return True if m else False
    