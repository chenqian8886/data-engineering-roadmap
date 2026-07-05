import pandas as pd
from db.connection import get_connection

# PostgreSQLへ接続
conn = get_connection()
sql_emp = "select * from employees"
sql2_sales = "select * from sales"
df_emp = pd.read_sql(sql_emp, conn)
df_sales = pd.read_sql(sql2_sales, conn)
conn.close()

'''print(df_emp)
print(df_sales)
'''
'''SELECT department,
       SUM(amount)
FROM employees e
JOIN sales s
ON e.employee_id = s.employee_id
GROUP BY department;'''

'''df_join_emp_sales = pd.merge(df_emp, df_sales, on="employee_id", how="inner")
print(df_join_emp_sales)
df_emp_sales_groupby = df_join_emp_sales.groupby("department").agg({"amount": "sum"})
print(df_emp_sales_groupby)'''

'''SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department;'''

df_emp_count = df_emp.groupby("department").agg(employee_count = ("employee_id", "count"))
print(df_emp_count)

'''SELECT
    department,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount
FROM employees e
JOIN sales s
ON e.employee_id = s.employee_id
GROUP BY department
ORDER BY total_amount DESC;'''

df_dep_sum_avg = (
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
    .sort_values(
        by="total_amount",
        ascending=False
    )
)

print(df_dep_sum_avg)

'''SELECT
    department,
    SUM(amount) AS total_amount
FROM employees e
JOIN sales s
ON e.employee_id = s.employee_id
GROUP BY department
HAVING SUM(amount) >= 300000;'''

df_dep_sum_having = (
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
    .query("total_amount >= 300000")
)
print(df_dep_sum_having)