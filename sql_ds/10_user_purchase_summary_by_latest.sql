"""
Problem: Twitter Users Who Do Not Follow Top 100 Topics

You are given two tables: user_topics and topic_rankings.

The user_topics table contains information about which topics each Twitter user follows.
Each row represents one user following one topic.

Table: user_topics

Columns:
- user_id: ID of the Twitter user
- topic_id: ID of the topic the user follows
- follow_date: date and time when the user followed the topic

The topic_rankings table contains the popularity ranking of each topic on each day.

Table: topic_rankings

Columns:
- topic_id: ID of the topic
- ranking: popularity rank of the topic
- ranking_date: date and time of the ranking

Task:
Find all existing users on 2021-01-01 who did not follow any topic in the top 100 most popular topics on that day.

Meaning:
1. First, find the top 100 topics on 2021-01-01.
2. Then, find all users who existed in user_topics on 2021-01-01.
3. Exclude users who followed at least one top 100 topic on 2021-01-01.
4. Return only users who followed zero top 100 topics.

Expected output column:
- user_id

Important:
"Top 100 topics" means ranking <= 100.
A user should be excluded if they followed even one topic ranked in the top 100.
Use NOT EXISTS to check that no matching top 100 topic exists for that user.
"""

WITH top_100_topics AS (
    SELECT
        topic_id
    FROM topic_rankings
    WHERE DATE(ranking_date) = '2021-01-01'
      AND ranking <= 100
)

SELECT DISTINCT
    u.user_id
FROM user_topics u
WHERE DATE(u.follow_date) = '2021-01-01'
  AND NOT EXISTS (
      SELECT 1
      FROM user_topics u2
      JOIN top_100_topics t
        ON u2.topic_id = t.topic_id
      WHERE u2.user_id = u.user_id
        AND DATE(u2.follow_date) = '2021-01-01'
  )
ORDER BY u.user_id;