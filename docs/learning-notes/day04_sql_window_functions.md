# Day04 SQL Window Functions

**学習日**：2026-07-01

## 本日の目標

- Window関数の考え方を理解する
- ROW_NUMBER・RANK・DENSE_RANKの違いを理解する
- PARTITION BYの使い方を理解する
- LAG・LEADを利用した時系列分析を学ぶ
- WITH（CTE）の使い方を理解する

---

# 学習内容

## 1. Window関数

### OVER()

Window関数を実行する範囲（Window）を指定する。

```sql
RANK() OVER(ORDER BY total_amount DESC)
```

---

## 2. ROW_NUMBER()

特徴

- 重複しない連番を付与する

使用例

```sql
ROW_NUMBER() OVER(ORDER BY total_amount DESC)
```

---

## 3. RANK()

特徴

- 同順位を認める
- 次の順位は飛ぶ

```text
1
2
2
4
```

使用例

```sql
RANK() OVER(ORDER BY total_amount DESC)
```

---

## 4. DENSE_RANK()

特徴

- 同順位を認める
- 順位は飛ばない

```text
1
2
2
3
```

---

## 5. PARTITION BY

部署ごとにランキングを作成する。

```sql
RANK() OVER(
    PARTITION BY department
    ORDER BY total_amount DESC
)
```

---

## 6. LAG()

前の行の値を取得する。

```sql
LAG(total_amount)
OVER(ORDER BY sales_month)
```

利用例

- 前月売上
- 前月比
- 前日との差額

---

## 7. LEAD()

次の行の値を取得する。

```sql
LEAD(total_amount)
OVER(ORDER BY sales_month)
```

利用例

- 次月売上
- 次月との差額

---

## 8. WITH（CTE）

SQLを読みやすくするため、一時的な結果セットを作成する。

```sql
WITH monthly_sales AS (

    SELECT
        DATE_TRUNC('month', sale_date) AS sales_month,
        SUM(amount) AS total_amount

    FROM sales

    GROUP BY DATE_TRUNC('month', sale_date)

)

SELECT *
FROM monthly_sales;
```

---

# 実践SQL

## 部署別売上ランキング

```sql
SELECT
    department,
    employee_name,
    SUM(amount) AS total_amount,
    RANK() OVER(
        PARTITION BY department
        ORDER BY SUM(amount) DESC
    ) AS ranking
FROM employees
JOIN sales USING(employee_id)
GROUP BY
    department,
    employee_name;
```

---

## 前月比分析

```sql
WITH monthly_sales AS (

    SELECT
        DATE_TRUNC('month', sale_date) AS sales_month,
        SUM(amount) AS total_amount

    FROM sales

    GROUP BY DATE_TRUNC('month', sale_date)

)

SELECT
    sales_month,
    total_amount,
    LAG(total_amount)
        OVER(ORDER BY sales_month) AS previous_amount,
    total_amount
        - LAG(total_amount)
        OVER(ORDER BY sales_month) AS diff

FROM monthly_sales;
```

---

## 次月比分析

```sql
WITH monthly_sales AS (

    SELECT
        DATE_TRUNC('month', sale_date) AS sales_month,
        SUM(amount) AS total_amount

    FROM sales

    GROUP BY DATE_TRUNC('month', sale_date)

)

SELECT
    sales_month,
    total_amount,
    LEAD(total_amount)
        OVER(ORDER BY sales_month) AS next_amount,
    LEAD(total_amount)
        OVER(ORDER BY sales_month)
        - total_amount AS diff

FROM monthly_sales;
```

---

# 本日のまとめ

- Window関数は各行の情報を保持したまま分析できる。
- OVER()はWindow関数の計算範囲を指定する。
- PARTITION BYはグループごとにWindow関数を適用する。
- ROW_NUMBER・RANK・DENSE_RANKはランキング分析で使用する。
- LAG・LEADは時系列分析で非常によく利用される。
- WITH（CTE）はSQLの可読性と保守性を向上させる。

---

# 感想

Window関数は最初は難しく感じたが、GROUP BYとの違いやOVER()・PARTITION BYの役割を理解できたことで、ランキング分析や前月比分析の書き方が分かった。WITH句を組み合わせることで、複雑なSQLでも読みやすく記述できることを学んだ。