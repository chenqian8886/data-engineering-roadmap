# Day05 Python・PostgreSQL・Pandas

**学習日**：2026-07-02

## 学習目標

- Python開発環境（venv）を構築する
- PythonからPostgreSQLへ接続する
- SQLをPythonから実行する
- SQL実行結果をPandas DataFrameへ変換する
- Pythonプロジェクトの基本構成を理解する

---

# 1. Python仮想環境（venv）

## 仮想環境作成

```bash
python3 -m venv .venv
```

## 仮想環境有効化

```bash
source .venv/bin/activate
```

## Python確認

```bash
which python
python --version
```

### 学んだこと

- プロジェクトごとにPython環境を分離できる
- ライブラリのバージョン競合を防げる
- 使用しているPythonを確認する習慣が重要

---

# 2. ライブラリインストール

```bash
pip install pandas "psycopg[binary]"
```

## requirements.txt作成

```bash
pip freeze > requirements.txt
```

### 学んだこと

- requirements.txtには使用ライブラリとバージョンが記録される
- 他PCでも

```bash
pip install -r requirements.txt
```

だけで同じ環境を構築できる

- macOS(zsh)では

```bash
pip install "psycopg[binary]"
```

のようにダブルクォーテーションが必要

---

# 3. PostgreSQL接続

接続に必要な情報

|項目|値|
|----|----|
|Host|localhost|
|Port|5432|
|Database|sample_db|
|User|postgres|
|Password|password|

## 接続コード

```python
import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="sample_db",
    user="postgres",
    password="password"
)

print("PostgreSQL Connected!")

conn.close()
```

### 学んだこと

- psycopgはPostgreSQL接続ライブラリ
- PostgreSQLへ接続するには5つの情報が必要
- Host・Port・Database・User・Password

---

# 4. SQL実行

```python
cur = conn.cursor()

cur.execute("SELECT * FROM employees")

rows = cur.fetchall()

cur.close()
```

### 学んだこと

## cursor()

SQLを実行するためのオブジェクトを取得する。

## execute()

SQLを実行する。

## fetchall()

SQL結果を全件取得する。

取得結果はPythonのList(Tuple)になる。

---

# 5. Pandas DataFrame生成

```python
import pandas as pd

df = pd.DataFrame(
    rows,
    columns=[
        "employee_id",
        "employee_name",
        "department"
    ]
)

print(df)
```

### 学んだこと

- DataFrameは表形式データ
- SQL結果をDataFrameへ変換できる
- DataFrameにすると集計・分析が容易になる

---

# 6. Day05完成コード

```python
import pandas as pd
import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="sample_db",
    user="postgres",
    password="password"
)

print("PostgreSQL Connected!")

cur = conn.cursor()

cur.execute("SELECT * FROM employees")

rows = cur.fetchall()

df = pd.DataFrame(
    rows,
    columns=[
        "employee_id",
        "employee_name",
        "department"
    ]
)

print(df)

cur.close()
conn.close()
```

---

# 7. 本日の成果

```
Docker
      │
      ▼
PostgreSQL
      │
      ▼
Python
      │
      ▼
psycopg
      │
      ▼
SQL実行
      │
      ▼
Pandas(DataFrame)
```

SQLとPythonを接続し、データベースから取得したデータをDataFrameとして扱えるようになった。

---

# 8. 気付き・設計改善

今回の学習では接続処理を1ファイルへ記述した。

しかし実務では、

- 可読性
- 保守性
- 再利用性

を考慮し、接続処理を別ファイルへ分離した方が望ましい。

今後は以下の構成へリファクタリングする予定。

```
python/
│
├── db/
│   ├── connection.py
│   ├── employee.py
│   └── __init__.py
│
└── day05_pandas_postgres.py
```

connection.py

- データベース接続

employee.py

- employeesテーブル操作

day05

- 全体制御

責務を分離することで可読性・保守性・再利用性を向上させる。

---

# 9. 今後改善予定

- connection.pyへ接続処理を分離
- .envによる接続情報管理
- SQLAlchemy導入
- PandasによるSQL読込
- ETLパイプライン作成

---

# Day05まとめ

Day05ではPython開発環境を構築し、PostgreSQLへ接続してSQLを実行し、その結果をPandas DataFrameへ変換する一連の流れを学習した。

また、単にプログラムを動作させるだけでなく、接続処理の共通化や責務分離など、実務で重要となる設計についても考えることができた。

SQL・Docker・Python・Pandasが一本につながり、本格的なデータエンジアリング学習の第一歩となった。