# Day07 Pandas集計（GROUP BY・merge・HAVING）

**学習日**：2026-07-05

## 学習目標

- PandasでGROUP BYを実装する
- SQLの集計処理をPandasへ変換する
- merge()によるJOINを理解する
- agg()を利用した集計を習得する
- HAVINGをquery()で実装する

---

# 1. PostgreSQLからデータ取得

```python
import pandas as pd
from db.connection import get_connection

conn = get_connection()

sql_emp = """
SELECT *
FROM employees
"""

sql_sales = """
SELECT *
FROM sales
"""

df_emp = pd.read_sql(sql_emp, conn)
df_sales = pd.read_sql(sql_sales, conn)

conn.close()
```

### 学んだこと

- employeesとsalesを別々のDataFrameとして取得する
- DataFrame作成後は接続を閉じても問題ない

---

# 2. INNER JOIN（merge）

SQL

```sql
SELECT *
FROM employees e
INNER JOIN sales s
ON e.employee_id = s.employee_id;
```

Pandas

```python
df_employee_sales = pd.merge(
    df_emp,
    df_sales,
    on="employee_id",
    how="inner"
)

print(df_employee_sales)
```

### 学んだこと

- SQLのJOINはPandasではmerge()を利用する
- INNER JOINはhow="inner"

---

# 3. GROUP BY

SQL

```sql
SELECT
    department,
    SUM(amount)
FROM employees e
JOIN sales s
ON e.employee_id = s.employee_id
GROUP BY department;
```

Pandas

```python
df_department_sales = (
    pd.merge(
        df_emp,
        df_sales,
        on="employee_id",
        how="inner"
    )
    .groupby("department")
    .agg(
        total_amount=("amount", "sum")
    )
)

print(df_department_sales)
```

### 学んだこと

- groupby()でグループ化する
- agg()で集計を行う
- Named Aggregationで列名を自由に設定できる

---

# 4. 複数集計

SQL

```sql
SELECT
    department,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM employees e
JOIN sales s
ON e.employee_id = s.employee_id
GROUP BY department;
```

Pandas

```python
df_department_summary = (
    pd.merge(
        df_emp,
        df_sales,
        on="employee_id",
        how="inner"
    )
    .groupby("department")
    .agg(
        total_amount=("amount", "sum"),
        avg_amount=("amount", "mean")
    )
)

print(df_department_summary)
```

### 学んだこと

SQLとPandasの集計関数

| SQL | Pandas |
|------|---------|
| SUM | sum |
| AVG | mean |
| COUNT | count |
| MAX | max |
| MIN | min |

---

# 5. ORDER BY

SQL

```sql
SELECT
    department,
    SUM(amount) AS total_amount
FROM employees e
JOIN sales s
ON e.employee_id = s.employee_id
GROUP BY department
ORDER BY total_amount DESC;
```

Pandas

```python
df_department_summary = (
    pd.merge(
        df_emp,
        df_sales,
        on="employee_id",
        how="inner"
    )
    .groupby("department")
    .agg(
        total_amount=("amount", "sum")
    )
    .sort_values(
        by="total_amount",
        ascending=False
    )
)

print(df_department_summary)
```

### 学んだこと

- sort_values()はORDER BYに相当する
- ascending=Falseで降順

---

# 6. HAVING

SQL

```sql
SELECT
    department,
    SUM(amount) AS total_amount
FROM employees e
JOIN sales s
ON e.employee_id = s.employee_id
GROUP BY department
HAVING SUM(amount) >= 300000;
```

Pandas

```python
df_department_summary = (
    pd.merge(
        df_emp,
        df_sales,
        on="employee_id",
        how="inner"
    )
    .groupby("department")
    .agg(
        total_amount=("amount", "sum")
    )
    .query(
        "total_amount >= 300000"
    )
)

print(df_department_summary)
```

### 学んだこと

- query()はDataFrameに対する条件抽出
- GROUP BY後に利用するとHAVINGと同じ役割になる

---

# 7. SQLとPandas対応表

| SQL | Pandas |
|------|---------|
| JOIN | merge() |
| GROUP BY | groupby() |
| SUM | sum() |
| AVG | mean() |
| COUNT | count() |
| MAX | max() |
| MIN | min() |
| HAVING | query() |
| ORDER BY | sort_values() |

---

# 8. 本日の成果

```
employees
        │
sales
        │
        ▼
merge()
        │
        ▼
groupby()
        │
        ▼
agg()
        │
        ▼
query()
        │
        ▼
sort_values()
        │
        ▼
集計結果
```

SQLで実装していた集計処理を、Pandasでも同じ考え方で実装できるようになった。

---

# 9. 気付き・設計改善

今回の学習では、SQLをそのままPandasへ変換する考え方を身につけた。

また、変数名は略称よりも意味が分かる名前の方が可読性が高いことを学んだ。

例

```python
df_employee_sales
df_department_summary
df_result
```

---

# 10. 今後改善予定

- reset_index()
- merge()（left・right・outer）
- fillna()
- dropna()
- CSV出力（to_csv）
- ETLパイプライン作成

---

# Day07まとめ

Day07では、Pandasのmerge()・groupby()・agg()・query()・sort_values()を学習し、SQLのJOIN・GROUP BY・集計・HAVING・ORDER BYをPandasで実装した。

また、SQLをPandasへ変換する考え方を理解し、データ集計処理を実務に近い形で実装できるようになった。

これにより、ETL処理に必要となるTransform工程の基本操作を習得することができた。