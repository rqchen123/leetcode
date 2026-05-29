-- leetcode/sql_ds/5_linkedin_duplicate_job_listings.sql
-- Topic: SQL / Aggregation / GROUP BY / HAVING
-- Problem: LinkedIn - Duplicate Job Listings
-- Link: N/A

-- Table: job_listings
-- column_name | type
-- job_id      | integer
-- company_id  | integer
-- title       | string
-- description | string
-- post_date   | datetime

-- Problem:
-- Assume you are given the table below that shows the job postings
-- for all companies on the platform.
-- Write a query to get the total number of companies that have posted
-- duplicate job listings.
--
-- Duplicate means:
-- Two or more jobs at the same company with the same title and description.

SELECT
    COUNT(DISTINCT company_id) AS duplicate_companies
FROM (
    SELECT
        company_id,
        title,
        description
    FROM job_listings
    GROUP BY
        company_id, title, description
    HAVING COUNT(*) >= 2
     ) T; 