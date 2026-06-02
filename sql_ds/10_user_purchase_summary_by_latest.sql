"""
Problem: User Purchase Summary by Latest Transaction Date

You are given a table named user_transactions.

The table contains transaction records from users.
Each row represents one product purchased in a transaction.

Table: user_transactions

Columns:
- transaction_id: ID of the transaction
- product_id: ID of the product
- user_id: ID of the user/customer
- spend: amount of money spent in this transaction
- transaction_date: date and time of the transaction

Task:
Bucket users based on their latest transaction date.

For each latest transaction_date, return:
1. the number of users whose latest transaction happened on that date
2. the total number of products bought on that latest transaction date

Meaning:
1. First, find each user's latest transaction_date.
2. Keep only the rows from each user's latest transaction_date.
3. Group by transaction_date.
4. Count distinct users.
5. Count total products bought.

Expected output columns could be:
- transaction_date
- user_count
- product_count

Important:
"Latest transaction date" means the most recent transaction_date for each user.
A user can start with many transaction records, but we only care about their latest transaction date.
"""

WITH latest_transactions AS (
    SELECT
        transaction_id,
        product_id,
        user_id,
        spend,
        transaction_date,
        RANK() OVER (
            PARTITION BY user_id
            ORDER BY transaction_date DESC
        ) AS transaction_rank
    FROM user_transactions
)

SELECT
    transaction_date,
    COUNT(DISTINCT user_id) AS user_count,
    COUNT(product_id) AS product_count
FROM latest_transactions
WHERE transaction_rank = 1
GROUP BY transaction_date
ORDER BY transaction_date;