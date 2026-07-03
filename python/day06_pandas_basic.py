import pandas as pd
from db.connection import get_connection

# PostgreSQLへ接続
conn = get_connection()

# データ取得
sql = """
SELECT *
FROM employees
"""

df = pd.read_sql(sql, conn)

# 接続終了
conn.close()

# -----------------------------------
# WHERE
# -----------------------------------

df_sales = df[df["department"] == "営業"]

# -----------------------------------
# SELECT
# -----------------------------------

df_sales_names = df_sales[
    ["employee_name", "department"]
]

# -----------------------------------
# ORDER BY
# -----------------------------------

df_sales_sorted = df_sales.sort_values(
    "employee_name"
)

# -----------------------------------
# LIMIT
# -----------------------------------

df_top3 = df.sort_values(
    "employee_name"
).head(3)

print(df_top3)
