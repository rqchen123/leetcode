-- leetcode/sql_ds/1_amazon _cumulative.sql
-- Topic: SQL / Window Function
-- Problem: Amazon - Cumulative Spend by Product
-- Link: N/A

-- Problem:
-- Assume you are given the table below for spending activity by product type.
-- Write a query to calculate the cumulative spend so far by date
-- for each product over time in chronological order.

-- Table: total_trans
-- order_id   integer
-- user_id    integer
-- product_id string
-- spend      float
-- trans_date datetime

-- Example:
-- Input: total_trans
-- order_id | user_id | product_id | spend | trans_date
-- 1        | 101     | A          | 10.00 | 2022-01-01
-- 2        | 102     | A          | 20.00 | 2022-01-03
-- 3        | 103     | B          | 30.00 | 2022-01-02
-- 4        | 104     | A          | 15.00 | 2022-01-05
-- 5        | 105     | B          | 25.00 | 2022-01-04
--
-- Output:
-- trans_date | product_id | cum_spend
-- 2022-01-01 | A          | 10.00
-- 2022-01-02 | B          | 30.00
-- 2022-01-03 | A          | 30.00
-- 2022-01-04 | B          | 55.00
-- 2022-01-05 | A          | 45.00

SELECT
    trans_date,
    product_id,
    SUM(spend) OVER (
        PARTITION BY product_id
        ORDER BY trans_date
    ) AS cum_spend
FROM total_trans
ORDER BY trans_date;