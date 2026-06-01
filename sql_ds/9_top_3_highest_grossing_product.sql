"""
Problem: Top 3 Highest-Grossing Products by Category in 2020

You are given a table named product_spend.

The table contains customer spending transactions for different products.
Each row represents one transaction.

Table: product_spend

Columns:
- transaction_id: ID of the transaction
- category_id: ID of the product category
- product_id: ID of the product
- user_id: ID of the customer
- spend: amount of money spent in this transaction
- transaction_date: date and time of the transaction

Task:
Find the top 3 highest-grossing products within each category in the year 2020.

Meaning:
1. Only use transactions from year 2020.
2. For each category_id and product_id, calculate total spend:
      total_spend = SUM(spend)
3. Within each category, rank products by total_spend from highest to lowest.
4. Return only the top 3 products for each category.

Expected output columns could be:
- category_id
- product_id
- total_spend
- rank

Important:
"Highest-grossing" means the product with the highest total spend,
not just one single large transaction.
"""

WITH product_total AS (
    SELECT
        category_id,
        product_id,
        SUM(spend) AS total_spend
    FROM product_spend
    WHERE transaction_date >= '2020-01-01'
      AND transaction_date < '2021-01-01'
    GROUP BY
        category_id,
        product_id
),

ranked_products AS (
    SELECT
        category_id,
        product_id,
        total_spend,
        RANK() OVER (
            PARTITION BY category_id
            ORDER BY total_spend DESC
        ) AS product_rank
    FROM product_total
)

SELECT
    category_id,
    product_id,
    total_spend
FROM ranked_products
WHERE product_rank <= 3
ORDER BY
    category_id,
    product_rank;