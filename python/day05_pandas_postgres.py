import pandas as pd
from db.connection import get_connection

conn = get_connection()

#print("PostgreSQL Connected!")

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