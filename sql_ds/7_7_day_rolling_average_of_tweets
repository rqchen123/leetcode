-- Twitter: 7-Day Rolling Average of Tweets
--
-- Description:
-- Given a table `tweets` containing each user's tweets over time,
-- calculate the 7-day rolling average number of tweets for each user
-- for every date.
--
-- Table: tweets
--
-- +-------------+----------+
-- | column_name | type     |
-- +-------------+----------+
-- | tweet_id    | integer  |
-- | msg         | string   |
-- | user_id     | integer  |
-- | tweet_date  | datetime |
-- +-------------+----------+
--
-- Rule:
-- For each user and each date, calculate:
--
--     average tweets per day over the current date and previous 6 days
--
-- In other words:
--
--     rolling_avg = AVG(daily_tweet_count)
--                   over 7-day window
--
--
-- Important:
-- Step 1:
-- First count how many tweets each user posted on each date.
--
-- Example:
--
-- user_id | tweet_date | daily_tweet_count
-- --------+------------+------------------
-- 1       | 2024-01-01 | 2
-- 1       | 2024-01-02 | 1
-- 1       | 2024-01-03 | 3
--
--
-- Step 2:
-- Then calculate the rolling average for each user.
--
-- For date 2024-01-07:
--
-- rolling average = average tweets from:
--
-- 2024-01-01
-- 2024-01-02
-- 2024-01-03
-- 2024-01-04
-- 2024-01-05
-- 2024-01-06
-- 2024-01-07
--
--
-- Partition logic:
-- Each user should be calculated separately.
--
-- So user 1's tweets should not mix with user 2's tweets.
--
--
-- Window logic:
--
-- PARTITION BY user_id
-- ORDER BY tweet_date
-- Use current date and previous 6 days
--
--
-- Expected output:
--
-- user_id | tweet_date | rolling_avg_7d
-- --------+------------+---------------
-- 1       | 2024-01-01 | ...
-- 1       | 2024-01-02 | ...
-- 1       | 2024-01-03 | ...

WITH daily_tweets AS (
    SELECT
        user_id,
        CAST(tweet_date AS DATE) AS tweet_day,
        COUNT(tweet_id) AS tweet_count
    FROM tweets
    GROUP BY
        user_id,
        CAST(tweet_date AS DATE)
)

SELECT
    user_id,
    tweet_day,
    tweet_count,
    ROUND(
        AVG(tweet_count) OVER (
        PARTITION BY user_id
        ORDER BY tweet_day
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ),
        2
        ) AS rolling_avg_7d
    FROM daily_tweets
    ORDER BY
        user_id,
        tweet_day;