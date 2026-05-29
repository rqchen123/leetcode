-- leetcode/sql_ds/4_stitch_fix_repeat_purchases.sql
-- Topic: SQL / Aggregation / CTE
-- Problem: Stitch Fix - Repeat Purchases on Multiple Days
-- Link: N/A

-- Table: purchases
-- column_name   | type
-- purchase_id   | integer
-- user_id       | integer
-- product_id    | integer
-- quantity      | integer
-- price         | float
-- purchase_time | datetime

-- Problem:
-- Assume you are given the table below containing information on user purchases.
-- Write a query to obtain the number of people who purchased at least one
-- of the same product on multiple days.

-- Example:
-- Suppose:
-- user 1 bought product 10 on 2020-01-01 and 2020-01-03
-- user 2 bought product 20 only on 2020-01-01
-- user 3 bought product 30 on 2020-02-01 and 2020-02-05
--
-- Then the output should be:
-- repeated_purchase_users
-- 2

WITH user_product_purchase_days AS (
    SELECT
        user_id,
        predict_id,
        COUNT(DISTINCT DATE(purchase_time)) AS purchase_days
    FROM purchases
    GROUP BY
        user_id,
        product_id
),

repeated_purchase_users AS (
    SELECT DISTINCT
        user_id
    FROM user_product_purchase_days
    WHEN purchae_days >= 2
)

SELECT
    COUNT(*) AS repeated_purchase_users
FROM repeated_purchase_users;