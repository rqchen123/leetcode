-- leetcode/sql_ds/2_ebay_customers.sql
-- Topic: SQL / GROUP BY / HAVING
-- Problem: eBay - Top 10 Customers by Number of Products
-- Link: N/A

-- Problem:
-- Assume that you are given the table below containing information
-- on various orders made by customers.
-- Write a query to obtain the ten customers who have ordered the
-- highest number of products among those customers who have spent
-- at least $1000 total.

-- Table: user_transactions
-- transaction_id integer
-- product_id     integer
-- user_id        integer
-- spend          float
-- trans_date     datetime

-- Note:
-- The problem says "customer names", but this table only has user_id.
-- So with the given table, we can return user_id.
-- To return customer names, we would need another customer/user table
-- that contains the customer name.

-- Example:
-- Input: user_transactions
-- transaction_id | product_id | user_id | spend  | trans_date
-- 1              | 101        | 1       | 400.00 | 2022-01-01
-- 2              | 102        | 1       | 350.00 | 2022-01-03
-- 3              | 103        | 1       | 300.00 | 2022-01-05
-- 4              | 201        | 2       | 700.00 | 2022-01-02
-- 5              | 202        | 2       | 200.00 | 2022-01-04
-- 6              | 301        | 3       | 600.00 | 2022-01-02
-- 7              | 302        | 3       | 500.00 | 2022-01-06
-- 8              | 303        | 3       | 100.00 | 2022-01-07
--
-- Output:
-- user_id | product_count
-- 1       | 3
-- 3       | 3
--
-- Explanation:
-- user 1 spent 1050 total and ordered 3 products
-- user 2 spent only 900 total, so user 2 is excluded
-- user 3 spent 1200 total and ordered 3 products

SELECT
    user_id,
    COUNT(product_id) AS product_count
FROM user_transactions
GROUP BY user_id
HAVING SUM(spend) >= 1000
ORDER BY product_count DESC
LIMIT 10;
