-- Groups in sql
-- Count the number of records for each score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
