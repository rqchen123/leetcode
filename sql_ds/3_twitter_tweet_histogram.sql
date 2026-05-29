-- leetcode/sql_ds/3_twitter_tweet_histogram.sql
-- Topic: SQL / Aggregation / CTE
-- Problem: Twitter - Histogram of Tweets
-- Link: N/A

-- Table: tweets
-- column_name | type
-- tweet_id    | integer
-- user_id     | integer
-- msg         | string
-- tweet_date  | datetime

-- Problem:
-- Assume you are given the table below containing information on tweets.
-- Write a query to obtain a histogram of tweets posted per user in 2020:
-- the number of users per the number of tweets in 2020.

-- Example:
-- Suppose in 2020:
-- user 1 posted 2 tweets
-- user 2 posted 2 tweets
-- user 3 posted 1 tweet
--
-- Then the output should be:
-- tweet_bucket | users_num
-- 1            | 1
-- 2            | 2

WITH user_tweet_counts AS (
    SELECT
        user_id,
        COUNT(*) AS tweet_bucket
    FROM tweets
    WHERE tweet_date >= "2020-01-01"
        AND tweet_date < "2021-01-01"
    GROUP BY user_id
)

SELECT
    tweet_bucket,
    COUNT(*) AS users_num
FROM user_tweet_counts
GROUP BY tweet_bucket
ORDER BY tweet_bucet