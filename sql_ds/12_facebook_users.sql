"""
Problem: Facebook Active User Retention by Month

You are given one table: user_actions.

The user_actions table contains information about actions performed by Facebook users.
Each row represents one action performed by one user.

Table: user_actions

Columns:
- user_id: ID of the Facebook user
- event_id: type of action performed, such as "sign-in", "like", or "comment"
- timestamp: date and time when the action occurred

Task:
Calculate the number of retained active users for each month.

Meaning:
1. First, identify each month in which a user performed at least one action.
2. Remove duplicate user-month combinations because a user may perform multiple actions in the same month.
3. A user is retained in the current month if the user was active in both:
   - the current month
   - the immediately previous month
4. Count the number of retained users for each current month.

Example:
If a user was active in January and February, the user is counted as retained in February.

If a user was active in January and March but not February, the user is not counted as retained in March because the activity was not in consecutive months.

Expected output columns:
- month: the current activity month
- retained_users: number of users active in both the current and previous month

Important:
A user should only be counted once per month, even if the user performed multiple actions.
The previous month must be the immediately preceding calendar month.
"""
WITH monthly_active_users AS (
   SELECT DISTINCT
       user_id,
       DATE_TRUNC('month', timestamp)::DATE AS activity_month
   FROM user_actions
   WHERE event_id IN ('sign-in', 'like', 'comment'
)
SELECT
    current_month.activity_month AS month,
    COUNT(DISTINCT current_month.user_id) AS retained_users
FROM monthly_active_users current_month
JOIN monthly_active_users previous_month
    ON current_month.user_id = previous_month.user_id
  AND previous_month.activity_month =
      current_month.activity_month - INTERVAL '1 month'
GROUP BY
    current_month.activity_month

ORDER BY
    current_month.activity_month;