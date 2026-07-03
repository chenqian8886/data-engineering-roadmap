# Day06 Pandas基礎（SELECT・WHERE・ORDER BY・LIMIT）

**学習日**：2026-07-03

## 学習目標

- PandasでDataFrameを操作する
- SQLとPandasの対応関係を理解する
- SELECT・WHERE・ORDER BY・LIMITをPandasで実装する
- pd.read_sql()でPostgreSQLのデータをDataFrameへ読み込む
- PandasとETLの関係を理解する

---

# 1. PostgreSQLからDataFrameを作成

```python
import pandas as pd
from db.connection import get_connection

conn = get_connection()

sql = """
SELECT *
FROM employees
"""

df = pd.read_sql(sql, conn)

conn.close()
```

### 学んだこと

- pd.read_sql()を使うとSQLの実行結果をDataFrameへ格納できる
- DataFrame作成後は、PostgreSQLとの接続を閉じても操作できる
- conn.close()はデータ取得後に実行する

---

# 2. SELECT *

SQL

```sql
SELECT *
FROM employees;
```

Pandas

```python
print(df)
```

### 学んだこと

- DataFrame全体を表示する場合はprint(df)を使用する
- Jupyter Notebookではdfだけでも表示できるが、Pythonファイルではprint(df)が必要

---

# 3. SELECT 1列

SQL

```sql
SELECT employee_name
FROM employees;
```

Pandas

```python
print(df["employee_name"])
```

### 学んだこと

- df["列名"]で1列を取得できる
- 1列だけ取得した場合はSeriesになる

---

# 4. SELECT 複数列

SQL

```sql
SELECT employee_name, department
FROM employees;
```

Pandas

```python
print(df[["employee_name", "department"]])
```

### 学んだこと

- 複数列を取得する場合は列名をリストで指定する
- df[["列1", "列2"]] のように角括弧が二重になる
- 複数列を取得した場合はDataFrameになる

---

# 5. WHERE

SQL

```sql
SELECT *
FROM employees
WHERE department = '営業';
```

Pandas

```python
df_sales = df[df["department"] == "営業"]
print(df_sales)
```

### 学んだこと

- df["department"] == "営業" はTrue / Falseを返す
- PandasではTrueの行だけが抽出される
- WHERE句はBoolean条件で表現する

---

# 6. WHERE + SELECT

SQL

```sql
SELECT employee_name, department
FROM employees
WHERE department = '営業';
```

Pandas

```python
df_sales = df[df["department"] == "営業"]

df_sales_names = df_sales[
    ["employee_name", "department"]
]

print(df_sales_names)
```

### 学んだこと

- 先にWHEREで絞り込み、その後に必要な列を取得すると読みやすい
- 処理ごとにDataFrameを分けると、可読性と保守性が高まる

---

# 7. ORDER BY

SQL

```sql
SELECT *
FROM employees
WHERE department = '営業'
ORDER BY employee_name;
```

Pandas

```python
df_sales = df[df["department"] == "営業"]

df_sales_sorted = df_sales.sort_values("employee_name")

print(df_sales_sorted)
```

### 学んだこと

- sort_values()で並び替えができる
- デフォルトは昇順
- 降順にしたい場合は ascending=False を指定する

```python
df.sort_values("employee_name", ascending=False)
```

---

# 8. LIMIT

SQL

```sql
SELECT *
FROM employees
ORDER BY employee_name
LIMIT 3;
```

Pandas

```python
df_top3 = df.sort_values("employee_name").head(3)

print(df_top3)
```

### 学んだこと

- head()で先頭行を取得できる
- head(3)はSQLのLIMIT 3に相当する

---

# 9. SQLとPandas対応表

| SQL | Pandas |
|----|----|
| SELECT * | print(df) |
| SELECT column | df["column"] |
| SELECT column1, column2 | df[["column1", "column2"]] |
| WHERE | df[df["column"] == value] |
| ORDER BY | sort_values() |
| LIMIT | head() |

---

# 10. Day06完成コード

```python
import pandas as pd
from db.connection import get_connection

conn = get_connection()

sql = """
SELECT *
FROM employees
"""

df = pd.read_sql(sql, conn)

conn.close()

# WHERE
df_sales = df[df["department"] == "営業"]

# WHERE + SELECT
df_sales_names = df_sales[
    ["employee_name", "department"]
]

# ORDER BY
df_sales_sorted = df_sales.sort_values("employee_name")

# LIMIT
df_top3 = df.sort_values("employee_name").head(3)

print(df_top3)
```

---

# 11. 本日の成果

```
PostgreSQL
      │
      ▼
connection.py
      │
      ▼
psycopg
      │
      ▼
pd.read_sql()
      │
      ▼
DataFrame
      │
      ▼
SELECT / WHERE / ORDER BY / LIMIT
```

PostgreSQLから取得したデータをPandasのDataFrameとして扱い、SQLと同じ考え方でデータ抽出・並び替え・件数制限ができるようになった。

---

# 12. PandasとETLの関係

ETLとは以下の3つの処理を指す。

- Extract：抽出
- Transform：変換・加工
- Load：保存

今回学習したPandasは、主にTransformを担当する。

```
Extract
PostgreSQL
      │
      ▼
pd.read_sql()

Transform
DataFrame
      │
      ▼
WHERE / SELECT / ORDER BY / GROUP BY / JOIN

Load
CSV / Excel / Database
```

### 学んだこと

- psycopgはPostgreSQLと通信するためのライブラリ
- Pandasはデータ加工・分析を行うライブラリ
- DataFrameはPandasで扱う表形式データ
- PandasはETL処理のTransformで重要な役割を持つ

---

# 13. 気付き・設計改善

今回の学習では、SQLとPandasの対応関係を意識して学習した。

SQLのSELECT、WHERE、ORDER BY、LIMITは、Pandasでも同じ考え方で実装できる。

また、変数名は処理名ではなく、データの意味が分かる名前にした方が読みやすい。

例：

```python
df_sales
df_sales_sorted
df_top3
df_result
```

---

# 14. 今後改善予定

- groupby()でGROUP BYを実装する
- merge()でJOINを実装する
- employee.pyにデータ取得処理を分離する
- ETL処理としてExtract・Transform・Loadを整理する
- CSV出力やDB書き戻しを実装する

---

# Day06まとめ

Day06では、PostgreSQLから取得したデータをPandas DataFrameとして扱い、SQLのSELECT、WHERE、ORDER BY、LIMITに相当する処理をPandasで実装した。

また、psycopg、Pandas、DataFrameの役割を整理し、PandasがETLのTransformにあたる重要なライブラリであることを理解した。

SQLの考え方を土台にしてPandasを学ぶことで、データ抽出・加工の流れをより実務に近い形で理解できた。