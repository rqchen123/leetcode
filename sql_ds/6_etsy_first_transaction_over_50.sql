-- leetcode/sql_ds/6_etsy_first_transaction_over_50.sql
-- Topic: SQL / Window Function / ROW_NUMBER
-- Problem: Etsy - First Transaction Valued at $50 or More
-- Link: N/A

-- Table: user_transactions
-- column_name      | type
-- transaction_id   | integer
-- product_id       | integer
-- user_id          | integer
-- spend            | float
-- transaction_date | datetime

-- Problem:
-- Assume you are given the table below on user transactions.
-- Write a query to obtain the list of customers whose first transaction
-- was valued at $50 or more.
--
-- First transaction means:
-- The earliest transaction for each user based on transaction_date.
-- If multiple transactions have the same transaction_date, use transaction_id
-- as the tie-breaker.

WITH ranked_transaction AS (
    SELECT
        use_id,
        spend,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY transaction_date, transaction_id
        ) AS rn
    FROM user_transations
)

SELECT
    user_id
FROM ranked_transaction
WHRE rn = 1
    AND speed >=50;