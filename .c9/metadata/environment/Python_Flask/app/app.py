{"filter":false,"title":"app.py","tooltip":"/Python_Flask/app/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":168,"column":40},"end":{"row":169,"column":0},"action":"insert","lines":["",""],"id":950},{"start":{"row":169,"column":0},"end":{"row":169,"column":4},"action":"insert","lines":["    "]},{"start":{"row":169,"column":4},"end":{"row":170,"column":0},"action":"insert","lines":["",""]},{"start":{"row":170,"column":0},"end":{"row":170,"column":4},"action":"insert","lines":["    "]},{"start":{"row":170,"column":4},"end":{"row":171,"column":0},"action":"insert","lines":["",""]},{"start":{"row":171,"column":0},"end":{"row":171,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":171,"column":0},"end":{"row":171,"column":4},"action":"remove","lines":["    "],"id":951},{"start":{"row":170,"column":4},"end":{"row":171,"column":0},"action":"remove","lines":["",""]},{"start":{"row":170,"column":0},"end":{"row":170,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":169,"column":4},"end":{"row":170,"column":0},"action":"remove","lines":["",""],"id":952}],[{"start":{"row":169,"column":4},"end":{"row":170,"column":0},"action":"insert","lines":["",""],"id":953},{"start":{"row":170,"column":0},"end":{"row":170,"column":4},"action":"insert","lines":["    "]},{"start":{"row":170,"column":4},"end":{"row":171,"column":0},"action":"insert","lines":["",""]},{"start":{"row":171,"column":0},"end":{"row":171,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":171,"column":0},"end":{"row":171,"column":4},"action":"remove","lines":["    "],"id":954}],[{"start":{"row":171,"column":0},"end":{"row":172,"column":12},"action":"insert","lines":["@app.route(\"/\", methods=['GET', 'POST', 'PUT', 'DELETE'])","def index():"],"id":955}],[{"start":{"row":171,"column":13},"end":{"row":171,"column":14},"action":"insert","lines":["l"],"id":956},{"start":{"row":171,"column":14},"end":{"row":171,"column":15},"action":"insert","lines":["o"]},{"start":{"row":171,"column":15},"end":{"row":171,"column":16},"action":"insert","lines":["g"]},{"start":{"row":171,"column":16},"end":{"row":171,"column":17},"action":"insert","lines":["i"]},{"start":{"row":171,"column":17},"end":{"row":171,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":172,"column":4},"end":{"row":172,"column":9},"action":"remove","lines":["index"],"id":957},{"start":{"row":172,"column":4},"end":{"row":172,"column":5},"action":"insert","lines":["l"]},{"start":{"row":172,"column":5},"end":{"row":172,"column":6},"action":"insert","lines":["o"]}],[{"start":{"row":172,"column":6},"end":{"row":172,"column":7},"action":"insert","lines":["g"],"id":958},{"start":{"row":172,"column":7},"end":{"row":172,"column":8},"action":"insert","lines":["i"]}],[{"start":{"row":172,"column":8},"end":{"row":172,"column":9},"action":"insert","lines":["n"],"id":959}],[{"start":{"row":172,"column":12},"end":{"row":173,"column":0},"action":"insert","lines":["",""],"id":960},{"start":{"row":173,"column":0},"end":{"row":173,"column":4},"action":"insert","lines":["    "]},{"start":{"row":173,"column":4},"end":{"row":174,"column":0},"action":"insert","lines":["",""]},{"start":{"row":174,"column":0},"end":{"row":174,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":174,"column":4},"end":{"row":191,"column":63},"action":"insert","lines":["# パスワードを確認して、買い物一覧画面に遷移する","        elif 'login' in request.form:","            try:","                df = pd.read_sql_query(sql=u\"SELECT password FROM users WHERE user_id ='{user_id}'\" .format(","                                            user_id=request.form['user_id']), con=conn)","                if len(df) == 0:","                    raise ValueError(\"存在しないログインIDです。\")","                elif request.form['password'] != df.iloc[0, 0]:","                    raise ValueError(\"パスワードが間違っています。\")","                session[\"login_user\"] = request.form['user_id']","                df = pd.read_sql_query(sql=u\"SELECT * FROM sales\", con=conn)","                conn.close()","                table = list_results(df)","                return render_template('index.html', login_user=session[\"login_user\"], table=table)","            ","            except ValueError as e:","                conn.close()","                return render_template('login.html', message=e)"],"id":961}],[{"start":{"row":175,"column":9},"end":{"row":175,"column":10},"action":"remove","lines":["l"],"id":962},{"start":{"row":175,"column":8},"end":{"row":175,"column":9},"action":"remove","lines":["e"]}],[{"start":{"row":71,"column":2},"end":{"row":88,"column":63},"action":"remove","lines":["      # パスワードを確認して、買い物一覧画面に遷移する","        elif 'login' in request.form:","            try:","                df = pd.read_sql_query(sql=u\"SELECT password FROM users WHERE user_id ='{user_id}'\" .format(","                                            user_id=request.form['user_id']), con=conn)","                if len(df) == 0:","                    raise ValueError(\"存在しないログインIDです。\")","                elif request.form['password'] != df.iloc[0, 0]:","                    raise ValueError(\"パスワードが間違っています。\")","                session[\"login_user\"] = request.form['user_id']","                df = pd.read_sql_query(sql=u\"SELECT * FROM sales\", con=conn)","                conn.close()","                table = list_results(df)","                return render_template('index.html', login_user=session[\"login_user\"], table=table)","            ","            except ValueError as e:","                conn.close()","                return render_template('login.html', message=e)"],"id":963},{"start":{"row":71,"column":1},"end":{"row":71,"column":2},"action":"remove","lines":[" "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":1},"action":"remove","lines":[" "]},{"start":{"row":70,"column":12},"end":{"row":71,"column":0},"action":"remove","lines":["",""]},{"start":{"row":70,"column":8},"end":{"row":70,"column":12},"action":"remove","lines":["    "]},{"start":{"row":70,"column":4},"end":{"row":70,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"remove","lines":["    "],"id":964},{"start":{"row":69,"column":100},"end":{"row":70,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":153,"column":12},"end":{"row":154,"column":0},"action":"insert","lines":["",""],"id":965},{"start":{"row":154,"column":0},"end":{"row":154,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":154,"column":4},"end":{"row":158,"column":32},"action":"insert","lines":["print(request.method)","    # データベースに接続する","    conn = sqlite3.connect('Python_Flask/models/sales.db')","    c = conn.cursor()","    if request.method == 'POST':"],"id":966}],[{"start":{"row":158,"column":32},"end":{"row":159,"column":4},"action":"remove","lines":["","    "],"id":967}],[{"start":{"row":158,"column":32},"end":{"row":159,"column":0},"action":"insert","lines":["",""],"id":968},{"start":{"row":159,"column":0},"end":{"row":159,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":159,"column":0},"end":{"row":160,"column":0},"action":"remove","lines":["        ",""],"id":969}],[{"start":{"row":159,"column":0},"end":{"row":160,"column":0},"action":"insert","lines":["",""],"id":970}],[{"start":{"row":177,"column":63},"end":{"row":178,"column":0},"action":"insert","lines":["",""],"id":971},{"start":{"row":178,"column":0},"end":{"row":178,"column":16},"action":"insert","lines":["                "]},{"start":{"row":178,"column":16},"end":{"row":179,"column":0},"action":"insert","lines":["",""]},{"start":{"row":179,"column":0},"end":{"row":179,"column":16},"action":"insert","lines":["                "]},{"start":{"row":179,"column":16},"end":{"row":180,"column":0},"action":"insert","lines":["",""]},{"start":{"row":180,"column":0},"end":{"row":180,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":180,"column":12},"end":{"row":180,"column":16},"action":"remove","lines":["    "],"id":972},{"start":{"row":180,"column":8},"end":{"row":180,"column":12},"action":"remove","lines":["    "]},{"start":{"row":180,"column":4},"end":{"row":180,"column":8},"action":"remove","lines":["    "]},{"start":{"row":180,"column":0},"end":{"row":180,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":180,"column":0},"end":{"row":186,"column":32},"action":"insert","lines":["@app.route(\"/login\", methods=['GET', 'POST', 'PUT', 'DELETE'])","def login():","    print(request.method)","    # データベースに接続する","    conn = sqlite3.connect('Python_Flask/models/sales.db')","    c = conn.cursor()","    if request.method == 'POST':"],"id":973}],[{"start":{"row":180,"column":17},"end":{"row":180,"column":18},"action":"remove","lines":["n"],"id":974},{"start":{"row":180,"column":16},"end":{"row":180,"column":17},"action":"remove","lines":["i"]},{"start":{"row":180,"column":15},"end":{"row":180,"column":16},"action":"remove","lines":["g"]},{"start":{"row":180,"column":14},"end":{"row":180,"column":15},"action":"remove","lines":["o"]},{"start":{"row":180,"column":13},"end":{"row":180,"column":14},"action":"remove","lines":["l"]}],[{"start":{"row":180,"column":13},"end":{"row":180,"column":14},"action":"insert","lines":["c"],"id":975},{"start":{"row":180,"column":14},"end":{"row":180,"column":15},"action":"insert","lines":["s"]},{"start":{"row":180,"column":15},"end":{"row":180,"column":16},"action":"insert","lines":["v"]}],[{"start":{"row":180,"column":15},"end":{"row":180,"column":16},"action":"remove","lines":["v"],"id":976},{"start":{"row":180,"column":14},"end":{"row":180,"column":15},"action":"remove","lines":["s"]},{"start":{"row":180,"column":13},"end":{"row":180,"column":14},"action":"remove","lines":["c"]}],[{"start":{"row":180,"column":13},"end":{"row":180,"column":14},"action":"insert","lines":["c"],"id":977},{"start":{"row":180,"column":14},"end":{"row":180,"column":15},"action":"insert","lines":["s"]},{"start":{"row":180,"column":15},"end":{"row":180,"column":16},"action":"insert","lines":["v"]}],[{"start":{"row":43,"column":7},"end":{"row":61,"column":75},"action":"remove","lines":[" # CSVを取り込んだ結果を画面表示する","        if 'input' in request.form:","             # テーブルの作成","            c.execute('''DROP TABLE IF EXISTS sales''')","            c.execute('''CREATE TABLE sales(name text, cost real, price real)''')","            # CSVをpandasで取得する","            df = pd.read_csv('Python_Flask/app/static/csv/list.csv')","            # INSERT文作成と実行","            for i in range(len(df.index)):","                c.execute(\"INSERT INTO sales VALUES ('{name}', '{cost}', '{price}')\" .format(","                    name=df.iloc[i, 0], cost=df.iloc[i, 1], price=df.iloc[i, 2]))","            # 登録した結果を保存（コミット）する","            conn.commit()","            ","        ","        # リストをCSVに出力する","        elif 'output' in request.form:","            df = pd.read_sql_query(sql=u\"SELECT * FROM sales\", con=conn)","            df.to_csv('Python_Flask/app/static/csv/list.csv', index=False) "],"id":978}],[{"start":{"row":43,"column":6},"end":{"row":43,"column":7},"action":"remove","lines":[" "],"id":979},{"start":{"row":43,"column":5},"end":{"row":43,"column":6},"action":"remove","lines":[" "]},{"start":{"row":43,"column":4},"end":{"row":43,"column":5},"action":"remove","lines":[" "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]},{"start":{"row":42,"column":8},"end":{"row":43,"column":0},"action":"remove","lines":["",""]},{"start":{"row":42,"column":4},"end":{"row":42,"column":8},"action":"remove","lines":["    "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "]},{"start":{"row":41,"column":32},"end":{"row":42,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":166,"column":32},"end":{"row":167,"column":0},"action":"insert","lines":["",""],"id":980},{"start":{"row":167,"column":0},"end":{"row":167,"column":8},"action":"insert","lines":["        "]},{"start":{"row":167,"column":8},"end":{"row":168,"column":0},"action":"insert","lines":["",""]},{"start":{"row":168,"column":0},"end":{"row":168,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":168,"column":8},"end":{"row":186,"column":75},"action":"insert","lines":[" # CSVを取り込んだ結果を画面表示する","        if 'input' in request.form:","             # テーブルの作成","            c.execute('''DROP TABLE IF EXISTS sales''')","            c.execute('''CREATE TABLE sales(name text, cost real, price real)''')","            # CSVをpandasで取得する","            df = pd.read_csv('Python_Flask/app/static/csv/list.csv')","            # INSERT文作成と実行","            for i in range(len(df.index)):","                c.execute(\"INSERT INTO sales VALUES ('{name}', '{cost}', '{price}')\" .format(","                    name=df.iloc[i, 0], cost=df.iloc[i, 1], price=df.iloc[i, 2]))","            # 登録した結果を保存（コミット）する","            conn.commit()","            ","        ","        # リストをCSVに出力する","        elif 'output' in request.form:","            df = pd.read_sql_query(sql=u\"SELECT * FROM sales\", con=conn)","            df.to_csv('Python_Flask/app/static/csv/list.csv', index=False) "],"id":981}],[{"start":{"row":131,"column":0},"end":{"row":131,"column":4},"action":"remove","lines":["    "],"id":982}],[{"start":{"row":131,"column":0},"end":{"row":132,"column":0},"action":"insert","lines":["",""],"id":983},{"start":{"row":132,"column":0},"end":{"row":132,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":132,"column":1},"end":{"row":132,"column":2},"action":"insert","lines":[" "],"id":984}],[{"start":{"row":132,"column":2},"end":{"row":132,"column":6},"action":"insert","lines":["ログイン"],"id":985}],[{"start":{"row":132,"column":6},"end":{"row":132,"column":10},"action":"insert","lines":["画面処理"],"id":986}],[{"start":{"row":160,"column":4},"end":{"row":160,"column":5},"action":"remove","lines":[" "],"id":987},{"start":{"row":160,"column":0},"end":{"row":160,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":160,"column":0},"end":{"row":161,"column":0},"action":"insert","lines":["",""],"id":988},{"start":{"row":161,"column":0},"end":{"row":161,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":161,"column":1},"end":{"row":161,"column":2},"action":"insert","lines":[" "],"id":989},{"start":{"row":161,"column":2},"end":{"row":161,"column":3},"action":"insert","lines":["C"]},{"start":{"row":161,"column":3},"end":{"row":161,"column":4},"action":"insert","lines":["S"]},{"start":{"row":161,"column":4},"end":{"row":161,"column":5},"action":"insert","lines":["V"]}],[{"start":{"row":161,"column":5},"end":{"row":161,"column":6},"action":"insert","lines":[" "],"id":990}],[{"start":{"row":161,"column":5},"end":{"row":161,"column":6},"action":"remove","lines":[" "],"id":991}],[{"start":{"row":161,"column":5},"end":{"row":161,"column":6},"action":"insert","lines":["h"],"id":992},{"start":{"row":161,"column":6},"end":{"row":161,"column":7},"action":"insert","lines":["o"]},{"start":{"row":161,"column":7},"end":{"row":161,"column":8},"action":"insert","lines":["z"]},{"start":{"row":161,"column":8},"end":{"row":161,"column":9},"action":"insert","lines":["o"]}],[{"start":{"row":161,"column":8},"end":{"row":161,"column":9},"action":"remove","lines":["o"],"id":993},{"start":{"row":161,"column":7},"end":{"row":161,"column":8},"action":"remove","lines":["z"]},{"start":{"row":161,"column":6},"end":{"row":161,"column":7},"action":"remove","lines":["o"]},{"start":{"row":161,"column":5},"end":{"row":161,"column":6},"action":"remove","lines":["h"]}],[{"start":{"row":161,"column":5},"end":{"row":161,"column":6},"action":"insert","lines":["の"],"id":994}],[{"start":{"row":161,"column":5},"end":{"row":161,"column":6},"action":"remove","lines":["の"],"id":995}],[{"start":{"row":161,"column":5},"end":{"row":161,"column":6},"action":"insert","lines":["の"],"id":996}],[{"start":{"row":161,"column":6},"end":{"row":161,"column":10},"action":"insert","lines":["関連処理"],"id":997}],[{"start":{"row":161,"column":5},"end":{"row":161,"column":6},"action":"remove","lines":["の"],"id":998}],[{"start":{"row":161,"column":7},"end":{"row":161,"column":8},"action":"insert","lines":["の"],"id":999}],[{"start":{"row":188,"column":75},"end":{"row":189,"column":0},"action":"insert","lines":["",""],"id":1000},{"start":{"row":189,"column":0},"end":{"row":189,"column":12},"action":"insert","lines":["            "]},{"start":{"row":189,"column":12},"end":{"row":190,"column":0},"action":"insert","lines":["",""]},{"start":{"row":190,"column":0},"end":{"row":190,"column":12},"action":"insert","lines":["            "]},{"start":{"row":190,"column":12},"end":{"row":191,"column":0},"action":"insert","lines":["",""]},{"start":{"row":191,"column":0},"end":{"row":191,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":191,"column":8},"end":{"row":191,"column":12},"action":"remove","lines":["    "],"id":1001},{"start":{"row":191,"column":4},"end":{"row":191,"column":8},"action":"remove","lines":["    "]},{"start":{"row":191,"column":0},"end":{"row":191,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":191,"column":0},"end":{"row":193,"column":12},"action":"insert","lines":["# CSV関連の処理           ","@app.route(\"/csv\", methods=['GET', 'POST', 'PUT', 'DELETE'])","def login():"],"id":1002}],[{"start":{"row":192,"column":13},"end":{"row":192,"column":16},"action":"remove","lines":["csv"],"id":1003},{"start":{"row":192,"column":13},"end":{"row":192,"column":23},"action":"insert","lines":["users_list"]}],[{"start":{"row":44,"column":8},"end":{"row":49,"column":100},"action":"remove","lines":["# ユーザ一覧画面に遷移する","        elif 'users_list' in request.form:","            df = pd.read_sql_query(sql=u\"SELECT * FROM users\", con=conn)","            conn.close()","            table = users_list(df)","            return render_template('users_list.html', login_user=session[\"login_user\"], table=table)"],"id":1004}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":8},"action":"remove","lines":["    "],"id":1005},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"remove","lines":["    "]},{"start":{"row":43,"column":8},"end":{"row":44,"column":0},"action":"remove","lines":["",""]},{"start":{"row":43,"column":4},"end":{"row":43,"column":8},"action":"remove","lines":["    "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]},{"start":{"row":42,"column":12},"end":{"row":43,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":186,"column":12},"end":{"row":187,"column":0},"action":"insert","lines":["",""],"id":1006},{"start":{"row":187,"column":0},"end":{"row":187,"column":4},"action":"insert","lines":["    "]},{"start":{"row":187,"column":4},"end":{"row":188,"column":0},"action":"insert","lines":["",""]},{"start":{"row":188,"column":0},"end":{"row":188,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":188,"column":4},"end":{"row":193,"column":100},"action":"insert","lines":["# ユーザ一覧画面に遷移する","        elif 'users_list' in request.form:","            df = pd.read_sql_query(sql=u\"SELECT * FROM users\", con=conn)","            conn.close()","            table = users_list(df)","            return render_template('users_list.html', login_user=session[\"login_user\"], table=table)"],"id":1007}],[{"start":{"row":189,"column":9},"end":{"row":189,"column":10},"action":"remove","lines":["l"],"id":1008},{"start":{"row":189,"column":8},"end":{"row":189,"column":9},"action":"remove","lines":["e"]}],[{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"remove","lines":["l"],"id":1009},{"start":{"row":46,"column":8},"end":{"row":46,"column":9},"action":"remove","lines":["e"]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":5},"action":"remove","lines":[" "],"id":1010},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"remove","lines":["    "]},{"start":{"row":43,"column":16},"end":{"row":44,"column":11},"action":"remove","lines":["","           "]},{"start":{"row":43,"column":12},"end":{"row":43,"column":16},"action":"remove","lines":["    "]},{"start":{"row":43,"column":8},"end":{"row":43,"column":12},"action":"remove","lines":["    "]},{"start":{"row":43,"column":4},"end":{"row":43,"column":8},"action":"remove","lines":["    "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":42,"column":12},"end":{"row":43,"column":0},"action":"remove","lines":["",""],"id":1011}],[{"start":{"row":184,"column":4},"end":{"row":184,"column":9},"action":"remove","lines":["login"],"id":1012},{"start":{"row":184,"column":4},"end":{"row":184,"column":9},"action":"insert","lines":["login"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":9},"action":"remove","lines":["login"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":5},"action":"insert","lines":["c"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":5},"action":"remove","lines":["c"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":6},"action":"insert","lines":["cs"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":6},"action":"remove","lines":["cs"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":7},"action":"insert","lines":["csv"]}],[{"start":{"row":154,"column":4},"end":{"row":154,"column":9},"action":"remove","lines":["login"],"id":1013},{"start":{"row":154,"column":4},"end":{"row":154,"column":9},"action":"insert","lines":["login"]},{"start":{"row":154,"column":4},"end":{"row":154,"column":9},"action":"remove","lines":["login"]},{"start":{"row":154,"column":4},"end":{"row":154,"column":5},"action":"insert","lines":["c"]},{"start":{"row":154,"column":4},"end":{"row":154,"column":5},"action":"remove","lines":["c"]},{"start":{"row":154,"column":4},"end":{"row":154,"column":6},"action":"insert","lines":["cs"]},{"start":{"row":154,"column":4},"end":{"row":154,"column":6},"action":"remove","lines":["cs"]},{"start":{"row":154,"column":4},"end":{"row":154,"column":7},"action":"insert","lines":["csv"]}],[{"start":{"row":184,"column":4},"end":{"row":184,"column":7},"action":"remove","lines":["csv"],"id":1014},{"start":{"row":184,"column":4},"end":{"row":184,"column":7},"action":"insert","lines":["csv"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":7},"action":"remove","lines":["csv"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":5},"action":"insert","lines":["う"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":5},"action":"remove","lines":["う"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":6},"action":"insert","lines":["うs"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":6},"action":"remove","lines":["うs"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":6},"action":"insert","lines":["うせ"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":6},"action":"remove","lines":["うせ"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":7},"action":"insert","lines":["うせr"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":7},"action":"remove","lines":["うせr"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":6},"action":"insert","lines":["うせ"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":6},"action":"remove","lines":["うせ"]},{"start":{"row":184,"column":4},"end":{"row":184,"column":5},"action":"insert","lines":["う"]}],[{"start":{"row":184,"column":4},"end":{"row":184,"column":5},"action":"remove","lines":["う"],"id":1015}],[{"start":{"row":184,"column":4},"end":{"row":184,"column":5},"action":"insert","lines":["u"],"id":1016},{"start":{"row":184,"column":5},"end":{"row":184,"column":6},"action":"insert","lines":["s"]},{"start":{"row":184,"column":6},"end":{"row":184,"column":7},"action":"insert","lines":["e"]},{"start":{"row":184,"column":7},"end":{"row":184,"column":8},"action":"insert","lines":["r"]},{"start":{"row":184,"column":8},"end":{"row":184,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":184,"column":8},"end":{"row":184,"column":9},"action":"remove","lines":["r"],"id":1017}],[{"start":{"row":184,"column":8},"end":{"row":184,"column":9},"action":"insert","lines":["_"],"id":1018},{"start":{"row":184,"column":9},"end":{"row":184,"column":10},"action":"insert","lines":["s"]}],[{"start":{"row":184,"column":9},"end":{"row":184,"column":10},"action":"remove","lines":["s"],"id":1019},{"start":{"row":184,"column":8},"end":{"row":184,"column":9},"action":"remove","lines":["_"]}],[{"start":{"row":184,"column":8},"end":{"row":184,"column":9},"action":"insert","lines":["s"],"id":1020},{"start":{"row":184,"column":9},"end":{"row":184,"column":10},"action":"insert","lines":["_"]},{"start":{"row":184,"column":10},"end":{"row":184,"column":11},"action":"insert","lines":["l"]},{"start":{"row":184,"column":11},"end":{"row":184,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":184,"column":11},"end":{"row":184,"column":12},"action":"remove","lines":["s"],"id":1021}],[{"start":{"row":184,"column":11},"end":{"row":184,"column":12},"action":"insert","lines":["i"],"id":1022},{"start":{"row":184,"column":12},"end":{"row":184,"column":13},"action":"insert","lines":["s"]},{"start":{"row":184,"column":13},"end":{"row":184,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":184,"column":17},"end":{"row":185,"column":0},"action":"insert","lines":["",""],"id":1023},{"start":{"row":185,"column":0},"end":{"row":185,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":185,"column":4},"end":{"row":189,"column":32},"action":"insert","lines":["print(request.method)","    # データベースに接続する","    conn = sqlite3.connect('Python_Flask/models/sales.db')","    c = conn.cursor()","    if request.method == 'POST':"],"id":1024}],[{"start":{"row":182,"column":9},"end":{"row":182,"column":10},"action":"remove","lines":["理"],"id":1025},{"start":{"row":182,"column":8},"end":{"row":182,"column":9},"action":"remove","lines":["処"]},{"start":{"row":182,"column":7},"end":{"row":182,"column":8},"action":"remove","lines":["の"]},{"start":{"row":182,"column":6},"end":{"row":182,"column":7},"action":"remove","lines":["連"]},{"start":{"row":182,"column":5},"end":{"row":182,"column":6},"action":"remove","lines":["関"]},{"start":{"row":182,"column":4},"end":{"row":182,"column":5},"action":"remove","lines":["V"]},{"start":{"row":182,"column":3},"end":{"row":182,"column":4},"action":"remove","lines":["S"]},{"start":{"row":182,"column":2},"end":{"row":182,"column":3},"action":"remove","lines":["C"]}],[{"start":{"row":182,"column":2},"end":{"row":182,"column":10},"action":"insert","lines":["ユーザー一覧画面"],"id":1026}],[{"start":{"row":182,"column":10},"end":{"row":182,"column":12},"action":"insert","lines":["への"],"id":1027},{"start":{"row":182,"column":12},"end":{"row":182,"column":14},"action":"insert","lines":["遷移"]}],[{"start":{"row":182,"column":5},"end":{"row":182,"column":6},"action":"remove","lines":["ー"],"id":1028}],[{"start":{"row":192,"column":0},"end":{"row":192,"column":40},"action":"remove","lines":["        if 'users_list' in request.form:"],"id":1029},{"start":{"row":191,"column":18},"end":{"row":192,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":192,"column":8},"end":{"row":192,"column":12},"action":"remove","lines":["    "],"id":1030}],[{"start":{"row":193,"column":8},"end":{"row":193,"column":12},"action":"remove","lines":["    "],"id":1031}],[{"start":{"row":194,"column":8},"end":{"row":194,"column":12},"action":"remove","lines":["    "],"id":1032}],[{"start":{"row":195,"column":8},"end":{"row":195,"column":12},"action":"remove","lines":["    "],"id":1033}],[{"start":{"row":190,"column":0},"end":{"row":190,"column":4},"action":"remove","lines":["    "],"id":1034},{"start":{"row":189,"column":32},"end":{"row":190,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":185,"column":0},"end":{"row":185,"column":25},"action":"remove","lines":["    print(request.method)"],"id":1035},{"start":{"row":184,"column":17},"end":{"row":185,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":187,"column":0},"end":{"row":187,"column":21},"action":"remove","lines":["    c = conn.cursor()"],"id":1036},{"start":{"row":186,"column":58},"end":{"row":187,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":187,"column":0},"end":{"row":187,"column":32},"action":"remove","lines":["    if request.method == 'POST':"],"id":1037},{"start":{"row":186,"column":58},"end":{"row":187,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":187,"column":4},"end":{"row":187,"column":18},"action":"remove","lines":["# ユーザ一覧画面に遷移する"],"id":1038}],[{"start":{"row":190,"column":30},"end":{"row":191,"column":0},"action":"insert","lines":["",""],"id":1039},{"start":{"row":191,"column":0},"end":{"row":191,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":191,"column":8},"end":{"row":191,"column":22},"action":"insert","lines":["# ユーザ一覧画面に遷移する"],"id":1040}],[{"start":{"row":187,"column":0},"end":{"row":187,"column":4},"action":"remove","lines":["    "],"id":1041},{"start":{"row":186,"column":58},"end":{"row":187,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":187,"column":4},"end":{"row":187,"column":8},"action":"remove","lines":["    "],"id":1042}],[{"start":{"row":188,"column":4},"end":{"row":188,"column":8},"action":"remove","lines":["    "],"id":1043}],[{"start":{"row":189,"column":4},"end":{"row":189,"column":8},"action":"remove","lines":["    "],"id":1044}],[{"start":{"row":190,"column":4},"end":{"row":190,"column":8},"action":"remove","lines":["    "],"id":1045}],[{"start":{"row":191,"column":4},"end":{"row":191,"column":8},"action":"remove","lines":["    "],"id":1046}],[{"start":{"row":189,"column":22},"end":{"row":189,"column":23},"action":"insert","lines":["_"],"id":1047}],[{"start":{"row":189,"column":22},"end":{"row":189,"column":23},"action":"remove","lines":["_"],"id":1048}],[{"start":{"row":184,"column":14},"end":{"row":184,"column":15},"action":"insert","lines":["_"],"id":1049},{"start":{"row":184,"column":15},"end":{"row":184,"column":16},"action":"insert","lines":["t"]},{"start":{"row":184,"column":16},"end":{"row":184,"column":17},"action":"insert","lines":["r"]},{"start":{"row":184,"column":17},"end":{"row":184,"column":18},"action":"insert","lines":["a"]},{"start":{"row":184,"column":18},"end":{"row":184,"column":19},"action":"insert","lines":["n"]},{"start":{"row":184,"column":19},"end":{"row":184,"column":20},"action":"insert","lines":["s"]},{"start":{"row":184,"column":20},"end":{"row":184,"column":21},"action":"insert","lines":["i"]}],[{"start":{"row":184,"column":21},"end":{"row":184,"column":22},"action":"insert","lines":["t"],"id":1050}]]},"ace":{"folds":[],"scrolltop":2291.5,"scrollleft":0,"selection":{"start":{"row":5,"column":10},"end":{"row":5,"column":10},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":142,"state":"start","mode":"ace/mode/python"}},"timestamp":1601141242083,"hash":"298877c7ba20d766450c1222ef2d311661a3403e"}